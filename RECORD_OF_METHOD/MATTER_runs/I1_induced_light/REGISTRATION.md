# I1: induced light from CO's walk, first rung: registration (14 Nov 2026, before the run)

**Reading.** Light is not a separate rule: the which-way phase's cost is induced by matter's transit (induced gauge theory, Zeldovich 1967, Sakharov 1967; the tuning-3 reading in OPEN_DIRECTIONS_notes/tuning_map.md). Its first consequence: induced light's long-wavelength speed is set by matter's loops. If it equals matter's light speed c₀ = 2cos w, the light–matter speed equality comes with the reading (for one species; with several, a coupling-weighted average). If not, induced light starts with a speed mismatch of its own.

**Setup.** CO's 3D walk (L1b form: four components, hops along the α_j eigen-directions, flip β), w = 5π/16. The walk's vacuum: every state with quasienergy in (−π, 0) filled (ruled, candidate). x a ring of Nx = 64 places; y, z momenta on a 24 × 24 grid (convergence checked at 32 × 32 for one point). Checked against the momentum-space vacuum energy (agreement 10⁻¹⁴); the π-gap stays ≥ 0.5 at θ = 0.3.

**Measure.** Vacuum energy per place ε under (B) a y-link phase A_y = a cos(qx) (a static magnetic field) and (E) a scalar potential V = a cos(qx) (phase per step, split palindromically). C(q) = Δε/a² (Richardson over a = 0.05, 0.1). q = 2πn/64, n = 1–5. Fit C = c₂q̂² + c₄q̂⁴ + c₆q̂⁶, q̂ = 2 sin(q/2). With the induced action ½Z_E E² − ½Z_B B², static energies are −Z_E E²/2 and +Z_B B²/2, so c₂^B/c₂^E = −Z_B/Z_E and **c_ind = √(Z_B/Z_E)** hops per step.

**Masses.** θ = 0.3, 0.5, 0.8 (q ≪ θ is not reached at θ = 0.3; the fit extrapolates).

**Outcomes (stated first).**
- Equal: |c_ind/c₀ − 1| < 1% at all three masses.
- Unequal: otherwise; the size and trend with mass reported. A leading-log argument expects the deviation to shrink like 1/ln(1/θ) as θ → 0 (the log comes from momenta where the walk is Lorentz-invariant at c₀; the finite part is lattice-dependent).
- Invalid: C_B and C_E have the same sign, or the fit residual exceeds 1%.

**Also reported, not tested.** Z_E (its size against the 1/α estimate); the static q⁴ coefficients c₄/c₂ for B and E. These are only part of light's bending c₂: the frequency-dependent terms are not computed here.
