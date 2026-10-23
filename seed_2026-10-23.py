"""Batch 1 (2026-10-23): analysis of four ING THINK articles. Probabilities are my own judgement."""
import store

D = "2026-10-23"
N = "Initial estimate (analyst judgement, not ING's)"


def sc(name, typ, prob, desc, triggers, fx):
    return {"name": name, "type": typ, "probability": prob, "description": desc,
            "triggers": triggers, "fx_impact": fx,
            "history": [{"date": D, "probability": prob, "note": N}]}


state = {
 "papers": [
  {"id": "ecb-french-drama", "date": "2026-10-22", "title": "ECB caught in the French drama (Carsten Brzeski)",
   "url": "https://think.ing.com/articles/ecb-caught-in-the-french-drama/",
   "summary": "ECB expected on hold on 29 Oct. The jump in bond yields after the French crisis already tightens policy: German yields ~ a 25bp hike, France ~ 50bp. Next hike decision pushed to December (new projections). Path depends on Middle East war length, energy pass-through, and French contagion. Defences: dovish rates, flexible reinvestment (pause QT), then TPI, which is hard to justify while France is non-compliant with fiscal rules.",
   "story_ids": ["france-ecb", "oil-iran"]},
  {"id": "fx-daily-safe-haven", "date": "2026-10-23", "title": "FX Daily: Dollar has lost its safe-haven crown",
   "url": "https://think.ing.com/articles/fx-daily-dollar-has-lost-its-safe-haven-crown/",
   "summary": "Equities sold off on oil and AI worries; JPY and CHF were the safe-haven winners, not USD. Bond/equity negative correlation is back. UST 10y below 5%, 2y SOFR swap -15bp to 4.50%, but the bar to price out a December Fed hike is high. OAT-Bund 10y at 174bp (peak 178bp); EUR sensitivity to France can return quickly. CEE hit by risk-off (PLN, HUF vulnerable; EUR/HUF capped 368-370). MXN -8% since early Sept; Banxico dovish; USD/MXN 19.00-19.10 trajectory.",
   "story_ids": ["usd-rates-ai", "france-ecb", "em-fx"]},
  {"id": "rates-spark-5pct", "date": "2026-10-22", "title": "Rates Spark: US and France like ships passing in the night at 5%",
   "url": "https://think.ing.com/articles/rates-spark-us-and-france-like-ships-passing-in-the-night-at-5/",
   "summary": "UST 10y broke below 5% on risk-off; ING expects it to revert above 5% (inflation, deficits, AI boom, US midterms), timing uncertain. French 10y above 5%, spread ~175bp vs Germany. Moody's (Aa3 negative) downgrade looks overdue, no fixed release time. A lasting French relief needs a credible 2027 budget, possibly not before December. Weak PMIs could trigger a bullish rates repricing and a more dovish ECB.",
   "story_ids": ["usd-rates-ai", "france-ecb"]},
  {"id": "commodities-brent", "date": "2026-10-23", "title": "The Commodities Feed: Brent builds geopolitical premium as Gulf risks rise",
   "url": "https://think.ing.com/articles/the-commodities-feed-brent-risk-premium-builds-with-fears-of-re-escalation/",
   "summary": "Brent +4% to just above $113/bbl on fears of renewed US-Iran escalation (reported strike consideration, second carrier, troop evacuations). ING's 4Q26 $80 average now looks unattainable; re-escalation seen as most likely path. TTF above EUR90/MWh (highest since Dec 2022); LNG largely absent this winter. Gold -2.8% toward $4,000 on inflation/policy worries; copper down on rising inventories and AI-stock selloff.",
   "story_ids": ["oil-iran", "usd-rates-ai"]},
 ],
 "stories": [
  {"id": "france-ecb", "name": "French fiscal crisis and the ECB", "category": "Europe", "updated": D,
   "summary": "French yields above 5% and OAT-Bund spread at ~175bp are doing the ECB's tightening for it. ECB should hold on 29 Oct and hint dovishly; a Moody's downgrade is pending. The key question is whether this stays a French problem or spreads to the eurozone and forces ECB support (QT pause, then TPI).",
   "pairs": ["EURUSD", "EURCHF", "EURJPY", "EURGBP"], "paper_ids": ["ecb-french-drama", "fx-daily-safe-haven", "rates-spark-5pct"],
   "scenarios": [
    sc("Contained, grinding stress", "base", 55, "Spreads stay 150-180bp, Moody's downgrade is absorbed, ECB holds in Oct and stays cautious in Dec. No TPI.",
       ["Moody's decision", "ECB 29 Oct tone", "OAT-Bund spread"], "EUR range-bound with a downside skew; the EUR/France correlation spikes on bad days."),
    sc("French relief", "bull", 15, "Credible 2027 budget with real consolidation and calmer risk sentiment; spreads retrace.",
       ["Budget adoption", "Political stability"], "EUR supported; ECB hike pricing returns, positive for EURUSD."),
    sc("Contagion and ECB backstop", "bear", 25, "Spreads blow out past 180bp, Italy/Spain widen, ECB pauses QT or reinvests flexibly, and TPI becomes live (possibly excluding France).",
       ["Spread above 180bp", "Italian/Spanish spreads", "ECB QT language"], "EUR weaker; safe-haven bid for CHF/JPY; Bunds rally."),
    sc("Disorderly sovereign event", "tail", 5, "Failed auctions or a multi-notch downgrade cascade force emergency policy action.",
       ["Auction failures", "Multiple downgrades"], "Sharp EUR sell-off, strong CHF.")]},
  {"id": "oil-iran", "name": "Oil shock and US-Iran re-escalation", "category": "Geopolitics / Commodities", "updated": D,
   "summary": "Brent at ~$113 carries a growing Gulf risk premium; ING now sees re-escalation as the likeliest path, which breaks its $80 4Q26 call. Energy prices drive ECB and Fed hike odds, European gas (TTF above EUR90) and inflation.",
   "pairs": ["USDCAD", "USDNOK", "EURUSD", "USDJPY", "XAUUSD"], "paper_ids": ["commodities-brent", "ecb-french-drama"],
   "scenarios": [
    sc("Elevated premium, no major disruption", "base", 40, "Brent stays $100-120 on threats and military build-up, with flows still intact.",
       ["Gulf shipping flows", "US statements"], "CAD/NOK supported; JPY and EUR pressured by terms of trade."),
    sc("De-escalation", "bull", 15, "Diplomacy or the midterm effect calms tensions; the premium unwinds and Brent heads toward $90.",
       ["Talks announced", "Carrier withdrawal"], "Oil FX fades; EUR and JPY relief; lower hike pricing."),
    sc("Re-escalation, flows threatened", "bear", 38, "US strikes on Iran and disruption risk; Brent above $120, gas spikes further.",
       ["US strikes", "Hormuz incidents", "Troop evacuations"], "USD mixed (haven demand weak); JPY/CHF and CAD/NOK strongest; EUR hit by energy."),
    sc("Major supply outage", "tail", 7, "Actual loss of Gulf flows; Brent far above $130.",
       ["Tanker attacks", "Facility damage"], "Severe risk-off; CHF/JPY surge; EM FX sells off.")]},
  {"id": "usd-rates-ai", "name": "US rates, Fed hike risk and AI-valuation wobble", "category": "US / Rates", "updated": D,
   "summary": "UST 10y slipped under 5% as AI worries and risk-off reasserted bond/equity inverse correlation. USD lost safe-haven status (JPY/CHF won). ING expects 10y to revert above 5%, and a December Fed hike is still not priced out. Gold falls on inflation/policy fears.",
   "pairs": ["USDJPY", "USDCHF", "EURUSD", "XAUUSD"], "paper_ids": ["fx-daily-safe-haven", "rates-spark-5pct", "commodities-brent"],
   "scenarios": [
    sc("Choppy around 5%, Dec hike alive", "base", 45, "10y oscillates around 5%, USD consolidates if risk calms; JPY/CHF keep a haven bid on sell-offs.",
       ["US PMIs", "CPI", "Equity/AI moves"], "USD range-trade; USDJPY and USDCHF downside on risk-off days."),
    sc("Yields back above 5%, hawkish Fed", "bull", 25, "Inflation, deficits and oil push yields up; December hike priced in; USD rebounds.",
       ["Hot CPI", "Fed speakers", "Midterm fiscal worries"], "USD up broadly; USDJPY higher; gold under pressure."),
    sc("AI-led risk-off and growth scare", "bear", 25, "Equity sell-off deepens and data weaken; hike pricing collapses; yields fall sharply.",
       ["Weak PMIs", "AI stock drawdown"], "JPY and CHF rally; USD weaker; EM FX sells off."),
    sc("Disorderly bond/equity break", "tail", 5, "Disorderly Treasury/equity move forces central bank response.",
       ["Failed auctions", "Credit spreads"], "Extreme haven flows; thin liquidity.")]},
  {"id": "em-fx", "name": "EM and CEE FX under pressure", "category": "Emerging markets", "updated": D,
   "summary": "MXN is worst EM performer (-8% since early Sept) on dovish Banxico and US-rate shock; RON next (-4%). PLN and HUF are vulnerable to energy-import costs and non-hawkish central banks; EUR/HUF capped at 368-370.",
   "pairs": ["USDMXN", "EURPLN", "EURHUF", "EURRON"], "paper_ids": ["fx-daily-safe-haven"],
   "scenarios": [
    sc("Persistent weakness", "base", 50, "Banxico stays dovish on 5 Nov; USD/MXN 19.00-19.10; PLN/HUF drift weaker with energy.",
       ["Banxico 5 Nov", "Oil", "Fed pricing"], "USDMXN up, EURPLN up, EURHUF capped."),
    sc("Relief rally", "bull", 20, "Banxico hawkish surprise or oil/risk calm.", ["Banxico hawkish", "Lower oil"], "MXN and CEE recover."),
    sc("Deeper sell-off", "bear", 25, "Global risk-off and AI unrest, with Mexico's US-securities exposure adding outflows.",
       ["Equity sell-off", "Oil spike"], "USDMXN breaks higher; EURPLN up."),
    sc("EM funding stress", "tail", 5, "Broad EM outflows.", ["Spreads", "Dollar funding"], "Sharp EM FX gaps.")]},
 ],
 "changelog": [{"date": D, "text": "Batch 1: four ING articles (22-23 Oct 2026) analysed; four stories created. Probabilities are initial estimates."}],
}

if __name__ == "__main__":
    store.save(state)
    print(store.validate(state) or "valid")
