## Reading I19: what could fix the medium's crossover p_c

*31 October 2026. DRAFT v2, revised after an independent check (`/home/claude/checkI19/`). Its corrections are adopted. The pre-check version is `reading_I19_v1_precheck.md`. A reading of the record, plus arithmetic (`i19_numbers.py`; numbers in `i19_numbers.log`). Not a registered test. It encodes no new rule. **Inference** marks a step past what the record says; **new statement** marks a proposal that would need a ruling.*

**In plain terms.** Route (c)'s onset map becomes a prediction once one number is fixed: the medium's crossover p_c. This number also sets the engine's hop. The record bounds p_c from both sides but fixes it nowhere. Every tie examined below does one of three things: it is excluded by clocks; it gives only a floor; or it moves the free number from p_c to P∞, which is also free. One new statement would require p_c to carry Reading I14's boost cap, P_e ≳ 12γ². That would raise the floor by about thirteen to seventeen decades. LISA-type and X-ray windows would then lie below the allowed range, and the test would pass to molecular interferometry with clusters of about 10⁷–10⁹ Da, enough to shut the window completely. The cap is a required cap, not a data exclusion, and the statement still gives a window, not a value.

### 1. The record as it stands
- **R1, amended** (Reading I18c ruling 1): f = 0.99P below p_c, f = A + B ln P above, with B = 0.99 p_c, A = 0.99 p_c(1 − ln p_c), and p_c ≡ (1/p_s + 1/P∞)⁻¹. The engine's hop is h = p_c.
- **The engine-hop relation** (Reading I18 ruling, H1; first order):
$$
\ell^2=\frac{0.99\pi a}{3}\,\ell_P^2\,p_c\quad\Longleftrightarrow\quad p_c=\frac{3}{0.99\pi a}\Big(\frac{\ell}{\ell_P}\Big)^2 .
$$
- **The window:**
  - **From clocks:** p_c ≳ 8×10⁴ through B, or 4×10⁵ through p (both kept, Run 104 UNRESOLVED). Run 104's own fit reaches gap 10⁻⁶ at p_c ≈ 1.0×10⁶ (1σ 3.9×10⁵–2.7×10⁶), an extrapolation (inference). All three are conditional on Reading I6 ruling 4.
  - **From the interference wall:** p_c ≲ 5.60×10²⁷ aK², conditional on route (c) with Γ_K = c/r_C.
  - **From C's domain:** p_c < P∞ ≲ 1.78×10³⁵/a (a reading). It is conditional on the a in κ_b = 1/(aP∞) being the hop line's a (I18c ruling 4).
  - **From route (b):** a·P∞ ≳ 2.5–5×10²⁷ (Run 96, addendum 2, B16-NR).
- **In hop units** (a = 1) the window runs from ℓ ≈ 290–1000 ℓ_P to 7.6×10¹³ ℓ_P (1.2×10⁻²¹ m).
- **Note D, reading 1:** the corpus has no per-place budget and no crossover, and the amendment adds no tie (Reading I18c §3).

### 2. The candidates

| # | statement | formula | gives | in the window? | grade |
|---|---|---|---|---|---|
| 1 | hop = Planck length (P08, P-G-Closure) | ℓ = ℓ_P ⇒ p_c = 3/(0.99πa) | 0.97 (a = 1); 0.15 (a = 2π) | no: below the clock floor by ≥ 8×10⁴. At a = 1 Run 104's measured gap covers it (0.069 at p_c = 1). At a = 2π, p_c = 0.15 lies below every measured point, so that case rests on extrapolation (I18c cites Run 24) | **excluded** (Note D; I18c 2.2′) |
| 2 | draw per renewal ~ p_c (Note D point 4, the "natural carrier") | S ~ p_c per renewal | G per pair order one, ℓ ~ ℓ_P | no: it restores the order-one self-dip that the crossover removes | **excluded** (Note D) |
| 3a | units per commitment (I14, (P1)–(P3)), with P_e read as P∞ (C1a, K = P∞) | P∞ ≳ 12γ² | P∞ ≳ 1.1×10²⁰–1.2×10²³ | weaker than route (b)'s a·P∞ ≳ 2.5×10²⁷ for a ≲ 2×10⁴ | **inert** for p_c |
| 3b | the cap carried by p_c, with K = 1 (I18 row 6). This sits between C1a and C1b: p_c is a place's crossover and the engine's hop, not a pattern's released stock | p_c ≳ 12γ² | **p_c ≳ 1.1×10²⁰** (Crab electrons, γ ≈ 3×10⁹) to **1.2×10²³** (UHE protons, γ ≈ 10¹¹); hop ≳ 1.1×10¹⁰–3.5×10¹¹ ℓ_P | yes, as a floor: it leaves [1.1×10²⁰–1.2×10²³, 5.6×10²⁷aK²] | **new statement**; floor only, not a value; a required cap, not a data exclusion |
| 3c | C1b (I14: the cap is the outflow per tick), under amended R1 | f(P∞) = 0.99p_c(1 − ln ε_c) ≳ 12γ² ⇒ p_c ≳ 12γ²/[0.99(1 − ln ε_c)] | Crab: 1.1×10²⁰ (ε_c → 1) down to 2.9×10¹⁸ (ε_c = 10⁻¹⁶). UHE: 1.2×10²³ down to 3.2×10²¹ | yes, as a floor that depends on ε_c | **inference** on an open choice (I14 choice 1; I14 notes that (P1) favours C1a). I14's "12c" carried original R1's ln(P∞/p_s), which has lapsed |
| 4 | p_c = P∞/n, n structural | p_c = ε_c P∞, ε_c = 1/n = p_s/(p_s + P∞) | n = 2 (p_s = P∞): a·p_c ≳ 1.25–2.5×10²⁷, under the wall by ×2.2–4.5 (a = K = 1) | yes, but only as I18's 3′: r_C ≳ 34 μm, κ_b within about ×2 of the B16-NR cap. At ε_c = ½ the shell below p_c reaches 8m/3 (I18c 2.3′) | **new statement**; it moves the free number to P∞; nearly closed (I18) |
| 5 | hop as "a typical spacing set by the local count" (I13 ruling 3) with the engine relation | ℓ = ℓ(P) while ℓ² ∝ p_c | no number. A scaleless substrate gives a count per region, not a length, and I18 row 9 holds ℓ at vacuum values inside matter | – | **inert** |
| 5′ | 5 plus a count per Planck cell (new) | area, one unit per ℓ_P² (Paper_025's capacity): ℓ² = P∞ℓ_P² ⇒ ε_c = 3/(0.99πa). Volume, ℓ³ = P∞ℓ_P³ ⇒ p_c = (3/0.99πa)P∞^{2/3} | area: ε_c = 0.97 (a = 1), 0.15 (a = 2π). Volume: p_c ≈ 1.8×10¹⁸ – 3×10²³ (a = 1) | area at a = 1: no. ε_c lies above the lapse at neutron-star surfaces (n ≈ 0.77), against C's stated condition. Area at a = 2π and the volume form: yes | **new statement**; ties p_c to P∞, which stays free; no basis in the record for either count |
| 6 | ħ_t | H = 2ħ_t P∞; light crosses ħ_t hops per hold | P∞ cancels through H (Note D); C1a gives ħ_t = V_c/2ℓ³ | – | **inert**: no tie to p_c |

**Which quantity takes P_e.** I18 row 5 already applied the cap to the capacity K, with K ≳ 12γ², and found it inert in the laboratory (ρ_K ≥ 2.7×10⁶ kg m⁻³). Row 3b gives the cap to p_c and keeps K = 1. If K took the cap as well, the wall would move as 5.6×10²⁷aK², up by K² ≳ 10⁴⁰. It would then lie above P∞'s ceiling, and the binding upper bound would become p_c < P∞.

**Finding.** Nothing in the record fixes p_c. Rows 1–2 are excluded, rows 3a, 5 and 6 are inert, and rows 3b, 3c, 4 and 5′ are new statements. Rows 3b and 3c give floors only; rows 4 and 5′ hand the free number to P∞.

### 3. The single statement that would fix it, and what would test it
A value for p_c needs one new statement that gives ℓ/ℓ_P, or ε_c together with a measured P∞. A measured P∞ would mean a route-(b) detection, since κ_b = 1/(aP∞). No structural count in the record supplies either. The nearest natural statement is row 3b. It gives a floor, not a value, but it moves the testable range.
- **Without 3b** (I18's near-zone numbers, a = K = 1):
  - LISA-type acceleration noise: an ASD ×1.0015 better tests p_c ≈ 1.2×10¹⁵; ×3.2 clears every point bound by LISA Pathfinder (1.26×10¹² – ~2×10²¹).
  - X-ray limits: natural Ge ×1.14 tests p_c ≈ 4×10¹¹; XENONnT about 15% tighter tests 4.8×10⁸; enriched Ge ×1.5–7.2 tests 3×10⁹–1.6×10¹⁰.
  - Each of these tests only the p_c it reaches, not the line.
- **With 3b** (p_c ≳ 1.1×10²⁰–1.2×10²³, K = 1): every X-ray window, and most or all of the LISA band, would be excluded if 3(a) were ruled. This is a required cap, not a data exclusion. What remains rests on criterion E (atmosphere) and on Vinante-type force noise (F, binding up to about 6×10²¹). The sharp test becomes the wall.
  - The wall moves with cluster mass M as
$$
h_{\rm wall}(M)=\frac{3}{0.99\pi}\Big(\frac{m_P}{M}\Big)^2aK^2 .
$$
  - Interference with clusters of M ≈ 3.7×10⁷ Da (×216 the present 172 kDa) would reach p_c = 1.2×10²³. M ≈ 1.2×10⁹ Da would reach 1.1×10²⁰. At these masses the wall meets the floor, so the window shuts completely.
  - The M⁻² scaling follows from N_cell = M/m_N (checked). That heavier clusters cover all 49 r_C, as 172 kDa does, is an **inference** and has not been registered.

### 4. Choices for a ruling
1. **Record the finding:** nothing in the record fixes p_c. The engine-hop line stays a family with one free number, inside 10⁵–10⁶ ≲ p_c ≲ 5.6×10²⁷aK² and p_c < P∞. *A restatement of Note D's reading 1 and of I18c §3.*
2. **Rows 1–2:** record as excluded. **Rows 3a, 5 and 6:** record as inert for p_c.
3. **Row 3b:**
   - (a) adopt P_e = p_c with K = 1 as a new statement, raising the floor to about 10²⁰–10²³ and making cluster interferometry the test;
   - (b) record it as a candidate;
   - (c) set it aside. Row 3c follows I14's open choice 1.
4. **Rows 4 and 5′:** record as moving the free number to P∞, with no basis in the record; row 4 stays nearly closed through I18's 3′.

### Recommended next steps
1. Rule on choice 3. It is the only option that changes which experiments bear on p_c.
2. If 3(a) or 3(b): register the moving wall (h_wall ∝ M⁻² on Run 99's 49 r_C) before computing it, with M from 10⁶ to 10¹⁰ Da and a ∈ {1, 2π}.
3. Keep Run 104's p_c = 1 discrimination (more seeds) on the list. It decides whether the clock floor is 8×10⁴ or 4×10⁵, but not p_c itself.
4. If 3(a) is ruled, state with it whether K also takes the cap. If it does, the wall moves up by about 10⁴⁰ and the cluster test lapses.

### Sources (read)
`ONTOLOGY.md` (R1 and its amendment; inputs table); `quantum/reading_I18_fixing_rhoK.md` (§2–§4, ruling); `quantum/reading_I18c_cutoff.md` (§2–§3, rulings); `gravity/run104_section.md`; `gravity/reading_P0ps_section.md` (Note D, points 1–4); `quantum/reading_I14_grid_free.md` ((P1)–(P3), ruling); `quantum/reading_I13_bounded_ledger.md` (§9, ruling 3); `quantum/run96_section.md` (addendum 2, the a·P∞ line only). Check: `/home/claude/checkI19/` (adopted).

### Ruling (30 October 2026)

Allen: "do as you recommend." Nothing in the record fixes p_c (recorded). The boost cap applied to p_c (p_c ≳ 12γ²/[0.99(1 − ln ε_c)], 2.9×10¹⁸–1.2×10²³) is kept as a **candidate**, not adopted: it goes past Reading I14, and it would remove most of saturation's testable map on a requirement rather than data. If it is ever adopted, the test to register is the moving interference wall, h_wall = 3/(0.99π)(m_P/M)², for cluster masses M from 10⁶ to 10¹⁰ Da.

*Note, 31 October: Run 105 reads THROUGH B; the clock floor is 8×10⁴ and the 4×10⁵ figure lapses (`gravity/run105_section.md`).*
