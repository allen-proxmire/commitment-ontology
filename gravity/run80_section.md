## Run 80: the clock theory with the ambient fixed by the conserved total, on 864 clocks

*23 October 2026. A registered test of the normalisation found by Run 78's check. The predictions were computed and hashed before any engine run (`dense80/PREREG_80.md`, 12:39:28 UTC); the first run started 4.8 s later. The idea is post hoc and disclosed as such. A validation on Run 72's existing 216-clock flat runs was seen before registering. An independent agent checked the run (below).*

**Question.** Run 78's check found that Run 72's clock theory evaluated the clocks at an ambient of 64 per place, while the conserved total puts the non-probe ambient higher. With the level set by the conserved total and the dip taken against the place-mean, the offsets reported since Run 72 vanished. That was a calculation made after the offsets were known. **Does the normalised theory, fixed beforehand, predict new runs where the effect is larger?**

**Setup.**
- Run 72's flat control (W = c_n on every link, c_n = 0.4463), with Run 72's dense layout: 864 clocks, designs 1 and 2 on a checkerboard.
- High medium (64 per place), p_s = 1, H = 640.
- Ten fresh seeds (801–810), 20,000 ticks with 5,000 of burn-in, the engine unchanged. No dense-layout engine run existed before.

**The theory, fixed beforehand.**
- **Field,** from the exact mean-current identity:
$$
z(x)=z_a+\sum_{l=1,2}r_l\,g_l(x),\qquad L\,g_l=-6\,(s_l-\bar s_l),\qquad r_j=\frac{2P_{{\rm own},j}}{jH},
$$
  with s_l = 1 at both places of each design-l clock (release is uniform).
- **Occupancy:** P_x = R(z(x))(1 + δ(R(z), S_x)), with δ the engine's own equation of state from Run 78.
- **Level:** z_a solves the conserved total, Σ_x P_x + 2N_on = 64V, with N_on = 864.
- **Dips:** dip_j = 1 − P_own,j/⟨P_x⟩_non-probe.

**Results** (conservation exact in every run).

| | ambient ⟨P⟩ | design-1 dip | design-2 dip |
|---|---|---|---|
| **normalised, with δ (registered)** | 64.5206 | 0.287850 | 0.178857 |
| measured (10 seeds) | **64.5211 ± 0.0004** | **0.28791 ± 0.00021** | **0.17924 ± 0.00025** |
| Run 72's theory as it stood | 64 | 0.285755 | 0.177060 |

| theory | design 1: measured / theory − 1 | design 2 |
|---|---|---|
| **normalised, with δ (registered)** | **+0.02 ± 0.07% (0.3σ)** | **+0.21 ± 0.14% (1.5σ)** |
| normalised, no δ | +0.09 ± 0.07% | +0.29 ± 0.14% |
| Run 72's theory at the measured ambient, no place-mean term (the check) | +0.24% (3.4σ) | +0.61% (4.3σ) |
| Run 72's theory as it stood (ambient 64) | +0.76 ± 0.07% (10.5σ) | +1.23 ± 0.14% (8.6σ) |

![Run 80](../figures/80_dense.png)

- **K80a, the ambient level: PASS** (64.5206 predicted, 64.5211 ± 0.0004 measured).
- **K80b, the dips against the normalised theory: PASS** (0.3σ and 1.5σ).
- **K80c, the old theory: EXCLUDED** (10.5σ and 8.6σ).

**What the check added.**
1. **Independent reproduction.**
   - All 15 hashes match, and seeds 801–810 each ran once with the registered parameters. Re-running seeds 801 and 810 with the unchanged engine reproduces the stored outputs bit for bit.
   - The checker's own implementation reproduces the predictions to 2×10⁻⁹.
   - Clocks restart on the tick they end, and none failed to restart on any reading tick, so N_on = 864 holds. The conserved-total equation is complete.
2. **K80a checks the bookkeeping, not the dips.** With the total conserved, the non-probe ambient follows from the clocks' own occupancy, identically in every run:
$$
\langle P\rangle_{\rm non\text{-}probe}=\frac{64V-2N_{\rm on}-\sum_{\rm clock\ places}P}{V-2N_{\rm on}} .
$$
   So K80a confirms the bookkeeping (two units held per clock, all 864 on) and adds no test of the dips beyond K80b. A level-only theory with no place-mean term would also pass it.
3. **What the agreement rests on.** Fitting a coefficient for each piece of the theory (1 = as in the theory, 0 = absent):
   - the level from the conserved total: 1.12 ± 0.12 (9σ from 0);
   - the place-mean term (the clocks' neighbours are depleted, so z varies over the non-probe places, and the equation of state is convex): 1.41 ± 0.33 (4.3σ from 0). Without it the registered rule gives FAIL (the third row above);
   - Run 78's δ moves the dips by only 0.07–0.08% and is not tested (1.9 ± 0.95).
4. **The design-2 residual is the clock-place term.** The checker measured the clock-place term D of Run 78's check directly on 864 clocks: −0.019 ± 0.004 and −0.029 ± 0.003 units. Fed back through the clock rate and the conserved total, it brings the registered offsets to −0.05% and −0.00%.
5. **The leverage was three times, not four.** The ambient shift is 3.9 times Run 72's (0.521 against 0.133), but the difference between the two theories' dips is 3.1–3.2 times. The runs' scatter (σ = 0.072% and 0.142%) gave separations of 10.2σ and 7.2σ rather than the planned 15σ and 5σ.
6. **The place-mean term itself is confirmed,** 0.0544 ± 0.0002 measured against the theory's 0.0542. But non-probe places sit 0.0062 ± 0.0004 below R_eng(z), because the release lands before the departures. The effect on the dips is under 0.05%.
7. **A wording correction to Run 78:** the units the clocks hold lower the non-probe ambient (by 2N_on/(V − 2N_on), 0.009 per place on 216 clocks). It is the clocks' depleted places that raise it.

**Reading.**
1. **With predictions registered beforehand, the normalised theory holds on the flat lattice, and Run 72's theory as it stood is excluded.** The level set by the conserved total and the place-mean term account for the offsets of Run 72's theory, at about three times the leverage of Run 72's layout. A simple rescaling of the ambient is not enough: the place-mean term is needed.
2. **For Runs 72b–76:** the level part is common bookkeeping on every lattice, so most of their offsets are very likely this normalisation. But Run 80 tests the flat lattice only. The curved cells rest on Run 78's post hoc calculation, and Run 76's negative-curvature design-2 question is untouched.
3. **Run 78's δ is not tested here,** and the clock-place term D is non-zero on this layout but not resolved by ten seeds.
4. **Next registered test, if wanted:** a curved lattice with the dense layout, for example s = −1. That reaches Run 76's cell and tests the place-mean term where the link totals vary.
