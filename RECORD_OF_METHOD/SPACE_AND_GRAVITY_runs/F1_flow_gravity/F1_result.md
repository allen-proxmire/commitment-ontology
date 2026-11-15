# F1: gravity's key cases on the flow step (15 Nov 2026)

Flow step U = exp(−iτH), τ = 0.4, r = 0.5 (the author's rulings), field entering by P7f restated: H = ½{N/ψ², K} + σ_z mN. Flow units (light speed 1).

| run | case | prediction | result | outcome |
|---|---|---|---|---|
| F1a | free fall, 1D, N = 1 − gx, ψ² = 1 + gx | a = g(1 + rm) | 0.9997 (m = 0.25), 0.9999 (m = 0.5) of prediction at width 300; a/g changes by 4×10⁻⁶ when g doubles | PASS (after a packet-gauge bug, recorded) |
| F1b | light bending, 2D, k = (0, 0.3) | a_x = 2g·ωω_xx (ωω_xx = 1.011) | a_x = 1.995 g, 0.986 of prediction | PASS |
| F1c | closed loop, 1D, two patterns each sourcing a lapse by a wave equation | no pull before the front; a = κm_other/2·(1 + rm) after; balance +0.056 | before: 0.02 of prediction; after: 0.993, 0.991; balance +0.057 | PASS |

Free fall carries the speed-excess factor (1 + s)² = 1 + rm, as on the palindrome. Light bends at twice the Newtonian rate. In one run, patterns source a field that crosses between them at light's speed and acts back with Newton's mutual attraction. The palindrome's G5, G6 and G13 results carry to the flow step.
