"""Invariant tests for the rules engine.  Run: python3 prop_risk/test_sim.py"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import portfolio as pf  # noqa: E402
import sim  # noqa: E402


class TestFloors(unittest.TestCase):
    def test_static_floor_never_moves(self):
        a = pf.a1_prop_phase2()
        for peak in (a.start, a.start + 500, a.start + 5000):
            self.assertEqual(a.next_floor(peak), a.floor)

    def test_trailing_floor_is_monotone(self):
        a = pf.a3_funded_locking()
        prev = a.floor
        for peak in (3000, 3050, 2900, 3100, 3500, 3200):
            f = a.next_floor(peak, prev)
            self.assertGreaterEqual(f, prev, "a trailing floor must never turn down")
            prev = f

    def test_floor_locks_at_breakeven(self):
        a = pf.a3_funded_locking()
        self.assertEqual(a.next_floor(3180.0), 3000.0)   # lock is reached
        self.assertEqual(a.next_floor(9000.0), 3000.0)   # and cannot climb past it

    def test_cushion_and_ratio(self):
        a1, a2, a3 = pf.default_accounts()
        self.assertAlmostEqual(a1.cushion, 325.0)
        self.assertAlmostEqual(a1.ratio, 3.25)
        self.assertAlmostEqual(a2.cushion, 15.0)
        self.assertAlmostEqual(a2.ratio, 0.5)
        self.assertAlmostEqual(a3.ratio, 1.0)


class TestStrategy(unittest.TestCase):
    def test_expectancy_matches_definition(self):
        s = sim.Strategy(win_rate=0.60, rr=1.5, friction=0.02)
        self.assertAlmostEqual(s.expectancy, 0.60 * 1.5 - 0.40 - 0.02)

    def test_break_even_win_rate_is_consistent(self):
        # at exactly the break-even win rate the edge must be zero
        for rr in (1.0, 1.5, 3.0):
            s = sim.Strategy(win_rate=(1 + 0.02) / (1 + rr), rr=rr, friction=0.02)
            self.assertAlmostEqual(s.expectancy, 0.0, places=9)


class TestMonteCarlo(unittest.TestCase):
    def test_probabilities_sum_to_one(self):
        a = pf.a1_prop_phase2()
        st = sim.simulate_account(a, 16.0, pf.base_strategy(), n_paths=400,
                                  seed=1, cushion_guard=4.0)
        total = st["p_pass"] + st["p_bust"] + st["p_unresolved"]
        self.assertAlmostEqual(total, 1.0, places=9)

    def test_same_seed_is_deterministic(self):
        a = pf.a3_funded_locking()
        kw = dict(n_paths=300, seed=42, cushion_guard=4.0)
        s = pf.base_strategy()
        self.assertEqual(sim.simulate_account(a, 27.0, s, **kw),
                         sim.simulate_account(a, 27.0, s, **kw))

    def test_wide_cushion_account_almost_always_passes(self):
        a = pf.a1_prop_phase2()
        st = sim.simulate_account(a, 16.0, pf.base_strategy(), n_paths=500,
                                  seed=3, cushion_guard=4.0)
        self.assertGreater(st["p_pass"], 0.97)
        self.assertLess(st["p_bust"], 0.01)

    def test_min_lot_beats_cushion_guard(self):
        """The guard cannot size below one lot, so A2 is hopeless at any size."""
        a = pf.a2_funded_tight()
        st = sim.simulate_account(a, 0.5, pf.base_strategy(), n_paths=400,
                                  seed=5, cushion_guard=4.0)
        self.assertGreaterEqual(st["risk_eff"], a.min_risk)

    def test_zero_risk_never_trades(self):
        a = pf.a1_prop_phase2()
        a.min_risk = 0.0
        st = sim.simulate_account(a, 0.0, pf.base_strategy(), n_paths=50, seed=1)
        self.assertEqual(st["p_pass"], 0.0)
        self.assertEqual(st["p_bust"], 0.0)

    def test_no_cash_without_a_payout(self):
        a = pf.a3_funded_locking()
        a.min_risk = 0.0
        st = sim.simulate_account(a, 0.0, pf.base_strategy(), n_paths=50, seed=1)
        self.assertEqual(st["cash_per_path"], 0.0)
        self.assertEqual(st["payouts_per_path"], 0.0)


class TestHedging(unittest.TestCase):
    def test_hedge_nets_zero_minus_costs(self):
        for ca, cb in ((180, 180), (180, 15), (15, 15)):
            honest, _ = sim.hedge_ev(ca, cb, sigma_move=200.0, n_paths=2000,
                                     seed=1, friction_cost=2.0)
            self.assertAlmostEqual(honest, -2.0, places=6)

    def test_gap_column_only_positive_for_big_moves(self):
        _, gap_small = sim.hedge_ev(180, 180, 10.0, n_paths=3000, seed=1)
        _, gap_big = sim.hedge_ev(180, 180, 900.0, n_paths=3000, seed=1)
        self.assertGreater(gap_big, gap_small)


if __name__ == "__main__":
    unittest.main(verbosity=2)
