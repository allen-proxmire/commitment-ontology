# B2c: registration (14 Nov 2026, before the run)

**Gap closed.** B2/B2b used disturbances uniform along x. This check lets them vary along x and slowly in time.

**Measure (time domain).** A packet of the one-way mode on wall 1 (s = L), centred at k₀ = 0.05 with width 40 places, evolves for T = 300 steps on a 400 × 2L lattice (x ring, s ring). A mass mixes the wall-1 mode with the opposite-moving wall-2 mode (s = 0). ΔP₂ = max over t of the weight within 3 places of wall 2, minus its value at t = 0.

**Cases.** ε = 0.2, w = 5π/16, θ = ±0.5. Each place (x, s) applies exp(−iε_{x,s}(t) n̂_{x,s}·σ) after each step, n = (1,1,1) + unit Gaussian, drawn per place (seed 5).
- (a) static: ε_{x,s} = ε.
- (b) slowly varying: ε_{x,s}(t) = ε cos(Ωt + φ_{x,s}), Ω = 0.05, random φ. Ω is below the bulk gap (≈ 0.5), so this is a slow disturbance, not heating. Fast random kicks would heat the bulk; that is a different question (absorption, not mass) and is not tested.
- (c) control: no disturbance, but a direct mixing of the wall-1 and wall-2 rows of strength ε (a deliberate mass).

L = 8, 12, 16.

**Fail conditions.**
- F1: (a) or (b) gives ΔP₂(L = 16) > 10⁻³.
- F2: (a) or (b) gives ΔP₂(16) > ΔP₂(8)/10 (no fall with L).
- Uninformative: (c) gives ΔP₂(16) < 0.1.
