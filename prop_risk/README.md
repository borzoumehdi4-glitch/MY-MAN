# Account management playbook — 3 accounts, $6.5k notional

Companion to the engine in this folder. Every number below comes out of
`python3 prop_risk/report.py` (full output saved in `report_output.txt`); nothing
is hand-waved. Change a rule in `portfolio.py`, re-run, and the plan re-derives.

## The one number that decides everything: cushion / need

| | balance | death line | need to next payout | cushion | **r = cush/need** | min-lot shots |
|---|---|---|---|---|---|---|
| **A1** prop 2.5k, phase 2, static 12% | 2525 | 2200 | 100 (5% target) | 325 | **3.25** | 81 |
| **A2** funded 1k, 1.5% DD, pays at +3% | 1000 | 985 | 30 | 15 | **0.50** | 3.8 |
| **A3** funded 3k, 6% trail, locks at +6% | 3000 | 2820 | 180 | 180 | **1.00** | 36 |

- `need` = profit required to get paid. `cushion` = loss you can absorb before dead.
- **r >= 2** = the rules are on your side. **r ~ 1** = coin flip. **r < 1** = lottery.
- `min-lot shots` = how many **0.01-lot** trades fit in the cushion. On A2 that is
  **3.8 trades**. A 0.01 lot with a 40-pip stop risks ~$4, which is **27% of A2's
  entire drawdown allowance**. You cannot size A2 down into safety.

This ratio, not win rate, is what should decide where your attention goes.
It is also why the account *sizes* ($1k / $2.5k / $3k) are the least important
thing about them.

## Verdict on your two candidate plans

**"Trade one account at a time"** — unnecessary. The engine says sequencing is
worth ~5% (parallel 2412 vs sequential 2296 USD/yr). It costs you nothing to run
all three, because the two that matter have wide floors.

**"Hedge the positions"** — no. It is a transfer, not an edge: the winner's gain
*is* the loser's loss, so the pair nets **exactly zero minus two spreads** in every
case where both accounts are closed at the limit. It only shows a profit if a move
**jumps through** the losing account's DD limit and the firm eats the overshoot —
that is a short-gap bet, and "simultaneous opposite positions in multiple accounts"
is the specific pattern that most firms void payouts over. Read your T&C first.
Real hedging is intra-account: don't open the second leg, just take smaller size.

**Correlation, the honest version:** copying one idea into three terminals is *one
position sized 3x*. But note what the table shows — rho=0.85 vs rho=0 barely moves
expected cash (2412 vs 2413). Correlation does not change `E[sum]`; it changes the
shape of the path. So decide size **once, on the idea**, and stop thinking of it
as three independent bets.

## The plan, in priority order

### 1. Press A1 — it is the cheapest win you own
You need **+4% ($100)** with **$325** of room. r = 3.25. Modelled P(pass) ~ 1.00
and a **median ~3 weeks** at 0.6% risk.
- Risk **$15-16/trade (0.6%)**, hard ceiling $25 (1%). Above ~1% you add variance
  for zero extra probability — P(pass) is already ~1.
- Its drawdown is **static from the initial balance**, the most generous rule in
  your portfolio. This is the one account where you can sit through adverse
  excursion, use wide structural stops and let winners run.
- Do not "preserve" it by trading tiny: at $4/trade it needs 25 net R instead of 6.

### 2. A3 is your cash engine — and the fastest *meaningful* payout
You need **+6% ($180)** with **$180** of room. Risk **$18-27/trade (0.6-0.9%)**.
- Modelled: P(first payout) ~ 1.00, **median 2-3 weeks** to the first payout,
  ~11.8 payouts/yr ~ **$1,300/yr** at 80% split, P(dead) ~ 0.14.
- The lock at +6% is the whole point: the floor freezes at **3000**. From then on
  you harvest cycles — **but never withdraw down to 3000.** Withdrawing to the
  locked floor leaves $0 cushion, and the next loser kills an account you already
  paid for and already won. Keep a **$60 (2%)** buffer: withdraw to **3060**.
  Leaving 3000 -> $266/yr and a 99% death rate. Leaving 3060 -> $1,306/yr and 14%.
  Same account, five times the money.
- **Trailing DD changes your trade management, not just your size.** A swing trade
  that retraces gives back the high-water mark and drags the floor up behind you.
  On A3 take partials and move to breakeven around +3%; on A1 you can hold.

### 3. A2 is a lottery ticket — treat it like one
**3.8 minimum-size trades of room.** $88/yr expected, **98% chance it dies**.
- Trade it with **0.01 lot only and a stop of 40 pips or less.** Anything wider is
  a coin flip on the whole account.
- Withdraw the moment you hit +3%. That is real cash in your pocket.
- Do not hedge it, do not "protect" it, do not spend decision-making on it.
- **One rule to verify:** after you take the payout, does the 1.5% trail re-base on
  the new balance? If yes -> repeatable, ~$88/yr. If the floor **never moves down**,
  the most you can ever book is **~$15** (at 1030 you are only 15 above a 1015
  floor) and you are at the wall the moment you take it. Ask support. It decides
  whether A2 is an annuity or a single $12 cheque.

## Concrete sizing sheet

| account | risk/trade | % of balance | stop guidance | harvest rule |
|---|---|---|---|---|
| A1 | $15-16 (max $25) | 0.6% (max 1.0%) | structural, wide OK (static DD) | pass at 2625 -> funded |
| A3 | $18-27 | 0.6-0.9% | tighter, partials at +3% (trailing DD) | at 3180 -> withdraw to **3060** |
| A2 | $4 (0.01 lot) | 0.4% | <=40 pips, non-negotiable | at 1030 -> withdraw everything |

**Why $18-27 on A3 and not the model's $45?** The engine's EV-maximising size is
exactly the de-risking cap (cushion/4 = $45, 1.5% of balance) — because expected
value does not price the thing you actually care about, which is not losing an
asset. At a realistic edge that ranking inverts: at E = +0.08R/trade, A3's
P(first payout) falls to 0.67 and the smaller size is the one that survives.
Run 60% of the cap and you keep most of the cash with half the path variance.

**Portfolio cap:** <=$50 simultaneous risk across all three (~0.8% of the $6.5k
combined). If you copy one idea into three terminals, that $50 is one position —
size it as one position, not three.

**Universal de-risking rule** (the single most valuable line in this document):
`risk = min(your size, cushion / 4)`. One loss may never cost more than a quarter
of the room you have left. With it, A1 and A3 keep their pass probability; without
it they degrade. A2 does not move at any guard level — its cushion ($15) is
smaller than 4x a minimum lot ($16), so there is no size small enough to save it.
That is a rule problem, not a discipline problem.


## What would change the plan

- **Your real R:R.** A 60% win rate alone is not an edge: at 1.0R you need >51%
  wins just to break even, and A2/A3 collapse to 0.52 / 0.93. Measure it over your
  last 50 closed trades. The *ordering* above (press A1, A3 is the engine, A2 is a
  ticket) holds all the way from E = +0.025R to +0.48R, so that part is robust.
  The *dollar amounts* are not — they scale with your edge.
- **The assumed +0.48R/trade is optimistic** (it implies 100R/year, which is a
  money printer). Expect +0.05 to +0.20R live after slippage. The report's
  realistic-edge table shows the same plan worth $84-409/yr at those levels
  instead of $1,395.
- **A1's funded-stage rules** — I modelled them as 6% trailing with a lock, like
  A3. If the phase-2-to-live terms differ, only A1's *credit* changes, never its
  priority.
- **The two rules worth a support ticket:** (1) does A2's trail re-base after a
  payout; (2) can A3's locked floor move after a withdrawal. Both are in
  `rule_uncertainty()` and both change the numbers a lot.

## Answering "what is the fastest payout?"

The engine's speed column is blunt: **A2 pays in ~3 weeks for ~$24-30; A3 pays in
~2-3 weeks for ~$96-120** and then keeps paying because the floor locks at
breakeven. A3 dominates A2 on *both* speed and size, so **there is no conflict
between preservation and fastest payout** in your portfolio — the conservative
choice and the greedy choice are the same account. A1's conversion runs in
parallel in the same ~3 weeks and is a different kind of win: not cash, an asset.

## Reproduce

```bash
python3 prop_risk/report.py          # full report, ~60s
python3 prop_risk/report.py --quick  # smaller Monte-Carlo, ~25s
```

Files: `sim.py` (rules engine + Monte-Carlo), `portfolio.py` (the three accounts,
every assumption in one place), `report.py` (the tables), `report_output.txt`
(saved run of the full report).

> Modelling caveat: this is a risk/capital-allocation model, not a market call.
> It assumes your trades are independent draws with a fixed edge; serial
> correlation after losses, slippage on stops and news gaps all make live results
> worse than the tables. Treat the probabilities as a ranking device, not as
> forecasts. Nothing here is financial advice.

