"""Batch 3 (2026-10-27..29): ten papers from the tracked FX/rates/commodities
sections, plus the three ECB/eurozone pieces the macro layer surfaced - including
Lagarde's resignation, which is filed as a snap outside the three sections but
drives the france-ecb story. Probabilities are my own judgement, not ING's.
Re-runnable: papers already in the store are skipped, and a probability is only
re-applied when it is not already recorded for D.
"""
import store

D = "2026-10-29"

NEW = {
 "fx-daily-ecb-doves": {
  "date": "2026-10-29",
  "title": "FX Daily: Can France wake up the ECB doves?",
  "url": "https://think.ing.com/articles/fx-daily-can-france-wake-up-ecb-doves/",
  "summary": "The softish dollar reaction to the Fed should not be over-read: the message stayed hawkish, a December hike is still 21bp priced and the bar to price it out is high. ING looked for core PCE at 0.3% MoM and 3Q GDP at 3.4% annualised, both dollar-positive, with DXY consolidating near the top of its range. On the ECB, the baseline was a neutral hold: not 'likely' to hike in December but 'possible/in play', with EUR/USD refusing to break 1.110. BoC hiked to 2.50% with more to come in 1Q27 and USD/CAD targeted at 1.420; the CNB looks set to go to 4.00% next week, and TTF above EUR100 keeps ING bearish on CEE currencies.",
  "story_ids": ["france-ecb", "usd-rates-ai"]},
 "fed-holds-10-2": {
  "date": "2026-10-28",
  "title": "Fed holds rates steady despite inflation being too high",
  "url": "https://think.ing.com/articles/fed-holds-rates-steady-despite-inflation-being-too-high/",
  "summary": "The FOMC held at 3.75-4.00% on a 10-2 vote, with Hammack and Cook dissenting for a hike (Cook's vote was the surprise given her centrist record). The statement kept 'inflation remains elevated' and 'expanding at a strong pace' with no pre-commitment; Warsh offered no guidance beyond promising price stability 'no ifs, ands or buts'. A December hike to 4.00-4.25% stays ING's call, with two payroll reports and a CPI print before the decision. ING expects US inflation back at 2% in 2H27, a prolonged pause through 2027 and the December 2026 hike reversed in December 2027; from September one FOMC meeting a year will carry no rate vote, two from 2028.",
  "story_ids": ["usd-rates-ai"]},
 "rates-spark-hawkish-lean": {
  "date": "2026-10-28",
  "title": "Rates Spark: Leaning hawkish, but no action",
  "url": "https://think.ing.com/articles/rates-spark-leaning-hawkish-but-no-action/",
  "summary": "The hawkish lean was enough to validate the 10y back above 5%; there was barely a word in the statement that did not lean hawkish, yet no hike. Warsh's comforting line on inflation expectations pulled yields back to 5%, but expectations actually rose after the decision, and ING maintains the journey toward 5.25% while the front end likes the hold, steepening the curve from both ends. Balance-sheet run-off stays a Warsh objective but is not imminent; repo liquidity is stable. For the ECB, 23bp of December tightening is already priced, so the France questions at the press conference mattered more than the decision, with a high hurdle for a QT pause or TPI.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "fx-daily-ai-risk-abates": {
  "date": "2026-10-28",
  "title": "FX Daily: Abatement in AI risk helps the dollar",
  "url": "https://think.ing.com/articles/fx-daily-abatement-in-ai-risk-helps-the-dollar/",
  "summary": "SK Hynix delivered strong earnings and Nasdaq futures added 0.6%, easing the AI-credit fear that had been the main threat to the bullish dollar story, so FX attention went back to energy, inflation and central banks. DXY is edging to the year's highs, where 102.50 opens 103.00. EUR/USD sits at the year's lows with 1.1065/1.1110 key support and 1.0880 the technical target below it, and the ECB bank lending survey showed tighter conditions plus an unexpected fall in corporate loan demand. A 20bp gilt risk premium could partly unwind on a boring UK budget, keeping EUR/GBP heavy toward 0.8315, and the BoC call was a coin flip.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "commodities-gas-100": {
  "date": "2026-10-29",
  "title": "The Commodities Feed: European gas tops EUR100 as supply fears grow",
  "url": "https://think.ing.com/articles/the-commodities-feed-european-gas-breaks-above-eur100-mwh-as-supply-fears-grow291026/",
  "summary": "TTF settled 4.85% higher and broke above EUR100/MWh for the first time since 2022, with little sign of relief in Persian Gulf LNG flows. QatarEnergy has extended force majeure for several buyers to the end of the year, Norwegian unplanned outages add supply risk and northwest Europe faces colder-than-usual weather from next week, with EU storage just under 75% and winter draws still ahead. Demand destruction is starting: power is deep into gas-to-coal switching and Yara has curtailed European ammonia, cutting its European gas use more than 7% YoY in 3Q26. Funds added 14.3TWh to their TTF net long, taking it to 207.4TWh.",
  "story_ids": ["oil-iran"]},
 "commodities-oil-wait-see": {
  "date": "2026-10-28",
  "title": "The Commodities Feed: Oil in wait-and-see mode ahead of US midterms",
  "url": "https://think.ing.com/articles/the-commodities-feed-oil-market-in-wait-and-see-mode281026/",
  "summary": "Crude fell for a second day with Brent still around $114, as the market waits for clarity on Trump's next move on Iran and will likely stay in wait-and-see until after the 3 November midterms. A US-Iran deal is not needed for prices to fall: simply getting past the elections without renewed strikes could start eroding the risk premium. Products are loosening - Russia lifted its diesel export ban and the ICE gasoil crack slid toward $70, its lowest since early October - and there are tentative signs of Russia-Ukraine diplomacy. API showed US crude stocks down about 2m barrels; gold recovered above $4,000, copper tightened on a record Yangshan premium and LME backwardation, while iron ore hit a two-year low.",
  "story_ids": ["oil-iran", "usd-rates-ai"]},
 "rbnz-dovish-hold": {
  "date": "2026-10-28",
  "title": "RBNZ's huge dovish surprise spells trouble for Kiwi dollar",
  "url": "https://think.ing.com/articles/rbnzs-huge-dovish-surprise-spells-trouble-for-kiwi-dollar/",
  "summary": "The RBNZ held at 2.75% on a 4-3 vote when markets priced 23bp of hikes, and NZD fell 1.4%; the dovish bloc, including Governor Breman, argued 3Q inflation was lower than expected and that growth risks dominate. With inflation set to break above 4% in 4Q26, a December hold would leave the real policy rate at -1.4%. ING still expects a hike in December (22bp priced) and at least one more in 1Q27, and sees pricing beyond that as too aggressive (60bp by March, 100bp by August 2027). NZD outperformance is dropped: year-end NZD/USD stays 0.570 but with downside risk, and AUD/NZD above 1.260 looks imminent after a hot Australian CPI.",
  "story_ids": ["usd-rates-ai"]},
 "boc-hike-250": {
  "date": "2026-10-28",
  "title": "Bank of Canada likely to hike again after today's move",
  "url": "https://think.ing.com/articles/bank-of-canada-likely-to-hike-again-after-todays-move/",
  "summary": "The BoC raised its overnight rate 25bp to 2.50% with about 80% priced and economists split; it justified the move with stronger-than-expected growth, solid consumer spending, rebounding oil-and-gas capex and sectors hit by US tariffs strengthening, while unemployment has risen to 6.5%. Cost pass-through could become a 2027 theme, so there 'could be the need to increase the policy rate further', but the BoC will 'proceed carefully'. ING targets 2.75% in 1Q27 (January preferred) with a December hike as the risk, and judges the 90bp of tightening priced over 12 months as too hawkish. CAD stays oil-dependent with a 1.420 year-end USD/CAD target.",
  "story_ids": ["usd-rates-ai"]},
 "rates-spark-gilts-warsh": {
  "date": "2026-10-27",
  "title": "Rates Spark: Kevin Warsh and John Healey walk into a bar",
  "url": "https://think.ing.com/articles/rates-spark-kevin-warsh-and-john-healey-walk-into-a-bar/",
  "summary": "About 20bp of risk premium sits in the 10y gilt ahead of the Autumn Budget, versus near zero a few months ago, and a boring budget could unwind most of it after gilts held up well in the pre-budget auctions. Global factors still drive sterling rates, and an early election would be the next surprise. In the US, the 10y had been clinging to 4.99% waiting to tick the FOMC off before deviating from 5%, and ING expects it to snap back above 5% on inflation, the deficit and the AI boom; a super-hawkish Warsh without a hike would tempt that, a super-dovish one would validate the break below. Balance-sheet shrinkage plans are expected nearer the turn of the year.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "ecb-holds-lagarde-out": {
  "date": "2026-10-29",
  "title": "ECB keeps rates on hold as Christine Lagarde announced her resignation",
  "url": "https://think.ing.com/snaps/ecb-keeps-rates-on-hold-as-christine-lagarde-announced-her-resignation/",
  "summary": "The ECB left rates unchanged because higher headline inflation is showing few knock-on effects while bond yields have already made financing conditions more restrictive - the bond market has taken over the ECB's job. The news came hours earlier: Lagarde announced she will step down on 7 February 2027. France dominates the TPI debate, because the instrument requires compliance with the EU fiscal framework and that is hard to argue for France today; ING hopes the ECB remembers March 2020, when saying it was not there to narrow spreads backfired. (Snap: filed outside the three tracked sections.)",
  "story_ids": ["france-ecb"]},
 "lagarde-december-hike": {
  "date": "2026-10-29",
  "title": "Lagarde's comments point to a December ECB rate hike",
  "url": "https://think.ing.com/articles/lagarde-comments-point-to-december-ecb-rate-hike/",
  "summary": "Rates on hold and Lagarde out is the headline, but the nuance is that the ECB still looks set to hike in December despite growing stagflationary pressures: it debated a hike today and the worsening of financing conditions took it off the table. Lagarde called growth risks tilted to the downside and inflation risks to the upside, saw no second-round effects beyond the September projections, and flagged two developments since September - higher energy prices and tighter financing conditions. ING's three parameters are the length of the Middle East war, the pass-through of energy into the rest of the economy, and French contagion.",
  "story_ids": ["france-ecb", "usd-rates-ai"]},
 "ez-sentiment-oct": {
  "date": "2026-10-29",
  "title": "Eurozone sentiment weakens in October as price expectations tick up",
  "url": "https://think.ing.com/snaps/eurozone-sentiment-weakened-in-october-as-price-expectations-tick-up/",
  "summary": "The eurozone Economic Sentiment Indicator fell to 96.9 from 97.5, the weakest since June, with employment expectations up slightly. Industry actually improved - production, orders and hiring intentions all firmer - while services were more downbeat on demand but more optimistic on the months ahead; consumers are shying away from major purchases. The ECB-relevant detail is that both industry and services expect stronger price increases ahead, especially for goods. No immediate need to hike, but no room to sound dovish either. (Snap: filed outside the three tracked sections.)",
  "story_ids": ["france-ecb"]},
 "webinar-2027-rates": {
  "date": "2026-10-29",
  "title": "ING webinar on the 2027 rates outlook: The Good, the Bad, and the Ugly",
  "url": "https://think.ing.com/articles/webinar-the-good-the-bad-and-the-ugly-for-rates-in-2027/",
  "summary": "ING's 2027 rates webinar (4 November, 1400 GMT) frames the debate rather than taking a view: whether the US 10y can reach 6% on AI and productivity, extraordinary deficits and stubborn inflation, what Treasury Secretary Bessent could do if yields surge, and whether the eurozone's inflation shock is changing rather than fading. It also asks how second-round effects, heavy bond supply and rising global real rates complicate the ECB's path even if it turns more dovish, with France's debt challenge as the extra sovereign uncertainty. Useful as the agenda for what to watch into year-end.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
}

PROB = {
 "france-ecb": {
  "Contained, grinding stress": (60, "ECB held on 29 Oct and kept December alive; spreads remain the anchor, but Lagarde's exit on 7 Feb 2027 adds a succession overhang into the April 2027 election run-up. Cut 62 -> 60."),
  "French relief": (12, "Softened 13 -> 12: a French bond rally needs a credible 2027 budget, and the ECB just showed it will not pre-commit to support while yields do the tightening."),
  "Contagion and ECB backstop": (22, "Raised 20 -> 22: the ECB explicitly argued the bond market has taken over its job, and TPI/QT sequencing now has to survive a change of president."),
  "Disorderly sovereign event": (6, "Raised 5 -> 6: leadership transition plus an unresolved budget and downside growth/upside inflation risks from Lagarde's own framing."),
 },
 "oil-iran": {
  "Elevated premium, no major disruption": (40, "Unchanged at 40: Brent around $114 and TTF above EUR100 keep the premium in place, but crude has stopped making new highs."),
  "De-escalation": (22, "Raised 18 -> 22: simply getting past the 3 November midterms without strikes could erode the premium without any US-Iran deal, Russia lifted its diesel export ban and the gasoil crack fell to ~$70."),
  "Re-escalation, flows threatened": (32, "Cut 36 -> 32: two days of lower crude and looser product markets trim the urgency, though renewed post-election strikes remain the main risk."),
  "Major supply outage": (6, "Unchanged at 6: no new evidence on flows or facilities."),
 },
 "usd-rates-ai": {
  "Choppy around 5%, Dec hike alive": (41, "Cut 43 -> 41: the 10y has already validated its move back above 5%, so the pure chop scenario gives up weight to the sustained-hawkish one."),
  "Yields back above 5%, hawkish Fed": (34, "Raised 30 -> 34: the Fed held on a 10-2 vote with two hike dissents, Warsh kept December alive at 21bp priced, and ING maintains the 5.25% path."),
  "AI-led risk-off and growth scare": (20, "Cut 22 -> 20: SK Hynix earnings and firmer Nasdaq futures are defusing the AI-credit fear that dominated last week."),
  "Disorderly bond/equity break": (5, "Unchanged at 5: repo liquidity is stable and no auction stress this week."),
 },
}

STORY_TEXT = {
 "france-ecb": "The ECB held on 29 Oct and kept a December hike in play, arguing that wider French spreads are already doing the tightening for it. Lagarde announced she steps down on 7 February 2027, so the support sequence (verbal softening, then a QT pause, then TPI) has to survive a leadership change, and TPI still cannot be justified while France is non-compliant with the fiscal rules. Eurozone sentiment slipped to 96.9 with price expectations rising, so there is no room to sound dovish. The April 2027 elections remain the cliff edge.",
 "oil-iran": "Brent holds around $114 with the market waiting for the 3 November midterms before repricing Gulf risk; simply getting past the vote without strikes could erode the premium without any US-Iran deal. TTF broke above EUR100/MWh for the first time since 2022 on Qatari force majeure, Norwegian outages and colder weather, with EU storage just under 75% and winter draws ahead. Products are loosening - Russia lifted its diesel export ban and the gasoil crack fell to ~$70 - but crude and gas supply risk stay the swing factors.",
 "usd-rates-ai": "The Fed held at 3.75-4.00% on a 10-2 vote with two dissents for a hike, and Warsh kept December alive ('no ifs, ands or buts' on price stability); the 10y has validated its break back above 5% and ING still targets 5.25%. AI-valuation fear is fading as chip earnings land, handing the dollar back to the hawkish-rate story, with DXY pressing the year's highs where 102.50 opens 103.00. The RBNZ's dovish 4-3 hold (NZD -1.4%) and the BoC's 25bp hike to 2.50% show how much FX risk sits in central-bank surprises.",
}
CHANGES = [
 "Fed held at 3.75-4.00% on a 10-2 vote: Hammack and Cook dissented for a hike, and Warsh promised price stability 'no ifs, ands or buts' without pre-committing to December. A hike to 4.00-4.25% stays ING's call with 21bp priced. Hawkish-Fed scenario raised 30% -> 34%, choppy base cut 43% -> 41%.",
 "The AI risk-off impulse faded: SK Hynix beat, Nasdaq futures added 0.6% and Alphabet/Microsoft reported next. AI-led risk-off and growth scare cut 22% -> 20%.",
 "ECB held on 29 Oct as expected. Lagarde framed it as the bond market taking over the ECB's job, saw growth risks to the downside and inflation risks to the upside, and still pointed to a December hike.",
 "Christine Lagarde announced she will step down on 7 February 2027 - a snap filed outside the three tracked sections, picked up by the macro layer. Contagion/ECB-backstop raised 20% -> 22%, disorderly raised 5% -> 6%, contained stress cut 62% -> 60%, French relief cut 13% -> 12%.",
 "Oil: Brent around $114 and lower for a second day into the 3 November midterms; Russia lifted its diesel export ban and the ICE gasoil crack fell to ~$70. De-escalation raised 18% -> 22%, re-escalation cut 36% -> 32%.",
 "Gas: TTF settled above EUR100/MWh for the first time since 2022 (+4.85%) on extended Qatari force majeure, Norwegian outages and colder weather; EU storage just under 75%. Elevated-premium scenario held at 40%.",
 "Eurozone sentiment fell to 96.9 from 97.5, but industry and services both expect stronger price increases ahead, so no hike is needed now and no dovish turn is available either.",
 "RBNZ held at 2.75% on a 4-3 vote and NZD fell 1.4%; BoC hiked 25bp to 2.50% with ING seeing a 2.75% peak in 1Q27. USD/CAD keeps a 1.420 year-end target and markets look too hawkish on both.",
 "Still open: BoJ on 30 Oct, US midterms 3 November, ING 2027 rates webinar 4 November, and payrolls plus CPI before the 9 December FOMC. UK Autumn Budget gilt reaction also pending.",
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


