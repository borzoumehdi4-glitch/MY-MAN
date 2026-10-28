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

## Rebuild

```bash
cd nail-trends-2026
python3 build_report.py
```

`nail_trends_data.py` is the single source of truth: edit the trend text there
and all three outputs regenerate. No third-party packages are used.

## Structure

- 6 macro themes, 30 trends in 4 categories (8 finishes, 7 colours, 11 nail-art
  looks, 4 shapes), each with palette, best shape, season, wearability,
  difficulty 1-5, a salon-ready "ask for" line and its sources.
- "Consensus" = how many of the 11 sources independently name the trend.
- Colour hex values are approximate swatches, not exact polish shades.
