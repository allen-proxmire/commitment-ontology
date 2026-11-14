# B2d: registration (14 Nov 2026, after B2c, before this run)

**Why.** B2c is uninformative by its own rule: its control (a deliberate wall-to-wall mass of strength 0.2) moved only 2.3% of the packet, below the 10% bar. Its packet sat at k₀ = 0.05, where the two walls' modes are detuned by 2c₀k₀ ≈ 0.11, so a mass barely mixes them. The disturbed cases also moved weight by switching the disturbance on suddenly (part of the packet lands in bulk states, which spread over the whole inner ring); that is not mass. B2c's numbers stay in the record. This check returns to the spectrum.

**Construction.** Disturbance varies along x with a period of Lc = 8 places (random within the cell), so a Bloch momentum q stays exact while x-variation is real. Folding brings the wall-1 and wall-2 modes to the same q at several points. Each crossing is avoided by a gap set by the walls' coupling, including couplings that use the disturbance's x-momentum.

**Measure.** For each q (fine scan, then refinement at local minima), the splitting between adjacent sub-gap levels (|E| < 0.25). At each local minimum, the pair counts as a wall-to-wall crossing if both states have between 30% and 70% of their weight on the wall-2 half of the ring. m = half the largest such splitting (the worst crossing).

**Cases.** ε = 0.2, w = 5π/16, θ = ±0.5, n = (1,1,1) + unit Gaussian per place (x, s), static. (a) one draw per L, seed 11; (b) seeds 12–14 at L = 16. Control: same, plus a direct mixing of the wall rows s = L and s = 0 of strength 0.2 at every x (a deliberate mass).

L = 8, 12, 16.

**Fail conditions.**
- F1: (a) m(16) > m(8)/10, or any case at L = 16 gives m > 10⁻³.
- F2: no wall-to-wall crossing found in the disturbed cases (the measure saw nothing).
- Uninformative: control m(16) < 0.03.

**Not tested.** Time variation (a slow disturbance is a sequence of static ones, each covered here; fast variation heats the bulk, a separate question).

## Control correction (after the run, before rerunning the control alone)
B2d's disturbed cases passed F1 and F2, but the control gave m = 1.5×10⁻³, below the 0.03 bar, so B2d is uninformative as registered. The cause: the control mixed the wall rows keeping each spin component. The two walls' modes have opposite handedness, so their spin states are close to orthogonal and a spin-keeping mix barely couples them (a Dirac mass is off-diagonal in handedness). Corrected control, fixed before running: mix with a spin turn, row 0 ← cos ε·row 0 − i sin ε·(n̂₀·σ)·row L and row L ← cos ε·row L − i sin ε·(n̂₀·σ)·row 0, n̂₀ = (1,1,1)/√3 (unitary, since n̂₀·σ is Hermitian and squares to 1). Same bar: m(16) ≥ 0.03, else uninformative. Only the control is rerun; F1 and F2 stand as recorded.
