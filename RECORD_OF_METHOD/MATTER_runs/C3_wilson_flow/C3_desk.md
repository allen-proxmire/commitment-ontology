# C3: the step as a one-tick flow of the cubic Wilson–Dirac Hamiltonian (desk, 15 Nov 2026)

**Why.** Tuning 4 traces to the palindrome's nesting order. Cycling the order (no gap), choosing it by sublattice (not unitary) and the body-centred-cubic automaton (doubled, first-order Lorentz violation) all fail. A literature search finds no strictly local, cube-symmetric, gapped Dirac walk with one light species (Bialynicki-Birula 1994 and Bisio–D'Ariano–Perinotti build theirs on body-centred-cubic neighbourhoods; Meyer's no-go forces partitioning for strictly local homogeneous automata).

**Candidate.** Drop strict locality to fast-fading reach, which the ruling of 12 Nov 2026 allows: the step is the flow, for one tick τ, of the standard cube-symmetric Wilson–Dirac Hamiltonian,
U = exp(−iτ H_W),  H_W(k) = Σ_j α_j sin k_j + β (m + r Σ_j (1 − cos k_j)).
H_W is nearest-neighbour; U reaches every distance, with amplitudes falling faster than exponentially (Bessel-like).

**Checks (c3_desk.py, c3_desk_out.txt; τ = 0.4, r = 1, τm = 0.03).**
- *One light species:* the smallest quasienergy over the zone is 0.03 (at k = 0, the mass); the extra species sit at 0.83, 1.63, 2.43 (one, two, three components at π: Wilson masses τ·2r per component).
- *Gaps:* 0-gap only at the light species; π-gap 0.71 (τ times the bandwidth 6.08 is 2.43 < π). A smaller τ moves every species further from π (relevant to the wrong-sign induced field seen when species sit near π).
- *Cube symmetry, as an operator identity:* R U(k) R† = U(Pk) for the cyclic axis permutation P, with R the 120° spinor rotation about (1,1,1), to 6×10⁻¹⁶; together with the half-turns about the axes this is the tetrahedral group, under which every two-index response (permittivity, permeability, speed tensors) is isotropic. Tuning 4 would vanish by symmetry.
- *Reach:* amplitude norms 1.85, 0.54, 1.6×10⁻², 1.4×10⁻⁴, 5.6×10⁻⁷, 1.3×10⁻⁹ at 0–5 places along an axis.
- *Light speed:* 0.400 places per tick (= τ), the same in every direction at low energy.

**What it changes.** CO's step would no longer be a sequence of hops but one tick of a nearest-neighbour flow. The continuum physics is the same Dirac field; the lattice-scale structure differs, so walk-specific numbers (the speed excess s = ½ sin w·mcℓ/ħ, the Wilson window in w, the quadratic terms behind the photon-splitting coefficients, P7f's Wilson-flip rule for the field) would be redone for H_W (here the Wilson parameter r plays w's role; the speed excess for H_W is about ½ r m). The domain-wall construction for tuning 2 is native to Wilson–Dirac Hamiltonians (Kaplan's original). Tuning 1's time-versus-space part is untouched.

**Status.** Shape, for the ruling: the step as a one-tick Wilson–Dirac flow. Checks before any ruling: the induced-light response (isotropy by symmetry, the sign at small mass, and the π-gap's effect) and how the field enters (P7f restated).
