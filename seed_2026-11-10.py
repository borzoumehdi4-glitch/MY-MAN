"""Batch 4 (2026-11-06..10): analysis of four ING papers from the tracked FX/rates/commodities
sections. Probabilities are my own judgement, not ING's.
Re-runnable: papers already analysed are skipped, and a probability is only
re-applied when it is not already recorded for D.
"""
import store

D = "2026-11-10"

PAPER_UPDATES = {
 "fx-daily-tech-collapses-fx-shrugs": {
  "date": "2026-11-06",
  "title": "FX Daily: Tech collapses, FX shrugs",
  "url": "https://think.ing.com/articles/fx-daily-tech-collapses-fx-shrugs/",
  "summary": "Tech stocks fell heavily on data-centre concerns, but FX markets shrugged it off with only muted moves. JPY and CHF gained as safe havens while AUD/NZD underperformed. US short-dated rates fell ~50bp since late September, softening the dollar's yield advantage. The October jobs report (whisper +82k vs +29k prior) will confirm whether the Fed's 'solid' jobs assessment holds, potentially supporting short-dated rates and the dollar. DXY remains resilient at 101.50-102.50. EUR/USD consolidates near 1.12 with ECB December hike priced at 18bp. Banxico cut rates 3-2 to 6.25%, narrowing the Banxico-Fed spread to 225bp.",
  "story_ids": ["usd-rates-ai"]},
 "fx-daily-dollar-rally-needs-more-risk-off-fuel": {
  "date": "2026-11-09",
  "title": "FX Daily: Dollar rally needs more risk-off fuel",
  "url": "https://think.ing.com/articles/fx-daily-dollar-rally-needs-more-risk-off-fuel/",
  "summary": "Dollar rallied after strong payrolls (165k) and the tech selloff, but the move may be stretched and requires persistent risk-off to avoid correction. October CPI expected at 0.3% MoM headline and core, supporting December Fed hike expectations (19bp priced). Brent stabilized below $100/bl. Gadi Eisenkot given mandate to form Israeli government, seen as more diplomatic on Iran. EUR/USD undervalued 2.1-2.3%, expected back above 1.120. ECB succession race between de Cos (dove) and Knot (hawk) should have contained impact. BoE expected to hike again in February; EUR/GBP seen returning to 0.840.",
  "story_ids": ["usd-rates-ai", "oil-iran", "france-ecb"]},
 "eurozone-housing-market-in-2027-recovery-relapse": {
  "date": "2026-11-10",
  "title": "Eurozone housing market in 2027: recovery, relapse or revolution?",
  "url": "https://think.ing.com/articles/eurozone-housing-market-in-2027-recovery-relapse-or-revolution/",
  "summary": "Eurozone housing market recovering in 2027 but affordability remains a major constraint. Base case: activity regains momentum as households adapt to structurally higher rates, but stronger rebound unlikely. Risk case: bond market stress deepens if fiscal concerns spread beyond France, keeping mortgage rates higher for longer. Bold case: political 'whatever it takes' moment for housing. Persistent supply-demand mismatch should floor house prices, limiting significant correction.",
  "story_ids": ["france-ecb"]},
 "rates-spark-us-inflation-too-hot-for-comfort": {
  "date": "2026-11-10",
  "title": "Rates Spark: US inflation likely too hot for comfort",
  "url": "https://think.ing.com/articles/rates-spark-us-inflation-too-hot-for-comfort/",
  "summary": "Lower oil has diminished impact on rates; oil-rate correlation has weakened significantly. Risk sentiment improved with oil easing and AI stocks recovering. Global 10yr rates ticked lower. US CPI expected at 0.3% MoM headline and core - above the 0.17% needed for 2% annualized Fed target. Brent near $90/bl helps ease inflation risks but doesn't remove upside risks. Focus rotating toward second-round effects. Fed officials Waller, Logan, Schmid and Paulson speaking Tuesday; US Treasury sells new 10y notes (US$42bn).",
  "story_ids": ["usd-rates-ai", "oil-iran"]},
}

PROB = {
 "france-ecb": {
  "Contained, grinding stress": (62, "ECB succession race (de Cos vs Knot) seen as contained impact; eurozone housing risk adds mild contagion possibility. Cut 63 -> 62."),
  "French relief": (9, "Unchanged at 9: no new French-specific relief signals."),
  "Contagion and ECB backstop": (23, "Raised 22 -> 23: eurozone housing paper flags fiscal concerns beyond France keeping long-term yields elevated; ECB succession adds mild uncertainty."),
  "Disorderly sovereign event": (6, "Unchanged at 6: no new disorderly signals."),
 },
 "oil-iran": {
  "Elevated premium, no major disruption": (34, "Cut 36 -> 34: Brent stabilized below $100 and ticking toward $90; oil-rate correlation diminished."),
  "De-escalation": (31, "Raised 29 -> 31: Gadi Eisenkot given mandate to form Israeli government, seen as more diplomatic on Iran; peace negotiations making timid progress."),
  "Re-escalation, flows threatened": (29, "Unchanged at 29: geopolitical risk remains but no new escalation signals."),
  "Major supply outage": (6, "Unchanged at 6: no new supply disruption evidence."),
 },
 "usd-rates-ai": {
  "Choppy around 5%, Dec hike alive": (35, "Cut 37 -> 35: strong payrolls (165k) and hot CPI expectations shift weight toward sustained hawkish path."),
  "Yields back above 5%, hawkish Fed": (36, "Raised 34 -> 36: October CPI expected at 0.3% MoM headline and core; December hike 19bp priced; dollar resilient despite tech selloff."),
  "AI-led risk-off and growth scare": (24, "Unchanged at 24: tech selloff was significant but FX markets shrugged it off; AI stocks recovering."),
  "Disorderly bond/equity break": (5, "Unchanged at 5: no disorderly market signals."),
 },
}

STORY_TEXT = {
 "france-ecb": "The ECB held on 29 Oct and kept a December hike in play, arguing that wider French spreads are already doing the tightening for it. Lagarde announced she steps down on 7 February 2027, so the support sequence (verbal softening, then a QT pause, then TPI) has to survive a leadership change. Eurozone housing recovery in 2027 faces affordability constraints; bond market stress could deepen if fiscal concerns spread beyond France. ECB succession race between de Cos (dove) and Knot (hawk) seen as contained impact. April 2027 elections remain the cliff edge.",
 "oil-iran": "Brent holds around $95-100 with the market waiting for the 3 November midterms before repricing Gulf risk; simply getting past the vote without strikes could erode the premium without any US-Iran deal. Gadi Eisenkot given mandate to form Israeli government, seen as more diplomatic on Iran. TTF broke above EUR100/MWh earlier but gas prices have eased. Products are loosening - Russia lifted its diesel export ban and the gasoil crack fell to ~$70 - but crude and gas supply risk stay the swing factors.",
 "usd-rates-ai": "The Fed held at 3.75-4.00% on a 10-2 vote with two dissents for a hike, and Warsh kept December alive ('no ifs, ands or buts' on price stability); the 10y has validated its break back above 5% and ING still targets 5.25%. Strong payrolls (165k) and CPI expected at 0.3% MoM support the hawkish path. AI-valuation fear is fading as chip earnings recover, handing the dollar back to the hawkish-rate story, with DXY pressing 101.50-102.50. The RBNZ's dovish 4-3 hold (NZD -1.4%) and the BoC's 25bp hike to 2.50% show how much FX risk sits in central-bank surprises.",
}

CHANGES = [
 "FX Daily (6 Nov): Tech selloff hit equities but FX shrugged it off - JPY/CHF gained, AUD/NZD underperformed, dollar resilient at 101.50-102.50. US short-dated rates fell ~50bp since late September. Banxico cut to 6.25% (3-2).",
 "FX Daily (9 Nov): Dollar rallied on strong payrolls (165k) but move may be stretched. October CPI expected at 0.3% MoM, supporting December Fed hike (19bp priced). Brent below $100. Eisenkot given Israeli government mandate, seen as more diplomatic. EUR/USD undervalued 2.1-2.3%. BoE expected to hike in February.",
 "Eurozone housing (10 Nov): Housing recovering in 2027 but affordability constrained. Risk case: bond market stress deepens if fiscal concerns spread beyond France. Mild contagion risk for France-ECB story.",
 "Rates Spark (10 Nov): US CPI expected at 0.3% MoM headline and core - above 0.17% needed for 2% annualized Fed target. Brent near $90/bl but oil-rate correlation diminished. Focus rotating to second-round effects. Hawkish-Fed scenario raised 34% -> 36%, choppy base cut 37% -> 35%.",
 "Oil: Brent stabilized below $100 and ticking toward $90; Eisenkot more diplomatic on Iran. De-escalation raised 29% -> 31%, elevated premium cut 36% -> 34%.",
 "France-ECB: ECB succession race (de Cos vs Knot) seen as contained; eurozone housing adds mild contagion possibility. Contagion/ECB-backstop raised 22% -> 23%, contained stress cut 63% -> 62%.",
]


def apply(state):
    """Apply the batch: update papers, move probabilities, update stories. Safe to re-run."""
    for pid, paper in PAPER_UPDATES.items():
        for p in state["papers"]:
            if p["url"].rstrip("/") == paper["url"].rstrip("/"):
                p["summary"] = paper["summary"]
                p["story_ids"] = paper["story_ids"]
                break

    for story in state["stories"]:
        story["paper_ids"] = [p["id"] for p in state["papers"] if story["id"] in p["story_ids"]]
        if story["id"] not in PROB:
            continue
        story["updated"] = D
        story["summary"] = STORY_TEXT[story["id"]]
        for scenario in story["scenarios"]:
            if scenario["name"] not in PROB[story["id"]]:
                continue
            prob, note = PROB[story["id"]][scenario["name"]]
            history = scenario.get("history") or []
            if history and history[-1]["date"] == D and scenario["probability"] == prob:
                continue
            store.set_probability(state, story["id"], scenario["name"], prob, note, D)

    for text in CHANGES:
        state["changelog"].append({"date": D, "text": text})
    return list(PAPER_UPDATES.keys())


if __name__ == "__main__":
    st = store.load()
    new_ids = apply(st)
    store.save(st)
    print("updated:", len(new_ids), new_ids)
    print(store.validate(st) or "valid")
