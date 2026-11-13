# G5 — free fall of CO's walk in a lapse field (13 Nov 2026)

**Question.** Does a pattern on CO's own walk, with gravity entering only through CO's clock rule, fall at Einstein's weak-field rate, and do all masses fall alike?

**Set-up.** One dimension, 6000 places, periodic. The walk is L1b's strictly local palindromic Wilson walk (w = 0.3): A = S₊ F(w) S₋ F(−w), one step U = A F(θN) A, with F(a) = cos a − i sin a σ_x. The field is a lapse N(z) = 1 − gz, entering only as the mass flip θN at each place (the clock rule: a pattern's phase advances as ω(1 − h)). Space is not stretched; hops are unchanged. The packet is built from the uniform walk's positive-energy states, Gaussian in momentum, at rest. Its mean position over 1500 steps is fitted to a parabola.

**Predictions compared.**
- *Einstein (weak field, slow body):* a = g c₀², with c₀ = 1.91067 hops per tick, light's speed on this walk.
- *The lattice's own:* a = −(dE₀/dz)·E″(0), the slope of the rest energy times the inverse inertia, both read from the walk's dispersion.

**Results** (g = 2 × 10⁻⁶; at g = 4 × 10⁻⁶ the acceleration doubles, ratios equal to four digits; with g = 0 the packet does not move).

| θ (rest energy per tick, mc²τ/ħ) | packet width | a / (g c₀²) | a / lattice prediction |
|---|---|---|---|
| 0.1 | 60 / 150 / 300 | 0.966 / 1.004 / 1.010 | 0.956 / 0.993 / 0.999 |
| 0.2 | 60 / 150 / 300 | 1.005 / 1.016 / 1.017 | 0.988 / 0.998 / 1.000 |
| 0.4 | 60 / 150 / 300 | 1.005 / 1.007 / 1.008 | 0.997 / 1.000 / 1.000 |

Narrow packets spread and carry fast parts; as the packet widens the fall converges on the lattice prediction: at width 300 to 1.4 × 10⁻³ (θ = 0.1), 4 × 10⁻⁴ (θ = 0.2) and 1 × 10⁻⁴ (θ = 0.4).

**The lattice prediction against Einstein's** (g5_mass_scan.py, from the dispersion alone). The rest energy is exactly θ. The ratio is

a / (g c₀²) = 1 + 0.154 θ + O(θ²) for small θ (1.00015 at θ = 0.001, 1.0015 at 0.01, 1.012 at 0.1).

The excess is twice the known tree-level speed excess of a massive pattern (MATTER: s ≈ 0.14 mcℓ/ħ, here 0.077 θ = 0.147 mcℓ/ħ, since θ = c₀ · mcℓ/ħ). Exactly, a/(g c₀²) = A(θ)/A(0) = (1 + s)², with A the k² coefficient of E² and s L1b's speed excess; s/θ → 0.077 as θ → 0 (0.147 mcℓ/ħ, L1b's 0.144 being its finite-θ value). It is the same Wilson-term effect seen twice, not a new one: a massive pattern's inertia uses its own limiting speed, slightly above light's.

**Reading.**
- A pattern on CO's own walk falls toward slower clocks at Einstein's weak-field rate g c², linear in the field, with nothing added beyond the clock rule.
- Every mass falls alike up to 2s ≈ 0.15 θ, which vanishes in the continuum limit. At the Crab bound on ℓ (1.3 × 10⁻³¹ m), 2s ≈ 10⁻¹⁹ for an electron and 2 × 10⁻¹⁶ for a nucleon taken whole. How the excess adds up in bound patterns is open. Per elementary pattern it sits far under MICROSCOPE's 10⁻¹⁵. If it scaled with a nucleus's whole mass, titanium and platinum would differ by about 0.29 × 147 m_u cℓ/ħ ≈ 3 × 10⁻¹⁴ at that ℓ, and MICROSCOPE would need ℓ ≲ 5 × 10⁻³³ m, tighter than the Crab.
- Not tested: the stretching of space (light bending needs it), more than one dimension, strong fields.

Grade: reading (a check of the curved walk's lapse part, D).

Scripts: g5_free_fall.py (main run), g5_width.py (width test), g5_lattice_pred.py (packet against the lattice prediction), g5_mass_scan.py (lattice prediction against Einstein's as θ shrinks).
