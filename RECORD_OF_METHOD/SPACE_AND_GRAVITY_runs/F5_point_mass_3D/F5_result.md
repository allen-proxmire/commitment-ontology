# F5: light past a point mass on the 3D flow step (16 Nov 2026)

Fail conditions in FAIL_CONDITIONS.md, written before the run. Four-component step, 64 × 128 × 64, 1/r field (A = 0.05, r_c = 3), mass 16 places to the side, light k_y = 0.5, width 6, path y = −56 to +56.

| check | run | prediction | outcome |
|---|---|---|---|
| F5a: full ÷ clock-only deflection | 2.0010 | 2 | PASS |
| F5b: deflection size against the packet-averaged rays | clock −1.877 × 10⁻³, full −3.756 × 10⁻³ | Gauss–Hermite (5 points in x, z, k_x, k_y): −1.404, −2.794 × 10⁻³ | FAIL (34% above) |

**Why F5b failed.** The packet's momentum spread (0.12 in k_x against k_y = 0.5) spreads it about ±26 places sideways over the path, so some of it passes the mass on the far side and is deflected the other way; the average is a delicate cancellation, not a smooth function of the start, and 5-point quadrature does not resolve it (a finer, factorised average after the run gives −0.52 and −0.99 × 10⁻³, worse, since the spread does not factorise). The 400-ray Monte Carlo made before the quadrature, −1.74 ± 0.22 and −3.48 ± 0.44 × 10⁻³ (f5_rays_montecarlo_out.txt), agrees with the run within its noise (0.6σ), too coarse to pass or fail a 5% window. The size check was poorly conditioned on a lattice this small; a packet wide enough to stay on one side needs a larger lattice. Not rerun.

**Reading.** In three dimensions, light passing a point mass on the step bends with the stretch at twice the clock-only amount (2.001): Einstein's 4GM/(c²b) against the clock's 2GM/(c²b). The size against the rays is not settled by this run.
