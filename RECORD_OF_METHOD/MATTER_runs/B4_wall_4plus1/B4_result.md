# B4: matter bound to the walls on the 4+1-dimensional flow step (16 Nov 2026)

Fail conditions in FAIL_CONDITIONS.md, written before the run. Free fermions; three space directions plus an inner ring of 2L places with mass walls ±0.5; r = ½ in all four directions; handedness γ₅ = iα₁α₂α₃, inner matrix α₄ = iγ₅β.

| check | result | outcome |
|---|---|---|
| B4a | at |k| = 0.05 exactly four light states (|E| = 0.0500), the next at 0.522 | PASS |
| B4b | two light states sit on one wall (98% of their weight within four places of it), both with γ₅ = −1; the other two on the other wall, both γ₅ = +1 (|⟨γ₅⟩| ≥ 0.99993) | PASS (wall assignment read along the axis) |
| B4c | light speed |E|/|k| = 0.9996 along an axis, 0.9999 along a body diagonal | PASS |
| B4d | leftover mass at k = 0 falls as e^{−κL}, κ = 0.405 per place (1+1D: 0.41), with an even–odd alternation | PASS |

**Reading.** On the step extended to four space directions, matter bound to the two walls of the inner ring is one-handed: one handedness on one wall and the opposite on the other (with γ₅ = iα₁α₂α₃ and α_j = γ⁰γ^j, γ₅ = −1 is right-handed), moving at light's speed along an axis and a body diagonal (0.9996, 0.9999), with the leftover mass falling at the 1+1-dimensional rate. Tuning 2's removal and the weak interaction's shape both rest on this. Free fermions; no gauge fields, no interactions.
