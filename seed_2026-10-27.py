"""Batch 2 (week of 2026-10-26): three new ING articles. Updates batch 1 stories,
removes the 'EM and CEE FX under pressure' story, logs what changed."""
import store

D = "2026-10-27"  # article days inferred from 'Today'/'Yesterday' labels
NEW = {
 "ecb-cheat-sheet": {"date": "2026-10-26", "title": "October ECB cheat sheet: French malaise shouldn't prompt a dovish turn",
  "url": "https://think.ing.com/articles/october-ecb-cheat-sheet-french-malaise-shouldnt-prompt-a-dovish-turn/",
  "summary": "ECB expected to hold at 2.5% on 29 Oct and keep the door open for a December hike, with a neutral, balanced message; a hike this week is priced near zero. Markets look for signs the French turmoil has triggered a dovish rethink - ING says not yet. EUR undervalued 1-1.5% vs short-term fair value; balance of risks still to the downside, but baseline is a broadly stable euro. ING preference: EUR/USD back to 1.120-1.130 in coming weeks. A surprise hike would risk a broader risk-off move, wider OAT spreads, lower equities and even lower Bund yields."},
 "fx-daily-dollar-buying": {"date": "2026-10-27", "title": "FX Daily: Dollar buying returns ahead of FOMC",
  "url": "https://think.ing.com/articles/fx-daily-dollar-buying-returns-ahead-of-fomc/",
  "summary": "Dollar firmer at the start of the week as AI-related sentiment stabilises and markets position ahead of the FOMC; Chair Kevin Warsh reiterating inflation commitments reinforces the structural dollar floor. ING expects a broadly supported dollar this week. US consumer confidence seen at 81.5 (consensus 81.0) after 81.9 in September - soft data could dent hike pricing. Israeli election is tight; both Netanyahu and Eisenkot blocs short of a majority, Eisenkot marginally more diplomatic on Iran. RBNZ expected to deliver a hawkish 25bp hike; NZD/USD 0.570 4Q forecast. CEE rates reconnecting with higher energy prices; CEE FX downside risk exceeds upside."},
 "rates-spark-relief": {"date": "2026-10-26", "title": "Rates Spark: Temporary relief for structural problems",
  "url": "https://think.ing.com/articles/rates-spark-temporary-relief-for-structural-problems/",
  "summary": "Moody's kept France at double-A (negative outlook), so the 10y OAT-Bund spread narrowed more than 10bp to below 155bp after being at its widest since 2011. Relief only - France still needs a significant, sustained fiscal effort, politics stay fragmented, elections are in April 2027, and a tail risk is support for Melenchon. For the ECB, the retightening removes some pressure to hike and lets officials keep constructive ambiguity. Elevated energy and resilient data outside France keep hawkish pressure on front-end rates."},
}

PROB = {
 "france-ecb": {"Contained, grinding stress": (62, "Moody's kept France at AA on 26 Oct; OAT-Bund narrowed to <155bp. Near-term downgrade trigger removed, structural problems unchanged."),
                "French relief": (13, "Much of the relief already happened via the spread tightening; a lasting move needs a credible 2027 budget."),
                "Contagion and ECB backstop": (20, "Spreads off their peak, but ING still sees wider spreads ahead and won't call the end of the turmoil."),
                "Disorderly sovereign event": (5, "Unchanged: April 2027 elections and a Melenchon tail keep the risk alive.")},
 "oil-iran": {"Elevated premium, no major disruption": (40, "No new oil paper this week; ING still flags high energy prices as a core driver."),
             "De-escalation": (18, "New: today's Israeli election could reset the Middle East equilibrium - Eisenkot is seen as more diplomatic on Iran."),
             "Re-escalation, flows threatened": (36, "Upgrades from 38 to 36: still the dominant risk, but the election adds a political off-ramp."),
             "Major supply outage": (6, "Trimmed slightly: flows remain intact and no new escalation headlines.")},
 "usd-rates-ai": {"Choppy around 5%, Dec hike alive": (43, "AI sentiment stabilised; dollar reconnecting with the hawkish Fed backdrop."),
                 "Yields back above 5%, hawkish Fed": (30, "Raised: ING now expects a broadly supported dollar this week into the FOMC, with Warsh stressing inflation commitments."),
                 "AI-led risk-off and growth scare": (22, "Lowered from 25: the AI-driven risk-off impulse that dominated last week has faded for now."),
                 "Disorderly bond/equity break": (5, "Unchanged.")},
}

STORY_TEXT = {
 "france-ecb": {"summary": "Moody's kept France at AA with a negative outlook, and the OAT-Bund spread narrowed to below 155bp from an 11-year wide. That is relief, not resolution: France still needs a sustained fiscal effort, elections are in April 2027, and Melenchon is a tail risk. The ECB is expected to hold at 2.5% on 29 Oct and keep a December hike on the table, which shelters EUR. ING's preference is EUR/USD back to 1.120-1.130."},
 "oil-iran": {"summary": "Brent above $113 still carries a large Gulf risk premium and ING's $80 4Q26 call is gone. No new oil note this week, but ING calls high energy prices a core driver of rates and inflation. Today's Israeli election is a new political variable: Eisenkot is seen as slightly softer on Iran than Netanyahu, so a workable coalition is the main de-escalation channel alongside diplomacy."},
 "usd-rates-ai": {"summary": "The dollar has regained support as AI-related sentiment stabilises and markets position for the FOMC: Chair Warsh's restated inflation commitment is treated as a structural floor for USD, and ING expects a broadly supported dollar this week. Soft consumer confidence (81.5 expected after 81.9) is the main data risk to tightening expectations. JPY/CHF keep their haven role on risk-off days."},
}

CHANGES = [
 "France: Moody's kept France at double-A (negative outlook) instead of downgrading; OAT-Bund tightened >10bp to <155bp from an 11-year wide. Contained-stress probability raised 55% -> 62%, contagion cut 25% -> 20%, relief cut 15% -> 13%.",
 "ECB: the 29 Oct meeting is now framed as a hold at 2.5% with the door open for December, not a debate about hiking now. Baseline is a neutral message and a broadly stable euro, with EUR/USD targeted at 1.120-1.130.",
 "USD: the narrative flipped this week. Last week the dollar had 'lost its safe-haven crown'; now stabilising AI sentiment and pre-FOMC positioning have brought dollar buying back. Hawkish-Fed scenario raised 25% -> 30%, AI risk-off cut 25% -> 22%.",
 "Oil: no new commodity note, but the Israeli election is a fresh de-escalation channel (Eisenkot softer on Iran than Netanyahu). De-escalation 15% -> 18%, re-escalation 38% -> 36%, supply outage 7% -> 6%.",
 "Removed the 'EM and CEE FX under pressure' story at your request. The source detail (MXN, PLN, HUF, RON) is still recorded inside the papers, and ING still flags CEE FX downside risk in this week's FX Daily.",
 "Still open: FOMC tomorrow, ECB on 29 Oct, RBNZ (hawkish 25bp expected), US consumer confidence today.",
]


def apply(state):
    for pid, p in NEW.items():
        p["id"] = pid
        p["story_ids"] = {"ecb-cheat-sheet": ["france-ecb", "usd-rates-ai"],
                         "fx-daily-dollar-buying": ["usd-rates-ai", "oil-iran"],
                         "rates-spark-relief": ["france-ecb", "usd-rates-ai"]}[pid]
        state["papers"].append(p)

    state["stories"] = [s for s in state["stories"] if s["id"] != "em-fx"]
    for p in state["papers"]:
        p["story_ids"] = [x for x in p.get("story_ids", []) if x != "em-fx"]

    for s in state["stories"]:
        s["updated"] = D
        s["summary"] = STORY_TEXT[s["id"]]["summary"]
        s["paper_ids"] = [p["id"] for p in state["papers"] if s["id"] in p["story_ids"]]
        for sc in s["scenarios"]:
            prob, note = PROB[s["id"]][sc["name"]]
            store.set_probability(state, s["id"], sc["name"], prob, note, D)

    for s in state["stories"]:
        for sc in s["scenarios"]:
            if sc["name"] == "Contained, grinding stress":
                sc["triggers"] = ["OAT-Bund spread", "April 2027 elections", "ECB 29 Oct tone"]
                sc["description"] = "Spreads hold roughly 145-175bp after the Moody's relief, budget talks drag on and the ECB holds at 2.5% with a neutral message. No TPI."
            if sc["name"] == "Choppy around 5%, Dec hike alive":
                sc["triggers"] = ["FOMC", "US consumer confidence", "AI equity moves"]

    for c in CHANGES:
        state["changelog"].append({"date": D, "text": c})


if __name__ == "__main__":
    st = store.load()
    apply(st)
    store.save(st)
    print(store.validate(st) or "valid")
