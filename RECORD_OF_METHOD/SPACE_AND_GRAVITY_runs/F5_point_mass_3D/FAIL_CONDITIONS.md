# F5: light past a point mass on the 3D flow step — fail conditions (16 Nov 2026, before the run)

Four-component step on a 64 × 128 × 64 lattice, τ = 0.4, r = 0.5. A 1/r field Φ = A/√(ρ² + r_c²), A = 0.05, r_c = 3, the mass 16 places to the side of the light's line; N = 1 − Φ, ψ² = 1 + Φ (full) or ψ = 1 (clock only). Light packet k_y = 0.5, width 6, from y = −56 to about +56. Deflection: change in mean k_x over k_y, minus the no-field run. Prediction: rays on the step's own dispersion, E = √(D²Σsin²k + (D·r Σ(1 − cos k))²), D = N/ψ², averaged over the packet's spread of positions and momenta (Gauss–Hermite, 5 points each in x, z, k_x, k_y), computed before the run (f5_rays.py; a 400-ray Monte Carlo was too noisy, ±13%, and was replaced before the run).

| check | fail if |
|---|---|
| F5a: full ÷ clock-only deflection = 2 (Einstein's 4GM/(c²b) against the clock's 2GM/(c²b)) | off by > 0.05 |
| F5b: each deflection against the packet-averaged rays | off by > 5% |
