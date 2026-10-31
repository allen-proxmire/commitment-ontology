## Reading I18b: R1's second-order clock departure, against data

*30 October 2026. DRAFT v2, revised after an independent check (`checkI18b/REPORT.md`). Its corrections are adopted; the pre-check version is `reading_I18b_v1_precheck.md`. Written in answer to Reading I18's ruling: "Candidate 3's second-order clock departure is to be checked against data." A reading of the record, plus one short calculation (`i18b_clock.py`; numbers in `i18b_clock.log` and `i18b_clock.json`; the pre-check log is kept as `i18b_clock_v1_precheck.log`), compared with published results fetched for this reading. Not a registered test. It encodes no new rule. **Inference** marks a step past what the record or a source says. **New statement** marks a proposal that would need a ruling.*

**In plain terms.** Candidate 3 puts the vacuum below R1's crossover (ε_med = p_s/P∞ ≳ 1). There R1's outflow is close to linear in P, not logarithmic. If R1 and R3 both held exactly, the clock would be linear in the potential (N → 1 − U) instead of GR's exponential (n = e^{−U}). The two agree at first order and differ by εU²/[2(1+ε)] at second.

The rulings do not make this departure physical:
- R11 as ruled (with Reading I17 §2) takes the medium's count to be P = P∞n, which is GR's lapse exactly.
- The I18 ruling holds H1 only at first order.

As ruled, then, R1, R3 and P = P∞n cannot all hold exactly once ε_med is not small, and the record does not say which gives way at O(ε_med U²).

**Reading A** keeps R1 and R3 exactly and lets everything read R1's clock. That is H1 extended to all orders. It reverses the ε = 0 ruling (ε_g = ε_med) and R11, and brings back a zero-clock surface and horn outside the horizon. Data would exclude candidate 3 under A by at least four orders of magnitude.

The two readings that fit the rulings, C (amend R1, with a stated low-P cutoff) and E (hold R3's linearity only at first order), have no clock departure at all. So no clock datum bears on candidate 3. Candidate 3 survives under either, but only on a new statement, and it is no longer a joint prediction tying ρ_K to κ_b. The 30 October note that p_s is bounded only below stands under C and E.

---

### 1. What the departure is

**The law, if R1 and R3 held exactly** (the record: I18 §2 and the I18 check's ERROR 2; algebra on R1–R3 and Run 66 §2).
- R1 linearised at the vacuum gives δN = (1 + ε)δz/c_o.
- Under H1, first-order matching to Newton's potential sets the medium's mean-field variable to φ_med = U/(1 + ε). Here U = −ln n is GR's potential, and φ_med is kept distinct from R9's φ, which equals U at ε = 0 (ONTOLOGY). This agrees with Run 67's Kepler mass M_K = (1+ε)m.
- If φ_med is harmonic on γ̃ exactly (R3, Run 66 §2), it is proportional to U outside a spherical body (**inference**: two harmonic functions with the same falloff and source shape). Then
$$
N_{\rm R1}(n)=(1+\varepsilon)\,n^{1/(1+\varepsilon)}-\varepsilon
=1-U+\frac{U^2}{2(1+\varepsilon)}-\dots,\qquad n=e^{-U}=1-U+\frac{U^2}{2}-\dots
$$
$$
\frac{N_{\rm R1}}{n}-1=-\frac{\varepsilon\,U^2}{2(1+\varepsilon)}+O(U^3),\qquad \lim_{\varepsilon\to\infty}N_{\rm R1}=1-U .
$$
- U = Φ + Φ³/12 in isotropic coordinates, so this is ERROR 2's form at O(Φ²).
- **Size.** The departure is a fraction ε/(1+ε) of the U²/2 term: half of it (U²/4) at ε_med = 1, and all of it as ε_med → ∞.
  - *Record correction:* Reading I18 §2 ("a fraction up to ½ of the Φ²/2 term") and row 3′ ("¼ of Φ²/2") each understate it by a factor of 2.
  - The I18 check's "that fraction tends to ½" meant the coefficient of Φ², which is the likely source of the slip.
- **Not the same as I17's excluded alternative.** That reading kept φ = U unrescaled, which gives N = (1+ε)n − ε and departs at first order.

**The rules as ruled are inconsistent at this order** (the check's ERROR 1; algebra).
- R11 (ruled 30 October; Reading I17 §2) takes P = P∞n, so possibility runs out at r = 2m, and the 2p_s surface sits at about 2m(1 + 4ε_med²).
- Put P = P∞e^{−U} into R1's outflow, z = c ln(1 + n/ε_med). It is then not harmonic in U:
$$
\frac{d^2z/dU^2}{-\,dz/dU}=\frac{\varepsilon_{\rm med}}{\varepsilon_{\rm med}+n},
$$
  which is ε/(1+ε) at the vacuum. It is checked numerically in `i18b_clock.log` (for example 0.5000 at ε = 1, U = 0; 0.9919 at ε = 100, U = 0.2).
- So R1 exact, R3 exact and P = P∞n (with R2 and R6, universal coupling) are mutually inconsistent at O(ε_med U²), unless ε_med = 0.
- The I18 ruling holds H1 "at first order". As ruled, the record fixes the lapse response only at first order and does not say which of R1, R3 or P = P∞n gives way beyond it.

**The observable, under a reading where the departure is physical, is coordinate-independent.** For identical static clocks at areal radius R_s and at infinity, compared by light in a stationary field:
$$
\frac{\nu_\infty}{\nu_s}\Big|_{\rm CO}=N_{\rm R1}(n_s),\qquad \frac{\nu_\infty}{\nu_s}\Big|_{\rm GR}=n_s,\qquad \frac{\rm CO}{\rm GR}=(1+\varepsilon)\,n_s^{-\varepsilon/(1+\varepsilon)}-\varepsilon\,n_s^{-1}.
$$
- n_s comes from the orbital mass m and the circumference, both measured without clocks.
- Between two finite potentials, the response to an added δU is
$$
\frac{e^{-U/(1+\varepsilon)}}{N_{\rm R1}}=1+\alpha_{\rm eff},\qquad \alpha_{\rm eff}\simeq\frac{\varepsilon\,U_{\rm bg}}{1+\varepsilon},
$$
  which is the redshift parameter α of Gravity Probe A and Galileo, evaluated at the clocks' background potential.

**The readings.** Each names what gives way beyond first order under H1.

| reading | what gives way | clock departure | kind | status |
|---|---|---|---|---|
| **A** | R11's P = P∞n (and the ε = 0 ruling): R1 and R3 exact, so all matter reads N_R1 | yes: the matter metric is g₀₀ = −N_R1² | a metric effect; coupling universal, but to a lapse-dependent matter metric (I15b §5's class C1b) | H1 at all orders. **Contradicts R11 as ruled, I17's ruling 1(i), the ε = 0 ruling and the I18 ruling's "at first order".** P = 0 returns at n₀ = (ε/(1+ε))^{1+ε} ≈ ε, outside GR's horizon (r₀ − 2m ≈ 2mε²), with Run 67's horn |
| **B** | universal coupling: clocks read N_R1, while light, rulers and free fall read n | yes: a redshift anomaly | an EEP violation, LPI-type, the same for every species | new statement; breaks I15 §6.1's premise |
| **C** | R1: amended to a pure logarithm above a stated low-P cutoff p_c | none | – | new statement (R1 is added and provisional; its stated job, β = 1, GR now does) |
| **D** | R2: no clock reads the count | none observable | – | new statement; I17 §2 rejected it as breaking R2 |
| **E** | R3's exact linearity (or the medium's hopping on γ̃) holds only at first order; R1, R2 and P = P∞n kept | none | – | new statement (R3 is listed as derived); the literal reading of the I18 ruling's "at first order" |
| **H2** | R3's draw field no longer sets the lapse at all (I18 §2) | none | – | declined by the I18 ruling; listed for completeness |

**Reading A is ε in gravity.** This restates Reading I15b §5: CO's static sector is GR with matter on a metric that depends on the foliation's lapse.
- Squaring gives g₀₀ = −N_R1² = −1 + 2U − [(2+ε)/(1+ε)]U² + …, so β − 1 = −ε/[2(1+ε)]. That is I15 §6.2's g₀₀ term.
- With the matter metric taken as −N_R1²dt² + N_R1⁻²γ̃_GR (an assumption A needs), A agrees with Run 67's ε-exterior at first post-Newtonian order: the same M_K = (1+ε)m, γ = 1, β and K₂ = −ε(1+ε)m² (the check).
- It differs at the next order, h₂ = −2ε(1+ε)m² against Run 67's −(4ε + 3ε²)m². The reason is that A's γ̃ is curved by the stress of U = (1+ε)φ_med, which is neither of R9's two choices.
- **Its SEP violation.** A states no energy functional. Matter in equilibrium on N_R1 does not conserve stress-energy on GR's metric, so A would have to be written as a lapse-coupled theory before Δ is even defined. That Run 66's Δ ≈ εC carries over at leading order in ε is an **inference**; Δ = εC/(1+ε) exactly is not shown.

**Reading B** violates the Einstein equivalence principle (**inference**, from the standard decomposition, Will 2014). Clocks against light or rulers is LPI failing. Matter against light is a position-dependent failure of LLI. Because R2 treats every species alike, clock-comparison tests between species see nothing; only clock-against-metric tests do. Two further points:
- Under R8 (action −m∫dτ), a pulsar's spin is motion, not "matter counting its own commitments" (R2). So under B the spin follows n unless R2 is extended to rotation.
- Note D point 4's G tie uses δN = δP/P∞, so D needs R2 at first order and not at second.

### 2. Against data (readings A and B only; C, D, E and H2 have no clock departure)

Columns: U at the clock; the predicted departure at ε_med = 1, as ε_med → ∞, and in general form; the measured precision; whether it constrains ε_med (2σ). Rows 1–7 are reading B, rows 8–11 reading A. Numbers are from `i18b_clock.log` and the check.

| # | test | U | ε_med = 1 | ε_med → ∞ | general ε | measured | constrains ε_med? |
|---|---|---|---|---|---|---|---|
| 1 | Gravity Probe A, first-order redshift | 7.0×10⁻¹⁰ (ground) | α_eff: 8.5×10⁻⁷ (Galaxy in U_bg); 5.8×10⁻⁶ (with ~10⁻⁵ from large-scale structure) | 1.7×10⁻⁶ / 1.2×10⁻⁵ | εU_bg/(1+ε) | α < 1.4×10⁻⁴ (Vessot et al. 1980, as quoted in Will 2014; not fetched here) | **no** |
| 2 | Galileo 5/6, eccentric orbits | 1.6×10⁻¹⁰ (orbit) to 7.0×10⁻¹⁰ (ground) | as row 1 | as row 1 | as row 1 | α = (0.19 ± 2.48)×10⁻⁵ (Delva et al. 2018) | **no**: short by ×4.4 (U_bg with large-scale structure) or ×30 (Galaxy only) |
| 2′ | the same, from Earth's own U alone | 7.0×10⁻¹⁰ | 3.5×10⁻¹⁰ | 7.0×10⁻¹⁰ | εU_⊕/(1+ε) | 2σ 5.2×10⁻⁵ | **no** (short by ~7×10⁴) |
| 3 | ACES (ISS against ground) | 6–7×10⁻¹⁰ | as row 1 | as row 1 | as row 1 | projected 2–3×10⁻⁶ after 20 days (Cacciapuoti et al. 2024, pre-launch); no redshift result found | **possibly**, through α_eff, if U_bg ≳ 3×10⁻⁶ (**inference**: U_bg depends on where the vacuum P∞ is defined) |
| 4 | solar redshift (HARPS laser comb) | 2.12×10⁻⁶ | δz/z = 5.3×10⁻⁷ (0.34 mm/s) | 1.06×10⁻⁶ (0.67 mm/s) | ≈ εU/[2(1+ε)] | 638 ± 6 m/s against 633.1 (González Hernández et al. 2020) | **no** (short by ~10⁴) |
| 5 | Sirius B (HST/STIS) | 2.69×10⁻⁴ | 6.7×10⁻⁵ (5 m/s) | 1.35×10⁻⁴ (11 m/s) | ≈ εU/[2(1+ε)] | 80.65 ± 0.77 km/s, agreeing with the astrometric mass and radius (Joyce et al. 2018) | **no** (short by ~1.4×10²) |
| 6 | neutron-star surface, m/R = 0.2 | 0.255 | clock −1.9%; z = 0.315 against GR's 0.291 (+8.4%) | clock −3.9%; z = 0.343 (+18%) | N_R1(n_s)/n_s − 1 | **no secure measurement**: EXO 0748−676's lines were not confirmed; compactness comes from model-dependent atmosphere fits (review, arXiv:1303.0317) | **no: untested** |
| 7 | double pulsar, Einstein delay γ_E (PSR J0737−3039A, m/R = 0.165 at R = 12 km) | U_A = 0.200 (self) × U_ext | γ_E +7.9% | +16.8% | f[e^{−U_A/(1+ε)}/N_R1(U_A) − 1], f = M/(m_A + 2m_B) = 0.674; = f ε(e^{U_A} − 1) = 0.149ε at small ε, → fU_A/(1 − U_A) = 0.168 | 0.384045(94) ms (Kramer et al. 2021); GR from Table IV's masses and the 2021 P_b and e: 0.383997 ms, obs/GR = 1.000126 ± 0.00024 | ε_med ≲ 4.1×10⁻³ (central value plus 2σ; the offset lies in the direction of the effect), **only if R2 is extended to a body's rotation**. As written, probably not binding under B (§1) |
| 8 | (A) perihelia and ephemerides, MESSENGER | – | β − 1 = −¼ | −½ | −ε/[2(1+ε)] | β − 1 = (−1.6 ± 1.8)×10⁻⁵ (Genova et al. 2018) | ε_med ≲ 1.0×10⁻⁴ |
| 9 | (A) Nordtvedt effect, lunar laser ranging | – | η = −1 | −2 | −2ε/(1+ε) from β alone; A's α₁ and α₂ would add −α₁ + ⅔α₂ | η = (−0.2 ± 1.1)×10⁻⁴ (Müller et al., ILRS 2023 workshop); MESSENGER (−6.6 ± 7.2)×10⁻⁵ | ε_med ≲ 1.2×10⁻⁴ (static part) |
| 10 | (A) pulsar triple, Run 66's Δ (leading order in ε, an inference for A) | ~0.2 (self) | Δ ≈ 0.2 | Δ ≈ 0.4 | ≈ εC, C = 0.375–0.442 | \|Δ\| < 2.3×10⁻⁶ (Voisin et al. 2025, via Run 66) | ε_med ≲ 5.2–6.1×10⁻⁶ |
| 11 | (A) preferred-frame α₁, α₂ and two-cone timing | – | not computed for A | – | for the record's lapse-coupled completion (T-I15d): α₁ ≈ −16ε, α₂ ≈ −2ε, γ_GW − γ_EM = −2ε/(1+ε) | T-I15d's bounds: ε ≲ 2.5×10⁻⁶ (α₁), 1.3×10⁻⁷ (two-cone), 8×10⁻¹⁰ (α₂) | needed for A. If A's completion has α's of O(ε), its bound tightens by up to ~10⁴. A's field-equation metric carries the Kepler mass, which I15b says removes the two-cone offset at first post-Newtonian order |
| 12 | clock-comparison LPI tests (Yb⁺ against Cs, annual solar potential) | ΔU_⊙ ≈ 3.3×10⁻¹⁰ | 0 (the same for every species, under A or B) | 0 | 0 | (c²/α)dα/dΦ = 14(11)×10⁻⁹ (Lange et al. 2021) | **no** |
| 13 | (I17's unrescaled alternative, for comparison) | first order | α = 1 | – | α = ε | Galileo | ε ≲ 5×10⁻⁵ |

**Notes on the table.**
- **U_bg.** Earth and Sun contribute 1.06×10⁻⁸. The Galaxy adds about 1.7×10⁻⁶, from an escape speed of 550 km/s. Large-scale structure may add of order 10⁻⁵. Both of the latter are **inference**.
- **Reading B's shortfalls.** Across rows 1–5, at ε_med → ∞, B falls short of the data by about ×4 (Galileo, if large-scale structure counts in U_bg) up to about 4×10⁵ (Earth's own potential, at Gravity Probe A; ~7×10⁴ at Galileo, row 2′).
- **Row 7's masses** come from the post-Keplerian parameters (mass function plus Shapiro shape), so the comparison is not circular (the check).
- **Under A the bound returns as a gravity bound** on ε_g = ε_med. With a·P∞ ≲ 1.78×10³⁵, rows 8–10 give a·p_s ≲ 1.1×10³⁰ (from 1.78×10³⁵/1.63×10⁵), and row 11 would push it to about 1.4×10²⁶ if its α's are of O(ε). That is a reversal of the ε = 0 ruling, not a medium-side addition to it.

### 3. What follows for candidate 3

**By reading.**
- **A: excluded, but A itself contradicts the rulings.**
  - Candidate 3 needs ε_med ≳ 1, against ≲ 10⁻⁴ (β, η) and ≲ 5–6×10⁻⁶ (the pulsar triple) from static tests alone.
  - The bound could fall to about 10⁻⁹ if A's completion has T-I15d's O(ε) α₂ (not computed for A).
  - Under A, h/p_s ≥ 0.999994, so candidate 2 cannot be told apart from candidate 1. The wall, min(p_s, P∞) ≲ 5.6×10²⁷ aK² on route (c), is then tighter than the restored 1.1×10³⁰/a (the check).
- **B: untested in practice.**
  - The direct redshift tests fall short by about ×4 (Galileo, if large-scale structure counts in U_bg) up to about 4×10⁵ (Earth's own potential, at Gravity Probe A).
  - Neutron-star surfaces (8–18% in z) have no clean measurement.
  - The double pulsar binds (ε_med ≲ 4×10⁻³) only if R2 is extended to rotation.
  - B breaks universal coupling, the premise of I15 §6.1.
- **C: no clock departure; candidate 3 survives as a fitted stipulation.** By algebra (this restates Run 66's check, points 4 and 6: an exponential clock with a field harmonic on γ̃ is exactly GR):
  - with z harmonic and P = P∞e^{−U}, every spherical vacuum harmonic function is a + bU, so z = z∞ + B ln(P/P∞) on the range of P the exterior reaches;
  - under R11 that range runs down to P = 0 at r = 2m, where a pure logarithm goes to −∞ and turns negative, which an outflow cannot do (R1 has f(0) = 0). So C needs a stated low-P cutoff p_c, which is a crossover again;
  - the engine's slope then ties B to p_c (Note D), and the vacuum sits above that crossover;
  - candidate 3's h = P∞ needs B set by hand to c_o/(1 + ε_med), so it is **fitted**, with B as the free number;
  - R5's g = dU/dφ − 1 becomes constant under C, so R5's g ≈ p_s/P is amended too.
- **D:** rejected in I17 §2 (it breaks R2).
- **E: no clock departure; candidate 3 survives on an amended derived rule.**
  - R1, R2 and P = P∞n are kept. R3's exact linearity holds only at first order.
  - The hop relation ℓ² = (0.99πa/3)ℓ_P²h, h = (1/p_s + 1/P∞)⁻¹, stands for any ε_med, so candidate 3's tie of ρ_K to κ_b stands as stated.
  - The price is that the non-harmonicity ε_med/(ε_med + n) is not small: at ε_med ≫ 1 it is the whole U²/2 term. R3, listed as derived, then holds only at first order.
- **H2:** declined. Under it candidates 1–3 lose their link to p_s and κ_b (I18 §2).

**Verdict.** No clock datum bears on candidate 3 under the readings consistent with the rulings (C, E). The readings that give a clock departure (A, B) contradict the rulings or their premise. A would exclude candidate 3; B is untested in practice. Under C or E, candidate 3:
- rests on a new statement: a fitted B under C, an amended derived rule under E;
- survives the data, with I18's existing window (r_C ≳ 48 μm, within ×1.1 of the relic-neutrino bound on κ_b);
- is no longer a joint prediction tying ρ_K to κ_b, since under C the tie is put in by hand, and under E it holds only because R3 is amended.

The same holds for row 3′ (ε_med = 1), with the A and B departures halved.

**What the universal-coupling objection amounts to.**
- With universal coupling and ε = 0 in gravity, the ruled clock is P/P∞ = n at all orders (R11, I17 §2).
- R1's crossover then cannot sit in an exactly linear field–clock relation. Something other than the clock must give way: R1 under C, or R3's exactness under E.
- Exact compatibility of R1, R3 and P = P∞n holds only at ε_med = 0, or with C or E stated. Approximate compatibility holds wherever ε_med is below what data can see, which, absent A, is any value.
- Giving up universal coupling instead (B) gives up I15 §6.1's route to GR.

### 4. Choices for a ruling

1. **Which rule gives way beyond first order under H1:**
   - (a) **C**: amend R1 to f = A + B ln P above a stated low-P cutoff p_c, and amend R5's g accordingly. Candidate 3 is then **fitted** (B set by hand).
   - (b) **E**: R3's exact linearity holds only at first order; R1, R2 and P = P∞n are kept. Candidate 3 then stands as stated, on an amended derived rule (**new statement**).
   - (c) Leave open.

   A (reverses the ε = 0 ruling and R11), B (breaks universal coupling) and D (breaks R2) are recorded as rejected; H2 stays declined.
2. **Candidate 3 and 3′:** grade under 1(a) or 1(b). Either way it rests on a new statement and is recorded as no longer a joint prediction tying ρ_K to κ_b. No present clock datum constrains it.
3. **Record corrections** (dated notes):
   - Reading I18 §2: "a fraction up to ½ of the Φ²/2 term" should read "a fraction ε/(1+ε) of the Φ²/2 term, all of it as ε_med → ∞".
   - Reading I18 row 3′: "¼ of Φ²/2" should read "½ of Φ²/2 (U²/4)".
   - The I18 check's ERROR 2: "that fraction tends to ½" should read "its coefficient tends to ½".
   - ONTOLOGY's R3 line ("β − 1 = −ε/[2(1+ε)], ε = p_s/P∞") and the inputs row for R9: a dated note separating ε_g (zero, ruled) from ε_med.
4. **The p_s upper bound:** the 30 October notes ("p_s is bounded only below") stand under C and E. They change only if A is ruled, which would be a reversal of the ε = 0 ruling.

### Recommended next steps
1. Rule on choice 1 (C or E), then grade candidate 3 under it (choice 2).
2. If C: state p_c and what fixes B, and re-read Runs 23–24's clock universality, R5's g and R11's 2p_s surface with the cutoff in place.
3. If E: state the order to which R3 holds, and record what the medium does at O(ε_med U²), so that "derived" is not claimed for R3 beyond first order.
4. Write the dated notes in choice 3.
5. If A is ever reconsidered: state it as a lapse-coupled action (I15b §5, class C1b), compute its α₁ and α₂ before quoting any p_s bound, and revise rows 8–11.

### Sources
**Record (read).**
- `quantum/reading_I18_fixing_rhoK.md` (§2, §3 rows 3/3′, ruling); `checkI18/REPORT.md` (ERROR 2, items 6 and 8); `checkI18b/REPORT.md` (adopted);
- `ONTOLOGY.md` (R1–R3, R5, R6, R8, R9, R11, "ε in gravity is zero", inputs table);
- `gravity/reading_I17_black_holes.md` §2 (P = P∞n; the excluded alternative); `gravity/reading_I15_borrowed_inputs.md` (§6.1, §6.2, §9, rulings and notes of 30 October); `gravity/reading_I15b_cuscuton.md` (§3 class C1b, §5); `gravity/test_I15d_section.md` (α₁, α₂, two-cone);
- `gravity/run66_section.md` (and its check, points 4 and 6), `run66b_medium_section.md` (Note E), `run67_section.md`.

**Data (fetched for this reading).**
- P. Delva et al., *PRL* 121, 231101 (2018), [arXiv:1812.03711](https://arxiv.org/pdf/1812.03711.pdf).
- L. Cacciapuoti et al., "Atomic Clock Ensemble in Space" (2024), [arXiv:2411.02912](https://arxiv.org/pdf/2411.02912).
- J. I. González Hernández et al., *A&A* 643, A146 (2020), [arXiv:2009.10558](https://arxiv.org/abs/2009.10558).
- S. R. G. Joyce et al., *MNRAS* 481, 2361 (2018), [arXiv:1809.01240](https://arxiv.org/pdf/1809.01240).
- Review of neutron-star X-ray constraints (2013), [arXiv:1303.0317](https://arxiv.org/pdf/1303.0317).
- M. Kramer et al., *PRX* 11, 041050 (2021), [NSF PAR copy](https://par.nsf.gov/servlets/purl/10321815).
- A. Genova et al., *Nat. Commun.* 9, 289 (2018), [MIT DSpace](https://dspace.mit.edu/handle/1721.1/118777).
- J. Müller et al., LLR results, ILRS workshop 2023, [slides](https://ilrs.dgfi.tum.de/lw23/docs/presentations/S03/S03-03_LLR-ILRS-WS2023JM_Jurgen_presentation.pdf).
- R. Lange et al., *PRL* 126, 011102 (2021), [record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_2480257650).
- A. Fienga et al., [arXiv:1409.4932](https://ar5iv.arxiv.org/html/1409.4932): ephemeris β, consistent with Genova et al. and not used in the table.

**Not fetched.** Gravity Probe A (Vessot et al. 1980), via Will 2014; Voisin et al. 2025, via Run 66.

*Files in this folder: `reading_I18b_DRAFT.md` (this reading, v2); `reading_I18b_v1_precheck.md`; `i18b_clock.py`, `i18b_clock.log`, `i18b_clock.json` (v2: 2021 P_b and e, central-plus-2σ convention, non-harmonicity check); `i18b_clock_v1_precheck.log`.*

### Ruling (30 October 2026)

Allen: "do as you recommend." **Choice 1, C:** R1 is amended beyond first order. Above a stated low-P cutoff p_c the outflow is a pure logarithm, f = A + B ln P, so R3's linear field, R2's clock and R11's P = P∞n hold together at all orders. p_c and what fixes B are to be stated. **Choice 2:** candidate 3 is graded fitted (B set by hand); it is no longer a joint prediction. p_s stays bounded only from below.
