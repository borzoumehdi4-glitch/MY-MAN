# ING Macro Scenarios Dashboard

Scope: only ING Think's three market sections are tracked.

- FX — https://think.ing.com/market/fx/
- Rates — https://think.ing.com/market/rates/
- Commodities — https://think.ing.com/market/commodities/

Workflow: new papers are summarised into `data/state.json` -> `python3 build.py` ->
open `dashboard.html` (single self-contained file, no install, no server).

Files: `store.py` (data logic), `feed.py` (site polling), `template.html` (page),
`build.py` (embeds data into the page), `test_feed.py` (offline tests).
Schema: papers, stories (scenarios with probability + history), changelog.

## Checking for new papers

```bash
python3 feed.py                          # JSON: in the 3 sections, not yet in data/state.json
python3 feed.py --md --since 2026-10-27  # readable, recent items only
python3 feed.py --all --limit 5          # what the sections currently list
python3 feed.py --text <url>             # cleaned article body, for summarising
python3 feed.py --macro                  # + ECB/eurozone pieces from the global RSS
```

Each paper carries `url`, `title`, `teaser`, `tags`, `sections`, `kind`
(`article` or `snap`) and `date` (UTC, read from the card's `data-date-raw`).
`teaser` is empty on many list cards - that is the site's behaviour, not a bug;
use `--text` for the body.

Why `--macro` exists: ECB and monthly pieces (e.g. the ECB cheat sheet) are filed
under "Articles" and never show up on the three market pages, yet they move the
`france-ecb` story. `--macro` adds RSS items matching ECB/eurozone keywords and
marks them `sections: ["macro"]`. Drop the flag for a strict three-section view.

`feed.py` never dies on one bad section (it warns and continues) and exits
non-zero with `ERROR:` if nothing at all could be fetched, so a scheduled run
cannot mistake a dead site for "nothing new".

## Updating the dashboard (unattended runbook)

1. `git pull`
2. `python3 feed.py --since <newest paper date in data/state.json> --md`
3. If it prints `Nothing new.` - stop. No commit, no rebuild.
4. For each new paper: `python3 feed.py --text <url>`, then write a 2-4 sentence
   summary (keep the numbers, levels and forecasts; drop the build-up).
5. Append the paper to `papers[]`: `id` (slug), `date`, `title`, `url`, `summary`,
   `story_ids`. Matching is by `url`, so copy it exactly from `feed.py`.
6. Move the affected scenarios with `store.set_probability(...)` so the history
   trail is kept, and append one `changelog` line per change plus one for
   anything still pending (meetings, data, elections).
7. `python3 build.py`
8. `python3 test_feed.py` - must end with `8 tests passed`.
9. `git add -A && git commit && git push`

## Tests

```bash
python3 test_feed.py   # offline, no network: card parsing, dedupe, RSS, text cleanup
```

The tests exist because the section pages mix card layouts (`h3` feature cards
with nested links, `p` list cards, `snaps/` reactions); if ING restyles the
listing, `test_feed.py` and `feed.py --all` are the fastest way to notice.

