"""Batch 4 (2026-10-30): four papers - the FX Daily and the BoJ piece from the FX
section, the Rates Spark that landed after yesterday's cut-off, and the Spain
election piece the macro layer surfaced under Articles. oil-iran is deliberately
untouched: no commodities paper in the batch. Probabilities are my own judgement,
not ING's.
Re-runnable: papers already in the store are skipped, and a probability is only
re-applied when it is not already recorded for D.
"""
import store

D = "2026-10-30"

NEW = {
 "spain-election-economy": {
  "date": "2026-10-30",
  "title": "A strong economy may not be enough to sway Spain's election",
  "url": "https://think.ing.com/articles/spains-strong-economy-may-not-decide-the-election/",
  "summary": "Spain's 29 November election has been overshadowed by a fatal high-speed rail collision near Urda in Toledo province that killed at least 69 people and led most parties to suspend campaigning, putting rail safety and public services into the debate alongside corruption cases touching the Socialists. The economy is still outperforming - 3Q GDP rose 0.6% QoQ and 2.7% YoY, well above most large eurozone peers - but unemployment climbed from 9.87% to 10.18% as the labour force grew 169,500 against 73,600 new jobs, harmonised inflation held at 4.9% and retail sales fell 1.4% YoY in September. The People's Party leads the polls and could reach a majority with Vox; Feijoo promises one million homes and a new Land Law within 100 days, against Socialist rent limits and eviction protection, while Spain added ~1.22m households between 2021 and 2025 but completed only ~466,000 homes. ING sees limited near-term macro impact - the energy shock and monetary tightening matter more - but a fragmented parliament would prolong the budget extensions and legislative paralysis.",
  "story_ids": ["france-ecb"]},
 "fx-daily-midterms": {
  "date": "2026-10-30",
  "title": "FX Daily: Time to think about the midterms?",
  "url": "https://think.ing.com/articles/fx-daily-time-to-think-about-the-midterms/",
  "summary": "Fresh pressure on tech stocks drove safe-haven demand into Treasuries and weighed on the dollar, and ING sees precautionary unwinding of net-long dollar positions as the main risk into Tuesday's midterms, with a Democratic sweep around 68% in prediction markets read as mildly dollar-negative through shutdown and debt-ceiling gridlock. Thursday's US data leaned hawkish - 3Q growth 3.4% and September core PCE 0.3% MoM - and the FOMC blackout ends with Barkin (neutral), Daly (moderate dove) and Musalem (moderate hawk), though ING doubts they can add much with a December hike priced. Lagarde said a hike was discussed, gave no indication French bonds prompt a dovish rethink and officials are 'ready' to raise in December, leaving room for EUR/USD to re-test 1.120-1.1250; ING expects eurozone 3Q GDP at 0.3% QoQ but only 0% in France against 0.1% consensus, and a negative French print would widen spreads. The BoJ held at 1.25% and flagged its 2% target as met, with ING now looking for hikes in December and March/April and USD/JPY holding a 155-160 range.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "boj-2pct-target": {
  "date": "2026-10-30",
  "title": "Bank of Japan hits 2% price target",
  "url": "https://think.ing.com/articles/bank-of-japan-2-price-target-hit/",
  "summary": "The BoJ left the policy rate at 1.25% - back-to-back hikes would have upset markets - but said for the first time that underlying CPI is 'generally consistent' with the 2% target set in 2013, so the debate shifts to how fast it reaches a 1.75-2.00% neutral rate. Energy prices, AI demand and the weak yen were all named as upside inflation risks, growth forecasts were held around 0.7-0.8%, CPI forecasts were nudged higher and the BoJ acknowledged overseas rate rises, with an implicit fear that not matching December hikes from the Fed and ECB would leave the yen vulnerable. ING now expects 25bp hikes in December and March, a 1.75% policy rate ahead of April consumption support, and an acceleration of ETF sales from JPY330bn to JPY860bn a year from 2027. USD/JPY stays bid toward the top of 155-160 until a decisive turn lower in 2Q27, with a USD/KRW-style AI-driven upside surprise the one to watch in 2027.",
  "story_ids": ["usd-rates-ai"]},
 "rates-spark-hikes-yields-fall": {
  "date": "2026-10-29",
  "title": "Rates Spark: Hikes coming, but bond yields choosing to fall",
  "url": "https://think.ing.com/articles/rates-spark-hikes-coming-but-bond-yields-choosing-to-fall/",
  "summary": "The US 10y made a decisive gap away from 5%, but to the downside, even though September core PCE rose to 3.1% - far from the 2% Warsh keeps restating - and income, spending and jobless claims all came in firm; the 7yr auction cleared with no tail and decent demand, and the move was more a back-end than front-end story. ING reads it as Treasuries staying responsive to AI-valuation sentiment and equity wobbles rather than fundamentals, calls it contrary to its preferred path back to higher yields but not enough to change its tune. On the ECB, a December hike looks near-certain with more than 20bp priced unless the Middle East improves or French bonds deteriorate, and a Reuters report that ECB staff see higher yields cutting 2027-28 growth by 100bp and inflation by 90bp supports ING's view that December could be the last hike of the cycle. Market pricing for further ECB tightening over 12 months has already fallen toward 65bp, driven mainly by French risk-off and more recently AI jitters, while Friday brings French, Spanish and German CPI plus eurozone 3Q GDP.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
}

PROB = {
 "france-ecb": {
  "Contained, grinding stress": (61, "Raised 60 -> 61: Lagarde confirmed a hike was discussed, saw no reason for a dovish rethink on French bonds and said officials are 'ready' for December with 20bp+ priced, so the grind continues."),
  "French relief": (11, "Cut 12 -> 11: ECB staff now estimate higher yields do much of the tightening (100bp of growth, 90bp of inflation in 2027-28), leaving less for a French budget-driven relief rally to deliver."),
  "Contagion and ECB backstop": (22, "Held at 22: ING expects 0% French 3Q GDP against 0.1% consensus and a negative print would widen OAT-Bund, but Spain's 29 November election looks unlikely to change near-term momentum."),
  "Disorderly sovereign event": (6, "Held at 6: the succession (de Cos dove vs Knot hawk) and an unresolved budget stay tail risks, with no new trigger this batch."),
 },
 "usd-rates-ai": {
  "Choppy around 5%, Dec hike alive": (39, "Cut 41 -> 39: the 10y has decisively left 5% behind and is trading on AI sentiment rather than levels, so pure chop around 5% gives up weight."),
  "Yields back above 5%, hawkish Fed": (32, "Cut 34 -> 32: yields fell despite core PCE at 3.1% and firm activity data, and the 7yr auction cleared cleanly, so the path back above 5% needs a fresh catalyst even though ING keeps its 5.25% call."),
  "AI-led risk-off and growth scare": (24, "Raised 20 -> 24: fresh tech pressure drove haven flows into Treasuries and ING warns against chasing USD upside into the midterms with a Democratic sweep ~68% priced."),
  "Disorderly bond/equity break": (5, "Unchanged at 5: the move was orderly, the 7yr auction had no tail and repo liquidity is stable."),
 },
}

STORY_TEXT = {
 "france-ecb": "The ECB held on 29 Oct and Lagarde confirmed a hike was discussed, saw no indication French bonds justify a dovish rethink and said officials are 'ready' to raise in December, with more than 20bp priced. ECB staff work estimating that higher yields cut 2027-28 growth by 100bp and inflation by 90bp keeps December as the likely last hike of the cycle. Her exit on 7 February 2027 brings the succession forward, with de Cos (dove) and Knot (hawk) the frontrunners and a dovish pick a euro negative. France is the immediate spread risk into Friday's flash CPI and 3Q GDP, where ING expects 0% growth against 0.1% consensus and a negative print would widen OAT-Bund, while Spain's 29 November election looks unlikely to change near-term momentum. The April 2027 French elections remain the cliff edge.",
 "usd-rates-ai": "The Fed held at 3.75-4.00% on a 10-2 vote and Warsh kept December alive, but the 10y has now gapped decisively away from 5% to the downside even with September core PCE at 3.1% and 3Q growth at 3.4% - Treasuries are trading on AI-valuation sentiment rather than data, and ING keeps its 5.25% target without changing its tune. A Democratic sweep is around 68% priced for the 3 November midterms, which ING reads as mildly dollar-negative and a reason not to chase USD upside after DXY pressed the year's highs where 102.50 opens 103.00. The BoJ held at 1.25% but declared its 2% target met, and ING now looks for hikes in December and March with USD/JPY bid in a 155-160 range until a 2Q27 turn lower.",
}



CHANGES = [
 "Rates Spark: the US 10y gapped decisively away from 5% to the downside even though September core PCE rose to 3.1% and income, spending and claims were firm; the 7yr auction cleared with no tail and the move was concentrated at the back end. ING keeps its 5.25% call. Hawkish-Fed scenario cut 34% -> 32%.",
 "AI sentiment is the marginal driver of Treasuries and the dollar again: fresh pressure on tech stocks brought haven flows, and a Democratic sweep is ~68% priced for the 3 November midterms, which ING reads as mildly dollar-negative and a reason not to chase USD upside. AI-led risk-off and growth scare raised 20% -> 24%, choppy base cut 41% -> 39% as the 10y left 5% behind.",
 "ECB: Lagarde confirmed a hike was discussed, gave no sign French bonds prompt a dovish rethink and officials are 'ready' to raise in December with 20bp+ priced; a Reuters report has ECB staff estimating higher yields cut 2027-28 growth by 100bp and inflation by 90bp, keeping December as the likely last hike of the cycle. Contained-grinding-stress raised 60% -> 61%, French relief cut 12% -> 11%.",
 "BoJ held at 1.25% but for the first time judged underlying CPI consistent with the 2% target, naming energy, AI demand and the weak yen as upside risks. ING now expects 25bp hikes in December and March, a 1.75% policy rate by April and ETF sales accelerated to JPY860bn a year from 2027, with USD/JPY bid in 155-160 until a 2Q27 turn lower.",
 "Spain's 29 November election is a close race with the PP ahead and a PP-Vox majority possible; 3Q GDP grew 0.6% QoQ and 2.7% YoY but unemployment rose to 10.18% and harmonised inflation held at 4.9%, and ING sees little immediate macro impact. Filed under the france-ecb story as eurozone political risk; no probability change.",
 "No commodities paper in this batch, so oil-iran weights are unchanged: Brent near $114 and TTF above EUR100 still hold the premium, with renewed speculation about US strikes on Iran offset by looser product markets and the lifted Russian diesel ban.",
 "Still open: US midterms 3 November, Spain's election 29 November, eurozone flash CPI and 3Q GDP (France 0% expected against 0.1% consensus, a negative print would widen spreads), ING's 2027 rates webinar 4 November, Lagarde's successor announcement (de Cos dove vs Knot hawk), BoJ hikes in December and March, and payrolls plus CPI before the 9 December FOMC.",
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
