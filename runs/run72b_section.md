## 9zzu. Run 72b: doubled seeds for Run 72's design-gap contrast

*21 October 2026. The recommendation, after Run 72's check, was to double the seeds for both signs of curvature so the design-gap contrast could reach the registered bar. Registered and hashed before any new engine run (`curve72/PREREG_72b.md`, 16:05:50 UTC). The engine, geometry, theory and its output are Run 72's files, unchanged and hashed again.*
- *The registration's header says 18:10 local; it was hashed at 18:05:50 local (16:05:50 UTC). The first new run finished at 16:12:58 UTC.*
- *The 40 runs were made in two batches, to stay inside the session's two-hour task limit. The runner skipped any job whose output already existed.*
- *An independent agent checked the run (below).*

**Question.** Run 72 found the design gap moving with the sign of curvature as the zero-range theory predicts:
- the contrast was +0.0079 ± 0.0032, against the theory's +0.0096;
- that is 2.5σ from zero, short of the registered 3σ, so K72d was UNDECIDED.

With twice the seeds, is the contrast real, and is it the theory's size?

**Optional stopping, and how the registration handles it.** Adding seeds after seeing a result that is not significant inflates the chance of a false detection, if one would have stopped had the result been significant. So two verdicts were registered:
- **K72d-R, a clean replication on the new seeds alone** (10 per sign). PASS if within 2σ of theory and at least 2σ from zero.
- **K72d-C, all 20 seeds per sign,** with the bar raised from 3σ to 3.2σ for the second look (a Pocock-type correction). PASS if within 2σ of theory and at least 3.2σ from zero.
- Either fails if the contrast differs from the theory by more than 3σ.

**The runs.** 40 new engine runs, identical to Run 72's in everything but the seeds:
- s = +1 (clocks at R̃ = +1.10): seeds 111–120;
- s = −1 (clocks at R̃ = −1.10): seeds 211–220;
- each at the high and the low medium;
- p_s = 1, λ = 0.25, c_n = 0.4463, Run 24's 216-probe layout, 20,000 ticks.
- The flat control (seeds 1–5) is unchanged; it does not enter the contrast.
- Charge is conserved exactly in every run.

The gap is computed per seed pair (high and low runs with the same seed):
$$
\text{gap}=1-\frac{\kappa_1}{\kappa_2},\qquad \kappa_j=\frac{1-r_j^{\rm low}/r_j^{\rm high}}{\varepsilon_{\rm amb}},\qquad \varepsilon_{\rm amb}=1-\frac{P_{\rm amb}^{\rm low}}{P_{\rm amb}^{\rm high}},
$$
where r_j is design j's mean tick rate. The contrast is
$$
c=\overline{\text{gap}}(+1)-\overline{\text{gap}}(-1),
$$
with errors from the seed-to-seed scatter. The theory's contrast, fixed before Run 72, is +0.0096.

**Results.**

| | gap(+1) | gap(−1) | contrast | from zero | from theory |
|---|---|---|---|---|---|
| theory (fixed beforehand) | 0.0840 | 0.0744 | +0.0096 | | |
| Run 72 (seeds 101–110, 201–210) | 0.0830 ± 0.0026 | 0.0751 ± 0.0019 | +0.0079 ± 0.0032 | 2.5σ | −0.5σ |
| **new seeds alone (K72d-R)** | 0.0869 ± 0.0022 | 0.0734 ± 0.0016 | **+0.0135 ± 0.0027** | **5.0σ** | +1.4σ |
| **all 20 seeds per sign (K72d-C)** | 0.0850 ± 0.0017 | 0.0743 ± 0.0012 | **+0.0107 ± 0.0021** | **5.1σ** | +0.5σ |

![Run 72b](figures/72b_gapcontrast.png)

**Reported on all seeds: the own-dip ratios.** These are the curved/flat ratios of each design's own dip.
- All eight rows agree with the theory within 1.7σ; seven of the eight sit below it.
- The amplitude fitted to all eight (registered covariance, with the shared flat control) is A = 1.007 ± 0.014.
- By sign: A₊ = 0.966 ± 0.036 and A₋ = 1.020 ± 0.053.
- The theory's χ² is 15.2 for 8 degrees of freedom (p = 0.056).
  - On Run 72's seeds alone it is 15.1; on the new seeds alone, 8.2 (post hoc).
  - The first guess was that the 5-seed flat control, which divides every row, caused the common low shift. The check showed it does not (below).
- Each sign's shift from the flat control alone is still not resolved:
  - +0.0047 ± 0.0039 at positive curvature (theory +0.0018);
  - −0.0060 ± 0.0037 at negative curvature (theory −0.0078).
  - The flat control's 5 seeds limit both.

**Verdicts.**
- **K72d-R PASSES.** The new seeds alone give +0.0135 ± 0.0027: 5.0σ from zero, within 1.4σ of the theory.
- **K72d-C PASSES.** All seeds give +0.0107 ± 0.0021: 5.1σ from zero (bar 3.2σ; the plain 3σ is also met), within 0.5σ of the theory.
- Run 72's K72d, UNDECIDED at 2.5σ, is settled.

**What the check added.**

1. **Independent reproduction.** Every number was reproduced from the raw files with the checker's own code: the seed pairing, the gap, the per-seed errors and the verdict logic, which matches the registration exactly.
   - One-sided Welch p-values: 7×10⁻⁵ for the replication, 7×10⁻⁶ combined.
   - Run 72's seeds alone and the new seeds alone differ by 1.3σ, which is consistent.
   - The two batches agree: contrasts +0.0132 and +0.0138.
2. **The registration and the runs are clean.**
   - Every registered file matches its hash.
   - All 40 new outputs are real files, made after the hash time.
   - Each batch ran all 20 of its jobs, so no stand-in file used to test the analysis was skipped as finished.
   - All 90 runs have the registered parameters, and conservation is exact in every run.
   - No two runs share outputs, and no seed overlaps Run 72's.
   - Run 72's strong high/low anti-correlation across seeds (r = −0.72) did not recur (−0.01 and −0.23), so it was most likely chance. The seed-paired error is valid either way.
3. **Optional stopping.**
   - The replication's data played no part in the decision to extend, so its 5.0σ stands as it is.
   - For the combined test, the Pocock constant for two equal looks at an overall 3σ is 3.18; the registered 3.2 is right.
   - At 5.1σ the result survives any reasonable correction.
4. **The first explanation of the χ² was wrong.** The cause is not the flat control.
   - **A free normalisation of the flat control barely helps:** χ² falls from 15.2 to 13.4.
   - **The seed subsets rule it out.** Run 72's seeds and the new seeds share the same flat control, yet give χ² of 15.1 and 8.2.
   - **The absolute fits locate the miss.** Comparing each cell's own dip directly with the theory (the checker's full covariance), the theory is low by:

| lattice | design 1 | design 2 |
|---|---|---|
| flat | 0.36 ± 0.16% | 0.96 ± 0.40% |
| R̃ = +1.10 | 0.16 ± 0.07% | 0.75 ± 0.13% |
| R̃ = −1.10 | 0.19 ± 0.09% | −0.09 ± 0.19% |

   - So the theory's design-2 error, about 1%, holds everywhere except at negative curvature, where it vanishes.
     - The two signs differ by 0.84 ± 0.24%, about 3.5σ.
     - One offset per lattice and design fits (χ² 1.7 for 6 degrees of freedom); one offset per design does not (20.8 for 10).
   - That is within the theory's known accuracy, and inside K72a's 3% tolerance, so it is not a falsification. It is a real, curvature-dependent part of the theory's roughly 1% error.
   - The checker's hypothesis, not tested: at negative curvature the clocks' outer links are 1.65 times stronger, so the medium mixes faster and the mean-field theory is more accurate there.
5. **The separate amplitudes depend on the estimator.**

| estimator | A₊ | A₋ |
|---|---|---|
| registered: each sign fitted on its own | 0.966 ± 0.036 | 1.020 ± 0.053 |
| joint fit, registered covariance | 1.047 ± 0.023 | 0.937 ± 0.035 |
| joint fit, full covariance | 1.009 ± 0.019 | 0.944 ± 0.027 |

   - Fitting each sign on its own ignores that both divide by the same flat control, which is why it reverses the order.
   - With the full covariance the shortfall at negative curvature that Run 72's check found (1.2σ then) persists at 1.75σ. It is the same design-2 effect as above.
   - With the full covariance, the overall amplitude is 0.985 ± 0.013 and χ² is 20.5 for 8 degrees of freedom (p = 0.009).

**Reading.**
1. **The design gap moves with the sign of curvature, by the theory's amount.**
   - The replication alone clears the bar. The combined contrast matches the prediction fixed before Run 72 to half a standard deviation.
   - Each sign's gap matches its own prediction: +0.6σ at positive curvature, −0.1σ at negative.
2. **What this shows, and what it does not.** On an equal-place lattice with imposed curvature at p_s = 1, the clocks' design-dependent response to curvature is the zero-range theory's, in sign and size, at both signs.
   - That is the theory's mechanism confirmed. It is not universality shown directly.
   - At physical scales the theory makes the design-dependent part about 0.01·R̃·h·ℓ_c, roughly 10⁻³⁹ for a neutron star.
   - It is still untested on a lattice curved by the medium's own stress, and at large p_s.
3. **The theory's own accuracy, about 1% for design 2, depends on the sign of the curvature** (the check, about 3.5σ).
   - It does not affect the contrast, which matches the theory to 0.5σ.
   - It does mean the row-level tests are now limited by the theory, and by the flat control's 5 seeds, rather than by the curved runs.
4. **Limits:**
   - one lattice (λ = 0.25) and one p_s;
   - the curvature is imposed, not solved from the medium's stress;
   - the flat control has 5 seeds;
   - the mixing explanation of the design-2 offset is untested.
   - A cheap test of that explanation: run the theory against the engine with one parameter changed (λ = 0.125, or p_s = 4).
