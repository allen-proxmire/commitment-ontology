## Reading I7: what could fix r_C — the criterion, the band, and the candidates

*28 October 2026. Checked independently (`checkI7/REPORT.md`); its corrections are adopted, with one softened (D4′, per Allen's "don't swing the pendulum"). The criterion and grading were ruled the same day (§7). The numbers in §2 are post hoc arithmetic on Run 96's registered window (`model96.py`, unchanged). Candidate C1 was written out in full (`reading_I7_C1_statement.md`) and registered in Run 97.*

### 1. Why

Route (b) has two scales: its rate, κ_b = 1/(aP∞) (a definition under Reading I6), and its coarseness r_C, ruled a primitive input bounded by data (Reading I5). Run 96 narrowed the window to 0.09 μm ≲ r_C ≲ 51 μm. A rule from the primitives that fixes r_C would make route (b) a one-parameter rule and turn the window into a range for P∞. It would not by itself tie route (b) to gravity: κ_b contains P∞ by definition, and gravity's P∞ ≳ 6.4×10¹⁰ is a lower bound, conditional since Reading I6, about 16 decades below the band here.

Two standing rulings frame the attempt:
- **Note I §9.** A scale counts as remarkable if it is derived from the primitives, registered before its value is computed, lands in the window and shares a scale with gravity; or, equally, if a CO-native reason fixes its form and gives a second consequence standard QM lacks. A scale "picked from free combinations of the scales" does not count.
- **Reading I5, ruling 2.** No test of the family r_C = ℓP∞ⁿ is registered unless a mechanism fixes n beforehand.

### 2. The band (post hoc arithmetic on Run 96)

With κ_b = 1/(aP∞), Run 96's window becomes a region in (aP∞, r_C):
$$
\frac{1}{\kappa_{\rm top}(r_C)}<aP_\infty<\frac{1}{5.62\times10^{-36}}=1.78\times10^{35},\qquad 9.01\times10^{-8}\ \text{m}\le r_C\le5.11\times10^{-5}\ \text{m},
$$
where κ_top(r_C) = min(0.948 r_C⁵, 7.29×10⁻¹⁹ r_C²) inside the window (SNO below 9.16×10⁻⁷ m, B7′ above; B4's 2.82×10⁻²⁷ binds only beyond the cap).

| r_C | a·P∞ allowed |
|---|---|
| 9.0×10⁻⁸ m (the lower edge) | 1.78×10³⁵ only |
| 1×10⁻⁷ m | 1.06×10³⁵ – 1.78×10³⁵ |
| 1×10⁻⁶ m | 1.37×10³⁰ – 1.78×10³⁵ |
| 5.1×10⁻⁵ m (the cap) | 5.25×10²⁶ – 1.78×10³⁵ |

So **5.3×10²⁶ ≲ a·P∞ ≲ 1.8×10³⁵**, whatever r_C is.

**Reading I5's family, r_C = ℓP∞ⁿ** (`band.py`, `band.log`; reproduced in `checkI7/`):

| a | hop | allowed n | n = 1: log₁₀ P∞ |
|---|---|---|---|
| 0.1 | P08 (ℓ_P) | 0.77–1.10 | 29.6–30.5 |
| 0.1 | the engine's (204 ℓ_P at p_s = 4×10⁵) | 0.70–1.02 | 28.0–28.2 |
| 1 | P08 | 0.79–1.14 | 29.2–30.5 |
| 1 | the engine's (644 ℓ_P) | 0.71–1.04 | 27.4–27.7 |
| 2π | P08 | 0.81–1.18 | 29.0–30.5 |
| 2π | the engine's (1.6×10³ ℓ_P) | 0.71–1.05 | 26.8–27.3 |
| 0.1–2π | the engine's, p_s free (1 ≤ p_s ≤ P∞/1.6×10⁵) | 0.35–1.16 | — |

The cap sets the upper end of each n = 1 band, and B7′ the lower end. The engine's narrow bands come from the window, not from any mechanism, and are not evidence.

**The prefactor is not tested.** P∞ is free, so it absorbs any prefactor: at n = 1, r_C = k·ℓ·P∞ passes for any k across about 11.3 decades (log₁₀ k from about −10 to +4, depending on hop and a). Of ten simple exponents with k = 1, only n = 1 passes for both hops at every a, and n = 3/4 for the engine's hop only. Hop·P∞ was already placed by Run 92 as a dimensional candidate.

**Disclosure.** For any candidate whose scaling with P∞ can be read off its statement, this table decides the outcome by inspection. A registration on r_C alone is therefore not blind on n. A candidate can count for more than "derived" only by fixing something the window does not already allow freely (§3, D5).

### 3. The criterion (to be hashed before any candidate is computed)

A candidate rule for r_C is graded **derived** only if all of these hold:
- **D1. From the primitives and the ruled rules only.** Inputs marked borrowed or not CO-native (Note I §3) may be used for estimates, not as steps. Provisional rules (R2) may be steps and are named; Note D's E = aħ/T_hold (an inference on DSR-4, "open to reversal") and κ_b's definition are named where used.
- **D2′. No free quantity beyond P∞.** ħ_t, δu, p_s, any speed or count must be fixed by the candidate's own statement. A free ħ_t renames r_C (Reading I5 §2). The hop is named in advance; if it is the engine's, the candidate is judged at p_s = 4×10⁵ and also states its band with p_s free.
- **D3. Stated, checked and hashed before its value is computed,** with n and k written down before hashing.
- **D4′. One r_C for every species,** as Reading I5 ruling 5 and Q4 stand, because Run 96's window presupposes it (SNO bounds nucleons, XENONnT electrons, B7′ every free particle). A species- or configuration-dependent candidate is not dropped: it is graded a **lead** whose new statements include reopening ruling 5, and it can be judged only against a window registered for it.
- **D5. Remarkable** (a tightening of Note I §9, labelled as such): n and k inside §2's range make a candidate at most derived. It is remarkable only if it also fixes P∞, a or p_s independently of route (b)'s window, or makes a gravity-side quantity measurable, or predicts something a registered datum outside the window can test.

**Grading (Allen, 28 October: "I don't want to throw out promising leads if CO is missing a primitive or ruling … don't swing the pendulum").**
- **Derived:** passes D1–D4′ with the record as it stands.
- **Lead:** needs one or more new statements, primitives or rulings, that the record does not have. Each is written out in CO's terms, with what else it would change, and is registered and tested as a proposed ruling. A lead becomes derived once those rulings are adopted and survive their own tests.
- **Fitted:** its exponent, prefactor, a or another quantity is chosen to land in the window. Kept as a clue, never counted as a result.

**Kill rules.**
- **K′.** A verdict at each a separately (0.1, 1, 2π). A candidate passes if it passes at all three, or at an a it fixes itself.
- **K″.** The kill is on Run 96's primary window; R1 (photoheated, aP∞ ≳ 3×10²⁷) and R6/R7 (caps at 44 and 36 μm) are reported alongside.
- A kill ends a stated candidate, not its direction. A variant that changes its new statement may be registered afresh, as a new candidate, before its value is computed.

### 4. What the record already rules out (not to be re-derived)

From Reading I5 (§2) and Note I (§6), computed against Run 93's window and still excluded under Run 96's narrower one:
- the hop and the pair, at any p_s (by length, or by the weak-field edge);
- one hold's light-crossing, ħ_tℓ, and Run 74's δu: both rename r_C, because ħ_t and δu are free;
- any identification of one renewal's energy E_pair with the Planck energy or a particle's rest energy (too short), or with a pattern's energy (state-dependent);
- the pattern's own extent (state-dependent);
- other lengths: R11's core, the medium's diffusion and Run 81's lattice-gas sound (no length without ħ_t), the 100 pc smoothing and photon coherence (bounds, not mechanisms);
- cosmic lengths (too long);
- Diósi–Penrose regularised at the hop (excluded by 22 decades), a fixed count of displaced possibility, and the threshold readings of Note I §6 (i)–(iv) (no CO-native quantity to read under the 27 October rulings);
- Reading I4's "one record per hop" (R6);
- **a deposit's kick set to light's speed:** Gμ/r_C² = c with μ = ħ/(κ_bc²) is κ_b r_C² = ℓ_P², the weak-field edge, which Run 96 reports at ≤ 3×10⁻⁵⁶, far below the floor.

So **no single statement in the record fixes r_C without a further free quantity.** Every candidate is at best a lead; the aim is the smallest set of new statements, in the ontology's own terms, with a consequence beyond r_C.

### 5. Candidates (statements only; no values computed)

**C1. Route (b) is placed by the medium, over the volume whose vacuum possibility amounts to one hold.** Written out in full in `reading_I7_C1_statement.md`.
- *New statements needed:* that route (b)'s r_C (Reading I6 ruling 3: "route (b) is exempt and localises at r_C") is set by the medium; that a hold's possibility is counted over a volume of places, where R2 counts it at a commitment's two places over ticks; and a value of ħ_t. C1 is worded as supplying ruling 3's r_C, not as extending ruling 2 to route (b).
- *Structure:* read at one moment (C1a), P∞ cancels: the volume is 2ħ_t places, so C1a is in Reading I5's ħ_tℓ class and needs ħ_t fixed. Read over the hold's duration (C1b), it becomes C2.
- *Conflicts to resolve:* Reading I4 ruling 1 (a pattern's own possibility fills its hold) is kept by separating filling from placing; to check against "the vacuum never commits" and Q1's "the medium holds no branches".

**C2. Route (b) is placed over the volume of vacuum that holds as much possibility as the pattern carries.**
- *Touches:* Reading I4 ruling 2 supplies the stock, q = 2E/E_pair, but E_pair = aħ/(ħ_tτ) brings in the free ħ_t.
- *Species:* electrons and nucleons get different r_C, since Q4's units commit on their own; a fixed stock per quantum (S-ii) conflicts with M2. So C2 is a lead that includes reopening Reading I5 ruling 5 (D4′).

**C3. A deposit's kick set to a speed the medium defines.** With light's speed it is excluded (§4). R1's outflow is units per tick, not a speed, so any other speed is a free quantity (D2′). Kept only as a lead if a speed is found in the record.

**C4. Commitment set by internal complexity.** This is the undefined reading of Note I §3 and §10 and Reading I6 §7, a programme rather than one statement.
- *Conflicts:* Reading I5 ruling 5 and Q4's "each committing on its own"; Reading I3's per-unit hold and rate, which no-signalling needs; Note I §6's exclusion of threshold readings.
- *Its distinctive consequence must go beyond what symmetrised GRW and CSL already have.* (Corrected 28 October after `checkI8/`: R = 1/[2n(2πr_C²)^{3/2}] suppresses force-noise effects, not decoherence; for decoherence the GRW-type units see configuration only above r_C, through Γ = Σλ_i(1 − e^{−d_i²/4r_C²}).)

### 6. Choices for a ruling

1. Whether D1–D5, the grading and K′–K″ are the criterion (then hashed).
2. **Whether ħ_t may be fixed by a new statement.** C1 and C2 cannot be defined without it.
3. The hop (P08's ℓ_P or the engine's) and p_s.
4. Whether an n = 1 candidate can ever count as remarkable, given that it passes almost by construction.
5. For C1: C1a, C1b, or both.
6. Whether C2 or C4 reopens Reading I5 ruling 5, with a window registered for a species-dependent r_C.

### 7. Rulings (28 October)

1. **The criterion** D1–D5, the grading (derived, lead, fitted) and K′–K″, as in §3 (Allen: "I agree with the criteria but don't swing the pendulum"; "adopt them").
2. **ħ_t may be fixed by a new statement** ("yes, if you agree"), as a lead's named missing primitive, tested against what else it touches.
3. **Both hops** (P08's ℓ_P and the engine's).
4. **C1a and C1b side by side** (Run 97).
5. **C1b's species-dependent coarseness** is judged against a window registered for it ("do as you recommend").
6. **Relic neutrinos are route-(b) units**; bounds stay within model92's non-relativistic-kick validity, with the relativistic extension a labelled variant (B16; Run 96 addendum 2).

C2 is C1b. C3 is excluded at light's speed and has a free speed otherwise. C4 stays open as a programme.

### Write-back
Pointer notes in Reading I5 (§6–§8) and Note I §10 that Run 96 supersedes n ≈ 0.44–2.1 and aP∞ ≳ 3.7×10²⁴: now n ≈ 0.70–1.18 at p_s's bound (0.35–1.16 with p_s free) and 5.25×10²⁶ ≲ aP∞ ≲ 1.78×10³⁵.

### Files
- `band.py`, `band.log`, with `model92.py`, `model93.py`, `model94.py` and `model96.py` (Run 96's registered files, unchanged).
- `reading_I7_C1_statement.md`.
- The check: `checkI7/REPORT.md`, `check_band.py`, `prefactor.py` and their logs.
