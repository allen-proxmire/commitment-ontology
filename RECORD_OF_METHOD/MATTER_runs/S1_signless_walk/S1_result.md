# S1 result — a signless spin-½ pattern moves only if its components anticommute

Script `s1_signless_walk.py`, output `s1_result.json`. Adopted walk (palindrome, θ = 0.3, r = 0.3), 200 random zone points. Charge conjugation for this walk is C = iγ² (C α_j* C⁻¹ = α_j, C β* C⁻¹ = −β); the walk is C-symmetric, C U(k)* C⁻¹ = U(−k), to 2 × 10⁻¹⁶.

**Measured.** For the Majorana bilinear kernel C G(k), G = i log U: symmetric part (what commuting components see) **≤ 1.1 × 10⁻¹⁵** at every point; antisymmetric part (what anticommuting components see) between 0.82 and 1.92 at every point.

**Reading.** A signless pattern with the four has, if its components commute, no generator at all: ψᵀ C G ψ vanishes identically, and the pattern does not move. Only anticommuting components give a walk. This is the lattice form of the known fact that the Majorana Lagrangian vanishes for commuting fields. In CO's words: *a pattern that does not move is not a pattern, so a signless pattern with the four must be a fermion to exist.*

**With the first rung.** Signed patterns with the four: fermions, by positivity of the count (the backward branch must be closed). Signless patterns with the four: fermions, by existence (a commuting version does not move). Together, candidate: **every pattern carrying the four is a fermion.** Nothing here speaks to patterns without the four (the photon); that is the next rung.

**Grade.** Candidate (one check per rung; no cold reading yet). Post-run check: the C-symmetry residual at machine precision is the control that the construction is the right one.

**Annotation, same day.** The antisymmetry of C G(k) follows from C-symmetry alone for any Hermitian generator; the measured quantity and the control are one identity, so this was a check, not a test with an unknown outcome. The reading "does not move" applies to the bosonic Fock Hamiltonian, not the first-quantised packet, which moves. Regraded with the record: consistency condition, restating the vanishing Majorana bilinear under commutators.
