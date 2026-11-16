"""Batch 5 (2026-11-10..16): analysis of 21 ING papers collected by GitHub Actions.
Probabilities are my own judgement, not ING's.
Re-runnable: papers already analysed are skipped, probabilities only re-applied
when not already recorded for D.
"""
import store

D = "2026-11-16"

PAPER_UPDATES = {
 "as-good-as-it-gets-for-the-dollar-3-calls-for-fx": {
  "date": "2026-11-10",
  "title": "As good as it gets for the dollar: 3 calls for FX",
  "url": "https://think.ing.com/articles/as-good-as-it-gets-for-the-dollar-3-calls-for-fx/",
  "summary": "ING's 2027 FX outlook: dollar stays supported until next spring on hawkish Fed, then EUR/USD could recover towards 1.18 by year-end 2027 as US rates soften. Risky case: AI bust would push dollar lower (IMF estimates -6%). Bold case: eurozone growth surprise could lift EUR/USD; Japan growth surprises could weaken USD/JPY. French budgetary politics keep EUR risk premium into April elections.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "rates-on-the-brink-3-calls-for-rates": {
  "date": "2026-11-10",
  "title": "Rates on the brink: 3 calls for 2027",
  "url": "https://think.ing.com/articles/rates-on-the-brink-3-calls-for-rates/",
  "summary": "ING's 2027 rates outlook: upward pressure on long Treasury yields into early 2027, targeting 5.25-5.50%, before easing towards 4.50-4.75%. Euro 10yr swaps could push above 4% but end-2027 baseline at 2.5%. AI and fiscal risk are upside risks to yields. French spreads elevated into elections but offer post-election rally potential. Extreme case: official sector intervention could cap yields.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "the-commodities-feed-oil-retreats-on-easing-middle-east-tensions": {
  "date": "2026-11-10",
  "title": "The Commodities Feed: Oil slides on easing Middle East tensions",
  "url": "https://think.ing.com/articles/the-commodities-feed-oil-retreats-on-easing-middle-east-tensions/",
  "summary": "Brent fell below $92/bbl and WTI around $86/bbl as geopolitical risk premium unwinds. Persian Gulf crude exports at 80-85% of pre-war levels. Chinese crude imports up 13% MoM in October. Gold slipped below $4,100/oz on tighter rate expectations. European gas (TTF) around EUR81/MWh as tension ease reduces supply concerns.",
  "story_ids": ["oil-iran", "usd-rates-ai"]},
 "fx-daily-bearish-yield-curve-flattening-lifts-dollar": {
  "date": "2026-11-11",
  "title": "FX Daily: Bearish yield curve flattening lifts the dollar",
  "url": "https://think.ing.com/articles/fx-daily-bearish-yield-curve-flattening-lifts-dollar/",
  "summary": "Fed Governor Waller threatened a 50bp December hike if October CPI comes in hot - it did. Short-dated Treasury yields rose 20bp, 2-10y curve flattened 7bp. Dollar strong against activity currencies (NOK, SEK underperforming). EUR/USD holding at 1.11 but risks testing lower end of 1.10-1.15. USD/JPY could push through 159; investors may buy yen above 160.",
  "story_ids": ["usd-rates-ai"]},
 "rates-spark-back-to-a-5-10y-ust-on-inflation-fears": {
  "date": "2026-11-11",
  "title": "Rates Spark: Back to a 5% 10Y UST on inflation fears",
  "url": "https://think.ing.com/articles/rates-spark-back-to-a-5-10y-ust-on-inflation-fears/",
  "summary": "Hot US CPI (core 0.3% MoM) pushed 10Y UST back to 5%. Markets now pricing December hike fully (was 20bp before Waller's comments). Waller backed 25bp December hike and left 50bp on table. Energy costs falling (gasoline below $4/gallon) should give subdued November print. No further hikes expected in 2027 as rate-sensitive sectors cool.",
  "story_ids": ["usd-rates-ai"]},
 "the-commodities-feed-oil-rebounds-as-geopolitical-risks-linger": {
  "date": "2026-11-11",
  "title": "The Commodities Feed: Oil rebounds as geopolitical risks linger",
  "url": "https://think.ing.com/articles/the-commodities-feed-oil-rebounds-as-geopolitical-risks-linger/",
  "summary": "Oil edged higher after falling below $90/bbl. US crude inventories up 9m barrels (API), bearish for supply. EIA expects Middle East production outside Iran to recover to pre-conflict levels by mid-2027. Russian energy infrastructure damage from Ukrainian drone attacks adds uncertainty. Strait of Hormuz remains key driver. Gold recovered above $4,000/oz on physical demand.",
  "story_ids": ["oil-iran", "usd-rates-ai"]},
 "webinar-the-g10-fx-winners-and-losers-in-2027": {
  "date": "2026-11-11",
  "title": "Webinar: The G10 FX winners and losers in 2027",
  "url": "https://think.ing.com/articles/webinar-the-g10-fx-winners-and-losers-in-2027/",
  "summary": "ING webinar (16 Nov, 1400 GMT) with Chris Turner and Francesco Pesole on G10 FX outlook for 2027: Fed policy path, dollar trajectory, EUR/USD scenarios, and FX volatility outlook. Solid US growth, above-target inflation and hawkish Fed keeping dollar near year highs.",
  "story_ids": ["usd-rates-ai"]},
 "fx-daily-eur-usd-gears-up-for-a-110-test": {
  "date": "2026-11-12",
  "title": "FX Daily: EUR/USD gears up for a 1.10 test",
  "url": "https://think.ing.com/articles/fx-daily-eur-usd-gears-up-for-a-110-test/",
  "summary": "Hawkish Fedspeak and US CPI beat continue to support dollar. DXY back at April 2025 levels. EUR/USD at material risk of testing 1.100, which should offer solid support. Decisive move below 1.100 would require markets to seriously price 50bp December hike - seen as a stretch. ECB's Makhlouf called for caution, contrasting with Waller's hawkishness.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "rates-spark-inflation-pricing-sending-mixed-signals": {
  "date": "2026-11-12",
  "title": "Rates Spark: Inflation pricing sends mixed signals",
  "url": "https://think.ing.com/articles/rates-spark-inflation-pricing-sending-mixed-signals/",
  "summary": "Long-term inflation pricing not reflecting upside risks. 5Y5Y EUR inflation swap at 2.07% (near ECB target), US measures similarly low. Markets anxious about near-term surprises but view structural inflation benignly. Risk tilted to upside: low unemployment means wages can add to price pressures; high government debt makes sustained high rates difficult. Central banks may tolerate higher inflation.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "asia-fx-outlook-2027-rotation-underway-but-tech-currencies-should-lead": {
  "date": "2026-11-12",
  "title": "Asia FX Outlook 2027: Rotation underway but tech currencies should lead",
  "url": "https://think.ing.com/articles/asia-fx-outlook-2027-rotation-underway-but-tech-currencies-should-lead/",
  "summary": "Asian FX mixed in 2026: AI-linked currencies (KRW, CNY, SGD, MYR) outperformed, while INR, IDR, PHP weakened >5%. Softer dollar should tailwind Asian FX in 2027. KRW, CNY, SGD expected to outperform; PHP, IDR face downside. CNY steady appreciation with two-way risks. TWD could recover to 31.5 by end-2027 on AI capex.",
  "story_ids": ["usd-rates-ai"]},
 "emea-fx-outlook-2027": {
  "date": "2026-11-12",
  "title": "EMEA FX Outlook 2027: Restrictive policy remains the key FX anchor",
  "url": "https://think.ing.com/articles/emea-fx-outlook-2027/",
  "summary": "EMEA central banks focused on currency stability amid inflation, fiscal risks and geopolitics. HUF preferred CEE currency (NBH keeping rates at 5.50%). PLN turned negative on narrower differentials and fiscal concerns. ZAR supported by hawkish SARB. Turkish lira offering attractive carry despite depreciation. French fiscal concerns remain key risk for euro.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "fx-outlook-2027-our-latest-forecasts": {
  "date": "2026-11-12",
  "title": "FX Outlook 2027: Our latest forecasts",
  "url": "https://think.ing.com/articles/fx-outlook-2027-our-latest-forecasts/",
  "summary": "ING's latest 2027 FX forecasts across G10 and emerging markets. Dollar 'up then down' baseline: hawkish through Q1 2027, then lower as inflation falls to 2%. EUR/USD ending 2027 at 1.18. EUR/GBP, USD/JPY and other major pairs forecast. French elections key risk for euro.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "fx-outlook-2027-seven-key-calls": {
  "date": "2026-11-12",
  "title": "FX Outlook 2027: Seven key calls",
  "url": "https://think.ing.com/articles/fx-outlook-2027-seven-key-calls/",
  "summary": "Seven key FX calls for 2027: JPY best risk/reward (undervalued, limited dovish repricing risk); CHF as SNB turns pro-franc; NZD high-beta gamble; HUF attractive carry; Asia rotation to tech currencies (KRW, TWD); MXN vulnerable (Banxico dovish); BRL can recover on fiscal consolidation. FX volatility expected to stay low.",
  "story_ids": ["usd-rates-ai"]},
 "fx-outlook-2027-seven-key-risks": {
  "date": "2026-11-12",
  "title": "FX Outlook 2027: Seven key risks",
  "url": "https://think.ing.com/articles/fx-outlook-2027-seven-key-risks/",
  "summary": "Seven key risks for 2027 FX: AI bust (dollar initially up, then down; JPY/CHF/EUR outperform); inflation 2022 replay (broad dollar gains); fiscal debasement trade; end of carry trade (yen/CHF positive); geopolitical blowout on three fronts (dollar winner in all scenarios); fiscal dominance; and French political risk.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "fx-volatility-in-2027-in-need-of-shock-therapy": {
  "date": "2026-11-12",
  "title": "FX Volatility in 2027: In need of shock therapy",
  "url": "https://think.ing.com/articles/fx-volatility-in-2027-in-need-of-shock-therapy/",
  "summary": "FX volatility expected to stay low in 2027. Markets have consistently overestimated volatility. Structural factors: huge growth in financial assets bringing liquidity, greater use of FX pricing algos. Fat tail risks (Liberation Day tariffs, Iran war start) can cause sudden liquidity drops but bar for raising volatility is high.",
  "story_ids": ["usd-rates-ai"]},
 "g10-fx-outlook-2027": {
  "date": "2026-11-12",
  "title": "G10 FX Outlook 2027: It's hard to look beyond the Fed",
  "url": "https://think.ing.com/articles/g10-fx-outlook-2027/",
  "summary": "Fed not turning dovish; one 25bp December hike seen concluding recalibration. 'Up then down' dollar baseline: dollar turns lower in Q2 2027 as inflation falls to 2%. EUR/USD ending 2027 at 1.18. ECB final hike in December to 2.75%. AI story and geopolitical/energy are the two key drivers beyond central bank reactions.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "latam-fx-outlook-2027": {
  "date": "2026-11-12",
  "title": "Latam FX Outlook 2027",
  "url": "https://think.ing.com/articles/latam-fx-outlook-2027/",
  "summary": "Banxico's dovish stance stands out (cut to 6.25%, peso vulnerable). Brazilian real can recover on fiscal consolidation and high real rates. MXN relative underperformer in 2027. Central bank policy more important than ever for EM currencies.",
  "story_ids": ["usd-rates-ai"]},
 "the-commodities-feed-stronger-dollar-weighs-on-commodities": {
  "date": "2026-11-12",
  "title": "The Commodities Feed: Stronger dollar weighs on commodities",
  "url": "https://think.ing.com/articles/the-commodities-feed-stronger-dollar-weighs-on-commodities/",
  "summary": "Oil slips as Middle East output rebounds; Brent around $91/bbl. OPEC crude production up almost 2m b/d in October to 27.16m b/d, led by Saudi Arabia, Iraq and Kuwait. Regional crude flows approaching pre-war levels but exports rely on alternative routes around Strait of Hormuz. Copper drops to four-month low on tech stock selling and firmer dollar. Gold extends decline below $4,000/oz on stronger US inflation data and hawkish Fed comments.",
  "story_ids": ["oil-iran", "usd-rates-ai"]},
 "fx-daily-dont-mess-with-the-dollar": {
  "date": "2026-11-13",
  "title": "FX Daily: Don't mess with the dollar near term",
  "url": "https://think.ing.com/articles/fx-daily-dont-mess-with-the-dollar/",
  "summary": "Powerful macro-driven dollar rally this week. Short-dated US yields ~40bp higher since Waller's 50bp December hike comment. Market pricing back-to-back December and January hikes (~85bp total tightening). DXY broke to new year high, targeting 104.60 (EUR/USD ~1.0880). ECB struggling to outhawk the Fed. EUR/USD break below 1.10 at risk into year-end.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "rates-spark-higher-rates-amid-a-fragile-calm": {
  "date": "2026-11-13",
  "title": "Rates Spark: Higher rates amid a fragile calm",
  "url": "https://think.ing.com/articles/rates-spark-higher-rates-amid-a-fragile-calm/",
  "summary": "Tactically bearish on rates. 2yr USD swap up ~12bp. AI event risk ahead: Anthropic IPO pricing and NVIDIA Q3 results next week. EUR swap curve prices optimistic ECB terminal rate above 3% - can only hold if growth outlook improves. French OAT/Bund back towards 150bp. Lagarde polling at 14%, Le Pen and Mélenchon in runoff.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
 "fx-daily-time-for-a-break-below-110-in-eur-usd": {
  "date": "2026-11-16",
  "title": "FX Daily: Time for a break below 1.10 in EUR/USD?",
  "url": "https://think.ing.com/articles/fx-daily-time-for-a-break-below-110-in-eur-usd/",
  "summary": "Two-year USD swap rates up 35bp since Waller's 50bp comment and hot core CPI. Market pricing back-to-back 25bp hikes in December and January - harder for moderate FOMC members to push back against. Dollar corrections likely to be faded. EUR/USD can hold 1.100 this week but break lower risks significant. EUR/USD 2y swap differential widest since September 2025.",
  "story_ids": ["usd-rates-ai", "france-ecb"]},
}

PROB = {
 "france-ecb": {
  "Contained, grinding stress": (58, "ECB succession uncertainty (de Cos dove vs Knot hawk), French polls showing Le Pen/Mélenchon runoff with Lagarde at only 14%, EUR/USD testing 1.10. Cut 62 -> 58."),
  "French relief": (6, "Softened 9 -> 6: no French budget clarity; elections approaching with tail risks."),
  "Contagion and ECB backstop": (27, "Raised 25 -> 27: eurozone fiscal concerns spreading beyond France; OAT/Bund back towards 150bp; ECB support sequence must survive leadership change."),
  "Disorderly sovereign event": (9, "Raised 8 -> 9: French political fragmentation with no clear majority; Lagarde resignation adds succession overhang into April 2027 elections."),
 },
 "oil-iran": {
  "Elevated premium, no major disruption": (31, "Cut 34 -> 31: Brent below $92 then rebounding on geopolitical risks; Persian Gulf flows at 80-85% of pre-war."),
  "De-escalation": (35, "Raised 34 -> 35: regional flows recovering, Iranian position softening on Strait of Hormuz, OPEC production up 2m b/d in October."),
  "Re-escalation, flows threatened": (28, "Cut 29 -> 28: risks persist but no new escalation; Strait of Hormuz remains key vulnerability."),
  "Major supply outage": (6, "Unchanged at 6: no new supply disruption evidence."),
 },
 "usd-rates-ai": {
  "Choppy around 5%, Dec hike alive": (32, "Cut 35 -> 32: strong payrolls (165k) and hot CPI expectations shift weight toward sustained hawkish path."),
  "Yields back above 5%, hawkish Fed": (40, "Raised 36 -> 40: October CPI expected at 0.3% MoM headline and core; December hike 19bp priced; dollar resilient despite tech selloff."),
  "AI-led risk-off and growth scare": (23, "Cut 24 -> 23: tech selloff was significant but FX markets shrugged it off; AI stocks recovering."),
  "Disorderly bond/equity break": (5, "Unchanged at 5: no disorderly market signals."),
 },
}

STORY_TEXT = {
 "france-ecb": "The ECB held on 29 Oct and kept a December hike in play. Lagarde announced she steps down on 7 February 2027, polling at only 14% in French presidential polls, with Le Pen and Mélenchon favoured for the runoff. The ECB support sequence (verbal softening, then a QT pause, then TPI) must survive a leadership change. French spreads elevated into April elections; OAT/Bund back towards 150bp. Contagion risk rising as fiscal concerns spread beyond France.",
 "oil-iran": "Brent slid below $92/bbl on easing Middle East tensions then rebounded slightly. Persian Gulf crude exports at 80-85% of pre-war levels; OPEC production up 2m b/d in October. De-escalation channels emerging but Strait of Hormuz remains vulnerable. Gold around $4,000-4,100/oz supported by central bank buying and geopolitical uncertainty.",
 "usd-rates-ai": "The Fed held at 3.75-4.00% but Governor Waller opened the door to a 50bp December hike if CPI stays hot. October CPI printed 0.3% MoM core, annualising well above 3%. Markets now fully pricing December hike; Fed funds futures favour back-to-back 25bp increases in December and January. 10Y Treasury back at 5%, DXY near 103. Short-dated yields up ~40bp since Waller's comments. AI event risk (Anthropic IPO, NVIDIA earnings) remains the main counterweight to dollar strength.",
}

CHANGES = [
 "Nov 10: ING 2027 FX outlook - dollar supported until spring on hawkish Fed, EUR/USD towards 1.18 by year-end. ING rates outlook - upward pressure on long yields into early 2027, targeting 5.25-5.50%.",
 "Nov 10: Oil slides below $92/bbl on easing Middle East tensions; Persian Gulf flows at 80-85% of pre-war.",
 "Nov 11: Waller threatens 50bp December hike if CPI hot - it prints 0.3% MoM core. 10Y back to 5%; markets fully pricing December hike. Dollar strong, DXY targeting 103.",
 "Nov 11: Oil rebounds on lingering geopolitical risks; Strait of Hormuz remains key driver despite Gulf flow recovery.",
 "Nov 12: EUR/USD at risk of testing 1.100 on hawkish Fed/ECB divergence. Long-term inflation pricing seen as too benign; risk tilted to upside.",
 "Nov 12: G10 FX Outlook 2027 - 'up then down' dollar baseline, one 25bp December hike, EUR/USD ending 2027 at 1.18. EUR/USD scenarios: bullish 1.13-1.18 range through 2027.",
 "Nov 12: FX Outlook seven key risks - AI bust, inflation replay, fiscal debasement, end of carry trade, geopolitical blowout - dollar winner in most scenarios.",
 "Nov 13: Dollar rally extends - DXY breaks to new year high targeting 104.60. Markets pricing back-to-back December/January hikes (~85bp total). EUR/USD break below 1.10 at risk.",
 "Nov 13: Rates tactically bearish; AI event risk (Anthropic IPO, NVIDIA earnings) next week. French OAT/Bund back towards 150bp; Lagarde polling at 14%.",
 "Nov 16: Dollar corrections likely to be faded; market pricing back-to-back 25bp December/January hikes. EUR/USD can hold 1.100 this week but break lower risks significant.",
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
