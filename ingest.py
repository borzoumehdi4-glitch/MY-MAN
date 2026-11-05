"""Deterministic daily ingest, designed for GitHub Actions (no AI, no analysis).

Appends papers that are missing from data/state.json using clearly labelled
MECHANICAL summaries, then stops. It never changes scenario probabilities and
never writes interpretation - the Cline agent stays the only analytical pass
(see README). Probabilities and story links are left exactly as they are, so an
auto-ingested paper shows up in the Papers tab labelled [auto] until an analyst
pass rewrites its summary and links it to a story.

Usage:
    python3 ingest.py --dry-run   # show what would be added, change nothing
    python3 ingest.py             # write data/state.json
"""
import argparse
import os
import re
import sys

import feed
import store

FLOOR = "2026-10-29"  # fixed catch-up floor: nothing before this is ever ingested
MAX_PER_RUN = 12  # bound the work; the floor is fixed so leftovers are picked up next run
LABEL = "[auto]"
SUMMARY_MAX = 380


def slug_from_url(url):
    """A short, stable id derived from the article URL."""
    tail = url.rstrip("/").rstrip("/").rsplit("/", 1)[-1]
    slug = re.sub(r"[^a-z0-9]+", "-", tail.lower()).strip("-")
    return (slug[:48] or "paper").strip("-")


def unique_id(base, taken):
    """base, base-2, base-3 ... so ids never collide with the archive."""
    if base not in taken:
        return base
    n = 2
    while "{}-{}".format(base, n) in taken:
        n += 1
    return "{}-{}".format(base, n)


def _first_sentences(text, limit=SUMMARY_MAX):
    """Trim to whole sentences within a rough character budget."""
    text = re.sub(r"\s+", " ", (text or "")).strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    stop = max(cut.rfind(". "), cut.rfind("; "), cut.rfind(" - "))
    if stop > limit // 2:
        return cut[: stop + 1].strip()
    return cut.rsplit(" ", 1)[0].strip() + "..."


def mechanical_summary(item):
    """A plainly labelled summary built only from ING's own words."""
    body = item.get("teaser") or ""
    if not body:  # many listing cards carry no teaser; extract the opening prose
        try:
            body = feed.article_text(item["url"])
        except Exception:
            body = ""
    body = _first_sentences(body)
    kind = item.get("kind") or "article"
    sections = "/".join(sorted(item.get("sections") or []))
    text = "{} Mechanical summary (not analysed): {}".format(LABEL, body or "no extract available")
    return "{} [{}, {}]".format(text, kind, sections)


def candidates(state):
    """Tracked papers at or after the floor that the store has not seen, oldest first.

    Oldest first on purpose: with a fixed floor and a per-run cap, nothing can
    starve, even if ING has a burst of publications.
    """
    known = feed.known_urls(state)
    items = [
        item
        for item in feed.collect(macro=True)
        if item["url"] not in known and (item.get("date") or "") >= FLOOR
    ]
    return sorted(items, key=lambda i: (i["date"] or "", i["url"]))


def ingest(state, limit=MAX_PER_RUN):
    """Append up to `limit` missing papers. Returns the ids added."""
    taken = {p["id"] for p in state["papers"]}
    added = []
    for item in candidates(state)[:limit]:
        pid = unique_id(slug_from_url(item["url"]), taken)
        taken.add(pid)
        state["papers"].append(
            {
                "id": pid,
                "date": item["date"],
                "title": item["title"],
                "url": item["url"],
                "summary": mechanical_summary(item),
                "story_ids": [],  # linking is an analyst decision, not an ingest one
            }
        )
        added.append(pid)

    if added:
        state["changelog"].append(
            {
                "date": max(p["date"] for p in state["papers"]),
                "text": "Auto-ingest (GitHub Actions): {} paper(s) added with mechanical "
                "summaries labelled {}; probabilities unchanged, analysis pending.".format(
                    len(added), LABEL
                ),
            }
        )
    return added


def main(argv=None):
    ap = argparse.ArgumentParser(description="Mechanically ingest new ING papers.")
    ap.add_argument("--dry-run", action="store_true", help="report candidates, change nothing")
    ap.add_argument("--limit", type=int, default=MAX_PER_RUN, help="max papers this run")
    args = ap.parse_args(argv)

    state = store.load()

    if args.dry_run:
        found = candidates(state)
        print("floor={} candidates={} (would add {})".format(
            FLOOR, len(found), min(len(found), args.limit)))
        for item in found[: args.limit]:
            print("  {} | {} | {}".format(item["date"], "/".join(item["sections"]), item["title"][:64]))
        return 0

    added = ingest(state, args.limit)
    problems = store.validate(state)
    duplicates = [p for p in problems if "duplicate" in p]
    if duplicates:  # never write a state that breaks the duplicate guarantee
        print("ABORT:", duplicates, file=sys.stderr)
        return 2
    store.save(state)
    print("added={} ids={}".format(len(added), ",".join(added) or "-"))
    for problem in problems:
        print("WARNING:", problem, file=sys.stderr)

    output = os.environ.get("GITHUB_OUTPUT")
    if output:  # expose the count to the workflow
        with open(output, "a", encoding="utf-8") as handle:
            handle.write("added={}\n".format(len(added)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
