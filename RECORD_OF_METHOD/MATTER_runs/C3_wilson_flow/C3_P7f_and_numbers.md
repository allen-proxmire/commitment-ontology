# C3: how the field enters the flow step, and the walk-specific numbers redone (desk, 15 Nov 2026)

## P7f restated for the flow

On the palindrome, P7f put the field in through three flips: mass θ → θN; Wilson flip 2cos w = c₀N/ψ² (the local light speed); the shift as a spin-blind directed hop. On the flow the same content is one Hamiltonian, Hermitian-ordered (½{·,·} where a field multiplies a hop):

H = ½{N/ψ², K} + β m N + ½ Σ_j {b_j, sin k_j},  K = Σ_j α_j sin k_j + β r Σ_j (1 − cos k_j),

with U = exp(−iτH) per tick. N is the lapse, ψ² the hop stretch (the conformal factor), b the shift (a drift of b in flow units, light speed 1).
- *Local light speed:* N/ψ², as P7f's Wilson rule required; *mass:* mN, as P7f's mass rule.
- *Shift:* the spin-blind directed term carries matter at b, as the brickwork rotation did (drift 2 sin b on the palindrome).
- *No window to leave:* on the palindrome the field moved w, and w left the Wilson window at GM/rc² ≈ 0.053 (P7f weak-field only). On the flow the field rescales the hop term; r is untouched. The only condition is that the tick's phases stay clear of π: τ·(N/ψ²·6.08 + |b|) < π for r = 1 (τ = 0.4: N/ψ² up to about 1.2 with b = 0). The strong-field form (shift alone, N = ψ = 1) and its horizon carry over (|b| > 1 is faster than light).
- *Grade:* shape, to be checked by rerunning the gravity runs' key cases (free fall G5, light bending G6, the closed loop G13) on the flow.

## The walk-specific numbers, redone (c3_numbers.py, c3_numbers_out.txt)

The tick's quasienergy is τ times H_W's energy exactly, so the dispersion is H_W's (no time-step corrections).
- *Speed excess* of a massive pattern: E² ≈ m² + k²(1 + rm), so s = ½ r·mcℓ/ħ (the palindrome's ½ sin w, with r in w's place).
- *Quadratic term* (group velocity v = 1 + c₂(kℓ)², the record's convention): c₂(n̂) = 3(r²/8 − Σ n_j⁴/6). At r = 1: −0.125 (axis), +0.125 (face), +0.208 (body). At r = 0.5: −0.406, −0.156, −0.073.
- *Consequence of r:* for r > 2/3, c₂ is positive off the axes, so electrons outrun straight light at high momentum there (vacuum Cherenkov from the quadratic term) and photons split only along the axes. For r < 2/3, c₂ is negative in every direction, as on the palindrome.
- *Crab bound* (electron speed excess below 2.45×10⁻²⁰ at 2.31 PeV): r = 1, s kept: ℓ < 1.4×10⁻³² m (body diagonal binds); s absorbed: ℓ < 2.9×10⁻³² m (the quadratic term alone, body diagonal). r = 0.5, s kept: ℓ < 3.8×10⁻³² m (s alone); s absorbed: no bound.
- *Photon splitting* (straight light; s absorbed; C from the quadratic term, C = (3/(2|c₂| f))^(1/4), f = 1/12 the lopsided-split factor, which reproduces the record's 3.8 for the palindrome's axis): r = 1: C = 3.46 along the axes only. r = 0.5: C = 2.58, 3.28, 3.96 (axis, face, body). The s-kept coefficients need the full kinematics (not computed).
- *r is a posited value,* as w was. r < 2/3 keeps the palindrome's pattern (electrons bend below light in every direction); r = 0.5 keeps the extra species at Wilson masses 1, 2, 3 (flow units), well clear of the light one. C3i's induced-light check was at r = 1; isotropy holds for every r, the sign at r = 0.5 is not computed.
