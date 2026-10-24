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
- *An independent agent is checking the run (below).*

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

**Overall (registered): PASS.** One local sliding closes {H, D} and {D, D} together at the first nonlinear order, with GR's structure functions.
- **The maxima** come from the "small" held-out set (wavevectors scaled by 0.1).
- **Along rays toward k = 0, J2's residual rises from 7×10⁻¹⁶ to 2×10⁻¹⁰.** This is rounding: each term falls as s³ while the stencil sums do not. J1's residual instead tends to 1 there, because its best fit gets even the continuum limit wrong.
- **The registered expectation** was NOT FOUND for J1 (right) and "leaning NOT FOUND" for J2 (wrong).

![Run 86](../figures/86_joint.png)

**What the closing sliding is.**
1. **Its size.**
   - J2's sliding uses pairs of places (r, r′) within one step of x and of each other: u at x + r, h at x + r′.
   - Its coefficients are of order one (largest 0.47, norm 4.9), so there are no large cancellations.
   - J1's axis-only offsets cannot close even {H, D} alone. Run 85's sliding Γ itself reaches x − e_a − e_b, which J1 lacks.
2. **The structure functions.**
   - **L.** It comes out as u·∇N to leading order even when left free: the first moment of l equals δ_ad exactly in J2-free. This is forced by the O(k) part of {H, D} (validation V3, and the Run 85 check).
   - **[u, v].** It is GR's Lie bracket when that is imposed (J2-GR), but other brackets also close (J2-free: 0.86 away from the Lie bracket at |k| ~ 10⁻³).
   - **Why [u, v] is not unique.** At this order, redefining the sliding's parameter, u → u + n(u, h) with n local, changes S by Γ∘n and [u, v] by n(u, Γv) − n(v, Γu). That change has one derivative, like the Lie bracket. So [u, v] is fixed only up to such redefinitions, as in the continuum, where it depends on whether D is smeared with ξ^a or ξ_a.
   - **Beyond leading order (post hoc).** L also differs between solutions: 3% median relative difference at generic wavevectors between J2-GR and J2-free. [u, v] differs by 40%.
3. **The solution family is large.** The reduced null space has 700 dimensions (J2-GR) and 710 (J2-free). It includes these redefinitions and the canonical transformations generated by Σπ·Γw(h, h).
4. **Not stencil-specific (post hoc, `posthoc/ph86_taylor.py`).**
   - **The method.** Every symbol is expanded in homogeneous powers of the wavevectors. The knowns M̂, Ĝ and Ĉ are expanded exactly; checked against the full symbols to 10⁻¹⁵. The unknowns' moments are left completely free, which is what an arbitrarily large local stencil allows.
   - **The result.** The joint conditions are solvable order by order through degree 5: (HD) to degree 5, (DD) to degree 4, residuals 10⁻¹⁵–10⁻¹⁰. That is three orders in the lattice spacing beyond the continuum's degree 3.
   - **Solver checks.** Planted solutions are recovered to 10⁻¹⁶, and a negative toy is rejected (ρ ≈ 1).
   - So the closure is not an artefact of J2's stencil, and J1's failure is a stencil-size limit, not an obstruction.
5. **A structural fact.** The lapse coupling to the body diagonal vanishes identically. So N0′'s nonlinear β drops out at this order, and the conditions involve only Regge's second-order energy, Run 85's sliding and the lapse coupling.
   - **The kinetic form does not enter at field order 1.** The result is a property of Regge's energy with the end-average lapse. To the order tested, it transforms as a scalar density under a local lattice diffeomorphism whose algebra closes.

**Which offsets the sliding needs (post hoc, `posthoc/ph86_family.py`).** Each probe uses the same samples and decision rule as the registered run, with GR's moments; L and [u, v] keep J2's stencils.

| probe | S: u at x + r, h at x + r′ | S pairs | held-out max ρ: {H, D}, {D, D} | |
|---|---|---|---|---|
| P1 | r in the 3×3×3 box, r′ on the axes (0, ±e_a) | 189 | 0.077, 0.034 | not found |
| **P2** | **r on the axes, r′ in the 3×3×3 box** | 189 | **7×10⁻¹⁵, 7×10⁻¹⁶** | **exists** |
| P3 | both in the "diagonal cone" {0, ±e_a, ±(e_a+e_b), ±(1,1,1)}, within one step | 151 | 0.017, 0.009 | not found |
| P4 | r = r′ (one place per term) | 27 | 0.61, 0.53 | not found |

So within these probes, the sliding has to read the metric across the whole 3×3×3 box around x. The shift u is needed only at x and its six axis neighbours.

**The independent check.** In progress; its report will be added here.

**Reading.**
1. **The first test at this order not fixed by Run 84 passes.** With Run 85, all three brackets of GR's constraint algebra close at the first nonlinear order on this lattice, with local generators and GR's structure functions in the continuum limit:
$$
\{H[N],H[M]\}=D[\xi U],\qquad\{H[N],D[u]\}=-H[L(u,N)],\qquad\{D[u],D[v]\}=D\big[[u,v]\big].
$$
   - Here L → u·∇N, [u, v] → u·∇v − v·∇u, and U → N∇M − M∇N.
   - For this order, it is the realisation of hypersurface deformations that Bonzom & Dittrich (2013) found only in 3D or in flat and homogeneously curved 4D sectors. It applies here to perturbations of flat 3D space with lapse and shift.
   - Regge-type breaking of diffeomorphism symmetry (Bahr & Dittrich 2009), if present on this lattice, must appear at a higher order: field order 2 or beyond.
2. **What field order 1 does not test:**
   - the π² part of {H, D}, which needs the kinetic metric's h-dependence (not yet defined), together with the sliding S found here;
   - Regge's third-order energy;
   - {H, H} at second order, which brings in γ^{ij}(h), √γ and N0′'s β at second order.
3. **The khronometric route** stays a fallback, not the operative reading: GR's route has not failed.

**Limits.**
- First nonlinear order, field order 1 only.
- N0′, a flat background and one triangulation.
- The lapse coupling is fixed at Run 84's end average.
- The structure functions are local and bilinear, and L does not depend on h.
- λ does not enter at this order.
- The solution family is large. Which member continues to field order 2 is open.

