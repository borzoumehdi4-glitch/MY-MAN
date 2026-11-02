"""The three accounts, expressed as rules the engine can enforce.

Every number here is an assumption that can be corrected in one place; the
report re-derives the whole plan from these.

A1 - prop challenge, phase 2
     nominal 2500, currently +1% (2525)
     max DD 12% of the INITIAL balance -> hard floor 2200, static (no trailing)
     phase-2 target 5% -> 2625, so 100 USD still to find, 325 USD of room
     no daily-DD rule, no consistency rule

A2 - funded, 1000
     30 USD already withdrawn, balance back to 1000
     DD 1.5% (the tight reading, modelled as trailing -> floor 985)
     payout allowed once balance >= 1030, i.e. every +3%
     ASSUMED profit split 80%

A3 - funded, 3000
     trailing DD 6% = 180 USD, floor ratchets with the high-water mark
     locks once +6% is reached: floor stops at 3000 (breakeven)
     payout trigger modelled at +6% (3180), leaving 3060 in the account so the
     locked floor still has a 60 USD / 2% buffer above it
     ASSUMED profit split 80%
"""
from __future__ import annotations

from sim import INF, Account, Strategy

SPLIT = 0.80  # default profit split; A2/A3 both assumed 80%

# Smallest position most FX brokers/firms allow is 0.01 lot.  On EURUSD that is
# 0.10 USD per pip, so a 40-pip swing stop is ~4 USD of risk -- you cannot size
# below that.  It is why a 15 USD cushion is only three or four trades deep.
MIN_LOT_RISK = 4.0


def a1_prop_phase2(profit_pct: float = 0.01, dd_pct: float = 0.12,
                   phase2_target_pct: float = 0.05, nominal: float = 2500.0) -> Account:
    """Prop challenge, phase 2, STATIC drawdown measured from the initial balance."""
    start = nominal * (1 + profit_pct)
    floor = nominal * (1 - dd_pct)
    return Account(
        key="A1",
        name="PROP 2.5k phase-2 (static 12% DD)",
        start=start,
        peak=start,
        floor=floor,
        dd_kind="static",
        dd_amount=0.0,
        floor_cap=INF,
        target=nominal * (1 + phase2_target_pct),
        harvest_keep=start,
        split=SPLIT,
        min_risk=4.0,
        mode="challenge",
        limit_pct=dd_pct,
    )


def a2_funded_tight(balance: float = 1000.0, dd_pct: float = 0.015,
                    payout_pct: float = 0.03, trailing: bool = True,
                    split: float = SPLIT) -> Account:
    """Funded 1k, very tight DD, withdraw every +3%.

    trailing=True  -> floor = high-water mark - 1.5%  (pessimistic, usual)
    trailing=False -> floor = 985 fixed from the start   (static reading)
    """
    dd = balance * dd_pct
    return Account(
        key="A2",
        name="FUNDED 1k (1.5% DD, pay at +3%)",
        start=balance,
        peak=balance,
        floor=balance - dd,
        dd_kind="trailing" if trailing else "static",
        dd_amount=dd,
        floor_cap=INF,  # this account never locks
        target=balance * (1 + payout_pct),
        harvest_keep=balance,
        split=split,
        mode="funded",
        reset_on_withdrawal=True,  # ASSUMPTION: payout re-bases the 1.5% trail
        min_buffer=0.0,
        min_risk=4.0,  # 0.01 lot x 40-pip stop
        limit_pct=dd_pct,
    )


def a3_funded_locking(balance: float = 3000.0, dd_pct: float = 0.06,
                      lock_at_pct: float = 0.06, keep_buffer_pct: float = 0.02,
                      split: float = SPLIT) -> Account:
    """Funded 3k, trailing 6% DD that freezes the floor at breakeven on +6%."""
    dd = balance * dd_pct
    return Account(
        key="A3",
        name="FUNDED 3k (6% trailing, locks at +6%)",
        start=balance,
        peak=balance,
        floor=balance - dd,
        dd_kind="trailing",
        dd_amount=dd,
        floor_cap=balance,  # the floor can never climb past breakeven
        target=balance * (1 + lock_at_pct),
        harvest_keep=balance * (1 + keep_buffer_pct),
        split=split,
        mode="funded",
        reset_on_withdrawal=False,  # the locked floor at breakeven must survive
        min_buffer=balance * keep_buffer_pct,
        min_risk=5.0,  # 0.01 lot x 50-pip stop
        limit_pct=dd_pct,
    )


def default_accounts() -> list[Account]:
    return [a1_prop_phase2(), a2_funded_tight(), a3_funded_locking()]


def base_strategy(**kw) -> Strategy:
    """60% win rate, 1.5R average winner, 4 swing trades a week, 2% of R friction."""
    return Strategy(**kw)
