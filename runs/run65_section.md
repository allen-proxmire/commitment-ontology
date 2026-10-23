## 9zzl. Run 65: ED's static field equation is GR's lapse equation; option 3's rule for space

*21 October 2026. Option 3 chosen provisionally. Registered and hashed before the run (`rule65/PREREG_65.md`, 04:44 UTC). An independent agent checked it; its corrections are included.*

**Question.** Option 3 was chosen provisionally (§9zzk): all binding tension shears space and acts back on the cadence field, as in GR. What is that rule for space when written to all orders? What does it do to ED's stars and holes, and what in ED's static gravity is left of its own?

**The identity.** Write a static metric in isotropic coordinates as ds² = −N²dt² + ψ⁴(dr² + r²dΩ²).
- **GR's equation for the clock rate** (its R₀₀ equation) is
$$
D^2N=4\pi N(e+3p),\qquad D^2f=\psi^{-4}\Big(f''+\frac{2f'}{r}+\frac{2\psi'f'}{\psi}\Big).
$$
- **ED's rule for space** is ψ²N = 1, that is g_ij = N⁻²δ_ij (the pattern rule c = N²). With N = e^{−U} it gives ∇N = −N∇U and ∇²N = N(|∇U|² − ∇²U), and ψ′/ψ = U′/2. So
$$
D^2N=-e^{-2U}N\,\nabla^2U ,
$$
  and the lapse equation becomes exactly ED's field equation, ∇²U = −4π(e + 3p)e^{2U}.
- **Hydrostatic balance**, h N = const, is the same in ED and GR.
- So **ED's static gravity is GR's equation for the clock rate, with a different rule for how space curves.** ED ties space to the clock. GR sets it from the energy density, through the Hamiltonian constraint
$$
\psi''+\frac{2\psi'}{r}=-2\pi\psi^5e\qquad(^{3}\!R=16\pi e).
$$
  The two rules agree at first order (ψ² ≈ 1 + U ≈ 1/N). Beyond it, every static difference between ED and GR found in this record comes from the rule for space.
- **How far ED's stars are from GR's rule.** With ψ = e^{U/2},
$$
\psi''+\frac{2\psi'}{r}+2\pi\psi^5e=\psi\Big(\tfrac14|\nabla U|^2-6\pi p\,e^{2U}\Big),
$$
  which is 16–106% of the source term inside the stars tested. In GR's terms ED's space is curved by the Tolman density minus a negative field-energy term, ³R_ED = 16π(e + 3p) − 2|DU|², against GR's 16πe (the check). In vacuum ³R_ED = −2|DU|² < 0, where GR has 0.

**Option 3, to all orders.** Option 3's rule for space is taken to be GR's Hamiltonian constraint (with the anisotropic equations satisfied in spherical symmetry).
- This is an identification, not a derivation from ED's primitives. A field whose own binding tension acts back consistently ends as GR (Deser 1970).
- The run tests that this system is GR's static gravity. It does not test the identification.

**Verdicts, as registered.**
- **K65a PASSES (the identity).** On ED's own stars (SLy, APR4, MPA1; h_c = 1.1, 1.3, 1.6), GR's lapse equation with ψ = e^{U/2} and N = e^{−U} holds to 6×10⁻¹⁶ of the source. This is an algebraic identity, so the check confirms the algebra rather than testing anything numerical.
- **K65b PASSES (option 3 = GR's stars).** The option-3 system (lapse equation, balance, Hamiltonian constraint) reproduces GR's TOV to 3×10⁻⁸:

| equation of state | M_max, option 3 / TOV | R(1.4 M☉), option 3 / TOV | M_max under option 1 (ED's rule, Run 57) |
|---|---|---|---|
| SLy | 2.048447 / 2.048447 | 11.7063 / 11.7063 km | 1.65 |
| APR4 | 2.188039 / 2.188039 | 11.3199 / 11.3199 km | 1.69 |
| MPA1 | 2.456444 / 2.456444 | 12.4345 / 12.4345 km | 1.91 |

- **K65c PASSES (static holes and exteriors).**
  - In vacuum the option-3 system gives ψ = 1 + M/2r and N = (1 − M/2r)/(1 + M/2r): Schwarzschild in isotropic coordinates. The clock rate reaches zero at r = M/2, a horizon where possibility runs out.
  - Every option-3 star's exterior matches it to 4.5×10⁻⁹.

![Run 65](figures/65_space.png)

**Reported.**
1. **The pulsar coefficient under option 3.**
   - The draw-weighted C = ⟨1/N⟩ − 1 for the 1.438 M☉ pulsar of PSR J0337+1715 is 0.425 (SLy), 0.442 (APR4) and 0.375 (MPA1). Under ED's rule it was 0.474, 0.492 and 0.400 (Run 57).
   - The triple then needs P₀/p_s ≳ 1.6–1.9×10⁵ (red noise) or 2.5–2.9×10⁵ (planet model), **provided Run 55's formula carries over**. Δ ≈ C p_s/P₀ was derived from ED's own action (Run 52); under option 3 it becomes Δ ≈ M_Komar/M_ADM − 1, and its weighting must be re-derived (the check).
2. **Which earlier runs change under option 3, provisionally** (first-order results are unaffected, since the two rules agree at first order):
   - **Neutron stars (Runs 57–63).** ED's stars become GR's for the same matter. Standard equations of state hold PSR J0740+6620. The need for near-causal matter (Runs 59–60), the GW170817 route analysis (Run 61) and the heavy-ion squeeze (Run 62) no longer apply as ED predictions; their GR columns are option 3's numbers. The test-mass orbit becomes GR's (Run 63: −27/8), and Run 64's open choice is settled with k = 0.
   - **Black holes (Runs 28, 32, 39, 41, 43).**
     - A static mass now has GR's horizon, reversing Run 32's "no horizon".
     - Its shadow is GR's (Run 28's +4.6% goes).
     - ED's core sits where N = 0, consistent with Run 43.
     - For static holes, option A follows from ED's lapse equation plus option 3's rule for space. For rotating holes (Runs 39, 41) the rotating case is not derived, so option A remains an input there.
   - **Strong-field engine runs (44–56).** These ran on ED's rule for space at neutron-star strength. Their structural results (exact fall in a scale-free medium; the first law, which GR shares) do not depend on that rule. Their strong-field numbers would shift and are to be re-read, not rerun.

**What the check added.**
1. **The identity, the solver and C are confirmed by hand and with the agent's own code.**
   - D²N = −e^{−3U}∇²U, and it holds to finite-difference error on an arbitrary U(r).
   - SLy at 1.438 M☉ gives R = 11.6815 km and C = 0.4254.
   - The Komar mass from the lapse flux equals the mass read from ψ to 10⁻¹⁰, as static GR requires.
   - K65a's 6×10⁻¹⁶ confirms the algebra only.
2. **ED's draw is exactly the Komar density.** ∂_i(ψ²∂_iN) = 4π(e + 3p)Nψ⁶ is the lapse equation in flux form.
3. **Option 3 costs more than a rule for space.** Two costs, recorded in §10:
   - **It revises ruling 2 from second order on.** Its back-reaction is the field acting on U in vacuum: in Schwarzschild U = −ln N = M/r + M³/(12r³) + …, so ∇²U ≠ 0 outside matter. Ruling 2's "the vacuum draws nothing" and "g₀₀ = −e^{−2U}" therefore hold only at first order.
   - **The engine's medium cannot carry it as built.** The medium has a curl-free flux, a flat Laplacian and an exponential clock, so it cannot produce GR's lapse at O(U³). A natural implementation (the agent's inference): possibility hops on the sheared space, with flux √γγ^{ij}∂_jP; the clock is N ∝ P; the sinks are the Komar draws. That gives D²N = 4πN(e + 3p) with no vacuum draw, and β = 1 comes from ψ rather than from the logarithmic outflow. The logarithmic medium's role, and the reason for p_s (Runs 22–24), would then have to be re-derived.
4. **The identification is honest as disclosed, but not unique.** Deser's argument needs a first-order Lagrangian, gauge invariance and no extra fields, and the field's stress tensor is ambiguous up to superpotentials (Padmanabhan 2008).
5. **Rotation is open.** For rotating holes, Kerr follows by uniqueness only if option 3 also puts the current field g₀ᵢ in GR's nonlinear form; ruling 2 currently builds it from boosted draws.
6. **Near-horizon shell.** Where N ≲ p_s/P₀ ≲ 10⁻⁵, the medium's g = p_s/P is no longer small. So option 3 is Schwarzschild except in a thin shell at redshift ≳ 10⁵. This is unexamined; Run 43's "the core commits" may cover it.
7. **No go-back criterion is triggered.** GR is a consistent all-orders theory. No first-order result is lost. No data that option 1 passes is failed by option 3.

**Reading.**
1. **ED's static field equation was GR's all along, for the clock rate.** What made ED's strong field different (no horizon, a 4.6% larger shadow, 0.75–0.8 of GR's maximum mass, the squeeze against nuclear physics) was its rule for space: space tied to the clock, c = N². This is the cleanest statement of what ED changes in static gravity.
2. **Under option 3 (provisional), ED's static gravity is GR's**, and so are its neutron stars and static black holes. ED's own content in classical gravity moves to:
   - the strong-equivalence-principle violation set by the medium's scale (Δ ≈ C p_s/P₀, C ≈ 0.38–0.44 if Run 55's formula carries over);
   - whatever happens where possibility runs low (P ≲ p_s): the cores, and a thin near-horizon shell;
   - the committing cores inside horizons;
   - the arrow of time, and the vacuum that draws nothing.
3. **A reading of option 3 in ED's own terms** (offered, not adopted). Patterns hop on their place's ticks (the factor N) and need free capacity there (the factor 1/ψ²).
   - Option 3 says free capacity is used up by the energy present (the Hamiltonian constraint, sourced by e).
   - The ticking is slowed by what draws (the lapse equation, sourced by e + 3p).
   - ED's original rule took both factors from the clock. At first order the two agree.
4. **What option 3 costs, recorded.**
   - Ruling 2's "the vacuum draws nothing" and the exponential metric hold only at first order.
   - The engine's medium would need possibility to move on curved (sheared) space with a clock linear in P. The logarithmic medium that gave β = 1 (Candidate A′) and the reason for p_s would need re-deriving.
   - None of the registered grounds for going back is triggered.
5. **Going back stays open.** Every run whose ED numbers change is listed above, and their option-1 results remain in the record as they were.
