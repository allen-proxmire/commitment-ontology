## 9v. Run 29: where the arrow lives (a one-way event layer, and time-averages that lose the order)

*18 October 2026.*
- *Pre-registered and hashed before any run (`arrow/PREREG_29.md`, 20:47 UTC), together with the engine, the analysis and the theory scripts.*
- *An independent agent re-ran the analysis, reproduced it exactly, and checked every verdict. Its corrections are included.*
- *Allen: "do the recommended steps".*

**Question.** Allen's papers say GR and QM are averages of a one-way process, and that averaging removes the order:
> "averages are permutation-invariant: a sum does not remember the order of its terms… Its reversibility is ignorance of order, formalized." (`Paper_HowTheoryCoarseGrainReality.md`)

His falsifiers include "substrate-level dynamics is genuinely time-reversal-symmetric" (T18 §10). A search of the three repos found no earlier numerical test of time-reversal asymmetry, so this is the first. In the engine the claim has three parts:
1. The bottom is one-way.
2. Averaging removes the order.
3. Something leaks.

**Runs.**
- **Rules.** The adopted rules (Candidate A′), unchanged: $p_s$ = 1, $P_0$ = 64, box 30.
- **V (the vacuum alone).** 100,000 ticks read.
- **C (clocks).** 125 lone probe clocks (presence clock, hold H = 2ħP₀ = 640), two seeds, 240,000 ticks each read.
- **Code checks for `engine29.py`, which only records.** Its field is bit-identical to engine21's. For independent walkers its entropy production is zero to 5×10⁻¹⁰ per tick.

**What is measured.**
- **The vacuum's one-wayness.** This is the move-level entropy production of a wander step, η → η′. At each place x, P units sit there, h hop out, h̃ hop in, and P′ = P − h + h̃:
$$
\sigma=\sum_x\Big[h\ln p(P)+(P-h)\ln\big(1-p(P)\big)-\tilde h\ln p(P')-(P-h)\ln\big(1-p(P')\big)\Big]-\sum_x\big[L_p(P)-L_p(P')\big],\quad L_p(P)=\sum_{k\le P}\ln p(k).
$$
  - The first sum, plus the state function $\sum_x[\ln P!-\ln P'!]$, is ln[Prob(these moves)/Prob(the same moves run backwards)].
  - The second sum is also a state function.
  - State functions average to zero in a steady state and only remove noise. So ⟨σ⟩ ≥ 0, and it is zero exactly when the moves are reversible.
- **The clock record.** Take window means over T ticks: x = presence $X=P_a+P_b$, y = completions.
$$
A_T=\frac{\langle x(k)\,y(k+1)-x(k+1)\,y(k)\rangle}{\mathrm{sd}_x\,\mathrm{sd}_y},\qquad
B_T=\frac{\langle x(k)^2x(k+1)-x(k)\,x(k+1)^2\rangle}{\mathrm{sd}_x^{3}} .
$$
  - Both change sign under time reversal, so both are zero for any reversible process.
  - A > 0 means presence leads completions.
  - Errors are jackknife over 20 time segments (10 per seed).

**Results against the registration.**

| | test | measured | registered | verdict |
|---|---|---|---|---|
| T1 | the vacuum's wandering is one-way | ⟨σ⟩ = (2.706 ± 0.0015)×10⁻³ per place per tick (1,870σ) | > 0 at ≥ 5σ. Size not predicted: 10⁻⁵ to 3×10⁻³. The product-state estimate printed beforehand, 2.74–2.86×10⁻³, was within 5% | **pass** |
| T2 | the clock record is one-way at the event level | A₁ = 0.0343 ± 0.00005 (695σ) | > 5σ | **pass** |
| **K29 (kill)** | averaging removes the order | A₁₀₂₄ = 0.0013 ± 0.0002. \|A\| + 2σ = 0.0018, against 0.1 A\* = 0.0034 | pass if ≤ 0.1 A\* | **pass**. Still 5σ from zero at T = 1024: reduced, not gone |
| T3 | how fast it fades | slope of ln\|A_T\| against ln T, T = 64–1024: −0.95 | −1.2 to −0.4 | in band |
| T4 | the window count becomes bell-shaped | skewness 0.07 at T = 16, rising to 0.26 at 128, then 0.16 at 1024. Slope over 16–1024: +0.14 | −0.5 ± 0.15 | **missed** |
| T5 | summing clocks keeps the order | A₁ = 0.0343, 0.0342, 0.0343, 0.0334 ± 0.0005 for 1, 5, 25, 125 clocks. B falls from 4.3×10⁻⁵ to zero within error | unchanged within 2σ; B falls | as predicted (1.7σ at 125, errors treated as independent) |
| T6 | the count becomes the sum of what it read | corr(presence, completions) in the same window: 0.06 (T = 1), 0.73 (16), 0.96 (64), 0.999 (1024) | rises toward 1 | as predicted |
| T7 | vacuum blocks become bell-shaped | skewness 0.320 ± 0.006 at one place; 0.113, 0.054, 0.030 at b = 2, 3, 5. Slope over b = 1–6: −1.74 | 0.30 ± 0.06; slope −1.5 ± 0.2 | first as predicted; **slope missed** (outside [−1.7, −1.3]; the b = 5–6 points are within 3σ of zero) |
| T8 | the vacuum's third-order asymmetry | one place: B = (7.4 ± 0.35)×10⁻⁵ at T = 1 (21σ), 3.9×10⁻⁴ at T = 16 (4.9σ). Blocks of 8: 1.9σ. Blocks of 27 or more: zero within error | consistent with zero everywhere | **missed at one place**; as predicted for blocks |
| code | presence-clock identity: rate × H / ⟨X while committed⟩ | 1.0000 (both seeds) | 1 | pass |

**Post hoc (suggested by the independent check; not registered): how long the clock record stays one-way.**
- The lag asymmetry is $D(\tau)=\mathrm{corr}(X_t,c_{t+\tau})-\mathrm{corr}(X_t,c_{t-\tau})$ (`lag29.py`, figure panel a). Its values:
  - 0.034 at τ = 1
  - it swings negative over τ = 4–10, the clock's own cadence of about 6 ticks
  - then +0.0024 at τ = 20, 0.0005 at 80, and 0.0002 at 120 (7σ)
  - zero within 2σ from about τ = 160
- From τ = 20 to 120 it falls with an e-fold of 41 ticks. So the record's one-way memory is the **medium's** relaxation around a clock, about 7 holds long, not the hold alone.

![Run 29](figures/29_arrow.png)

**Reading.**

1. **The bottom is one-way, in two ways (T1, T2).**
   - **Commitments are absolutely one-way.** A commitment takes a unit from each of its two places and releases two units to random places. The reversed history would need units to vanish from random places, which the rules never do, so it has probability zero.
   - **The vacuum's wandering is one-way too, far more weakly: 2.7×10⁻³ per place per tick.** It needs both the global tick and the ratio outflow.
     - Independent walkers give exactly zero (exact enumeration, and the engine's control).
     - The continuous-time version of the same rule is a symmetric zero-range process with one-unit jumps, which is reversible with respect to its product measure. This is theory, not tested here. So if the wandering were made tick-free in that way (§11 item 8), the vacuum's arrow would go, leaving the arrow in commitments alone.
   - **The vacuum's arrow shows in what one place holds:** its record is third-order lopsided in time (21σ).
2. **Averaging over time shrinks the order (K29, T3).**
   - The forward/backward asymmetry of a clock's record stays at 0.023–0.034 up to windows of 32 ticks. The exception is a dip to 0.005 at T = 4, from the clock's cadence.
   - From T = 64 it falls about as 1/T (slope −0.95), to 0.0013 at 1024. That is 26× below single ticks, but still 5σ from zero.
   - A 1/T fall is what any one-way record with a finite memory shows when averaged over windows much longer than that memory. The order lives within about 150 ticks of each event, and a long window dilutes it.
   - **Allen's sentence describes what the averaged record becomes.** Over a long window a clock's completions are, to 0.999 correlation, the presence it collected divided by H. That is a sum, and a sum does not remember the order of its terms. The run shows the record becoming such a sum. It does not show that this is the cause of the 1/T fall rather than a description of it.
3. **Averaging over space does not shrink it (T5).** Summing 125 clocks leaves the asymmetry unchanged: 0.0334 against 0.0343. Independent clocks add their asymmetries in proportion. In the engine, losing the order is what averaging over **time** does: "GR basically averages time" (Allen).
4. **The bell curve is not what removes the order (T4 missed).**
   - Time-averaging first *raises* skewness:
     - a vacuum place: 0.32 → 0.42 at T = 256
     - a clock's presence: 0.21 → 0.28 at T = 128
     - its count: 0.07 → 0.26
   - Skewness then falls only slowly: the count is still 0.14 at T = 2048. Meanwhile the asymmetry has fallen 26× from single ticks.
   - A bell curve would erase a *single* record's odd-order asymmetry, B, since a stationary Gaussian scalar record is time-symmetric. It would not erase the cross-asymmetry A between presence and completions: a jointly Gaussian pair can still lead and lag. So Gaussianity is neither what happens here nor enough for A.
   - For the vacuum, the bell curve does arrive with **space**-averaging: skewness 0.32 at one place, 0.03 in blocks of 125.
5. **What leaks.**
   - From T = 256 to 2048 the asymmetry left is
$$
A_T\approx\frac{c}{T},\qquad c\approx1.2\ \text{ticks at these settings},
$$
     with c set by the medium's memory around a clock (the post-hoc e-fold of 41 ticks).
   - At physical $P_0$ and $p_s$ the memory is not known, and neither is the tick length, so no number for real clocks is claimed.
   - The pre-registration's alternative, a $T^{-1/2}$ tail from diffusion, would need a box larger than 30 places to show. It is not excluded.
   - **One average keeps its order (exact bookkeeping, no measurement).** Possibility flows steadily into every drawing clock and is released uniformly. In a steady state the mean inflow through a sphere of radius r around one clock is $D-D_{\rm tot}V_r/V_{\rm box}$. Here D is that clock's draw and $D_{\rm tot}$ is the total draw. A current reverses under time reversal, so this average carries the arrow. Clocks and patterns read P, not the current.

**What this shows and does not show.**
- **It shows:** Allen's coarse-graining claim works in ED's own engine, in this form.
  - A one-way event layer, including a one-way vacuum, produces clock records whose time-averages lose most of their order, falling as 1/T, while averaging over space keeps it.
  - The bottom is not two-way, which is one of Allen's falsifiers, so that falsifier is not triggered.
- **It does not show** that nature works this way. Standard physics gets time-symmetric averages from time-symmetric micro-laws. Telling the two apart needs the leak (c/T, with c unknown at physical scales) or the arrow in fluctuations.
- **Not tested:** wells (only lone clocks), Allen's Result 22 "age" residue, the tick length, and boxes large enough to see a diffusive tail.
