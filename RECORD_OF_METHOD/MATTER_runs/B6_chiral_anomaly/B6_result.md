# B6: the chiral anomaly on the walls, by spectral flow (16 Nov 2026)

Fail conditions in FAIL_CONDITIONS.md, written before the run. B5's set-up; k_z swept over the whole zone (64 points, offset from zero) at k_y = 0 and 0.7; states below |E| = 0.15 (under half the first Landau level and the bulk gap) sorted by wall.

| check | result | outcome |
|---|---|---|
| B6a | each wall's lowest level crosses zero exactly once in the whole zone, at k_z = 0: on one wall upward, on the other downward (the γ₅ = −1 branch rising, the γ₅ = +1 branch falling, as in B5), at both k_y | PASS |
| B6b | no other state below |E| = 0.15 anywhere in the zone (no crossing near k_z = π) | PASS |

**Reading.** Each wall carries exactly one chiral crossing, with opposite directions on the two walls and nothing else at low energy. An electric field along the magnetic one then moves charge from one wall to the other through the inner ring at (qE/2π) per guiding centre per unit time, (q²/4π²)E·B per unit volume on each wall, opposite in sign, the total kept: the chiral anomaly with coefficient 1 per Weyl fermion, its non-conservation on each wall balanced by flow through the ring (anomaly inflow). Free fermions, static fields; the k_z grid is coarse (spacing 0.098, four points per wall below the cut), enough to count crossings, not to resolve the residual gap at k_z = 0 (about 10⁻³ at L = 14). Which handedness sits on which wall depends on the inner direction's orientation (B4 and B5 use opposite orientations); the docs state only that the walls are opposite.
