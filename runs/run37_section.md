## Run 37: which memory carried Run 29's tail?

*19 October 2026. (step 3). Pre-registered and hashed before any registered run (`tail/PREREG_37.md`, 11:19 UTC), with registered verdict thresholds.*

**Question.** In Run 29 a clock's record leads in time over 20–120 ticks: the mean lag asymmetry D over τ = 20–120 is +8.3×10⁻⁴. Run 35 showed this tail needs memory in the medium between ticks. Run 29's engine has two such memories:
- **H-hole:** the clock's own reservation hole. Each renewal takes a unit from each of its two places, and the hole relaxes over tens of ticks.
- **H-ambient:** ambient fluctuations of possibility, which the clock integrates.

**Method.**
- `engine37.py` is Run 29's engine with one change. A renewing clock takes its two units from the whole box, uniformly by unit, not from its own places, so it leaves no hole of its own.
- Everything else is Run 29's: medium, release, presence clock, 125 clocks in box 30, P₀ = 64, p_s = 1, 2 seeds × 240,000 ticks read.
- Without its self-dip a clock collects more presence (128.0 against 106.6) and ticks faster (0.2000 against 0.1665 per tick).
- **Verdict (registered):** R = tail(Run 37)/tail(Run 29).
  - **H-hole:** R < 0.1, and Run 37's tail within 3σ of zero.
  - **H-ambient:** R > 0.5.
  - **Both:** anything between.

**Result.**

| | tail: mean D over τ = 20–120 | D(1) | D at τ = 5 |
|---|---|---|---|
| Run 29 (own hole) | (8.29 ± 0.02)×10⁻⁴ | +0.0343 | −0.0103 |
| **Run 37 (no own hole)** | **(9.27 ± 0.02)×10⁻⁴** | +0.0033 | +0.0029 |
| Run 35 (no memory in the medium) | (0.1 ± 0.2)×10⁻⁵ | +0.0857 | +0.0003 |

**R = 1.118 ± 0.004: H-ambient.** Ambient fluctuations of possibility carried Run 29's long tail. Without its own hole the tail is unchanged, slightly larger and slower to fall: 3.7×10⁻⁴ against 2.1×10⁻⁴ at τ = 120.

![Run 37](figures/37_tail.png)

**Reading.**
1. **The long tail is the medium's ambient memory.** A clock integrates presence, and presence at a place is correlated over tens of ticks in the diffusive medium. So the record leads with that correlation's shape.
   - Removing the medium's memory (Run 35) removes the tail.
   - Removing only the clock's own hole (this run) leaves it.
2. **The clock's own hole shaped the short lags.** Without it:
   - the swings at τ = 4–10 (the clock's own cadence) vanish
   - D(1) falls from 0.034 to 0.0033
   - the profile becomes smooth and monotone
3. **For Run 29's arrow-of-time reading:** the "leak" of time order into a clock's long-window record came from the medium's slow fluctuations. Under the adopted rules (Run 35) the medium relaxes each tick, and that leak becomes the clock's own one-tick lead.
