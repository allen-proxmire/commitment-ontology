# I2: induced light at small masses: registration (14 Nov 2026, before the run)

**Why.** I1 found both induced coefficients negative at θ = 0.3–0.5, where the light species' leading log (ln(1/θ) ≈ 1) cannot dominate. I1's real-space method cannot reach q ≪ θ ≪ 1.

**Method.** The same quantity (O(a²) vacuum-energy response, vacuum as ruled), computed exactly at second order: perturbation theory of the walk's unitary on momentum pairs (k, k+q), with the field's second-order diagonal part split evenly between the two pairs containing each k. Validated against I1 at θ = 0.3, q = 2π/64 on I1's own k-grid: C_E agrees to 10⁻⁷, C_B to 0.09% (I1's finite-difference residual). The Brillouin-zone integral uses nested cubes around k = 0 (each shell 12³ cells less its centre, 2×2×2 Gauss points), down to θ/4; at θ = 0.3 it matches I1's grid sum to 0.08%, and at θ = 0.01 the 9- and 12-cell versions agree to 10⁻⁴. A pre-check at θ = 0.01 already shows C_E < 0 (seen before this registration).

**Cases.** θ = 10⁻³, 3×10⁻³, 10⁻², 3×10⁻², 0.1, 0.3. q = θ/20 and θ/10; c₂ extrapolated to q → 0 from the two (linear in q̂²). Z_E = −4c₂^E, Z_B = 4c₂^B; c_ind = √(Z_B/Z_E).

**Leading log, one four-component Dirac species of unit charge and speed c₀ = 2cos w:** dZ_E/d ln(1/θ) = 1/(6π²c₀) = 0.01520, dZ_B/d ln(1/θ) = c₀/(6π²) = 0.01876.

**Fail conditions.**
- F1: Z_E or Z_B not positive at θ = 10⁻³.
- F2: the slopes dZ/d ln(1/θ), fitted over θ = 10⁻³ to 3×10⁻², differ from the leading-log values by more than 10%.

**Reported, not tested.** c_ind/c₀ − 1 against 1/ln(1/θ); the finite parts Z_fin (intercepts).

## Result of the registered run, and a fix for Z_B (after the run, before rerunning Z_B)
As registered, F1 and F2 FAIL, both through Z_B: Z_B = −2.1×10³, −2.3×10², −20, −2.0, −0.16 at θ = 10⁻³ … 0.1, scaling as 1/θ². That scaling is a q-independent constant in C_B divided by q̂² ∝ θ²: the response to a uniform A_y, which gauge invariance sets to zero, but which the nested-cube quadrature (not translation-invariant in k_y) leaves at a finite value. The registered extrapolation assumed no constant term. Z_E has no such offset (a potential does not shift k) and is taken as run: positive for θ ≤ 0.1, slope 0.01648 against the leading log 0.01520 (+8.4%).

**Fix for Z_B, chosen before rerunning.** C_B at q = θ/20, θ/10, θ/5, fitted as C₀ + c₂q̂² + c₄q̂⁴; Z_B = 4c₂. Gate: the fitted C₀ must match the uniform-A_y response computed directly on the same quadrature (¼∫Σ_filled ∂²E/∂k_y², finite difference) within 2%; otherwise invalid. F1 and F2 then as registered, with this Z_B and the Z_E above.
