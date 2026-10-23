## Run 64 (a reading, not scored): what ED's rules leave open beyond first order

*20–21 October 2026. Writing ruling 2 out precisely enough to derive ED's second-order two-body dynamics showed that one choice it hides is a decision about ED's statics. This section sets out what is fixed, the decision, and what each option implies. Nothing here is scored. An independent agent checked it; its corrections are included.*

**What the rulings fix.**
- **First order is GR's, for any masses.** ED's g₀₀ = −e^{−2U_T}, where each body draws by its redshifted Tolman draw, gives
$$
U_T=\sum_A\frac{m_A\big(1+\tfrac32v_A^2-U_{\neg A}(x_A)\big)}{r_A},
$$
  and −1 + 2U_T − 2U_T² is GR's first-order g₀₀ written with conserved masses. Combined with γ = β = 1 and the Lorentz input (Run 34), the two-body dynamics are Einstein–Infeld–Hoffmann's.
- **The static two-body interaction is fixed exactly by the redshifted draw.** Without field self-energy (the vacuum draws nothing), the two-body Fokker Lagrangian at rest is
$$
L=-m_1e^{-\mu_2/r}-m_2e^{-\mu_1/r}-\frac{\mu_1\mu_2}{r},\qquad \mu_A=m_Ae^{-\mu_B/r}\ \ (\text{the draw }mN),
$$
$$
L=-(m_1+m_2)+\frac{m_1m_2}{r}-\frac{m_1m_2(m_1+m_2)}{2r^2}+\frac{m_1m_2(m_1^2+m_2^2)/6+m_1^2m_2^2}{r^3}+\dots
$$
  The G² term is Einstein–Infeld–Hoffmann's. The G³ term is ED's own, in ED's coordinates (`open64/static_two_body.py`).
- **The test-mass orbit in ED's static exterior is fixed (Run 63).**

**What they do not fix: whether the tension of the relations around a single body shears space.**
- **Run 11b's premise.** Radiation needs the relations binding a system to carry tension. Momentum conservation, ∂_μ(T^{μν} + t^{μν}) = 0, demands it, and the shear is sourced by matter's stress plus that tension.
- **The same law applies to a single static star.** Its matter's pressure gradient is balanced by the tension of its own relations,
$$
t_{ij}=\frac{1}{4\pi}\Big(\partial_iU\,\partial_jU-\tfrac12\delta_{ij}|\nabla U|^2\Big),\qquad \partial_jt_{ij}=-\rho\,\partial_iU .
$$
- **Patterns must feel the shear.** Gravitational-wave detectors register it through light travel times, and a body must feel it for radiation reaction to remove energy. So if a star's own tension sources shear, ED's static exterior is not exactly the exponential metric at second order. ED's statics (the engine's action, Runs 50–63) have no shear at all.

**A single number carries the physics (the check).** For circular orbits only g₀₀ and the areal radius R matter. Writing g₀₀ against Y = M/R as A = 1 − 2Y + kY³ + …, the test-mass second-order binding coefficient is exactly
$$
e_2=-rac{27}{8}+k .
$$
ED fixes g₀₀ = e^{−2U} with U = M/r in lattice coordinates, so where the shear is added on the lattice is physical. In GR the same freedom would be a choice of coordinates. The static shear is not pure gauge: removing its anisotropy with a radial coordinate shift leaves a residual −½U²δ_ij and changes g₀₀ at O(U³).

**The options.**

| option | what shears space | static exterior | k | test-mass 2PN coefficient (GR −27/8) | 2PN light deflection (GR 15π/4 (M/b)²) |
|---|---|---|---|---|---|
| **S2** | only tension between distinct bodies | unchanged (exponential) | −1/3 | −89/24 | 4π (M/b)² |
| **S3** | only the time-varying part of the tension | unchanged | −1/3 | −89/24 | 4π |
| **S4** | all tension, but patterns feel only its transverse-traceless part (a static spherical shear has none) | unchanged | −1/3 | −89/24 | 4π |
| **S1** | all tension, a body's own included, added in harmonic gauge (Run 11b's), no feedback on U | g_ij becomes GR's harmonic form at O(U²) | +2/3 | −65/24 | 15π/4 |
| S1, isotropic gauge | as S1, added in isotropic gauge | changed | +1/6 | −77/24 | 15π/4 |
| **S1 + feedback** | as S1, and the tension acts back on the cadence field in GR's form (c3) | GR's through second order | 0 | −27/8 | 15π/4 |

The coefficients are exact rational series (`open64/testmass_family.py`; the check's `check5759/i64/variants.py`). The same code gives GR's −27/8 in both harmonic and isotropic coordinates. The light deflection uses Epstein & Shapiro's π(2 + 2γ − β + ¾δ)(M/b)² with ED's δ = 4/3; it has not been measured at this order.

**The costs.**
- **S2, S3, S4 keep ED's statics (Runs 57–63)**, but each needs a rule for which tension counts:
  - S2 draws an arbitrary line inside extended matter;
  - S3's "time-varying" depends on the frame, against the Lorentz input;
  - S4's transverse-traceless part is nonlocal, so the near field couples nonlocally.
- **S1 changes the pattern rule:** light would no longer travel isotropically at c = N² in lattice coordinates (Run 28's rule).
- **S1 in either form changes ED's static field at second order**, so the neutron-star results (Runs 57–63) must be redone. That needs the shear rule written to all orders, including inside matter, because at a neutron star's centre U ≈ 0.5–1 and a second-order rule is not a controlled approximation.

**The time dependence (c1)** is not in question: time-symmetric near-zone fields, as the Lorentz input at every order requires.

**What the check added.**
1. **The first-order equivalence is confirmed.** Will's U uses the local proper density; with the conserved density ρ* = ρ(1 + v²/2 + 3U), 2U_Will + 4Φ₁ + 4Φ₂ = 2U_T exactly.
2. **The static Fokker Lagrangian is confirmed:** the field term's sign, stationarity in μ, and the series. The G³ term is coordinate-dependent (GR's differs between harmonic and ADM coordinates), so it is ED's own only in ED's coordinates.
3. **The static shear is physical**, not removable by a change of coordinates, and its effect reduces to the number k above. The gauge in which it is added, and any feedback on U, change k.
4. **S4 was missing** from the first draft, and so were S1's gauge and feedback variants.
5. **Corrections to the draft's reading.**
   - S1 without feedback moves ED further from GR (k from −1/3 to +2/3), not closer.
   - The effect on the neutron-star mass deficit (the draft said it "may shrink or change sign") has no calculation behind it. A GR-like completion would likely move ED's statics toward GR's. At neutron-star compactness the change could be of order 10% in M_max, sign and size unknown.

**Reading.**
1. **ED's second-order dynamics are not determined by its present rules, even for a small body orbiting a star.** The answer turns on one number, k (from −1/3 to +2/3 across the options), and on the comparable-mass terms and flux beyond it. So no second-order gravitational-wave or double-pulsar test of ED is meaningful until this is ruled.
2. **The choice is between keeping ED's statics and following Run 11b's logic to the end.**
   - S2, S3 or S4 keep every static result, at the price of a rule for which tension shears space.
   - S1 follows Run 11b, momentum conservation and the detectability of gravitational waves to their conclusion: every body's binding tension shears space.
   - With feedback in GR's form (S1 + feedback), ED's static exterior is GR's through second order, and ED's own content moves to higher order and the deep interior.
3. **S1 + feedback also points toward option B.** If ED's static field matches GR's beyond first order, black holes might come out GR-like from ED's own rules rather than by input (option A). Whether it does needs the nonlinear rule, which would also decide the neutron-star results.
