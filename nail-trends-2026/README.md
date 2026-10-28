# 30 Nail Trends for 2026 - downloadable report

Research deliverable compiled 28 October 2026 from 11 published sources
(Vogue, Allure, Harper's Bazaar, ELLE, Good Housekeeping, Marie Claire,
Who What Wear and Pure Nails' 2026 shape report).

## Files

| File | What it is | Use it for |
| --- | --- | --- |
| `nail-trends-2026.html` | Self-contained, print-ready report | Open in any browser; "Print / Save as PDF" gives an A4 PDF |
| `nail-trends-2026.csv` | All 30 trends, 13 columns | Excel / Sheets / import into a moodboard or product sheet |
| `nail-trends-2026.md` | Same content as Markdown | Notion, Obsidian, GitHub, copy-paste |
| `30-nail-trends-2026-pictures.zip` | 30 photo cards + overview grid | Send the pictures: one 1080x1350 card per trend |
| `pictures/` | The same 30 cards unzipped | Pick individual images to send |

## Photo pack

`pictures/` holds one card per trend (1080x1350 px, 4:5 portrait) with the
trend name and a ready-made "ask for" line in the caption, plus
`00-all-30-trends.jpg` as a single overview image.

- 24 photos: Pexels (Pexels License, free to use, no attribution required)
- 6 photos: Wikimedia Commons (CC0 / CC BY / CC BY-SA - credited in `CREDITS.txt`)
- No true plaid/argyle manicure exists in the free-license libraries, so trend
  20 uses a check-print "preppy" mood shot; trend 06 uses a swirled velvet
  effect as the closest cat-eye match. Both are noted in the pack README.

## Rebuild the text report

```bash
cd nail-trends-2026
python3 build_report.py
```

`nail_trends_data.py` is the single source of truth: edit the trend text there
and all three text outputs regenerate. No third-party packages are used.

## Structure

- 6 macro themes, 30 trends in 4 categories (8 finishes, 7 colours, 11 nail-art
  looks, 4 shapes), each with palette, best shape, season, wearability,
  difficulty 1-5, a salon-ready "ask for" line and its sources.
- "Consensus" = how many of the 11 sources independently name the trend.
- Colour hex values are approximate swatches, not exact polish shades.
