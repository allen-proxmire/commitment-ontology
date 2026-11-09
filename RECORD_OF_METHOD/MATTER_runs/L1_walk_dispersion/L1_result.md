# L1 result — the 3D walk's low-energy dispersion

Run 2026-11-09, `l1_dispersion.py`, `l1_result.json`. Walk: Dirac α, β on C⁴, unitary Wilson angle θ(k) = θ + rΣ(1 − cos k_j), r = 0.3. Lattice units; the palindrome makes two hops per direction per step, so its massless speed is 2 per step and the rest quasi-energy θ = 2mcℓ/ħ.

**Pre-check.** At θ = 0, r = 0 the palindrome's speed is 2.000000 along the axis, face and body diagonals: as built.

**1. A massive pattern outruns the massless one (palindrome).** Fitting E² = θ² + Ak² + Bk⁴, the speed shift s(θ) = √(A(θ)/A(0)) − 1:

| θ | s | s/(rθ) |
|---|---|---|
| 0.01 | 3.58 × 10⁻⁴ | 0.119 |
| 0.02 | 6.83 × 10⁻⁴ | 0.114 |
| 0.04 | 1.23 × 10⁻³ | 0.103 |

identical along axis, face and body diagonals (isotropic), linear in θ with an order-θ² correction. In physical units s ≈ 0.12·r·θ = 0.24·r·mcℓ/ħ: positive, so a massive pattern's limiting speed exceeds the massless speed. The 1D reduction's sign is confirmed; its coefficient (r/2) is about half the measured 0.24r.

**2. Massless bending (palindrome).** B(0)/A(0)²: +0.0014 (axis), −0.082 (face), −0.110 (body). Anisotropic and, off-axis, subluminal: the 1D reduction's "superluminal r²/4" does not hold in 3D. In physical units Δv/c ≈ (3/2)(B/A²)(2Eℓ/ħc)², about −0.6(Eℓ/ħc)² on the body diagonal.

**3. Sequential step: a linear-in-energy term, confirmed.** Along the body diagonal the two positive branches sit at k ± 0.19k² (0.192 measured; k_xk_yk_z/|k| = k²/(3√3) = 0.192k² predicted), the same under k → −k; zero along the axis. The palindrome shows no branch splitting (≤ 10⁻¹² k²).

**Post-run check.** Fit residuals ≤ 2 × 10⁻⁷ of the fitted range.

**What it decides (by the registered rule).**
- Result 1 is linear in θ with an order-one coefficient times r, so the electron bound moves from candidate to needed. With s < 4.9 × 10⁻²⁰ (Crab, Li & Ma 2022; the bound needs the electron superluminal relative to light, which holds if light moves at the walk's massless c): ℓ < 4.9 × 10⁻²⁰ / (0.24 × 0.3 × mₑc/ħ) ≈ **3 × 10⁻³¹ m**. With q = P_max: (ℓ/ℓ_P)² ≲ 2.6 × 10⁸, P_max/δ ≲ 2 × 10⁷, **δ ≳ 5 × 10⁻⁸ P_max/ħ**.
- Result 2: the quadratic term is subluminal off-axis, so it gives no Cherenkov bound; it is not the binding term.
- Result 3: the sequential exclusion stands; the palindrome is needed.
