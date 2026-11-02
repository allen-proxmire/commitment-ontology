### Run 104: clock universality under R1's amended outflow (a registered calculation, gravity sector)

*30 October 2026.*
- *Registered and hashed before the run (`modes104/PREREG_104.md`, 21:42:06 UTC). The builder's validation (V0–V2) passed; an independent pre-registration check was started and stopped before it reported, to save usage (disclosed in the PREREG). One post-run check (`check104/`) found no errors: the hashes verify, the analysis reruns byte for byte, and an independent recompute from the saved outputs reproduces every number.*
- *The run reuses Run 24's code by byte-identical copy and changes only the outflow table and the output paths.*

**Why.** Reading I18c's check found that Runs 23–24's clock-design gaps fit 1/c scaling as well as p_s scaling, so carried through R1's amended outflow (f = 0.99P below p_c, f = A + B ln P above, B = 0.99p_c) the clock bound is either p_c ≳ 4×10⁵ (through p) or ≳ 8×10⁴ (through B).

**The question.** Rerun Run 24's design under the amended outflow at p_c = 1, 4, 16 (two media, two seeds) and compare the gaps with two predictions from Run 24's own gaps: THROUGH p (the measured gap at p_s = p_c) and THROUGH B (Run 24's c/0.99 fit at p_c). A prediction fits at χ² ≤ 7.81 and is excluded at χ² > 11.35 (3 degrees of freedom). Only p_c = 1 discriminates (predictions 0.056 ± 0.003 and 0.081 ± 0.006).

**Result: UNRESOLVED.**

| p_c | gap |
|---|---|
| 1 | 0.0692 ± 0.0044 |
| 4 | 0.0236 ± 0.0024 |
| 16 | 0.0071 ± 0.0013 |

- THROUGH B fits, χ² = 4.15 (p = 0.25). THROUGH p is outside the fit band but not excluded, χ² = 10.18 (p = 0.017).
- At p_c = 1 the gap lies at t = 0.54 ± 0.23 of the way from the p prediction to the B prediction: between the two, as the zero-range theory column (0.071, reported, not tested) placed it.
- Reported, not tested: the gaps sit above Run 24's at equal p at every p_c (z = +2.39, +1.65, +1.31), and at 0.91–0.97 of the theory column.

**The bound** (registered as the run's own fit; inference):
$$
\text{gap}\propto p_c^{-0.81\pm0.06},\qquad \text{gap}=10^{-6}\ \text{at}\ p_c\approx1.0\times10^{6}\quad(1\sigma:\ 3.9\times10^{5}\text{–}2.7\times10^{6}),
$$
an extrapolation from three points over about five decades, conditional on Reading I6 ruling 4 (physical clocks do not dip themselves). The slope was registered as non-discriminating; neither the slope nor the bound favours either hypothesis.

**What it means.** The gap carries neither p alone nor B alone; under UNRESOLVED both carried-over figures (8×10⁴ and 4×10⁵) are kept, and the run's own extrapolation gives about 10⁶. Settling the p_c = 1 discrimination would need more seeds there, a new registration.

*Note, 31 October: Run 105 (eight seeds at p_c = 1) reads THROUGH B; the 4×10⁵ figure lapses (`run105_section.md`).*
