### Run 89: the kinetic sector at order a², with the kinetic dressing and the lapse couplings freed (Note H, field order 2; a calculation)

*25 October 2026.*
- *Registered and hashed before the run (`modes89/PREREG_89.md`, with the code and the validation outputs; 17:43:41 UTC).*
- *Validation beforehand:*
  - *the coefficient-mode solver reproduces Run 88 (closes at D1, fails at D2 with Run 88's rank);*
  - *the new terms against explicit real-space Poisson brackets (the dressing and U⁰'s change) and against direct substitution (the lapse couplings);*
  - *the Jacobians;*
  - *planted and negative toys at D2.*

  *A dry run at D1 and two disclosed fixes (a results-file save, a report degree) preceded the registration.*
- *An independent agent checked the run (below), and its corrections are adopted here.*

**Why.** Run 88 found no local first-class closure of the kinetic sector at order a² for the registered lattice Hamiltonian. The failure began in {H, D} at order π², the D4 dressing's covariance. Post hoc, the Run 88 check found that a non-ultralocal a² dressing closes that part, while {H, H} still failed under every freedom it tested. It recommended registering both, and it listed the first-order energy's a² lapse coupling as untested.

**Question.** At order a², does the kinetic sector close once these freedoms of the *theory* are added?
- (i) the kinetic term may couple neighbouring places;
- (ii) in addition, both energies' lapse couplings may change.

**The freedoms** (added to Run 88's 'wide' form, which already contains every triangular change of constraint basis):
- **The order-a² kinetic dressing, non-ultralocal.** Ω → Ω_D4 + Ω₂, with
$$
\Omega_2(k,s)_{il}=P(k,s)_{il}+P(k,-k-s)_{li},
$$
  the general symmetric local π² term linear in N (real space: Σπ·P(N)π). With it, U⁰'s change: U⁰ → U⁰ + Q(k₁,k₂) − Q(k₂,k₁).
- **In form (ii), the order-a² lapse coupling of Regge's second-order energy.** The general change vanishing for constant lapse:
$$
\delta M(p,q)_{in}=\sum_b i(p+q)_b\big[Z(p,q)_{bin}+Z(q,p)_{bni}\big].
$$
- **In form (ii), the order-a² lapse coupling of the first-order energy:** C → C + δC (degree 4), keeping E⁽¹⁾'s gauge invariance, δC(k)·G(−k) = 0.

Together, δM and δC are an energy change E → E − Σ∂N·V(h) (the check).

**The forms:**

| form | conditions | brackets |
|---|---|---|
| (i) | HD1, DD1, A, HH1 | the spatial covariance of the λ = 1 kinetic sector, with {H, H} at order π |
| (ii) | HD1, DD1, A, B, HH1, CG | the full kinetic sector |

The truncation is D2 (order a²); there are 4,558 (i) and 6,146 (ii) reduced unknowns.

**The solver** works on exact monomial coefficients, as the Run 88 check recommended. Each block's rows give its exact polynomial coefficients, so solvability does not depend on the point set; a held-out point set gives the coefficients a second time.

**Decision:**
- **EXISTS** if, on both point sets, non-floored max ρ ≤ 10⁻⁸ and floored |residual| ≤ 10⁻¹² of the largest block;
- **NOT FOUND** if every start has held-out max ρ ≥ 10⁻⁴.

**Controls.** NC1 and NC2 are random top-degree terms, which must be NOT FOUND for a PASS to stand.

**Result (registered).**

| rule | form | starts | final cost | held-out max ρ: non-floored | verdict |
|---|---|---|---|---|---|
| **K89a** | (i) | 1 of 3 (closed at start 0) | 2.7×10⁻²² | 1.1×10⁻¹⁵ | **PASS** (as expected) |
| **K89b** | (ii) | 1 of 3 (closed at start 0) | 6.7×10⁻²⁷ | 1.2×10⁻¹⁵ | **PASS** (against the expectation) |
| NC1, NC2 | controls | | | 0.70, 1.0 | NOT FOUND |

**Overall (registered): FIRST-CLASS.**

![Run 89](../figures/89_first_class_a2.png)

**The independent check.** Its certifying computations were:
- Cauchy-integral degree extraction of the full-symbol residual of the stored solutions, realised as finite stencils, on fresh points;
- LAPACK SVD on the exact S3-reduced coefficient systems;
- exact eigenvalues for the dispersion.

The findings:
1. **Hashes and time order.** 23/23 OK at the start and the end. The registration precedes every run output, and every stored solution reproduces every logged block exactly.
2. **Both closures are certified.**
   - Independent extraction gives non-floored max ρ 5.9×10⁻¹⁴ (K89a) and 4.9×10⁻¹⁴ (K89b).
   - The ranks match the engine's (3,042 and 3,910), with clean gaps.
   - The closures are genuine balances. In A3, for example, the dressing terms cancel a base-term sum of 7.85; in B4, five groups of terms of size 9–67 cancel to rounding.
   - Random symmetric terms in every block lie 35–100% outside the Jacobian's range, so the freedom does not absorb anything.
3. **What closes {H, H} is the first-order energy's a² lapse coupling δC.**
   - Without it, the fit from the K89b solution stalls at cost 1.9×10⁻², with the residual in B4 and HD15, as in the Run 88 check's probes.
   - Of δC's six gauge-invariant degree-4 directions, two are lapse relabellings (the basis change H[N] → H[N + a²DN]), and two are fixed at the solution.
   - Only about 7% of the stored δC is essential; the rest is relabelling.
4. **The solution's large norms are almost all free directions.** The part that cannot change has norms (reduced): dressing 0.11, Z 0.03, δC 0.15, W⁽¹⁾ 0.43.
   - The π-linear term V can be removed.
   - A π-linear D[Y] term at a² is needed in this basis.
   - δC's essential part, read as a lapse-gradient term, is about 27% of Regge's own order-a² coupling C₄.
   - **No simple geometric identification (post hoc).** None of the candidates tested lies in the allowed set: D4 itself, any ultralocal dressing (so no re-averaging of the lapse), a smoothing of π, or π paired at the two ends of each relation (distances 0.15–0.55 of D4's own a² part).
5. **The closing Hamiltonians change the ordinary dynamics, and this is the main physical result.** At constant lapse (N = 1) the linear graviton (TT) waves of Run 84's lattice obey
$$
\omega^2=|\delta|^2=s^2-\tfrac1{12}\sum_a s_a^4+O(s^6),
$$
   which has a small direction-dependent error at order a².
   - **K89b's closing Hamiltonian gives ω²_TT = s² + O(s⁵).** The a² lattice anisotropy is removed exactly, in all 30 directions tested, with no splitting between the two polarisations at a². The coefficients that the family cannot change are exactly the ±1/24 that cancel the −s_c⁴/12:
$$
\Omega_2(0,s)_{ij}\ni K^{-1}_{ij}\,s_c^2/12\qquad(i,j\ \text{in the plane}\perp c).
$$
     A polarisation splitting of about ±0.019 s⁵ appears at order a³, beyond the truncation.
   - **K89a's closing Hamiltonian gives an anisotropic, birefringent a² dispersion,** with a polarisation splitting of up to 0.17 s⁴.
   - In both cases the dispersion is effectively fixed: it barely changes along the solution family.
   - Form (i) has no closure that keeps Run 84's dispersion. By variable projection, the minimum residual is 0.61 at every sliding sampled, against 10⁻¹³ without that restriction (post hoc).
6. **Why (the check's interpretation, not proved as a theorem here).** GR's algebra contains the Poincaré algebra: {H[1], H[x^a]} = D[e_a] is the boost relation.
   - At field order 2, on the lattice, (B) and {H, H} at order π carry it, and closing them requires Lorentz-invariant linear dynamics through the order of the truncation.
   - The constant-lapse energy is fixed (δM and δC vanish there), so only the dressing's constant-lapse part can supply the a² improvement.
   - This explains Run 88's (A)–(B) incompatibility, why δM alone could not help, and the exact ±1/24.
   - In lattice language, first-class closure at a² requires an order-a² (Symanzik-type) improvement of the graviton dispersion.

**Corrections adopted (the check).**
- **The report's "minimum-norm P over the solution set"** is a first-order (tangent-space) minimum, and not itself a solution. The supported size statement is the forced part of the dressing: 0.41 and 0.39 of D4's own order-a² part.
- **The report's "contains pure-s² terms, so it changes the kinetic term at constant lapse"** does not follow, since slides also contain such terms and act trivially. The valid statement is the dispersion in item 5.
- **NC2's NOT FOUND, as run, is weak.** Its Gauss–Newton diverged, because the solver accepts any step once the step size falls below 10⁻³. A linear test at the K89b solution supports it: 60% of the NC2 term lies outside the Jacobian's range.
- **The registration's khronometric statement was incomplete.** The khronometric route proper has λ > 1 and an α term in the lapse gradient a = ∂ln N. That term is nonlinear in N, so it lies outside the H[N] = ∫N·H framework, and without it the non-projectable theory is inconsistent (Henneaux, Kleinschmidt and Lucena Gómez 2010). {H, H} also supplies the coefficients of the lapse equation. K89a tests the spatial covariance of the λ = 1 kinetic sector, which a khronometric theory also needs, not the khronometric route itself.
- **The projectable case is untested, not "empty".** With constant lapse the kinetic sector has no source, but the sliding is then fixed by the potential sector.
- **The registered reading "GR's route survives at this order in the kinetic sector"** holds with these qualifications:
  - the closing Hamiltonian has different constant-lapse dynamics (ω² = s², not |δ|²), and this is effectively forced;
  - it needs the first-order energy's a² lapse coupling and a π-linear D[Y] at a²;
  - the potential sector at a² and field order 3 are untested.
- **The registered expectation for K89b** ("no specific reason to expect δC to supply what (B) needs") was wrong: δC is what closes (B).
- **The sizes table's "δC: 44"** counts every degree. The effective freedom is the six gauge-invariant degree-4 directions of item 3.
- **The rank drop at the K89b solution** was 4,258 (iteration 2) to 3,910 (iteration 3). It is not a degenerate point: the 389 extra null directions have singular values that vanish as the iterate approaches the solution set.
- **A latent bug in the report's residual share by condition** (used only for a form that does not close, so not triggered): it strips digits from block names.

**Reading.**
1. **The kinetic sector is first class at order a²,** but only for a different lattice Hamiltonian. The changes are:
   - a non-ultralocal order-a² kinetic term, whose constant-lapse part makes the graviton dispersion relativistic through a²;
   - an order-a² change of the first-order energy's lapse coupling, equivalent to a lapse-gradient term −Σ∂N·V(h);
   - a π-linear D[Y] structure function at a².

   Run 88's FAIL concerned the registered choices: the ultralocal dressing, the constant-lapse kinetic term and E⁽¹⁾'s lapse coupling.
2. **Requiring GR's constraint structure at order a² fixes part of the lattice's dynamics.** Gravitational waves must travel at exactly the same speed in every direction through that order. The choices made by hand in Runs 84–85 are thereby partly replaced by a requirement. This does not derive Lorentz invariance: GR's constraint algebra, imposed here, contains it.
3. **For the routes.**
   - GR's route survives in the kinetic sector at a², with relativistic waves.
   - A preferred-frame Hamiltonian can close the spatial brackets with direction-dependent waves (K89a). The khronometric route proper (λ > 1, with its α term) is untested.
4. **Bearing on the two readings of how space curves (Note G).** Run 88's modest count toward reading (A) rested on {H, H} failing on a fixed-connectivity lattice. In the kinetic sector at a² that failure came from hand-placed choices, and a corrected kinetic term and lapse coupling remove it, so the count is withdrawn at this order. The literature's expectation of failure away from flat space, and the potential sector, remain untested here.
5. **Size.** The effects are of relative order (as)², far below any measurement at CO's hop. They bear on consistency, i.e. which lattice dynamics is admissible.

**Limits.**
- The kinetic sector only. The decisive open test for GR's route is the potential sector at a² (conditions C and D at D2, where Regge's third-order energy, δM and δC all enter); it needs a sparse solver.
- Formal, at the origin of momentum space; through a²; at field order 2.
- The solution is a family, not a unique Hamiltonian. The dressing's forced part is small, and most of its freedom is unfixed.
- N0′, λ = 1, a flat background, one triangulation.

*Note added 26 October, after Run 90.* Run 90's check corrects and confirms parts of this section:
- **"In both cases the dispersion is effectively fixed" is too strong for K89a.** Its birefringent anisotropic part is fixed, but one isotropic s⁴ coefficient is free along its family. K89b's dispersion is fixed, and exactly relativistic (to 8×10⁻¹⁴).
- **"Form (i) has no closure that keeps Run 84's dispersion (0.61)" stands, and is now certified** (Run 90's K90d). The check's rows coincide with the exact ones at every form-(i) closure.
- **The boost-relation interpretation is supported** within the full kinetic sector without an order-a constant-lapse kinetic change: Run 84's dispersion and an isotropic non-relativistic one are not found there.
