### Run 85: GR's constraint algebra at the first nonlinear order on Run 84's lattice (Note H, second order; a calculation)

*24 October 2026.*
- *Registered and hashed before the run (`modes85/PREREG_85.md`, with the code and the validation outputs; 11:40:05 UTC).*
- *Validation beforehand was structural:*
  - *agreement with Run 84's objects;*
  - *the linear gauge and time-reparametrisation relations;*
  - *the bracket formula, checked in real space on an unregistered dressing;*
  - *the continuum analog;*
  - *the least-squares search, on a toy with a known answer.*

  *A dry run's outputs were deleted unread.*
- *After the run, a post hoc analysis described the closing dressings and probed the test's sensitivity; it is labelled post hoc.*
- *An independent agent checked the run with its own fully nonlinear construction (below). Its corrections are adopted.*

**Question.** Run 84 gave GR's route a healthy linear realisation on the Kuhn lattice, with the Hamiltonian constraint first class at linear order. In the continuum, what singles out GR is that the constraints keep closing beyond linear order:
$$
\{H[N],H[M]\}=D\big[\gamma^{ij}(N\partial_jM-M\partial_jN)\big].
$$
On lattices this generically fails (Bahr & Dittrich 2009). **At the first nonlinear order, does the bracket of two smeared Hamiltonian constraints of Run 84's GR route (N0, λ = 1) close onto the momentum constraints?**

**The canonical form.**
- **Variables.** The vertex metric h(x) and its momentum π(x), six of each per place. h(x) is read from the six relations arriving at x:
$$
h_{aa}(x)=2q_a(x-e_a),\qquad h_{ab}(x)=q_{ab}(x-e_a-e_b)-q_a(x-e_a)-q_b(x-e_b).
$$
  - The map from relations is local and invertible.
  - In N0 the body diagonal is auxiliary.
  - In these variables Run 84's kinetic energy is ultralocal: T = Σ_x ½ḣᵀKḣ = Σ_x ¼[ḣ:ḣ − (tr ḣ)²].
- **The smeared Hamiltonian constraint:**
$$
H[N]=\sum_x\tfrac12\sum_{kl}\pi_k\pi_l\,(\Omega_{kl}N)(x)\;-\;\xi\sum_e\bar N_e\,2\ell_e\varepsilon_e,\qquad(\Omega_{kl}N)(x)=\sum_rw_{kl}(r)\,N(x+r),\qquad\sum_rw(r)=K^{-1}.
$$
  - The potential term is Regge's energy with Run 84's end-average lapse.
  - **The dressing** w, how the lapse multiplies the kinetic energy, is the one new choice at this order. At N = 1 every dressing gives Run 84's theory.
- **The bracket at the first nonlinear order.** With N = e^{ik·x} and M = e^{ik′·x}, to first order in the fields:
$$
\{H[N],H[M]\}=-\xi\sum_x\pi(x)\cdot B(k,k')\,e^{i(k+k')\cdot x},\qquad B(k,k')=\hat\Omega(k')\hat C(k)-\hat\Omega(k)\hat C(k').
$$
  - Ĉ is the lapse coupling's symbol in h.
  - The bracket closes onto the linear momentum constraints D[u] = Σπ·δh(u) exactly when B(k, k′) lies in range Ĝ(k + k′), the symbol of sliding.
  - At k′ = −k that range is {0}, so B(k, −k) must vanish.
- **The residual:**
$$
\rho=\frac{\|P_\perp B\|}{\|K^{-1}\|_2\,\big(\|\hat C(k)\|+\|\hat C(k')\|\big)},
$$
  with P⊥ the projector onto the complement of range Ĝ.

**The dressings.**
- **D1:** the lapse at the place of the vertex metric (GR's ultralocal form).
- **D2:** Run 84's literal per-place density, with the lapse at its place.
- **D3:** each kinetic monomial with the lapse averaged over the places its relations touch.
- **G1 and G2:** any local dressing within one or two spacings (546 and 2604 free parameters), fitted by least squares on 1,900 pairs and tested on 1,200 held-out pairs.

**Point sets and kill rules.**
- **Pairs:**
  - 2000 random pairs;
  - 300 with k′ = −k;
  - 300 with k′ near −k (10⁻³–10⁻¹);
  - rays at |k|, |k′| = 0.01–0.32, along 50 direction pairs, and along 50 directions with k′ = −k;
  - 500 fresh pairs.
- **A fixed dressing closes** if max ρ ≤ 10⁻⁹.
- **A local dressing exists** if the fitted one gives max ρ ≤ 10⁻⁸ on both the fit set and the held-out sets.

**Verdicts.**

| test | prediction | registered result | physics (the check) |
|---|---|---|---|
| **K85a, D1** | FAIL: at k′ = −k, B = 2iK⁻¹ Im Ĉ(k) ≠ 0, because h reads the relations *arriving* at a place | **FAIL.** max ρ = 0.34; ρ ∝ s^1.00. The k′ = −k identity holds exactly | **FAIL.** The defect is the shear lapse, offset by half a plaquette diagonal |
| **K85b, D2** | FAIL | **FAIL.** max ρ = 0.56; ρ ∝ s^1.00 | **FAIL** |
| **K85c, D3** | no prediction | **FAIL.** max ρ = 0.25; ρ ∝ s^1.00 | **FAIL** |
| **K85d, G1 (radius 1)** | NOT FOUND (held loosely) | **EXISTS.** ρ ≤ 1.0×10⁻¹⁵ on the fit set, 8.8×10⁻¹⁶ held out | **EXISTS.** Its bracket is identical to D4's (below) |
| **K85e, G2 (radius 2)** | NOT FOUND (held loosely) | **EXISTS** | **EXISTS**, the same bracket |

The registered expectation for G1 and G2 was wrong. It rested on the no-go theorem for lattice Leibniz rules (Kato, Sakamoto & So 2008). That theorem does not cover the *twisted* rule used here.

![Run 85](../figures/85_algebra.png)

**The closing dressing (post hoc, confirmed by the check).**
1. **D4.**
   - Products of the axis stretches (π_aaπ_bb, π_aa²) take the lapse at x.
   - Each shear term π_ab² takes the lapse averaged over the two ends of its face diagonal, ½[N(x) + N(x − e_a − e_b)].

   In the Lagrangian, at λ = 1:
$$
T=\sum_x\Big[-\frac{1}{2N(x)}\sum_{a<b}\dot h_{aa}\dot h_{bb}+\sum_{a<b}\frac{\dot h_{ab}^2}{N(x)+N(x-e_a-e_b)}\Big]+O(n^2).
$$
   D4 closes on 3,000 fresh pairs, including pairs with k′ within 10⁻⁶ of −k, to 1.3×10⁻¹⁵.
2. **It is the only one, up to canonical transformations (the check).**
   - The closing dressings in the radius-1 box form a 56-dimensional family. 56 = dim Sym³(ℝ⁶): the family is D4's orbit under the ultralocal canonical transformations generated by Σ_x ⅙T_klj π_kπ_lπ_j.
   - Every member gives the same bracket. The registered G1 is D4 plus such terms, to 6×10⁻¹⁵.
3. **Why it exists: two exact identities (the check).**
   - The lapse coupling is a lattice Hessian. With (Δ⁺N)_a(x) = N(x + e_a) − N(x):
$$
C^\dagger N=K\,\Gamma(\Delta^+N).
$$
     Here Γ is sliding, so 𝓗 = ΓΔ⁺ is the second-difference operator. Each diagonal second difference is centred at x; each shear difference is a plaquette centred at x − (e_a + e_b)/2. This is the vertex-metric form of Run 84's c_G = Ggδ = c_ends.
   - A twisted discrete Leibniz rule, exact:
$$
\Gamma(U)=(\mathcal AN)\,\mathcal HM-(\mathcal AM)\,\mathcal HN,\qquad U_a(x)=N(x)M(x+e_a)-M(x)N(x+e_a),
$$
     where 𝒜 places the lapse at the centre of each second difference. D4 is Ω = 𝒜K⁻¹.
   - So, with GR's sign and a local structure function:
$$
\{H[N],H[M]\}=D[\xi U],\qquad U\to\xi\,(N\nabla M-M\nabla N).
$$
4. **What the test discriminates.**
   - **On Run 84's kinetic form at λ = 1, first-order {H, H} closure is equivalent to the Hamiltonian constraint being first class at linear order (the check).**
     - Setting M = 1 gives B(k, 0) = K⁻¹Ĉ(k) ∈ range Ĝ(k), which is Run 84's linear condition.
     - Conversely, linear first-class structure forces Ĉ = φĈ₀ with φ local, and D4 composed with φ closes it.
   - **So K85d–e follow from Run 84. They are not independent evidence of nonlinear consistency.**
   - **λ ≠ 1:** no dressing of any range closes the algebra (residual about 0.03 at λ = 1.1, 4×10⁻⁴ at λ = 1.001). The reason is linear: the shift has no zero-kinetic direction.
   - **The other two probes are trivial.**
     - A smeared coupling is closed by D4 with the lapse relabelled.
     - A randomly perturbed, non-gauge-invariant coupling closes only because Ĉ(0) ≠ 0, which permits a dressing with B ≡ 0. Such a coupling already fails {H, D} at zeroth order.

**What else the check found.**
1. **The bracket formula holds in a fully nonlinear construction.** The check's construction has √γ and γ⁻¹ in the kinetic term, two different lapse completions, Regge's full energy and three treatments of the body diagonal. Poisson brackets computed explicitly at small random fields agree with the formula to 10⁻¹²–10⁻¹⁶. The bracket's second-order part is present and of order one, and it differs between completions, as expected.
2. **N0's body diagonal is fine at this order but ill-defined beyond it.**
   - Its own equation depends on the lapse. The eight corner conditions on one body diagonal have rank 5, and the equation is singular when the lapse contrast inside a cube exceeds 5/3.
   - Higher orders need **N0′**, the body diagonal fixed by its N = 1 equation, β := β₁(h); or N1.
3. **A first probe of {H, D}.**
   - **At first order in lapse gradients,** Regge's second-order energy with the end-average lapse transforms exactly as a scalar density, with GR's coefficient and no lattice phase:
     $$\delta_uE^{(2)}_N=-E^{(1)}_{u\cdot\nabla N}+O(\nabla^2N).$$
     That is the part no local field-dependent sliding could repair.
   - **The O(∇²N) remainder** lies in the ideal generated by Ĉ, so a local field-dependent sliding exists that closes {H, D} on its own.
   - **Whether one sliding also closes {D, D}** is open. Thirteen natural candidates close neither.
4. **Literature.**
   - Discrete hypersurface-deformation algebras are known for 3D gravity, and for flat or homogeneously curved 4D sectors (Bonzom & Dittrich 2013).
   - Diffeomorphism symmetry of generic discretisations breaks at higher orders (Bahr & Dittrich 2009; Dittrich & Höhn 2013; Höhn 2014).
   - Shifted Leibniz rules become order-dependent for products of several fields (Bruckmann, Catterall & de Kok 2006), which bears on the next order.
   - Not found in any source checked: a Regge-type metric lattice closing {H, H} at first nonlinear order through a lapse dressing.

**Reading.**
1. **GR's route passes the first nonlinear test on this lattice, but the test turns out to add nothing to Run 84.**
   - The natural dressings fail at O(ka).
   - D4, which times each shear term by the lapse averaged along its face diagonal, closes the algebra exactly, with GR's structure function in lattice form.
   - On this kinetic form that closure is guaranteed by Run 84's linear result. Run 85 therefore establishes the lattice's *form* at this order: which dressing, and why (a twisted Leibniz rule). It does not supply new evidence of consistency.
2. **The decisive test is {H, D} and {D, D} together,** in N0′.
   - Does one local field-dependent sliding close both brackets, with structure functions tending to −u·∇N and the Lie bracket?
   - The O(∇N) part of {H, D} already passes exactly. What remains are two components per wavevector of {D, D}.
   - This is the first test at this order whose outcome Run 84 does not fix. Failure is possible: Regge-type gauge symmetries are known to break beyond linear order.
   - If it fails, the khronometric route becomes the operative one. That route needs only one global time and sliding, not {H, H} closure.
3. **What is chosen, not derived.**
   - D4's shear timing echoes the potential's end-average lapse, but CO's rules do not yet pick it.
   - N0′'s body diagonal is a definition.
4. **Limits.** One bracket, at the first nonlinear order, around a flat background, on one triangulation. The lapse coupling is fixed at Run 84's.
