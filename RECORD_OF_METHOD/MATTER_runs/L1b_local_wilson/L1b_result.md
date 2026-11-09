# L1b result — a strictly local Wilson walk, and L1 rechecked on it

Run 2026-11-09, `l1b_local_wilson.py`, `l1b_result.json`. Step A_x A_y A_z F(θ) A_z A_y A_x with A_j = S_j⁺ F(w) S_j⁻ F(−w): half-shifts (one part moved one place) and on-site coins only, so strictly local.

**Pre-check.** At w = 0 the walk is the palindrome without the Wilson term: speed 2.000000 along axis, face and body diagonals.

**1. One light species, for w ≳ 0.3.**

| w | light species, quasi-energy 0 | quasi-energy π |
|---|---|---|
| 0.2 | k = 0 only | 8 extra (at k = ±π/2 on the axes, and two near (π, ±0.6π, π)) |
| 0.3 | k = 0 only | none |
| π/10 | k = 0 only | none |

At w = 0.3 and π/10 every species but the one at k = 0 is gapped in both sectors: the strictly local form does what the quasi-local Wilson flip did.

**2. A massive pattern still outruns the massless one.** s(θ) = √(A(θ)/A(0)) − 1, identical along axis, face and body diagonals:

| w | massless speed per step | s/θ at θ = 0.01, 0.02, 0.04 | s in units of mcℓ/ħ |
|---|---|---|---|
| 0.3 | 1.911 | 0.076, 0.074, 0.071 | 0.144 |
| π/10 | 1.902 | 0.080, 0.078, 0.075 | 0.151 |

(θ = c₀·mcℓ/ħ with c₀ the massless speed per step.) Positive, isotropic, linear in mass, as on the quasi-local walk (L1: 0.072 mcℓ/ħ at r = 0.3): about twice as large.

**3. Massless bending and splitting.** Bending B/A²: −0.002 (axis), −0.082 (face), −0.108 (body): subluminal off-axis, as in L1. No branch splitting (≤ 10⁻¹³ k²).

**Post-run check.** Fit residuals ≤ 2 × 10⁻⁷.

**What it decides (by the registered rule).** (i) holds for w ≳ 0.3, and s is linear in θ, so the electron bound is recomputed: with the Crab bound s < 4.9 × 10⁻²⁰, **ℓ ≲ 1.3 × 10⁻³¹ m** for the strictly local walk at w = 0.3 (1.25 × 10⁻³¹ m at π/10), and δ ≳ 2 × 10⁻⁷ P_max/ħ. This replaces 3 × 10⁻³¹ m if the strictly local walk is adopted. The effect is not an artefact of the quasi-local flip's tails: a strictly local walk carries it too, at about twice the size.
