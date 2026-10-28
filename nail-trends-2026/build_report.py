"""Generate the downloadable 2026 nail-trend report: HTML, CSV and Markdown.

Usage: python3 build_report.py
Outputs: nail-trends-2026.html, nail-trends-2026.csv, nail-trends-2026.md
"""
import csv
import html
from pathlib import Path

import nail_trends_data as d

ROOT = Path(__file__).parent
HTML_OUT = ROOT / "nail-trends-2026.html"
CSV_OUT = ROOT / "nail-trends-2026.csv"
MD_OUT = ROOT / "nail-trends-2026.md"

SHORT = {
    "ALLURE": "Allure", "VOGUE": "Vogue", "GH": "Good Housekeeping",
    "HB": "Harper's Bazaar UK", "WWW": "Who What Wear", "ELLE": "ELLE UK",
    "ALLURE_FALL": "Allure (fall colour)", "MC": "Marie Claire",
    "MC_SPRING": "Marie Claire (spring)", "HB_RUNWAY": "Harper's Bazaar (runway)",
    "PURE": "Pure Nails",
}

CSS = """
:root{--ink:#241f1c;--muted:#6f645c;--line:#e2d8cc;--bg:#fbf8f3;--card:#fffdf9;
--accent:#6d2e46;--accent-soft:#f3e8ec;--gold:#a9865b}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);
font:16px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent)}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.hero{padding:52px 0 30px;border-bottom:1px solid var(--line);
background:linear-gradient(180deg,#fffdf9,#fbf8f3)}
.kicker{letter-spacing:.18em;text-transform:uppercase;font-size:12px;
color:var(--accent);font-weight:700}
h1{font-family:Georgia,"Times New Roman",serif;font-weight:400;
font-size:clamp(34px,5vw,58px);line-height:1.04;margin:.28em 0 .3em}
h1 em{font-style:italic;color:var(--accent)}
.standfirst{max-width:70ch;color:var(--muted);font-size:17px;margin:0 0 22px}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px}
.pill{font-size:12px;letter-spacing:.04em;text-transform:uppercase;
border:1px solid var(--line);background:#fff;border-radius:999px;padding:6px 12px;
color:var(--muted)}
.pill b{color:var(--ink)}
.btn{display:inline-block;background:var(--accent);color:#fff;border:0;
border-radius:999px;padding:10px 18px;font-size:13px;font-weight:600;
letter-spacing:.03em;cursor:pointer;text-decoration:none}
.btn:hover{opacity:.9}
.toolbar{position:sticky;top:0;z-index:20;background:rgba(251,248,243,.96);
backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:12px 0}
.toolbar .row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.chip{font:inherit;font-size:13px;padding:7px 13px;border-radius:999px;
border:1px solid var(--line);background:#fff;color:var(--ink);cursor:pointer}
.chip[aria-pressed="true"]{background:var(--accent);color:#fff;border-color:var(--accent)}
#q{flex:1 1 200px;min-width:160px;font:inherit;font-size:14px;padding:8px 12px;
border:1px solid var(--line);border-radius:999px;background:#fff;color:inherit}
.count{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);
margin-left:auto}
section.block{padding:40px 0;border-bottom:1px solid var(--line)}
section[id]{scroll-margin-top:76px}
h2{font-family:Georgia,"Times New Roman",serif;font-weight:400;
font-size:clamp(24px,3vw,34px);margin:0 0 6px}
.lede{color:var(--muted);max-width:72ch;margin:0 0 22px}
.themes{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(300px,100%),1fr));gap:16px}
.theme{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px}
.theme h3{font-family:Georgia,serif;font-weight:400;font-size:19px;margin:0 0 8px}
.theme p{margin:0;color:var(--muted);font-size:14.5px}
.top{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(280px,100%),1fr));
gap:10px;counter-reset:rank;padding:0;margin:0}
.top li{list-style:none;background:var(--card);border:1px solid var(--line);
border-radius:12px;padding:12px 14px;display:flex;gap:12px;align-items:baseline;
counter-increment:rank;font-size:14.5px}
.top li::before{content:counter(rank,decimal-leading-zero);font-family:Georgia,serif;
color:var(--gold);font-size:15px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(330px,100%),1fr));gap:18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;
overflow:hidden;display:flex;flex-direction:column;break-inside:avoid}
.swatch{display:flex;height:46px}
.swatch span{flex:1}
.body{padding:18px 20px 20px;display:flex;flex-direction:column;gap:12px;flex:1}
.card-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
.num{font-family:Georgia,serif;font-size:13px;color:var(--gold);letter-spacing:.1em}
.cat{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;
background:var(--accent-soft);color:var(--accent);border-radius:999px;padding:4px 9px}
.card h3{font-family:Georgia,serif;font-weight:400;font-size:21px;line-height:1.2;margin:0}
.tag{font-size:13.5px;font-style:italic;color:var(--muted);margin:-6px 0 0}
.what{margin:0;font-size:14.5px}
dl{margin:0;display:grid;gap:7px}
dl div{display:grid;grid-template-columns:74px 1fr;gap:10px;align-items:baseline}
dt{font-size:10.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
dd{margin:0;font-size:13.5px}
.ask{margin:0;background:#f7f0e8;border-left:3px solid var(--gold);
border-radius:0 10px 10px 0;padding:10px 12px;font-size:13.5px;font-style:italic}
.diff{display:inline-flex;gap:3px;vertical-align:middle}
.diff i{width:7px;height:7px;border-radius:50%;background:#ded2c4;display:inline-block}
.diff i.on{background:var(--accent)}
.src{font-size:11.5px;color:var(--muted);margin:0;padding-top:10px;
border-top:1px dashed var(--line)}
.cal{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(240px,100%),1fr));gap:16px}
.cal div{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px}
.cal h3{font-family:Georgia,serif;font-weight:400;font-size:18px;margin:0 0 10px;
color:var(--accent)}
.cal ul{margin:0;padding-left:16px;font-size:14px;color:var(--muted)}
.cal li{margin-bottom:4px}
.script{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(320px,100%),1fr));gap:10px;
margin:0;padding:0}
.script div{background:var(--card);border:1px solid var(--line);border-radius:12px;
padding:12px 14px;font-size:14px}
.script b{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;
color:var(--gold);margin-bottom:3px;font-weight:700}
ol.sources{padding-left:0;margin:0;list-style:none;counter-reset:src}
ol.sources li{counter-increment:src;padding:10px 0 10px 34px;position:relative;
border-bottom:1px solid var(--line);font-size:14px}
ol.sources li::before{content:counter(src,decimal-leading-zero);position:absolute;left:0;
font-family:Georgia,serif;color:var(--gold);font-size:13px}
ol.sources a{word-break:break-word;color:var(--muted);font-size:12.5px}
.note{font-size:13px;color:var(--muted);max-width:80ch}
footer{padding:28px 0 60px;font-size:12.5px;color:var(--muted)}
.empty{display:none;padding:24px;text-align:center;color:var(--muted)}
@media (max-width:560px){.hero{padding:36px 0 22px}.count{margin-left:0}}
@media print{
@page{size:A4;margin:14mm}
body{background:#fff;font-size:10pt}
.toolbar,.btn,.print-hint{display:none!important}
.hero{padding:0 0 16px}
.grid{grid-template-columns:1fr 1fr;gap:10px}
.card{border:1px solid #cfc4b7;box-shadow:none}
section.block{padding:18px 0}
a{color:inherit;text-decoration:none}
.top li,.theme,.cal div,.script div{border:1px solid #ddd}
h1{font-size:30pt}
}
"""

JS = """
(function(){
  var cards=[].slice.call(document.querySelectorAll('.card'));
  var chips=[].slice.call(document.querySelectorAll('.chip'));
  var q=document.getElementById('q');
  var out=document.getElementById('count');
  var empty=document.getElementById('empty');
  var cat='All';
  function apply(){
    var term=(q.value||'').trim().toLowerCase(),shown=0;
    cards.forEach(function(c){
      var okCat=(cat==='All'||c.dataset.cat===cat);
      var okTerm=!term||c.dataset.search.indexOf(term)>-1;
      var show=okCat&&okTerm;
      c.style.display=show?'':'none';
      if(show)shown++;
    });
    out.textContent=shown+' of '+cards.length+' trends';
    empty.style.display=shown?'none':'block';
  }
  chips.forEach(function(b){
    b.addEventListener('click',function(){
      cat=b.dataset.cat;
      chips.forEach(function(x){x.setAttribute('aria-pressed',String(x===b));});
      apply();
    });
  });
  q.addEventListener('input',apply);
  apply();
})();
"""


def esc(text):
    return html.escape(str(text), quote=True)


def diff_dots(level):
    dots = "".join('<i class="on"></i>' if i < level else "<i></i>" for i in range(5))
    return '<span class="diff" title="Difficulty %d/5">%s</span>' % (level, dots)


def card(t):
    srcs = " &middot; ".join(SHORT[s] for s in t["sources"])
    chips = "".join('<span style="background:%s"></span>' % c for c in t["swatch"])
    haystack = " ".join([t["name"], t["tagline"], t["what"], t["palette"],
                         t["shape"], t["season"], t["wear"]]).lower()
    return f"""
<article class="card" data-cat="{esc(t['cat'])}" data-search="{esc(haystack)}">
  <div class="swatch" aria-hidden="true">{chips}</div>
  <div class="body">
    <div class="card-top"><span class="num">{t['n']:02d}</span>
      <span class="cat">{esc(t['cat'])}</span></div>
    <h3>{esc(t['name'])}</h3>
    <p class="tag">{esc(t['tagline'])}</p>
    <p class="what">{esc(t['what'])}</p>
    <dl>
      <div><dt>Palette</dt><dd>{esc(t['palette'])}</dd></div>
      <div><dt>Shape</dt><dd>{esc(t['shape'])}</dd></div>
      <div><dt>Season</dt><dd>{esc(t['season'])}</dd></div>
      <div><dt>Wear</dt><dd>{esc(t['wear'])}</dd></div>
      <div><dt>Difficulty</dt><dd>{diff_dots(t['diff'])}</dd></div>
    </dl>
    <p class="ask">Ask for: &ldquo;{esc(t['ask'])}&rdquo;</p>
    <p class="src">Sources: {srcs} &middot; consensus {len(t['sources'])}/{len(d.SOURCES)}</p>
  </div>
</article>"""


def hero():
    return f"""
<header class="hero">
  <div class="wrap">
    <p class="kicker">Nail trend report &middot; 2026</p>
    <h1>30 Nail Trends<br><em>for 2026</em></h1>
    <p class="standfirst">{esc(d.REPORT_SUBTITLE)}</p>
    <div class="meta">
      <span class="pill"><b>30</b> trends</span>
      <span class="pill"><b>{len(d.SOURCES)}</b> sources</span>
      <span class="pill">Compiled <b>{esc(d.REPORT_DATE)}</b></span>
      <span class="pill">Categories <b>{len(d.CATEGORIES)}</b></span>
    </div>
    <button class="btn" onclick="window.print()">Print / Save as PDF</button>
    <p class="note print-hint" style="margin-top:10px">Tip: this file is
      self-contained - open it anywhere, or use the button for a print-ready A4 PDF.</p>
  </div>
</header>"""


def toolbar():
    chips = ['<button class="chip" data-cat="All" aria-pressed="true">All 30</button>']
    for cat in d.CATEGORIES:
        n = sum(1 for t in d.TRENDS if t["cat"] == cat)
        chips.append(f'<button class="chip" data-cat="{esc(cat)}" aria-pressed="false">'
                     f'{esc(cat)} <span style="opacity:.6">{n}</span></button>')
    return f"""
<div class="toolbar">
  <div class="wrap row">
    {''.join(chips)}
    <input id="q" type="search" placeholder="Search a colour, shape or technique..." aria-label="Search trends">
    <span class="count" id="count">30 of 30 trends</span>
  </div>
</div>"""


def themes_section():
    cards = "".join(
        f'<div class="theme"><h3>{esc(title)}</h3><p>{esc(text)}</p></div>'
        for title, text in d.THEMES)
    return f"""
<section class="block" id="themes"><div class="wrap">
  <h2>What is actually driving 2026</h2>
  <p class="lede">Six shifts explain almost every look in this report. The short
    version: fewer, better-executed details on healthier nails - with a loud
    counter-current for people who are done with minimalism.</p>
  <div class="themes">{cards}</div>
</div></section>"""


def top_section():
    ranked = sorted(d.TRENDS, key=lambda t: (-len(t["sources"]), t["n"]))[:10]
    items = "".join(
        f'<li>{esc(t["name"])} '
        f'<span style="color:#6f645c">- {len(t["sources"])} sources</span></li>'
        for t in ranked)
    return f"""
<section class="block" id="top10"><div class="wrap">
  <h2>Top 10 by source consensus</h2>
  <p class="lede">Ranked by how many of the {len(d.SOURCES)} publications and
    reports independently name the look. It is a measure of agreement, not of
    what will suit your hands - use the filters below for that.</p>
  <ol class="top">{items}</ol>
</div></section>"""


def trends_section():
    cards = "\n".join(card(t) for t in d.TRENDS)
    return f"""
<section class="block" id="trends"><div class="wrap">
  <h2>The 30 trends</h2>
  <p class="lede">Grouped by finish, colour, nail art and shape. "Ask for" lines
    are written to be read aloud in the salon; difficulty is rated from 1 (a
    polish change) to 5 (specialist sculpting or mixed media).</p>
  <div class="grid" id="grid">
{cards}
  </div>
  <p class="empty" id="empty">No trend matches that search - try "chrome",
    "brown", "French" or clear the filters.</p>
</div></section>"""


def calendar_section():
    cols = "".join(
        "<div><h3>%s</h3><ul>%s</ul></div>" % (
            esc(season),
            "".join(f"<li>{esc(x)}</li>" for x in items))
        for season, items in d.SEASON_CALENDAR)
    return f"""
<section class="block" id="calendar"><div class="wrap">
  <h2>The 2026 calendar</h2>
  <p class="lede">What to book when. The same look often runs two seasons, but
    this is where each one peaks in editorial and salon demand.</p>
  <div class="cal">{cols}</div>
</div></section>"""


def script_section():
    blocks = "".join(
        f'<div><b>{esc(label)}</b>&ldquo;{esc(line)}&rdquo;</div>'
        for label, line in d.SALON_SCRIPT)
    return f"""
<section class="block" id="script"><div class="wrap">
  <h2>Salon script</h2>
  <p class="lede">Ten sentences that get you exactly what is in this report -
    copy them into your notes app before your appointment.</p>
  <div class="script">{blocks}</div>
</div></section>"""


def sources_section():
    items = "".join(
        f'<li>{esc(name)}<br><a href="{esc(url)}">{esc(url)}</a></li>'
        for name, url in d.SOURCES.values())
    return f"""
<section class="block" id="sources"><div class="wrap">
  <h2>Sources &amp; method</h2>
  <p class="lede">Every trend here is named by at least one of these
    publications or reports; the "consensus" figure on each card counts how many
    of the {len(d.SOURCES)} mention it. Colour chips are approximate swatches,
    not exact polish shades.</p>
  <ol class="sources">{items}</ol>
  <p class="note" style="margin-top:18px"><b>Method.</b> Editorial round-ups
    published 17 Dec 2025 - 25 Aug 2026 were read in full, their trend lists
    de-duplicated, and overlapping names merged into one entry (for example
    "cloudy French", "milky French" and "the soft, slim French"). Statements in
    quotation marks are attributed to the named expert in the source. Prices and
    product availability were not verified. Compiled {esc(d.REPORT_DATE)}.</p>
</div></section>"""


def footer():
    return f"""
<footer><div class="wrap">
  <p>{esc(d.REPORT_TITLE)} - compiled {esc(d.REPORT_DATE)} from
    {len(d.SOURCES)} published sources. Trend names and quotes belong to the
    publications credited above; this document is a summary for personal use.</p>
</div></footer>"""


def render_html():
    parts = [
        "<!doctype html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{esc(d.REPORT_TITLE)} - the full 2026 edit</title>",
        f'<meta name="description" content="{esc(d.REPORT_SUBTITLE)}">',
        f"<style>{CSS}</style>",
        "</head>",
        "<body>",
        hero(),
        toolbar(),
        themes_section(),
        top_section(),
        trends_section(),
        calendar_section(),
        script_section(),
        sources_section(),
        footer(),
        f"<script>{JS}</script>",
        "</body>",
        "</html>",
        "",
    ]
    return "\n".join(parts)


CSV_COLUMNS = [
    "Rank", "Trend", "Category", "Tagline", "What it is", "Palette / finish",
    "Best shape", "Peak season", "Wearability", "Difficulty (1-5)",
    "Source mentions", "Ask your nail tech", "Sources",
]


def write_csv():
    with CSV_OUT.open("w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.writer(fh)
        writer.writerow(CSV_COLUMNS)
        for t in d.TRENDS:
            writer.writerow([
                t["n"], t["name"], t["cat"], t["tagline"], t["what"],
                t["palette"], t["shape"], t["season"], t["wear"], t["diff"],
                f"{len(t['sources'])}/{len(d.SOURCES)}", t["ask"],
                "; ".join(SHORT[s] for s in t["sources"]),
            ])
    return CSV_OUT


def write_md():
    lines = [f"# {d.REPORT_TITLE}", "", f"> {d.REPORT_SUBTITLE}", "",
             f"Compiled {d.REPORT_DATE} | {len(d.TRENDS)} trends | "
             f"{len(d.SOURCES)} sources", "", "## Contents", ""]
    for cat in d.CATEGORIES:
        nums = [t["n"] for t in d.TRENDS if t["cat"] == cat]
        lines.append(f"- **{cat}** ({len(nums)}): trends "
                     f"{nums[0]:02d}-{nums[-1]:02d}")
    lines += ["- Top 10 by source consensus", "- 2026 calendar", "- Salon script",
              "- Sources & method", "", "---", "", "## What is driving 2026", ""]
    for title, text in d.THEMES:
        lines += [f"### {title}", "", text, ""]
    lines += ["## Top 10 by source consensus", ""]
    ranked = sorted(d.TRENDS, key=lambda t: (-len(t["sources"]), t["n"]))[:10]
    for i, t in enumerate(ranked, 1):
        lines.append(f"{i}. **{t['name']}** - named by {len(t['sources'])} of "
                     f"{len(d.SOURCES)} sources")
    lines += ["", "## The 30 trends", ""]
    for cat in d.CATEGORIES:
        lines += [f"### {cat}", ""]
        for t in d.TRENDS:
            if t["cat"] != cat:
                continue
            lines += [
                f"#### {t['n']:02d}. {t['name']}", "",
                f"*{t['tagline']}*", "",
                t["what"], "",
                f"- **Palette/finish:** {t['palette']}",
                f"- **Best shape:** {t['shape']}",
                f"- **Peak season:** {t['season']}",
                f"- **Wearability:** {t['wear']}",
                f"- **Difficulty:** {t['diff']}/5",
                f"- **Ask for:** \"{t['ask']}\"",
                f"- **Sources** ({len(t['sources'])}/{len(d.SOURCES)}): "
                f"{', '.join(SHORT[s] for s in t['sources'])}",
                "",
            ]
    lines += ["## The 2026 calendar", ""]
    for season, items in d.SEASON_CALENDAR:
        lines += [f"**{season}:** " + " | ".join(items), ""]
    lines += ["## Salon script", ""]
    for label, sentence in d.SALON_SCRIPT:
        lines.append(f"- **{label}:** \"{sentence}\"")
    lines += ["", "## Sources", ""]
    for i, (name, url) in enumerate(d.SOURCES.values(), 1):
        lines.append(f"{i}. {name} - <{url}>")
    lines += ["", "## Method", "",
              "Editorial round-ups published 17 Dec 2025 - 25 Aug 2026 were read "
              "in full, their trend lists de-duplicated, and overlapping names "
              "merged into one entry (for example \"cloudy French\", \"milky "
              "French\" and \"the soft, slim French\"). The consensus figure "
              "counts how many of the sources name the look. Colour chips and hex "
              "values in the HTML version are approximations, not exact polish "
              "shades; prices and availability were not verified. Quoted "
              "statements are attributed to the named expert in the source.", ""]
    MD_OUT.write_text("\n".join(lines), encoding="utf-8")
    return MD_OUT


def main():
    HTML_OUT.write_text(render_html(), encoding="utf-8")
    write_csv()
    write_md()
    for path in (HTML_OUT, CSV_OUT, MD_OUT):
        print(f"Wrote {path.name} ({path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
