# R8 result — a random lattice does not remove the doublers; it replaces them with worse

Run: `r8_relational_doublers.py`, 1331 sites each, massless, hop weights normalised so c = 1 on average. Output `r8_result.json`, `r8_dos.png`.

**Post-run check (passed).** Cubic naive calibration: species count 8.9 (expected 8; finite-size). The measurement is trusted.

**Random Delaunay lattice.** No E² regime at all. The density of states is a broad peak centred at E = 0 (2892 of 5324 modes inside |E| < 0.5; a nominal "species count" of 246 at E_c = 0.5, 759 at E_c = 0.3, rising as E_c → 0). The cubic lattice has eight Dirac cones; the random lattice has a continuum of low-energy modes with no cone structure, as Perantonis and Wheater found for random-lattice fermions after Christ, Friedberg and Lee proposed them.

**Reading.** Translation invariance is a premise of Nielsen–Ninomiya, and removing it does void the theorem, but what replaces the eight doublers is not one species. A naive nearest-neighbour Dirac operator on a disordered graph has a large density of near-zero modes. The relational lattice, by itself, is not the escape.

**Ruling.** Candidate "relational lattice removes doublers": **excluded** in this form. The doubler problem in the matter sector stays open. Any escape has to add structure (a Wilson-type term, which costs unitarity or chirality; or a specific unitary walk family, which is a ruling choice; or an account of the extra modes).

**Scope.** Hamiltonian nearest-neighbour operator, one disorder sample, 11³ sites. The automaton's own eight γ⁵ modes were not tested here; this run is about the lattice property.
