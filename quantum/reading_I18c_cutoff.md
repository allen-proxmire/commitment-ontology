## Reading I18c: the cutoff p_c and the constants of R1's amended outflow

*30 October 2026. DRAFT v2, revised after an independent check (`checkI18c/REPORT.md`: 3 errors, 8 imprecisions). All its corrections are adopted. The pre-check version is `reading_I18c_v1_precheck.md`. Written in answer to Reading I18b's ruling (choice 1, C): "p_c and what fixes B are to be stated." A reading of the record, plus one short calculation on Run 35's zero-range measure (`i18c_outflow.py`; numbers in `i18c_outflow.log` and `i18c_outflow.json`; the pre-check outputs are kept as `*_v1_precheck.*`). Not a registered test. It encodes no new rule. **Inference** marks a step past what the record says. **New statement** marks a proposal that would need a ruling.*

**In plain terms.** The amendment keeps R1's logarithm and drops the "1 +" inside it above a cutoff p_c. What the record already fixes:
- R2 and R11 do not constrain B, because the clock reads only differences of the field (a restatement of I18b §3 C).
- The additive constant A drops out in mean field.
- If R1's words "linear below the crossover" are kept, with the engine's one-unit hop chance 0.99 and a smooth join, then B = 0.99 p_c, and the engine's hop is h = p_c.

**What p_c is called is a choice the record does not make.** Above the cutoff, p_s has no other role.
- Naming p_c ≡ (1/p_s + 1/P∞)⁻¹ keeps Reading I18's ruled first-order hop exactly, and keeps the amendment inside its stated scope, "beyond first order".
- Naming p_c ≡ p_s gives Note D's form instead, which changes the ruled first-order hop by 1 + ε_med.

Either way the physical content is the same: h = p_c < P∞, and nothing fixes p_c.

**What changes under the amendment:**
- R5's g is zero in mean field, so every result built on g ≈ p_s/P, or on R1's curvature, is null. Most of these had already lapsed as gravity results.
- R11's surface keeps its form.
- The quantum sector's engine-hop line reads p_c where it read p_s.
- Runs 23–24's clock-universality bound depends on which variable carries it. Through B it is p_c ≳ 8×10⁴, against the record's 4×10⁵ through p_s. A short rerun under the amended rule would settle which.

**Open:**
- what holds below p_c, in a thin shell outside each horizon;
- whether "pure logarithm" describes each place's outflow or the medium's equation of state. In the record's exact measure, the first leaves a small finite-count residual, which is derived here.

---

### 1. The constants

**The original rule and its large-P form** (R1; Note D point 4; Run 23):
$$
f(P)=c\,\ln\!\Big(1+\frac{P}{p_s}\Big)=c\ln P-c\ln p_s+\frac{c\,p_s}{P}-\dots,\qquad c=\frac{0.99}{\ln(1+1/p_s)}=0.99\big(p_s+\tfrac12\big)+O(p_s^{-1}).
$$
The 0.99 is the engine's base hop chance: c is set so that f(1) = 0.99 (`zrp35.py`).

**The amended rule** (the ruling): f = A + B ln P for P > p_c.

**What R2 and R11 require of B: nothing.** This restates I18b §3 C, bullet 1, its check (item 7), and Run 66's check point 4. In mean field, with the medium hopping on γ̃ (Run 66 §2; never run, Run 66's check point 5):
$$
N=\frac{P}{P_\infty}=\exp\!\Big(\frac{z-z_\infty}{B}\Big),\qquad U\equiv-\ln N=\frac{z_\infty-z}{B}.
$$
- R3 makes z harmonic, so U is harmonic and P = P∞n holds, for every B (mean field, medium on γ̃; not run).
- A cancels in z − z∞.
- B enters only the field's strength per unit of draw: Note D's U = (6/c)G_lat∗s becomes U = (6/B)G_lat∗s. So B is fixed only through the G tie, where it trades against the hop (2.4).
- That a pure logarithm needs a cutoff, and that the vacuum sits above it, restates I18b §3 C, bullets 2 and 3.

**What fixes B: the join at p_c.** The ruling states no rule below the cutoff. The joins the record's wording allows (log §3, §6):

| join | below p_c | at p_c | B | A | free numbers |
|---|---|---|---|---|---|
| **Cb** | f = 0.99P (R1's "linear below the crossover"; f(1) = 0.99 as in the engine) | value and slope continuous | **0.99 p_c** | 0.99 p_c(1 − ln p_c) | one: p_c |
| **Ca** | R1 itself, c ln(1 + P/p_s) | value continuous; slope jumps by 1 + p_s/p_c | **c** | −c ln p_s + c ln(1 + p_s/p_c) | two: p_s and p_c = Kp_s |
| **Ca, smooth** | R1 itself | value and slope continuous | **cK/(1 + K)** = c p_c/(p_s + p_c) | fixed by the value join | two: p_s and p_c = Kp_s. At p_c = P∞ this is I18b's candidate-3 value c_o/(1 + ε_med) |
| **asymptote** | f = kP | – | c | −c ln p_s exactly | f = 0 at P = p_s. A linear branch meets it only if k ≤ c/(e p_s) ≈ 0.36–0.53, smoothly at p_c = e·p_s. The engine's branch, k = 0.99, cannot meet it: 0.99 p_c = c ln(p_c/p_s) has no solution |

- **Under Cb**, B/c = p ln(1 + 1/p) = 1 − 1/(2p) + … at equal crossover p (0.99999875 at p = 4×10⁵). A differs from −c ln p_s by about c.
- **A is inert in mean field.** In the exact measure it shifts the finite-count residual (§1.2) by −(A − A_Cb)/(2BP), which is equally inert for data. The small Ca/Cb differences in the exact measure are this A-dependence. They are not an effect of the region below p_c, which carries negligible weight at P = 16p_c (the check, item 4).
- **The asymptote row.** The pure asymptote, B = c with A = −c ln p_s, keeps the engine's f(1) = 0.99 only if it is joined to R1 itself (Ca). A linear branch of slope c/(e p_s) gives up f(1) = 0.99.

**Answer to question (1).** In substance yes: the pure logarithm is R1's large-P form, with B = c up to the join, and matching R2 and R11 forces no other B. But p_c "playing p_s's role" is a naming choice (2.4), and the amendment does more than change P ≲ p_c (§1.1).

#### 1.1 What the "1 +" did above the crossover
Under the original rule the outflow is curved at every P, by the fraction p_s/(p_s + P) (I18b §1):
$$
\frac{d\ln P}{dz}=\frac{1}{c}\Big(1+\frac{p_s}{P}\Big),\qquad \frac{d^2z/dU^2}{-dz/dU}=\frac{\varepsilon_{\rm med}}{\varepsilon_{\rm med}+n}.
$$
That curvature is the source of every ε_med factor in the record's weak-field and far-field results:
- R5's g = p_s/P;
- the clock departure εU²/[2(1+ε)];
- β − 1 = −ε/[2(1+ε)];
- Δ = εC/(1+ε);
- M_K = (1+ε)m;
- the first-order (1 + ε) in I18 §2's linearisation.

ε_med enters elsewhere as a position, not a curvature:
- R11's surface at n = kε_med;
- Run 43's echo delay ln(1/n_c);
- I17's held-matter factor 1/(8ε_med).

Under C the curvature is zero for P > p_c:
$$
\frac{d\ln P}{dz}=\frac1B,\qquad \frac{d^2z/dU^2}{-dz/dU}=0 .
$$
So every effect of R1's curvature above the cutoff vanishes. The first-order (1 + ε) factor in the hop and the G tie is the exception. It survives or disappears with the naming of p_c (2.4), because at first order it is just a number that p_c can absorb.

#### 1.2 "All orders" in the exact measure
The record's medium is a zero-range process (Run 35). Its fugacity z = ⟨f(n)⟩ is made exactly linear by R3, and the clock reads ⟨P⟩ = R(z). A pure logarithm per place does not make ln R exactly linear in z.

**The residual, derived** at leading order in 1/P (the check, item 5). It uses Var ≈ f/f′ and z = ⟨f⟩ ≈ f + ½f″Var, with Run 52's g = B d ln R/dz − 1 and Run 22's β − 1 = y″/(2y′²), y = ln R:
$$
g\simeq-\frac{f(P)/B-1}{2P},\qquad \beta-1\simeq\frac{f(P)/B-2}{4P},\qquad f=A+B\ln P .
$$
- **Under Cb**, f/B = 1 + ln(P/p_c), so
$$
g\simeq-\frac{\ln(P/p_c)}{2P},\qquad \beta-1\simeq\frac{\ln(P/p_c)-1}{4P}.
$$
- **The same method reproduces Run 55's** g = (p_s − b)/P, b = ½ ln(1 + P/p_s) − ½, for R1. Run 55's −½ is absorbed into A/B.
- **Against the exact measure** (cumulant identities dR/d ln z = Var, dVar/d ln z = κ₃; log §1, §5). The R1 rows also reproduce Run 55's exact form to 2×10⁻⁴ or better, as a code test.

| law | P/p | g exact / formula (p = 256) | β − 1 exact / formula (p = 256) |
|---|---|---|---|
| R1 (original) | 16 / 1024 | 6.23×10⁻² / Run 55: 6.23×10⁻²; 9.65×10⁻⁴ / 9.65×10⁻⁴ | −2.9×10⁻² / −4.8×10⁻⁴ |
| Cb | 16 | −3.384×10⁻⁴ / −3.385×10⁻⁴ | 1.082×10⁻⁴ / 1.082×10⁻⁴ |
| Cb | 1024 | −1.322×10⁻⁵ / −1.322×10⁻⁵ | 5.73×10⁻⁶ / 5.66×10⁻⁶ |
| Cb with A + B | 16 / 1024 | g·P lower by 0.500 at every count | – |

- **Size.** The residual is smaller than R1's by about 2p_c/ln(P/p_c). At the vacuum, |g| ≤ 1/(2e·p_c) = 4.6×10⁻⁷ at p_c = 4×10⁵. Under ε = 0 in gravity it is a property of the medium, not the metric. **Inert.**
- **Sign.** It has the opposite sign to R1's (g < 0, β − 1 > 0), so a medium-side Δ built from it would be negative. **Inert.**
- **A wording point for the ruling:** stated as the medium's equation of state, z = A + B ln⟨P⟩, "at all orders" is exact by construction. Stated per place, as R1 is worded, it is exact in mean field and holds to this residual in the exact measure.

### 2. What the amendment changes

| # | item | before (record) | under C (Cb join unless stated) | grade |
|---|---|---|---|---|
| 2.1 | Runs 23–24, clock universality | self-dip D_self ≈ 6(G₀ + G₁)q·y′ (Run 22), with y′ = (1 + p_s/P)/c; Run 24's gaps fitted against p_s, slope −0.85, giving p_s ≳ 4×10⁵ for 10⁻⁶ | y′ = 1/B exactly. Mapping R1's run at p_s onto Cb at p_c = p_s changes y′ by c/B = 1.443, 1.120, 1.031 (p = 1, 4, 16), outside the gaps' errors. Refitted in the self-dip theory's own variable (log §7), the same gaps scale as 1/c: gap ∝ (c/0.99)^(−1.00 ± 0.08), against p_s^(−0.85 ± 0.06). Carried through B, the bound is **p_c ≳ 8×10⁴**, against 4×10⁵ through p_s. The same reading would apply to the record's own p_s bound under R1. β's part (Run 23's K2) is 1 in mean field under C | **inference**: assumes the gap depends on the medium only through y′; not rerun. Conditional since Reading I6, unchanged |
| 2.2 | R5's g | g = dU/dφ − 1 = p_s/P (Run 66 §2; Run 55's exact (p_s − b)/P) | **g = 0** in mean field (a constant c/B − 1 under any other normalisation of φ, absorbed into G; I18b §3 C, last bullet). In the exact measure, −ln(P/p_c)/(2P) (§1.2). R5's factor (1 + g) becomes inert, rules V and E coincide, and the draw is T, the Tolman/Komar density | **derived** (mean field); **inert** |
| 2.2′ | results that rest on g ≈ p_s/P or on R1's curvature | Runs 55, 57 and 66: Δ = εC/(1+ε). Run 66 point 2, Run 66b and the ONTOLOGY R3 line: β − 1 = −ε/[2(1+ε)], "ε sets every departure". Run 52's V-against-E split, G_eff ∝ (1 + g_bg)² and its ζ₂-like term. Run 55's "the medium is not scale-free". Run 23's K2 (β depends on P₀/p_s). Run 25's β − 1 ≈ −0.45 p_s/P₀ and Nordtvedt P₀/p_s ≳ 2000, with Run 24's "P₀ ≳ 2000p_s ≈ 10⁹" and Run 45's η_N ≈ −1.5p_s/P₀. Run 65 point 6 and Run 67: the near-horizon shell "where g = p_s/P is no longer small", and M_K = (1+ε)m (used by I18b §1 for φ_med = U/(1+ε)). Reading I15b's concordance G_N = (1+ε)²G₀. I18 §2's linearisation δN = (1+ε)δz/c_o. ONTOLOGY R9's N = (1+ε)e^(−φ) − ε. RESULTS.md's row "clocks of different design agree; ζ₂; the pulsar triple" (Runs 23, 24, 30, 45, 48, 55, 57, 66). Note D's P-G-Closure number | under C all are null in the medium: Δ = (1 + ḡ)/(1 + g_bg) − 1 = 0 for constant g; β = 1 in mean field; M_K = m. Most had already lapsed as gravity results with ε = 0 in gravity. Note D's P-G-Closure (ℓ = ℓ_P) needs p_c = 3/(0.99πa) = 0.97 (a = 1) or 0.15 (a = 2π) under Cb, replacing p_s = (e^(0.99πa/3) − 1)⁻¹, and is still excluded by Run 24. Runs 51 and 54 are controlled toy media (g = αp_s/P) and are unaffected. Every entry stands as computed for the original R1 | **derived**; dated notes **needed** (choice 5) |
| 2.3 | R11's surface | P = 2p_s at n = 2ε_med, r ≈ 2m(1 + 4ε_med²) (I17 §2) | P = 2p_c lies above the cutoff, so P = P∞n locates it: n = 2ε_c, r_c = 2m/(1 − 4ε_c²) ≈ 2m(1 + 4ε_c²), ε_c = p_c/P∞. Under Ca with K > 2, the 2p_s surface lies below p_c, where what holds is open (2.3′). I17 graded k **inert**, so nothing rests on it | **reading** |
| 2.3′ | below p_c | – | in the shell n < ε_c, R1's low branch, R3's harmonic field and P = P∞n cannot all hold. R3 is exact by conservation on the engine's lattice (Run 22 T3), so either P = P∞n fails there (a clock departure confined to the shell) or the medium's hopping on curved γ̃ does (Run 66's check point 5). The shell runs from 2m to 2m/(1 − ε_c²), about 2mε_c² thick (log §4: 2×10⁻⁶m at ε_c = 10⁻³; 0.02m at 0.1; 8m/3 at ½; the photon sphere at 0.577). C also needs P∞ > p_c, and ε_c below the smallest lapse inside static matter. A surface at m/R = 0.2 has n = 0.77; a uniform-density star at M/R = 0.246 has central n = 0.57 (the check; realistic equations of state are more centrally condensed, **inference**) | **open**; inert while ε_c ≪ 1 (**inference**) |
| 2.4 | engine-hop relation | ℓ² = (0.99πa/3)ℓ_P²h, h = (1/p_s + 1/P∞)⁻¹ (I18 §2, ruled at first order) | the hop reads the log slope at the vacuum, dz/d ln P = B, so ℓ² = (πa/3)Bℓ_P² and **h = B/0.99**. Under Cb, h = p_c (Ca: c/0.99 ≈ p_s + ½; Ca smooth: cK/[0.99(1 + K)]). It equals I18's ruled first-order form if p_c is identified with (1/p_s + 1/P∞)⁻¹, and Note D's form if p_c is identified with p_s. Above the cutoff p_s has no other role, so the choice is a naming one. Identifying p_c ≡ p_s would change the ruled first-order hop and G tie by 1 + ε_med, outside the amendment's stated scope ("beyond first order") and against the I18 ruling. **The physical content is h < P∞**, I18's cap h ≤ min(p_s, P∞) sharpened, because C's domain needs P∞ > p_c. In the exact measure, slope/B − 1 = 1.3×10⁻⁵ at P/p = 1024, p = 256 | h = B/0.99: **derived**, given Note D's chain; the naming: **open** (choice 1) |
| 2.5 | quantum sector | Reading I10's line ℓ = ℓ_P√(0.99πa p_s/3); Runs 99–100 mapped against p_s; I18's candidates 1–3; the wall min(p_s, P∞) ≲ 5.6×10²⁷aK² | see the bullets after this table | relabel: **reading**; candidate 3: **inference** |

**2.5 in detail.**
- **The line and the map.** The line reads h = p_c where it read p_s, and Runs 99–100's map is unchanged.
- **Candidates 1 and 2 merge,** since h = p_c < P∞.
- **The wall** becomes p_c ≲ 5.6×10²⁷aK², still conditional on route (c) with Γ_K = c/r_C.
- **I11's dispersion bounds** bear on ℓ, so on B.
- **Candidate 3** (h = P∞):
  - under Cb it needs ε_c = 1 and has no room;
  - its ε_c < 1 forms (3′ at ε_c = ½, h = P∞/2) are candidate 2 relabelled, with p_c = ε_c/(aκ_b). The wall condition becomes κ_b ≥ 1.785×10⁻²⁸ε_c/(aK)². These forms are limited by the shell and by the central lapse of static matter (2.3′);
  - under Ca with K < 1, or with B untied, it stays fitted (the I18b ruling).

  Under the naming p_c ≡ (1/p_s + 1/P∞)⁻¹, candidate 3 (p_s ≫ P∞) is the limit ε_c → 1 and 3′ (p_s = P∞) is ε_c = ½.

### 3. Is p_c a new free number, and does anything fix it?

**How many numbers.**
- **Under Cb there is one,** p_c, with B = 0.99p_c. Which older quantity it is named after is choice 1:
  - (1/p_s + 1/P∞)⁻¹, which keeps the I18 ruling;
  - or p_s, which gives Note D's form.

  The count of free medium numbers is unchanged (p_c and P∞). ε_med loses its role as the outflow's curvature and survives as the cutoff's position, ε_c = p_c/P∞ (2.3, 2.3′). **Inference.**
- **Under Ca or Ca smooth there are two:** p_s, which sets B, and p_c = Kp_s, which sets where the log starts. K enters B under the smooth join. **Inference.**
- **With B untied from p_c** (the ruling's wording, "p_c and B are open"), there are again two numbers. B is then a free number, and candidate 3 is **fitted** through it (I18b ruling).

**Nothing fixes it.** This restates Note D's reading 1: the corpus has no per-place budget and no crossover. The amendment adds no tie.

**Bounds.**
- **From below:** p_c ≳ 8×10⁴ through B, or 4×10⁵ through p_s (2.1; **inference**; conditional since Reading I6).
- **From C's domain:** p_c < P∞ ≲ 1.78×10³⁵/a (route (b)'s floor, κ_b = 1/(aP∞)). Under Ca this also gives p_s < P∞/K.
  - It assumes the a in κ_b is the hop line's a (I18 §2, hop-cap bullet).
  - It is a **reading** of I18b §3 C, bullet 3, and its check item 7.
  - It conflicts with "p_s stays bounded only from below". That conflict is already inside I18b, between §3 C and its own choice 4, and so in the I18b ruling.
- **Conditional:** p_c ≲ 5.6×10²⁷aK² under route (c) (2.5).

### 4. Choices for a ruling

1. **The join and the naming of p_c:**
   - (a) **Cb, with p_c ≡ (1/p_s + 1/P∞)⁻¹ (recommended).** f = 0.99P below p_c, a smooth join, B = 0.99p_c, A = 0.99p_c(1 − ln p_c). It keeps the I18 ruling's first-order hop and the amendment's "beyond first order" scope exactly. One number; candidate 3 is the limit ε_c → 1, with no room. *New statement.*
   - (b) Cb with p_c ≡ p_s. Note D's form; it changes the ruled first-order hop by 1 + ε_med, so it needs the I18 ruling amended. *New statement.*
   - (c) Ca or Ca smooth: R1 kept below p_c. Two numbers, p_s and p_c = Kp_s. *New statement.*
   - (d) Leave B untied from p_c. Candidate 3 stays fitted through B.
2. **What the logarithm describes:**
   - (a) each place's outflow, as R1 is worded, so "all orders" holds to the derived residual of §1.2;
   - (b) the medium's equation of state z(⟨P⟩), so it holds exactly.

   Either is inert for data.
3. **Below p_c:** either
   - record as open which rule gives way in the shell n < ε_c (P = P∞n, or the medium on curved γ̃), together with the conditions P∞ > p_c and ε_c below the lapse inside static matter; or
   - state P = P∞n there as part of R11, so that clocks stay GR's everywhere and the medium alone departs.
4. **p_c's upper bound:** whether p_c < P∞ ≲ 1.78×10³⁵/a (with its condition on a) is recorded as a reading of I18b §3 C. If it is, the note "bounded only below" gets a dated qualification, which also resolves I18b's internal conflict (§3 C against choice 4).
5. **Record notes** (dated, under the choice made):
   - ONTOLOGY R1: state p_c, B and A;
   - ONTOLOGY R3 line and R9's N line: these belong to the original R1;
   - R5: g = 0 above p_c;
   - R11: 2p_s → 2p_c, ε_med → ε_c;
   - Reading I18 §2's box, its linearisation and candidates 2–3: h = B/0.99, candidate 2 merges with candidate 1;
   - Note D point 4 and its P-G-Closure number;
   - Run 55's reading 1;
   - Runs 23 (K2), 24, 25 and 45, Run 65 point 6, Run 66b and Run 67, Reading I15b's concordance;
   - the RESULTS.md row;
   - I10, Runs 99–100 and the inputs table: p_s read as p_c;
   - the p_s lower bound: state its variable (2.1).

### Recommended next steps
1. **Rule on choice 1.** Option (a) keeps the I18 ruling and the amendment's scope exactly. Then rule on choices 2–3.
2. **Register the Cb rerun** before running it. Use Run 24's uniform-media design under Cb at p_c = 1, 4, 16. State in advance the question it decides: does the design gap scale with B (slope −1 in c/0.99, giving p_c ≳ 8×10⁴) or with the crossover itself (slope −0.85 in p_s, giving 4×10⁵)? It is the test of 2.1's inference.
3. **Rule on choice 4,** citing I18b's internal conflict.
4. **Write choice 5's notes** in the same session as the ruling, including the variable of the p_s lower bound.
5. **Leave the shell below p_c** (choice 3) on the open list with I17's collapse question. It bears on nothing observable while ε_c ≪ 1.

### Sources (read)
- **Ontology:** `ONTOLOGY.md` (R1 with its amendment note, R2, R3, R5, R9, R11, "ε in gravity is zero", inputs table).
- **Quantum readings:**
  - `quantum/reading_I18b_clock_departure.md` (§1, §3 C bullets 1–3 and last, choice 4, ruling), with `checkI18b/REPORT.md` (item 7);
  - `quantum/reading_I18_fixing_rhoK.md` (§2 box, linearisation and hop cap, H1, §3 candidates 1–3, ruling and note);
  - `quantum/reading_I10_tying_rhoK.md` (ruling 2);
  - `quantum/reading_I11_ps_upper_bound.md`;
  - `quantum/reading_I6_matter_and_pattern.md` (ruling 4);
  - `quantum/run100_section.md`.
- **Gravity readings and runs:**
  - `gravity/reading_P0ps_section.md` (Note D, point 4 and reading 1);
  - `gravity/reading_I17_black_holes.md` (§2, the surface table row);
  - `gravity/run21_section.md`–`run25_section.md` (self-dip theory, Runs 23–24's scaling, Run 22's β formula and T3);
  - `gravity/run52_section.md`, `run54_section.md`, `run55_section.md` (g and Δ);
  - `gravity/run66_section.md` (§2, the check's points 4–6).
  - Cited through the check's item 8, not reopened here: Runs 45, 65 (point 6), 66b, 67, Reading I15b and the RESULTS.md row.
- **Check:** `/home/claude/checkI18c/REPORT.md` (adopted).
- **Code (read-only):** `/home/claude/adopted/zrp35.py`.

*Files in this folder: `reading_I18c_DRAFT.md` (this reading, v2); `reading_I18c_v1_precheck.md`; `i18c_outflow.py`, `i18c_outflow.log`, `i18c_outflow.json` (v2: adds §5, the derived residual against the exact measure; §6, the joins; §7, Runs 23–24's gaps refitted); `i18c_outflow_v1_precheck.log` and `i18c_outflow_v1_precheck.json`.*

### Rulings (30 October 2026)

Allen: "do as you recommend."
1. **(a)** The smooth linear join: f = 0.99P below p_c, f = A + B ln P above, with B = 0.99 p_c, A = 0.99 p_c(1 − ln p_c), and p_c ≡ (1/p_s + 1/P∞)⁻¹. One number; the I18 ruling's first-order hop and the amendment's scope hold exactly; h = p_c.
2. **(b)** The logarithm is the medium's equation of state z(⟨P⟩), so "all orders" holds exactly.
3. **Below p_c** (the shell n < ε_c): open which rule gives way, with the conditions P∞ > p_c and ε_c below the lapse inside static matter.
4. **The upper bound p_c < P∞ ≲ 1.78×10³⁵/a** is recorded as a reading of I18b §3 C, conditional on the a of κ_b = 1/(aP∞) being the hop line's a. "Bounded only below" is qualified accordingly.
5. The record notes are written.

