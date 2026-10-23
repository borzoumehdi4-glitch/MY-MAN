# ING Macro Scenarios Dashboard (Phase 1)

Workflow: paste ING articles/URLs in chat -> analysis is written to `data/state.json` -> run `python3 build.py` -> open `dashboard.html` (single self-contained file, no install, no server).

Files: `store.py` (data logic), `template.html` (page), `build.py` (embeds data into the page).
Schema: papers, stories (scenarios with probability + history), changelog.
