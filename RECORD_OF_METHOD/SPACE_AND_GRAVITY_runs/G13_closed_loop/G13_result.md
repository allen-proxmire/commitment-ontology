# G13 — the closed loop, first toy: patterns source the field, the field evolves, the field acts back (14 Nov 2026)

**Question.** In one run with nothing set by hand but the coupling and the field's speed (set to the walk's, the tuning question): do two patterns on CO's walk, each sourcing a field that evolves on the lattice, pull on each other with Newton's law, equal and opposite, only after the field has had time to cross between them?

**Set-up.** CO's 1D palindromic walk (w = 0.3). Two patterns of rest energy θ_a, θ_b per tick, at rest, separation 2D. Each sources its own lapse field from its rest-energy density ρ = θ|ψ|² by a wave equation at the walk's light speed (CO's linear cost, reduced to the lapse in one dimension):

h_tt = c₀²(h_xx + κ(ρ − ⟨ρ⟩)), N = 1 − h,

stepped four times per tick. Each pattern feels the other's field through P7f (mass flip θN, Wilson flip 2 cos w = c₀N); no pattern feels its own (no self-pull). κ = 1.4 × 10⁻⁵. The fields start at zero.

**Predictions.** Before the field front arrives (t < 2D/c₀): no acceleration. After it: in one dimension the field's slope behind the front is the static one, so a_b = −c₀²κθ_a/2 and a_a = +c₀²κθ_b/2: each falls toward the other, θ_a a_a + θ_b a_b = 0. The walk's own factor (1 + s)² (G5) is 1.008 at θ = 0.4 and 1.017 at θ = 0.2.

**Result** (g13_runs.out).

| θ_a / θ_b | separation | width | before the front: a/prediction | after: a_a, a_b ÷ prediction | (θ_a a_a + θ_b a_b)/(θ_a|a_a|) |
|---|---|---|---|---|---|
| 0.4 / 0.2 | 1200 | 250 | 0.002, 0.002 | 1.010, 1.017 | −0.007 |
| 0.4 / 0.2 | 600 | 100 | 0.000, 0.000 | 0.91, 0.89 | +0.024 |
| 0.8 / 0.4 | 1200 | 250 | 0.001, 0.002 | 0.90, 1.01 | −0.12 |

- **First row (the clean case):** nothing moves until the field arrives; then each pattern falls toward the other at the predicted rate, including the walk's own factor (1.010 against 1.008, 1.017 against 1.017), and the pulls balance as the two (1 + s)² factors require ((1.008 − 1.017)/1.008 = −0.009 predicted, −0.007 found).
- **Second row:** in the 3000-place ring each field returns round the boundary after (L − 2D)/c₀ = 1256 ticks, inside the fit window; rerun at L = 9000 (cold read) it gives 1.010 and 1.007.
- **Third row:** θ = 0.8 is above 2w = 0.6, where the walk's rest band meets an extra species' band; a pattern that heavy is outside the walk's clean range.

**Reading.** In one run, patterns on CO's walk source a field on the lattice, the field crosses between them at light's speed, and acts back: Newton's mutual attraction, equal and opposite, with the walk's own G5 factor, and nothing before the field arrives. A first closed loop. Limits: one dimension (the lapse alone; GR has no field dynamics of its own in 1D, so this is CO's linear cost reduced to a scalar), semiclassical (the mean density sources the field), no self-pull by construction, weak field, no stretch or shift. Grade: reading.

Scripts: g13_loop.py, g13_runs.py (g13_runs.out).
