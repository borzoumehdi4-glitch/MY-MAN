"""Batch 6 (2026-11-04..11-05): twelve papers - the post-midterm FX Dailies and
Rates Sparks, ING's 2027 rates outlook suite (US, euro, spreads, GBP, Dutch
pensions) and two France macro pieces the --macro layer surfaced under
"Articles". The two 11-03 items (Commodities Feed, FX Daily) are left for
tomorrow's run, which --since will still pick up. Probabilities are my own
judgement, not ING's.
Re-runnable: papers already in the store are skipped, and a probability is only
re-applied when it is not already recorded for D.
"""
import store

D = "2026-11-05"

NEW = {
 "rates-spark-boe-hike-club": {
  "date": "2026-11-05",
  "title": "Rates Spark: Bank of England likely to join the hiking club",
  "url": "https://think.ing.com/articles/rates-spark-bank-of-england-likely-join-the-hiking-club/",
  "summary": "Euro rates liked the oil move, with Brent sliding well below $100/bbl, front-end inflation swaps dropping and the money market now pricing only a little more than 50bp of ECB tightening by summer next year - though October headline inflation still rose to 4%. Bunds rallied with 10y yields below 3.3% and the 10y OAT/Bund spread easing below 150bp, tighter by more than 10bp on the day, which ING had expected towards year-end on a 2027 budget showing some deficit consolidation (even by decree) but not beyond it, given the presidential election. ING is less convinced than the market about the need for almost three more BoE hikes after today's 24bp-priced move, and sees a big repricing lower for GBP rates once inflation dynamics improve by mid-2027. Today brings French September industrial production (consensus -0.3% YoY), eurozone September PPI at +10.6% YoY and Spanish and French auctions of €6.75bn and €12bn.",
  "story_ids": ["france-ecb", "usd-rates-ai", "oil-iran"]},
 "fx-daily-rate-ingredient": {
  "date": "2026-11-05",
  "title": "FX Daily: A dollar downturn lacks the rate ingredient",
  "url": "https://think.ing.com/articles/fx-daily-a-dollar-downturn-lacks-the-rate-ingredient/",
  "summary": "The Democratic sweep delivered the dollar-negative move ING expected but no case for more, because lower oil is not unequivocally dollar-negative: with crude down 8%, 2y USD swap rates fell only 5bp while EUR, GBP and NZD 2y swaps fell 8-10bp, leaving DXY favoured to stabilise at 101.0-101.50. US data still support Fed tightening - ISM services employment rose to 51.4, the highest since February, and ADP payrolls at 86k point to a robust print against a 65k consensus - while a Banxico cut could push USD/MXN to 19. Knot came out firmly hawkish after the Netherlands backed his ECB candidacy, arguing second-round effects will pick up, while eurozone October inflation rose to 4.0% as expected with core anchored at 2.5%, making at least one December ECB hike look a done deal and leaving little upside in EUR/USD beyond the 1.130 year-end target. The BoE is expected to hike 25bp to 4.00% today on a 7-2 vote with a February follow-up as the base case, EUR/GBP stabilising near 0.840 and cable capped at 1.350, while Norges Bank holds at 4.5% and Sweden's October CPIF slows to 1.1% with the ex-energy measure at 0.1% after yesterday's hike.",
  "story_ids": ["usd-rates-ai", "france-ecb", "oil-iran"]},
 "france-manufacturing-sept": {
  "date": "2026-11-05",
  "title": "France\u2019s manufacturing rebound offers some relief, but no turning point yet",
  "url": "https://think.ing.com/articles/frances-manufacturing-rebound-offers-some-relief-but-no-turning-point-yet/",
  "summary": "French manufacturing output rose 0.5% in September after 0.3% in August, back to its June level, with food up 1.0%, electrical and computer equipment up 2.6% to the highest since November 2023 and transport equipment up 2.7% on a 7.5% rebound in autos - but output is still 0.9% below a year earlier, autos are down 9.3% YoY and total industrial production fell 0.5% on lower electricity output. Construction remains in deep recession, down another 0.2% in September and 4.5% below a year ago (civil engineering -6.6%, building -4.8%), and credit is tightening harder than anywhere else in the eurozone, with a net 27% of French banks stricter on business loans in 3Q. ING keeps GDP at 0.3% for 2026 and 0.5% for 2027 with risks to the downside, and notes the National Assembly unanimously rejected the revenue side of the 2027 budget by 458 votes after 11 days of debate, with adopted amendments pushing the deficit to an estimated 5.9% of GDP against the 5% target and only the Senate, Article 49.3 or a budget by ordinance before the 70-day deadline left.",
  "story_ids": ["france-ecb"]},
 "us-rates-triple-whammy": {
  "date": "2026-11-04",
  "title": "US rates and a triple whammy of obstacles to overcome",
  "url": "https://think.ing.com/articles/us-rates-and-a-triple-whammy-of-obstacles-to-overcome/",
  "summary": "ING's 2027 US rates baseline is a 10y Treasury yield back to 5.25%-plus (from 4.9% now) in the first quarter, with the absolute upside capped at 5.5%, as AI-sparked productivity growth, elevated fiscal deficits and sticky inflation keep the real yield and the term premium rising. Beyond the first quarter it looks for inflation to ease enough for the Fed to step away and the market to re-discount cuts, taking the 10y to 4.75% and then 4.5-4.75%, and flags three uncalled routes to 6%: GDP growth of 3-4%, a deficit blowing out to 7-8% of GDP, or inflation stuck around 3%. It prefers to fade the swap-spread tightening - the 10y swap spread below 40bp should re-widen above 50bp through 2027 and the 30y to at least 75bp - unless Treasury Secretary Bessent materially cuts long-end issuance or adds to buybacks.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "dutch-pension-finale": {
  "date": "2026-11-04",
  "title": "The grand Dutch pension reform finale",
  "url": "https://think.ing.com/articles/the-grand-dutch-pension-reform-finale/",
  "summary": "Dutch pension reform reaches its finale with almost €900bn of assets scheduled to transition in January 2027 on top of roughly €600bn already moved in 2026, out of a system holding more than €1.5tr. Because hedges will be set by age cohort rather than at fund level - just 10% for younger participants against 75% for those close to retirement - demand for hedges beyond 25 years will be relatively small, so the 10s30s euro swap curve should steepen structurally; ING credits the reforms with some 20bp of the 2025 steepening, while this year's flattening was a hawkish ECB and Fed repricing. The January transition should be orderly given funding ratios well above the 105% threshold (ABP above 130%), but hedging needs now move with asset prices, so funds will have to rebalance more often than under the old once-a-year liability review.",
  "story_ids": ["france-ecb"]},
 "rates-2027-good-bad-ugly": {
  "date": "2026-11-04",
  "title": "The Good the Bad and the Ugly for Rates in 2027",
  "url": "https://think.ing.com/articles/the-good-the-bad-and-the-ugly-for-rates-in-2027/",
  "summary": "ING's 2027 outlook centres on the good, the bad and the ugly causing trouble through at least the first quarter, taking the 10y Treasury back above 5.25% (capped at 5.5%) before inflation eases enough for a move to 4.5-4.75% later in the year. Euro rates get a bumpy ride in which a benign outcome brings the 2y swap down some 50bp while the 10y stays sticky, and an ugly inflation outcome could push the 10y well above 4%. European spreads face a turbulent first half with France the fault line and Bunds' safe-haven appeal masking supply, sterling rates sit well above fair value but only reprice significantly lower once the BoE can prove inflation is heading back to target by end-2027, and the Dutch pension finale should keep the 10s30s euro swap curve structurally steeper.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "rates-spark-blue-wave": {
  "date": "2026-11-04",
  "title": "Rates Spark: A blue wave in the US and euro inflation",
  "url": "https://think.ing.com/articles/rates-spark-a-blue-wave-in-the-us-and-euro-inflation/",
  "summary": "A decisive Democratic victory removes the risk of a contested result and of a Congress split between the parties, which should support sentiment, but the Democrats campaigned on a firmer anti-free-market line on data centres - and with much of US growth relying on the AI boom, stricter policy could become a headwind to watch. With Trump still running foreign policy inflation remains a wild card: the Iran war is not over, oil barely budged on the result and tariffs could return, and implied volatility measures suggest preparing for significant rate moves. Eurozone flash October CPI is seen at 4.0% headline with core steady at 2.5%, still pointing to a December ECB hike, with the ECB wage tracker and Lane speaking, while the US gets ISM services (seen 54.8), ADP and the quarterly refunding announcement with no change to coupon issuance expected.",
  "story_ids": ["usd-rates-ai", "france-ecb", "oil-iran"]},
 "fx-daily-blue-wave-preview": {
  "date": "2026-11-04",
  "title": "FX Daily: Blue wave price action a preview of what's to come",
  "url": "https://think.ing.com/articles/fx-daily-blue-wave-price-action-a-preview-of-whats-to-come/",
  "summary": "The blue wave first hit AI-sensitive assets - Korean and Taiwanese equities fell 3-4% overnight - but those losses were fully recouped once investors noted the Democrats do not take office until January and Trump accepted the results, leaving US 2y yields holding most of their 8-9bp drop and the overnight DXY low of 101.25 as important support into Friday's payrolls. ING still reads a Democratic Congress as mildly dollar-negative via the AI story and a possible prolonged shutdown from next summer, but with a strong US economy and a Fed ready to tighten it will not chase the dollar lower now; EUR/USD is correcting from a 1.1260 spike that marks the top of the range ahead of flash CPI (headline 4.0%, core 2.5%), where an upside core surprise would be euro-positive. Swiss October inflation at a surprisingly high 1.5% raises questions over whether the SNB can avoid tightening through 2027, a clean franc positive with downside risk to EUR/CHF, while the Riksbank's hike to 2.0% keeps its tightening bias and EUR/SEK around 11.00.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "france-social-fiscal-squeeze": {
  "date": "2026-11-04",
  "title": "France\u2019s social demands run up against tightening fiscal constraints",
  "url": "https://think.ing.com/articles/frances-social-demands-run-up-against-tightening-fiscal-constraints/",
  "summary": "Between 320,000 and 500,000 people marched last Saturday and all the main unions mobilise on 5 November over wages and purchasing power, pushing a government that is already considering a discretionary minimum-wage rise of 0.5-0.6pp on top of January's automatic ~1% - the first since 2012 - even though private-sector employment has fallen for seven straight quarters, 0.3% lower YoY and almost 70,000 jobs lost. After ten days and more than 2,300 amendments the 2027 budget is drifting towards a wider deficit than planned: the revenue vote was postponed again, adopted amendments have already worsened the projected deficit by €23.9bn (the 2026 total will be around €165bn), and with the National Assembly unlikely to approve anything the government faces Article 49.3 or, once the 70-day deadline expires on 18 December, a budget by ordinance. The 5% target is unrealistic on 1% growth assumptions given 3Q GDP fell 0.1%, investment dropped 0.6%, consumer confidence slid five points to 80 (lowest since June 2013) and a net 27% of banks tightened credit, so ING sees 0.3% growth this year and 0.5% in 2027, a deficit near 5.5% of GDP, debt above the 121.7% forecast for 2027 and a 10y OAT at 4.9%, more than 155bp over Bund against 70bp at end-2025.",
  "story_ids": ["france-ecb"]},
 "euro-spreads-duel-bad": {
  "date": "2026-11-04",
  "title": "European bond spreads in a duel with the 'Bad'",
  "url": "https://think.ing.com/articles/european-bond-spreads-in-a-duel-with-the-bad/",
  "summary": "Eurozone sovereign spreads are back in focus not just as country stories but as a function of rate volatility and risk sentiment, and the bad - high deficits - has re-entered the narrative with France singled out while Spain votes this month, Italy goes before the end of next year, Finland votes and Germany faces five state elections. ING sees the 10y OAT/Bund spread holding around 150bp as a floor through the electoral uncertainty around the 18 April and 2 May 2027 presidential rounds, with a tail risk that support for Mélenchon (who has floated cancelling the debt held by the Banque de France) pushes it beyond 200bp, and warns spreads could stay well above 100bp even afterwards alongside further downgrades - the market already prices France as if rated BBB. The ECB is likely to let markets work while the stress stays French, dialling back hawkishness or suspending QT rather than deploying TPI whose bar is high by the 500bp-plus BTP precedent of 2011, and Germany's safe-haven bid should fade as gross Bund funding exceeds €400bn next year plus at least €80bn of ECB runoff, taking 10y Bunds to at least 20bp over OIS from around 13bp.",
  "story_ids": ["france-ecb"]},
 "euro-rates-nervous": {
  "date": "2026-11-04",
  "title": "Euro rates have good reason to be nervous",
  "url": "https://think.ing.com/articles/euro-rates-have-good-reason-to-be-nervous/",
  "summary": "ING's 2027 euro rates view pairs substantial near-term upside risk with a more constructive year-end: ugly second-round inflation fears could take the 10y euro swap above 4% while faster disinflation could take it to 2%, and the baseline has inflation pressures easing and the ECB terminal rate anchoring near 2.5% by end-2027, with the 2y swap some 50bp lower if all goes well. Oil no longer tells the story - even at below $80/bbl swap rates would find little immediate relief - so each inflation print is watched for second-round effects, and with the 1Y1Y forward at just 2.2% and three further ECB hikes priced, a perceived weakening of transmission plus upside surprises could add another 100bp to 2y swaps. The 10y swap should stay sticky near fair value against nominal growth expectations of 3.3% as global real rates and heavy supply rise, with France the risk that forces the ECB to keep conditions supportive, halt QT and tolerate higher inflation - steeper curves, and the ECB caving to inflation is an unpriced risk with 5y5y swaps at just 2.1%.",
  "story_ids": ["france-ecb", "usd-rates-ai"]},
 "gbp-rates-delayed-landing": {
  "date": "2026-11-04",
  "title": "A delayed landing for GBP rates",
  "url": "https://think.ing.com/articles/a-delayed-landing-for-gbp-rates/",
  "summary": "ING expects the 10y gilt to ease in 2027 as inflation fears abate and the BoE starts considering cuts, but the path lower will be volatile because the 10y GBP swap is almost perfectly explained (98%) by BoE expectations plus the level and 2s10s slope of the US curve. Forwards already imply at least 100bp of further hikes to a ~4.75% terminal rate, above what is priced for the Fed, and ING disagrees - it sees a risk premium in the front end beyond macro fundamentals, so 2y GBP rates ease into 1H27 with the bigger dovish turn in the second half once inflation gives confidence of a return to 2%. QT tweaks that keep gilts of 23 years or longer on the balance sheet relieve the 30y, but the rise in long yields is a global trend and the extra supply is being absorbed by price-sensitive buyers - banks only partially, insurers and pension funds playing a smaller role - which keeps a material term premium justified.",
  "story_ids": ["usd-rates-ai"]},
}

# Own judgement on the evidence in this batch, not ING's forecasts.
# (new probability, why) - each story's scenarios must still sum to 100.
PROB = {
 "france-ecb": {
  # Revenue side of the 2027 budget rejected 458-0, amendments at 5.9% of GDP,
  # 5 Nov strikes, 18 Dec ordinance deadline: the grind is the base case, not relief.
  "Contained, grinding stress": (63, "Budget deadlock deepens: revenue side rejected 458-0, amendments at 5.9% of GDP, 5 Nov strikes"),
  "French relief": (9, "A credible 2027 budget looks further away after the 458-0 rejection"),
  "Contagion and ECB backstop": (22, "Fitch negative plus ING's 150bp floor/200bp tail keep the tail alive, no new trigger"),
  "Disorderly sovereign event": (6, "No auction failure or downgrade cascade; unchanged"),
 },
 "oil-iran": {
  # Brent from settled $113 on 30 Oct to well below $100, talks in Doha, midterm relief.
  "Elevated premium, no major disruption": (36, "Brent broke below $100 on diplomacy, out of the $100-120 band"),
  "De-escalation": (29, "Trump lets diplomacy run, Doha talks, oil down 8% in a day"),
  "Re-escalation, flows threatened": (29, "War not over and oil barely moved on the midterms, so only a small cut"),
  "Major supply outage": (6, "No flow disruption; unchanged"),
 },
 "usd-rates-ai": {
  # ING's 2027 call is 10y back above 5.25% in 1Q27; strong ADP/ISM; AI sell-off recouped.
  "Choppy around 5%, Dec hike alive": (37, "DXY stabilises 101.0-101.50, 10y 4.9%, ING sees 5.25%+ in 1Q27"),
  "Yields back above 5%, hawkish Fed": (34, "ING's 2027 baseline is 5.25-5.5% on AI productivity, deficits and sticky inflation"),
  "AI-led risk-off and growth scare": (24, "Blue-wave tech sell-off fully recouped; Democrats' data-centre stance a slower-burn risk"),
  "Disorderly bond/equity break": (5, "Unchanged"),
 },
}

STORY_TEXT = {
 "france-ecb": "The 2027 budget is going nowhere except towards a wider deficit: after eleven days the National Assembly rejected the revenue side unanimously by 458 votes, adopted amendments have already added €23.9bn (taking the deficit to an estimated 5.9% of GDP against the 5% target), and with the 70-day deadline expiring on 18 December the government's only routes are Article 49.3 or a budget by ordinance. Unions mobilise on 5 November over wages and purchasing power while growth stays near zero - 3Q GDP fell 0.1%, consumer confidence dropped five points to 80 and a net 27% of banks tightened credit - and ING sees just 0.3% growth this year and 0.5% in 2027, a deficit near 5.5% of GDP and debt above the 121.7% forecast, with the 10y OAT at 4.9% and more than 155bp over Bund against 70bp at end-2025. Fitch's unscheduled move of the A+ outlook to negative is now compounded by a spread market pricing France as if rated BBB; ING sees 150bp OAT/Bund as a floor through the 18 April and 2 May 2027 presidential rounds with a Mélenchon tail beyond 200bp, and expects the ECB to let markets work - the TPI bar is high. Eurozone October inflation at 4.0% with core at 2.5% keeps a December ECB hike on track and the succession (Knot hawkish, de Cos the dove) is the other EUR lever.",
 "oil-iran": "Brent has slid from the $113/bbl settle on 30 October to well below $100 - an 8% one-day drop - as Trump lets diplomacy with Iran run and Iranian negotiators talk to Qatari mediators, with the Democratic sweep adding risk-on momentum, though ING notes oil barely moved on the election result itself and the war is not over. The lower price is already doing macro work: front-end euro inflation swaps have dropped, the market prices only a little more than 50bp of ECB tightening by summer 2027 and ING's 2027 outlooks assume oil below $80/bbl. The physical buffer is thinner than the price action implies, with the ICE Brent net long far below March's peak and renewed Ukrainian attacks on Russian refineries holding the gasoil crack up, and Norway's krone is the clearest casualty as ING sees EUR/NOK back to 10.50 and ending the year at 10.55-10.65.",
 "usd-rates-ai": "The blue wave delivered exactly the mild dollar-negative move ING expected - US 2y yields fell 8-9bp and DXY touched 101.25 before stabilising, with ING seeing a 101.0-101.50 base rather than another break lower because lower oil is not unequivocally dollar-negative and US data still argue for tightening (ADP 86k, ISM services employment at 51.4, payrolls consensus 65k). The 2027 call is for the 10y Treasury back above 5.25% and possibly 5.5% in the first quarter on AI-sparked productivity, deficits and sticky inflation, then 4.5-4.75% later in the year as inflation eases and cuts are re-discounted - with three plausible routes to 6% - and for 10y swap spreads to re-widen above 50bp. Sterling rates sit above ING's fair value with the market pricing at least 100bp of further BoE hikes to a 4.75% terminal rate that ING rejects, and the BoE is expected to hike 25bp to 4.00% today on a 7-2 vote with a February follow-up as the base case. The AI angle cuts both ways: Korean and Taiwanese equities fell 3-4% on the result before recouping, and the Democrats' firmer line on data centres is a policy headwind for the capex boom.",
}

CHANGES = [
 "Oil: Brent broke from Friday's $113 settle to well below $100, an 8% drop in a day, as Trump let diplomacy with Iran run and negotiators met Qatari mediators in Doha, with the Democratic sweep adding risk-on relief - so the $100-120 band of the base case no longer holds, though ING notes the war is not over and oil barely moved on the election itself. De-escalation raised 23% -> 29%, elevated premium cut 40% -> 36%, re-escalation cut 31% -> 29%.",
 "France: the National Assembly rejected the revenue side of the 2027 budget unanimously by 458 votes after eleven days, adopted amendments had already added 23.9bn of deficit (5.9% of GDP against the 5% target), the 70-day deadline expires on 18 December with Article 49.3 or a budget by ordinance the only exits, unions mobilise on 5 November, and ING's spread work puts a 150bp OAT/Bund floor with a 200bp Melenchon tail through the April/May 2027 election. Contained-grinding-stress raised 62% -> 63%, French relief cut 10% -> 9%.",
 "US rates: ING's 2027 baseline has the 10y Treasury back above 5.25% (capped at 5.5%) in the first quarter on AI productivity, deficits and sticky inflation before easing to 4.5-4.75% later, while this week's data stayed hot (ADP 86k, ISM services employment at 51.4, payrolls consensus 65k) and the blue-wave tech sell-off was fully recouped. Yields back above 5% raised 32% -> 34%, choppy base cut 38% -> 37%, AI-led risk-off cut 25% -> 24%.",
 "The 2027 outlook suite (good/bad/ugly, euro rates, European spreads, GBP rates, Dutch pensions) is filed without further probability moves: euro rates carry material near-term upside risk with the 10y swap able to break 4% but a 2.5% terminal rate anchoring by end-2027, French spreads are floored near 150bp with the ECB reluctant to deploy TPI, sterling sits above ING's fair value against a 4.75% terminal rate it rejects, and almost 900bn of Dutch pension assets transition in January 2027, keeping the 10s30s curve structurally steeper.",
 "Still open: the 5 November BoE decision (25bp to 4.00% expected, 7-2 vote, February follow-up) and the 5 November French union mobilisation, the 3 November Commodities Feed and FX Daily not yet summarised (kept for tomorrow's --since run), France's 70-day budget deadline on 18 December and the promised Fitch review by end-February, Lagarde's succession (Knot hawkish vs de Cos dove), Spain's 29 November election, the 18 April and 2 May 2027 French presidential rounds, the December FOMC on 9 December with payrolls and CPI before it, and BoJ hikes in December and March.",
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

