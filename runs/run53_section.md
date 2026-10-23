## Run 53: the far-field first law, surface-averaged and registered

*20 October 2026. Registered and hashed before the run (`firstlaw53/PREREG_53.md`, 11:41 UTC).*
- *The scans started about 6 minutes after registration. A waiting loop that never fired had to be replaced first; nothing had been computed.*
- *The h = ¼ scan used in the fit is Run 50's post hoc scan, disclosed as known.*
- *An independent agent checked the run; its corrections are included.*

**Question.** Run 50's far-field test was undecided as registered, because the miss oscillates with the star's surface cells. Post hoc, surface averages pointed to zero. This run registers that analysis: new radius scans at h = ⅕ and ⅙ with the fit fixed in advance.

**Design.**
- Run 50's Γ = 2 star in the scale-free medium, with the count fixed and K multiplied by f = 0.945, 0.9575, …, 1.045: 9 points per grid.
- The surface moves across 1.6–1.9 cells.
- The fit is weighted, c₀ + ah², over the means at h = ¼ (Run 50's 7 points), ⅕ and ⅙.

**Results** (far-field miss in units of b).

| h | points | mean | standard error |
|---|---|---|---|
| ⅓ (Run 50, post hoc; not in the fit) | 7 | +0.026 | 0.014 |
| ¼ (Run 50, post hoc) | 7 | +0.0165 | 0.0057 |
| ⅕ | 9 | +0.0118 | 0.0029 |
| ⅙ | 9 | +0.0086 | 0.0022 |

The scan points sample a quasi-periodic function, so these standard errors are uncertain by about 25%.

**Verdicts, as registered.**
- **K53a passes:** c₀ = +0.002 ± 0.006 b.
  - The fit extrapolates a long way: c₀ = −0.72 m(¼) − 0.23 m(⅕) + 1.95 m(⅙).
  - A constant, +0.010 ± 0.002 b, fits only slightly worse (χ² = 2.0 for 2 degrees of freedom).
  - Adding the h = ⅓ scan gives c₀ = +0.003 ± 0.005 b.
  - The main evidence that the miss depends on h is that all four means fall steadily. That would happen about 1 time in 24 if the miss were constant.
- **K53b fails as registered.** With the pattern's amplitude raised tenfold, the first-law residual is +4.4×10⁻⁷ at h = ⅕ and −1.1×10⁻⁷ at ⅙, above the registered 5×10⁻⁸. The check traced this to how ∫ω dκ was integrated, not to the physics:

| κ multiple | h = ⅕ | h = ⅙ |
|---|---|---|
| ×1 | +6.9×10⁻⁹ | −1.8×10⁻⁸ |
| ×3 | +5.4×10⁻⁸ | +8.5×10⁻⁹ |
| ×10 | +4.4×10⁻⁷ | −1.1×10⁻⁷ |

  - The registered test estimated the integral with the trapezoid rule, ∫ω dκ ≈ κ(ω₀ + ω₁)/2. At h = ⅕ that error grows as κ²:
    - integrating a quadratic ω(κ) exactly leaves 9×10⁻¹⁰ and −2×10⁻¹⁰;
    - at ×10, 48 surface cells switch off and ω(κ) has kinks.
  - At h = ⅙ the star sits on such a kink: 192 cells empty within the amplitude range. An 8-step trapezoid gives +9×10⁻¹⁰, and Simpson's rule +1.3×10⁻⁹.
  - **So the discrete first law holds to about 10⁻⁹.** The "~8×10⁻⁹" quoted in Runs 50 and 52–54 is trapezoid error. The registered threshold failed, not the first law.
- **The reported extras did not complete.**
  - The Γ = 3 existence scan made no progress in about 17 CPU-minutes and was stopped. Its log is empty.
  - The check notes that the solver returns no convergence flag, so such a scan could record a non-converged state as an equilibrium. It needs a flag and a time cap.
  - The weak-field case, run on its own afterwards with the same settings (`weak53.py`), gave U_self = 0.066, b = 0.062, first law 2×10⁻¹⁰, and a far-field miss of −0.013 b. That is a single star, not surface-averaged.

![Runs 52–54](../figures/52_54.png)

**Reading.**
1. **The far-field first law holds as registered.** Adding a quantum to a star in exact hydrostatic balance at neutron-star strength raises its far-field mass by its energy.
   - The continuum miss is consistent with zero: |c₀| ≲ 0.014 b at 2σ, about 0.3% of κω.
   - A constant offset near 0.01 b is disfavoured only weakly.
   - Adding h = 1/7, or more points per scan, would sharpen it.
2. **The old body model's 4% deficit is gone for a balanced star.** That it was *caused* by the old body model is an interpretation, consistent with Runs 49–50; this run did not test the old model.
3. **The first-law tests should integrate over amplitude with Simpson's rule** (adding ω at κ/2) and avoid kinks. The record's first-law precision is about 10⁻⁹.
