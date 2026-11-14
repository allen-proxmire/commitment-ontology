# G15 — can the shift carry strong gravity? The drift past light's speed (14 Nov 2026)

**Why.** P7f carries the lapse and stretch through the Wilson flip, which leaves its window near compact masses (Φ ≳ 0.05). In Painlevé–Gullstrand form a non-rotating mass has unit lapse and flat slices, and all its gravity is a drift (the river), v_s = √(2GM/r); the horizon is where the drift reaches light's speed, and inside it the drift exceeds it. With w = 5π/16, light runs at c₀ = 1.111 hops per step while the directed hop's drift reaches 2 sin b ≤ 2 hops per step. So the shift alone, with w fixed, might carry a horizon.

**Set-up.** CO's 1D palindromic walk at w = 5π/16 with G7's directed-hop brickwork at both ends of the step, uniform nudge b. Light packets at k = ±0.1 and a slow packet (θ = 0.3, at rest in momentum), width 40, 300 steps; velocities by circular mean.

**Result** (g15_shift.out).

| b | drift 2 sin b (÷ c₀) | light downstream | light upstream | tilt ÷ drift | light's half-width (c₀ = 1.111) | matter |
|---|---|---|---|---|---|---|
| 0.2 | 0.397 (0.36) | +1.506 | −0.715 | 0.995 | 1.110 | 0.397 |
| 0.4 | 0.779 (0.70) | +1.885 | −0.335 | 0.995 | 1.110 | 0.779 |
| 0.6 | 1.129 (1.02) | +2.233 | +0.015 | 0.996 | 1.109 | 1.129 |
| 0.8 | 1.435 (1.29) | +2.534 | +0.320 | 0.994 | 1.107 | 1.434 |
| 1.0 | 1.683 (1.51) | +2.772 | +0.567 | 0.992 | 1.102 | 1.683 |
| 1.5 | 1.995 (1.80) | +3.026 | +0.861 | 0.974 | 1.083 | 1.994 |

Matter is carried at the drift exactly. Light's cone tilts by the drift to within 0.6% up to 1.5 c₀, keeping its half-width to within 1%. At a drift of c₀ (b ≈ 0.6), light heading upstream stalls: a horizon. Beyond it, upstream light is carried downstream: the inside of a horizon. At w = 0.3 (G7) the same brickwork matched only to about 40% of light's speed, because there light ran at 1.91 against the drift's cap of 2.

**Reading.** At w = 5π/16 the directed hop alone, with the lapse and stretch left at 1 and w fixed, carries a drift to 1.8 times light's speed with light and matter following GR's shift form: a horizon and its inside are within the walk's reach, without the Wilson flip leaving its window. A candidate entry for strong fields wherever spacetime admits unit lapse and flat slices (Painlevé–Gullstrand for non-rotating masses, Doran for rotating ones): an entry for E. Not tested: a radial (non-uniform) drift with its tidal parts, 2D or 3D, a horizon's formation, which spacetimes admit the form. Grade: reading.

Script: g15_shift.py (g15_shift.out).
