# L1 — the 3D walk's low-energy dispersion (registered 2026-11-09)

**Why.** The Lorentz entry (MATTER record, 2026-11-08) rests on a 1D small-k reduction, not run: on the Wilson walk a massive pattern's limiting speed exceeds the massless one at order r·m (dimension four, tree level), the massless dispersion bends superluminally at order r²k², and the sequential ordering carries a chirality-dependent term linear in energy. Crab PeV electrons then give ℓ ≲ 6 × 10⁻³² m. The outcome in 3D is unknown and decides that bound.

**Walk.** The adopted walk (MATTER.md): Dirac α, β on C⁴; palindromic step x y z | flip | z y x with the unitary Wilson angle θ(k) = θ + rΣ(1 − cos k_j), r = 0.3; the sequential step x y z | flip for comparison. Lattice units; the palindrome makes two hops per direction per step.

**Measured.** Smallest quasi-energy E(k) along the axis, face diagonal and body diagonal, k from 0.005 to 0.08, at θ = 0 and θ = 0.01, 0.02, 0.04. Fit E² = θ² + A k² + B k⁴.
- Speed of a massive pattern relative to the massless one: s(θ) = √(A(θ)/A(0)) − 1. Expected from the 1D reduction: s ≈ (r/2)·θ' with θ' the mass in hop units (order one coefficient; sign positive).
- Massless bending: B(0)/A(0)² sign and size, by direction (positive = superluminal).
- Sequential step: the splitting of the two near-zero positive quasi-energies, its order in k and its dependence on direction (linear-in-energy term expected ∝ k_xk_yk_z/|k|, zero along the axis).

**Decision.** If s(θ) is linear in θ with an order-one coefficient times r, the electron bound ℓ ≲ 10⁻³¹ m goes from candidate to needed. If s vanishes or is suppressed (order θ²), the binding tree-level bound is the quadratic term's or light's. If the sequential splitting is order k² with an order-one coefficient off-axis, the sequential exclusion stands.

**Checks.** Pre-run: at θ = 0, r = 0, the palindrome's small-k speed is 2 (two hops per step) and isotropic. Post-run: one check of the fits' residuals.
