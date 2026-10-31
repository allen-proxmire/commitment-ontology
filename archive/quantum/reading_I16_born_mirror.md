## Reading I16: Born as a wave meeting its mirror

*30 October 2026. Allen's idea, in his words (14 September): "ED says that it not psi^2, its psi x psi*, its mirror image." Developed in Allen's earlier notes (July and September); Allen, 29 October: "Something in CO would have to play that role, perhaps the record itself as it reads the pattern. If CO's one-way commitment forced the counting step rather than just allowing it, that would be the first non-restatement on Born." A reading of the record and the literature; it encodes no new rule. Revised after an independent check (`checkI16/REPORT.md`, script `check_I16.py`), whose corrections are adopted; the pre-check version is `reading_I16_v1_precheck.md`. **New statement** marks a proposal needing a ruling; **inference** marks a step past what a source says.*

**In plain terms.** The answer to Allen's question is no: CO's one-way commitment does not force the counting step. A pattern's amplitude for an outcome is a complex number carrying a phase; times its mirror (its complex conjugate, what time reversal does to it) it becomes real and phase-free. That the weight is the amplitude's square, rather than another power, is CO's rule that amplitudes are √P. Why the chance of an outcome equals its share would follow from two statements. CO has the first: each record fixes one outcome. It lacks the second: a record's chance for an outcome depends only on the pattern's share in it, the same way for every record (noncontextuality). The one-way character of commitment plays no part. The argument is Logiurato and Smerzi's, an elementary relative of Gleason's theorem. For CO it is needed, one new statement, now ruled as Q6: it moves the Born rule from borrowed to added, as Reading I15 §7 did with an indifference assumption, and predicts nothing new.

### 1. The mirror: why the weight is real

A pattern in state ψ carries amplitude a_φ = ⟨φ|ψ⟩ for an outcome φ. The amplitude times its mirror is
$$
a_\varphi\,a_\varphi^{*}=\big(\sqrt{w}\,e^{i\theta}\big)\big(\sqrt{w}\,e^{-i\theta}\big)=w=|\langle\varphi|\psi\rangle|^2 ,
$$
real and independent of the phase θ; a_φ² = w e^{2iθ} is not real.

- **The mirror is time reversal (a reading).** For a spinless pattern, Wigner's time reversal is complex conjugation. For any antiunitary T, ⟨Tφ|Tψ⟩ = ⟨φ|ψ⟩*, so every antiunitary symmetry yields a*; time reversal is the natural reading, not the only one.
- **Phase-free does not fix the power.** (a a*)^p is real and phase-free for every p. That the weight is |a|², and not another power, is A5's √P. §2's merge step depends on it.
- **In CO's terms.** A5 gives amplitudes √P with phases at places. That a pattern with ΣP units carries
$$
P_\varphi=\Big(\sum P\Big)\,a_\varphi a_\varphi^{*}
$$
  units at an outcome φ of any record, not only at a place, goes past A5 (Reading I13 ruling 3 puts position values only at places). It is an **inference**, to be stated as part of A5 if adopted.
- **The backward leg (a reading).** The record is the natural candidate: the units at φ are what a record at φ can read of the pattern. It matches the bra–ket pairing ρ = ψψ† (ket forward, bra backward), Cramer's transactional handshake and Aharonov's two-state vectors, none of which predicts anything different from quantum mechanics. An earlier referee of Allen's notes found that this reading adds nothing beyond ρ = ψψ† and decoherence; that verdict stands for §1.

### 2. The counting step

**Two statements.**
- **(X) One outcome per record.** A measurement forces a pattern to commit to one channel (A1); a commitment is one irreversible update at a place. In the record.
- **(NC) Noncontextual reading** (**new statement**). For every record, with effects 0 ≤ E ≤ 1 summing to 1, the chance of the outcome with effect E is
$$
\Pr(E\,|\,\psi)=F\big(\langle\psi|E|\psi\rangle\big),
$$
  with one function F for every record. The chance depends on the pattern's share in that outcome, not on which other outcomes the record distinguishes. It is not a reading of A3, whose stamp is a place's commitment count, not a pattern's units. Read as a statement about places ("each part commits from what is at its own place"), it would be the rule Reading I3 excluded by Bell; it is a statement about outcomes, not places.

**What follows** (Busch's form; Logiurato–Smerzi's argument for effects).
- The records {E, 1 − E, 0} and {E, 1 − E} give F(w) + F(1 − w) + F(0) = 1 = F(w) + F(1 − w), so F(0) = 0.
- The records {E₁, E₂, 1 − E₁ − E₂} and {E₁ + E₂, 1 − E₁ − E₂} give
$$
F(w_1)+F(w_2)=F(w_1+w_2),
$$
  Cauchy's equation. F is a chance, so it is bounded, and a bounded solution is linear. With F(1) = 1,
$$
\Pr(E\,|\,\psi)=\langle\psi|E|\psi\rangle,\qquad \Pr(\varphi)=\frac{P_\varphi}{\sum P}=|\langle\varphi|\psi\rangle|^2 .
$$
- The additivity of shares under merging, ⟨ψ|E₁+E₂|ψ⟩ = ⟨ψ|E₁|ψ⟩ + ⟨ψ|E₂|ψ⟩, holds because the weight is the quadratic form aa*, from A5's √P. For (aa*)^p with p ≠ 1 it fails. So the merge step uses A5; the noncontextuality comes from (NC).
- In effect form the argument works in two dimensions (split E = E/2 + E/2), so no count of outcomes is needed.
- **(NC) must be stated in shares, not units.** With units, one f for every record is inconsistent: the argument forces f(x) = x/ΣP, and patterns carry different totals (Reading I4: units scale with energy).

**Does one-way commitment force it? No.** Irreversibility is used nowhere above; (X) uses only "exactly one outcome". A rule that respects (X) and is not Born (`check_I16.log`): f_n(x) = (1 − ε)x/T + ε/n, which depends on the number of outcomes. (The ratio r(φ)w(φ)/Σ r w for outcome-dependent rates is a chance conditional on a record occurring in [t, t + dt], not a record's outcome chance; the instrument for where the next record lands satisfies (NC), §6.)

What forces the count is noncontextuality, and nothing in the arrow supplies it.

### 3. Where CO's rules stand on (NC)

| rule | single-outcome form at places | effect form |
|---|---|---|
| route (b), Q4: outcome density ⟨ψ\|L_x†L_x\|ψ⟩, smeared over r_C | broken: at fixed units at x, p(x) moves (0.312 → 0.282) when units within r_C move | holds by construction (E_x = L_x†L_x, ∫E_x dx = 1) |
| route (a), (T1), Q5 | not tested | holds by construction: Born weights are written into the rulings |
| route (c), Reading I8: jump density ⟨ψ\|Π̂_x²\|ψ⟩ | broken (collective over r_C) | holds by construction |
| outcome-dependent rates (route (b)'s operator rate; route (c)'s gate) | – | holds: the first-record instrument's effects F_x (K†F_x + F_xK = E_x) are shares in effects; r w/Σ r w is a conditional chance, outside (NC)'s unconditioned effects (§6) |

So the single-outcome form is broken by ruled rules, and the effect form holds by construction wherever Born is already written in. The open case is outcome-dependent rates: whether the chance of *which* record occurs, given rates that differ by outcome, satisfies (NC) in rate form.

### 4. What is known, and what this replaces

- **Logiurato and Smerzi (2012)** prove the Born rule from noncontextuality of probability (their Postulate 2, additivity over orthogonal projectors, "equivalent to assuming NP"), for dimension N ≥ 3, with N = 2 by an ancilla. §2 is their argument for effects.
- **Gleason (1957)** assumes less: a noncontextual, additive measure on projectors in dimension ≥ 3 is Tr(ρP), with no assumption that the chance is a function of |⟨φ|ψ⟩|². **Busch (2003)** extends the trace form to effects, covering dimension 2.
- **No-signalling routes.** Simon, Bužek and Gisin (2001) assume the trace rule and derive linear, completely positive dynamics, the reverse direction. Torres Alegre (arXiv:2512.12636, unrefereed) argues that a rule Φ of the transition probability must be the identity if steering exists and signalling is excluded; it also assumes purification and that ensembles with the same average state are equivalent. Han and Choi's no-signalling bound admits power-law rules for Bell states, an instance of the same two-outcome freedom.
- **Reconstructions.** Masanes, Galley and Müller (2019) argue that the measurement postulates follow from the structural ones plus state estimation. Kent (2023) disputes this with non-quantum alternatives; their reply (Quantum 9, 1592, 2025) argues that those alternatives use pure states that are not rays.
- **The earlier attempt.** Allen's earlier notes tried to derive this noncontextuality from the locality of channels. The attempt was downgraded because the step held by definition, and only the relabelling sense survived; the sense in which a different context could change a chance stayed open. (NC) is that open sense, stated here as a principle, not derived.
- **Relation to Reading I15 §7.** I15 graded unit counting a restatement: Born moved to A5's √P plus an indifference assumption. (NC) is weaker than indifference, since the linear step is derived, but the grade is the same kind. I16 replaces I15 §7's candidate.

### 5. Grade

| claim | grade |
|---|---|
| the weight is real because it is an amplitude times its mirror; the power 2 is A5's √P | restatement (Wigner; the bra–ket pairing) |
| units at an outcome of any record | **inference**, beyond A5 |
| the record as the backward leg | reading |
| (X) one outcome per record | in the record (A1) |
| (NC) a record's chance depends only on the pattern's share in that outcome | **new statement** (noncontextuality) |
| (X) + (NC) + A5 ⇒ Pr(E) = ⟨ψ\|E\|ψ⟩ | **needed** (one new statement, ruled as Q6); in novelty a restatement of Logiurato–Smerzi |
| one-way commitment forces the count | **no** |

**What changes if (NC) is ruled.**
- A5 splits into A5a, amplitudes √P with phases and units at an outcome of any record (borrowed: the state structure), and A5b, the Born weights, which follow from (NC), (X) and A5a.
- Q2's Born outcome, Q4's hit density, route (c)'s channel and (T1)'s weights would cite (NC) instead of stating Born.
- One borrowed input is replaced by one added principle of the same content, through a known theorem. Its status changes; the number of inputs does not.
- A10 stays a requirement. Born weights are necessary for Q5's no-signalling and are already used there, but no-signalling also needs Reading I3's four rulings (deposits branch by branch, the hold per unit, the rate's Ĥ, and the instantaneous field, still open).

### 6. A next step that could fail

**T-I16b, outcome-dependent rates.** Route (b)'s operator rate ("each branch commits at its own rate") and route (c)'s gate give records whose rate differs by outcome. Write the chance that the next record lands at φ, over a finite window, and test whether it satisfies (NC) in rate form: a chance per unit time Pr(E, dt) = F(⟨ψ|E|ψ⟩, dt) with one F. Kill: a ruled rate rule whose outcome chances depend on the spread over other outcomes at first order in dt. Then (NC) contradicts the record, and either that rule changes or (NC) is declined.

**Result of T-I16b** (30 October; exploratory, not registered; `t_i16b.py`, `t_i16b.log`; checked independently, `checkI16b/REPORT.md`, whose corrections are adopted). Ensemble independence tests linearity in the state; through §2 (F is linear), a rule that depends on the ensemble cannot satisfy (NC).
- **Route (b) holds, by construction.** With the ruled rate κ_b M̂c²/ħ per unit proper time (an operator), a hit has a jump operator J_x built from the rate and L_x, and its chance in dt is
$$
\Pr(x,dt)=\langle\psi|J_x^{\dagger}J_x|\psi\rangle\,dt ,
$$
  a share in an effect. The two orderings of rate and localisation differ as rules (the unruled combined update, Reading I3 §4), but both satisfy (NC). This restates §3's table, Reading I3 ruling 5 and Run 95.
- **Where the next record lands** is an instrument with effects F_x solving K†F_x + F_xK = E_x (K = ½Σ_x E_x + iĤ₀), with ΣF_x = 1. It satisfies (NC). The ratio r w/Σ r w is a post-selection on a record occurring in [t, t + dt], not an outcome chance.
- **Route (c): (NC) excludes only a c read from the state.** Reading I10 writes the channel D[Π̂ − c], "for any real c", with c = 1 in a saturated bulk and 0 outside; the text covers uniformly saturated configurations, not superpositions of bulk and vacuum at x.
  - **A fixed field c(x)** gives jump chances ⟨ψ|(Π̂_x − c)²|ψ⟩ dt, shares in effects: (NC) holds, D[Π̂] is kept, and Runs 98–100 stand as computed.
  - **c read from the state** depends on the ensemble (0.201 against 0.265 for one mixed state in the toy). Through Q5's updates it would signal, through the distant part's later record count and deposits, not its state: the failure Reading I3 §4 item 1 names and Run 95's NL1 control detects.
  - **An operator Ĉ** (1 on bulk branches, 0 on vacuum branches) satisfies (NC) but changes the channel: D[Π̂ − Ĉ] ≠ D[Π̂] for that Ĉ. It removes route (c)'s decoherence between bulk and vacuum branches, which Reading I8 §3 rules and Reading I9 §3's Γ_dec uses, so Runs 98–100's interference bounds and edge would need recomputing.
- **A cost either way (a reading).** No fixed unravelling of D[Π̂] has zero records in both the bulk and the vacuum branch at the same x: the jump operators are u_kΠ̂ + c_k with Σ|u_k|² = 1, and a zero rate at Π = 1 and Π = 0 needs every u_k = c_k = 0. So with a fixed c = 1 in the bulk, the vacuum branches of a bulk/vacuum superposition make records, about one per cell per 1/Γ_K, which deposit nothing. Reading I9 ruling 4 ("a uniformly saturated bulk makes no record") then holds on uniform configurations only.

### 7. Choices for a ruling
1. **Record §1:** the weight as amplitude times mirror, the power from A5, the record as the backward leg (a reading).
2. **Record §2's answer:** one-way commitment does not force the counting step; noncontextuality does.
3. **(NC):** rule it as an added principle, in effect form on shares (then A5 splits and Born leaves the borrowed list), leave it open pending T-I16b, or decline.
4. **T-I16b:** run it, or park.
5. **Reading I15 §7:** mark its unit-counting candidate as superseded by this reading.

### Sources
- E. P. Wigner, time reversal (1932); standard textbook form.
- A. M. Gleason, *J. Math. Mech.* 6, 885 (1957). Standard listing, not fetched.
- P. Busch, "Quantum states and generalized observables: a simple proof of Gleason's theorem", [arXiv:quant-ph/9909073](https://arxiv.org/abs/quant-ph/9909073); *Phys. Rev. Lett.* 91, 120403 (2003).
- F. Logiurato and A. Smerzi, "Born rule and noncontextual probability", [arXiv:1202.2728](https://arxiv.org/abs/1202.2728).
- C. Simon, V. Bužek and N. Gisin, "The no-signaling condition and quantum dynamics", [arXiv:quant-ph/0102125](https://arxiv.org/abs/quant-ph/0102125).
- E. O. Torres Alegre, [arXiv:2512.12636](https://arxiv.org/abs/2512.12636), preprint.
- L. Masanes, T. Galley and M. P. Müller, [arXiv:1811.11060](https://arxiv.org/abs/1811.11060); A. Kent, [arXiv:2307.06191](https://arxiv.org/abs/2307.06191); Masanes, Galley and Müller, reply, *Quantum* 9, 1592 (2025).
- Y. D. Han and T. Choi, [arXiv:1208.2814](https://arxiv.org/abs/1208.2814).
- The record: `ONTOLOGY.md` (A1, Q1–Q5); `quantum/reading_I3_two_place_commitment.md` (A3, A5, A10, §4 and §9.5); `quantum/reading_I4_hold_rule.md`; `quantum/reading_I8_C4b_statement.md`; Reading I13 ruling 3; Reading I15 §7.

### Rulings (30 October 2026)

Allen: "do as you recommend."
1. **§1 recorded** (a reading): the weight is an amplitude times its mirror, real and phase-free; its power 2 comes from A5's √P; the record is the backward leg.
2. **§2's answer recorded:** one-way commitment does not force the counting step; noncontextuality, (NC), does.
3. **Reading I15 §7's unit-counting candidate is superseded** by this reading.

(NC) is left open. Its check (T-I16b, §6) finds no ruled rule contradicting it provided route (c)'s c is a fixed field; the choice between a fixed c and an operator Ĉ is open.

**Ruling on (NC)** (30 October; Allen: "do as you recommend"). (NC) is added as Q6, in effect form on shares. Route (c)'s unravelling constant c is a fixed field, not read from the state, so Runs 98–100 stand as computed; the vacuum branches of a bulk/vacuum superposition make records that deposit nothing. A5 splits: amplitudes √P with phases stay borrowed; the Born weights follow from Q6. The rules that state Born (Q2, Q4's hit density, route (c)'s channel, (T1)) now rest on Q6.
