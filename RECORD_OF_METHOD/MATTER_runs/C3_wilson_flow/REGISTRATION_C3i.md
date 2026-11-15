# C3i: induced light on the flow step: registration (15 Nov 2026, before the run)

**Reading.** On the one-tick Wilson–Dirac flow (U = exp(−iτH_W), τ = 0.4, r = 1; shape, the author's ruling), the vacuum (quasienergies in (−π, 0) filled, as ruled) induces a field with the right sign at small mass, growing as the light species' leading log, and the same in every direction by symmetry.

**Method.** I2/I4's pair method (exact second order; filled–filled pairs dropped), with U(a) = exp(−iτ(H₀ + aH₁ + a²H₂)) and its Taylor blocks taken exactly from the exponential of a block upper-triangular matrix (checked against finite differences to 2×10⁻⁹). Peierls coupling: a link phase A on j-hops enters as H_W(k_j + A) to second order (diagonal part halved per pair); a potential V enters as H_W + V. Nested-cube quadrature (9 cells); each coefficient fitted as C₀ + c₂q̂² + c₄q̂⁴ at q = θ/20, θ/10, θ/5. θ = τm (the mass per tick) = 10⁻³, 3×10⁻³, 10⁻², 3×10⁻². ε_x from a potential along x; Z_B from a phase on y-hops varying along x.

**Leading log** (one Dirac species, unit charge, light speed c = τ places per tick): dZ_E/d ln(1/θ) = 1/(6π²τ) = 0.04222, dZ_B/d ln(1/θ) = τ/(6π²) = 0.006755.

**Fail conditions.**
- F1: Z_E or Z_B not positive at θ = 10⁻³.
- F2: either slope over θ = 10⁻³ to 3×10⁻² differs from the leading log by more than 10%.
- Construction check (not a test of the reading): ε_z − ε_x and Z_B(z,x) − Z_B(x,y) at θ = 10⁻² must vanish to 10⁻⁸ (cube symmetry); otherwise the code is wrong.

**Reported.** c_ind/τ − 1.

## After the run: result as registered, a units error, and a further check (registered before running it)
As registered: F1 PASS (both positive at every θ), cube check passes (ε_z − ε_x = −5×10⁻¹², Z_B difference 1×10⁻⁹), F2 FAIL (Z_E slope 0.00743 against 0.04222, −82%; Z_B slope 0.007655 against 0.006755, +13%).

**Units error in the registration.** Here the potential enters the Hamiltonian (energy per unit flow time), not as a phase per tick as on the palindromic walk, and the vacuum measure is phase per tick (τ times energy). Both coefficients then carry one factor τ: Z_E = Z_B = τ·ln(1/θ)/(6π²) at leading log (light speed 1 in flow units, τ places per tick), slope τ/(6π²) = 0.006755 for both. The registered Z_E value 1/(6π²τ) was wrong. Against the corrected value the straight-line slopes are +10% (E) and +13% (B); the local slopes fall toward it as θ falls (E: 0.00792, 0.00737, 0.00702; B: 0.00835, 0.00756, 0.00710), the same pattern as I2's O(θ) term. The induced speed is c_ind = √(Z_B/Z_E) in flow units against 1: +5.0%, +5.9%, +7.2%, +9.0% at θ = 10⁻³ … 3×10⁻², falling as θ falls.

**Further check, chosen before running.** θ = 10⁻⁴ and 3×10⁻⁴ (same method). Pass: the local slope between them is within 5% of τ/(6π²) for both Z_E and Z_B. Fail otherwise.
