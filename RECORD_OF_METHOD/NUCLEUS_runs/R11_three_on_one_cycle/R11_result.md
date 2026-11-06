# R11 result — three on one cycle: the three-fold charge arises; the sectors differ in mass; all propagate; no confinement from this alone

Script `r11_three_on_one_cycle.py`, output `r11_result.json`. θ = 0.3; shared flip M = exp(−iθ β ⊗ (S + S†)/2).

- **Symmetry (known by construction, confirmed):** the thirds-shift commutes with the step to 1.4 × 10⁻¹⁶. Its eigenvalues ω^k define a Z₃ charge: triality.
- **Sectors (the unknown):**

| triality | mass angle at rest | dispersion |
|---|---|---|
| 0 | 0.300 (= θ) | Dirac, √(θ² + (2q)²) |
| 1 | 0.150 (= θ/2, sign flipped) | Dirac, mass θ/2 |
| 2 | 0.150 | same as 1 |

All three sectors propagate as free Dirac species. The triality-zero sector (the three in step, the "baryon-like" sector) carries the full flip; the triality-one and -two sectors (one copy out of step with the cycle) carry half, with reversed sign. Nothing fails to propagate.

**Reading.** The sharing gives a three-fold charge that arises rather than being posited, and it is the centre of colour's charge. It also gives a dynamical difference between sectors, a mass splitting (θ vs −θ/2), from the one ruling-shaped choice (the flip passes around the cycle). It gives no confinement: an out-of-step copy is lighter, not trapped. So the moiré shape supplies the three and the centre, and a cost for being out of step that is a mass, not a wall.

**Rulings.** None changed. Shape upgraded to: candidate for the origin of the three (as a consequence of three copies on one cycle), with the shared-flip coupling flagged as the one choice; confinement not from this. The continuous matching (the eight gluons) remains the missing column.

**Cold reading, same day; excluded as a route to the three.** The symmetry of the step is U(1) × U(2) (the commutant of T), of which S₃ and the cyclic Z₃ are subgroups; the Z₃ was inserted by writing T. The "triality" identification is wrong: the centre of SU(3) acts by a scalar phase, so every colour of a quark has triality 1; the cyclic permutation S is non-central, conjugate to diag(1, ω, ω²), and its three eigenstates are the three colours of one fundamental, not three trialities; a one-particle state in C³ cannot be a singlet. The model is exactly three decoupled Dirac walks with masses θ·spec(T) = θ(1, −½, −½): a three-flavour free theory with the S₃-symmetric circulant mass texture (Harari–Haut–Weyers 1978; Fritzsch–Plankl 1990), nothing to do with colour. The sign of the sector masses is unobservable (ψ → γ⁵ψ) and was not measured: `eff_mass_angle` in the json is a formula, not a result. n copies give Z_n with masses θ cos(2πk/n) for every n (checked n = 2, 4, 5 by the reader), so the three was an input. "A sector fails to propagate" is not a confinement criterion; confinement is an interacting multi-particle statement (area law). Carried forward, negative and useful: any shared flip exp(−iθ β⊗X) is simultaneously diagonalisable with flavour-blind hops, so no shared cycle of this form can give colour, self-coupling or confinement; a route to the three needs a position-dependent, non-commuting internal coupling, a gauge field, which the inventory lacks.
