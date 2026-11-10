"""Batch 4b (2026-11-05): analysis of two remaining ING papers from the tracked FX/rates/commodities
sections. Probabilities are my own judgement, not ING's.
These papers were auto-ingested on 5 November but not yet analysed.
Re-runnable: papers already analysed are skipped.
"""
import store

D = "2026-11-10"

PAPER_UPDATES = {
 "czech-national-bank-review-the-new-neutral-norma": {
  "date": "2026-11-05",
  "title": "Czech National Bank review: The new neutral normal",
  "url": "https://think.ing.com/articles/czech-national-bank-review-the-new-neutral-normal/",
  "summary": "The CNB raised its base rate to 4% on a split 4-3 vote, matching market expectations. Persistently elevated core inflation, weaker exchange rate, strong housing market and ample credit growth were cited as risks to price stability. The CNB forecast suggests a further increase up to 4.5% in the near term, followed by a gradual decline to 3.5% by end-2028. ING sees 4% as the new neutral normal, enabling the CNB to ride out second-round effects if its GDP and inflation forecasts prove right. EUR/CZK expected in the 24.350-24.400 range. Two additional rate hikes seen as the minimum the market will tolerate.",
  "story_ids": ["usd-rates-ai"]},
 "rates-spark-treasury-heat-from-tech-flight-but-for-how-long": {
  "date": "2026-11-05",
  "title": "Rates Spark: Treasury heat from tech flight - but for how long?",
  "url": "https://think.ing.com/articles/rates-spark-treasury-heat-from-tech-flight-but-for-how-long/",
  "summary": "The US 10yr yield is down ~50bp from recent highs, now in the low 4.80s%, as AI jitters drive safety flows into Treasuries. The 4.65% area is seen as the potential floor if risk-off intensifies. The market is ignoring elevated inflation, fiscal deficits and the AI growth boost. Jobless claims remain very low; unemployment expected to stay at 4.2%. The BoE hiked as expected with every committee member agreeing, revising inflation forecasts higher - markets now price a 50% chance of a December hike and at least one more in 2027. US jobs report expected at 65k non-farm payrolls for October.",
  "story_ids": ["usd-rates-ai"]},
}

CHANGES = [
 "CNB review (5 Nov): Czech National Bank raised rate to 4% on 4-3 split vote, seen as the new neutral normal. Further hike to 4.5% possible. EUR/CZK expected 24.350-24.400.",
 "Treasury heat (5 Nov): US 10yr yield down ~50bp to low 4.80s on AI jitters and safety flows. BoE hiked with all members agreeing; markets price 50% chance of December hike. US jobs report expected at 65k payrolls, unemployment 4.2%.",
]



def apply(state):
    """Apply the batch: update papers, update stories. Safe to re-run."""
    for pid, paper in PAPER_UPDATES.items():
        for p in state["papers"]:
            if p["url"].rstrip("/") == paper["url"].rstrip("/"):
                p["summary"] = paper["summary"]
                p["story_ids"] = paper["story_ids"]
                break

    for story in state["stories"]:
        story["paper_ids"] = [p["id"] for p in state["papers"] if story["id"] in p["story_ids"]]

    for text in CHANGES:
        state["changelog"].append({"date": D, "text": text})
    return list(PAPER_UPDATES.keys())


if __name__ == "__main__":
    st = store.load()
    new_ids = apply(st)
    store.save(st)
    print("updated:", len(new_ids), new_ids)
    print(store.validate(st) or "valid")
