### Run 87: GR's constraint algebra at field order 2, order by order in the lattice spacing (Note H, the next order; a calculation)

*24 October 2026.*
- *Registered and hashed before the run (`modes87/PREREG_87.md`, with the code and the validation outputs; 16:42:01 UTC).*
- *Validation beforehand:*
  - *Regge's third-order energy against exact energies on the lattice;*
  - *the jets against hyper-dual derivatives;*
  - *U⁰'s sign (Run 85's closure);*
  - *Run 86's solution in the new engine;*
  - *the Taylor machinery and its Jacobian;*
  - *S3 covariance;*
  - *every condition formula against explicit real-space Poisson brackets;*
  - *planted and negative solver toys.*

  *A dry run's outputs were deleted unread.*
- *An independent agent checked the run (below), and its corrections are adopted here.*

**Question.** Runs 85 and 86 closed all three brackets at first order in the fields. **At field order 2, can the sliding, the kinetic metric and the structure functions be extended so that all three brackets still close?**

**The constraints at field order 2.**
$$
H[N]=\tfrac12\sum\pi\cdot\Omega(N)\pi+\tfrac12\sum W^{(1)}(N;h)[\pi,\pi]-E^{(1)}_N-E^{(2)}_N-E^{(3)}_N,\qquad D[u]=\sum\pi\cdot\big(\Gamma u+S_uh+T_u(h,h)\big).
$$
- Ω is Run 85's D4 dressing. W⁽¹⁾, the kinetic metric's dependence on h, is unknown and local.
- E⁽³⁾ is Regge's third-order energy. It is computed with exact (jet) third derivatives, and with the body diagonals fixed by ε_b = 0 to second order:
$$
E^{(3)}_p=\tfrac16D^3E_p[Ah,Ah,Ah]+D^2E_p[Ah,\beta_2(h,h)],\qquad \beta_2=-\tfrac12\,\frac{D^2\varepsilon_b[Ah,Ah]}{\partial\varepsilon_b/\partial L_b}.
$$
- The structure functions gain h-dependent parts: L⁽¹⁾(u, N; h), B⁽¹⁾(u, v; h) and U⁽¹⁾(N, M; h). In the registered ansatz they do not depend on π.

**The new conditions:**
- (A) {H, D} at order π², the kinetic metric's covariance:
$$
W^{(1)}(N;\Gamma u)=S_u\Omega(N)+\Omega(N)S_u^\dagger-\Omega(L^0);
$$
- (B) {H, H} at order πh, with the structure function U⁰ + U⁽¹⁾(h):
$$
-\partial E^{(2)}_N(h)\cdot\Omega(M)\pi-(C^\dagger N)\cdot W^{(1)}(M;h)\pi-(N\leftrightarrow M)=\pi\cdot\big(\Gamma U^{(1)}+S_{U^0}h\big);
$$
- (C) {H, D} at order h²:
$$
\partial E^{(3)}_N\cdot\Gamma u+\partial E^{(2)}_N\cdot S_uh+E^{(1)}_N(T_u(h,h))+E^{(2)}_{L^0}+E^{(1)}_{L^{(1)}}=0;
$$
- (D) {D, D} at order πh:
$$
S_uS_vh-S_vS_uh+2T_u(h,\Gamma v)-2T_v(h,\Gamma u)-S_{B^0(u,v)}h-\Gamma B^{(1)}=0 .
$$

The first-order conditions are solved jointly with them. The check re-derived all six from the canonical form and found them complete at this order (below).

**The method: order by order in the lattice spacing.**
- **Why.** A full stencil search would need millions of unknowns; T alone is trilinear.
- **What is expanded.** Every symbol is expanded in homogeneous powers of its wavevectors. The fixed ones are expanded exactly. The unknowns' moments are completely free, which is what an arbitrarily large local stencil allows.
- **What this can show.**
  - A failure at some degree rules out every local construction *of the form fitted*.
  - A pass is formal: it holds at the origin of momentum space.
- **Two truncations:**
  - **D0,** the continuum degree of every condition: 1,128 unknowns after S3 reduction.
  - **D1,** the first lattice correction: 5,862 unknowns, against roughly 170,000 conditions.
- **The fit.** The system is linear in every unknown except two bilinear terms of (D), so it is fitted by Gauss–Newton with up to five starts (D0) or three (D1).
- **Decision.** EXISTS if every block (condition, degree) has ρ ≤ 10⁻⁸ on fit and held-out points; NOT FOUND if every start leaves ρ ≥ 10⁻⁴.
  - ρ is a block's residual over the sum of its terms' sizes.
  - A block whose terms are all at rounding is measured against 10⁻⁶ of the largest block (the floor).

**Result (registered).**

| rule | truncation | unknowns | starts | final weighted cost | held-out max ρ (worst block) | verdict |
|---|---|---|---|---|---|---|
| **K87a** | D0, the continuum degree | 1,128 | 1 | 10⁻¹⁹ | 2.7×10⁻⁹ (C1, a floored block). Every other block ≤ 1.1×10⁻¹⁵. | **PASS** (as expected) |
| **K87b** | D1, the first lattice correction | 5,862 | 3 | 1.4213, 1.4217, 1.4215 | 0.69–0.81 (B1, A0) | **FAIL** (against the expectation) |

**Overall (registered): FAIL.**

- **The three starts stall at the same cost.** Starts 1 and 2 began from different members of the first-order family, and all three end within 3×10⁻⁴ of one another.
- **The registered sector diagnostics:**
  - the kinetic sector (HD1, DD1, A, B) fails alone (cost 1.315);
  - the potential and sliding sector (HD1, DD1, C, D) closes alone (every block ≤ 10⁻¹⁵, apart from the floored ones).
- **The FAIL is certified, within the ansatz (the check).**
  - The kinetic sector is linear in its 1,052 unknowns. With LAPACK least squares, its weighted cost is 1.314679 for every rcond from 10⁻¹⁵ to 10⁻⁶, with a clean rank gap (singular values 22.8 … 0.408, then 3.6×10⁻¹⁵).
  - The inconsistency is 0.091 of the residual, robust to weighting and to a fresh point set twice as large.
  - It sits in the top-degree blocks of all four kinetic conditions: A2 3×10⁻², B3 4×10⁻², HD14 2×10⁻², DD13 9×10⁻³. The registered diagnostic's worst block (HD12, ρ 0.70) is an artefact of the weighting.
  - Every solution of the full D1 system would solve this subsystem, so the full NOT FOUND is not a local minimum of the bilinear fit.
- **Amendment 1.** The registered single process was stopped by the environment's two-hour limit during start 2. The remaining steps were run as separate processes with identical code, seeds and draws (`AMENDMENT_87_1.md`, hashed before they ran). The resumed starts reproduce the logged costs digit for digit.
- **The registered reading** ("every local sliding fails at the first lattice correction. GR's constraint algebra then breaks on this lattice at field order 2, at order a, and the khronometric route becomes the operative reading") **is not supported** (the check). The same applies to the reading string in `analyse87.json`. What fails is the ansatz: structure functions independent of π, in the D4 constraint basis. A change of constraint basis removes the failure (below).

![Run 87](../figures/87_order2.png)

**Where the obstruction is, and what it is (post hoc).**
1. **(A) and (B) each close; together they do not.** With the first-order conditions, the kinetic metric's covariance (A) closes alone, to 10⁻²¹, and so does {H, H} at πh (B). Together they do not.
2. **A wider ansatz removes it.** Time reversal (π → −π) allows exactly three π-dependent structure functions at this order, all linear in π (the check): V in {H, H} = D[U] + H[V], Y in {H, D} = −H[L] + D[Y], and ν in {D, D} = D[B] + H[ν]. The registration excluded all three.
   - Allowing D[Y(u, N; π)] does not help (cost 1.15).
   - Allowing H[V(N, M; π)] closes the kinetic sector exactly, to 10⁻²¹.
3. **That term is a change of constraint basis.** Write H^(c)[N] = H[N] + c D[X(N; π)], with X local and linear in N and π. To field order 2 (the check's derivation),
$$
\{H^{(c)}_N,H^{(c)}_M\}=\{H_N,H_M\}+c\,H\big[L(X_N,M)-L(X_M,N)\big]+c\,D[\dots],
$$
   and with L's forced part, L(u, N) → u·∇N, the H-term is c H[V_X] with V_X = i(k₂ − k₁)·X₀[π]. Starting from {H, H} = D[U] + H[V_X], the H-term cancels only for c = −1:
$$
\tilde H[N]=H[N]-D[X(N;\pi)].
$$
   - **The sign is the check's correction.** The first version of this note had H + D[X]. That basis does not close (0.18); H − D[X] does (3×10⁻¹²). The *registered* time rule is therefore H = H̃ + D[X]: it already contains a slide by +X relative to the basis that closes.
   - **That the fitted V has this form is automatic** (the check). Antisymmetry under N ↔ M forces every degree-≤ 1 V into the form i(k₂ − k₁)·X₀, so the form alone is not evidence for the reading. The evidence is items 4 and 5.
   - **The redefinition is legitimate.** (H, D) → (H̃, D) is triangular with identity diagonal, so the constraint surface and the first-class property are unchanged. H̃ = H at order h, and D is unchanged, so Runs 85 and 86 stand; {H̃, H̃} at order π changes Run 85's U⁰ only at order a.
4. **X is forced, and is simple.** With V restricted to the basis-change form, the kinetic sector closes, and the map X₀ comes out uniquely, with or without the S3 reduction (the check):
$$
X_a(N;\pi)=\tfrac14\,N\,\big(2\pi_{aa}-\operatorname{tr}\pi\big)=\tfrac14\,\dot h_{aa}\quad(\text{at }\lambda=1,\ \dot h=N K^{-1}\pi).
$$
   - **It is specific.** The obstruction (0.091 of the residual) lies in the span of X₀'s four S3 directions, against up to 2,815 possible obstructions. The absorption uses two of the four, at exactly ±¼. Other four-parameter forms do not close (cost 0.94–1.31), and a random term added to (B) at degree 3 is not absorbed even with V present (ρ 0.89).
   - **A geometric reading (a heuristic, the check).** The size, ¼ = ½ × (a link's change in length, ½ h_aa), and the sign fit one picture. The registered time rule reads each place's metric from its links, and as an axis link lengthens, the point that link measures moves away from its fixed end by half the change. The GR-form basis subtracts that drift. This picture does not explain why the face diagonals contribute nothing, and it is not a derivation.
5. **The whole system closes in the basis H̃.**
   - The basis change also puts a D-term into {H̃, D}. The free unknowns absorb it, and only their order-a parts change.
   - All six conditions at D1 then close together with π-independent structure functions: cost 7×10⁻²⁰ in one Gauss–Newton step from the kinetic solution (the check's run). Every non-floored block is ≤ 1.1×10⁻¹⁵, on held-out and fresh points alike.
   - The first post hoc version (registered constraints, with H[V_X] allowed in {H, H}) closes the same way, to cost 8×10⁻²⁰, with the same X₀.
   - **This is formal,** like every result of this method: order by order at the origin of momentum space, through the first lattice correction.

**The independent check.** The check built its own real-space Regge construction, sharing no code with the run:
- its own Kuhn lattice and its own map from the vertex metric to squared lengths;
- a fourth dihedral formula, the spherical law of cosines at a vertex;
- an exact solve for the body diagonals in complex arithmetic;
- Taylor coefficients by Cauchy integrals;
- its own gauge map, built from vertex displacements.

Every solve used LAPACK least squares or MINPACK Levenberg–Marquardt, not the engine's solver.

1. **Hashes and time order.** 16/16 OK. The registration precedes the run, and the stored solutions reproduce every registered per-block ρ exactly.
2. **The conditions, re-derived.**
   - All six match the code term by term, signs included.
   - Nothing is missing at field order 2 except the three π-linear structure functions that time reversal allows (item 2 above). There are no h² or π² terms in {H, H} and no π² or h² terms in {D, D}.
   - A check with GR's own continuum algebra, written in the engine's conventions, satisfies every D0 block to ≤ 5.4×10⁻¹⁵. That fixes every sign, factor and phase.
   - The engine's residuals equal real-space brackets taken with the exact energy to 5×10⁻¹²–1.2×10⁻⁹, and its degree blocks equal Cauchy-extracted degree parts to 7×10⁻¹⁶.
3. **Regge's third-order energy, recomputed independently.**
   - E⁽²⁾ agrees with the stencil to ≤ 3.4×10⁻¹², and E⁽³⁾ with T₃ to ≤ 2.1×10⁻⁹ (typically 10⁻¹¹–10⁻¹⁰).
   - **The β₂ term matters.** It contributes nothing for N = 1, exactly, but its share of E⁽³⁾ is up to 3.1 for other lapses. Without it, T₃ would be wrong by up to three times E⁽³⁾ itself.
4. **Neither too tight nor too loose.**
   - There are many more equations than unknowns: at D0, 8,092 equation coefficients against 1,128 unknowns of rank 1,094.
   - Every condition rejects a random perturbation of its input at 0.3 of its own size (residuals 0.03–0.9), so no condition is absorbed by the free unknowns.
   - The pure-gauge directions are identified: second-order redefinitions in T and β, and redefinitions u → u + n(u, h).
5. **K87a, reproduced.**
   - LAPACK Gauss–Newton reproduces the registered solution to 2.9×10⁻¹⁴.
   - Levenberg–Marquardt finds another solution, differing only by a second-order redefinition.
   - **The registered solution is GR's continuum algebra,** to ≤ 1.5×10⁻¹⁴ in every unknown: Lie-derivative sliding, L = u·∇N, the Lie bracket, U = γ^{ab}(N∂_bM − M∂_bN), and the DeWitt W⁽¹⁾. Its kinetic part is unique (rank 230/230).
6. **K87b, certified** (above).
7. **The quoted EXISTS figures come from the floor.**
   - The 2.7–5.2×10⁻⁹ maxima quoted for K87a, the potential sector and the post hoc runs are rounding in blocks that are identically zero at their degree, divided by the floor.
   - The blocks with real content close to ≤ 4×10⁻¹⁵, cancelling terms of size 5–34 over 14–15 orders of magnitude.
   - The margin to the 10⁻⁸ threshold is only 2–4×, so future runs should report non-floored blocks separately.
8. **Real space, with the exact energy.** Each solution was realised as a finite stencil, and the brackets were taken explicitly on periodic lattices of 12³–32³ places. ρ falls with the wavevector k as:
   - D0 (the continuum degree): k^0.97 for (B) and k^0.98 for (C), where closure through the continuum degree requires k¹;
   - the D1 closure: k^2.02 for (B) and k^1.96 for (C), where closure through the first lattice correction requires k²;
   - the D1 closure with V removed: k^0.80, which fails at degree 3.

**What was guaranteed, and what is new (the check).**
- **K87a was guaranteed** once the lattice's known symbols have GR's continuum parts at field order 2. It is a real check of Regge's third-order energy, N0′'s β₂, the end-average lapse and D4's DeWitt metric, and it confirms them exactly. It is not evidence of a lattice gauge symmetry.
- **New at order a, the potential sector.** Regge's third-order energy is covariant at order a under a local second-order sliding: (C) and (D) close, and a random order-a change of E⁽³⁾ is rejected.
- **New at order a, the kinetic sector.** The D4 constraint basis is not the GR-form basis at order a; H̃ = H − D[X] is. This concerns which combination of constraints generates the normal deformation. It is not a loss of gauge symmetry.
- **What field order 2 fixes.**
  - Run 86's first-order family shrinks from 87 free directions (at this truncation) to 20, all of them redefinitions u → u + n(u, h).
  - **Run 86's order-a bracket parameter κ is fixed at the Lie value.** Up to redefinitions, [u, v] is the Lie bracket through degree 2 in every D1 solution.
  - The kinetic metric's continuum h-dependence is forced to be DeWitt's, W⁽¹⁾₀ = ∂_h(K(γ)⁻¹), to 8×10⁻¹⁵, where
$$
K_{kl}=\tfrac{\sqrt{\det\gamma}}{2}\big[\operatorname{tr}(\gamma^{-1}E_k\gamma^{-1}E_l)-\operatorname{tr}(\gamma^{-1}E_k)\operatorname{tr}(\gamma^{-1}E_l)\big].
$$
    Its order-a part is not the simple (ultralocal) lattice DeWitt form (ρ 0.73–0.90 for three candidates), and a 35-dimensional family remains.
- **D4's role.** H̃'s π² part couples π at neighbouring places, so it lies outside Run 85's dressing class. D4 still does its first-order job, but the basis that closes at field order 2 is not a D4 dressing. The registered Limits' "Run 85's other dressings differ from it by canonical transformations" holds within the class only.

**Reading.**
1. **At field order 2, the lattice's continuum limit is GR's constraint algebra exactly.** This covers Regge's third-order energy with β₂, D4's DeWitt kinetic metric and Run 85's U⁰.
2. **At the first lattice correction, the algebra still closes.** It closes in the constraint basis H̃ = H − D[X], X_a = ¼N(2π_aa − tr π), with π-independent structure functions (post hoc, confirmed independently). The registered FAIL is a FAIL of the registered ansatz.
3. **For the routes.** The registered rule triggered the khronometric fallback, but the evidence does not show GR's algebra breaking. GR's route survives through order a at field order 2, with a changed constraint basis.
4. **Where breaking is expected (the check; qualified 25 October by Run 88's check).** Bahr and Dittrich's breaking is quadratic in the background curvature. It enters the action at fourth order in the fields, so breaking *of Regge's own vertex-displacement symmetry* would appear in the algebra at field order 3, not 2. Run 86's "that is field order 2" should be read that way. Other discreteness effects can appear at field order 2: Run 88 found one at order a² (the kinetic dressing's covariance).

**Limits.**
- Formal only: order by order at the origin of momentum space, through the first lattice correction. Not shown:
  - anything beyond D1, or whether the X needed at D2 stays this simple;
  - locality on the loci where one momentum vanishes;
  - a basis valid to all orders;
  - a geometric derivation of H̃;
  - field order 3.
- N0′, λ = 1, a flat background and one triangulation.
- The registered verdict stands as FAIL. Everything about the basis change is post hoc, and its next test must be registered with X as part of the ansatz.
