# B2b: registration (14 Nov 2026, after B2, before this run)

**Why a second check.** B2's F2 failed as registered: worst leak 1.4×10⁻² against the 10⁻² bar. The bar was mis-set. At L = 16 the undisturbed residual mass (8.1×10⁻⁴) already exceeds 0.01ε for ε = 0.05 (5×10⁻⁴), so F2 could fail with no leak at all. In the data, m did not grow with ε (coherent: 8.1 → 6.1 → 5.7 → 5.3 ×10⁻⁴). B2's F2 stays recorded as failed. This check replaces the bar with the signature that separates protection from leak; it was chosen before running.

**Signature.** A leak gives a mass of order ε that does not depend on L: m(L) plateaus. Protection gives m(L) still falling exponentially under the disturbance.

**Setup.** As B2 (θ = ±0.5, w = 5π/16, P_s = exp(−iε n̂_s·σ), n_s = (1,1,1) + unit Gaussian, uniform in x). ε = 0.2, the strongest B2 value. Coherent disturbance plus 5 random draws (seed 77). L = 8, 12, 16, 20, 24.

**Fail conditions.**
- F1: for any case, log m against L is not a falling straight line (slope > −0.1 per place, or R² < 0.98).
- F2: for any case, m(24) > 10⁻³ ε = 2×10⁻⁴.
