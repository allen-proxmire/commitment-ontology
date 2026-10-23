## 9zzx. Run 75: do the clocks' outer links carry the zero-range theory's design-2 error?

*21 October 2026. This is the follow-up to Run 72b's check. It was registered and hashed before any run that reads clocks (`outer75/PREREG_75.md`, 18:42:41 UTC). The theory's predictions were computed and hashed beforehand (`theory75.json`).*
- *Batch B was first launched under a runner that would not have outlasted the session. It was stopped after 5 s, before any output, and restarted. The log records this.*
- *An independent agent checked the run (below).*

**Question.** Run 72b's check found that the zero-range theory's error for design 2 (hold 2H) is about +0.7% on the flat and positive-curvature lattices and about zero at negative curvature: 0.84 ± 0.24% between the signs. It proposed mixing through the clocks' outer links as the cause.
- The x-links leading outward from each clock's two places are 1.65 times stronger at negative curvature and 0.61 times as strong at positive curvature.
- Faster refill would make the mean-field theory more accurate.

If that is the cause, changing only those links should reproduce the effect.

**Design.**
- **The lattices.** Run 72's flat lattice (every link c_n = 0.4463), with only the x-links at x = 2.5 and 4.5 (mod 6) multiplied by a.
  - Two lattices, a = e^−1 and a = e^+1. That is twice Run 72's log-strength.
  - Everything else is unchanged, including each clock's own link.
- **The runs.** Run 72's engine, high medium (P∞ = 64 p_s), p_s = 1, Run 24's 216 clocks, 20 seeds per lattice.
- **The statistic.** For design j on lattice a, the theory's error is
$$
\text{off}_j(a)=\frac{\overline{\text{dip}}_j(a)}{\text{dip}_j^{\rm theory}(a)}-1,\qquad \text{dip}_j=1-\frac{\overline P_{\rm own,\,j}}{P_{\rm amb}} ,
$$
  and the test statistic is
$$
D_2=\text{off}_2(e^{-1})-\text{off}_2(e^{+1}).
$$
- **The prediction.** If the outer links carry Run 72b's effect, linearly in ln a, D₂ ≈ +1.5% (± 0.6% from Run 72b's own error). If they do not, D₂ ≈ 0.
- **K75a:** PASS if D₂ ≥ 3σ; FAIL if D₂ ≤ 1σ; UNDECIDED otherwise.

**Results** (20 seeds per lattice; conservation exact in every run).

| outer links a | design | theory dip | measured dip | theory's error off_j |
|---|---|---|---|---|
| e^−1 = 0.368 | 1 | 0.33660 | 0.33783 ± 0.00036 | +0.37 ± 0.11% |
| e^−1 | 2 | 0.21007 | 0.21141 ± 0.00051 | +0.64 ± 0.24% |
| e^+1 = 2.718 | 1 | 0.26286 | 0.26362 ± 0.00031 | +0.29 ± 0.12% |
| e^+1 | 2 | 0.15263 | 0.15324 ± 0.00048 | +0.40 ± 0.31% |

- **D₂ = +0.24 ± 0.40%** (0.6σ). The registration expected σ_D ≈ 0.3%. The measured scatter was larger, so the test had less power than planned.
- D₁ = +0.08 ± 0.16% (reported).

![Run 75](figures/75_outerlinks.png)

**Verdict.**
- **K75a FAILS.** D₂ is within 1σ of zero. Changing only the outer links, by twice Run 72's amount, does not move the theory's design-2 error. The hypothesis is disfavoured, by odds of about 8:1 (the check), not excluded.
- D₂ sits 3.2σ below the hypothesis's central prediction of +1.5% on the measurement error alone, and 1.8σ below it once the prediction's own uncertainty is included.
- At 2σ, D₂ < 1.0%. So outer links could carry at most about two thirds of Run 72b's difference.

**What the check added.**

1. **Independent reproduction.** Every registered number was reproduced from the raw files with the checker's own code, and the verdict logic matches the registration.
   - The checker's own solver reproduces the theory's response matrices to 10⁻¹² and its own-dips to 10⁻⁶.
   - Its flat entry equals Run 72's flat theory.
2. **The registration and runs are clean.**
   - Every registered file matches its hash, and all 40 outputs were written after the hash time.
   - The parameters are as registered, conservation is exact, and no outputs are duplicated.
   - Seeds do not overlap any earlier run's.
   - The batch B restart did no harm: outputs are written only at the end of a run, and seeds 311 and 411 are complete.
3. **The lattice is as registered.** Only the outer x-links differ, each clock's own link is c_n, and the links are symmetric.
4. **What the FAIL means: disfavoured, not excluded.**
   - The likelihood ratio, no effect against the linear outer-link effect, is about 8:1.
   - With the prediction's own uncertainty, the true chance of a PASS under the hypothesis was about 0.67, not the planned 0.95.
   - **The broader form of the hypothesis also fails.** At a = e^+1 the clocks' places have more total outflow (3.44) than at negative curvature (2.85), yet the error stays at +0.40%. So "faster refill at the clocks" in general is disfavoured, not only the outer x-links.
   - A non-monotonic dependence, or one tied to other links, is not excluded.
5. **Post hoc: the design-2 error on every lattice** (high medium; each lattice has its own seeds).

| lattice | design-2 error | seed halves |
|---|---|---|
| flat (5 seeds) | +1.06 ± 0.64% | — |
| s = +1 | +0.70 ± 0.22% | +1.02 / +0.38 |
| a = e^−1 | +0.64 ± 0.24% | +0.46 / +0.81 |
| a = e^+1 | +0.40 ± 0.31% | +0.28 / +0.51 |
| s = −1 | −0.06 ± 0.17% | −0.26 ± 0.23 / +0.14 ± 0.24 |

   - **The other four agree:** χ² = 1.08 for 3 degrees of freedom, with a mean of +0.63 ± 0.14%.
   - **Negative curvature is the single outlier.** Locally it is 3.1σ (p = 0.0017). Corrected for picking it out of 5 lattices it is 2.6σ, or 2.4σ out of 10 cells. A homogeneity test of all five gives p = 0.027.
   - **It has weakened.** Run 72's original seeds (201–210), where it was first seen, deviate at 3.3σ. Run 72b's new seeds (211–220), in effect a replication, deviate by −0.49 ± 0.28% (1.8σ).
   - **A candidate mechanism (post hoc):** negative curvature is the only lattice where the theory's cross-coupling between the two designs, M₁₂, is negative.
     - offset = 0.25% + 2.9%·M₁₂ fits all five lattices.
     - The fit rests entirely on the s = −1 cell, so it restates the same 3σ rather than supporting it.
     - Theory-only screening shows a negative M₁₂ needs strong x-links and weak y/z-links together. So scaling only the y/z-links at the clocks would not discriminate.
6. **The cheapest decisive next test:** replicate the s = −1 lattice with 20 fresh seeds (about 1.1 hours), registered against the four-lattice baseline of +0.63 ± 0.14%.
   - If the full −0.69% deviation is real, it shows at about 3σ.
   - If the weaker −0.49% is the truth, about 2.2σ.
   - Only if it replicates is a mechanism test (a lattice screened to have a strongly negative M₁₂) worth running.
7. **Design 1** shows a uniform +0.2–0.4% theory underestimate on every lattice.

**Reading.**
1. **The outer links are not the main cause of the sign effect.** Both outer-link lattices sit with the flat and positive-curvature lattices, at a design-2 error of about +0.4 to +0.7%.
   - Run 72b's negative-curvature lattice remains the one cell near zero.
   - Corrected for having been picked out, it is now about 2.5σ, and it weakened from Run 72's seeds to Run 72b's (the check).
   - The sign effect is no longer well established. One replication with fresh seeds would settle it.
2. **The theory follows the links' effect on the clocks closely.** Changing the outer links moves the own-dips by 12–17%:
   - design 1: 0.2994 → 0.3366 and 0.2629;
   - design 2: 0.1797 → 0.2101 and 0.1526.
   The zero-range theory, fixed beforehand, tracks these changes to within 0.3–0.6% at both strengths.
3. **The theory's residual error is about +0.3% for design 1 and +0.6% for design 2** on every lattice tested, except possibly Run 72b's negative-curvature one. So the zero-range theory is accurate to about half a percent for these clocks.
4. **Limits:**
   - one p_s, high medium only;
   - the hypothesis's predicted size came from Run 72b's own uncertain slope;
   - the measured scatter was about a third larger than planned.
