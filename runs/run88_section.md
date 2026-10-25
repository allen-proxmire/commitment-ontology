### Run 88: the kinetic sector at the second lattice correction, with the constraint basis part of the ansatz (Note H, field order 2, order a²; a calculation)

*25 October 2026.*
- *Registered and hashed before the run (`modes88/PREREG_88.md`, with the code and the validation outputs; 11:22:15 UTC).*
- *Validation beforehand:*
  - *the extended engine against Run 87's;*
  - *the new three-factor terms against exact differences;*
  - *{H̃, H̃} at order π as an identity;*
  - *every new formula against explicit real-space Poisson brackets;*
  - *Run 87's D1 results reproduced in the new code;*
  - *planted and negative solver toys;*
  - *the negative controls' construction.*

  *A timing run on the registered basis at D2, whose outcome Run 87 already implies, and a dry run at D1 were disclosed in the registration.*
- *An independent agent checked the run (below), and its corrections are adopted here.*

**Why.** Run 87 failed at the first lattice correction (order a) with structure functions independent of π in the D4 basis. Post hoc, the basis H̃ = H − D[X] with X_a = ¼N(2π_aa − tr π) closed all six conditions. The Run 87 check recommended registering the basis change in the ansatz at the next truncation.

**Question.** In the kinetic sector at the second lattice correction (D2, order a²), does the algebra close:
- (K88a, primary) as a first-class algebra, with the π-linear structure functions that time reversal allows; or
- (K88b, secondary) in a slide basis H̃ = H − D[X(N; π)], with X free through degree 1 and π-independent structure functions?

**Scope.** The kinetic sector only.
- The full D2 system has 22,680 reduced unknowns and about 683,000 rows. That is beyond a dense solve on the machine used, and most of the size is in the potential sector.
- The kinetic sector is where Run 87 failed. It is necessary for closure, not sufficient.

**The conditions.** These are Run 87's kinetic conditions: (HD1) {H, D} at order h, (DD1) {D, D} at order π, and
$$
\text{(A)}\quad \tfrac12W^{(1)}(N;\Gamma u)[\pi,\pi]-\pi\cdot S_u\big(\Omega(N)\pi\big)+\tfrac12\pi\cdot\Omega(L^0)\pi\;\big[-\pi\cdot\Gamma Y(u,N;\pi)\big]=0,
$$
$$
\text{(B)}\quad -\partial E^{(2)}_N(h)\cdot\Omega(M)\pi-(C^\dagger N)\cdot W^{(1)}(M;h)\pi-(N\leftrightarrow M)=\pi\cdot\big(\Gamma U^{(1)}+S_{U^0}h\big)\;\big[-E^{(1)}_{V(N,M;\pi)}(h)\big].
$$
- **The bracketed terms are the primary form's π-linear structure functions.** Time reversal (H even in π, D odd) allows exactly three at field order 2: H[V] in {H, H}, D[Y] in {H, D}, and H[ν] in {D, D}. Only V and Y enter the kinetic sector.
- **In the secondary form,** H̃ is an H with the dressing
$$
\tilde\Omega(N)=\Omega(N)-\Gamma X_N-(\Gamma X_N)^\dagger,\qquad \tilde U^0(N,M)=U^0(N,M)+X(M;C^\dagger N)-X(N;C^\dagger M),
$$
  which replace Ω and U⁰ in (A) and (B). The identity behind Ũ⁰ uses E⁽¹⁾_N(Γu) = 0, i.e. C(k)·G(−k) = 0.

**Truncation:** HD1 ≤ 5, DD1 ≤ 4, A ≤ 3, B ≤ 4. The unknowns' degrees are exactly those the equations contain: S, L⁰, B⁰, U⁽¹⁾ ≤ 3; W⁽¹⁾, V, Y ≤ 2; X ≤ 1. That gives 4,324 reduced unknowns (wide) or 3,772 (htilde), and 93,330 fit rows.

**Decision:**
- **EXISTS** if, on fit and held-out points, every non-floored block has ρ ≤ 10⁻⁸ and every floored block has |residual| ≤ 10⁻¹² of the largest block.
- **NOT FOUND** if every start has held-out max ρ ≥ 10⁻⁴, with a clean spectral gap for the linear form.

**Negative controls** (NC1–NC3): random top-degree terms added to (B) or (A), which must be NOT FOUND.

**Result (registered).**

| rule | form | unknowns | starts | final weighted cost | held-out max ρ | verdict |
|---|---|---|---|---|---|---|
| **K88a** (primary) | wide: V and Y | 4,324 | 1 (linear) | 0.1607 | 0.96 (B1); top blocks 1–2% | **FAIL** (against the expectation) |
| **K88b** (secondary) | htilde: X ≤ 1 | 3,772 | 4 | 0.1446–0.1448 (still falling at iteration 8) | 0.92–0.94 (B1) | **FAIL** |
| NC1, NC2, NC3 | controls | | | | 0.72–0.85 | NOT FOUND, as required |

**Overall (registered): FAIL.**

- **The identical code closes both forms at D1.** Validation V5 found X⁰ = +¼(2π_aa − tr π) again, from a zero start. So the D2 failure is new at the top degree.
- **Disclosed:** the control steps started 3 minutes after the last K88b start, because a waiting loop matched its own command line. The steps are deterministic and reproduce exactly.
- **The registered reading** ("GR's constraint algebra then breaks on this lattice at field order 2 at order a², and the khronometric route becomes the operative reading") **is stronger than shown** (the check). The corrected reading is below.

![Run 88](../figures/88_kinetic_a2.png)

**The independent check.** Every certifying solve was a LAPACK solve on assembled rows (chunked QR, and SVD of the exact polynomial-coefficient equations), or LSQR. Point sampling was removed altogether by converting every block to its exact coefficients.
1. **Hashes and time order.** 21/21 OK at the start and the end. The registration precedes every run output, and every stored solution reproduces every logged block exactly.
2. **K88a's FAIL is certified.**
   - The wide system is exactly linear (9×10⁻¹⁶).
   - Three solvers agree on rank 3,743 with a clean gap, and on the minimum weighted cost 0.16067313217 (to 11 digits).
   - The relative inconsistency is |P⊥r₀|/|r₀| = 0.030 with the registered weights, 0.052 in the point-free coefficient equations, and 0.029 on a fresh point set 1.6 times as large.
   - The registered solve had reached this exact minimum.
3. **The solver closes D2 when a solution exists.** Planted D2 problems with the real symbols come out EXISTS (non-floored 4–9×10⁻¹⁶). Cauchy-integral degree parts of the full-symbol residual equal the engine's blocks to 5.5×10⁻¹⁵.
4. **The primary criterion is complete for the registered Hamiltonian.**
   - The four conditions were re-derived and match term by term.
   - Every unknown's degree cap is exactly the degree that can enter: raising any cap by one adds nothing (≤ 1.5×10⁻¹⁵).
   - U⁰ is forced (rank 50 of 50).
   - π² and h² terms in D do not enter these conditions.
   - Canonical transformations preserve closure.
   - The S3 restriction loses nothing for an affine system with covariant symbols.
   - A field-dependent lapse redefinition H[N + Z(N; h)] adds no independent direction (36 columns, 0 new): it is already inside the wide form.
5. **K88b's FAIL follows from K88a's.** A slide-basis solution induces a wide one within the registered caps. S's degree-0 part is forced to zero, so X ≤ 1 is complete. The four starts on their own were not a certificate: they had not converged.
6. **Where the obstruction is** (exact coefficients):

| sub-system | \|P⊥c\|/\|c\| |
|---|---|
| HD1 + DD1 | 6×10⁻¹⁵ |
| HD1 + DD1 + B | 8×10⁻¹⁵, **closes** |
| HD1 + DD1 + A | **0.063** |
| all four | 0.052 |

   The failure begins in (A), the kinetic dressing's covariance under the sliding at order a². It shows once HD1 forces a nonzero sliding. With every lower-degree block imposed exactly, the irreducible residual lies in A3 (64%), B4 (29%), DD14 (4%) and HD15 (3%). It is spread over many directions (90% in 760 S3 directions), not a defect of a few parameters as at D1, where X⁰'s four directions absorbed it.

**What would remove it (the check, post hoc).** Each probe adds one freedom of the *theory* (not of the test) to the wide system; "remaining" is the share of the obstruction left in all four conditions.

| probe | free coordinates | new directions | remaining (all four) | HD1 + DD1 + A |
|---|---|---|---|---|
| (c) lapse redefinition H[N + Z(N; h)] | 36 | 0 | 1.00 | — |
| (b1) E⁽²⁾'s lapse placement, second moment | 2 | 0 | 1.00 | — |
| (b2) E⁽²⁾'s lapse coupling, general at a² | 1,024 | 64 | 0.94 | 0.997 |
| (a′) Ω₂ ultralocal (Run 85's dressing class), with HH1 | 90 | 45 | 0.69 | 0.41 |
| **(a) Ω₂ non-ultralocal, with HH1** | 186 | 73 | **0.48–0.50** | **closes** (non-floored 8.5×10⁻¹⁶) |
| (a12) Ω₁ and Ω₂ non-ultralocal | 226 | 89 | 0.49 | closes |
| (a12) + (b2) | 1,250 | 153 | 0.43 | — |

Here Ω → Ω_D4 + Ω₂, with
$$
\Omega_2(k,s)_{il}=P(k,s)_{il}+P(k,-k-s)_{li},
$$
of degree 2. HH1 ({H, H} at order π) is kept, with U⁰ free.
- **A non-ultralocal order-a² kinetic dressing** (coupling π at neighbouring places beyond D4) restores the spatial covariance exactly. An ultralocal one does not.
- **No freedom tested closes all four conditions.** With Ω₂ free, the condition that fails is (B), {H, H} at order πh. About 0.43–0.50 of the obstruction remains.

**Reading (corrected, as the check gives it).**
1. **Certified:** for the registered lattice Hamiltonian (D4's dressing, Regge's energy with the end-average lapse, this kinetic form), the kinetic sector has **no local first-class closure at order a²**. The obstruction begins in {H, D} at order π², the kinetic dressing's covariance.
2. **Post hoc:** a non-ultralocal order-a² dressing removes that part, but {H, H} at order πh then fails under every freedom tested. Within the tested family, this lattice can be made spatially covariant at a², but not first class.
3. **For the routes.**
   - The khronometric route, which needs {D, D} and {H, D} to close but not {H, H}, faces the same obstruction *as registered*, since (A) fails.
   - With the post hoc dressing, its kinetic sector closes at this order. What fails is exactly the bracket it does not need.
   - The route is therefore not yet "operative": the dressing change must itself be registered.
4. **Consistent with the literature.**
   - Curved Regge configurations have no exact gauge symmetries (Bahr & Dittrich, arXiv:0905.1670).
   - Discretized constraints generically fail to close (Gambini & Pullin, gr-qc/0512065).
   - In 4D, closed discrete hypersurface-deformation algebras are known only in flat and homogeneously curved sectors (Bonzom & Dittrich, arXiv:1304.5983).
   - Against that background, Run 87's D1 closure was the non-generic result.
5. **A correction to Run 87's reading 4 and Run 86's reading 3.** The Bahr–Dittrich argument concerns Regge's own vertex-displacement symmetry, so breaking *of that symmetry* is expected at field order 3. Other discreteness effects, such as the kinetic dressing's covariance found here, can and do appear at field order 2.
6. **Size.** The breaking is of relative order (ak)². At CO's hop (about 10⁻³² m) and astrophysical wavelengths that is far below any measurement. What it bears on is the theory's consistency, i.e. whether extra modes exist, not a direct observable.
7. **Bearing on the two readings of how space curves (Note G).** Note H's carrier has fixed relations, reading (B)'s kind of lattice. The part the hand-placed dressing caused is removable. What remains is the generic failure of fixed-connectivity lattices to close {H, H}, which counts, modestly, toward reading (A), where relations form and dissolve. That reading has its own known costs: relational approaches tend to trade the symmetry problem for an emergence problem.

**Limits.**
- The kinetic sector only. The potential sector at a², and joint closure, are untested.
- Formal, at the origin of momentum space; through order a²; at field order 2.
- The post hoc probes do not exhaust the lattice Hamiltonians. Untested: E⁽¹⁾'s own a² lapse coupling, T-odd terms in H, and other triangulations.
- N0′, λ = 1, a flat background and one triangulation.
- The report step's X analysis was computed at a fit that does not close, and carries no information about a closing basis.
- Control NC3 was scaled against that fit's inflated block, so it is weak evidence; NC1 and NC2 are the informative controls.
