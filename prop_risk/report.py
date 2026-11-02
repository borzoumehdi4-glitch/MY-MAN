"""Builds the account-management decision tables.

Run:  python3 prop_risk/report.py            (full report, ~1-2 min)
      python3 prop_risk/report.py --quick    (smaller Monte-Carlo, ~20 s)

Nothing here is tuned to a preferred answer: every table is produced by the
rules engine, so if a rule I had to guess is wrong, change portfolio.py and the
ranking changes with it.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import portfolio as pf  # noqa: E402
import sim  # noqa: E402

QUICK = "--quick" in sys.argv
N_SINGLE = 4000 if QUICK else 8000
N_PORT = 2500 if QUICK else 6000
SEED = 20261


def rule(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def constraints_table(accts) -> None:
    rule("1. WHAT EACH ACCOUNT ACTUALLY IS  (the ratio decides everything)")
    print(
        f"{'':4}{'account':38}{'bal':>7}{'floor':>8}{'need':>7}{'cush':>7}{'r':>6}"
        f"{'shots':>7}"
    )
    for a in accts:
        r = a.ratio
        tag = "OK" if r >= 2 else ("MARGINAL" if r >= 1 else "LOTTERY")
        shots = a.cushion / a.min_risk if a.min_risk else float("nan")
        print(
            f"{a.key:4}{a.name:38}{a.start:7.0f}{a.floor:8.0f}{a.need:7.0f}"
            f"{a.cushion:7.0f}{r:6.2f}{shots:7.1f}  {tag}"
        )
    print()
    print("  need  = USD of profit to the next payout / pass")
    print("  cush  = USD of loss before the account is dead")
    print("  r     = cush / need.  r>=2 comfortable | r~1 a coin flip | r<1 a lottery")
    print("  shots = how many MINIMUM-SIZE trades fit in the cushion (0.01 lot).")
    print("          This is the number that actually kills tight-DD accounts:")
    print("          below ~6 shots the rules have decided, not your win rate.")


def sizing_sweep(accts, strat, credit: dict) -> dict:
    """Sweep risk = fraction of the remaining cushion, per account."""
    rule("2. POSITION SIZING: what fraction of your remaining rope per trade?")
    best = {}
    for a in accts:
        print()
        print(f"--- {a.key}: {a.name}")
        print(f"    need {a.need:.0f} | cushion {a.cushion:.0f} | min lot risk "
              f"{a.min_risk:.0f} ({a.cushion / a.min_risk:.1f} shots)")
        print(
            f"{'frac':>6}{'risk$':>7}{'eff$':>7}{'%bal':>7}{'R/tgt':>7}"
            f"{'P(ok)':>7}{'P(dead)':>9}{'pays':>6}{'1st wks':>8}{'value$':>8}"
        )
        rows = []
        for frac in (0.05, 0.10, 0.15, 0.20, 0.30, 0.50, 0.75, 1.00):
            risk = a.cushion * frac
            st = sim.simulate_account(
                a, risk, strat, n_paths=N_SINGLE, seed=SEED,
                cushion_guard=4.0, min_risk=a.min_risk,
            )
            med = st["median_trades_to_pass"]
            med_wk = med / strat.trades_per_week if med else float("nan")
            # challenge passes are worth the funded account they convert into
            value = (
                st["p_pass"] * credit.get(a.key, 0.0)
                if a.mode == "challenge"
                else st["cash_per_path"]
            )
            clamp = " *" if risk < a.min_risk else ""
            rows.append((frac, st, value))
            print(
                f"{frac:6.2f}{risk:7.1f}{st['risk_eff']:6.1f}{clamp}"
                f"{100 * st['risk_eff'] / a.start:7.2f}{a.need / st['risk_eff']:7.1f}"
                f"{st['p_success']:7.2f}{st['p_bust']:9.2f}"
                f"{st['payouts_per_path']:6.2f}{med_wk:8.1f}{value:8.0f}"
            )
        best[a.key] = max(rows, key=lambda t: t[2])
    print()
    print("  frac = risk / remaining cushion | eff$ = risk after the min-lot clamp")
    print("  P(ok)= pass (A1) or first payout (A2/A3) | value$ = cash over 52 weeks,")
    print("         with an A1 pass credited at its funded-account value")
    print("  ' *' = the minimum lot is bigger than the requested risk, so that row")
    print("        is not actually available to you -- the account cannot be sized down")
    for a in accts:
        frac, st, value = best[a.key]
        print(
            f"    {a.key} best: frac {frac:.2f} -> risk {st['risk_eff']:.1f} USD "
            f"({100 * st['risk_eff'] / a.start:.2f}% of balance, "
            f"{a.need / st['risk_eff']:.1f}R to target), P(ok) {st['p_success']:.2f}, "
            f"P(dead) {st['p_bust']:.2f}, value {value:.0f} USD/yr"
        )
    return best


def rule_uncertainty(strat) -> None:
    """The rules I had to guess, and how much they change the answer."""
    rule("3. THE RULES I GUESSED -- and the two that decide A2's fate")
    print("\n  A2, 1.5% drawdown: does a payout re-base the trail?")
    print("  (i.e. after you take 30 USD at 1030, is your floor 985 again, or")
    print("   does it stay at the 1015 high-water mark?)")
    print(f"{'variant':>34}{'risk$':>7}{'P(pay)':>8}{'pays':>7}{'cash$':>8}"
          f"{'P(dead)':>9}")
    a_noreset = pf.a2_funded_tight()
    a_noreset.reset_on_withdrawal = False
    a_noreset.min_buffer = 0.0  # take everything you legally can, floor stays put
    variants = [
        ("trail, payout re-bases", pf.a2_funded_tight(), 4.0, 4.0),
        ("trail, floor never moves down", a_noreset, 4.0, 4.0),
        ("static floor 985 (no trail)", pf.a2_funded_tight(trailing=False), 4.0, 4.0),
        ("trail, re-bases, no de-risking", pf.a2_funded_tight(), 12.0, None),
    ]
    for label, acct, risk, guard in variants:
        st = sim.simulate_account(acct, risk, strat, n_paths=N_SINGLE, seed=SEED,
                                  cushion_guard=guard, min_risk=acct.min_risk)
        print(f"{label:>34}{st['risk_eff']:7.1f}{st['p_payout']:8.2f}"
              f"{st['payouts_per_path']:7.2f}{st['cash_per_path']:8.0f}"
              f"{st['p_bust']:9.2f}")
    print("  Under the strict reading (floor never moves down) you can never take")
    print("  the full 30: at 1030 you are only 15 above the floor, so the payout")
    print("  you can actually book is ~15, and then you are at the wall.")

    print("\n  A3 after the lock at 3000: what do you leave in the account?")
    print(f"{'withdraw down to':>20}{'buffer':>8}{'cash$':>9}{'P(dead)':>9}")
    for keep in (0.000, 0.010, 0.020, 0.040):
        a = pf.a3_funded_locking(keep_buffer_pct=keep)
        st = sim.simulate_account(a, a.cushion * 0.15, strat, n_paths=N_SINGLE,
                                  seed=SEED, cushion_guard=4.0, min_risk=a.min_risk)
        print(f"{a.harvest_keep:20.0f}{a.harvest_keep - 3000:8.0f}"
              f"{st['cash_per_path']:9.0f}{st['p_bust']:9.2f}")
    print("\n  -> withdrawing down to the locked floor leaves 0 cushion: the next")
    print("     loser kills an account that is already paid for and already won.")
    print("     Always leave a buffer above a locked floor.")

    print("\n  THE MOST IMPORTANT POLICY: shrink risk as the cushion shrinks")
    print("  (risk = min(size, cushion/guard); guard=4 means one loss can never")
    print("   cost more than a quarter of what you have left)")
    print(f"{'':26}{'guard':>7}{'A1 P(ok)':>10}{'A2 P(ok)':>10}{'A3 P(ok)':>10}"
          f"{'A2 P(dead)':>12}")
    for guard in (None, 1.0, 2.0, 4.0, 6.0):
        cells = []
        for a in pf.default_accounts():
            st = sim.simulate_account(a, a.cushion * 0.30, strat, n_paths=N_SINGLE,
                                      seed=SEED, cushion_guard=guard)
            cells.append(st)
        g = "none" if guard is None else f"{guard:.0f}"
        print(f"{'':26}{g:>7}" + "".join(f"{c['p_success']:10.2f}" for c in cells)
              + f"{cells[1]['p_bust']:12.2f}")
    print("  A1 and A3 gain real pass-probability from de-risking. A2 does not")
    print("  move at all: its cushion (15) is smaller than 4x a minimum lot (16),")
    print("  so there is no size small enough to make it safe. That is a rule")
    print("  problem, not a discipline problem.")


def rr_sensitivity(accts, strat) -> None:
    """Win rate alone says nothing: 60% at 1.0R is a different business."""
    rule("4. THE R:R YOU DID NOT TELL ME  (60% win rate is not an edge by itself)")
    print(f"{'R:R':>6}{'E/trade':>10}   P(success) at risk = 15% of cushion")
    for rr in (0.8, 1.0, 1.2, 1.5, 2.0, 3.0):
        st = type(strat)(win_rate=strat.win_rate, rr=rr,
                         trades_per_week=strat.trades_per_week,
                         friction=strat.friction)
        cells = []
        for a in accts:
            res = sim.simulate_account(a, a.cushion * 0.15, st, n_paths=N_SINGLE,
                                       seed=SEED, cushion_guard=4.0,
                                       min_risk=a.min_risk)
            ok = res["p_pass"] if a.mode == "challenge" else res["p_payout"]
            cells.append(f"{a.key} {ok:.2f}")
        print(f"{rr:6.1f}{st.expectancy:10.3f}   " + "   ".join(cells))
    print()
    print("  Break-even win rate = (1 + friction) / (1 + R:R):")
    for rr in (1.0, 1.5, 2.0, 3.0):
        be = (1 + strat.friction) / (1 + rr)
        print(f"    at {rr:.1f}R you need > {100 * be:.1f}% wins. You have "
              f"{100 * strat.win_rate:.0f}%.")
    print()
    print("  Read the 1.0R row: at 60% wins and 1.0R the edge is thin and the")
    print("  tight accounts flip to coin flips. Your real R:R is the single")
    print("  input that decides whether this portfolio is a business or a bet --")
    print("  measure it from your last 50 closed trades, not from memory.")

    print("\n  What the plan looks like at a REALISTIC live edge")
    print("  (208 trades/yr, risk = 15% of cushion; rho=0.85, all three at once):")
    print(f"{'E/trade':>9}{'R per yr':>10}   " + "   ".join(
        f"{a.key}:P(ok)" for a in accts) + "   E[cash]/yr")
    for edge_rr, edge_wr in ((1.5, 0.60), (1.2, 0.58), (1.0, 0.60),
                             (1.0, 0.55), (0.9, 0.55)):
        st = type(strat)(win_rate=edge_wr, rr=edge_rr,
                         trades_per_week=strat.trades_per_week,
                         friction=strat.friction)
        cells, cash = [], 0.0
        for a in accts:
            res = sim.simulate_account(a, a.cushion * 0.15, st, n_paths=N_SINGLE,
                                       seed=SEED, cushion_guard=4.0,
                                       min_risk=a.min_risk)
            cells.append(f"{res['p_success']:.2f}")
            cash += res["cash_per_path"]
        print(f"{st.expectancy:9.3f}{st.expectancy * 208:10.0f}   "
              + "   ".join(f"{c:>5}" for c in cells) + f"   {cash:6.0f}")
    print()
    print("  The message that does not change across the whole row: A1 keeps")
    print("  converting (its cushion is 3x its target) while A2's odds collapse")
    print("  first. Order your attention by cushion/need, not by account size.")


def sequencing(accts, strat) -> None:
    """One account at a time, or all three at once, and at what correlation."""
    rule("5. SEQUENCING: one account at a time vs all three at once")
    a1, a2, a3 = accts
    # 15% of the remaining cushion, clamped to at least one minimum lot
    plan = {a.key: max(a.cushion * 0.15, a.min_risk) for a in accts}
    print(f"  risk budget used: A1 {plan['A1']:.0f}  A2 {plan['A2']:.0f}  "
          f"A3 {plan['A3']:.0f} USD per trade "
          f"({', '.join(f'{100 * plan[a.key] / a.start:.2f}%' for a in accts)} of balance)")
    print("  horizon 52 weeks.  'cash' = USD actually withdrawn, 80% split.")
    print("  A1 passing is scored as a conversion, not as cash.\n")
    print(f"{'policy':30}{'rho':>5}{'mean':>8}{'p10':>8}{'med':>8}"
          f"{'P(any)':>8}{'P(2+dead)':>11}{'P(all dead)':>12}{'alive':>7}")

    # what a passed A1 is worth: a 2.5k funded account with the same 6% trail/lock
    credit = conversion_credit(strat)
    print(f"  (a passed A1 is credited {credit['A1']:.0f} USD = the 12-month cash "
          f"value of the 2.5k funded account it becomes)")

    budget = dict(plan)
    flat = {"A1": 0.0, "A2": 0.0, "A3": 0.0}

    cases = [
        ("all three, same signal", "parallel", 0.85, budget),
        ("all three, independent", "parallel", 0.0, budget),
        ("all three, risk halved", "parallel", 0.85,
         {k: v / 2 for k, v in budget.items()}),
        ("one at a time (A1->A3->A2)", "sequential", 0.0, budget),
        ("A1 only (press the cushion)", "parallel", 0.0, {**flat, "A1": plan["A1"]}),
        ("A3 only (largest payout)", "parallel", 0.0, {**flat, "A3": plan["A3"]}),
        ("A2 only (fastest payout)", "parallel", 0.0, {**flat, "A2": plan["A2"]}),
    ]
    for label, policy, rho, risk_map in cases:
        accts_used = [a for a in accts if risk_map[a.key] > 0]
        res = sim.simulate_portfolio(
            accts_used, risk_map, strat, policy=policy, rho=rho,
            n_paths=N_PORT, max_steps=208, seed=SEED, pass_credit=credit,
        )
        print(f"{label:30}{rho:5.2f}{res['cash_per_path']:8.0f}{res['cash_p10']:8.0f}"
              f"{res['cash_p50']:8.0f}{res['p_any_payout']:8.2f}"
              f"{res['p_multi_dead']:11.2f}{res['p_all_dead']:12.2f}"
              f"{res['alive_end']:7.2f}")
    print()
    print("  Two honest readings of this table:")
    print("  1. rho barely moves any number, and that is the lesson. Correlation")
    print("     does NOT change your expected yearly cash (E[sum] = sum of E[.]);")
    print("     it changes the shape of the path. Copying one idea into three")
    print("     accounts is ONE position sized 3x, so the size gets decided once,")
    print("     on the idea -- not three times, once per account.")
    print("  2. Sequencing, one-at-a-time vs parallel, is worth about 5%. Where you")
    print("     put your risk is worth 60x (A2 20 USD/yr vs A3 1294 USD/yr). Spend")
    print("     your decision-making on sizing, not on juggling terminals.")


def hedging(accts) -> None:
    rule("6. DOES CROSS-ACCOUNT HEDGING CREATE MONEY?")
    a3, a2 = accts[2], accts[1]
    print("  Opposite legs, same size, in two accounts. The P&L's are mirror")
    print("  images, so the losing leg dying is the winning leg's profit.")
    print(f"{'pair':34}{'sigma':>7}{'net (closed at limit)':>22}"
          f"{'net (firm eats the gap)':>24}")
    for label, ca, cb in (
        ("A3 (180) short A3 (180)", a3.cushion, a3.cushion),
        ("A3 (180) short A2 (15)", a3.cushion, a2.cushion),
        ("A2 (15) short A2 (15)", a2.cushion, a2.cushion),
    ):
        for sigma in (50.0, 180.0, 600.0):
            honest, gap = sim.hedge_ev(ca, cb, sigma, n_paths=8000, seed=7,
                                       friction_cost=2.0)
            print(f"{label:34}{sigma:7.0f}{honest:22.1f}{gap:24.1f}")
    print()
    print("  Column 1 is what you actually get: zero, minus two spreads. Column 2")
    print("  only turns positive if a move jumps THROUGH the losing account's")
    print("  drawdown limit and the firm eats the overshoot. That is not an edge,")
    print("  it is a short-gap bet with two extra spreads -- and it is the exact")
    print("  pattern ('simultaneous opposite positions across accounts') that most")
    print("  firms void payouts for. Read your T&C before you even think about it.")
    print()
    print("  The transfer is real but it is not free: you convert two live, paying")
    print("  accounts into one account worth the same, minus costs, minus an")
    print("  account's remaining optionality. Hedging moves risk, it never deletes")
    print("  it, and it is only 'smart' when the sacrificed account is already dead")
    print("  anyway -- which is the same as saying: cut size on the one you were")
    print("  protecting, and keep the other.")


def conversion_credit(strat) -> dict:
    """What a passed A1 is worth: the 2.5k funded account it turns into."""
    converted = pf.a3_funded_locking(balance=2500.0)
    conv = sim.simulate_account(converted, converted.cushion * 0.15, strat,
                                n_paths=N_SINGLE, seed=SEED, cushion_guard=4.0)
    return {"A1": conv["cash_per_path"]}


def main() -> None:
    accts = pf.default_accounts()
    strat = pf.base_strategy()
    credit = conversion_credit(strat)
    print(f"edge assumed: {100 * strat.win_rate:.0f}% wins, {strat.rr:.1f}R average "
          f"winner, {strat.expectancy:+.3f}R per trade after friction, "
          f"{strat.trades_per_week:.0f} trades/week")
    print(f"implied edge: {strat.expectancy * 208:.0f}R per 52 weeks -- section 4 "
          f"tests what happens when that is optimistic (it is)")
    constraints_table(accts)
    sizing_sweep(accts, strat, credit)
    rule_uncertainty(strat)
    rr_sensitivity(accts, strat)
    sequencing(accts, strat)
    hedging(accts)


if __name__ == "__main__":
    main()

