# F4: free fall and light bending on the 3D flow step (16 Nov 2026)

Four-component step on a 64³ lattice, τ = 0.4, r = 0.5, field by P7f restated (N = 1 − g n̂·x, ψ² = 1 + g n̂·x, g = 2 × 10⁻⁴), packets of width 6, acceleration from a quadratic fit of the mean position over flow time 16, odd part in g. Fail conditions in FAIL_CONDITIONS.md, written before the run.

| check | run | point-packet prediction | packet-averaged rays (after the run) |
|---|---|---|---|
| m = 0.25, fall along an axis | 1.9455 × 10⁻⁴ | g(1 + rm) = 2.25 × 10⁻⁴ | 1.933 × 10⁻⁴ (run +0.6%) |
| m = 0.25, fall along a body diagonal | 1.9455 × 10⁻⁴ | 2.25 × 10⁻⁴ | 1.906 × 10⁻⁴ (+2.1%) |
| m = 0.5, axis | 2.3131 × 10⁻⁴ | 2.50 × 10⁻⁴ | 2.319 × 10⁻⁴ (−0.3%) |
| m = 0.5, body diagonal | 2.3131 × 10⁻⁴ | 2.50 × 10⁻⁴ | 2.310 × 10⁻⁴ (+0.1%) |
| light, k_y = 0.3: stretch ÷ clock only | 2.0000 | 2 | 2.0000 |
| light, size with the stretch | 3.024 × 10⁻⁴ | 2gωω_xx = 4.04 × 10⁻⁴ | 3.065 × 10⁻⁴ (−1.3%) |

**Outcome: FAIL as stated.** The registered predictions were for a point packet, and f4_run.py compared with the wrong sign (clocks run slow toward +n̂, so patterns fall that way; F1a's convention). A packet 6 places wide carries a momentum spread of about 0.12, comparable to the masses and to light's k, which lowers the mean acceleration by 7–25%; on the 64³ lattice a wider packet does not fit. The packet-averaged ray prediction on the step's own dispersion (f4_rays.py, 400 rays, computed after the run) matches the run to 0.1–2.1% (ray sampling noise about 1.4%: the rays' axis and body-diagonal values differ by that much, where the cube symmetry makes them equal). Not rerun.

**Reading.** In three dimensions on the step: free fall is the same along an axis and along a body diagonal to 10⁻⁵ (the cube symmetry), at the rate the step's rays give, within their sampling noise; light bends at exactly twice the clock-only rate (2.0000). Three dimensions, weak uniform field; a 1/r field, the closed loop and strong fields in 3D not run.
