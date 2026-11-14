# G14 — the closed loop in 2D, with the stretch (14 Nov 2026)

**Question.** In two dimensions, with one field carrying both the lapse and the stretch, do two patterns that source it and feel it fall toward each other at Newton's 2D rate, only after the field arrives?

**Set-up.** G6's 2D walk at w = 5π/16 (inside the window π/4 < w < 3π/8, w ≠ π/3; c₀ = 1.111). One field per pattern: Φ_tt = c₀²(∇²Φ + κ(ρ − ⟨ρ⟩)), ρ = θ|ψ|², three substeps per tick, κ = 10⁻²; static form Φ = −(κm/2π) ln r. Felt by the other pattern through P7f with N = 1 − Φ and ψ² = 1 + Φ (γ = 1), after removing Φ's spatial mean (a uniform part relabels every clock alike). θ_a = 0.4, θ_b = 0.3, width 60, separation 400, 700 steps; displacements are differences from the no-field run, positions by circular mean. Lattice 1200 × 800, so the field's periodic images cannot arrive within the run.

**Prediction.** For a source switched on at t = 0, the 2D field behind the front has gradient (κm/2πr)/√(1 − (r/c₀t)²); the slow acceleration is c₀² times it, toward the source, integrated with r fixed.

**Result** (g14_pair.out).

| t | dx_a (pred) | dx_b (pred) |
|---|---|---|
| 300 (front at 360) | +0.001 (0) | −0.001 (0) |
| 450 | +0.036 (+0.040) | −0.041 (−0.053) |
| 600 | +0.141 (+0.150) | −0.170 (−0.200) |
| 700 | +0.240 (+0.247) | −0.291 (−0.330) |

Each falls toward the other: 0.97 (a) and 0.88 (b) of the point-pattern prediction at t = 700. The pulls balance to 9%. The shortfall and imbalance are of the size set by the packets' widths (about 60 hops, spreading by 20–25 over the run) across a 1/r gradient that is still settling. Before the front, motion is 1% of the later values, from the packets' near edges.

**Three earlier passes failed, each for a reason now understood.** On a 640-wide lattice at w = 0.3 the patterns moved apart and moved early: the field's periodic image (240 away across the boundary) arrived before the direct field (400 away); light packets spreading at w = 0.3 made it worse. On an 800-wide lattice the second pattern sat exactly midway between the source and its image, and the pull cancelled. Removing the field's uniform part was also needed: it grows everywhere at once and, through the packets' spreading in a periodic box, shifted their measured centres before any signal arrived.

**Reading.** In two dimensions, with the stretch, patterns on CO's walk source a field that evolves on the lattice and acts back: Newton's 2D attraction, to 3–12% (packet size), causal. Limits: 2D, semiclassical (the mean density sources the field), no self-pull, a scalar field carrying lapse and stretch together (no shift, no waves of the tensor kind), weak field. Grade: reading.

Scripts: g14.py (set-up; uses ../G6_light_bending/g6.py at w = 5π/16), g14_pair.py (g14_pair.out).
