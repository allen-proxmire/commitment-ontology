### Reading I17 (draft): R11 and the hole picture at ε = 0 in gravity

*30 October 2026. A reading of the record, plus one small unregistered calculation (`i17_numbers.py`, output `i17_numbers.log`). It encodes no new rule. Written in answer to the 30 October ruling that R11's statements are "to be re-read" under ε = 0 in gravity. Revised after an independent check (`checkI17/REPORT.md`, with `check_i17.py` and its log), whose corrections are adopted; the pre-check version is `reading_I17_v1_precheck.md`. Statements marked **inference** go one step past what the record or a source says and should be checked independently before anything is built on them.*

**In plain terms.** Every unusual feature of CO's black holes came from the medium's scale ε = p_s/P∞ sitting in the metric: no event horizon, a cold surface that stops Hawking radiation, a throat and a horn, and a core at areal radius 3m. With ε = 0 in gravity the hole outside matter is exactly GR's, and possibility runs out at GR's horizon itself. The rule "infalling matter commits where possibility falls to 2p_s" can still be read in a static hole. It marks a sphere a hair outside the horizon, at areal radius about 2m, not 3m, as Run 43 already placed the core surface under GR's exterior. But the hole's geometry no longer needs the rule to stop a bounce. In GR a causal thin shell (flat interior) cannot turn back below 25m/12, and static matter satisfying the dominant energy condition is excluded far outside that sphere (2M/R ≤ 48/49, Andréasson). In a collapse the sphere depends on how time is sliced: one standard slicing puts it just outside the horizon, another well inside. So R11 must now say what commitment does, which is Note C's 19 October fork again. If committed matter carries on as GR says, the event horizon, Hawking evaporation and GR's singularity in the metric all return, and "no singularity" becomes an open requirement on a rule inside the horizon. If committed matter is held where it commits, CO keeps a horizonless, cold, non-evaporating hole. But held matter violates the dominant energy condition by a large factor: for a thin shell, its stress is about 1/(8ε_med) times its energy density.

---

### 1. What was read

- **Top-level files:** `ONTOLOGY.md` (R1, R2, R9, R10, R11, "ε in gravity is zero"); `README.md` (Black holes, What would break it); `RESULTS.md` (Strong field and black holes; Where CO differs).
- **The full record:** `record/ONTOLOGY_full.md` (R9, R10, R11, §5 items 4–5, §7); `record/RULINGS.md` (19–21 and 30 October).
- **The readings and the test:** `gravity/reading_I15_borrowed_inputs.md` (§5, §6.1, §9, rulings); `gravity/test_I15d_section.md`.
- **The runs and notes:** Runs 43 and 64–80 (`run43_section.md`, `run64`–`run80`, `run66b_medium_section.md`); Note C (`run_radiation_section.md`); `design_spherical_lattice.md`.

Runs 70, 72, 72b, 75–78 and 80 test clocks on curved lattices and make no statement about holes. Runs 77 and 79 bear on how space curves, not on R11. The hole statements rest on Runs 43, 65, 67, 68, 69, 71, 73 and 74, and on Note C.

**What this reading re-uses rather than re-derives:**
- The surface just outside the horizon, and its echo delay, are Run 43's calculation (19 October, option A) in Schwarzschild. Run 43 put the core surface at a small lapse α_s ~ p_s/P₀ just outside r₊, with delay [(2/κ)ln(1/α_s) − 9.7]M. In Schwarzschild this is 2Δr* = 8M ln(1/n_c) − 0.77M (the check). Note C records the same placement.
- The fork in choice 1 is Note C's fork between (a) holes evaporate and (b) holes never evaporate.
- The invariance and slicing points are Reading I15 §5's R11 row: the surface is "a level set of the Killing norm and is invariant" in a static field, and "needs a slicing-free definition, for example a local count" in collapse.
- "P = 0 at r = 2m" is Run 65's K65c.

What is new: at ε = 0 the zero-clock surface coincides with GR's horizon, the old core radius has no counterpart, and the threshold's purpose is gone.

### 2. The key question: does "possibility falls to 2p_s" still define a surface?

**What the record had (ε in the metric; Runs 66–67, 73–74).** The clock was the occupancy, N = P/P∞. It differed from GR's lapse n = √(1 − 2m/r) by the medium's offset:
$$
N=(1+\varepsilon)\,n-\varepsilon,\qquad \frac{P}{p_s}=\frac{N}{\varepsilon},\qquad ds^2=-N^2dt^2+N^{-2}\big(dr^2+(r^2-2mr)\,d\Omega^2\big).
$$
- P = 0 sat outside GR's horizon, at n₀ = ε/(1 + ε).
- The areal radius R = rn/N blew up there: the horn.
- P = 2p_s was the surface N = 2ε, at
$$
R_c=\frac{r\,n}{N}\Big|_{N=2\varepsilon}=2m\,\frac{k+1}{k}\big(1+O(\varepsilon)\big)=3m\quad(k=2).
$$

**At ε = 0 in gravity.** The metric is Schwarzschild's, and R2's clock is GR's lapse. In a static field N is the Killing norm (Reading I15 §5, choice 3). Keep ε_med ≡ p_s/P∞ as a medium quantity. Reading P through R2 then gives:
$$
P=P_\infty\,n,\qquad P=0\ \text{at}\ r=2m,\qquad P=k\,p_s\ \Leftrightarrow\ n_c=k\,\varepsilon_{\rm med},\qquad r_c=\frac{2m}{1-k^2\varepsilon_{\rm med}^2}\approx2m\big(1+4\varepsilon_{\rm med}^2\big).
$$
Taking P = P∞n as R2 at ε = 0 is a **reading**. Run 65 (K65c) already states it at ε = 0: "the clock rate reaches zero at r = M/2 [isotropic], a horizon where possibility runs out".

**The excluded alternative.** Suppose R1's mean-field law, 1 + P/p_s = (1 + 1/ε)e^{−φ}, were kept as the medium's state while the metric's lapse is n. Then:
- P = P∞[(1 + ε)n − ε];
- P = 0 would sit outside the horizon, at r − 2m ≈ 2mε²;
- P = 2p_s would sit at r_c ≈ 2m(1 + 9ε²);
- clocks would no longer read P/P∞, which breaks R2 and universal coupling.

So the reading above is the one consistent with R2 and the ruling. Either way the surface is at about 2m, so the absence of 3m does not depend on the choice.

**In a stationary hole, the rule defines a surface,** and the surface is invariant: a level set of the Killing norm (as I15 §5's R11 row says).
- It lies **outside r = 2m by 8mε_med²**, with areal radius ≈ 2m, not 3m (log §2).
- For spinning holes under R10's reading Z, the clock is the ZAMO lapse α (Run 69). P = 2p_s is then α = 2ε_med, just outside r₊.
- At ε = 0, R10's "Kerr to O(ε/α)" is exact Kerr.

**Why 3m goes.** With the metric's offset ε_g and the medium's ε_med as separate parameters,
$$
R_c\approx2m\Big[1+\frac{\varepsilon_g}{k\,\varepsilon_{\rm med}}\Big],
$$
which is continuous in ε_g (the check: 2.000, 2.010, 2.100, 3.000 and 4.000m as ε_g/ε_med runs 0, 0.01, 0.1, 1, 2). **3m is 2m(k + 1)/k only when the metric's offset equals ε_med. At ε_g = 0 it is 2m.** The record's runs tied the two together, which is why log §3 gives 3m at every ε > 0.

**Where ε_med stands.** The bounds on P∞/p_s in the inputs table (pulsar triple, α₁, α₂, GW170817) were bounds on ε in the metric. If the medium no longer enters the metric, they no longer bound ε_med.
- P∞ ≳ 6.4×10¹⁰ was p_s's bound times the pulsar triple's ratio (`quantum/design_commitment_quantum.md`), so it lapses too.
- T-I15d's P∞ ≳ 5×10¹⁴ is built the same way and lapses with it.
- Only two bounds remain: p_s ≳ 4×10⁵ (conditional since Reading I6), and p_s ≲ 1.1×10³⁰/a via P∞ (Reading I11).
- **Gravity leaves ε_med unbounded.**
- Readings I4, I5, I7 and I14 and Run 93 quote 6.4×10¹⁰ and inherit the lapse. A text search also finds it in Readings I1 and I6, `note_matter_pattern_status.md`, the quantum design note and Reading I15.

Whatever ε_med is, the surface sits within 8mε_med² of r = 2m.

**In a collapse, the surface depends on the slicing.** Under the ruling the medium is a slicing condition of maximal type (Reading I15, choice 2(i); Note H §8). Once there is no Killing field, the level set N = kε_med of a slicing's lapse is not invariant. Different maximal slicings of the same hole even disagree on which side of r = 2m it lies.

- **Stationary maximal slicings of Schwarzschild** (computed here; standard). A slice whose unit normal has n^R = −C/R² has ∇·n = 0, so it is maximal. Its lapse relative to Killing time is
$$
\alpha^2=1-\frac{2m}{R}+\frac{C^2}{R^4}.
$$
  - **C = 0 is the static slicing:** α = n, and P = 2p_s lies just outside r = 2m.
  - **C² = 27m⁴/16 is the "trumpet".** α has a double root at R = 3m/2, inside the horizon, with α(2m) = 3√3/16 ≈ 0.325. Near the root α ≈ (2√2/3)|R − 3m/2|. So P = 2p_s lies at R ≈ 3m/2 + 3ε_med/√2, **inside the event horizon** (log §6: 1.500021m at ε_med = 10⁻⁵).
  - **The trumpet reading breaks R2's redshift content outside the horizon** (the check). Static clocks there would no longer run at P/P∞: α = 0.325 against n = 0 at R = 2m, and 0.493 against 0.447 at 2.5m. That supports restricting R2 to stationary fields, read through the Killing norm (choice 2).
- **Late-time maximal slicing approaches the limit surface R = 3m/2.** The maximal foliation covers r > 3m/2, and the lapse at the bifurcation sphere collapses as exp(−4τ/(3√6 m)). Source: Beig & Ó Murchadha 1998. The draft took the rate from the ar5iv text; the check confirmed only the abstract.
  - For Oppenheimer–Snyder collapse, Petrich–Shapiro–Teukolsky's lapse-collapse rate, 0.5443 (reported second-hand by Brewin & Kajtar), equals 4/(3√6).
  - That a collapse evolved in maximal slicing settles toward the trumpet is an **inference** supported by this agreement.
- **One case stays invariant during collapse** (a **reading**). Outside a spherical collapse the metric is exactly static by Birkhoff's theorem, which applies at ε = 0 because the medium no longer puts stress outside matter. So a thin shell's outer face reaches n = 2ε_med at r_c, before the horizon forms there. Inside extended matter, and in any collapse without spherical symmetry, P per place needs a slicing.

**Locality.** No local quantity marks r_c through the metric alone.
- In exact vacuum, derivatives of curvature do mark it (the check). With K = 48m²/r⁶, the gradient norm ∇K·∇K = (288m²/r⁷)²(1 − 2m/r) vanishes at r = 2m. The ratio (∇K·∇K)/K^{5/2} then fixes n locally: the check recovers n = 2.000000×10⁻⁵ at r_c. This is the effect Karlhede, Lindström & Åman (1982) reported at the Schwarzschild sphere (cited by the check from memory, not fetched).
- A trigger built on such a quantity couples matter to curvature derivatives, which universal non-derivative coupling excludes. It also fails inside matter (Ricci ≠ 0) and does not track n in collapse.
- R11's trigger read through the lapse fares no better: it depends on the normalisation at infinity (P∞). That conflicts with locality and universal coupling, which (with HKT) are what give ε = 0 in gravity (Reading I15 §6.1). This is an **inference**.

### 3. Claim by claim

| claim | rested on | at ε = 0 (metric outside matter is Schwarzschild/Kerr) | grade |
|---|---|---|---|
| **no event horizon** | ε in the metric: the zero-clock surface at n₀ = ε/(1 + ε), outside GR's horizon, κ = 0 (Run 67, "follows from option 3") | P = 0 at r = 2m (Run 65, K65c): the zero-clock surface is GR's horizon. A collapse forms an event horizon unless committed matter is held outside it (choice 1(ii)) | **withdrawn** as a result of option 3; survives only under 1(ii), and there it rests on an added rule |
| **no singularity** | R11's commitment, which pre-empts Run 67's stretching singularity at P = 0; the no-infinities principle; the core | Run 67's singularity is gone: Schwarzschild is regular at r = 2m. The medium's null-energy violation is gone too (Run 71, K71a: ρ + p_r ≈ −3ε/(4πr⁴) far out, about −0.03 at the throat). So Penrose's theorem applies once a trapped surface forms, and GR's r = 0 returns in the metric | **open**: no mechanism remains under 1(i); under 1(ii) none is needed, since no trapped surface forms; the no-infinities principle stays a principle, not a mechanism |
| **no evaporation** | Run 68: the cold surface (κ = 0) cuts Hawking's flux after 8M[ln(1/ε) − 1]. Run 71: a power-law endpoint in the horn. Run 74: commitment at N = 2ε in the horn, with a cold core (model A) or a tail (model B). The 21 October ruling "holes are stable … with nothing added" rested on Run 68's choice (i) | Run 68's own GR control (K68d) is the ε = 0 case: the flux stays at Hawking's for ever. Under 1(i), GR's evaporation at T_H = ħc³/(8πGMk_B) returns (Note C's reading (a)). Under 1(ii), a cold surface at N_c = 2ε_med cuts it after Δu_eff ≈ 8M ln(1/N_c) − O(10M) for a collapsing shell. The 85M (ε_med = 10⁻⁵) and 159M (10⁻⁹) of log §5 are the cut on the static exterior; log §5 reproduces Run 68's 72, 109, 146 and 183M, and Run 71 found a collapsing shell about 9.4M shorter. Run 74's flash or tail was computed only in the horn and is an analogue here, not a result | **changes**: withdrawn under 1(i); under 1(ii) it survives, on the added rule plus the core's state (open) |
| **commitment at P = 2p_s** | R2's clock plus the 21 October ruling, placed in the horn at N = 2ε | In stationary holes, a level set of the Killing norm (or ZAMO lapse) at n = 2ε_med, r_c ≈ 2m(1 + 4ε_med²). Slicing-dependent in collapse (§2; I15 §5's R11 row) | **reading** in stationary holes; **open** in collapse (needs I15's choice 3, and a slicing) |
| **… before any causal matter can turn back** | Run 71: in the horn the medium's stress turns shells back at N ≈ wε. Run 73: causal matter turns at most at 1.27p_s, so any k ≳ 1.34 works | In GR a thin shell (flat interior) momentarily at rest at R can turn back only if w ≥ w_static(R) = [n + m/(Rn) − 1]/[2(1 − n)], which decreases monotonically on (2m, 3m]. At w = 1, 5n² − 6n + 1 = 0, so n = 1/5: causal matter cannot turn back below **R = 25m/12** (2M/R = 24/25, Andréasson's thin-shell value). w ≤ 0.6 cannot turn below 2.19m, and w ≤ ⅓ not below 2.45m (log §1). Static matter of any kind that satisfies the dominant energy condition needs 2M/R ≤ 48/49 (Andréasson), far outside r_c. Inside r = 2m nothing turns. The bounce that motivated the ruling (Run 71) does not occur | **restatement**: the clause is GR's. The threshold's purpose is gone and k is **inert**: any k gives a surface at 2m(1 + k²ε_med²) |
| **core at areal radius 3m** | R = rn/N at N = kε, with the metric's offset tied to the threshold's ε (Run 74) | ≈ 2m under the static reading; ≈ 3m/2, inside the horizon, under the trumpet slicing; 3m in no slicing | **withdrawn** |
| **holes stable** | Run 68's cold surface; commitment before Run 71's bounce | Classically these are GR's holes, with no bounce to prevent. The quantum side follows "no evaporation" | **changes**: classical stability is a **restatement** of GR's; "never lose mass" follows the evaporation row |
| **throat and horn** | ε in the spatial metric (Run 67): throat at n* ≈ (ε/2)^{1/3}, R_min ≈ 2m(1 + 3(ε/2)^{2/3}); horn where R grows as 1/(r − r₀) | R_min → 2m, so the throat merges with the horizon's sphere. The horn, its curvature singularity and Run 71's medium-assisted crossing are gone | **withdrawn** (Run 71's crossing result is **inert**) |
| **no echoes** | Run 43: the core commits what reaches it (a total absorber). Run 67: infinite tortoise distance. Run 74: "now rests on the total-absorber ruling" | Under 1(i) there is an event horizon, so no echoes, as in GR. Under 1(ii) the surface is at finite tortoise distance: Run 43's delay in Schwarzschild, 2Δr* = 8M ln(1/n_c) − 0.77M, which is 86M (ε_med = 10⁻⁵) to 159M (10⁻⁹), about 4–8 ms for 10 M☉ (log §4). Echoes are then absent only by the total-absorber ruling, which Run 43's bounds test | **changes**: a **restatement** under 1(i); under 1(ii) it rests on the absorber ruling (added) |
| **option A (GR's exterior for mergers)** | borrowed, 19–20 October | covered by the ruling: the metric outside matter is GR's | **inert** as a separate input |

**Statements in the record that now read stale.** This is bookkeeping, not new inferences.
- **T-I15d:**
  - "What it means" says Run 67's throat and horn, R11's commitment surface (at N = 2ε) and the core (at 3m) persist inside holes. That held at small ε ≠ 0; at ε = 0 they do not.
  - Its "P∞ ≳ 5×10¹⁴" (§2).
- **`RESULTS.md`:**
  - "a hole's clock stops just outside GR's horizon, at a cold surface; no event horizon | follows from option 3 | 67";
  - the "no echoes; no evaporation" row, whose basis is option 3 with ε;
  - "static stars and holes as GR's, to O(ε)", now exact.
- **`ONTOLOGY.md`:**
  - the inputs row "R10 rotation (provisional), R11 the core | added | … no singularity, no evaporation";
  - R10's "to O(ε/α)";
  - the P∞/p_s and P∞ rows of the inputs table (§2).
- **`README.md`:** the P∞/p_s and P∞ entries in the inputs table (§2).
- **`record/ONTOLOGY_full.md`:**
  - §5 items 4–5 (lines 430–437);
  - the tables at lines 55–56, 341 and 683–684;
  - R9 at line 278 (the clock stops where GR's lapse would be about ε);
  - R10 at line 285 ("to O(ε/α)").
- **If they are live summaries:** `record/AT_A_GLANCE.md` lines 59–63, and Note E (`run66b_medium_section.md`, line 28: "where a hole's clock stops, at GR's lapse ε/(1 + ε)").
- **The files that quote P∞ ≳ 6.4×10¹⁰** (§2).

### 4. What else changes, and what carries over

- **Black-hole thermodynamics.** Under 1(i), S = A/4 and T = κ/2π return as GR's (borrowed), and the Open item "black-hole thermodynamics without evaporation" lapses. Under 1(ii), T = 0 and the item stays open.
- **Primordial holes.** Under 1(i), GR's evaporation bounds apply again. Under 1(ii) they lapse (Run 68's reading 3).
- **"What would break it: black-hole echoes, or evaporation."** Under 1(i), evaporation is predicted and echoes are absent, as in GR. Under 1(ii) the line stands, with the echo delay now set by ε_med.
- **Record and information.** "What falls in becomes record" (Run 43) survives as a **reading** under either choice. Under 1(i), Note C's 19 October reading (a) returns: holes evaporate while the record stays.
  - Its first tracked assumption ("the core acts on quantum fields as a horizon would") is no longer an assumption, since there is a horizon.
  - Its second (the pull drops while the record stays) is how the engine already works (Run 30).
  - The information question that Note C left open returns with it.
- **The quantum sector** (an **inference**; **open**). Q1 says a pattern has no gravity of its own between records. Hawking's negative-energy partners are patterns falling inward. Whether, and where, they are recorded decides whether a hole's draw falls. The record says nothing on this.
- **Unchanged.**
  - Run 43's absorption bounds and Note C's reading of papers 039–052 depend on GR's exterior, which is now exact.
  - Runs 70–80's clock results do not involve holes.
  - The spherical design note's engine hole uses ε ≈ 1/8–1/10 by construction. It stays an engine design, not a physical hole.

### 5. Choices for a ruling

1. **What commitment does to infalling matter** (Note C's fork, at ε = 0).
   - (i) **Commitment is a relabelling.** Matter that commits becomes record, and its stress-energy follows GR.
     - Holes are GR's: an event horizon, Hawking evaporation, GR's interior.
     - R11 becomes "what crosses becomes record" (a reading).
     - "No singularity" becomes **needed**: a rule acting inside the horizon. Since the lapse there is slicing-dependent, the rule must be defined by an invariant local quantity, as I15 §5's R11 row asks: the matter's own count per place, or a curvature scale coupled in a way universal coupling allows.
   - (ii) **Commitment holds matter where it commits.** This gives a horizonless, cold, non-evaporating hole with its surface at n = 2ε_med.
     - It needs an added rule.
     - For a thin shell with flat interior, holding it there takes w ≈ 1/(4n_c) = 1/(8ε_med) (log §1: 1.25×10⁸ at ε_med = 10⁻⁹). **The held matter violates the dominant energy condition by that factor.** That is a conflict with established physics, not only an added rule.
     - It also conflicts with universal coupling (§2, an inference), and it is the only remaining place where the medium would act on gravity.
   - (iii) **Leave R11 unruled** until a collapse is computed in a stated slicing (next step 3).
2. **How P is read in holes.** This repeats Reading I15's open choice 3. Either restrict N = P/P∞ to stationary fields (the Killing norm, or the ZAMO lapse for spin) and list collapse as open, or name the slicing and accept a slicing-dependent commitment surface. §2's trumpet comparison favours the first: the second breaks R2's redshift outside the horizon in at least one maximal slicing.
3. **Evaporation:** accept GR's (with 1(i)), or keep "no evaporation" as a consequence of 1(ii) only.
4. **Bookkeeping, once ruled:** the stale statements listed in §3, R11 in `ONTOLOGY.md` and `record/ONTOLOGY_full.md`, the Black holes bullet and "What would break it" in `README.md`, the Open item on thermodynamics, and the R11 entries in Reading I15's §5 table.

### 6. Recommended next steps

1. Rule on choice 1.
2. Write back §2's lapsed P∞ bound (the P∞ ≳ 6.4×10¹⁰ and 5×10¹⁴ statements, and the files that quote them). It does not wait on choice 1.
3. If (i) or (iii): register a calculation of where N = 2ε_med falls on the matter in an Oppenheimer–Snyder collapse under maximal slicing (Petrich, Shapiro & Teukolsky give the slicing), relative to where the matter crosses its horizon. It decides between the choices:
   - if commitment falls inside the horizon in the slicing the medium uses, commitment cannot keep a horizon from forming, and 1(ii) is unavailable in that slicing;
   - if it falls outside, 1(ii) stays available.
4. If (ii): write the core's stress as a source and check it against Bianchi conservation and the energy conditions before any run. The thin-shell value already violates the dominant energy condition.
5. Write a short reading of Q1 for Hawking partners (does a hole's draw fall under Q1?), since 1(i) depends on it.
6. Do the bookkeeping in choice 4 after the ruling.

### Sources

- The record files listed in §1, plus `quantum/design_commitment_quantum.md` (the P∞ product) and Reading I11 (the upper bound).
- H. Andréasson, "Sharp bounds on 2m/r of general spherically symmetric static objects", [arXiv:gr-qc/0605097](https://ar5iv.arxiv.org/html/gr-qc/0605097), via the check: 2M/R = 24/25 for an infinitely thin shell with zero radial pressure satisfying the dominant energy condition; 48/49 for general dominant-energy matter in the thin-shell limit.
- R. Beig and N. Ó Murchadha, "Late time behaviour of the maximal slicing of the Schwarzschild black hole", [arXiv:gr-qc/9706046](https://arxiv.org/abs/gr-qc/9706046). The abstract was fetched by the draft and the check, and the ar5iv text by the draft only: the foliation covers r > 3m/2, 0 < C < 3√3m²/4, and α ~ exp(−4τ/(3√6 m)) along observers through the bifurcation sphere.
- L. Brewin and J. Kajtar, [arXiv:0903.5367](https://arxiv.org/pdf/0903.5367), via the check: Petrich–Shapiro–Teukolsky's lapse-collapse rate, 0.5443311 = 4/(3√6).
- L. I. Petrich, S. L. Shapiro and S. A. Teukolsky, Oppenheimer–Snyder collapse with maximal time slicing, *Phys. Rev. D* 31, 2459 (1985). Title and reference from memory; not confirmed by the check.
- F. Estabrook, H. Wahlquist, S. Christensen, B. DeWitt, L. Smarr and E. Tsiang, "Maximally slicing a black hole", *Phys. Rev. D* 7, 2814 (1973). From standard accounts, not fetched.
- A. Karlhede, U. Lindström and J. E. Åman (1982), on a curvature invariant that vanishes at the Schwarzschild horizon. Via the check, from memory, not fetched.
- R. Penrose, "Gravitational collapse and space-time singularities", *Phys. Rev. Lett.* 14, 57 (1965). Standard, not fetched.
- T. Harada, V. Cardoso and D. Miyata (2019), via Run 68.

*Files in this folder:*
- *`reading_I17_DRAFT.md`: this reading.*
- *`reading_I17_v1_precheck.md`: the version before the check.*
- *`i17_numbers.py` and `i17_numbers.log`: the calculation (the static-shell bound, the surface's position, the old horn formula at a tied offset, tortoise delays, Run 68's flux at ε = 0, the stationary maximal slicings). Not registered.*

### Ruling (30 October 2026)

Allen: "do as you recommend." **Choice 1, (i):** commitment relabels matter as a record; CO's holes are GR's, with a horizon and Hawking evaporation. "No singularity, no event horizon, no evaporation", the core at 3m, the throat and horn are withdrawn. A registered collapse calculation (Oppenheimer–Snyder under maximal slicing) is to show where possibility runs out on infalling matter relative to the horizon. The lapsed P∞ bounds are written back.
