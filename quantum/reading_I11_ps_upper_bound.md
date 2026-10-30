## Reading I11: is p_s bounded from above?

*29 October 2026. After Run 100 (the engine-hop minimal line against p_s). A reading of the record, plus arithmetic on published limits. It encodes no new rule. Revised after two independent checks, whose corrections are adopted. Ruled in §7.*

**In plain terms.** The model has one free number, which sets how fine its underlying grid is. This reading asks whether any existing measurement puts a ceiling on that number. If ordinary matter felt the grid directly, observations of the Crab Nebula would rule out every value the model's recent runs point to, and cosmic-ray data might rule out all values. But the model takes the symmetries of special relativity as given, so in the model matter is not meant to feel the grid in this way. Since the model does not make that claim, these measurements do not test it. The only ceiling that follows from the model's own record is a very loose one, far above the values of interest, so the number remains a fitted input rather than a prediction.

### 1. Why
Reading I10 ruling 2 made the engine-hop minimal line (C1a, K = 1, a = 1) a named candidate. Its free number is p_s:
$$
\ell=\ell_P\sqrt{\frac{0.99\pi\,a\,p_s}{3}},\qquad m_\ell=\frac{\hbar}{c\ell},\qquad \rho_K=\frac{m_\ell}{V_c},\qquad p_s=\frac{3}{0.99\pi a}\Big(\frac{\ell}{\ell_P}\Big)^2 .
$$
Run 100 (`PREREG_100.md` §3a; `run100_engine.log`) puts the near-zone saturation onset at present limits **continuously from 1.3×10¹² to 4.3×10¹⁹, and intermittently at 2–5×10⁸, 3×10⁹–1.6×10¹⁰ and 8×10¹⁰–4×10¹¹** (a = 1; PREREG_100 windows H, G, G′, LISA). The record bounds p_s from below (≳ 4×10⁵, conditional since Reading I6 ruling 4). An upper bound would make the link a definite test.

| p_s (a = 1) | ℓ (m) | ℓ/ℓ_P | ħc/ℓ (GeV) |
|---|---|---|---|
| 4×10⁵ | 1.0×10⁻³² | 644 | 1.9×10¹⁶ |
| 2×10⁸ – 10⁹ | 2.3–5.2×10⁻³¹ | 1.4–3.2×10⁴ | 8.5–3.8×10¹⁴ |
| 1.3×10¹² | 1.8×10⁻²⁹ | 1.1×10⁶ | 1.1×10¹³ |
| 10¹⁶ | 1.6×10⁻²⁷ | 1.0×10⁸ | 1.2×10¹¹ |
| 4.3×10¹⁹ | 1.1×10⁻²⁵ | 6.7×10⁹ | 1.8×10⁹ |

### 2. What the record already says
- **The hop is the engine's lattice step, the one light crosses.** Note D point 4 (`gravity/reading_P0ps_section.md`) builds G from three counts in hops: U = 3S/(2πcr) with r in hops, light crossing ħ_t hops per vacuum hold, and E = aħ/T_hold. So the hop that sets G is the step light takes (an inference, checked against the code).
- **The hop is conditional.** Reading I6 ruling 4 made p_s ≳ 4×10⁵ and the hop of 10^2.5–10³ ℓ_P conditional, and reopened P-G-Closure (ℓ_ED = ℓ_P). Reading I5 ruling 3 keeps the hop "an open tension": P08's ℓ_P against the engine's ℓ(a, p_s). **On P08's hop the hop does not depend on p_s,** and nothing below bounds p_s.
- **Upper bounds on record** bound ε or P∞, not p_s alone: the pulsar triple, P∞/p_s ≳ 1.6–1.9×10⁵ (Run 57); Run 96's floor κ_b > 5.6×10⁻³⁶, with κ_b = 1/(aP∞) by definition (Reading I4, I6), so aP∞ ≲ 1.78×10³⁵ (Reading I7).
- **β − 1, Δ and Nordtvedt** depend on ε = p_s/P∞ only (R3, R9; Run 66). With |β − 1| ≲ 10⁻⁴ and the P∞ bound they give p_s ≲ 4×10³¹/a, weaker than §3. The lower bound P∞ ≳ 6.4×10¹⁰ bounds nothing from above.
- **Light's dispersion on the lattice is not a statement of the record.**
  - R6 derives light's speed from hopping on ticks ("a pattern hops on its place's ticks … so light's coordinate speed is N²") but states only the continuum equation, −N⁴∇²ψ + m²N²ψ = ω²ψ.
  - The lattice dispersions that appear belong to the engine's schemes: Run 9's k = 2 arcsin(ω₀/2v); Run 16's (2/δt)²sin²(Ωδt/2) = m²N² + Σ4sin²(k_i/2), with δt = 0.1 tick and "the one-hop-per-tick limit c = 1".
  - R4: "the engine's tick is not physical time". The 23 October statement: "the engine's medium is itself an average … stand-in" (`record/ONTOLOGY_full.md`, arrow section).
- **The record borrows Lorentz invariance** (R7, "put in by hand", for ticks and relations; R8's Lorentz input of 19 October; the Open item "Deriving the borrowed inputs: Lorentz invariance"). A lattice term for light or matter therefore contradicts a borrowed input; it does not fill a gap.
- **Run 90 concerns gravitational waves.** "Relativistic to O(s⁵)" is the constant-lapse TT dispersion at field order 2 under GR's imposed constraint algebra:
$$
\omega^2_{TT}=s^2+O(s^5)\quad\text{in place of Run 84's}\quad \omega^2=s^2-\tfrac1{12}\textstyle\sum_a s_a^4 .
$$
  These are Run 90's own limits: kinetic sector, constant lapse, field order 2; form (iii) not certified globally. Run 90's reading (ONTOLOGY_full line 613): the boost relation {H[1], H[xᵃ]} = D[e_a] "holds only for Lorentz-invariant linear dynamics", so closure at a² needs a Symanzik-type improvement. Matter contributes to the same constraints; on a flat background its boost relation is Lorentz invariance of its linear dynamics. If the algebra is imposed on the coupled system, patterns must also be relativistic through a². This is an inference; the calculation for a matter field or light has not been run.
- **The design note's carrier table** (`gravity/design_shear_waves.md` §2(a)) used ℓ_hop = 10³ ℓ_P for gravitational-wave damping. It is an estimate, not a bound.
- **No file in the record** mentions Fermi, LHAASO, MAGIC, H.E.S.S., Auger LIV bounds, E_QG or birefringence.

### 3. The record's upper bound (Reading I10 §3), with its number
Reading I10 line 75 already gives p_s ≲ P∞/1.6×10⁵ ≲ 10³⁰. With the numbers:
$$
a\,p_s\le\frac{a P_\infty}{1.6\times10^5}\le\frac{1}{1.6\times10^5\,\kappa_b^{\min}},\qquad
\ell\le\ell_P\sqrt{\frac{0.99\pi}{3\cdot1.6\times10^5\,\kappa_b^{\min}}} .
$$
| Run 96 floor κ_b^min | a·p_s < | ℓ < |
|---|---|---|
| 5.617×10⁻³⁶ (primary; assumes a Mo housing) | 1.1×10³⁰ | 1.7×10⁻²⁰ m |
| 3.634×10⁻³⁶ (self term only) | 1.7×10³⁰ | 2.2×10⁻²⁰ m |

- a cancels in ℓ. The bound sits far above Run 100's ladder (top 4.3×10¹⁹).
- **Grade: from the record (restates Reading I10 §3).** Conditional on Note D's G, Run 57, and Run 96's route (b) and Q4, and on κ_b's P∞ being gravity's P∞.

### 4. Bounds from established data, by what each would need
Notation. The lattice term is written, in units ħ = c = 1,
$$
E^2=m^2+p^2-\alpha_n\,p^{2+n},\qquad
\alpha_2=\frac{\ell^2(S-\sigma^2)}{12},\quad S=\sum_i n_i^4\in\big[\tfrac13,1\big],\quad \sigma=\frac{c\,\delta t}{\ell},
$$
for the plain nearest-neighbour stencil (n = 2), and, for a stencil improved through a² (n = 4; the fourth-order central stencil as the example),
$$
\alpha_4=\frac{\ell^4 S_6}{90},\qquad S_6=\sum_i n_i^6\in\big[\tfrac19,1\big].
$$
Odd n do not occur: a cubic lattice is inversion-symmetric, so ω² is even in k. Bounds are quoted at a = 1 and continuous time (σ = 0) unless stated; a = 0.1 multiplies p_s by 10, a = 2π divides it by 6.3.

**Time discretisation.** With a leapfrog step (the engine's Run 16 scheme) the n = 2 coefficient is (S − σ²)/12, checked numerically (log §2a). At σ = 0.1 the change is 1–3%. At σ² = ⅓ the body-diagonal term vanishes and that direction gives no bound; at σ = 1 (one hop per tick) the axis term vanishes and the diagonal turns superluminal, and the 3-D nearest-neighbour leapfrog is unstable above σ = 1/√3. Every lattice statement below therefore specifies continuous time or σ ≪ 1.

Two statements are tested:
- **S-γ:** in vacuum, light carries the unimproved nearest-neighbour dispersion at the engine's hop ℓ, fixed in physical length, in continuous time.
- **S-m:** massive patterns (nucleons, pions, electrons) carry the same term. Together with S-γ this is the plain lattice shared by matter.

#### 4.0 Conventions confirmed from the papers
**Pierre Auger Collaboration, JCAP 01 (2022) 023 (arXiv:2112.06773).**
- Dispersion (Eq. 2.2): E_i² − p_i² = m_i² + Σ_n δ_{i,n} E_i^{2+n}. δ > 0 is superluminal, δ < 0 subluminal; the photon analysis takes "subluminal LIV (δ_γ < 0)". The lattice term is δ = −α (subluminal).
- **Hadronic sign.** "If δ_had,0 > 0 … the number of interactions during propagation is reduced"; "We consider only positive LIV coefficients (δ_had > 0)." Negative values are not constrained, because the photopion and photodisintegration cross-sections "prevent a significant decrease in the attenuation length". **So the sign that suppresses photopion production in Auger's analysis is δ_had > 0, the superluminal sign, the opposite of the lattice term.**
- **Per nucleon.** "δ_had := δ_p = δ_π/2 = Aⁿ δ_A" (Eq. 6.3, superposition model). The bound is on the per-nucleon coefficient, with nuclei already included; no further Aⁿ dilution applies. The choice δ_π = 2δ_p is motivated by photopion effects depending on δ_π − δ_p (following Scully and Stecker).
- **Hadronic bounds:** δ_had,0 < 10⁻¹⁹ at 5σ, "valid for all the UHECR scenarios studied here"; the n = 1, 2 values (δ_had,1 < 10⁻³⁸ eV⁻¹, δ_had,2 < 10⁻⁵⁷ eV⁻²) are estimated from it by Eq. 6.4, δ_had,0 R_cut²Z² = δ_had,n R_cut^{n+2}Z^{n+2}.
- **Photon bounds:** none in the reference scenario (the simulated flux stays below the limits even as δ_γ,0 → −∞). With a subdominant proton component up to 10²⁰ eV: δ_γ,0 > −10⁻²¹, δ_γ,1 > −10⁻⁴⁰ eV⁻¹, δ_γ,2 > −10⁻⁵⁸ eV⁻². No confidence level is stated.
- **Consequence.** Auger's hadronic bound does not transfer to the lattice term: the sign is opposite and the pion-to-proton ratio differs (universal lattice: δ_π = δ_p). The check's p_s ≲ 2–5 (and ≲ 10⁶ with A³ dilution) is withdrawn.
- **Residual tension.** The collinear threshold for p + γ → p + π, at x = m_p/(m_p + m_π),
$$
4E\omega\ \ge\ 2m_pm_\pi+m_\pi^2+E^{n+2}\big[\delta_p x^{n+1}+\delta_\pi(1-x)^{n+1}-\delta_p\big],
$$
  gives at n = 0 with δ_π = 2δ_p a shift +0.13 δ_p E² (suppression for δ_p > 0, agreeing with Auger). At n = 2 it gives −0.336 δ_p E⁴, i.e. suppression for δ_p < 0 (log §3). Auger's n ≥ 1 hadronic limits are rescalings of the n = 0 fit (Eq. 6.4), so their sign statement is the n = 0 one (δ_π − δ_p > 0); at n = 2 the kinematics makes δ_p < 0 the suppressing sign. The number does not transfer either way.

**Jacobson, Liberati and Mattingly, Nature 424, 1019 (2003) (astro-ph/0212190).**
- Dispersion E² = m² + p² + η p³/M, M = 10¹⁹ GeV: cubic (n = 1), not the lattice's p⁴. For η < 0 electrons have a maximal speed below c, so γ is bounded and the synchrotron critical frequency has a maximum.
- Lorentz-invariant 100 MeV synchrotron emission needs **γ = 3×10⁹ (about 1500 TeV) at B = 0.6 mG**, the top of the 0.15–0.6 mG range, chosen as the weakest case. If 100 MeV were the LIV maximum frequency, electrons of about 2300 TeV would be needed. Result: η > −7×10⁻⁸; no confidence level stated.
- The p⁴ case was published by **Liberati, Maccione and Sotiriou, Phys. Rev. Lett. 109, 151602 (2012) (arXiv:1207.0670)**: E² = m² + p² + η p⁴/M_LV², with subluminal η < 0 giving a maximal critical frequency. "M_LV ≲ 2×10¹⁶ GeV are excluded at 95% CL." This is the row used below. The first check's γ range 10⁹–3×10⁹ is replaced by JLM's field, B = 0.6 mG, which gives γ_req = 3.1×10⁹.

**Maccione, Taylor, Mattingly and Liberati, JCAP 04 (2009) 022 (arXiv:0902.1756)** covers the universal case. Its dispersion is E² = p² + m² + η p⁴/M_Pl², with independent η_p, η_π and a purely protonic flux; nuclei are treated as Lorentz-invariant. In the narrow region where η_p and η_π are both negative and nearly equal, the proton bound weakens to η_p ≳ −10⁻³ (99% CL); the −10⁻³ lies at one edge of their simulated field. The paper does not exclude that region. Mapping: α₂ = |η|/M_Pl², and ħc/M_Pl = ℓ_P.

#### 4.1 Photons (S-γ): time of flight, n = 2
$$
\omega^2=c^2k^2\Big[1-\frac{(k\ell)^2}{12}S\Big],\qquad v_g=c\Big[1-\frac{(k\ell)^2}{8}S\Big],\qquad E_{QG,2}=\frac{\hbar c}{\ell}\sqrt{\frac{12}{S}},
$$
in LHAASO's convention E² ≃ p²c²[1 − s(E/E_QG,n)ⁿ], s = +1 subluminal, Δt = s (n+1)/2 (E_hⁿ − E_lⁿ)/E_QG,nⁿ ∫₀ᶻ(1+z′)ⁿ/H dz′. Inverted:
$$
p_s<\frac{3}{0.99\pi a}\,\frac{12}{S}\Big(\frac{\hbar c}{\ell_P\,E_{QG,2}^{\rm lim}}\Big)^2 .
$$
| limit (subluminal, n = 2) | E_QG,2 > (GeV) | ℓ < (m), S = ⅓ … 1 | p_s < (a = 1), S = ⅓ … 1 |
|---|---|---|---|
| LHAASO, GRB 221009A (95%) | 6.9×10¹¹ | 1.7×10⁻²⁷ … 9.9×10⁻²⁸ | **1.1×10¹⁶ … 3.6×10¹⁵** |
| Fermi-LAT, GRB 090510 (95%) | 1.3×10¹¹ | 9.1×10⁻²⁷ … 5.3×10⁻²⁷ | 3.1×10¹⁷ … 1.0×10¹⁷ |
| H.E.S.S., Mrk 501 (normalisation unchecked) | 8.5×10¹⁰ | 1.4×10⁻²⁶ … 8.0×10⁻²⁷ | 7.2×10¹⁷ … 2.4×10¹⁷ |
| H.E.S.S., PKS 2155-304 (normalisation unchecked) | 6.4×10¹⁰ | 1.9×10⁻²⁶ … 1.1×10⁻²⁶ | 1.3×10¹⁸ … 4.2×10¹⁷ |

- Under S-γ alone, Run 100's continuous band is cut to 1.3×10¹²–1.1×10¹⁶ (S = ⅓; to 3.6×10¹⁵ at S = 1). The intermittent windows, all below 10¹², are untouched.
- A comoving hop changes the delay integral by about 16% at z = 0.151 and about a factor of 2 at z = 0.903.
- **Grade: needs S-γ (contrary to the borrowed Lorentz input); published limit; continuous time.**

#### 4.2 Photons (S-γ): Auger's photon sector, n = 2
A subluminal photon term raises the pair-production threshold, so UHE photons travel farther and their flux would exceed Auger's limits. Setting δ_γ,2 = −ℓ²S/12:
$$
\ell<\sqrt{\frac{12\,|\delta_{\gamma,2}|}{S}}\,\hbar c=1.2\times10^{-35}\ \text{m}\ (S=\tfrac13),\qquad p_s<0.5 .
$$
If electrons share the term, the threshold shift is (3/4)|δ|E⁴ instead of |δ|E⁴. That loosens the threshold-level mapping by 4/3 (p_s < 0.7); the full propagation was not recomputed.
- This excludes S-γ over the whole record-allowed range (p_s ≳ 4×10⁵).
- **Grade: needs S-γ; published; holds only in Auger's subdominant-proton scenario (no constraint in the reference scenario); no CL stated.**

#### 4.3 Matter (S-m): threshold kinematics and the Crab, n = 2
A lattice term enters threshold reactions as αE⁴ against m², far below the band edge. For a universal term (δ_π = δ_p = −α) the shift is +0.338 αE⁴: the GZK threshold rises and photopion production is suppressed (log §3).
| bound | ℓ < (m), S = ⅓ … 1 | p_s < (a = 1) | grade |
|---|---|---|---|
| Maccione et al. 2009, η_p ≈ η_π < 0: \|η\| ≲ 10⁻³ (99% CL) | 3.1×10⁻³⁶ … 1.8×10⁻³⁶ | 0.035 … 0.012 | needs S-m; published; pure-proton flux |
| GZK shift equal to the threshold scale at 5×10¹⁹ eV (estimate, not a fit) | 4.3×10⁻³⁷ (S = ⅓) | 7×10⁻⁴ | needs S-m; own estimate; protons |
| Auger δ_had,2 < 10⁻⁵⁷ eV⁻² | — | does not apply | opposite sign (§4.0) |
| **Crab synchrotron, LMS 2012, M_LV > 2×10¹⁶ GeV (95% CL)** | 5.9×10⁻³² (S = ⅓) | **1.3×10⁷** (S = ⅓, conservative; 4.3×10⁶ along an axis); \|η\| = 1 as implied by the scan in M_LV; LMS assume an isotropic term | needs S-m for electrons; published; Crab emission model |
| Crab, JLM's ω_c-maximum criterion at n = 2, B = 0.6 mG (γ_req = 3.1×10⁹): M_eff = 2.2×10¹⁶ GeV | 5.4×10⁻³² … 3.1×10⁻³² | 1.1×10⁷ … 3.5×10⁶ | same; own application of JLM's method, consistent with LMS's fit |

For the Crab rows, an electron carrying the term has γ⁻² ≃ m_e²/E² + 3α₂E², and JLM's criterion is that the largest LIV critical frequency, ω_c = (3/2)(eB/m_e)·m_eγ³/E, reaches 0.1 GeV. For n = 2 the maximum lies at E⁴ = m_e²/(6α₂), not at γ_max (E⁴ = m_e²/(3α₂)):
$$
\max_E\frac{m_e\gamma^3}{E}=\frac{0.222}{m_e\sqrt{\alpha_2}}=\gamma_{\rm req}^2\ \Rightarrow\ \alpha_2<\frac{1}{20.25\,m_e^2\gamma_{\rm req}^4},\qquad \ell<\frac{\hbar c}{\sqrt S\,m_e\,\gamma_{\rm req}^2}\sqrt{\frac{12}{20.25}} .
$$
(v2 used γ_max ≥ γ_req, coefficient 0.289, which is looser by a factor of 1.9 in α₂.) The record's coefficient is S/12 because R6's patterns are scalar; a naive first-order fermion stencil would give S/3 and tighten the bound by 4.
- The Crab bound needs no composition assumption. It excludes S-m on **all of Run 100's ladder** (its lowest point is 2.2×10⁸; at a = 0.1 the bound is ≲ 1.3×10⁸). Of the record-allowed range, only 4×10⁵ ≲ p_s ≲ 1.3×10⁷ survives it.
- The UHECR rows exclude S-m on the **whole record-allowed range**, but only if the flux near the suppression is protonic. Auger's composition data favour heavier primaries, and Maccione et al. treat nuclei as Lorentz-invariant.
- **The band edge** (E_max = √12 ħc/ℓ; Fly's Eye proton p_s < 1.7×10¹⁶, iron 5.3×10¹⁹) is the weakest probe and is superseded (log §6).
- **Matter-only variant** (S-m without S-γ): Lorentz-invariant photons decay to e⁺e⁻ once αE⁴ > 16m_e². LHAASO's ~1.4 PeV photons then need p_s ≲ 1.9–5.6×10⁹. This is an own estimate that cuts the upper intermittent windows.
- **Hughes–Drever and SME tests** of cubic anisotropy in nuclei would also bear on S-m. They were not computed.

#### 4.4 Vacuum Cherenkov (rests on an assumption contrary to R6)
If photons carried the term and electrons did not, electrons above E_th = (12/S)^{1/4}√(m_e ħc/ℓ) would radiate. LHAASO's 1.1 PeV Crab photons imply electrons of 1 PeV or more, which gives p_s ≲ 4.5×10⁸–1.4×10⁹ (conservative, since about 2 PeV electrons are needed). R6 and S-m put matter on the same footing as light. A shared term gives no threshold.
- **Grade: rests on an assumption contrary to R6 and to the borrowed Lorentz input.** It is reported only because it coincides with Run 100's lowest window. Not recommended.

#### 4.5 Improved through a² (n = 4): the residual
If patterns and light are relativistic through a², as Run 90 finds for gravitons, the leading term is α₄p⁶. **No published n = 4 (p⁶, dimension-8) bound was found in the sources consulted**: Auger stops at n = 2, LHAASO at n = 2, Gagnon and Moore (Phys. Rev. D 70, 065002 (2004)) at dimension 6, and LMS's general-n form has an explicit result only for p⁴. Own estimates with the same methods, using α₄ = ℓ⁴S₆/90:
| estimate (n = 4) | p_s < (a = 1), S₆ = ⅑ … 1 | bites on Run 100's ladder? |
|---|---|---|
| photon time of flight, LHAASO sensitivity scaled to 10 TeV (coefficient 1) | ~2×10²² (uncertain by a factor of several) | no |
| Crab synchrotron, ω_c-maximum criterion, γ_req = 3.1×10⁹: γ⁻² ≃ m²/E² + 5α₄E⁴, maximum at E⁶ = m²/(17.5α₄) | 7.2×10¹⁶ … 2.4×10¹⁶ (1.2×10¹⁷ at S₆ = ⅑ with the compact stencil's 1/240) | cuts the continuous band above ~2×10¹⁶–7×10¹⁶ |
| GZK shift equal to the threshold scale at 5×10¹⁹ eV (protons) | 2.5×10⁷ … 8×10⁶ | whole ladder, if protonic |

- An a²-improved term on photons alone bites on nothing. On matter, own estimates still bite: the Crab cuts the top of the band, and protonic UHECR would exclude the ladder.
- 1/90 is the 5-point stencil's coefficient. The compact stencil gives 1/240, and other improvements give other values, possibly of the other sign or zero. Bounds scale as c₄^(−1/2). The engine's improved stencil, if one is forced, is not known; if the residual is zero these rows mean nothing, and if it is superluminal vacuum Cherenkov bounds apply instead.
- All n = 4 rows assume continuous time: with a leapfrog step, spatial improvement leaves a superluminal −σ²/12 n = 2 term, E² = m² + p² + (σ²ℓ²/12)p⁴ (at σ = 0.1, PeV electrons would give p_s ≲ 1.5×10¹⁰; `checkI11b` log §G). That applies only if the engine tick is physical, which R4 denies.
- **Grade: needs S-m plus an improvement statement; own estimates, not published limits.**

#### 4.6 Gravitational-wave dispersion (in the record, superseded, useless)
Run 84's s⁴ term with the GWTC-3 bound |A₄| ≲ 2.7×10³ eV⁻² (90%; value not re-verified) gives ℓ ≲ 4–6×10⁻⁵ m. Run 90 removes the s⁴ term through a². **Grade: from the record (Run 84), superseded; no constraint.**

#### 4.7 Length conditions and data that do not apply
| condition | ℓ < | p_s < (a = 1) | grade |
|---|---|---|---|
| Note I §5: hop well below r_C ≥ 0.09 μm | 9×10⁻⁸ m | 3×10⁵⁵ | from the record; weak |
| short-range gravity (lattice Green function at ≲ 10 μm) | ~10⁻⁵ m | ~4×10⁵⁹ | derived; weak |
| hop sub-nuclear (1 fm) | 10⁻¹⁵ m | 3.7×10³⁹ | not a record statement; weaker than §3 |
| hop below ħ/(m_pc) | 2.1×10⁻¹⁶ m | 1.6×10³⁸ | new statement; weaker than §3 |

- **Birefringence.** The engine's light is a scalar wave with no polarisation structure on the lattice. The bounds above are polarisation-averaged.
- **Photon decay γ → e⁺e⁻** needs superluminal photons. The lattice term is subluminal only for continuous time or σ² < S.
- **Unused because too small:** atom interferometers, photon–photon scattering, the CMB and the GW speed all have (kℓ)² < 10⁻⁴⁰.

### 5. Finding
1. **A plain (unimproved) lattice dispersion shared by matter (S-m)** is excluded on all of Run 100's ladder by the Crab synchrotron (LMS 2012, 95% CL: p_s ≲ 1.3×10⁷ at S = ⅓, a = 1); on the record range only 4×10⁵ ≲ p_s ≲ 1.3×10⁷ survives, and none if the UHECR flux near the suppression is protonic (Maccione et al. 2009, 99% CL, at the edge of their simulated range; p_s ≲ 0.04). **Auger's hadronic bound does not apply:** its sign statement is the n = 0 one, and the number is a rescaling (§4.0).
2. **Photons alone (S-γ)** would bound p_s ≲ 1.1×10¹⁶ (a = 1, S = ⅓, continuous time) by LHAASO's time of flight, cutting Run 100's continuous band to 1.3×10¹²–1.1×10¹⁶. In Auger's subdominant-proton scenario they are excluded over the whole record-allowed range (p_s < 0.5); Auger's reference scenario gives no photon constraint.
3. **So the engine's lattice cannot be a physical, unimproved dispersion for patterns** on Run 100's ladder, and on the whole record range with a protonic UHECR flux. This agrees with the Lorentz invariance the record borrows (R7, R8) and with Run 90's logic, which points to improvement through a² for anything sharing the constraint algebra (an inference; not computed).
4. **Improved through a² (n = 4)** (continuous time; coefficient depends on the stencil): no published bound was found in the sources consulted. Photon time of flight does not bite (~2×10²²). Own estimates for matter still bite: the Crab gives p_s ≲ 2×10¹⁶–7×10¹⁶ (1/90 stencil), cutting the top of the continuous band, and a protonic GZK gives ≲ 10⁷. So improvement through a² does not by itself free the line from LIV bounds if patterns carry the residual. Improvement to higher order, or a hop that is not a physical length for patterns, would.
5. **Therefore the record's only upper bound remains p_s ≲ 1.1×10³⁰/a (1.7×10³⁰/a on the self term; ℓ ≲ 1.7–2.2×10⁻²⁰ m).** S-γ and S-m are excluded or contrary to borrowed inputs, so the data above do not yield a bound on CO as recorded. The link from saturation to p_s stays fitted.
6. **Time discretisation:** every lattice bound above assumes continuous time or σ ≪ 1. At σ² = ⅓ the n = 2 body-diagonal term vanishes, and at σ = 1 the axis term vanishes and the diagonal turns superluminal.
7. **On P08's hop** none of this bounds p_s.

### 6. Choices for a ruling
1. **Plain lattice term for patterns:** record that it is excluded on all of Run 100's ladder by the Crab synchrotron (LMS 2012, 95% CL: p_s ≲ 1.3×10⁷ at S = ⅓, a = 1); on the record range only 4×10⁵ ≲ p_s ≲ 1.3×10⁷ survives, and none if the UHECR flux near the suppression is protonic (Maccione et al. 2009, 99% CL, at the edge of their simulated range). Record also that this bounds a statement CO does not make, since the record borrows Lorentz invariance (R7, R8), and that an a²-improved residual is constrained only by own estimates that depend on the stencil and assume continuous time (§4.5).
2. **No upper bound beyond ~10³⁰:** record that no upper bound on p_s beyond p_s ≲ 1.1×10³⁰/a (self term 1.7×10³⁰/a) follows from the record. The ONTOLOGY inputs row for p_s gains that bound with its grade and source (Reading I10 §3, Run 57, Run 96), and the minimal line stays fitted through p_s. This is compatible with choice 1, not an alternative to it: choice 1 concerns a statement outside the record, choice 2 the record as it stands.
3. **Run 90-type closure calculation for a matter field:** decide whether to register one, in continuous time, with the sign and the size of the a⁴ residual as explicit outputs. Run 90's reading of the boost relation applies to matter's share of the same constraints, so the record's logic points to improvement through a², but the calculation has not been run. The size decides whether §4.5's residual bites; the sign decides which bounds apply (subluminal: the Crab and UHECR rows of §4.5; superluminal: vacuum Cherenkov and photon decay; zero: none).
4. **Vacuum Cherenkov (§4.4):** set aside as contrary to R6 and to the borrowed Lorentz input, recording that its p_s ≲ 10⁹ coincides with Run 100's low window and carries no weight.


### 7. Rulings (29 October; Allen: "yes to both as you recommend")
1. **A plain lattice term for patterns is recorded as excluded** on all of Run 100's ladder by the Crab synchrotron (p_s ≲ 1.3×10⁷ at S = ⅓, a = 1), and entirely if the UHECR flux near the suppression is protonic. It bounds a statement CO does not make, since the record borrows Lorentz invariance (R7, R8).
2. **No upper bound on p_s beyond p_s ≲ 1.1×10³⁰/a follows from the record** (self term 1.7×10³⁰/a). The ONTOLOGY inputs row for p_s carries it. The engine-hop minimal line stays fitted through p_s.
3. **A Run 90-type closure calculation for a matter field is to be registered,** in continuous time, with the sign and size of the a⁴ residual as outputs.
4. **Vacuum Cherenkov is set aside** as contrary to R6 and the borrowed Lorentz input.

### Sources
- Pierre Auger Collaboration, "Testing effects of Lorentz invariance violation in the propagation of astroparticles with the Pierre Auger Observatory", *JCAP* 01 (2022) 023; [arXiv:2112.06773](https://arxiv.org/abs/2112.06773). Eq. 2.2, Eq. 6.3, §5–6 as quoted in §4.0.
- T. Jacobson, S. Liberati, D. Mattingly, "A strong astrophysical constraint on the violation of special relativity by quantum gravity", *Nature* 424, 1019 (2003); [astro-ph/0212190](https://arxiv.org/pdf/astro-ph/0212190).
- S. Liberati, L. Maccione, T. P. Sotiriou, "Scale hierarchy in Hořava–Lifshitz gravity: a strong constraint from synchrotron radiation in the Crab nebula", *Phys. Rev. Lett.* 109, 151602 (2012); [arXiv:1207.0670](https://www.arxiv.org/pdf/1207.0670). Journal reference from standard listings.
- L. Maccione, A. M. Taylor, D. M. Mattingly, S. Liberati, "Planck-scale Lorentz violation constrained by ultra-high-energy cosmic rays", *JCAP* 04 (2009) 022; [arXiv:0902.1756](https://www.arxiv.org/pdf/0902.1756). Journal reference from standard listings; the summary bound was read from an extracted text, and the typeset equation should be checked.
- O. Gagnon, G. D. Moore, "Limits on Lorentz violation from the highest energy cosmic rays", *Phys. Rev. D* 70, 065002 (2004); [hep-ph/0404196](https://arxiv.org/pdf/hep-ph/0404196). Consulted for the absence of n = 4 bounds; its dimension-6 bounds are flavour-by-flavour, parton-level, and not used; they would bear on CO only if nucleons are composites of lattice-carrying constituents.
- LHAASO Collaboration (Z. Cao et al.), *Phys. Rev. Lett.* 133, 071501 (2024); [arXiv:2402.06009](https://arxiv.org/abs/2402.06009). E_QG,2 > 6.9×10¹¹ GeV (subluminal, 95%).
- V. Vasileiou et al., *Phys. Rev. D* 87, 122001 (2013); [arXiv:1305.3463](https://arxiv.org/abs/1305.3463). E_QG,2 > 1.3×10¹¹ GeV, subluminal, GRB 090510.
- MAGIC Collaboration, *Phys. Rev. Lett.* 125, 021301 (2020); [arXiv:2001.09728](https://arxiv.org/abs/2001.09728) (quotes H.E.S.S. Mrk 501). H.E.S.S. (A. Abramowski et al.), *Astropart. Phys.* 34, 738 (2011); [arXiv:1101.3650](https://arxiv.org/abs/1101.3650). Normalisations not re-verified.
- LIGO–Virgo–KAGRA, [arXiv:2112.06861](https://arxiv.org/abs/2112.06861); rescaled in [arXiv:2511.00497](https://arxiv.org/abs/2511.00497). Not re-verified.
- Fly's Eye (Bird et al. 1995); Telescope Array "Amaterasu" (*Science* 382, 903, 2023); LHAASO Crab (*Science* 373, 425, 2021).

*Note (30 October): P∞ ≳ 6.4×10¹⁰ was p_s's bound times the pulsar triple's ratio bound; with ε = 0 in gravity the ratio bound and this figure lapse (Reading I17). What remains is p_s ≳ 4×10⁵ (conditional), p_s ≲ 1.1×10³⁰/a, and Run 96's a·P∞ ≳ 5.25×10²⁶ from route (b).*
