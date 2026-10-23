# ING Macro Scenarios Dashboard (Phase 1)

Workflow: paste ING articles/URLs in chat -> analysis is written to `data/state.json` -> dashboard shows stories, scenarios, probability shifts.

    pip install -r requirements.txt
    streamlit run app.py

`store.py` holds the data logic (no dependencies). Schema: papers, stories (scenarios with probability + history), changelog.
