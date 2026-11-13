# E1 — does a Regge cost on CO's lattice reduce to G1's linear cost? (13 Nov 2026)

**Question.** E's candidate for gravity's full (nonlinear) cost is Regge's: Σ over hinges of area × deficit angle. At weak field it must reduce to G1's forced linear cost, linearised Einstein–Hilbert (Fierz–Pauli), isotropic and gauge-invariant.

**Fail condition, stated before the run.** The ratio of the Regge cost's quadratic part to Fierz–Pauli's not one constant across polarisations and directions as kℓ → 0, or relabelling (gauge) modes costing at order k².

**Set-up.** Euclidean 4D hypercubic lattice. CO's cells are not flat in general (each relation carries its own length, so opposite edges of a cell differ), so each 4-cube is cut into 24 flat 4-simplices, one per ordering of the axes (the Kuhn cut). Edge lengths come from a metric at each edge's midpoint, l² = Δ·g·Δ: along the axes from the relations' displacements, on face diagonals from the squares' shear, and on the longer diagonals from the same metric. Hinges are the simplices' triangles. Cost S = Σ_t A_t(2π − Σ θ_t), dihedral angles from each simplex's Gram matrix. Field: g = 1 + ε e cos(k·x), random symmetric polarisations e, directions n = (1,0,0,0), (1,1,0,0), (1,1,1,0), (1,2,0,0), k = 2πn/L; the quadratic part from ±ε (ε = 10⁻⁴). Fierz–Pauli in the same variables: Q = ½k²(e:e) − |e·k|² + (k·e·k) tr e − ½k² (tr e)².

**Result** (e1_regge.out; S₂/Q per cube, 12 polarisation–direction pairs per L):

| L | mean | spread across pairs | gauge modes, S₂/(k²|ξ|²) per cube |
|---|---|---|---|
| 16 | −0.2442 | 3.3% | ≤ 2 × 10⁻³ |
| 32 | −0.2483 | 1.3% | ≤ 8 × 10⁻⁵ |
| 64 | −0.2501 | 0.4% | ≤ 9 × 10⁻⁵ |

The ratio tends to −¼ (the Euclidean linearised √g R in these units) with a spread falling about fourfold per halving of kℓ, as (kℓ)²; gauge modes cost nothing to the precision of the second difference.

**Reading.** Passed. On CO's lattice, a Regge cost reduces at weak field to linearised Einstein–Hilbert, isotropic and gauge-invariant, with lattice corrections of order (kℓ)². This agrees with Roček and Williams (1981) for the same cut. Two choices made here are not yet in CO's rules: the cut of each cell into simplices (with triangles as hinges, not the squares), and the lengths of the cells' longer diagonals, set here by the same metric. Not checked: Lorentzian signature (deficits as boost angles), the nonlinear regime, the broken-symmetry estimate (ℓ²R)². Grade: reading.

Script: e1_regge.py.
