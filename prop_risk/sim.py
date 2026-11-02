"""Monte-Carlo engine for FX prop-firm / funded account management (stdlib only).

Models the three account types in the portfolio:

    A1  prop challenge phase 2 : static DD from INITIAL balance, wide cushion
    A2  funded                 : very tight trailing DD, low payout threshold
    A3  funded                 : trailing DD that LOCKS once a profit target is hit

Modelling conventions (conservative readings -- change them and the ranking is
recomputed, nothing is hard-coded to a conclusion):

  * The drawdown floor is monotone: a trailing floor ratchets up with the equity
    high-water mark and never turns back down.  This is the "hard trailing"
    reading, which is the pessimistic one for the trader.
  * A withdrawal never lowers the floor.  Pessimistic reading, and it also
    catches the classic mistake of withdrawing down to a locked floor, which
    silently re-arms the death zone.
  * A trade risks a fixed number of dollars (not a fixed % of a moving balance),
    because that is what a prop trader actually does: size from the stop.
  * `friction` is spread/commission as a fraction of R, charged on every trade,
    win or lose.  It is what makes small position sizes over many trades costly.
  * Per-trade outcome is the two-point approximation (+rr*R with prob p,
    -1*R with prob 1-p).

Run:  python3 prop_risk/report.py
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass
from statistics import NormalDist

INF = float("inf")

# --------------------------------------------------------------------------- #
# Account definition
# --------------------------------------------------------------------------- #


@dataclass
class Account:
    """One account plus the rules that can kill it.

    floor        current hard death line (equity <= floor -> account dead)
    dd_kind      "static"   -> floor never moves
                 "trailing" -> floor = max(floor, min(floor_cap, peak - dd_amount))
    floor_cap    highest the floor may ratchet to (the "lock" level); INF if none
    mode         "challenge" -> one-shot: pass at `target`, then stop
                 "funded"    -> repeatable: withdraw at `target`, keep going
    harvest_keep balance left in the account after a withdrawal
    """

    key: str
    name: str
    start: float
    peak: float
    floor: float
    dd_kind: str
    dd_amount: float
    floor_cap: float
    target: float
    harvest_keep: float
    split: float
    mode: str
    reset_on_withdrawal: bool = True   # does a payout re-base the high-water mark?
    min_buffer: float = 0.0            # $ kept above the floor after a payout
    min_risk: float = 0.0              # $ risk of the smallest position you can take
    limit_pct: float = 0.0  # display only: DD as % of nominal balance

    # ---- derived bookkeeping ------------------------------------------------
    @property
    def need(self) -> float:
        """Dollars of profit required to reach the next payout / pass."""
        return max(0.0, self.target - self.start)

    @property
    def cushion(self) -> float:
        """Dollars of loss the account can still absorb before it dies."""
        return max(0.0, self.start - self.floor)

    @property
    def ratio(self) -> float:
        """cushion / need.  >=2 comfortable, ~1 coin-flip, <1 lottery ticket."""
        return self.cushion / self.need if self.need else INF

    def next_floor(self, peak: float) -> float:
        """Monotone floor update after the equity high-water mark advances."""
        if self.dd_kind == "static":
            return self.floor
        return max(self.floor, min(self.floor_cap, peak - self.dd_amount))


@dataclass
class Strategy:
    """The trader's edge, in the units the rules engine cares about."""

    win_rate: float = 0.60
    rr: float = 1.5  # average winner / average loser
    trades_per_week: float = 4.0
    friction: float = 0.02  # spread+commission as a fraction of R, per trade

    @property
    def expectancy(self) -> float:
        """Expected P&L per trade in R, net of friction."""
        return self.win_rate * self.rr - (1.0 - self.win_rate) - self.friction


# --------------------------------------------------------------------------- #
# Single-account simulation
# --------------------------------------------------------------------------- #


def simulate_account(
    acct: Account,
    risk: float,
    strat: Strategy,
    n_paths: int = 8000,
    max_trades: int = 208,
    seed: int = 0,
    cushion_guard: float | None = None,
    min_risk: float | None = None,
):
    """Play `n_paths` independent histories of one account.

    risk           dollars risked per trade (the base size)
    cushion_guard  if set, cap risk at cushion/guard so the last few R are not
                   spent on a foregone conclusion (guard=4 -> risk <= cushion/4)
    min_risk       the smallest position the broker/firm lets you take: 0.01 lot
                   with a 40-pip swing stop on EURUSD is about 4 USD.  You cannot
                   size below this, so it is a hard floor on risk and the reason a
                   15 USD cushion is only three or four trades deep.
    max_trades     horizon in trades (208 ~= 52 weeks at 4 trades/week)
    """
    rng = random.Random(seed)
    p, rr, fric = strat.win_rate, strat.rr, strat.friction
    mr = acct.min_risk if min_risk is None else min_risk

    passed = 0
    busted = 0
    alive_end = 0
    cash_total = 0.0
    payouts_total = 0
    got_payout = 0
    pass_trades: list[int] = []
    first_pay_trades: list[int] = []
    cash_hist: list[float] = []

    for _ in range(n_paths):
        bal, peak, floor = acct.start, acct.peak, acct.floor
        cash = 0.0
        paid_this_path = 0
        done = False
        t = 0
        while t < max_trades and not done:
            t += 1
            r = risk
            if cushion_guard is not None:
                r = min(r, (bal - floor) / cushion_guard)
            # ...but you cannot size below the minimum lot, so near the floor the
            # guard stops protecting you and that is precisely how tight-DD
            # accounts die.
            r = max(r, mr)
            if r <= 1e-9:
                break
            if rng.random() < p:
                bal += rr * r
            else:
                bal -= r
            bal -= fric * r
            peak = max(peak, bal)
            floor = acct.next_floor(peak)

            if bal <= floor:  # account dead
                busted += 1
                done = True
                break

            if bal >= acct.target:
                if acct.mode == "challenge":
                    passed += 1
                    pass_trades.append(t)
                    done = True
                    break
                # funded: withdraw, but never down through the floor
                if acct.reset_on_withdrawal:
                    # the firm re-bases the trail on the post-payout balance, so
                    # only the stated payout size binds
                    keep = acct.harvest_keep
                else:
                    # floor is frozen: keep a real buffer above it or the next
                    # loser kills an account you already paid for
                    keep = max(acct.harvest_keep, floor + acct.min_buffer)
                take = bal - keep
                if take <= 0:
                    continue  # nothing safe to take yet, keep trading
                cash += take * acct.split
                payouts_total += 1
                if paid_this_path == 0:
                    first_pay_trades.append(t)
                paid_this_path += 1
                bal = keep
                if acct.reset_on_withdrawal:
                    # firm re-bases the trail on the post-payout balance
                    peak = bal
                    floor = acct.next_floor(peak)
        cash_total += cash
        got_payout += 1 if paid_this_path else 0
        if not done:  # never passed, never died -> still trading at the horizon
            alive_end += 1
        cash_hist.append(cash)

    cash_hist.sort()
    pass_trades.sort()
    first_pay_trades.sort()
    tpw = strat.trades_per_week
    first = pass_trades or first_pay_trades
    return {
        "risk": risk,
        "risk_eff": max(
            min(risk, acct.cushion / cushion_guard) if cushion_guard else risk, mr
        ),
        "p_pass": passed / n_paths,
        "p_payout": got_payout / n_paths,
        "p_success": (passed if acct.mode == "challenge" else got_payout) / n_paths,
        "p_bust": busted / n_paths,
        "p_unresolved": alive_end / n_paths,
        "median_trades_to_pass": first[len(first) // 2] if first else None,
        "payouts_per_path": payouts_total / n_paths,
        "cash_per_path": cash_total / n_paths,
        "cash_p50": cash_hist[len(cash_hist) // 2],
        "cash_p90": cash_hist[int(0.90 * (len(cash_hist) - 1))],
        "cash_per_week": cash_total / n_paths / (max_trades / tpw),
    }



# --------------------------------------------------------------------------- #
# Portfolio simulation (sequencing + correlation)
# --------------------------------------------------------------------------- #


def simulate_portfolio(
    accts: list[Account],
    risk_map: dict,
    strat: Strategy,
    policy: str = "parallel",
    rho: float = 0.0,
    n_paths: int = 6000,
    max_steps: int = 208,
    seed: int = 0,
    pass_credit: dict | None = None,
    cushion_guard: float | None = 4.0,
):
    """Run the accounts together.

    policy  "parallel"   every live account takes a trade each step -- the real
                         case, because the same signal gets copied everywhere
            "sequential" one account at a time, in list order, until it resolves
    rho     correlation of the *latent* trade outcome across accounts. 0.7-0.9 is
            the honest number when you copy one idea into three terminals: it is
            one bet sized three ways, not three bets.
    """
    rng = random.Random(seed)
    z_thresh = NormalDist().inv_cdf(strat.win_rate)
    p, rr, fric = strat.win_rate, strat.rr, strat.friction

    cash_total = 0.0
    any_payout = 0
    all_dead = 0
    multi_dead = 0
    alive_end = 0
    passed_any = 0
    totals: list = []

    for _ in range(n_paths):
        state = {
            a.key: {
                "bal": a.start,
                "peak": a.peak,
                "floor": a.floor,
                "alive": True,
                "busted": False,
                "cash": 0.0,
                "got": False,
                "passed": False,
            }
            for a in accts
        }
        by_key = {a.key: a for a in accts}
        order = [a.key for a in accts]

        for _step in range(max_steps):
            active = [k for k in order if state[k]["alive"]]
            if not active:
                break
            if policy == "sequential":
                active = [active[0]]
            z_common = rng.gauss(0.0, 1.0) if rho > 0 else 0.0
            for k in active:
                a, s = by_key[k], state[k]
                r = risk_map[k]
                if r <= 0:
                    continue
                if cushion_guard is not None:
                    # same de-risking rule as the single-account engine: never let
                    # one loss cost more than 1/guard of the remaining cushion
                    r = min(r, (s["bal"] - s["floor"]) / cushion_guard)
                r = max(r, a.min_risk)  # min-lot clamp applies here too
                if s["bal"] - r <= 0:
                    continue
                if rho > 0:
                    z = math.sqrt(rho) * z_common + math.sqrt(1 - rho) * rng.gauss(0.0, 1.0)
                    win = z < z_thresh
                else:
                    win = rng.random() < p
                s["bal"] += rr * r if win else -r
                s["bal"] -= fric * r
                s["peak"] = max(s["peak"], s["bal"])
                s["floor"] = a.next_floor(s["peak"])

                if s["bal"] <= s["floor"]:
                    s["alive"] = False
                    s["busted"] = True
                    continue
                if s["bal"] >= a.target:
                    if a.mode == "challenge":
                        s["alive"] = False
                        s["passed"] = True
                        # credit the account the challenge converts into, so the
                        # sequencing table compares cash with cash
                        s["cash"] += (pass_credit or {}).get(k, 0.0)
                    else:
                        take = max(0.0, s["bal"] - a.harvest_keep)
                        s["cash"] += take * a.split
                        s["got"] = True
                        s["bal"] -= take

        total_cash = sum(s["cash"] for s in state.values())
        cash_total += total_cash
        totals.append(total_cash)
        if any(s["got"] or s["passed"] for s in state.values()):
            any_payout += 1
        if any(s["passed"] for s in state.values()):
            passed_any += 1
        # "all dead" must mean every account was actually busted: a passed
        # challenge is a win, not a casualty
        n_bust = sum(1 for s in state.values() if s["busted"])
        if n_bust == len(state):
            all_dead += 1
        if n_bust >= 2:
            multi_dead += 1
        alive_end += sum(1 for s in state.values() if s["alive"])

    totals.sort()
    return {
        "policy": policy,
        "cash_p10": totals[int(0.10 * (len(totals) - 1))],
        "p_multi_dead": multi_dead / n_paths,
        "rho": rho,
        "cash_per_path": cash_total / n_paths,
        "cash_p50": totals[len(totals) // 2],
        "p_any_payout": any_payout / n_paths,
        "p_all_dead": all_dead / n_paths,
        "alive_end": alive_end / n_paths,
        "p_pass_challenge": passed_any / n_paths,
    }


# --------------------------------------------------------------------------- #
# Hedging: is a cross-account hedge worth anything?
# --------------------------------------------------------------------------- #


def hedge_ev(
    cushion_a: float,
    cushion_b: float,
    sigma_move: float,
    n_paths: int = 20000,
    seed: int = 7,
    friction_cost: float = 2.0,
):
    """Two accounts, opposite legs, same size.

    The honest mechanic: the two P&L's are exact mirror images, so the moment the
    losing leg reaches its drawdown limit BOTH legs are closed -- the winner is
    up exactly the loser's cushion. The pair nets zero before costs, whether or
    not an account dies. Returns (net_if_closed_at_limit, net_if_firm_eats_gap).

    The second number is where the "hedging is free money" myth comes from: it
    only turns positive if a move jumps PAST the losing account's drawdown limit
    and the firm absorbs the excess instead of invoicing you for it. That is a
    bet on gaps, and it is normally a terms violation, not an edge.
    """
    rng = random.Random(seed)
    honest = 0.0
    gap_illusion = 0.0
    for _ in range(n_paths):
        x = rng.gauss(0.0, sigma_move)
        move = abs(x)
        loser_cap = cushion_b if x > 0 else cushion_a
        # both legs closed the instant the losing leg hits its limit -> nets 0
        honest += 0.0
        # excess the firm would have to eat for the pair to show a profit
        gap_illusion += max(0.0, move - loser_cap)
    return (honest / n_paths - friction_cost, gap_illusion / n_paths - friction_cost)

