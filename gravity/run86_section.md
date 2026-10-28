### Run 86: {H, D} and {D, D} together at the first nonlinear order (Note H, the joint test; a calculation)

*24 October 2026.*
- *Registered and hashed before the run (`modes86/PREREG_86.md`, with the code and the validation outputs; 13:57:03 UTC).*
- *Validation beforehand:*
  - *Regge's exact energy against the second-order stencil, and against Run 84's checked potential;*
  - *the hyper-dual derivatives;*
  - *the O(k) part of {H, D}, which reproduces the Run 85 check;*
  - *the continuum Lie bracket's sign;*
  - *S3 covariance;*
  - *the row assembly;*
  - *planted and negative toys for the solver.*

  *Two dry runs' outputs were deleted unread.*
- *After the run, post hoc probes described the closing slidings; they are labelled post hoc.*
- *An independent agent checked the run with its own real-space construction (below). Its corrections are adopted.*

**Question.** Run 85 closed {H, H} at the first nonlinear order. Its check showed that, on this kinetic form, that closure follows from Run 84's linear result, and named the decisive next test: **does one local field-dependent sliding close {H, D} and {D, D} together at the same order?** In GR the momentum constraint generates spatial diffeomorphisms, and the algebra reads
$$
\{H[N],D[u]\}=-H[u\cdot\nabla N],\qquad\{D[u],D[v]\}=D\big[[u,v]\big],\quad [u,v]=u\cdot\nabla v-v\cdot\nabla u .
$$
On a lattice, sliding must itself become field dependent beyond linear order:
$$
D[u]=\sum_x\pi(x)\cdot\big(\Gamma u+S_uh\big)(x),\qquad (S_uh)_j(x)=\sum_{(r,r')}s(r,r')_{jai}\,u_a(x+r)\,h_i(x+r'),
$$
where Γ is Run 85's flat-embedding sliding. The structure functions are local and bilinear:
$$
L(u,N)(x)=\sum l(r,r')_a\,N(x+r)\,u_a(x+r'),\qquad [u,v]_c(x)=\sum b(r,r')_{cab}\,u_a(x+r)\,v_b(x+r').
$$

**The set-up.**
- **The theory:** Run 85's canonical form in **N0′**.
  - The body diagonal has no momentum. Its length is fixed by the N = 1 equation, which by Schläfli's identity is ε_b = 0, one equation per cube.
  - λ = 1, and the lapse coupling is Regge's energy with the end-average lapse: E_N = Σ_pN_pE_p, with E_p = Σ_{e∋p}ℓ_eε_e.
- **The conditions at first order in the fields.**
  - **(HD), at order h:**
$$
\partial_hE^{(2)}_N(h)\cdot\Gamma u+E^{(1)}_N(S_uh)+E^{(1)}_{L(u,N)}(h)=0 .
$$
    For N = e^{ik·x}, u = Ue^{iq·x}, h = He^{ip·x} with p = −k − q:
$$
\hat M(p,q)\hat G(q)+\textstyle\sum_j\hat C_j(k)\,\hat S(q,p)_{j}+\hat C(k+q)\,\hat L(k,q)^T=0 .
$$
    M is the per-place second-order Regge stencil, E⁽²⁾_N = Σ_pN_p½Σ h(p+y)ᵀM(y,y′)h(p+y′), from exact (hyper-dual) dihedral Hessians.
  - **(DD), at order π:**
$$
\hat S(q,q')[U,\hat G(q')V]-\hat S(q',q)[V,\hat G(q)U]=\hat G(q+q')\,\hat B(q,q')[U,V].
$$
  - **Field order 2, not tested:** the π² part of {H, D}, which involves the kinetic metric's h-dependence; E⁽³⁾; and {H, H} at second order.
- **A structural fact (validation).** The lapse coupling to the body diagonal vanishes identically: max_p|∂E_p⁽¹⁾/∂L_b| = 4×10⁻¹⁶. So β's second-order part never enters at this order, and N0′ with a nonlinear or a linear β gives the same conditions.
- **The search.**
  - Both conditions are linear in (s, l, b). The search is a least-squares existence problem over fit samples, with held-out samples to judge.
  - **Stencils:**
    - J1: radius-1 axis offsets, 7,182 unknowns;
    - J2: all box(1) pairs with |r − r′|∞ ≤ 1, 47,334 unknowns.

    Both are reduced to the S3-symmetric subspace (1,233 and 8,036), which loses nothing because the problem is S3-covariant.
  - **Variants:**
    - "GR" imposes L → u·∇N and [u, v] → the Lie bracket through their first moments;
    - "free" leaves them open.
- **Decision rule.**
  - EXISTS if the fit residual and every held-out ρ are ≤ 10⁻⁸.
  - NOT FOUND if the median held-out ρ (rand set) is ≥ 10⁻⁴.
  - Otherwise UNDECIDED.
  - Kill rules K86a–d: J1-GR, J2-GR, J1-free, J2-free.

**Result.**

| rule | variant | unknowns (S3-reduced) | fit residual | held-out ρ, median / max: {H, D} | {D, D} | verdict |
|---|---|---|---|---|---|---|
| **K86a** | J1-GR | 1,233 | 0.33 | 0.099 / 0.62 | 0.070 / 0.58 | **FAIL** (as expected) |
| **K86b** | J2-GR | 8,036 | 1.6×10⁻¹⁵ | 4×10⁻¹⁶ / 1.7×10⁻¹² | 5×10⁻¹⁶ / 6×10⁻¹⁵ | **PASS** (against the expectation) |
| **K86c** | J1-free | 1,233 | 0.31 | 0.095 / 0.75 | 0.065 / 0.68 | **FAIL** (as expected) |
| **K86d** | J2-free | 8,036 | 1.5×10⁻¹⁵ | 4×10⁻¹⁶ / 1.8×10⁻¹² | 5×10⁻¹⁶ / 7×10⁻¹⁵ | **PASS** (against the expectation) |
| diagnostic | J1, {H, D} alone | 1,233 | 0.24 | 0.067 / 0.86 | (not fitted) | NOT FOUND |
| diagnostic | J1-GR, unreduced | 6,972 | 0.31 | 0.10 / 0.64 | 0.075 / 0.63 | NOT FOUND |
| diagnostic | J2, {H, D} alone | 8,036 | 1.5×10⁻¹⁵ | 4×10⁻¹⁶ / 1.8×10⁻¹² | (not fitted: 0.24) | EXISTS |

**Overall (registered): PASS.** One local sliding on the box(1) stencil (|r|∞, |r′|∞, |r − r′|∞ ≤ 1) closes {H, D} and {D, D} together at first order in the fields.
- **The maxima** come from the "small" held-out set (wavevectors scaled by 0.1).
- **Along rays toward k = 0, J2's residual rises from 7×10⁻¹⁶ to 2×10⁻¹⁰.** This is floating-point cancellation, not a defect (the check). The terms fall as s³, while |M̂(−q, q)Ĝ(q)| sits at 2×10⁻¹⁴, and the rise is identical for all three J2 solutions.
- **The registered expectation** was NOT FOUND for J1 (right) and "leaning NOT FOUND" for J2 (wrong). Its rationale does not apply at this order (the check). Bahr & Dittrich find that Regge's would-be gauge modes near flat space lose their symmetry *quadratically* in the curvature, i.e. at field order 2.
- **The registered dichotomy between GR and free moments is void at J2 (the check):** K86b ⇔ K86d.
  - Of the 38 GR moment constraints, 28 are implied by the equations themselves.
  - The other 10 are a constant redefinition of the sliding's parameter, n(u, h)_c = A_caj u_a h_j, which fits J2's stencils.

![Run 86](../figures/86_joint.png)

**The independent check.** The check used its own real-space construction, sharing no code with the run: its own Kuhn lattice, a third dihedral formula (from the adjugate of the vertex Gram matrix), an exact β solve, and the gauge map as the exact derivative of the embedding-to-metric map.
1. **Hashes.** 9/9 OK. The registration precedes the run, and the stored solutions reproduce every registered held-out statistic exactly.
2. **The conditions, re-derived.** (HD) and (DD) are complete at field order 1, with the signs confirmed. The π² terms and E⁽³⁾ are field order 2. The body coupling vanishes (3×10⁻¹⁶), so β₂ never enters.
3. **Regge's second-order energy, recomputed independently.** It agrees with the stencil M to 5×10⁻¹⁴ – 6×10⁻¹² for five lapse fields on 6³ and 7³ lattices.
4. **The brackets, end to end in real space,** with explicit Poisson brackets on a 5³ lattice:
   - J2-GR closes {H, D} to 3×10⁻¹³, limited by the differentiation, and {D, D} to 5×10⁻¹⁶;
   - {D[u], D[v]} equals D[[u, v]] to every printed digit;
   - the Fourier rows match real space to 10⁻¹³ even where they do not vanish (J1, random unknowns).
5. **Fresh special loci** (k, q, p or q + q′ → 0; zone corners): the J2 solutions close to ≤ 7×10⁻¹¹.
6. **J1, re-solved with LAPACK** (SVD and pivoted QR, no normal equations): the registered fits are reproduced exactly, and are robust to rcond, row scaling, a fresh seed and the S3 reduction.
   - **J1's defect is of order a², and it is already in {H, D}.** Fitted with wavevectors scaled by s, J1's best residual falls as s²: 0.32, 1.2×10⁻², 1.2×10⁻⁴ and 1.1×10⁻⁵ at s = 1, 0.1, 0.01 and 0.003.
   - The registered J1 rays, which tend to 1, describe the uniform-zone fit, not the stencil.
7. **What the sliding needs (the check's probes, with LAPACK).**
   - {H, D} alone closes once either slot of S is enlarged beyond J1's axis offsets: the shift in box(1) (P1) or the metric in box(1) (P2).
   - The joint closure also needs the bracket stencil larger than B₁ × B₁. P2 closes with J2's bracket stencil (1.8×10⁻¹⁴), but not with J1's (0.13).
   - At no stencil size do (HD) and (DD) contradict each other.
   - Run 86's own post hoc probes (table below) agree: with J2's L and [u, v] stencils, P2 closes and P1, P3 and P4 do not.

**Which offsets the sliding needs (post hoc, `posthoc/ph86_family.py`).** Each probe uses the registered samples and decision rule, with GR's moments, and keeps J2's stencils for L and [u, v].

| probe | S: u at x + r, h at x + r′ | S pairs | held-out max ρ: {H, D}, {D, D} | |
|---|---|---|---|---|
| P1 | r in the 3×3×3 box, r′ on the axes (0, ±e_a) | 189 | 0.077, 0.034 | not found |
| **P2** | **r on the axes, r′ in the 3×3×3 box** | 189 | **7×10⁻¹⁵, 7×10⁻¹⁶** | **exists** |
| P3 | both in the "diagonal cone" {0, ±e_a, ±(e_a+e_b), ±(1,1,1)}, within one step | 151 | 0.017, 0.009 | not found |
| P4 | r = r′ (one place per term) | 27 | 0.61, 0.53 | not found |

**What was guaranteed, and what was tested (the check).**
- **Guaranteed before the run:**
  1. {H, H} at this order (Run 85: equivalent to linear first class).
  2. {H, D} alone, at some finite radius. Ĉ's components generate the ideal of functions vanishing to second order at k = 0, and the O(k) part of term 1 is exactly −iĈ(q)(k·U).
  3. The Ĉ-direction of (DD), given (HD).
  4. L for affine lapses.
  5. A *non-local* joint solution, which always exists. It would have poles where the output wavevector vanishes.
- **Tested, and not implied by any of these:** whether the two remaining components of (DD) per wavevector (the TT directions) close *locally* together with (HD).
  - They do, at box(1).
  - Neither the exact vertex-translation symmetry of flat Regge configurations nor Run 84 implies it. The flat-embedding sliding is not a local function of h, because it depends on the rotation part of the displacement.
- **The post hoc Taylor expansion** (below) works at the origin of momentum space only. So it does not settle locality on the loci k = 0, p = 0 or Q = 0 at finite other momenta; the J2 result does.

**The structure functions: what is forced, and what is a choice (the check).**
- **L.** Its affine-lapse part is forced at every q, L̂(0, q) = 0 and ∂_kL̂(0, q) = i·1. That is L = u·∇N. Every other change of L across the solution family lies in m²_k, a redefinition.
- **[u, v] at leading order.** The basis-independent part (its zeroth moment, and the part of its first moment antisymmetric in the derivative and the second slot) equals the Lie bracket's, ½(δ_adδ_cb − δ_abδ_cd), to 8×10⁻¹⁶ in both J2 solutions.
  - J2-free's "0.86 from the Lie bracket" is exactly a constant redefinition u → u + n(u, h), residual 1.2×10⁻¹⁵. It is not a deformation.
  - **So the GR content of L and [u, v] at leading order is forced by (HD) and (DD), not imposed.**
- **Beyond leading order.** One genuine free parameter κ appears in [u, v] at degree 2 (order a): no local redefinition removes it.
  - The registered J2-GR member carries an O(a) deformation of this kind.
  - The family also contains slidings whose bracket is the Lie bracket up to redefinitions through degree 4.
- **The family.** The null space has 710 dimensions (free moments) with a clean gap, or 700 with GR's moments. Of the 710:
  - 390 are redefinitions u → u + n(u, h);
  - 4 are D[u] → D[u] + H[m(u, π)];
  - 17 more change neither structure function on pure-gauge h;
  - the other 299 are unidentified. They are consistent with, but not proved to be, canonical point transformations h → h + g(h, h).

**Order by order at the origin of momentum space (post hoc, `posthoc/ph86_taylor.py`).**
- **The method.** Every symbol is expanded in homogeneous powers of the two wavevectors. The knowns M̂, Ĝ and Ĉ are expanded exactly, checked against the full symbols to 10⁻¹⁵. The unknowns' moments are left completely free.
- **The result.** The joint conditions are solvable through degree 5: (HD) to degree 5, (DD) to degree 4. Every block's residual is at rounding level. (Blocks whose terms are all at rounding are measured against 10⁻⁶ of the largest block, which gives ≤ 10⁻¹⁰.)
- **Solver checks.** Planted solutions are recovered to 10⁻¹⁶, and a negative toy is rejected (ρ ≈ 1).
- **The limit.** This settles the expansion at the origin only (above).

**A structural fact.** The lapse coupling to the body diagonal vanishes identically. Hence:
- N0′'s nonlinear β drops out at this order;
- the conditions involve only Regge's second-order energy, the sliding and the lapse coupling;
- the kinetic form does not enter at field order 1, and neither does λ.

**Reading.**
1. **The first test at this order that Run 84 does not decide passes.**
   - The two TT components of {D, D}, together with {H, D}, close with a local sliding on the box(1) stencil.
   - With Run 85, all three brackets close at field order 1 on this lattice, with local structure functions:
$$
\{H[N],H[M]\}=D[\xi U],\qquad\{H[N],D[u]\}=-H[L(u,N)],\qquad\{D[u],D[v]\}=D\big[[u,v]\big].
$$
   - Their basis-independent continuum content is GR's: U → N∇M − M∇N, L → u·∇N (exact for affine N), and [u, v] → u·∇v − v·∇u. This content is forced by the equations, not imposed.
2. **What it does not show (the check):**
   - an exact or fully nonlinear diffeomorphism symmetry;
   - a unique sliding. The sliding found is one member of a large family and has not been identified with a geometric action;
   - anything at field order 2.
3. **Consistent with the literature, not a surprise.** Near flat space, Regge's diffeomorphism symmetry is broken quadratically in the curvature (Bahr & Dittrich 2009). That is field order 2, which this record has not reached.
4. **For the routes.** GR's route survives the first nonlinear order, so the khronometric fallback is not triggered. The free parts of the sliding (the family, and κ in [u, v]) are what field order 2 must fix or rule out.

**Limits.**
- Field order 1 only. Untested:
  - the π² part of {H, D}, which needs the kinetic metric's h-dependence;
  - Regge's third-order energy;
  - {D, D} at order πh;
  - {H, H} at order πh.
- N0′, a flat background and one triangulation.
- The lapse coupling is fixed at Run 84's end average.
- The structure functions are local and bilinear, and L does not depend on h.
- The sliding is not unique; which member, if any, continues to field order 2 is open.
- The registered reading's sentence "that sliding is the lattice's nonlinear diffeomorphism at this order" is not supported (the check). The same applies to the reading string in `analyse86.json`.
