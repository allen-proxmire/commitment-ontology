# C3s: the Crab synchrotron cutoff with subluminal electrons (desk, 15 Nov 2026)

**Assumptions, stated before computing.**
- Flow step at r = 0.5: electron speed v − 1 = s − m²/(2p²) + c₂(pℓ)², s = ½ r μ, μ = mₑcℓ/ħ = ℓ/λ_C (λ_C = 3.86×10⁻¹³ m), c₂ = −0.406, −0.156, −0.073 (axis, face, body). Its maximum over p is μ(r/2 − √(2|c₂|)) < 0, so the Lorentz factor is capped: γ_max = [2μ(√(2|c₂|) − r/2)]^(−1/2) (s kept) or [2μ√(2|c₂|)]^(−1/2) (s absorbed). Following Jacobson, Liberati and Mattingly (2003), synchrotron emission at the critical frequency ħω_c = (3/2)γ²ħeB/(mₑc) = 1.74×10⁻⁸ eV·(B/1 G)·γ² is taken to hold up to γ_max.
- The Crab's synchrotron spectrum reaches 100 MeV. Nebular field B = 125 μG (the value used in standard one-zone models) to 1 mG (higher estimates).
- The direction of the emitting electrons against the lattice is unknown, so the weakest direction (the body diagonal, smallest deficit) is used.

**Computation.** Needed γ = (10⁸ eV / (1.74×10⁻⁸ eV·B[G]))^(1/2): 6.8×10⁹ at 125 μG, 2.4×10⁹ at 1 mG. Bound: 2μ·Δ ≤ 1/γ², Δ = √(2|c₂|) − r/2 = 0.132 (s kept, body) or √(2|c₂|) = 0.382 (s absorbed, body).

| B | s kept | s absorbed |
|---|---|---|
| 125 μG | ℓ ≲ 3.2×10⁻³² m | ℓ ≲ 1.1×10⁻³² m |
| 1 mG | ℓ ≲ 2.6×10⁻³¹ m | ℓ ≲ 8.8×10⁻³² m |

**Reading.** Subluminal electrons restore an electron bound of the old size at the standard field (3.2×10⁻³² m, s kept), weakening eightfold at the highest field estimates; the photon bound (4.2×10⁻³¹ m) is the model-independent floor. Grade: candidate bound, conditional on the nebular field and on synchrotron's form holding up to γ_max. δ ≳ 3×10⁻⁶ (125 μG, s kept) to 2×10⁻⁸ (photon floor).
