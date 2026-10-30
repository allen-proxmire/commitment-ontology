## Reading I18: what could fix saturation's threshold density ρ_K now

*30 October 2026. DRAFT v2, revised after an independent check (`checkI18/REPORT.md`). Its corrections are adopted; the pre-check version is `reading_I18_v1_precheck.md`, and its ERROR 3, the stale record notes, is already written back in the repo. Written after the 30 October rulings: ε = 0 in gravity; Q6; Reading I14's (P1)–(P3); Reading I17. A reading of the record, plus arithmetic on Runs 99–100's hashed code, used read-only (`i18_map.py`, `i18_near.py`; numbers in `i18_map.log`, `i18_map.json`, `i18_near.log`). Candidate 3's κ_b window and the wall are the check's (`checkI18/check_i18_4.log`, §4 of the report). Not a registered test. It encodes no new rule. **Inference** marks a step past what the record says; **new statement** marks a proposal that would need a ruling.*

**In plain terms.** Route (c), saturation, makes a definite map of where it could be seen. But the map describes a family, because nothing in the record fixes the threshold density ρ_K. That was the finding of Reading I9, and it still holds with ε = 0 in gravity.

The best tie on record runs ρ_K through the engine's hop, and the hop through p_s. Today's rulings change it in two ways:
- **p_s's upper bound lapses.** It rested on a bound on ε in the metric. p_s is now bounded only below.
- **The hop is capped, under one reading.** The formula tying the hop to p_s is a limit that the old gravity bounds guaranteed. If the medium still sets the slicing's lapse at first order (reading H1), the hop is set by the smaller of p_s and P∞, and route (b)'s floor caps it.

On Runs 99–100's map the extended line keeps points within a factor of ten of present limits up to an exact wall set by cluster interferometry. Beyond the wall nothing survives. The line is still a family indexed by one free number, so no present or near-future experiment can turn it into a prediction without a statement that fixes that number.

One variant would tie ρ_K to route (b)'s rate κ_b: a vacuum below its crossover. It survives only at r_C ≳ 48 μm, within ×1.1 of the ruled relic-neutrino bound on κ_b. It also needs H1 in exactly the regime where H1 makes clocks depart from GR. So it is nearly closed, and it is in tension with the ε = 0 ruling.

### 1. What is fixed and what is free (the record as it stands)
- **Route (c)** (Reading I8, C4-β; Run 98): Π̂ = S((ϱ̂ − ρ_K)/δρ + ½), with δρ = ρ_K/10 and S(s) = 3s² − 2s³. Its rate is **Γ_K = c/r_C** (Reading I9 ruling 2; Run 99).
- **The threshold as a count** (Reading I8 §2):
$$
\rho_K=\frac{K\,a\,\hbar}{2c\,\hbar_t\,\ell^4}\ \xrightarrow{\ \text{C1a: }\hbar_t=V_c/2\ell^3\ }\ \rho_K=\frac{K\,a\,m_\ell}{V_c},\qquad m_\ell=\frac{\hbar}{c\ell},\qquad N_{\rm cell}=\frac{K\,a\,m_\ell}{m_N}.
$$
- **The engine-hop minimal line** (Reading I10 ruling 2): C1a, K = a = 1, ℓ = ℓ_P√(0.99πa p_s/3). Run 100 maps it over p_s = 4×10⁵ to 4.3×10¹⁹. Every p_s keeps laboratory survivors. The near zone (q = Γ_max/Γ_K ≤ 10) is continuous from 1.26×10¹².
- **Bounds after today** (corrected record):
  - p_s ≳ 4×10⁵ (conditional);
  - a·P∞ ≳ 2.5–5×10²⁷ (Run 96 addendum 2, relic-neutrino heating B16-NR) and a·P∞ ≲ 1/κ_b^floor = 1.78×10³⁵;
  - every P∞/p_s bound lapses, and with them P∞ ≳ 6.4×10¹⁰ and p_s ≲ 1.1×10³⁰/a.
- **Q6** (Reading I16 ruling): route (c)'s unravelling constant c is a fixed field. Runs 98–100 stand as computed.

### 2. The engine's hop: where it comes from, and what ε = 0 does to it
**Source.** Note D point 4 (`gravity/reading_P0ps_section.md`; restated in Reading I5 §2 and Reading I11 §2). The hop comes from equating the engine's field to Newton's potential. The ingredients:
- **R1:** z = c_o ln(1 + P/p_s), with c_o = 0.99/ln(1 + 1/p_s) ≈ 0.99(p_s + ½). The 0.99 is the engine's base hop chance PHOP (`zrp35.py`; Runs 14–17), an engine setting.
- **R3:** the exactly linear traffic equation, δz = 6G_lat∗s, which gives 3S/(2πr) at r hops.
- A pair draws S = 2/ħ_t per tick.
- Light crosses ħ_t hops per hold.
- E = aħ/T_hold.

The result is
$$
\frac{\ell_P^2}{\ell^2}=\frac{3}{\pi a\,c_o}\quad\Longrightarrow\quad \ell=\ell_P\sqrt{0.99\pi a\,p_s/3}.
$$

**It did not use ε in the metric.** It used only the medium's response to draw and the requirement that this response reproduce G. P∞ cancels through H ∝ P∞.

**Its stated limit.** Note D's form is its stated scale-free limit (P∞ ≫ p_s), which the pulsar triple then guaranteed. Linearising R1 at the vacuum (algebra on R1–R2, checked against `zrp35.py`):
$$
\delta N=\frac{\delta P}{P_\infty}=\frac{p_s+P_\infty}{c_o\,P_\infty}\,\delta z=\frac{1+\varepsilon_{\rm med}}{c_o}\,\delta z,\qquad \varepsilon_{\rm med}=\frac{p_s}{P_\infty}.
$$
This is R9's N = (1 + ε)e^{−φ} − ε at first order. The factor holds exactly in mean field, and the exact zero-range measure agrees to 0.1–5% for P∞ = 5–3000 (the check). Kept, it gives, in the mean-field, first-order sense:
$$
\boxed{\ \ell^2=\frac{0.99\pi a}{3}\,\ell_P^2\,h,\qquad h=\Big(\frac1{p_s}+\frac1{P_\infty}\Big)^{-1}\le\min(p_s,P_\infty)\ }
$$
For ε_med ≪ 1 this is Note D's form. For ε_med ≫ 1, a vacuum below its crossover, the hop is set by P∞, not p_s.

**The fork: whether the relation stands at all after ε = 0.**
- **(H1)** R1 and R3 still set the slicing's lapse response at first order. The ruling's wording (I15 choice 2(i): "N is the lapse of a maximal-type slicing") and Note H §8 both point here.
  - The relation stands, in the boxed form.
  - **The hop cap (inference):** h ≤ P∞ ≤ 1.78×10³⁵/a, so ℓ ≤ 6.9×10⁻¹⁸ m (4.3×10¹⁷ ℓ_P) and N_cell ≥ 30 at K = a = 1. This assumes the a in E = aħ/T_hold is the a in κ_b = 1/(aP∞), and uses Run 96's Mo-housing floor. The self-term floor gives 8.6×10⁻¹⁸ m.
  - **H1 strains beyond first order.** R1's clock and GR's lapse differ at O(Φ²), with Φ = m/r:
$$
N_{\rm R1}=(1+\varepsilon)e^{-\Phi/(1+\varepsilon)}-\varepsilon=1-\Phi+\frac{\Phi^2}{2(1+\varepsilon)}+\dots,\qquad n=1-\Phi+\frac{\Phi^2}{2}+\dots,
$$
    so the clock departs from GR by εΦ²/[2(1 + ε)]. That is a fraction up to ½ of the Φ²/2 term for ε_med ≫ 1, and it breaks the universal coupling the ε = 0 ruling rests on (I15 §6.1; I17 §2's "excluded alternative").
  - If H1 therefore forces ε_med ≪ 1, then h ≈ p_s and the boxed form cannot be told apart from Note D's. That would also restore a medium-side bound p_s ≲ P∞ ≲ 1.78×10³⁵/a.
  - Whether data bound the O(Φ²) clock departure is not computed.
- **(H2)** The medium carries GR's lapse, P = P∞n (I17 §2), and R3's draw field no longer sets the lapse. G is then HKT's measured constant (I15 §3.3).
  - The engine's G tie has no ground, and the hop is free.
  - P-G-Closure (ℓ = ℓ_P, P08) no longer conflicts with Run 24.
  - Candidates 1–3 below lose their link to p_s and κ_b, which returns ρ_K to Reading I9's position.
  - H2 needs that extra statement about R3; I17 fixes P = P∞n only in stationary fields and says nothing about R3. R1 was "chosen to give β = 1", which GR now supplies.
- **The fork is lopsided.** The ruling's wording favours H1 at first order, and H2 needs a further statement.

**p_s's upper bound lapses.** Reading I11 §3 derives a·p_s ≤ a·P∞/1.6×10⁵ ≤ 1/(1.6×10⁵ κ_b^min) = 1.1×10³⁰. The 1.6×10⁵ is Run 57's pulsar-triple ratio, a bound on ε in the metric, so the derived bound lapses with ε = 0 in gravity. I11's β-based 4×10³¹/a lapses too. As the record now stands, p_s is bounded only below, apart from the medium-side bound H1 may restore. The record notes have been corrected (the check's ERROR 3).

### 3. The candidates
Map criteria are Run 99's: N_cell ≥ 10, every bound allows c/r_C, and c/r_C ≥ 10λN_cell. "Laboratory" means ρ_K < 1.98×10⁴ kg m⁻³, on Run 99's 49 r_C with H added (Run 100).

| # | candidate | formula | left free | laboratory densities? | on the map | grade |
|---|---|---|---|---|---|---|
| 1 | engine-hop line, Note D form | ρ_K = ħ/(cℓV_c), ℓ = ℓ_P√(0.99πp_s/3) | p_s (now bounded only below) | yes | Run 100: survivors at every p_s ≤ 4.3×10¹⁹; near zone continuous from 1.26×10¹² | candidate, fitted through p_s; needs H1 |
| 2 | **engine-hop line, boxed form**, extended | ρ_K = ħ/(cℓV_c), ℓ² = (0.99π/3)ℓ_P²h | h ∈ [4×10⁵, 1.78×10³⁵] (a = 1) | yes, down to ~10⁻⁶ kg m⁻³ | survivors at every h below the wall h_wall = 5.60×10²⁷ aK²; none above it (interference, all 49 r_C). Near zone at every h from 1.26×10¹² to the wall (table below) | candidate, fitted through h; needs H1; differs from row 1 only where H1 strains |
| 3 | vacuum below its crossover (p_s ≫ P∞), so h = P∞ = 1/(aκ_b) | N_cell = K a (m_P/m_N)√(3κ_b/0.99π) | κ_b (and a, K) | yes, gas densities, ~10⁻¹⁰ kg m⁻³ | needs κ_b ≥ κ_wall = 1.785×10⁻²⁸/(aK)², under κ_top including B16-NR (1.99×10⁻²⁸ at the cap). Survives only at r_C ≳ 48.5 μm, a window of width ×1.11 at the cap; ≳ 34.3 μm with B16-NR's ×2 proxy allowance; ≳ 37.1 μm under Run 96's photoheated variant. Margins ≥ 2×10⁸ on the grid points (atmosphere). No near zone | candidate only under H1 together with a clock departure from GR at O(Φ²), or with R1 amended; in tension with I17 §2 and the premise of the ε = 0 ruling. Needs a new statement (ε_med ≫ 1) |
| 3′ | the same at ε_med = 1 (p_s = P∞, h = P∞/2) | as 3, with κ_wall = 8.93×10⁻²⁹/(aK)² | κ_b | yes, ~10⁻¹⁰ kg m⁻³ | r_C ≳ 34.3 μm with B16-NR (width ×2.22 at the cap); ≳ 24.2 μm with the ×2 proxy. Margins ≥ 2.6×10⁷ on the grid points | as 3 (the O(Φ²) departure is ε/[2(1+ε)] = ¼ of Φ²/2) |
| 4 | P08 line (ℓ = ℓ_P), reopened only under H2 | ρ_K = a m_P/V_c, N_cell = 1.3×10¹⁹a | a (r_C shared with route (b)) | only at 45–51 μm, a = 1 | margins ≈ 1.2×10¹¹ (Reading I10 §3); none at a = 2π | candidate under H2; the one tie with no free number; no laboratory test |
| 5 | boost cap as the capacity: K ≳ 12γ² (Reading I14 ruling) | ρ_K = K a m_ℓ/V_c, K ≥ 1.1×10²⁰–1.2×10²³ | which γ; the hop | no: ≥ 2.7×10⁶ kg m⁻³ even at ℓ_max and the r_C cap; ≥ 1.8×10²¹ on the engine hop at p_s = 4×10⁵; ≥ 1.1×10²⁴ on P08 | white-dwarf interiors at best | candidate (identifies K with P_e); inert in the laboratory |
| 6 | K = 1 as "one unit per transfer" ((P2); Note D: a renewal takes one unit from each place) | supports K = 1 in rows 1–4 | as in rows 1–4 | – | – | reading; fixes nothing new |
| 7 | K = P∞ (C1a; C1b) | Reading I9 §2 | – | C1a: ≳ 3×10²⁷; C1b: one unit per cell | C1a inert; C1b excluded (Run 99) | unchanged |
| 8 | the medium as a slicing condition: a density from the lapse equation ∇²N = 4πG(ρ + 3p)N at scale r_C | ρ ~ c²/(Gr_C²) | an O(1) factor | no: 5×10³⁵ – 1.7×10⁴¹ | – | excluded (reads the potential, Reading I8 §4; no self-interaction, I10 §2) |
| 9 | hop "set by the local count" (Reading I13 ruling 3) | ℓ = ℓ(P_local) inside matter | – | – | would make ρ_K read the potential at O(Φ/c²) | constraint: ℓ and E_pair take vacuum values (Reading I8 §2); inert |
| 10 | Q6: route (c)'s c a fixed field | D[Π̂ − c] = D[Π̂] | – | – | no change (Reading I16 ruling) | inert for ρ_K |
| 11 | route (b) reaching the cell ceiling (Reading I10 (ii)) | ρ_K = ħ/(κ_b c r_C V_c) | κ_b | only near κ_top, r_C ≥ 12 μm; no jump | unchanged | candidate, no jump |
| 12 | atomic density, Λ, Compton mass, nuclear saturation | Reading I9 §2 | an O(1) factor | atomic density only | per-particle forms excluded (Run 99) | fitted / borrowed, unchanged |

**Candidate 2 against the map** (a = K = 1). Rows up to 4.3×10¹⁹ come from Run 100 and the check's ×1.02 ladder; rows above it from `i18_map.log`, which the check reproduces.

| h | N_cell | laboratory survivors | smallest q (binding) | near zone |
|---|---|---|---|---|
| 2.0–5.1×10⁸ | 6.3–9.0×10¹⁴ | yes | 1.18 at h = 4.77×10⁸, r_C = 2.80 μm (XENONnT) | Xe window |
| 2.9×10⁹–1.6×10¹⁰ | ~1–2.4×10¹⁴ | yes | 1.54 (enriched Ge) | enriched-Ge windows |
| 7.9×10¹⁰–4.1×10¹¹ | ~2–4.5×10¹³ | yes | **1.14** at h = 4.0×10¹¹, r_C = 0.746 μm (natural Ge, Donadi 2021) | natural-Ge window |
| 1.26×10¹² – ~2×10²¹ | 1×10¹³ – 3×10⁸ | 36–41 | 1.003 at h = 1.2×10¹⁵ (LISA Pathfinder) | at every h (Run 100: 183 consecutive values, 177 set by LISA Pathfinder and 6 by Earth's heat) |
| ~3×10²¹ – 5.6×10²⁷ | 2×10⁸ – 1.7×10⁵ | 36 → 27 | 1.04–2.2 (atmosphere criterion E); F (Vinante microsphere) next, at ×1.3–2.3 for h ≲ 6×10²¹ | 2–3 points, E |
| ≥ h_wall = 5.60×10²⁷ | ≤ 1.71×10⁵ | **0** | – | interference (172 kDa clusters) excludes all 49 r_C, up to h = 1.78×10³⁵ |

- **The wall is exact.** It sits where N_cell = M_cl/m_N = 1.706×10⁵ at every r_C:
$$
h_{\rm wall}=\frac{3}{0.99\pi}\Big(\frac{m_P}{M_{\rm cl}}\Big)^2aK^2=5.60\times10^{27}\,aK^2 .
$$
- **What the wall bounds.** Under the box, h ≤ min(p_s, P∞), so the wall gives **min(p_s, P∞) ≲ 5.6×10²⁷ aK²**. This is conditional on route (c) with Γ_K = c/r_C and on H1. It is a bound, not a value.
- **Above about 3×10²¹ the near zone rests on criterion E.** The record calls that criterion fair only above about 19 km, and these points are provisional (ρ_K ≤ 10: proximity and nanoparticle estimates; Run 99).

### 4. Does anything turn the map into a prediction?
**No.** Every candidate that lands at laboratory densities (rows 1, 2, 3, 3′) still has one free number: p_s, h or κ_b. Each value moves the onset along ρ_K ∝ r_C⁻³ at fixed N_cell. A null result at improved sensitivity therefore moves the number rather than excluding the line, except at the line's ends: the interference wall and p_s's lower bound.

**What present and near-future experiments would do on candidate 2.** These use Run 100 targets' conversions. Each improvement is in the binding measurement's own quantity.
- **LISA-type acceleration noise:**
  - ASD ×1.0015 excludes the closest point (q = 1.003, h ≈ 1.2×10¹⁵, r_C = 0.385 μm, ρ_K = 684 kg m⁻³);
  - ×3.2 clears every LISA-bound near-zone point;
  - the LISA mission's requirement is no better than LISA Pathfinder's achieved noise (Run 99), so the gain must come from lower force noise per unit face area.
- **X-ray limits:**
  - a natural-germanium limit ×1.14 tighter tests h ≈ 4×10¹¹, the lowest-margin X-ray window;
  - XENONnT's λ/r_C² about 15% tighter tests h ≈ 4.8×10⁸;
  - enriched germanium needs ×1.5–7.2 for h ≈ 3×10⁹–1.6×10¹⁰;
  - each new detector material opens a row of its own.
- **Levitated nanoparticles:** F (Vinante 2017, r_C ≤ 2 μm) is next-binding at ×1.3–2.3 in S_F at r_C ≈ 0.44–0.5 μm for h ≈ 3×10²⁰–6×10²¹. It is binding at 0.85–1.1 μm with q ≈ 23–80. A force-noise floor a few times lower would test the low-density part of the line, where the near zone otherwise rests on criterion E.
- **None of these tests the line itself,** only the h they reach.

**Candidate 3 is the one definite joint statement, and it is nearly closed.**
- It survives only at r_C ≳ 48 μm, with κ_b within ×1.1 of the ruled relic-neutrino bound (Run 96 addendum 2).
- With that bound's ×2 allowance, or at ε_med = 1, it survives at r_C ≳ 34 μm.
- A tightening of ×1.1–2 at the cap would exclude it.
- No LISA-type, X-ray or levitated-particle experiment reaches it.
- It also needs H1 with ε_med ≫ 1, where R1's clock departs from GR's lapse at O(Φ²).

**What new statement would fix ρ_K.**
- Under H1: a value of h. That means p_s fixed with ε_med ≪ 1, or ε_med fixed together with an independent P∞ (for example from a route-(b) detection).
- Under H2: P-G-Closure (ℓ = ℓ_P). It fixes the line with no free number, but puts it at 45–51 μm with margins of about 10¹¹, out of reach.
- Nothing in the record or today's rulings supplies either. A capacity per place (K) as a primitive does not help unless its value is stated. Its natural values, K = 1 and K ≳ 12γ², give rows 1–4 and row 5.

### 5. Choices for a ruling
1. **Record the finding:** under the record as it now stands, nothing fixes ρ_K. Route (c)'s laboratory forms remain a family with one free number. *A restatement of Reading I9 ruling 1 (and I10 §4) for ε = 0.*
2. **The hop relation under ε = 0:**
   - (a) H1: the medium's field sets the slicing's lapse at first order. The relation stands in §2's boxed form, with the O(Φ²) clock departure for ε_med not small left open.
   - (b) H2: R3's draw field no longer sets the lapse. The engine's G tie lapses, the hop is free, and the P08 line returns as a candidate.
   - (c) Leave open.
3. **Whether to register an extension of Run 100's ladder** to h = 1.78×10³⁵/a in the boxed form. The wall would be stated in advance as h_wall = 5.60×10²⁷ aK², a and K scaled, and the natural-Ge window included among the low-h targets.
4. **Candidate 3:** record it as nearly closed, conditional on H1 with a clock departure from GR, or on an amended R1, and in tension with the ε = 0 ruling. Or set it aside.
5. **Record rows 5, 8, 9 and 10** as inert or excluded for ρ_K.

### Recommended next steps
1. Rule on choice 2 (H1 or H2), since it decides whether the engine-hop line exists after ε = 0.
2. If H1: compute whether existing clock data bound R1's O(Φ²) departure εΦ²/[2(1 + ε)]. That decides whether ε_med is free under H1, and so whether candidate 3 is live and whether the boxed form differs from Note D's.
3. If H1: register the extended ladder (choice 3) before computing it, with a ∈ {0.1, 1, 2π}, the wall stated in advance, and κ_top including B16-NR.
4. Re-check the zero-range factor's exact form at the counts the hop line uses, beyond the check's P∞ ≤ 3000.

### Sources (read)
`quantum/reading_I8_internal_complexity.md`, `reading_I8_C4b_statement.md`, `reading_I9_fixing_saturation.md`, `reading_I10_tying_rhoK.md`, `reading_I11_ps_upper_bound.md` (§2–§3, §7), `reading_I13_bounded_ledger.md` (§9), `reading_I14_grid_free.md` (ruling), `reading_I16_born_mirror.md` (ruling), `run96_section.md` (addendum 2, via the check), `run97_section.md`, `run98_section.md`, `run99_section.md`, `run100_section.md`, `run100_targets.md`; `gravity/reading_P0ps_section.md` (Note D point 4), `reading_I15_borrowed_inputs.md` (§3, §5–§6, rulings), `test_I15d_section.md`, `reading_I17_black_holes.md` (§2); `ONTOLOGY.md`; `record/RULINGS.md`. Code, read-only: `/home/claude/quantum100/` (`run99_lib.py`, `run100_lib.py`, model files), `/home/claude/adopted/zrp35.py`. Check: `/home/claude/checkI18/`.

### Ruling (30 October 2026)

Allen: "do as you recommend." **H1:** the medium still sets the slicing's lapse through R3's draw field, so the engine's G tie and the corrected hop relation ℓ² = (0.99πa/3)ℓ_P²·h, h = (1/p_s + 1/P∞)⁻¹, stand at first order. The engine-hop line stays a candidate, with min(p_s, P∞) ≲ 5.6×10²⁷ aK² conditional on route (c) with Γ_K = c/r_C. ρ_K stays free (a restatement of Reading I9 ruling 1 for ε = 0). Candidate 3's second-order clock departure is to be checked against data.
