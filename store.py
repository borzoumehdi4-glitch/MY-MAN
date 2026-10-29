"""JSON-backed store for the ING macro dashboard (no third-party deps)."""
import json
from datetime import date
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "state.json"

EMPTY = {"papers": [], "stories": [], "changelog": []}


def load(path=DATA_FILE):
    path = Path(path)
    if not path.exists():
        return json.loads(json.dumps(EMPTY))
    return json.loads(path.read_text(encoding="utf-8"))


def save(state, path=DATA_FILE):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def validate(state):
    """Return list of problems (empty = ok). Probabilities per story should sum to ~100."""
    problems = []
    paper_ids = {p["id"] for p in state["papers"]}
    for s in state["stories"]:
        total = sum(sc["probability"] for sc in s["scenarios"])
        if s["scenarios"] and abs(total - 100) > 1:
            problems.append(f"{s['id']}: scenario probabilities sum to {total}, not 100")
        for pid in s.get("paper_ids", []):
            if pid not in paper_ids:
                problems.append(f"{s['id']}: unknown paper {pid}")

    # Guard against duplicate ingestion, which matters now that batches are automated.
    seen_ids, seen_urls = {}, {}
    for p in state["papers"]:
        if p["id"] in seen_ids:
            problems.append(f"duplicate paper id {p['id']}")
        seen_ids[p["id"]] = True
        url = p["url"].rstrip("/")
        if url in seen_urls:
            problems.append(f"duplicate paper url {url} ({seen_urls[url]} and {p['id']})")
        seen_urls[url] = p["id"]
    return problems


def prob_shift(scenario):
    """Change in probability between the last two history points (None if <2)."""
    h = scenario.get("history", [])
    return h[-1]["probability"] - h[-2]["probability"] if len(h) >= 2 else None


def set_probability(state, story_id, scenario_name, prob, note, when=None):
    when = when or date.today().isoformat()
    for s in state["stories"]:
        if s["id"] == story_id:
            for sc in s["scenarios"]:
                if sc["name"] == scenario_name:
                    sc["probability"] = prob
                    sc.setdefault("history", []).append(
                        {"date": when, "probability": prob, "note": note})
                    return
    raise KeyError((story_id, scenario_name))


