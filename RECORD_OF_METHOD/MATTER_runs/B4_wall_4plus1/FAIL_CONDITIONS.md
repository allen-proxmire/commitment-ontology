# B4: matter bound to the walls on the 4+1-dimensional flow step — fail conditions (16 Nov 2026, before the run)

The flow step's Hamiltonian in three space directions plus the inner ring (2L places, mass +M on one half and −M on the other, M = 0.5, r = ½ in every direction), free fermions. Translation-invariant in the three space directions, so each momentum k is an exact problem of size 4 × 2L (four components on 2L inner places); the flow's eigenstates are H's (quasienergy τ_f E). Handedness in 3+1 dimensions: γ₅ = iα₁α₂α₃ (commutes with α_j, anticommutes with β); the inner direction's matrix α₄ = iγ₅β.

| check | prediction | fail if |
|---|---|---|
| B4a | at small k exactly four light states (|E| ≪ M), two bound to each wall | not four |
| B4b | the two at one wall have handedness γ₅ = +1, the two at the other −1 (one handedness per wall: a Weyl fermion at each) | |⟨γ₅⟩| < 0.99 at |k| = 0.05, L = 16, or the walls the same sign |
| B4c | light states move at light's speed, E = ±|k|, along an axis and a body diagonal | off by > 1% at |k| = 0.05 |
| B4d | at k = 0 the leftover mass falls as e^{−κL} with κ ≈ 0.41 per place, the 1+1-dimensional rate (B3), since at k = 0 the inner problem is the same | κ off 0.41 by > 5% |
