# B5: charged matter on the walls in a magnetic field, 4+1-dimensional step (16 Nov 2026)

Fail conditions in FAIL_CONDITIONS.md, written before the run. B4's set-up (inner ring 28 places, walls ±0.5, r = ½, free fermions) with a uniform magnetic field along z through the which-way phase (Landau gauge, one flux quantum per 120-place period, qB = 2π/120), exact at each (k_y, k_z).

| check | result | outcome |
|---|---|---|
| B5a | lowest Landau level one-way along the field on each wall: E/k_z = +0.9997 for the γ₅ = −1 wall, −0.9997 for the γ₅ = +1 wall, at k_y = 0 and 0.7 | PASS |
| B5b | next level at 0.3190 against √(2qB) = 0.3236 (−1.4%) | PASS |
| B5c | below half the first level exactly two states (one per wall) at every k_y and k_z tried | PASS |

**Reading.** The wall-bound fermions carry charge as ordinary particles do: in a magnetic field each wall's fermion has its lowest level moving one way along the field, opposite on the two walls, set by handedness (the chiral Landau level, the setting of the chiral anomaly), with Landau levels at the continuum spacing and no extra light states. Vector-like charge (both walls alike), free fermions, static field.
