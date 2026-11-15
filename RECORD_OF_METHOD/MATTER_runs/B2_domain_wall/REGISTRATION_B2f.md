# B2f: registration (14 Nov 2026, before the run)

**Reading under test.** The two walls' speeds (the two handednesses of the light species) are set locally at each wall, so a disturbance that differs between the walls makes them unequal by an amount that does not fall with the inner length L. If so, the speed counter-terms of tuning 1 are needed per handedness.

**Second question (same run).** For disturbances the same at every inner place (coherent, any direction n̂₀), are the two speeds equal to rounding? If so, a symmetry exchanges the walls, and a loop correction respecting it would not split them.

**Measure.** Strip (x-uniform, k exact), w = 5π/16, θ = ±0.5. Find the crossing k*. At k* + 0.04 and k* + 0.12, take the two sub-gap levels, assign each to the wall holding most of its weight, v_i = |ΔE_i|/0.08.

**Cases.** P_s = exp(−iε n̂_s·σ). Coherent: n̂₀ = (1,1,1), (1,0,0), (0,1,0), (0,0,1), uniform in s. Random: n_s = (1,1,1) + unit Gaussian per s, 5 draws (seed 21). ε = 0.05, 0.1, 0.2. L = 8, 16, 24.

**Outcomes (stated first).**
- Not protected: at ε = 0.2, median |v₁ − v₂| over the random draws at L = 24 ≥ ½ of that at L = 8.
- Protected: that ratio ≤ 1/10.
- Otherwise inconclusive.
- Symmetry: each coherent case has |v₁ − v₂| < 10⁻⁶ at every ε and L, or not.
