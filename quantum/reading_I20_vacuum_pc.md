## Reading I20: can the quantum vacuum fix the medium's crossover p_c?

*31 October 2026. Allen: "Look for a principled source of p_c outside the current record, for example from how CO's medium relates to the quantum vacuum." A reading of the record, plus outside physics and arithmetic (`i20_numbers.py`; numbers in `i20_numbers.log`). Not a registered test; it encodes no new rule. Revised after one independent check, whose corrections are adopted. **Inference** marks a step past what the record or the literature says; **new statement** marks a proposal that would need a ruling.*

**In plain terms.** Three kinds of outside tie were tried, and none fixes p_c.
- **Area laws** (horizon entropy, one unit per Planck area). The engine-hop relation already makes p_c per hop area Planckian for every p_c, so counting p_c that way says nothing. Counting what a vacuum place actually holds, P∞, ties p_c to P∞, which is also free.
- **Counts** (Sakharov's induced gravity, Dvali's species bound). These have the same form as the relation, with p_c in the place of the number of vacuum species. If G were wholly induced at the hop by the Standard Model, p_c would be too small by ×28–4400, excluded by clocks. A larger hidden sector moves the free number to that sector's size.
- **Lengths** (known energy scales). The window runs from about 4×10¹⁶ GeV down to 160 TeV. Dark energy and the electroweak scale fall outside it, as do string and Planck scales. The GUT and inflation scales sit at the clock floor, and the seesaw and Peccei–Quinn scales sit inside. Nothing in CO picks one.

### 1. The relation being tied
Reading I18's boxed form (H1, first order), with h = p_c (I18c ruling 1):
$$
\ell^2=k\,a\,\ell_P^2\,p_c,\qquad k=\frac{0.99\pi}{3}=1.037 .
$$
It came from making the medium's lapse response reproduce G: each place's response to a draw is ∝ 1/c_o ≈ 1/(0.99 p_c), so
$$
G=\frac{\ell^2c^3}{k\,a\,\hbar\,p_c}.
$$
Read at fixed ℓ, G is small because the response per draw is small, by a factor 1/p_c (a reading of the relation; in I18 §2 the hop is derived from the measured G, and the record does not explain G). G is a measured input (ONTOLOGY.md inputs table).

**The window** (Reading I19 §1, a = K = 1), with E ≡ ħc/ℓ:

| bound | p_c | ℓ/ℓ_P | E (GeV) |
|---|---|---|---|
| clock floor through B / through p | 8×10⁴ / 4×10⁵ | 290 / 640 | 4.2×10¹⁶ / 1.9×10¹⁶ |
| Run 104's own fit (extrapolation) | 1.0×10⁶ | 1000 | 1.2×10¹⁶ |
| boost cap on p_c (I19 candidate) | 2.9×10¹⁸–1.2×10²³ | 1.7×10⁹–3.5×10¹¹ | 7×10⁹–3.5×10⁷ |
| interference wall | 5.6×10²⁷ aK² | 7.6×10¹³ | 1.6×10⁵ |

Reading a length as an energy has a 2π ambiguity (ℓ = ħc/E or 2πħc/E), which moves p_c by ×39 and the window to 2.7×10¹⁷ GeV – 1.0×10⁶ GeV. It is carried through §3–§4.

### 2. Area laws: inert, or a tie to P∞
R1 holds P∞ per place far from matter; p_c is the crossover, with p_c < P∞. Three area counts follow.

| count | statement | result | grade |
|---|---|---|---|
| p_c per hop area | p_c/ℓ² = 1/(k a ℓ_P²) for every p_c | an identity of the engine-hop relation; holds whatever p_c is | **inert** (derived) |
| P∞ per hop area, s nats per unit, set to Bekenstein–Hawking | sP∞/ℓ² = 1/(4ℓ_P²) ⇒ ε_c = p_c/P∞ = 4s/(ka) | a = 1: ε_c = 3.86 (1 nat), 2.67 (ln 2), against p_c < P∞, **excluded**. a = 2π: ε_c = 0.61 or 0.43, allowed (below n ≈ 0.77 at neutron-star surfaces). It ties p_c to P∞, which stays free | Reading I19 row 5′, extended to entropy s; **new statement** |
| one place per Planck area | ℓ = ℓ_P | p_c = 0.97 or 0.15 | **excluded** (I19 row 1, Note D) |

These cover Bekenstein–Hawking entropy and entanglement area laws (Bombelli et al.; Srednicki). That each unit at a horizon carries a fixed entropy s is itself a new statement.

### 3. Counts: Sakharov and Dvali (new statement; inference on its form)
**The outside result.**
- Sakharov's induced gravity gives 1/G ∝ str[k₁] κ²: N vacuum species with cutoff κ = 1/ℓ make G weak (Visser 2002, Eq. 29).
- Dvali's bound (2007) gives M_P² ≳ N Λ², that is ℓ² ≳ c_N N ℓ_P². The convention constant c_N is taken as 1/(2π) (Visser's prefactor), 1, or 8π (the bound read with the reduced Planck mass).

**The tie.** CO's 1/G ∝ p_c/ℓ² has the same form, with p_c in N's place. Saturating Dvali's bound, or taking G as wholly induced at the hop:
$$
p_c=\frac{c_N\,N}{k\,a}.
$$
Reading p_c, a place's crossover and the engine's hop (I19 row 3b), as the vacuum's species count is a **new statement**. The record gives no basis for it beyond the matching form.

**Results** (`i20_numbers.log`):
- **Dvali's inequality alone is inert:** it gives p_c ≳ c_N N/(ka), which for the Standard Model (≤ 2900) the clock floor already exceeds.
- **The Standard Model as the whole count, with G wholly induced at the hop** (the equality). N = 118 (28 bosonic and 90 fermionic degrees of freedom) gives p_c = 18–2900 over c_N ∈ {1, 8π} and a ∈ {1, 2π}, short of the clock floor of 8×10⁴ by ×28–4400 (×4400–28000 at c_N = 1/2π). **Excluded**, conditional on the equality and on Reading I6 ruling 4. Spin weights do not rescue it: per-field k₁ has magnitude ≤ 2/3 per state, bosons and fermions enter the supertrace with opposite signs, and Kabat's gauge-field contact terms are negative (Visser, Table 1), so weighting lowers or cancels the count of 118.
- **A hidden sector of N ≈ 3.3×10³–2.3×10²⁹ species** (over c_N ∈ {1, 8π}, a ∈ {1, 2π}; 8×10⁴–6×10²⁷ at c_N = a = 1) lands inside the window, with the free number moved to N. Nothing in CO counts species.
- **Dvali's large-N solution to the hierarchy problem** (Λ ≈ 1 TeV, N ≈ 1.5×10³²) gives p_c ≈ 1.4×10³². That lies above the wall unless aK ≳ 160 (≳ 1000 with 2π). It is **excluded at a = K = 1**, conditional on route (c) with Γ_K = c/r_C.
- **If the tie held, ℓ would be the scale where gravity becomes strong** (species scale; inference from Dvali). The record does not say whether CO's hop plays that role.

### 4. Lengths: vacuum energy scales (new statements)
p_c = (M_P/E)²/(ka), with M_P = 1.22×10¹⁹ GeV, at a = 1; the 2π column takes ℓ = 2πħc/E.

| scale | E (GeV) | p_c (a = 1) | with 2π | status |
|---|---|---|---|---|
| dark energy, ρ_Λ^{1/4} | 2.3×10⁻¹² | 2.8×10⁶¹ | 1.1×10⁶³ | **excluded**: above P∞'s ceiling (1.8×10³⁵/a) and the wall. CO's R5 also rules that the undisturbed vacuum draws nothing, so the tie has no ground |
| holographic dark energy, √(M_P H₀), non-reduced M_P (reduced: 1.9×10⁻¹², p_c 4.1×10⁶¹) | 4.2×10⁻¹² | 8.2×10⁶⁰ | 3.2×10⁶² | **excluded**, as above |
| electroweak, v | 246 | 2.4×10³³ | 9.4×10³⁴ | **excluded at a = K = 1** by the wall; allowed only if aK ≳ 650 (≳ 4100 with 2π) |
| Peccei–Quinn, f_a | 10⁹–10¹² | 1.4×10²⁰–1.4×10¹⁴ | ×39 | inside the window; f_a not measured. Under the I19 boost-cap candidate only the low end (1.4×10²⁰) survives |
| seesaw, M_R | 10¹⁴–10¹⁵ | 1.4×10¹⁰–1.4×10⁸ | ×39 | inside; M_R not measured. Below the I19 boost-cap candidate |
| inflation, H_inf < 4.7×10¹³ (r < 0.036) | bound | ≳ 6.5×10¹⁰ | ≳ 2.6×10¹² | floor only |
| inflation, V^{1/4} < 1.4×10¹⁶ | bound | ≳ 7.3×10⁵ | ≳ 2.9×10⁷ | floor only, within Run 104's 1σ band |
| GUT (SUSY unification) | ≈ 2×10¹⁶ | 3.6×10⁵ | 1.4×10⁷ | **at the clock floor**: above 8×10⁴, just below 4×10⁵ and Run 104's fit (1σ 3.9×10⁵–2.7×10⁶); at a = 2π (5.7×10⁴) below every floor |

**What this shows.**
- The window runs from about 4×10¹⁶ GeV down to 160 TeV in energy, about eleven decades (2.7×10¹⁷ GeV – 1 PeV under the 2π reading).
- Proposed scales between those ends fall inside it; string and near-Planck scales lie above it. CO has no rule that ties the hop to one sector of the vacuum, so choosing a scale chooses p_c.
- The GUT case is the only one that lands on an edge. It does not fix p_c. The GUT scale is itself model-dependent, the 2π ambiguity spans ×39, and Run 104 cannot yet tell 8×10⁴ from 4×10⁵.

### 5. Finding
**Nothing outside the record fixes p_c.**
- **Area laws.**
  - The p_c count is an identity (inert).
  - The P∞ count ties p_c to P∞ (I19 row 5′ with entropy s; excluded at a = 1, allowed at a = 2π).
  - One place per Planck area stays excluded.
- **The species tie** is the one outside principle with the relation's form.
  - As an inequality it is inert.
  - As an equality it excludes the Standard Model as the whole count, and excludes Dvali's TeV solution at a = K = 1.
  - Any other N moves the free number to that sector's size.
- **Vacuum energy scales.**
  - Dark energy and the electroweak scale are excluded (the electroweak one at a = K = 1).
  - Inflation gives floors only.
  - The GUT scale sits at the clock floor.
  - Seesaw and Peccei–Quinn lie inside the window as it stands. CO chooses none of them.

### 6. Choices for a ruling
1. **Record the finding:** no outside tie fixes p_c; area laws are inert or move the number to P∞. *A reading.*
2. **The species tie:**
   - (a) record it as a candidate (the equality form), with the Standard Model-only and Dvali-TeV cases excluded;
   - (b) set it aside.
3. **The GUT coincidence:** record it as a reading, not a candidate, since the 2π ambiguity and Run 104's unresolved floor leave it untestable as a value.

### Sources
- A. D. Sakharov (1967); M. Visser, [arXiv:gr-qc/0204062](https://arxiv.org/abs/gr-qc/0204062) (Eq. 29, Table 1); D. Kabat, [arXiv:hep-th/9503016](https://arxiv.org/abs/hep-th/9503016).
- G. Dvali, [arXiv:0706.2050](https://arxiv.org/abs/0706.2050).
- L. Bombelli, R. Koul, J. Lee and R. Sorkin, Phys. Rev. D 34, 373 (1986); M. Srednicki, [arXiv:hep-th/9303048](https://arxiv.org/abs/hep-th/9303048).
- BICEP/Keck 2021, r < 0.036 ([arXiv:2110.00483](https://arxiv.org/abs/2110.00483)); Planck 2018 (Ω_Λ, H₀).
- The record: Reading I18 §2 (the boxed relation and its source); Reading I18c ruling 1; Reading I19 §1–§2 (rows 1, 3b, 5′); Note D (`gravity/reading_P0ps_section.md`); `gravity/run104_section.md`; ONTOLOGY.md (inputs; R5).

### Ruling (30 October 2026)

Allen: "do as you recommend."
1. **No outside tie fixes p_c** (recorded). Area laws are inert or move the number to P∞.
2. **The species tie, in its equality form, is kept as a candidate.** Its Standard Model-only and Dvali-TeV cases are excluded.
3. **The GUT coincidence is recorded as a reading,** not a candidate.

Saturation's onset map stands as a description with one free number.

*Note, 31 October: Run 105 reads THROUGH B, so the clock floor is 8×10⁴. The GUT case (p_c ≈ 3.6×10⁵) lies above it, though inside the engine's own 1σ bound (4.2×10⁵–2.4×10⁶) only at its edge; it stays a reading (`gravity/run105_section.md`).*
