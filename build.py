"""Generate dashboard.html (single self-contained file) from data/state.json.

Usage: python3 build.py
"""
import json
import sys
from pathlib import Path

import store

ROOT = Path(__file__).parent


def build(state_path=store.DATA_FILE, out_path=ROOT / "dashboard.html"):
    state = store.load(state_path)
    for p in store.validate(state):
        print("WARNING:", p, file=sys.stderr)
    data = json.dumps(state, ensure_ascii=False).replace("</", "<\\/")
    html = (ROOT / "template.html").read_text(encoding="utf-8").replace("__DATA__", data)
    Path(out_path).write_text(html, encoding="utf-8")
    return Path(out_path)


if __name__ == "__main__":
    print("Wrote", build())
