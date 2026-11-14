# B2/B2b result: domain-wall walk (14 Nov 2026)

**Construction.** CO's 2D walk U = A_x A_s F(θ(s)) A_s A_x, w = 5π/16; x physical (momentum k), s an inner ring of 2L places, θ = +0.5 on one half and −0.5 on the other. Chern number of the band above quasienergy 0: −1 for 0 < θ ≲ 1.6 (CO's matter sign), 0 for −1.5 ≲ θ < 0 (scout.py). Each wall carries one one-way mode; the pair moves at c₀ = 2cos w (|E|/k = 1.110 at k = 0.02).

**Mass measure.** m = ½ min over k of the splitting of the two sub-gap levels (one per wall).

**B2 (b2_out.txt).**
- F1, ε = 0: m(L) = 1.58×10⁻², 3.73×10⁻³, 8.11×10⁻⁴, 1.71×10⁻⁴ at L = 8, 12, 16, 20; log-slope −0.378 per place, R² = 0.9997. PASS.
- F2, L = 16, bar m ≤ 0.01ε: worst 1.4×10⁻² ε (at ε = 0.05). FAIL as registered. The bar was mis-set: the undisturbed residual (8.1×10⁻⁴) already exceeds it at ε = 0.05. m did not grow with ε (coherent 6.1, 5.7, 5.3 ×10⁻⁴ at ε = 0.05, 0.1, 0.2).
- Control, plain 1D walk at θ = 0: m = 0.988 ε. Informative.

**B2b (b2b_out.txt), registered after B2's failure.** ε = 0.2, coherent plus 5 random draws, L = 8–24. All six: m keeps falling, log-slope −0.46 to −0.49 per place (R² ≥ 0.989), m(24) = 0.6–1.6 ×10⁻⁵ ≤ 2×10⁻⁴. PASS.

**Reading.** A disturbance that gives the plain walk a mass of 0.99ε leaves the wall mode's mass falling as e^(−αL), α ≈ 0.4–0.5 per place at these settings. The additive mass shift is suppressed exponentially in the inner length; no counter-term is needed. For an electron-sized mass at the Planck grain (θ ≈ 4×10⁻²³), L ≈ 130 at this wall height.

**Not shown here.** x-varying and time-varying disturbances (B2c, B2d); interactions; the 3+1D version (a 4+1D walk with a second-Chern phase); the rule by which a physical mass enters (a direct wall-to-wall coupling).
