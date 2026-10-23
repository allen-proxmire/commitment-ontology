### Run 82: the speed of the relations' stretch waves in a well (Note H, test H2; a calculation)

*23 October 2026.*
- *Registered and hashed before it was run (`speed82/PREREG_82.md` with `speed82.py`, 21:33:20 UTC).*
- *A convergence study was run afterwards and is labelled post hoc.*
- *An independent agent checked the run (below). Its scoring corrections are adopted.*

**Question.** Note H's carrier (C2) is a stretch carried by the relations. Its waves must move at light's speed at infinity and in wells. The GW170817 bounds (ApJL 848 L13, §§4.1 and 4.3) are
$$
-3\times10^{-15}<\frac{\Delta c}{c}<7\times10^{-16},\qquad -2.6\times10^{-7}<\gamma_{GW}-\gamma_{EM}<1.2\times10^{-6}.
$$
CO's light gets c = N² from two factors, its place's ticks and its free capacity (R6). **Which formulation of the stretch's restoring energy gives its waves light's speed?**

**The calculation.**
- **The wave equation.** Take the quadratic action N√γ[K_ijK^ij + ξR] with K_ij = ḣ_ij/(2N), on a static background with lapse N = e^{−U} and spatial metric γ_ij = A²δ_ij. For a transverse-traceless amplitude u, along a ray and in the eikonal limit:
$$
\partial_t\!\Big(\frac{A^3}{N}\,\partial_tu\Big)=\partial_x\big(\xi\,NA\,\partial_xu\big),\qquad c_h=\sqrt{\xi}\,\frac{N}{A}.
$$
- **Two formulations of the space the wave rides on,** with A = 1 + γ_sU at first order:
  - **(i) the medium's space γ̃,** flat at first order: A = 1, so c_h = √ξ N;
  - **(ii) physical space g = N⁻²γ̃,** with PPN γ = 1: A = N⁻¹, so c_h = √ξ N².
- **Light** (R6: the wave equation in −N²dt² + N⁻²dx²) obeys ∂_t(N⁻⁴∂_tφ) = ∂_x²φ, which is (ii)'s equation at ξ = 1.
- **Shapiro delay** along a straight ray:
$$
\Delta T=\int\Big(\frac1{c_h}-1\Big)dx\simeq(1+\gamma_s)\int U\,dx\quad\Rightarrow\quad\gamma_{GW}=\gamma_s,\qquad\gamma_{EM}=1 .
$$
- **Numerics.**
  - A Gaussian packet (k = 1, σ = 12) crosses U = M/√(x² + b²), with M = 1 and b = 50, on a path of ±2000. The grid has Δx = 0.25, and the scheme is leapfrog at CFL 0.4.
  - The delay against flat space is read from the envelope peak at a detector, and divided by ∫U dx to give the statistic 1 + γ.

**Registered predictions.**
- **(i):** γ_GW = 0 and Δγ = −1, so excluded by GW170817.
- **(ii):** γ_GW = 1 and Δγ = 0, since it has the same equation as light; so it passes.
- **γ_s = 0, 0.5, 1:** γ_GW = γ_s.
- **Tests:**
  - K82a–c: the γ statistic within 10⁻³ of these values;
  - K82d: each numerical delay within 10⁻³ of its eikonal integral.

**Results** (registered run, Δx = 0.25, k = 1).

| medium | numerical delay | eikonal ∫(1/c_h − 1)dx | numerical/eikonal | statistic delay/∫U − 1 | registered value |
|---|---|---|---|---|---|
| light | 17.328 | 17.003 | 1.0191 | 1.053 | 1 |
| (ii) physical space | 17.328 (light's, to 3×10⁻¹³) | 17.003 | 1.0191 | 1.053 | 1 |
| (i) medium space | 8.631 | 8.470 | 1.0189 | 0.023 | 0 |
| γ_s = 0.5 | | | 1.0190 | 0.536 | 0.5 |
| γ_s = 1 | | | 1.0191 | 1.049 | 1 |

The ratio delay(i)/delay(light) is 0.4981. Its eikonal value is 0.4982, and 0.5 at first order.

**Verdicts as registered.** The registered outcome and the physics status are kept separate, as the check required.

| test | registered outcome | physics status |
|---|---|---|
| K82a | **FAIL.** γ_GW(i) = 0.0227, against 0 ± 10⁻³. | (i) is excluded by GW170817 regardless: Δγ = −1.03 numerically, −1.011 eikonal, −1 at first order, against a lower bound of −2.6×10⁻⁷. |
| K82b | **FAIL.** γ_GW(ii) = 1.053, against 1 ± 10⁻³. The delay-equality clause holds, but by construction (below), so it carries no weight. | (ii) has c_h = c identically, so Δγ = 0: compatible with GW170817. |
| K82c | **FAIL.** Offsets +0.023, +0.036, +0.049. | γ_GW = γ_s at first order, confirmed analytically. |
| K82d | **FAIL.** Ratios 1.0189–1.0191, against 1 ± 10⁻³. | The excess is the scheme's dispersion (post hoc, below). |

**All four registered tests fail on their tolerances. The registered physics predictions are confirmed analytically and by post hoc numerics.**

**What the check added.**
1. **Reproduction and integrity.**
   - Both hashes match, and the file times are consistent with registration before the run.
   - The registered run reproduces bit for bit.
2. **K82a–c could not have passed at any resolution: a design error in the registration.**
   - At M/b = 0.02, the statistic delay/∫U − 1 is not γ. Its exact eikonal values are:
$$
\frac{1}{c_h}-1=(1+\gamma_s)\,U+\big(\gamma_s+\tfrac12\big)\,U^2+O(U^3),\qquad \frac{\int U^2}{\int U}=0.0073 ,
$$
     which give offsets of +0.0037 for (i), +0.0073 for γ_s = 0.5, +0.0110 for γ_s = 1, and +0.0147 for light and (ii). That is 3.7–15 times the tolerance.
   - A 10⁻³ tolerance would have needed M/b ≲ 1.4×10⁻³, a fit of the linear coefficient across several masses, or tolerances set against the exact eikonal integrals.
3. **The 1.9% excess is leapfrog dispersion,** of a specific kind.
   - The scheme's group-velocity error at ν = 0.4 and kΔx = 0.25 is only −0.66%. What enters the delay is how the slowness error changes with the local speed, which gives (3 − ν²)(kΔx)²/8 = 2.22%.
   - The figure drops to 1.91% because the packet is launched with k = 1 inside the well, at a slightly lower frequency than the flat reference.
   - Integrating the exact discrete group slowness along the path predicts every numerical delay to 9×10⁻⁵.
   - K82d would have needed kΔx < 0.057.
4. **K82b's delay-equality clause holds by construction.** The script's coefficient arrays for (ii), ((1/N)³/N, N·(1/N)), and for light, (N⁻⁴, 1), are the same to rounding. So the delays agree whatever the scheme does. The case for (ii) rests on the analytic identity c_h = c, which the check confirmed.
5. **The wave equation and light's equation, checked independently.**
   - The reduction was confirmed by a finite-difference Christoffel/Ricci computation, to 2×10⁻⁷. The eikonal limit drops a mass term 2ξMu, here 4×10⁻⁶ of the gradient term, as well as ray bending, spreading and mode coupling. None of these changes the first-order delay.
   - **"Term for term" holds for R6's minimally coupled scalar and the mixed-index amplitude u = h^i_j.** Maxwell's A_y obeys ∂_t(N⁻²∂_tA_y) = ∂_x(N²∂_xA_y): the same speed, but a different equation. The invariant content is that the two speeds, and so the two delays, are equal.
   - Likewise, "the TT parts of γ̃ and g are equal" holds for the mixed-index strain. The lower-index components differ by N⁻².
6. **The bounds** were confirmed against the paper. |Δγ| = 1 is about 3.8×10⁶ times the size of the lower bound, and ξ − 1 must lie in (−6×10⁻¹⁵, 1.4×10⁻¹⁵).
7. **The test fixes the cone, not the space** (the check's main correction to the reading).
   - Write A = 1 + γ_sU and ξ = 1 + ξ₁U. Then 1/c_h − 1 ≈ (1 + γ_s − ξ₁/2)U, so
$$
\gamma_{GW}=\gamma_s-\tfrac12\,\xi_1 .
$$
     GW170817 requires that this be 1 to 10⁻⁶: the wave's effective metric, −N²dt² + (A²/ξ)dx², must have light's cone.
   - **With constant ξ and the GR lapse coupling, this forces γ_s = 1, so (i) is excluded.**
   - But the second factor of N can sit in any of three places with the same speed:
     - **in the space:** A = N⁻¹, formulation (ii);
     - **in the stiffness:** (i) with ξ = N² has c_h = N²;
     - **in the clock:** with K_ij = ḣ_ij/(2N^p), c_h = √ξ N^p/A, so (i) with p = 2 has light's speed.
   - In CO's terms, the clock version means the stretch's rate is gated by both place ticks and free capacity, as light's is in R6.
   - These options differ only in the wave's impedance, √(aβ): N⁻² for (ii) against N for (i) with ξ = N². In a static well the amplitude returns to its asymptotic value, so far-field tests do not separate them at this order.
8. **Missing from the registered Limits:**
   - an overall conformal weight of the action, which no speed test constrains;
   - non-TT modes;
   - frequency dependence, since a medium with a microscopic scale can make c_h depend on frequency (GW170817 tests about 100 Hz);
   - the cosmological background along most of the 40 Mpc path, which the "at infinity" requirement on ξ assumes coincides for the wave and light;
   - second order: A = 1 + U and A = N⁻¹ differ at O(U²), which GW170817 does not probe.
9. **Smaller points.**
   - The hashed script's docstring names a cross-correlation estimator; the code uses the Hilbert-envelope peak, as the registration states.
   - A one-step time label gives a bias of at most 6×10⁻⁶ relative.
   - The integration window is short by half a cell, 3.5×10⁻⁵ relative.

**Post hoc (not registered): convergence.** Five resolutions, kΔx from 0.25 to 0.031 (figure, panel b).
- Numerical/eikonal − 1 falls as 0.31·(kΔx)², to 1.0003 at kΔx = 0.031. Richardson-extrapolated, it agrees with the eikonal integral within 5×10⁻⁶.
- delay(i)/delay(light) is 0.4981–0.4982 at every resolution: (i) carries half light's delay.
- delay(ii)/delay(light) is 1 to 10⁻¹² at every resolution.

![Run 82](../figures/82_speed.png)

**Reading.**
1. **At first order, the stretch wave's effective metric must have light's cone,** −N²dt² + N⁻²dx² up to a conformal factor.
   - Note H §4's statement holds: updating a relation's stretch on its places' ticks alone gives c_h = N, γ_GW = 0, and Δγ = −1. That is excluded by a factor of about 3.8×10⁶.
   - **A second factor of N is required.** Physical space (ii) supplies it, and so do the two alternatives the check found. All three give light's speed, and this test cannot tell them apart.
   - The registered reading's "the stretch's propagation must be gated as patterns are" is the correct general statement. "Rides on physical space" is the simplest way to realise it, not the only one.
   - **The gate closest to R6 is the clock version:** the stretch's rate gated by both ticks and free capacity, as light's is.
2. **Which version CO's rule uses is a question for the engine (H5).** Each puts the factor somewhere different: in the space, the stiffness or the clock. They differ in the wave's impedance, which a test of the amplitude in a well, or of second order, could separate.
3. **ξ = 1 to 10⁻¹⁵ remains a requirement on the energy's normalisation.** It is not derived here.
4. **Two lessons for registering calculations.**
   - Set tolerances against the exact eikonal integrals, or use a weak enough well. At M/b = 0.02, second-order terms exceed 10⁻³.
   - Check kΔx against the scheme's dispersion before registering.
5. **Limits.**
   - First order, eikonal, a straight ray, TT only, static well.
   - It tests the formulation, not a lattice rule.
