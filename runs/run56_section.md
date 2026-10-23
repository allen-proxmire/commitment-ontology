## 9zzb. Run 56: housekeeping — a finer scan, Simpson's rule, and a stiffer star

*20 October 2026. (step 4). Registered and hashed before the run (`house56/PREREG_56.md`, 12:41 UTC). An independent agent checked the run; its corrections are included. Two deviations are disclosed:*
- *The scan's 9th point was computed post hoc with the outer loop capped at 30 (`posthoc56_ninth.py`). In the registered run its composite cycled between two states 4×10⁻¹² apart, which never meets the 10⁻¹² stopping test, so it would have run for hours to the 200-iteration cap. The check estimates the cycle's effect on the miss at about 3×10⁻⁷ b.*
- *The fit's error is discussed beyond the registered form, at the check's suggestion.*

**Question.** Three loose ends from Runs 50–53:
1. Does the far-field first law still hold in the continuum with a fourth, finer grid?
2. With Simpson's rule, does the discrete first law hold to about 10⁻⁹, as Run 53's check expected?
3. Does a stiffer equation of state (Γ = 3), which stalled twice before, behave the same?

**Design.**
- **K56a.** Run 53's radius scan at h = 1/7: 9 points, K × f with f = 0.945 … 1.045, with the star's radius about 28 cells. The registered fit is weighted, c₀ + ah², over the scan means at h = ¼, ⅕, ⅙ and 1/7.
- **K56b.** The first law integrated by Simpson's rule,
$$
\Delta E\;\text{vs}\;\frac{\kappa}{6}\big(\omega_0+4\,\omega_{\kappa/2}+\omega_\kappa\big),
$$
  at the scan's middle point and at the Γ = 3 stars. PASS if every residual is ≤ 5×10⁻⁹.
- **Γ = 3.** An existence scan in K (20–2000) at h = ½, with a convergence flag and a time cap per solve. Then calibration to U_self = 0.2178 at radius 8.3 cells, and the first law and far-field miss at h = ½ and ⅓.

**Results: the h = 1/7 scan** (far-field miss in units of b).

| f | radius (cells) | U_self | miss (b) | first law (trapezoid) |
|---|---|---|---|---|
| 0.945 | 27.000 | 0.2249 | −0.0046 | 7.2×10⁻⁹ |
| 0.9575 | 27.302 | 0.2224 | −0.0026 | 6.6×10⁻⁹ |
| 0.970 | 27.594 | 0.2200 | −0.0032 | 8.0×10⁻⁹ |
| 0.9825 | 27.877 | 0.2176 | +0.0049 | 9.3×10⁻⁹ |
| 0.995 | 28.162 | 0.2153 | −0.0032 | 7.5×10⁻⁹ (Simpson 1.6×10⁻⁹) |
| 1.0075 | 28.449 | 0.2131 | −0.0011 | 7.3×10⁻⁹ |
| 1.020 | 28.727 | 0.2110 | +0.0050 | 5.2×10⁻⁹ |
| 1.0325 | 28.996 | 0.2089 | −0.0067 | 6.6×10⁻⁹ |
| 1.045 (post hoc, capped) | 29.277 | 0.2068 | +0.0047 | −9.3×10⁻⁸ |

The last point's larger trapezoid residual is a kink: in the check's reproduction, 78 surface cells switch on inside the composite (Run 53's finding). It is not a K56b point.

| h | points | mean miss (b) | standard error |
|---|---|---|---|
| ¼ (Run 50, post hoc) | 7 | +0.0165 | 0.0057 |
| ⅕ (Run 53) | 9 | +0.0118 | 0.0029 |
| ⅙ (Run 53) | 9 | +0.0086 | 0.0022 |
| 1/7 | 9 | −0.0007 | 0.0015 |

**Verdicts, as registered.**
- **K56a: PASS, on the line, and resting on the post hoc point.** c₀ = −0.0097 ± 0.0032 b (χ² = 5.6 for 2 degrees of freedom), against the PASS threshold |c₀| ≤ 0.01.
  - **The PASS depends on the 9th point.** With the 8 registered points c₀ = −0.0107 (UNDECIDED); any 9th miss below +0.0038 would have left it UNDECIDED. The capped point is a fair stand-in for the registered one: the cycle changes its miss by about 3×10⁻⁷ b, against a margin of 9×10⁻⁴ b.
  - **The fit leans on the new grid:** c₀ = 1.54 m(1/7) + 0.18 m(1/6) − 0.39 m(1/5) − 0.34 m(1/4). The h = 1/7 mean is 5σ below Run 53's fit extrapolated to h = 1/7 (+0.0067).
  - **The quoted error is too small.** The points are samples of a deterministic function of the surface radius, and χ²/dof = 2.8. Scaling by √(χ²/dof) gives ±0.0054. Dropping one grid at a time gives c₀ from −0.014 to +0.002.
  - **The form is not established.** c₀ + ah fits slightly better (χ² = 3.9) and gives c₀ = −0.028 ± 0.009 b (χ²-scaled), near the FAIL line (0.03). A star's sharp surface can give lattice errors of first order in h.
  - **A constant is excluded** (χ² = 26.6 for 3), so the miss does depend on the grid.
- **K56b: PASS.** Simpson residuals are +1.6×10⁻⁹ (h = 1/7, middle point), +5.8×10⁻¹⁰ (Γ = 3, h = ½) and +2.0×10⁻¹⁰ (Γ = 3, h = ⅓).
- **Γ = 3, reported.**
  - All 11 K converged (U_self from 0.29 at K = 20 to 0.09 at K = 2000), bracketing 0.2178. Calibrated to U_self = 0.21780 at radius 8.300 cells (residuals ≤ 2×10⁻¹²). The h = ⅓ star is that star rescaled (count × 3/2, K × (2/3)⁻⁴), not recalibrated, so its U_self is 0.2169.
  - The calibration and the composites carry no convergence flag. The first-law residuals of ≤ 6×10⁻¹⁰ show they converged.
  - Far-field misses: −0.030 b (h = ½) and +0.045 b (h = ⅓). These are single stars, within the surface scatter seen at those grids.
  - The lattice virial defect falls 6.7× from h = ½ to ⅓, where h² would give 2.25×, so no h² convergence is claimed for Γ = 3.
  - Run 53's stall is not explained: its scan started at K = 5, this one at K = 20.

**Reading.**
1. **The discrete first law holds to ≤ 2×10⁻⁹ with Simpson's rule, at three kink-free points and for both equations of state:**
$$
\frac{dE_H}{d\kappa}=\omega,\qquad E_H=W_f+k_0\sum\nu N(1+\varepsilon)+\kappa\omega .
$$
2. **The far-field first law: zero in the continuum is analytic, and the grids are consistent with it to about 1%.** That c₀ = 0 in the continuum follows from the dilation symmetry (Run 50). The four grids neither confirm nor contradict it to better than about 1% of κω: the 2σ envelope across fit forms reaches about 0.05 b (b ≈ 0.2), and the form of convergence (h² or h) is unsettled. This supersedes Run 53's "≲ 0.3% of κω". Either way it is far from the old body model's 4% (−0.20 b).
3. **Solver housekeeping.** Future scans should record the outer iteration count and flag any point that reaches the cap.

![Runs 55–56](figures/55_56.png)
