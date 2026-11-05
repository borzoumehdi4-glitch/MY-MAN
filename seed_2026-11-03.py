"""Backfill batch (2026-11-03): the two papers that the 5 November run missed
because it capped at 12 items, and the --since guard then stranded them.

Probabilities are deliberately NOT touched here: the 4-5 November papers already
moved them with fresher information. This only completes the archive.
Re-runnable: papers already in the store are skipped.
"""
import store

D = "2026-11-03"

NEW = {
 "commodities-iran-talks": {
  "date": "2026-11-03",
  "title": "The Commodities Feed: False US-Iran hopes or the real deal?",
  "url": "https://think.ing.com/articles/the-commodities-feed-false-hopes-or-the-real-deal031126/",
  "summary": "ICE Brent settled 7.6% lower and fell back below $105/bbl on renewed hopes of US-Iran talks: Trump answered 'no' when asked whether he would strike Iran after the midterms, and Iran's president said the supreme leader has given the government more authority to negotiate. ING is not convinced the escalation risk has passed - the US struck Iran's Qeshm Island on Monday after Iran fired at a US aircraft - but clear progress in talks would mean more downside, because a large risk premium is still baked in while Gulf flows remain strong. TTF fell 8.7% to just under EUR95/MWh on the same hopes, with gas more exposed than oil since regional LNG flows have not recovered. Gold rebounded 1.85% from a one-year low as lower crude eased inflation fears.",
  "story_ids": ["oil-iran", "usd-rates-ai"]},
 "fx-daily-democratic-sweep": {
  "date": "2026-11-03",
  "title": "FX Daily: Democratic sweep can weigh on the dollar",
  "url": "https://think.ing.com/articles/fx-daily-democratic-sweep-can-weigh-on-the-dollar/",
  "summary": "All 435 House seats and 35 Senate seats were up on 3 November: the Democrats were expected to take the House comfortably, prediction markets gave them a 74% chance of the Senate, and ING's baseline assumed markets fully price a Republican House loss but only partially a clean sweep. A blue sweep could pressure the dollar via regulation fears hitting AI stocks and gridlock risk on government funding and the debt ceiling, though ING doubted it would shift the dollar structurally; a split Congress was seen as neutral to slightly USD-positive, with the Fed story still dominant. Brent's slide below $105 on diplomacy hopes had already softened the dollar alongside commodity currencies, EUR/USD was trying to establish support at 1.120, and French spreads showed above 150bp is the new normal.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
}

CHANGES = [
 "Backfill: the 3 November FX Daily and Commodities Feed were skipped by the 12-item cap on the 5 November run, then stranded because that run used the newest stored date as its --since floor. Added for completeness without moving probabilities, which already reflect the 4-5 November papers. The scheduler floor is now fixed at 2026-10-29 so this cannot recur.",
]


def apply(state):
    existing = {p["url"].rstrip("/") for p in state["papers"]}
    added = []
    for pid, paper in NEW.items():
        if paper["url"].rstrip("/") in existing:
            continue
        paper["id"] = pid
        state["papers"].append(paper)
        existing.add(paper["url"].rstrip("/"))
        added.append(pid)

    for story in state["stories"]:
        story["paper_ids"] = [p["id"] for p in state["papers"] if story["id"] in p["story_ids"]]

    if added:
        for text in CHANGES:
            state["changelog"].append({"date": D, "text": text})
    return added


if __name__ == "__main__":
    st = store.load()
    new_ids = apply(st)
    store.save(st)
    print("added:", len(new_ids), new_ids)
    print(store.validate(st) or "valid")
