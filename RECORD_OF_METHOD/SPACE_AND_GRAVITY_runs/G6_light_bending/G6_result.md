# G6 — light bending on CO's walk (13 Nov 2026)

**Question.** With the field reaching the walk through the Wilson flip as well as the mass flip, does light bend by twice the clock-only amount (Einstein's), and does slow matter still fall at G5's rate with no extra push from the stretch?

**The rule tested** (the author's ruling, candidate, conditional on this run). At each place:
- mass flip θ → θN (the clock rule, as in G5);
- Wilson flip w set by light's local speed: 2 cos w = c₀ N/ψ, with N the lapse and ψ the hop stretch.

On the uniform walk, light's speed is exactly 2 cos w and the rest energy is exactly θ for every w (checked for w from 0 to π/2), so the Wilson flip sets light's speed and nothing else. Since 2 cos w ≤ 2, the rule can slow light freely but speed it up only within the walk's headroom (c₀ = 1.911, about 4.7%).

**Set-up.** A 2D palindromic Wilson walk, U = A_x A_y F(θN) A_y A_x, with A_x = S₊ F(w) S₋ F(−w) hopping in the σ_z basis and A_y the same rotated by R = exp(−iπσ_x/4), so hops along y are in the σ_y basis and the flips stay σ_x. Light's speed is c₀ = 1.9107 along the axis and the diagonal alike. Lattice 640 × 256, field along x: N = 1 − gx, ψ = 1 + gx. Each field is run at +g and −g. The linear response is the odd part, (a(+g) − a(−g))/2; the even part is the field's second order and halves when g halves. Light packets move along y; the slow packet is at rest. Transverse acceleration from a quadratic fit over 150 steps, minus the no-field run.

**Results** (a_x / (g c₀²), odd part; g = 5 × 10⁻⁵, with 2.5 × 10⁻⁵ in brackets).

| packet | clock only | stretch only | clock + stretch | ratio to clock only |
|---|---|---|---|---|
| light, k_y = 0.15, width 40 | 0.921 (0.920) | 0.921 (0.920) | 1.855 (1.843) | 2.013 (2.004) |
| light, k_y = 0.30, width 30 | 0.888 (0.888) | 0.888 (0.888) | 1.776 (1.776) | 2.000 (2.000) |
| matter, θ = 0.4, at rest, width 40 | 0.994 (0.995) | −0.0001 (−0.0001) | 0.993 (0.995) | — |

- **Light:** the clock and the stretch each give half the bending; together, twice the clock-only amount. The absolute value, 0.89–0.92 of the smooth-space value, is the lattice's dispersion at these wavenumbers and the packet's spread of directions; in an earlier pass the lattice's own ray prediction, −(∂ω/∂x)(∂²ω/∂k_x²), matched to 1–4%.
- **Slow matter:** the stretch adds no push at first order, as in GR, where a slow body feels only the lapse. In 1D (g6_1d.py) the pure-stretch push is −0.0013 to −0.0002 of g c₀² and shrinks as the packet widens, the size of the velocity-dependent term carried by the packet's spread.
- **An earlier apparent push of about 3% on matter** came from runs at one sign of g. It is the field's second order, even in g, and is removed by the ±g split.
- **Headroom seen directly:** at g = 10⁻⁴ on the 640-wide lattice, the far side's field asks for light faster than 2 hops per tick, and the rule has no solution there.

**Reading.** On CO's own walk, with the field entering through the mass flip (clock) and the Wilson flip (light's speed), light bends by Einstein's amount, twice the clock-only value, and slow matter falls at Einstein's rate with no stray push from the stretch. Not tested: 3D, a point mass, strong fields, the shift (frame dragging), which this knob cannot carry beyond the headroom.

Grade: reading (the rule's condition met).

Scripts: g6.py (the 2D walk), g6_final.py (the ±g runs; output g6_final.out), g6_1d.py (1D stretch check; output g6_1d.out).
