## Run 57: realistic neutron-star equations of state, in CO's continuum equations

*20 October 2026. (step 2). Registered and hashed before the run (`eos57/PREREG_57.md`, 15:37 UTC). An independent agent checked the run; its corrections are included.*

**Question.** Run 55 left the pulsar's coefficient C spread over 0.33–0.49, from its unmeasured radius and two polytropes. With a realistic equation of state, the star of the pulsar's measured mass has a definite compactness. What are its C and U_s in CO's own equations? And, as reported (not registered as a test), what is CO's maximum neutron-star mass?

**Method: the engine's static equations in the continuum.** For a spherical star in the scale-free medium (G = c = 1):
$$
ds^2=-e^{-2U}dt^2+e^{2U}d\mathbf x^2,\qquad \frac1{r^2}\big(r^2U'\big)'=-4\pi\,(e+3p)\,e^{2U},\qquad h(n)\,e^{-U}=e^{-U_s}.
$$
- The field equation is U = (6/c)G∗d with the draw d = (ρ + 3p)N√γ per coordinate volume. The balance is N h = μ̃.
- Outputs:
  - M_far, the coefficient of 1/r outside;
  - the rest mass M₀ = ∫ n e^{3U} dV;
  - the areal radius R = r_s e^{U_s};
  - C = ⟨e^U⟩_T − 1.
- x = r e^{U_c} removes the unknown central potential; the integration runs in ln h (Lindblom's method).
- Equations of state: Read et al. 2009's piecewise polytropes (SLy crust; SLy, APR4 and MPA1 cores).

**Verdicts, as registered.**
- **K57a FAILS as registered, narrowly.** The continuum C at the lattice stars' U_s lies 0.2–1.1% below the lattice for Γ = 2 and 0.04–0.36% below for Γ = 3. One point is outside the registered 1%: Γ = 2 at U_s = 0.218, at −1.06%.
  - **The failure is lattice error, and the tolerance was set too tight** (the check). The 1% came from one 12-cell star at U_s 0.134, with no allowance for growth toward the fold.
    - Along Run 55's branch at h = ⅓ the gap grows from 0.26 to 1.07% as the star shrinks from 12 to 9 cells across.
    - For the same physical stars at h = ½, ⅓ and ¼ it falls as h². At the 12-cell star it is 0.57%, 0.26% and 0.14%, and extrapolates to −0.002%.
    - The FAIL stands as registered; the continuum solver is not in question.
- **K57b PASSES.** GR's TOV with the same code reproduces Read et al.'s Table III. That table lists the *tabulated* equations of state; the piecewise fits' own errors explain APR4's 1.1% (the fit: −1.08% in M_max, −0.90% in R₁.₄). Against the fits themselves the code agrees to ≤ 0.05%.

| | M_max (here / published) | R₁.₄ (here / published) |
|---|---|---|
| SLy | 2.048 / 2.049 | 11.71 / 11.74 km |
| APR4 | 2.188 / 2.213 | 11.32 / 11.43 km |
| MPA1 | 2.456 / 2.461 | 12.43 / 12.47 km |

- **K57c PASSES.** The Γ = 2 maximum of M₀ at fixed K is at U_s = 0.238, against the lattice's fitted fold at about 0.235. The lattice folds at a count about 1.5% lower.
  - M₀ and M_far peak at the same star, and the check found why: along every sequence dM_far/dM₀ = e^{−U_s} to 10⁻⁶. That is Run 50's first law plus the virial identity.
  - The coincidence also confirms the draw factors, since a wrong factor would break it.

**Reported: the pulsar and CO's maximum mass.**

| equation of state | CO: the 1.438 M☉ star (U_s, R, C) | P₀/p_s ≥ (2.3×10⁻⁶ / 1.5×10⁻⁶) | CO M_max | GR M_max |
|---|---|---|---|---|
| SLy | 0.244, 11.11 km, **0.474** | 2.1×10⁵ / 3.2×10⁵ | **1.65 M☉** | 2.05 |
| APR4 | 0.254, 10.77 km, **0.492** | 2.1×10⁵ / 3.3×10⁵ | **1.69 M☉** | 2.19 |
| MPA1 | 0.219, 12.06 km, **0.400** | 1.7×10⁵ / 2.7×10⁵ | **1.91 M☉** | 2.46 |

- In CO a star of given mass is more compact than in GR: for SLy at 1.4 M☉, 11.2 km against 11.7 km.
- **The check reproduced every number** with its own equation-of-state code and an independent shooting solver, to a few parts in 10⁵. It also confirmed the continuum equations from `star50.draws`: they are the Euler–Lagrange equations of the engine's action at fixed count.
- **No heavier static star exists for these equations of state.** M_far along the sequence is a damped spiral; for SLy it goes 1.646 at the peak, then 1.29, 0.99, 1.14 and 1.09 at h_c = 3, 10, 30 and 100. So "no static, spherical, cold equilibrium heavier than M_max" needs no stability criterion.
- CO's maximum-mass stars are causal at the centre (v_s² = 0.72, 0.94, 0.82).
- **CO's maximum mass is about 0.78 of GR's, and with all three standard equations of state CO fails PSR J0740+6620** (2.08 ± 0.07 M☉). All three maxima are below Run 59's FAIL line of 1.94.
  - SLy and APR4 also fail PSR J0348+0432 (2.01 ± 0.04).
  - Only MPA1 holds PSR J1614−2230 (1.908 ± 0.016), at 1.911.
  - GR holds J0740 with APR4 and MPA1, and SLy is within 1σ.
- **The registered stance:** maximum mass was reported, not tested. Run 59 tests it.

![Runs 57–59](figures/57_59.png)

**Reading.**
1. **With realistic equations of state, the pulsar's coefficient is C ≈ 0.40–0.49,** and the triple requires P₀/p_s ≳ 1.7–2.1×10⁵ (red noise) or 2.7–3.3×10⁵ (the planet model). This replaces Run 55's range of 1.4–2.9×10⁵. The remaining spread is the equation of state.
2. **CO's static strong field holds less mass than GR's.** The source term (e + 3p)e^{2U} grows deep in the well (e^{2U} ≈ 5.5–6 at the centre of a maximum-mass star), so stars turn over sooner. **With SLy, APR4 or MPA1 as they are, CO cannot hold the measured 2 M☉ pulsars.** Whether any allowed equation of state can is Run 59.
3. **Scope.** Option A (Run 44: "outside a compact object the field is GR's") covers black-hole exteriors only. The neutron-star interiors here are CO's own static equations. Whether a failure here could be absorbed by extending that tracked input to neutron-star interiors was put up for a ruling. It was ruled (20 October) that CO's interior equations bind (§3).
