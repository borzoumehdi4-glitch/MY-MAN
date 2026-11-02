"""Batch 5 (2026-10-30..11-02): five papers - the FX Daily, the Commodities Feed
and the BoE preview from the tracked sections, plus the Riksbank piece (FX) and
the German inflation snap the macro layer surfaced under /snaps/. Fitch's
unscheduled move on France's outlook came inside the FX Daily. Probabilities are
my own judgement, not ING's.
Re-runnable: papers already in the store are skipped, and a probability is only
re-applied when it is not already recorded for D.
"""
import store

D = "2026-11-02"

NEW = {
 "fx-daily-dollar-midterms": {
  "date": "2026-11-02",
  "title": "FX Daily: Dollar holds gains into midterms",
  "url": "https://think.ing.com/articles/fx-daily-dollar-holds-gains-into-midterms/",
  "summary": "The dollar was fractionally lower to start the week, tracking oil 2-3% lower on reports that Trump wants to let diplomacy run its course with Iran, while betting sites give the Democrats a 70-72% chance of taking both chambers in Tuesday's midterms - an outcome ING calls mildly dollar-negative on debt-ceiling gridlock and a prolonged shutdown next year, but largely speculative against 3Q growth of 3.4%, a sixth consecutive year of above-target inflation and a Fed readying another hike. DXY should keep trading around 102.00 with no strong case for a correction lower, with ISM surveys and Friday's October payrolls mattering less than price data barring a disastrous report. The 9% Nasdaq sell-off last month has softened short-dated US rates and a further tech slide is the biggest risk to long dollar positioning, with Apple reporting after today's close. Fitch's unscheduled late-Friday move of France's A+ outlook to negative, with another review promised by end-February, should cap EUR/USD rebounds - sellers are suspected in the 1.1200/1.1250 area - and keep EUR/CHF pressed toward 0.9180/85; a 25bp BoE hike to 4.00% on Thursday looks fully priced, the CNB is set to hike 25bp to 4.00%, and the NBP is expected to hold at 3.75% with no hike before 1Q27.",
  "story_ids": ["usd-rates-ai", "france-ecb", "oil-iran"]},
 "commodities-feed-midterms": {
  "date": "2026-11-02",
  "title": "The Commodities Feed: US midterm elections key for oil market",
  "url": "https://think.ing.com/articles/the-commodities-feed-post-midterms-key-for-the-oil-market021126/",
  "summary": "ICE Brent settled almost 2.4% higher on Friday to close above $113/bbl, with the expiring Dec-26 contract at $117.64 on its last trading day, but prices are off 2-3% today on reports that Trump wants to give diplomacy a chance and as Iranian negotiators hold talks with Qatari mediators in Doha. If the midterms pass with neither US/Israeli strikes nor a deal, the question is whether the geopolitical premium keeps being priced or starts to unwind, and with the speculative ICE Brent net long up 3,576 lots to 245,457 lots - still well below March's ~430k peak - there is room to add on the right catalyst. Ukrainian attacks on Russian refineries resumed after a roughly two-week pause that had taken the ICE gasoil crack below $70/bbl, Russia plans to export 2.15m tonnes of diesel in November against just over 500kt in October, and OPEC+ kept December output targets unchanged with most members already producing below target. TTF settled more than 6% higher near EUR104/MWh with colder-than-usual NW European weather ahead and storage just under 75% after peaking last Tuesday; gold fell 3.65% to a one-year low of $3,874.62/oz with silver down more than 6%, copper slipped although the LME cash-3m backwardation at $174.85/t and a Yangshan premium above $200/t show physical tightness, and CBOT corn lost nearly 11% in October on harvest pressure with the speculative net long cut for a sixth week to 55,314 lots.",
  "story_ids": ["oil-iran", "usd-rates-ai"]},
 "boe-first-hike": {
  "date": "2026-11-02",
  "title": "Bank of England set for first rate hike as energy shock worsens",
  "url": "https://think.ing.com/articles/bank-of-england-set-for-first-rate-hike-as-energy-shock-worsens/",
  "summary": "The BoE is set to hike 25bp to 4.00% on 5 November - its first move since the Iran war began, after an 'active hold' that stood in for 50bp of cuts - because a circa 25% January rise in the household energy cap pushes CPI to peak just above 4% early next year, with ING seeing a follow-up in February as more likely than not. It would be an insurance hike: there is no sign of second-round effects, energy-intensive inflation has actually fallen this year, core services are well behaved, private-sector wage growth is 3.4% and the labour market is stabilising. Watch the vote split (Dhingra and Taylor are the known doves, with Breeden the likeliest extra dissenter), guidance the Bank is expected to keep as non-committal as possible, and whether anyone pushes back on more than four hikes priced by this time next year - Huw Pill has already suggested that pricing looks unlikely. Global factors now explain less of GBP rate moves and UK swaps stay positively correlated with oil, so a big repricing is unlikely and sterling's outperformance can continue with EUR/GBP consolidating after a near-4% drop in just over a month.",
  "story_ids": ["usd-rates-ai", "oil-iran"]},
 "german-inflation-oct": {
  "date": "2026-10-30",
  "title": "German inflation drops to 2.8% YoY in October",
  "url": "https://think.ing.com/snaps/german-inflation-oct26/",
  "summary": "German headline inflation fell to 2.8% YoY in October from 3.3% and core inflation to 2.1% from 2.4%, a broader retreat than the fuel tax rebate alone, with services inflation also lower, household energy prices down month-on-month and no sign of indirect effects from higher energy prices at state level. ING still expects headline inflation back above 3% into late 2026 and early 2027 on oil, the winter heating season and low gas storage, and says it could take until end-2027 before it drops below 2% again - but selling price expectations remain below their April-May levels and consumers have less willingness and ability to pay than in 2022, so margin squeezing rather than pass-through is the expectation. For the ECB the numbers comfort the doves: with no second-round effects in sight, even a December hike might not yet be a done deal. (Snap: filed outside the three tracked sections.)",
  "story_ids": ["france-ecb"]},
 "riksbank-nov-hike": {
  "date": "2026-10-30",
  "title": "Riksbank to hike despite soft inflation and rallying krona",
  "url": "https://think.ing.com/articles/riksbank-to-hike-despite-soft-inflation-and-rallying-krona/",
  "summary": "The Riksbank is expected to hike 25bp to 2.00% on 4 November even though market bets have slipped from 22-24bp to 15-18bp, with officials' in-meeting and off-meeting commentary endorsing a move and the energy shock outweighing September's soft print and the stronger krona; no explicit commitment to more should follow, but the tightening bias stays. CPIF came in at 1.5% YoY as expected while CPIF excluding energy was just 0.5%, 0.2ppt below the Riksbank's forecast, though goods inflation was broad-based with durable prices up 1.1% month-on-month; ING keeps CPIF at 2.5% in December and expects a further hike to 2.25% on 3 February, after which the risks are hawkish. Brent is $118 against the $92 end-2026 assumption from September and European gas is up around 35%, while the krona is only 1.4% stronger on a trade-weighted basis and still 4% weaker year-to-date, so a hold would invite fresh SEK weakness. ING cuts its year-end EUR/SEK target to 11.00 from 11.10-11.15, sees a possible break below 10.90 in the coming week and a gradual slide to 10.70 over the next year.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
}

PROB = {
 "france-ecb": {
  "Contained, grinding stress": (62, "Raised 61 -> 62: Fitch moved France's A+ outlook to negative in an unscheduled Friday review and promised another by end-February, so the grind continues even as German inflation falls."),
  "French relief": (10, "Cut 11 -> 10: German October inflation at 2.8% with core at 2.1% and no second-round effects gives the ECB doves cover, but the Fitch move caps any OAT-led relief rally."),
  "Contagion and ECB backstop": (22, "Held at 22: Lagarde's 7 February exit keeps the succession (de Cos dove vs Knot hawk) live and TPI conditions remain hard to argue for France, with no new trigger this batch."),
  "Disorderly sovereign event": (6, "Held at 6: the promised Fitch review by end-February and an unresolved budget keep the tail alive without a fresh trigger."),
 },
 "usd-rates-ai": {
  "Choppy around 5%, Dec hike alive": (38, "Cut 39 -> 38: with the 10y already off 5% and ING judging ISM and payrolls less important than prices, the pure-chop branch gives a point to the AI-liquidation risk."),
  "Yields back above 5%, hawkish Fed": (32, "Held at 32: 3Q growth of 3.4%, a sixth straight year of above-target inflation and a Fed readying another hike keep the call alive, though the midterms are the nearer catalyst."),
  "AI-led risk-off and growth scare": (25, "Raised 24 -> 25: a 9% Nasdaq fall last month, Apple's earnings tonight and gold down 3.65% to a one-year low as investors liquidate to cover losses keep the equity-led branch bid."),
  "Disorderly bond/equity break": (5, "Held at 5: the precious-metals liquidation echoes forced selling but there is still no disorderly break in bonds or equities."),
 },
 "oil-iran": {
  "Elevated premium, no major disruption": (40, "Held at 40: Brent above $113, TTF near EUR104 and EU storage just under 75% keep the premium in place, with the midterms the swing event."),
  "De-escalation": (23, "Raised 22 -> 23: Trump is reported to want diplomacy to run, Iranian negotiators are in Doha, and a midterms week without strikes or a deal is exactly the path on which the premium unwinds."),
  "Re-escalation, flows threatened": (31, "Cut 32 -> 31: Ukrainian strikes on Russian refineries resumed after a two-week pause and Russia plans 2.15m t of November diesel exports, but the diplomatic track takes a point off the threat."),
  "Major supply outage": (6, "Held at 6: no change to the Hormuz or Gulf infrastructure tail this batch."),
 },
}

STORY_TEXT = {
 "france-ecb": "German October inflation fell to 2.8% YoY from 3.3% with core at 2.1% from 2.4%, services also lower and no second-round effects from energy at state level, which ING says comforts the ECB doves - even a December hike may not be a done deal - though it still expects headline back above 3% into late 2026 and early 2027. Against that, Fitch cut its outlook on France's A+ rating to negative in an unscheduled Friday review and promised another review by end-February, which ING sees capping EUR/USD rebounds around 1.1200/1.1250 and keeping EUR/CHF pressed toward 0.9180/85, with the budget and the April 2027 election the cliff edge. Lagarde's exit on 7 February 2027 keeps the succession (de Cos dove vs Knot hawk) in play, and the energy shock's longevity is now pulling European rates in both directions, with Spain's 29 November election unlikely to shift the near-term momentum.",
 "oil-iran": "Brent settled 2.4% higher on Friday just above $113/bbl with the expiring Dec-26 contract at $117.64, then fell 2-3% as Trump signalled he would let diplomacy with Iran run and Iranian negotiators met Qatari mediators in Doha; if the midterms pass with neither strikes nor a deal, the question becomes whether the premium unwinds gradually. Renewed Ukrainian attacks on Russian refineries after a two-week pause put a floor under the gasoil crack and Russia plans 2.15m t of November diesel exports against just over 500kt in October, while OPEC+ left December targets unchanged and the speculative ICE Brent net long, at 245,457 lots, is well below March's ~430k peak. TTF settled more than 6% higher near EUR104/MWh on colder NW European weather with storage just under 75% and the heating season under way, and the energy shock now looks deep and long enough that the BoE and Riksbank are both hiking through it.",
 "usd-rates-ai": "The dollar holds its gains into the 3 November midterms, where Democrats are 70-72% priced to take both chambers - ING reads that as mildly dollar-negative but speculative against 3Q growth of 3.4%, a sixth straight year of above-target inflation and a Fed readying another hike, so DXY stays around 102.00 with no case for a correction lower. The 9% Nasdaq sell-off last month has softened short-dated US rates and a further tech slide is the biggest risk to long-dollar positioning, with Apple reporting tonight and gold down 3.65% to a one-year low of $3,874.62/oz as investors liquidate to cover losses elsewhere. The energy shock is still forcing hikes elsewhere - the BoE is set to go 25bp to 4.00% on 5 November with a February follow-up likely, and the Riksbank 25bp to 2.00% on 4 November despite CPIF ex-energy at just 0.5%, with ING looking for 2.25% on 3 February and a EUR/SEK target cut to 11.00.",
}

CHANGES = [
 "FX Daily: Democrats are 70-72% priced to take both chambers on 3 November, which ING calls mildly dollar-negative but speculative against 3Q growth of 3.4%, a sixth year of above-target inflation and a Fed readying another hike, with DXY holding around 102.00 and no case for a correction lower. The bigger risk to long-dollar positioning is the tech sell-off - Nasdaq fell 9% last month, Apple reports tonight and gold slid 3.65% to a one-year low of $3,874.62/oz as investors raise cash. AI-led risk-off and growth scare raised 24% -> 25%, choppy base cut 39% -> 38%.",
 "Fitch moved its outlook on France's A+ sovereign rating from stable to negative in an unscheduled review late Friday and promised another review by end-February, citing the failure to repair public finances in weak growth; ING sees it capping EUR/USD rebounds (sellers suspected at 1.1200/1.1250) and keeping EUR/CHF pressed toward 0.9180/85. Contained-grinding-stress raised 61% -> 62%, French relief cut 11% -> 10%.",
 "German inflation snap (macro layer): headline fell to 2.8% YoY in October from 3.3% and core to 2.1% from 2.4%, with services lower, household energy down MoM on the fuel tax rebate and no indirect energy effects at state level; ING still sees headline back above 3% into early 2027 and says even a December ECB hike may not be a done deal. The dovish comfort is offset by the Fitch move, so contagion/ECB-backstop stays at 22% and disorderly at 6%.",
 "Commodities Feed: Brent settled 2.4% higher on Friday just above $113 (Dec-26 expiry $117.64) but is down 2-3% today on reports Trump wants to let diplomacy with Iran run, with Iranian negotiators in Doha; Ukrainian attacks on Russian refineries resumed after a two-week pause, Russia plans 2.15m t of November diesel exports against 500kt in October and OPEC+ kept December targets unchanged. De-escalation raised 22% -> 23%, re-escalation cut 32% -> 31%.",
 "The energy shock spreads to UK and Swedish policy: the BoE is set to hike 25bp to 4.00% on 5 November with a February follow-up more likely than not (CPI peaking just above 4% early next year on a ~25% energy cap rise, with no second-round effects yet), and the Riksbank is expected to hike 25bp to 2.00% on 4 November despite CPIF ex-energy at 0.5%, then to 2.25% on 3 February, with ING cutting its year-end EUR/SEK target to 11.00. Filed under usd-rates-ai, oil-iran and france-ecb as European tightening; no probability change beyond the entries above.",
 "Still open: US midterms 3 November and Apple's earnings tonight, BoE 5 November, Riksbank 4 November, ING's 2027 rates webinar 4 November, France's promised Fitch review by end-February, Lagarde's successor (de Cos dove vs Knot hawk), Spain's election 29 November, December FOMC on 9 December with payrolls and CPI before it, and BoJ hikes in December and March.",
]


def apply(state):
    """Add the batch once, then move probabilities once. Safe to re-run."""
    existing = {p["url"].rstrip("/") for p in state["papers"]}
    added = []
    for pid, paper in NEW.items():
        if paper["url"].rstrip("/") in existing:  # never ingest the same URL twice
            continue
        paper["id"] = pid
        state["papers"].append(paper)
        existing.add(paper["url"].rstrip("/"))
        added.append(pid)

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
                continue  # already applied on an earlier run
            store.set_probability(state, story["id"], scenario["name"], prob, note, D)

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
