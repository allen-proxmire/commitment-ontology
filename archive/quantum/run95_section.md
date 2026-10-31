### Run 95: Test I3, the two-place commitment rule against rival rules (an engine run of the commitment rules)

*27 October 2026.*
- *Registered and hashed before the run (`quantum95/PREREG_95.md`, 11 files, 19:52:10 UTC), after an independent pre-registration check (`checkPre95/REPORT.md`) whose corrections and recommended additions were adopted, and Allen's review.*
- *Validated beforehand (V1–V5, all PASS).*
- *A second independent agent checked the registered run (`check95/REPORT.md`). Its corrections are adopted below as a post hoc addendum; K95 is unchanged.*

**Why.** Reading I3 ruled the two-place rule (T1): a commitment of one part of a pattern updates the whole pattern at once, with Born weights, and commits only that part. The distant part gets no record, no stamp and no deposit.

(T1)'s correlations are QM's by construction. So the run puts (T1) side by side with the rules Reading I3 excluded, and with nonlinear controls, all under one protocol and one set of statistics. It counts only if every rival is detected as failing.

**The protocol** (`model95.py`, `run95.py`).
- **The setup:**
  - a spin singlet shared by Alice and Bob, D = 1000 hops apart; light covers a hop per tick;
  - Alice's settings {0, π/2}, or no measurement; Bob's settings {π/4, 3π/4};
  - seven orderings, t_B − t_A ∈ {±1500, ±500, ±10, 0} ticks.
- **What is measured:**
  - **Bob's interferometer:** B travels two arms at different local counts (1 and 0.98 per tick).
  - **B's deposits** are per unit and branch by branch, λ = λ_B(1 + εs_z) in a field along z, with B's branch drawn from its updated state.
  - **An energy-entangled counting variant:** α|eg⟩ + β|ge⟩, with Alice flipping her part or not.
- **The rules:**

| rule | what it does | how it should fail |
|---|---|---|
| T1 (ruled) | the first commitment updates the whole state and commits only that part | — |
| L | each part answers from its own place (the standard local model) | S = 2 |
| F1, F10, F1e4 | the update travels at v = 1, 10, 10⁴ hops per tick; outside its cone, both parts answer locally | S = 2 outside the cone |
| T2 | one commitment at both places: B stamped and given a deposit at Alice's tick | B's visibility, records at Alice's tick, deposit times |
| NL1 | B's deposit rate from its conditional state, not branch by branch | B's deposit counts |
| NL2, NL2′ | B's deposit size (and, for NL2′, rate) from a mean rate; NL2′ keeps the mean draw exact | B's deposited draw (and, for NL2′ as coded, its record count: addendum) |
| NL3 | B's outcome probability nonlinear in its conditional state | Bob's marginal |
| per pattern | the hold filled by the whole pattern's stock, so the rate seen at B is κE_tot | B's count in the energy variant |

- **The decision rule.** Eighteen tests apply to T1, at a Bonferroni-corrected 3σ (|z| > 3.791):
  - S at seven orderings, against 2√2;
  - Bob's and Alice's marginals across the other side's conditions;
  - the joint distribution across orderings;
  - B's visibility;
  - B's deposit counts, deposited draw and deposit times;
  - B's per-unit count in the energy variant.

  K95 is FAIL if T1 triggers any test or leaves a record at B carrying Alice's tick. It is PASS if T1 triggers none and all ten rivals and controls are detected. Otherwise it is UNDECIDED.

**Results (registered: K95 PASS).** 10⁶ trials per setting pair (σ_S = 0.0014), seed 95.
- **T1 triggers none of its 18 tests:**
  - S = 2.8257–2.8305 at the seven orderings, against 2√2 = 2.8284 (|z| ≤ 1.95);
  - Bob's marginal p = 0.55, Alice's p = 0.37, joint across orderings p = 0.20;
  - V_B = 1 with and without Alice;
  - B's deposits: counts p ≥ 0.19, draw KS p ≥ 0.13, times KS p ≥ 0.19, and no record at Alice's tick;
  - per-unit energy count 1.0613 against 1.0595 (z = −1.28).
- **Every rival and control is detected:**

| rule | where | result |
|---|---|---|
| L | every ordering | S = 1.999–2.002 (z ≈ −478) |
| F1 | outside its cone (0, ±10, ±500) | S ≈ 2.00 |
| F10 | outside its cone (0, ±10) | S ≈ 2.00 |
| F1e4 | outside its cone (0) | S = 1.998 |
| T2 | when Alice measures | V_B falls from 1 to 0; 2×10⁵ records carry Alice's tick; B's mean draw rises from 4.00 to 5.00 |
| NL1 | Alice at a = 0 | B's mean draw doubles, 4.00 to 8.00 |
| NL2 | Alice at a = 0 | B's mean draw halves |
| NL2′ | Alice at a = 0 | mean draw unchanged (4.001 against 4.003), but its distribution shifts (KS p ≈ 0) |
| NL3 | Alice measuring | Bob's marginal moves from 0.50 to 0.85 |
| per pattern | Alice flips A | B's count moves from 2.302 to 2.121 (z = −85) |

- **Reported:** inside their cones the travelling rules reproduce QM. F10 gives S = 2.827 and 2.830 at ±500, and F1e4 gives 2.827–2.830 at |dt| ≥ 10. So the cone logic depends on v, and a two-party test bounds v only down to D/|dt|.
- **The smallest effects T1's tests could detect:**

| test | smallest detectable effect |
|---|---|
| S | 0.0054 |
| marginals | 0.0027 |
| visibility | 0.0054 |
| B's deposit mean | 0.67% as registered; 0.85% corrected (addendum) |
| energy count | 0.52% (relative) |

**Post-run check and post hoc addendum** (`check95/REPORT.md`):
- **Integrity.** The hashes hold. Validation, smoke test and run reproduce byte for byte, and K95 was applied as registered.
- **An independent recomputation agrees.** The check used its own code and seed, with an explicit 4-dimensional singlet and Lüders projectors in both orderings.
  - It gives E = −cos(a − b) to 10⁻¹², and the run's seven T1 values of S match it (Σz² = 10.1, p = 0.18).
  - B's count distribution is identical in every Alice condition, to 3×10⁻¹⁷: the mixture Σ_o Σ_s w_o p(s|o) Poisson(μ(1 + εs)) has mean 4 and variance 8 in each.
  - All 28 L and F rows match their analytic local or QM values (worst |z| = 2.8).
- **Which of T1's tests could respond.** Every test can fail only through a coding error, as the registration said. Six of the 18 cannot respond to anything in the suite:
  - **visibility:** T1's p₀ = 1 and p_π = 0 exactly, so z ≡ 0. The listed smallest detectable visibility describes no test that was run;
  - **the two draw KS tests:** for T1 the draw equals the count, so they reuse the count tests' data. KS on discrete data is conservative: in a null study, median p = 0.79 and P(p > 0.99) = 0.19, which is where the p = 1 values come from;
  - **the two times KS tests:** deposit times are uniform for any rate that does not depend on time, so they respond only to T2's deposits at tick 0 (NL1 at a = 0: counts p = 0, times p = 0.48);
  - **the per-unit energy count:** both samples come from the same expression for B's energy, so its z = −1.28 is a draw from N(0, 1) by construction.

  The other 12 (S, the marginals and joint, the counts) respond as designed.
- **Fixed by construction.** The records count at Alice's tick is set in the code, not counted. Every rival's detection follows from its definition. The deposits' no-signalling reduces to one identity,
$$
P(s_z=+1)=\mathbb E_{o}\Big[\tfrac12\big(1-o\cos a\big)\Big]=\tfrac12\quad\text{for every }a,
$$
  which any conditional ⟨σ_z⟩ odd in o satisfies. So the deposit test catches only an error in the conditional's form; it is not an independent check of ruling 5.
- **NL2′ is not the reading's concern as coded.** It used ⟨λ⟩ = λ_B(1 + |⟨σ_z⟩|), not the state mean of the rate model, λ_B(1 + ε⟨σ_z⟩). So its record count doubles at a = 0 (z = +517), and "only the shot noise changes" was wrong.
  - A faithful version keeps rate λ_B(1 + ε⟨σ_z⟩) and size E_TK/⟨λ⟩. The count test is blind to it (z = +0.1), and the draw KS still catches it (p ≈ 0). K95 would not change.
  - NL1 likewise drops ε. NL2's "rate left at λ_B" in fact keeps the branch rate λ_B(1 + εs_z).
- **The smallest detectable deposit effect is 0.85%, not 0.67%.** The run used a per-trial variance μ(1 + ε²) = 5. The true variance is μ + (εμ)² = 8. "Smallest detectable" means 50% power, and it covers only the mean count. A 1% shift is detected 75% of the time.
- **Minor:**
  - the no-measurement condition in the marginal tests is a fair coin for every rule (correct here, but a label);
  - the two arms' local counts are declared but not used;
  - the Bell, marginal, visibility and deposit blocks are separate ensembles. At the engine's ε = 0.5, B's deposits would be a strong measurement of its spin, and that back-action is not carried into the Bell block. The registration's claim that it is negligible rests on physical rates, not on the engine values.

**Reading.**
- **The ruled rule passes, and every rule Reading I3 excluded fails, each where the reading said it would.**
  - A local commitment, and a travelling one outside its cone, lose Bell's violation.
  - One commitment at both places changes what Bob sees: his fringe, and the records and draw at his part.
  - Rules that set B's deposits from its conditional state let Alice's setting show up in Bob's deposits, even when the mean draw is kept exact.
  - A hold filled by the whole pattern's stock lets Alice change Bob's count.
- **What CO needs for Bell is therefore specific:** one part's commitment updates the whole pattern at once and commits only that part, with deposits, holds and rates counted per unit and branch by branch.
- **It is a consistency check, not a prediction.** (T1)'s correlations are QM's, its visibility enters as a label, and every rival's failure is fixed by its definition (addendum). What is CO's own is the set of requirements; the run shows they are coherent together and that each rival violates one of them.
- **Not covered:**
  - CO's medium itself: the run is a Monte Carlo of the commitment rules with places and counts as labels;
  - the instantaneous field (R4's open item);
  - the singlet's origin (an input);
  - the Born rule (borrowed).

**Carried forward:**
- the line between matter and pattern: when a detector counts as committed matter, which decides which commitments are route (a);
- how interactions make two-part patterns;
- whether the engine's foliation is the cosmic frame, and whether the update's moment makes the tick physical;
- "signalling through the constraint" (R4);
- if wanted as a real test: a follow-up with the faithful mean-preserving control, B's deposit back-action in the Bell block, and the non-responding tests replaced.
