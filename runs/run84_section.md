### Run 84: a kinetic form that keeps GR's constraint structure exactly on the lattice (Note H, test H1, second attempt; a calculation)

*23–24 October 2026.*
- *Registered and hashed before the run (`modes84/PREREG_84.md`, with the code, the theory and every validation output, 23:36:43 UTC).*
- *Run 82's and Run 83's lessons were applied. Before registration the numerics were validated on the lattice, at the registered k, against 50-digit arithmetic and a second reduction. Those comparisons computed registered-case frequencies but printed only discrepancies; the registration's heading "no frequency of any registered case was computed or printed" overstates this (the check). Exact singular structures were handled exactly.*
- *An independent agent checked the run with its own construction, its own Hamiltonian (Dirac) reduction and 50-digit arithmetic (below). Its corrections are adopted. The figure was made after the run, and its titles were revised after the check.*

**Question.** Run 83's check traced every failure of the per-tetrahedron kinetic form to one term, the shift's longitudinal kinetic form:
$$
g_L^\dagger G g_L=2(1-\lambda)k^2+\mu_L(\hat k)\,k^4,\qquad\mu_L\ge0 .
$$
The continuum has no k⁴ term. At λ = 1 that term left the conformal mode unfrozen and the Hamiltonian constraint second class; for λ > 1 it set the khronon's onset of instability at k* ≈ √(2(λ−1)/μ_L). **The criterion:** the longitudinal part exactly proportional to (1 − λ) at every k, and the kinetic form's inertia the same across the zone. **With a kinetic form built to meet it, and the lapse coupling taken from the same construction, do GR's route and the khronometric route become healthy?**

**The construction.**
- **A metric at each place,** read from six of its seven relations by finite differences (E_a = e^{ik_a}, δ_a = E_a − 1):
$$
h_{aa}(o)=2q_a(o),\qquad h_{ab}(o)=q_{ab}(o)-q_a(o+e_b)-q_b(o+e_a)\quad(a<b).
$$
  Under sliding places it moves exactly as a continuum metric does, with one vector symbol for every component:
$$
h_{ab}\to h_{ab}+\delta_au_b+\delta_bu_a .
$$
- **The kinetic energy** is the DeWitt form, with the trace read from the three axis relations *arriving* at the place:
$$
T=\sum_o\tfrac14\Big[\dot h(o):\dot h(o)-\lambda\Big(\sum_a\dot h_{aa}(o-e_a)\Big)^2\Big].
$$
  - **What this is (the check).** Up to a phase per component, h(o) is the metric of the six relations arriving at one place p,
$$
h_{aa}(p)=2q_a e^{-ik_a/2},\qquad h_{ab}(p)=q_{ab}e^{-i(k_a+k_b)/2}-q_ae^{-ik_a/2}-q_be^{-ik_b/2},
$$
    and the arriving trace is that metric's own trace. It is the ordinary DeWitt form of one vertex metric, not a fix.
- **Then, exactly, at every k:**
$$
g^\dagger Gg=|\delta|^2I+(1-2\lambda)\,\delta\delta^\dagger,\qquad g_L^\dagger Gg_L=2(1-\lambda)|\delta|^2,\qquad|\delta|^2=\sum_a4\sin^2\tfrac{k_a}{2}.
$$
  The cross term in h:h̄ is 2|δ†u|², and the arriving trace of a shift is −2δ†u, so
$$
u^\dagger g^\dagger Gg\,u=|\delta|^2|u|^2+(1-2\lambda)\,|\delta^\dagger u|^2 .
$$
  - **Two variants were rejected on the way.** Read at the place itself, the trace gives |δ^Tu|² instead, and the shift's form acquires a negative eigenvalue at λ = 1. Validation caught this before registration. Centred differences satisfy the identity but vanish on the planes k_a = π (doublers).
- **The body diagonal** is not read by h. Its own inertia is either absent (**N0:** auxiliary, fixed each instant by the energy) or (m/2)|ν̇|² with m = 1 (**N1**), where
$$
\nu^\dagger q=-\tfrac1{14}\,v^\dagger D\,A(k)\,D\,q,\qquad v=(1,1,1,-1,-1,-1,1)/\sqrt7,
$$
  is a local, gauge-invariant non-metric coordinate. The check found it is the potential's gradient along the non-metric vector.
- **The potential is Regge's energy,** as in Run 83.
- **The lapse coupling,** c_G = ξ G_h(λ = 1) g δ. It is gauge invariant, because δ is the null vector of g†G₁g. **The check found that it equals Regge's end-average coupling (Run 83's) exactly, at every k** (below).
  - At λ = 1 the shift direction δ has zero kinetic energy and G g δ ∥ c_G, so **the Hamiltonian constraint is first class by construction.**
  - The α term uses κ = |δ|², which equals Run 83's P1 form exactly.
- **What follows before any potential is considered.** Haynsworth's inertia theorem, with the shift's form above, makes the reduced kinetic form positive definite for λ > 1, for λ < 1/3, and on GR's constraint surface. **So health is decided by the potential side alone.** (For N1 this needs ν₇ ≠ 0, which fails on one curve in the zone; see the check.)

**Cases** (ξ = 1). Scalar predictions from N√γ[K_ijK^ij − λK² + ξR + αa_ia^i]:
$$
c_s^2=\xi\Big(\frac{2\xi}{\alpha}-1\Big)\frac{\lambda-1}{3\lambda-1}.
$$

| case | λ | α | predicted | modes (N0 / N1) |
|---|---|---|---|---|
| A, GR's route (lapse a multiplier) | 1 | — | 2 TT at c² = 1; N1 also the gapped non-metric mode | 2 / 3 |
| B1 | 1.05 | 0.1 | c_s² = 0.441860 | 3 / 4 |
| B2 | 1.01 | 10⁻³ | 9.84729 | 3 / 4 |
| B3 | 1.001 | 10⁻⁴ | 9.98452 | 3 / 4 |
| B4 | 2 | 0.1 | 3.8 | 3 / 4 |
| B1 with Regge's end-average lapse (N1) | 1.05 | 0.1 | 0.441860 | 4 |
| L02 (N1) | 0.2 | 0.1 | 38.0 | 4 |
| B5 (N1) | 1.05 | 2.5 | −0.00465116, unstable | 4 |
| C0, C1, C2 (N1, lapse fixed) | 1, 1.05, 0.8 | — | frozen; −0.0232558, unstable; +0.142857, a ghost | 3, 4, 4 |
| AT: Run 83's kinetic form with the Run 83 check's tuned lapse | 1 | — | registered expectation FAIL | 3 |

**Point sets.**
- **Small k:** |k| = 0.005–0.04 along 255 directions: Run 83's 16, 200 random, 12 on the cone |k̂·(1,1,1)| = 1, and the three (1,−1,0)-type lines with 8 tilts each.
- **The zone:** the 12³ grid, 2000 random points, and shells at 0.05–0.8 on the same 255 directions; 5002 points per case.

**Kill rules.**
- **GR's route** (N0 and N1 each): K84a, exactly the two TT modes (c² = 1 ± 10⁻⁵, overlap ≥ 0.99), plus for N1 one gapped healthy mode, in all 255 directions; K84b, every zone mode healthy with a constant count; K84c, first class at every point (misalignment ≤ 10⁻⁸).
- **Khronometric route:** K84d, the TT pair plus the scalar within 10⁻⁴ of the formula in every direction; K84e, as K84b.
- **K84f:** the end-average lapse passes K84d–e. **K84g:** L02 passes K84d–e. **K84h:** the health boundaries come out as predicted, and C0's spectrum equals A_N1's. **K84i:** AT passes as GR's route (expected FAIL).

**Verdicts.** The registered outcome and the physics status are kept separate; the physics column is the check's.

| test | registered | physics status (the check) |
|---|---|---|
| K84a N0 | PASS | **PASS, exact:** ω² = \|δ\|² for both TT modes at every k |
| K84a N1 | PASS | **PASS:** TT c² = 1 to 2×10⁻¹⁴; the TT pair splits at finite k (lowest ≥ 0.94\|δ\|²) |
| K84b N0 | PASS | **PASS, exact** |
| K84b N1 | PASS | **PASS on the registered points. Not constant across the zone:** 3 modes on the curve ν₇ = 0, where the non-metric ω² → ∞; no negative ω² or energy anywhere |
| K84c N0, N1 | PASS | **True by construction.** First class also in the full linear Dirac sense |
| K84d B1–B4 (N0, N1) | PASS | **PASS:** c_s² to ≤ 1.1×10⁻¹³ |
| K84e B1–B4 (N0, N1) | PASS | **PASS:** equivalent to In(U) = (3,1) plus α < 2ξ; N1 caveat as K84b |
| K84f | PASS | **Not an independent test:** the end-average coupling is c_G |
| K84g | PASS | **PASS** |
| K84h | PASS | **PASS:** B5 and C1 unstable, C2 a ghost, at the formula's values; the C0 clause holds by construction |
| K84i (AT) | FAIL, as expected | **FAIL:** 22 of 255 directions (105 of 3,552) near the (1,−1,0) lines; 634 of 5002 zone points unhealthy |

![Run 84](../figures/84_corner.png)

**What the check added.**
1. **Integrity.** All 17 hashes match. Re-running the registered pipeline reproduces `run84.json` and `analyse84.json` bit for bit. The file times are consistent with the stated order. One undocumented step: the 50-digit toolkit was imported 23 s after the run, outside the registered pipeline, with no effect on the verdicts.
2. **Every registered verdict reproduced independently,** with a construction read from the arriving vertex metric and a Hamiltonian (Dirac) reduction:
   - float64 on the 255 registered directions and on 3,552 more (3,000 random, tilts of 10⁻⁶–10⁻³ about nine special lines, 72 cone directions);
   - 50-digit spectra (Cholesky plus Hermitian Jacobi; no polynomial roots) on the 255 directions for eight cases;
   - 22,031 zone points, and inertia checks at 75,204.
3. **N0 is exact.** Every branch obeys the continuum dispersion with k² → |δ|²:
$$
\omega^2=c^2|\delta|^2,
$$
   for both TT modes (c² = 1) and the scalar (c² = c_s²), at every k and in every case tested, to ≤ 4×10⁻¹⁴. N0 is the continuum's linear theory with each derivative replaced by a forward difference, mode by mode: no direction dependence and no doublers.
4. **c_G is Regge's own lapse coupling.** Regge's end-average coupling c_ends = 2ξDA(w∘ℓ), with w_c = cos(k·d_c/2), equals G₁gδ at every k (1.5×10⁻¹⁴ in float64; 1.8×10⁻⁴⁹ at 50 digits). So:
   - the registration's limit "agrees with Regge's curvature coupling only at O(k²)" is wrong;
   - K84f is the same system as B1_N1;
   - **Runs 83 and 84 share the potential and the lapse coupling exactly, and differ only in the kinetic form.**
5. **An exact Regge identity decides the khronometric route.** For q_w = w∘ℓ², the pattern of a unit lapse wave, c_ends = −Vq_w and, at 50 digits, at every k,
$$
q_w^\dagger Vq_w=-4|\delta|^2,\qquad\text{so}\qquad F(k)\equiv-\frac{\tilde c^\dagger U^{-1}\tilde c}{2\kappa}=2\xi .
$$
   - With U_B = U + c̃c̃†/(2ακ), det U_B = det U (1 − 2ξ/α). U has inertia (3,1) at every sampled k (positive eigenvalues ≥ 0.586|δ|², the negative one ≤ −0.333|δ|²), so with the kinetic form positive, **case B is healthy at every k exactly when α < 2ξ: the continuum's condition.**
   - The identity is the flat-background case of Glickenstein's second variation of Regge's functional under a conformal change (JDG 87, 2011).
   - B1–B4, the end-average case and L02 therefore test one fact, not eight. In(U) = (3,1) is measured, not proved.
6. **First class in the full linear Dirac sense, at λ = 1.** With H = ½p†G⁺p + ½q†Vq and the constraints C_i = g†p, C_H = c†q, at 20 random k: {C_H, C_i} ≤ 7×10⁻¹⁵, and both constraints are preserved in time. N1 has 4 first-class constraints and (14 − 8)/2 = 3 degrees of freedom; N0 has 2. Equivalently, the quadratic action has an exact linear time-reparametrisation symmetry, because g†Ggδ = 0 and c = Ggδ:
$$
s\to s+\delta\,\epsilon,\qquad n\to n-\dot\epsilon .
$$
7. **The defect: N1's kinetic form is singular on a closed curve.** ν₇ = ν·e_xyz vanishes on one closed curve on the 3-torus, of length ≈ 11.9, at |k| ≥ 4.0 (every component between 1.50 and π in magnitude). There G has inertia (5,1,1), the mode count drops from 4 to 3, and the non-metric branch diverges as ω² ≈ 4.2/(m|ν₇|²). Nothing turns negative, but N1's spectrum is unbounded, and float64 solvers fail within about 10⁻⁵ of the curve. The registered statements "min|ν·e_xyz| = 0.0053, so N1's G is invertible everywhere" and "the same inertia at every point" are false for N1; the registered points never came closer than |ν₇| = 0.0053. **N0 is unaffected.**
8. **Which rules could fail.** K84c, the C0 clause of K84h and K84f hold by construction. The others can fail: the rejected first construction (trace read at the place) fails K84a in 240 of 255 directions, and K84b and K84e at 816 and 860 of 1,500 zone points.
9. **Symmetry.** G keeps the axis permutations and mirrors (so there is no chirality) but breaks lattice inversion at O(1): the point group is C₃ᵥ, not the Kuhn lattice's D₃d. Spectra are unaffected (exactly even in k), and the departing-corner variant gives identical spectra. Averaging the two corner forms loses the null vector. The asymmetry is polar, along (1,1,1), and appears as O(ka) offsets in mode shapes, which matters once sources are coupled.
10. **Smaller corrections.** The registered AT values near the (1,−1,0) lines are accurate only to about 6×10⁻³; the FAIL stands at 50 digits. The TT overlap is measured in a metric where non-TT branches reach 0.92 (N1); the 0.99 threshold worked only because the TT modes are exact. Extra cases behave as the continuum predicts: λ = 1 + 10⁻⁶ (α = 10⁻⁷ and 10⁻⁵) healthy at the formula's speed; λ = 0.999 and 0.99 unhealthy; m = 0.01 and 100 healthy, with the gap at 28/m.
11. **The literature.**
    - Known: reading metric components from the edges at a vertex, with phase factors, is the Roček–Williams weak-field identification (e.g. Hamber & Williams 2004).
    - Known: in Regge-type models an exact linear gauge symmetry around flat space is generic, and it breaks at higher order and on curved backgrounds (Bahr & Dittrich 2009; Bahr, Dittrich & He 2011; Höhn 2014). Run 84's first-class structure is the semi-discrete analogue, of the same limited kind.
    - Not found: a lattice DeWitt kinetic form engineered so that the longitudinal shift block is exactly 2(1 − λ)|δ|². In spirit it is a compatible discretisation, keeping the discrete complex gauge → metric → curvature exact (compare Arnold & Hu 2021).

**Reading.**
1. **GR's route has a healthy lattice realisation at the linear level.**
   - N0 is the reference: the corner kinetic form, Regge's energy and Regge's own end-average lapse coupling.
   - It has the full linearised gauge symmetry, exactly GR's two polarisations, and the exact dispersion ω² = |δ|², with no extra propagating scalar, no direction dependence and no doublers, at every wavelength the zone contains.
   - **This is Note H's carrier, C2, achieved in that linear sense.**
2. **Run 83's instabilities belonged to its kinetic form, now proved.** Run 83 used the same potential, the same lapse coupling and the same κ. Since F ≡ 2, its potential side was healthy for α < 2ξ at every k. Its khronon instability and its second-class GR route came from the kinetic form alone.
3. **The khronometric route is healthy exactly when α < 2ξ,** as in the continuum, for every λ > 1 tested, from 1 + 10⁻⁶ to 2. Run 83's form turned unstable from |k| ≈ 0.1 at λ − 1 = 10⁻³.
4. **What is chosen, not derived.**
   - The kinetic form is a construction that meets the criterion. It is one of two inversion-related choices, it breaks lattice inversion, and it does not come from a 4D action or from CO's rules.
   - N1's inertia is ad hoc and degenerates on a curve. N0 is the version to carry forward.
   - The constraints are imposed as exact multipliers.
5. **What linear first-class structure buys, and what it does not.**
   - It buys the right mode count, no conformal scalar, an exact linear time-reparametrisation gauge, and a linear Hamiltonian constraint c_G†q = source that is an exact finite-difference Poisson equation (relevant to H4).
   - It does not buy closure of the nonlinear constraint algebra, which in the continuum is what singles out GR and on lattices generically fails; nor anything on curved backgrounds; nor a discrete-time evolution law.
   - **In CO's terms:** the quadratic dynamics is time-reversal invariant and the lapse is pure gauge, so on this route the engine's tick cannot itself be physical time. That is R4's statement ("the engine's tick is not physical time"), and it leaves the arrow in commitment, not in the waves (Run 81b).
6. **What remains.** Everything here is linear, around flat space, on one triangulation, in continuous time.
   - **Second order:** whether the linear gauge symmetry extends to the cubic action, i.e. whether the bracket of two Hamiltonian constraints closes onto the momentum constraints at first nonlinear order. That is H5's precondition, and where Regge-type lattices are known to fail.
   - A non-flat background; and a parity-even construction (for example a doubled cell), before sources are coupled.
   - **H3:** the source, matter's conserved stress radiating through this lattice, against the quadrupole formula. **H4:** the static field to second order (β). **H5:** a one-way stochastic engine whose average is this dynamics and which keeps both constraints every tick.
   - The face-centred complex no longer answers an open question at the linear level.
7. **Run 83's tuned lapse fails, as registered.** The repair had to be in the kinetic form.
