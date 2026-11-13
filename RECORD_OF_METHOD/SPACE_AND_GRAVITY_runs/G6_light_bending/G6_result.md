# G6 — light bending on CO's walk (13 Nov 2026)

**Question.** With the field reaching the walk through the Wilson flip as well as the mass flip, does the walk's light follow the local speed the flip gives it, so that with the route factor's stretch (γ = 1) it bends by Einstein's amount, and does slow matter still fall at G5's rate with no push from the stretch?

**The rule tested** (the author's ruling, candidate, conditional on this run). At each place:
- mass flip θ → θN (the clock rule, as in G5);
- Wilson flip w set by light's local speed: 2 cos w = c₀N/ψ², with N the lapse and ψ² the hop stretch (the route factor; ψ the standard conformal factor, γ_ij = ψ⁴δ_ij).

On the uniform walk, light's long-wavelength speed is exactly 2 cos w (1D, and 2D along the axes and the diagonal) and the rest energy is exactly θ for every w, since at k = 0 the half-shift is F(w)F(−w) = 1. So the Wilson flip sets light's long-wavelength speed and leaves the rest energy unchanged. It also changes the massive dispersion at finite k (the speed excess s: 0.144 at w = 0.3, 0.151 at π/10) and the doublers' masses.

**Set-up.** A 2D palindromic Wilson walk, U = A_x A_y F(θN) A_y A_x, with A_x = S₊ F(w) S₋ F(−w) hopping in the σ_z basis and A_y the same rotated by R = exp(−iπσ_x/4), so hops along y are in the σ_y basis and the flips stay σ_x. Lattice 640 × 256, uniform field along x: N = 1 − gx, ψ² = 1 + gx (γ = 1 to first order). "Clock only" sets N and leaves ψ² = 1; for matter it changes both flips (θN and 2 cos w = c₀N), for light (θ = 0) only the Wilson flip. (In G5 "clock" changed the mass flip alone.) Each field is run at +g and −g; the linear response is the odd part, (a(+g) − a(−g))/2, and the even part is the field's second order. Light packets move along y; the slow packet is at rest. Transverse acceleration from a quadratic fit over 150 steps, minus the no-field run.

**Results** (a_x / (g c₀²), odd part; g = 5 × 10⁻⁵, with 2.5 × 10⁻⁵ in brackets).

| packet | clock only | stretch only | clock + stretch | ratio to clock only |
|---|---|---|---|---|
| light, k_y = 0.15, width 40 | 0.921 (0.920) | 0.921 (0.920) | 1.855 (1.843) | 2.013 (2.004) |
| light, k_y = 0.30, width 30 | 0.888 (0.888) | 0.888 (0.888) | 1.776 (1.776) | 2.000 (2.000) |
| matter, θ = 0.4, at rest, width 40 | 0.994 (0.995) | −0.0001 (−0.0001) | 0.993 (0.995) | — |

The light k_y = 0.15 clock + stretch row is not fully converged in g: its even part goes 0.049 → 0.031 rather than halving, and its odd part moves 0.7%. The other rows' even parts halve with g.

**Light against the lattice's ray prediction** (g6_raypred.py: −(∂ω/∂x)(∂²ω/∂k_x²) at k_x = 0, clock only): 0.997, 0.989, 0.975, 0.898 at k_y = 0.05, 0.1, 0.15, 0.3. Measured: 0.921 at 0.15, 0.888 at 0.3. At k_y = 0.3 the gap is 1% (lattice dispersion); at 0.15 it is 5.5%, mostly the packet's spread of directions (width 40 against k_y = 0.15). The continuum value is approached as kℓ → 0.

**Slow matter in 1D** (g6_1d.py, ±g, odd part, a / (g c₀²)). The pure-stretch push falls by four each time the packet's width doubles (150 → 300 → 600): −0.0074 → −0.0019 → −0.0005 at θ = 0.1, −0.0017 → −0.0004 → −0.0001 at θ = 0.2, −0.0003 → −0.0001 → −0.00002 at θ = 0.4, against the clock's 1.008–1.017. It goes as the square of the packet's velocity spread, the velocity-dependent term, and vanishes for a body at rest.

**How far the flip can speed light up** (g6_doubler_gap.py, 3D walk of L1b). Lowering w below 0.3 speeds light up but narrows the doublers' gap: on a 24³ grid the π-sector gap falls from 0.175 at w = 0.3 to 0.004 at w = 0.26 (+1.2% in light's speed), and L1b finds extra light species at w = 0.2. So the flip can speed light up by at most about 1%, well inside the walk's causal headroom of 4.7%, which only another entry could use. Static fields normalised at infinity only slow light, so they need none. (At g = 10⁻⁴ on the 640-wide lattice the far side asks for N/ψ² > 1 and the rule has no solution; that is an artefact of normalising N = ψ = 1 at the box centre.)

**Reading.**
- The walk's light follows the local speed the Wilson flip sets: its bending matches the lattice ray prediction, approaching the continuum value as kℓ → 0. Light's local speed here is c₀N/ψ², and N and 1/ψ² have equal first-order slopes when γ = 1. So the clock and the stretch each give half and together twice the clock-only value, Einstein's amount, by construction once γ = 1. The run checks that the walk carries γ = 1 correctly; the doubling is not an independent prediction.
- Slow matter at rest falls at G5's rate, and the stretch adds no push at first order, as in GR. This follows from the rest energy being θ for every w; the run checks it.
- A scalar Wilson flip changes light's speed equally in every direction, so it cannot tilt the light cone; the shift (frame dragging) needs another entry.
- Not tested: 3D, a point mass (where the flip varies from place to place, an effect suppressed by ℓ/r and unrun), strong fields.

Grade: reading (the rule's condition met).

Scripts: g6.py (the 2D walk; its run() clips arccos and is not used), g6_final.py (the ±g runs; g6_final.out), g6_raypred.py (ray prediction; g6_raypred.out), g6_1d.py (1D, ±g; g6_1d.out), g6_doubler_gap.py (g6_doubler_gap.out).
