# G8 — light passing a point mass on CO's walk (13 Nov 2026)

**Question.** In a 1/r field, with the field entering by P7f (mass flip θN, Wilson flip 2 cos w = c₀N/ψ²), does light passing a mass bend by Einstein's 4GM/(c²b), twice the clock-only value?

**Set-up.** G6's 2D walk, light only (θ = 0). The plane is a slice through the mass, so a ray in it stays in it and its deflection is the 3D one. Field: Φ = A/√(r² + r_c²) with A = 0.6 and r_c = 5 hops; N = 1 − Φ; ψ² = 1 + Φ (γ = 1) or ψ² = 1 (clock only). Lattice 512 × 1024. A packet with k_y = 0.5 and width 40 starts at y = −440, impact parameter b = 120, and runs 475 steps to y ≈ +440. The deflection is the change in mean k_x (FFT, insensitive to wrap) over k_y, minus the no-field run. The packet passes once on each side of the mass and the two are averaged; they differ by 2%, the 2D walk's sideways drift.

**Predictions.**
- Continuum, over the finite path: θ_full = (4A/b)·½(|y₀|/√(y₀² + b²) + y₁/√(y₁² + b²)) = 0.01929; clock only half.
- The lattice ray through the packet's centre (g8_ray.py, Hamilton's equations on the walk's own dispersion with the local flips): clock 0.009855, full 0.01971 (1.022 of continuum).
- The lattice ray averaged over the packet's spread of starting positions and directions (g8_rayavg.py, 150 rays): clock 0.0113 ± 0.0004, full 0.0227 ± 0.0009. A packet of width 40 at b = 120 samples rays nearer the mass, and ⟨1/b⟩ exceeds 1/⟨b⟩.

**Result** (g8_run.out).

| | clock only | clock + stretch | ratio |
|---|---|---|---|
| measured (mean of both sides) | 0.01081 | 0.02167 | 2.004 |
| / continuum | 1.121 | 1.123 | |
| / packet-averaged lattice ray | 0.95 ± 0.04 | 0.95 ± 0.04 | |

**Reading.** Light passing a point mass on CO's walk bends twice as much with the stretch as with the clock alone (2.004), Einstein's 4GM/(c²b) against Newton's 2GM/(c²b). Its size agrees with the walk's own ray prediction over the packet to 5%, within the ray average's sampling error, and lies 12% above the single-ray continuum value because of the packet's width. As in G6, the doubling follows once γ = 1 is carried by the walk; the run checks that it is carried in a non-uniform field. Not tested: matter's orbits, 3D, strong fields, the shift (a spinning mass). An earlier pass (k_y = 0.3, width 20, b = 80) spread so far sideways that the packet wrapped the box and sampled the core; it gave ratio 2.0007 and size 1.15 of continuum, and was replaced by this one.

Grade: reading.

Scripts: g8.py (set-up; uses ../G6_light_bending/g6.py), g8_run.py (g8_run.out), g8_ray.py (g8_ray.out), g8_rayavg.py (g8_rayavg.out).
