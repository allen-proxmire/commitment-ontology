# R8 — Does a relational (disordered) lattice remove the Dirac doublers?

**Question.** On the cubic lattice the Dirac identification carries extra low-energy species. Translation invariance is a premise of Nielsen–Ninomiya. CO's lattice is relational, with no translation invariance. Does the disorder remove the extra species?

**Model.** Hermitian nearest-neighbour Dirac operator H = Σ_⟨ij⟩ (−i w_ij α·ê_ij |i⟩⟨j| + h.c.), massless, on (a) the periodic cubic lattice (naive fermions; known: 8 species) and (b) a periodic random point set with Delaunay adjacency (Christ–Friedberg–Lee lattice). Hop weights normalised per site so the continuum coefficient tensor T_i = Σ_j w_ij ℓ_ij ê_ij ê_ijᵀ has trace 3 (c = 1) on average. Same site count for both. The Hamiltonian form is used because the species count is a property of the lattice, not of the time-stepping; the automaton's own extra modes are a separate matter.

**Measured quantity.** Low-energy density of states ρ(E) = A·E² for |E| < E_c. For a single massless Dirac species in volume V, A = V/(π²c³) (two signs, two helicities). Species count n = A_measured / A_single. Expected n_cubic = 8 (calibration). n_random is the result.

**Outcome unknown.** If n_random ≈ 1: the relational lattice removes doublers; the identification should be remade on it (ruling: relational lattice *needed* for the matter sector). If n_random ≈ 8, or ρ(E) has no clean E² regime: disorder does not remove them; doublers stay open.

**One check post-run:** the cubic calibration must give n ≈ 8 with the same normalisation, or the measurement is not trusted.
