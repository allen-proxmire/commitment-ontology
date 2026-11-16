# G16 — a black hole on CO's walk, in Painlevé–Gullstrand form (14 Nov 2026)

**Rule tested.** E's strong-field entry (ruled, candidate): gravity as the shift alone, lapse and stretch at 1, w = 5π/16 fixed. A non-rotating mass in Painlevé–Gullstrand form: the drift v(r) = √(2GM/r) inward, carried by directed hops on both axes (drift 2 sin b per axis, nudge set by the drift's component at each link's midpoint). Horizon at r_s = 2GM/c₀² = 40 hops (c₀ = 1.111). The drift is softened at the centre (r → √(r² + 4²)) and capped at 1.9 hops per step (inside r ≈ 14).

**Fail conditions, stated first.** Zero-momentum packets (the form's free-fallers, from rest far away) not following dr/dt = −v(r), through the horizon; light sent outward not escaping from outside r_s, or not swept in from inside it.

**Result** (g16.out; lattice 420 × 420; positions of the packets' centres on the x axis).

| packet | r at t = 0, 25/50, 50/100, 100/150 | free-faller or ray |
|---|---|---|
| matter (θ = 0.5, width 12), from 150 | 150, 119.8 (t = 50), 85.0 (100), 42.1 (150) | 150, 119.8, 85.1, 40.9 |
| matter, from 110 | 110, 73.4 (50), 25.5 (100) | 110, 73.4, 22.6 |
| light outward (k = 0.4, width 10), from 70 | 69.9, 77.5 (25), 85.4 (50), 102.3 (100) | 70, 76.9, 84.8, 103.2 |
| light outward, from 50 (just outside r_s) | 49.9, 53.4, 55.9, 58.6 | 50, 53.0, 56.7, 66.7 |
| light outward, from 32 (inside r_s) | 31.9, 26.7, 17.5, 4.1 | 32, 27.8, 20.4, 2.8 |

**Reading.** Passed. Zero-momentum packets fall as the form's free-fallers to within 0.1 hop far out, and through the horizon; light sent outward escapes from outside the horizon, at the rate the ray gives far out, and is swept inward from inside it. Near the horizon and the softened centre the packets (10–12 hops wide) straddle regions of very different drift, and their centres lag the single ray (light from 50: 58.6 against 66.7; matter near r ≈ 25: 25.5 against 22.6). With the drift alone and w fixed, CO's walk carries a black hole's horizon and interior, the tidal stretching coming from the drift's variation. Not tested: 3D, a rotating hole (Doran form), the hole's formation from matter (here the drift is given, not sourced), the centre. Grade: reading.

Scripts: g16.py (g16.out; uses ../G12_rotation_and_gradient/g12.py and ../G6_light_bending/g6.py at w = 5π/16).
