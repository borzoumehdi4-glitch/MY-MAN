"""Poll ING Think's FX, rates and commodities sections.

Only those three sections are tracked (see SECTIONS). Every card on a section page
carries its tags, title, teaser and a unix timestamp, so no JS/browser is needed.

Usage:
    python3 feed.py                # papers in those sections not yet in the store (JSON)
    python3 feed.py --all          # everything currently listed in the sections
    python3 feed.py --md           # human-readable listing
    python3 feed.py --macro        # also flag ECB/eurozone pieces from the global RSS
    python3 feed.py --text URL     # cleaned article text, for summarising
    python3 feed.py --limit 5      # cap the number of items printed

Standard library only, like store.py and build.py.
"""
import argparse
import html as htmllib
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

import store

BASE = "https://think.ing.com"
SECTIONS = {"fx": "FX", "rates": "Rates", "commodities": "Commodities"}
MARKET_TAGS = set(SECTIONS.values())
RSS_URL = BASE + "/rss/"
UA = "Mozilla/5.0 (compatible; ing-dashboard-feed/1.0)"
TIMEOUT = 30

# Only used with --macro: pieces that shape the stories but are filed under
# "Articles" rather than a market section (e.g. the monthly ECB cheat sheet).
MACRO_WORDS = ("ecb", "lagarde", "eurozone", "euro area", "france", "bund", "oat")

# Cards are sliced by anchor position rather than matched to the closing </a>,
# because the large feature cards contain nested links (category links, share menu).
CARD_RE = re.compile(
    r'<a href="(https://think\.ing\.com/(?:articles|snaps)/[^"]+/)"'
    r'[^>]*class="card[^"]*card-article[^"]*"[^>]*>'
)
CARD_WINDOW = 6000  # chars used for the final card on a page, which has no next anchor
TITLE_RE = re.compile(r'<[a-z0-9]+ class="card-title[^"]*">(.*?)</[a-z0-9]+>', re.S)
TEASER_RE = re.compile(r'<[a-z0-9]+ class="card-text[^"]*">(.*?)</[a-z0-9]+>', re.S)
DATE_RE = re.compile(r'data-date-raw="(\d+)"')
TAG_RE = re.compile(r'<span class="entry-category">\s*([^<]+?)\s*</span>')
BODY_RE = re.compile(r'class="[^"]*content_builder[^"]*"')
BLOCK_TAG_RE = re.compile(
    r"</?(?:p|div|br|li|ul|ol|h[1-6]|tr|td|table|section|article|figure|blockquote)\b[^>]*>", re.I
)
STRIP_RE = re.compile(
    r"<(script|style|nav|header|footer|svg|noscript)\b[^>]*>.*?</\1>", re.S | re.I)
TAIL_MARKERS = ("In this article", "Topics in this article", "Disclaimer", "Content disclaimer")


def fetch(url):
    """Return the body of url as text."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, "replace")


def clean(fragment):
    """Strip tags/entities and collapse whitespace."""
    text = BLOCK_TAG_RE.sub(" ", fragment)  # block tags separate words
    text = re.sub(r"<[^>]+>", "", text)  # inline tags (b, em, span, a) vanish
    text = htmllib.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return re.sub(r"\s+([.,;:!?])", r"\1", text).strip()


def normalise(url):
    """Canonical form for comparing a URL with the store."""
    return url.split("?")[0].split("#")[0].rstrip("/") + "/"


def parse_cards(markup, section):
    """Extract the article cards from one market section page."""
    items = []
    anchors = list(CARD_RE.finditer(markup))
    for i, anchor in enumerate(anchors):
        end = anchors[i + 1].start() if i + 1 < len(anchors) else anchor.end() + CARD_WINDOW
        block = markup[anchor.end():end]
        stamp = DATE_RE.search(block)
        title = TITLE_RE.search(block)
        teaser = TEASER_RE.search(block)
        items.append(
            {
                "url": normalise(anchor.group(1)),
                "title": clean(title.group(1)) if title else "",
                "teaser": clean(teaser.group(1)) if teaser else "",
                "tags": [t.strip() for t in TAG_RE.findall(block)],
                "sections": [section],
                "kind": "snap" if "/snaps/" in anchor.group(1) else "article",
                "date": datetime.fromtimestamp(int(stamp.group(1)), timezone.utc).date().isoformat()
                if stamp
                else None,
            }
        )
    return items



ENTITY_RE = re.compile(r"&([a-zA-Z][a-zA-Z0-9]*);")
XML_ENTITIES = {"amp", "lt", "gt", "quot", "apos"}


def _xml_safe(markup):
    """Decode HTML-only entities (&rsquo; etc.) that ElementTree rejects as invalid XML."""
    return ENTITY_RE.sub(
        lambda m: m.group(0) if m.group(1) in XML_ENTITIES else htmllib.unescape(m.group(0)),
        markup,
    )


def parse_rss(markup, words=MACRO_WORDS):
    """Global RSS items whose title/teaser mention an ECB/eurozone keyword."""
    items = []
    for node in ET.fromstring(_xml_safe(markup)).findall(".//item"):
        title = (node.findtext("title") or "").strip()
        desc = (node.findtext("description") or "").strip()
        if not any(w in (title + " " + desc).lower() for w in words):
            continue
        link = (node.findtext("link") or node.findtext("guid") or "").strip()
        if not link:
            continue
        stamp = (node.findtext("date") or "").strip()
        items.append(
            {
                "url": normalise(link),
                "title": htmllib.unescape(title),
                "teaser": clean(desc),
                "tags": [t.strip() for t in (node.findtext("subject") or "").split(",") if t.strip()],
                "sections": ["macro"],
                "kind": "article",
                "date": stamp[:10] or None,
            }
        )
    return items


def merge(items):
    """One entry per URL, combining the sections it was listed under."""
    merged = {}
    for item in items:
        key = item["url"]
        if key not in merged:
            merged[key] = dict(item, sections=sorted(set(item["sections"])))
            continue
        existing = merged[key]
        existing["sections"] = sorted(set(existing["sections"]) | set(item["sections"]))
        existing["tags"] = sorted(set(existing["tags"]) | set(item["tags"]))
        existing["date"] = max(filter(None, [existing["date"], item["date"]]), default=None)
    return sorted(merged.values(), key=lambda i: (i["date"] or "", i["url"]), reverse=True)


def collect(macro=False):
    """Every paper currently listed in the tracked sections, newest first."""
    items = []
    for slug in SECTIONS:
        try:
            items.extend(parse_cards(fetch("{}/market/{}/".format(BASE, slug)), slug))
        except Exception as exc:  # one dead section must not abort an unattended run
            print("WARNING: section {} skipped: {}".format(slug, exc), file=sys.stderr)
    if macro:
        try:
            items.extend(parse_rss(fetch(RSS_URL)))
        except Exception as exc:  # the RSS is a nice-to-have, never fail the run for it
            print("WARNING: macro scan skipped: {}".format(exc), file=sys.stderr)
    if not items:
        raise SystemExit("ERROR: nothing fetched from any section (site down or layout changed)")
    return merge(items)


def known_urls(state=None):
    """URLs already stored in data/state.json."""
    state = state or store.load()
    return {normalise(p["url"]) for p in state["papers"]}


def new_papers(state=None, macro=False):
    """Papers in the tracked sections that the dashboard has not seen yet."""
    state = state or store.load()
    known = known_urls(state)
    return [p for p in collect(macro=macro) if p["url"] not in known]


def article_text(url):
    """Cleaned body text of one article, without site chrome, authors and boilerplate."""
    markup = fetch(url)
    start = BODY_RE.search(markup)
    if start:
        open_end = markup.find(">", start.end())
        markup = markup[open_end + 1:] if open_end != -1 else markup[start.start():]
    text = clean(STRIP_RE.sub(" ", markup))
    for marker in TAIL_MARKERS:
        cut = text.rfind(marker)  # footer markers sit at the end of the page
        if cut > len(text) // 2:
            text = text[:cut]
    return text.strip()


def to_markdown(papers):
    lines = []
    for p in papers:
        sections = "/".join(s.upper() for s in p["sections"])
        if p.get("kind") == "snap":
            sections += " ·snap"
        lines.append("- {} - {} [{}]".format(p["date"] or "undated", p["title"], sections))
        lines.append("  {}".format(p["url"]))
        if p["tags"]:
            lines.append("  tags: {}".format(", ".join(p["tags"])))
        if p["teaser"]:
            lines.append("  > {}".format(p["teaser"]))
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Poll ING Think FX/rates/commodities sections.")
    ap.add_argument("--all", action="store_true", help="include papers already in the store")
    ap.add_argument("--md", action="store_true", help="print a readable list instead of JSON")
    ap.add_argument("--macro", action="store_true", help="also flag ECB/eurozone RSS pieces")
    ap.add_argument("--text", metavar="URL", help="print cleaned article text for one URL")
    ap.add_argument("--since", metavar="YYYY-MM-DD", help="only papers published on/after this date")
    ap.add_argument("--limit", type=int, default=0, help="cap the number of papers printed")
    args = ap.parse_args(argv)

    if args.text:
        print(article_text(args.text))
        return 0

    papers = collect(macro=args.macro) if args.all else new_papers(macro=args.macro)
    if args.since:
        papers = [p for p in papers if (p["date"] or "") >= args.since]
    if args.limit:
        papers = papers[: args.limit]

    if args.md:
        print(to_markdown(papers) if papers else "Nothing new.")
    else:
        print(json.dumps(papers, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
