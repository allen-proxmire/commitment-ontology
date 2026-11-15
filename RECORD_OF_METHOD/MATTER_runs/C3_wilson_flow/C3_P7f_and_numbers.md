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

## Corrections (cold read, 15 Nov 2026)
- *Crab bound, wrong above:* the script kept only positive quadratic terms (max(c₂, 0)). With the electron's full excess v − 1 = s − m²/(2p²) + c₂(pℓ)², its maximum over p is μ(r/2 − √(2|c₂|)) for c₂ < 0 (μ = mcℓ/ħ): a vacuum-Cherenkov band exists only where Σn_j⁴ < r², i.e. for r > 1/√3 ≈ 0.577. At r = 0.5: max(v − 1)/μ = −0.651, −0.309, −0.132 (axis, face, body); electrons never outrun straight light, s kept or absorbed: **no electron Crab bound at r = 0.5.** At r = 1 the axis case is marginal (maximum exactly 0); the face and body bounds stand.
- *"r < 2/3 keeps the palindrome's pattern":* only half true; the palindrome had an off-axis electron band, r = 0.5 has none. Positive c₂ sets in near the body diagonal for r > 2/3 and at the face diagonal only for r > √(2/3).
- *Photon splitting, s kept (now computed):* C solves (|c₂|/3)g(x)C⁴ − (r/2)C² − 1/(2x(1−x)) = 0, minimised over the share x (g = x³ + (1−x)³; the same kinematics give the palindrome's 3.80 and 5.37). At r = 0.5: axis 2.58 / 2.92, face 3.28 / 3.94, body 3.96 / 5.10 (s absorbed / kept).
- *The bound on ℓ then comes from LHAASO's 2.5 PeV photon surviving:* ℓ < C²mₑc²ħc/E²: 1.1–2.5×10⁻³¹ m (s absorbed), 1.4–4.2×10⁻³¹ m (s kept); 4.2×10⁻³¹ m if the photon's direction is unknown; δ ≳ 2×10⁻⁸ (against 3.5×10⁻⁶ from the palindrome's Crab bound). A photon above about 1.1–2.1×10¹⁷ eV excludes straight light at every allowed ℓ.
- *Strong fields:* at r = 0.5 the band edge is 3.0 + m; the tick condition τ(3.0·N/ψ² + |b|) < π allows N/ψ² < 2.6 or |b| < 4.85. N/ψ² ≤ 1 in attractive static fields, so it never bites there; in Painlevé–Gullstrand form b exceeds 4.85 at ρ < 0.043 r_s, deep inside a hole, where the tick's phases wrap and the ruled vacuum stops being H's sea. Strong-field form and shift drift: expected to carry, not rerun.
- *Extra species in a field:* under P7f restated their rest energy is (N/ψ²)·2rn + mN, so they gravitate through N/ψ² ≈ 1 − 2gx (about twice the clock's change, same sign), not as G9 found on the palindrome. Placing the Wilson term with the mass instead would make them fall like matter; the restatement follows the ruling that the Wilson turn is part of the hop.
- *Numbers at r = 0.5 (τ = 0.4, θ = 0.03):* extra species at quasienergies 0.43, 0.83, 1.23; π-gap about 1.9; reach 0.44, 3.0×10⁻², 2.2×10⁻³, 7.5×10⁻⁵ at 1–4 places. The step's symmetry is the full cubic group (quarter-turns and parity hold), not only the tetrahedral subgroup. τ is a convention (tick length against flow time) except in the strong-shift limit.
- *C3j:* induced light at r = 0.5 extrapolates to −0.7% at ln(1/θ) = 53.
