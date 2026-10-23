### Run 83: the normal modes of a lattice of relations that carry their own stretch (Note H, test H1; a calculation)

*23 October 2026.*
- *Registered and hashed before the run (`modes83/PREREG_83.md`, with the code, the theory and the validation outputs, 22:13:14 UTC).*
- *Validation beforehand was structural, plus the solver run on the continuum system. A dry run's outputs were deleted unread.*
- *After the run, a post hoc reduction recomputed the spectra. Everything from it, and the figure, is labelled post hoc.*
- *An independent agent checked the run with its own implementation and 50-digit arithmetic (below). Its corrections are adopted.*

**Question.** Note H's carrier (C2) is a stretch carried by each relation, with Regge's energy, on a relation graph that carries the full strain tensor. **On the Kuhn-triangulated cubic lattice, does it carry exactly GR's two polarisations, at light's speed, isotropically, with no ghost, no instability and no gapless extra mode?** That was asked for GR's route, with both constraints every tick, and for the khronometric route of the earlier papers (Note H §8).

**The lattice and its energy.**
- **The lattice.** Z³, each cube cut into the 6 Kuhn tetrahedra along its (1,1,1) diagonal (Roček & Williams's triangulation).
  - There are 7 relation classes per place: the 3 axes, 3 face diagonals of one orientation, and the body diagonal.
  - Seven relations against six strain components leaves one non-metric mode per place.
- **Variables:** per-relation stretches q_c = δ(ℓ_c²)/2, a shift (3 per place), and a lapse n (1 per place).
- **Kinetic energy: the per-tetrahedron DeWitt form.** Each tetrahedron's metric h^t is read exactly from its six relations, and
$$
T=\sum_t V_t\,\tfrac14\big[\dot h^t\!:\dot h^t-\lambda(\mathrm{tr}\,\dot h^t)^2\big].
$$
  At λ = 1 this is the Lund–Regge simplicial supermetric. The shift enters as q̇_c → q̇_c − d_c·(s(o + d_c) − s(o)).
- **Potential: Regge's energy,** ξ∫√γR = 2ξΣ_eℓ_eε_e, to second order. By Schläfli's identity its Hessian is ∂ε_e/∂ℓ_f.
- **Lapse.** The coupling is 2ξΣ_e n̄_eℓ_eδε_e, with n̄_e the mean lapse at the relation's two ends. Hořava's α term is αΣ_tV_t|∇_tn|².
- **The cases,** with continuum predictions from N√γ[K_ijK^ij − λK² + ξR + αa_ia^i] at ξ = 1:
  - **A, GR's route:** λ = 1, α = 0, the lapse a Lagrange multiplier (the Hamiltonian constraint per place), the shift eliminated (the momentum constraint). Predicted: 2 TT modes with ω² = k², plus the non-metric mode.
  - **B1–B4, the khronometric route** (healthy α), with the scalar at
$$
\frac{\omega^2}{k^2}=\xi\Big(\frac{2\xi}{\alpha}-1\Big)\frac{\lambda-1}{3\lambda-1}:
$$
    B1 (λ 1.05, α 0.1) 0.44186; B2 (1.05, 10⁻³) 46.488; B3 (1.2, 1.0) 0.07692; B4 (0.2, 0.1) 38.0.
  - **Health boundaries:**
    - B5 (α = 2.5 > 2ξ): unstable;
    - lapse fixed: C1 (λ = 1.05) unstable at −(1 − λ)/(1 − 3λ) = −0.02326; C2 (λ = 0.8) a ghost at +0.14286; C0 (λ = 1) frozen.
- **Kill rules,** following Note H's H1 row, over 16 directions at |k| = 0.004–0.032 and the Brillouin zone (the 12³ grid plus 2000 random k):
  - **GR route:**
    - K83a: exactly 2 gapless TT branches, c² = 1 ± 10⁻⁴;
    - K83b: the extra branch gapped and healthy;
    - K83c: no ω² < 0, ghost, complex or frozen mode in the zone;
    - K83d: the gauge structure.
  - **Khronometric route:**
    - K83e: the scalar at the formula's speed to 10⁻³, together with the two TT modes;
    - K83f: as K83b and K83c.
  - **Health boundaries:** K83g.

**Verdicts.** The registered outcome and the physics status are kept separate. The physics column comes from the check's leak-free 50-digit spectra, with the same registered k, classification rules and tolerances.

| test | registered outcome | physics status |
|---|---|---|
| K83a | FAIL | **FAIL.** A third gapless branch, a tachyon with negative kinetic energy, appears in 12 of 16 directions, and an exact zero mode along (1,−1,0). The two TT branches are exact, c² = 1 ± 10⁻¹³, in all 16. |
| K83b | FAIL | **FAIL.** The gapped mode survives the Hamiltonian constraint only along the three axes. |
| K83c | FAIL | **FAIL.** Of 3727 points, 901 have modes with ω² < 0, 22 have negative-energy modes and 33 frozen modes, and 3 are singular-G points. |
| K83d | FAIL (numerical) | rank g = 3 everywhere. The spurious-count clause is ill-posed at λ = 1 in four directions. |
| K83e | FAIL (classification leak) | **As predicted** for B1–B4 in all 16 directions: TT \|c² − 1\| ≤ 2×10⁻¹², \|c_s²/formula − 1\| ≤ 10⁻⁶. |
| K83f | FAIL | **FAIL for λ > 1** (B1–B3): finite-k instability. **PASS for B4** (λ = 0.2). |
| K83g | FAIL (classification leak) | **As predicted:** B5 and C1 unstable at the formula's values, C2 a ghost at 0.142857, C0 frozen at O(k²). |

**At route level:**
- **GR's route:** FAIL as registered, and FAIL in physics with the registered lapse coupling.
- **The khronometric route:** FAIL as registered. In physics the infrared passes, and the route fails through the λ > 1 ultraviolet.

**The registered solver, and why the verdicts split.**
- The registered method solved the pencil A z = ω²B z with the shift kept as a variable. The shift block of B is small:
$$
g_T^\dagger G g_T\simeq k^2,\qquad g_L^\dagger G g_L\simeq 2(1-\lambda)k^2+\mu_L(\hat k)\,k^4 .
$$
  - At λ = 1 the longitudinal block is O(k⁴), and exactly zero along the axes and (1,−1,0).
  - μ_L ranges from 0 to 2/9 with direction. The registration's "0.146 k⁴" was the (1,2,3) value.
- The shift's spurious ω² = 0 solutions leaked into the mode lists through the eigenvector threshold, in 6–16 of 16 directions per case. No threshold separates them at k = 0.004, because physical modes have equally small position parts.
- Worst-case errors at k = 0.004 were 10⁻⁵ to 10⁻³, and in case A modes were wrong or missing (TT c² = 0.99833 along x, against 1 ± 10⁻¹³).
- **The registered precision statement, "about 10⁻¹⁰", was false.** The solver had been validated only on the continuum system, where these near-singular blocks do not arise. It is Run 82's lesson again, for the solver this time.
- **The post hoc Hamiltonian reduction** (W = Q†G⁻¹Q, with no spurious solutions) is correct and well conditioned, to ≤ 5×10⁻⁹ against the 50-digit reference.
  - The exception is its Dirac step along the axes. There the lattice Hamiltonian constraint is exactly first class, so the step divides 0 by 0, and the values were right by luck to about 10⁻⁴.

**What the check added.**
1. **Integrity and the lattice.** All 12 hashes match, and the registered outputs reproduce bit for bit. An independent implementation, written from the registration with its own dihedral-angle formula, exact rational metric maps and a different Bloch convention, reproduces G, V, g, c and κ to 10⁻¹⁴.
2. **Khronometric route, long wavelengths: the continuum's, plus one gapped mode** (figure, panel c).
   - In all 16 directions there are two TT modes at c² = 1 and the scalar at the continuum's speed.
   - The non-metric mode is gapped and healthy, with
$$
\omega^2(k\to0)=\sigma\,v^{\mathsf T}G(0)^{-1}v=28\cdot\tfrac{3}{14}=6
$$
     exactly, for every λ. Here σ = 28 is V(0)'s single nonzero eigenvalue, on v = (1,1,1,−1,−1,−1,1)/√7. The value belongs to the chosen kinetic form.
3. **Khronometric route, short wavelengths: for λ > 1 the khronon becomes unstable** (panel d).
   - Its kinetic energy changes sign, with positive potential energy, so ω² < 0. **It is an instability, not a ghost.**
   - The onset is where g_L†Gg_L crosses zero:
$$
k^*a\simeq\sqrt{\frac{2(\lambda-1)}{\mu_L(\hat k)}}\;\approx\;3\sqrt{\lambda-1}\ \ \text{along }(1,1,1),
$$
     the same at α = 0.1 and 10⁻³. The unstable band therefore begins at wavelengths of about 2.1/√(λ−1) spacings: 9.6 at λ = 1.05, 21 at 1.01, 66 at 1.001 and 190 at 1.0001.
   - **The nearer λ is to GR's 1, the longer the wavelength at which the instability starts.** There is none along the axes and (1,−1,0), where μ_L = 0.
   - For λ ≳ 1.2 there is a second mechanism: an eigenvalue of G crosses zero near the zone boundary, and the gapped mode turns unstable.
   - Every λ > 1 tested, from 1.0001 to 5, is unstable on 23–66% of zone points.
   - For λ < 1/3 (B4) the whole zone is healthy: G and U + c̃c̃†/(2ακ) are positive definite on 17,550 points. The boundary is the continuum's λ = 1/3; the post hoc "0.32" came from a point set that cannot see small k.
4. **GR's route: the failure comes from the lapse coupling, not from Regge's energy.**
   - **The pattern of failure.** With the lapse averaged over each relation's two ends, the route fails at long wavelengths in every direction except two sets:
     - the cone |k̂x + k̂y + k̂z| = 1, which contains the axes, where it is healthy, with 2 TT modes and the gap at 6;
     - the (1,−1,0) lines, where there is an exact zero mode.

     The tachyon's ω²/k² is unbounded below near the cone (199 of 200 random directions are tachyonic). Health along the axes is a measure-zero accident: any tilt gives ω²/k² ≈ −1.15.
   - **The mechanism.** The lattice coupling is
$$
c^\dagger q=\big(-k_ik_jh_{ij}+k^2h_{ii}\big)+b(\hat k)\,k^2\,(v\!\cdot\!q)+O(k^4),\qquad b(\hat k)k^2=\frac{k^2+3(k\!\cdot\!n)^2}{\sqrt7},\quad n=(1,1,1).
$$
     Its metric part is exactly R⁽¹⁾; its non-metric part is not what first-class structure needs. For the constraint to be first class, c̃ must be parallel to Q†Ggσ_L, the G-dual of the zero-kinetic longitudinal shift, as it is in the continuum. That needs
$$
\Delta b\,k^2=\tfrac{\sqrt7}{3}\big[k^2-(k\!\cdot\!n)^2\big],
$$
     which vanishes only on the cone. Off the cone, the second-class constraint leaves a mixture of the scalar and the non-metric mode. It carries the lattice conformal mode's negative kinetic energy and the non-metric mode's O(1) potential: a gapless tachyon.
   - **A different lapse weighting removes it** (post hoc, the check's). On each body-diagonal hinge, average the lapse as
$$
\bar n=\tfrac{5}{12}(n_{000}+n_{111})+\tfrac{1}{36}\textstyle\sum_{\text{6 other cube corners}}n .
$$
     This is local, with positive weights. It keeps the metric coupling R⁽¹⁾ unchanged and cancels Δb identically.
     - Case A is then healthy in 15 of 16 registered directions and in 200 of 200 random ones: 2 TT modes at c² = 1, with the gap at 6.
     - Defects remain within an angle of order k of the (1,−1,0) lines, where W has an exact null vector. The zone is also still unclean: 519 of 3727 points.
   - **So Run 83 does not exclude this lattice for GR's route.** It excludes the end-average lapse coupling.
5. **One root.** μ_L ≠ 0, the per-tetrahedron kinetic form's longitudinal-shift structure, lies behind three findings:
   - the khronon's onset;
   - the residual defects of GR's route;
   - C0's scalar, which on the lattice is not frozen but a negative-energy mode with ω² = ¼μ_L k⁴.
6. **The literature.**
   - Known: linearised Regge on hypercubic/Kuhn lattices reproduces linearised GR at long wavelengths, with the extra variable decoupling (Roček & Williams 1981, 1984; Dittrich, Freidel & Speziale 2007).
   - Known: the Lund–Regge supermetric is indefinite, its conformal direction timelike (Hartle, Miller & Williams 1997).
   - Known: in canonical Regge calculus the Hamiltonian constraint is second class and diffeomorphisms are broken (Friedman & Jack 1986; Khatsymovsky; Bahr & Dittrich 2009), while fully discrete linearised 4D Regge keeps first-class vertex constraints (Höhn).
   - Not found: the direction dependence, the closed forms for b and μ_L, the gap 6, and the khronon onset.
   - Run 83's model is not a 3+1 split of a 4D Regge action. Its kinetic form and lapse coupling were chosen, so its second-class structure belongs to those choices.

![Run 83](../figures/83_modes.png)

**Reading.**
1. **The counting obstacle is cleared at long wavelengths.**
   - On the Kuhn lattice, a stretch per relation with Regge's energy and the per-tetrahedron DeWitt kinetic form carries GR's two polarisations exactly: c² = 1, isotropic, in every direction tested, on both routes.
   - On the khronometric route it also carries the continuum's scalar at the continuum's speed, and the extra non-metric mode is gapped at ω² = 6 and healthy.
   - This is the first time in the record that relations with their own energy and kinetic form are shown to carry GR's two polarisations. Run 11b assumed a strain field's wave equation and counted what radiates; Note H §4 showed the engine's cubic relations cannot carry them, by counting.
2. **Stability is not achieved.**
   - **Khronometric route.** For the observationally allowed λ − 1 ≲ 0.1, the khronon is unstable above |k| ≈ √(2(λ−1)/μ_L). Any one-way engine (H5) would grow there.
   - **The registration's reading applies:** "short-wavelength ghosts or instabilities would wreck any engine (H5). The lattice is excluded with this kinetic form, whatever its long-wavelength behaviour."
   - λ < 1/3 is healthy throughout but excluded by observation.
3. **GR's route is not excluded by Run 83, but it is not achieved.**
   - Its long-wavelength failure belongs to the end-average lapse coupling. A tuned local weighting removes it in generic directions.
   - Defects remain near the (1,−1,0) lines, and in the zone. Both trace to the kinetic form (μ_L).
   - The weighting was tuned post hoc and would have to be registered.
4. **The next test is the kinetic form,** not the counting.
   - **The criterion:** g_L†Gg_L = 2(1 − λ)k² exactly, with no k⁴ term in any direction, and G positive away from the conformal direction.
   - **Candidates:**
     - a per-relation kinetic form;
     - a vertex-averaged metric with the DeWitt form;
     - the L² inner product of Regge finite elements;
     - the kinetic term of a 3+1 split of a 4D Regge action.
   - **The lapse coupling should come from the same construction,** so that c̃ ∥ Q†Ggσ_L holds by construction, not by fitting.
   - **The face-centred complex,** which has no non-metric mode, avoids the mechanism of item 4 of the check. It does not avoid μ_L.
5. **In CO's terms.**
   - The relations' stretch with Regge's energy gives the right waves at long wavelengths. Note H's input list is confirmed: a triangulated graph, Regge's energy, the shift.
   - What the relations' *current* is, the kinetic form, is now the open choice. It decides stability.
   - This is where Run 81b's lesson recurs: the large-scale wave is fixed, and the small-scale rule decides whether it survives.
6. **Limits.**
   - Linear, flat background, one triangulation, one kinetic form.
   - The lapse and shift are treated as exact multipliers, so how a one-way update could enforce the constraints is still H5's question.
   - The tuned lapse and every other post hoc statement here are unregistered.
