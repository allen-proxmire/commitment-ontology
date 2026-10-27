## Reading I3: what happens at the distant part when one part of a pattern commits (a reading, before Test I3)

*27 October 2026. Checked independently (`checkI3/REPORT.md`); its corrections are adopted below; ruled the same day (§9). Nothing here is registered.*

**The question** (Note I §8, I3). Register the two-place commitment rule first: what happens at the distant part when one part commits, and in which frame. Then show the singlet correlation E(a, b) = −cos(a − b), so CHSH = 2√2, with each side's marginals independent of the other side's setting. Note I adds: "An engine that simply encodes a tensor-product state with Born-rule joint outcomes reproduces the earlier papers' route. What would be new is the two-place commitment rule."

Reading I1 left one item waiting on this one. Under its option (R-a3), "a photon's absorption commits a distant molecule, a two-place commitment that Note I's I3 requires to be registered first" (§5 below).

### 1. What the record says

| item | statement | source | standing |
|---|---|---|---|
| A1 | QM is what happens before ticking; a measurement forces a pattern to commit to one channel | ONTOLOGY §1, stated 23 October | CO's own |
| A2 | a pattern commits (a) by interacting with the committed world, or (b) on its own | ONTOLOGY §1, stated 25 October; route (b) ruled a rate 27 October | CO's own |
| A3 | a commitment is stamped with the local count at the place where it happens; a stamp at a place makes the channels position-like | ruled 26 October; Note I §5 | CO's own |
| A5 | amplitudes √P with phases, weighted by the Born rule | Run 16; Run 14's withdrawn event layer | **borrowed** |
| A10 | the commitment rule is nonlocal in Bell's sense, and no-signalling | Note I Appendix A, point 4 | a requirement |
| (C) | a pattern draws only where and when it commits; the medium holds no branches | Reading I0, ruled 27 October | CO's own |
| M3 | each record deposits the pattern's draw E_TK/λ_tot at the recorded place, smeared at r_C | ONTOLOGY §1, ruled 27 October | CO's own |
| route (a) | a record is made at the interaction, when committed matter keeps which-path information, with the standard coherence kernel | Reading I1, ruled 27 October | CO's own |
| route (b) | symmetrised GRW-type, with the operator rate κ_bĤ/ħ | ONTOLOGY §1; Reading I1 §9 | ruled 27 October |
| R4 | the field is re-solved on each slice; the engine's tick is not physical time | ONTOLOGY R4; write-up | ruled; "signalling through the constraint" is open beyond first post-Newtonian order |
| the foliation | the engine has one global hop rate. Listed among the engine's choices, "not claims about nature"; a local tick is under consideration (Run 77) | ONTOLOGY engine table; Note I Appendix A, point 4 | engine choice |
| dissolved relations | in Note G a relation is a link between neighbouring places of the medium (reading (A) of how space curves). A dissolved link "goes back to possibility as a two-part pattern, as in entanglement" and keeps its two ends tied. Whether this is CO's account of entanglement, and how interactions make two-part patterns, are not stated | Note G (22 October); Note I §2 | stated, open |
| the earlier papers | the ED entanglement arc (Papers 063–072, by its own README and ledger) reconstructs the tensor product, Schmidt form, monogamy, no-signalling and the Tsirelson bound. Its "locality without superdeterminism" (a local, stochastic commitment) fails Bell, as Note I corrects | ED `entanglement/`; Note I Appendix A, point 4 | restatements; a caution |

Note I Appendix A already established the main constraint. A commitment rule that is local in Bell's sense gives CHSH ≤ 2 whatever the pattern is. So CO's rule must make the joint outcome of a pattern's two parts not factorise, while each side's marginals stay independent of the other side's setting. Most of what follows applies that standing point; what is new is the rule, and what it requires of CO's own primitives.

### 2. The constraints a rule must meet

- **Q3, Bell.** Loophole-free tests give S > 2 (Hensen et al. 2015; Storz et al. 2023). The target is QM's E(a, b) = −cos(a − b) for the singlet:
$$
S=|E(a,b)-E(a,b')+E(a',b)+E(a',b')|=2\sqrt2\quad\text{at the optimal settings},
$$
  and nothing above Tsirelson's 2√2.
- **Q4, no-signalling.** Bob's statistics must not depend on Alice's setting, or on whether or when she measures.
- **Q8, the speed of influence.**
  - Bancal et al. (2012) prove the following. Take a model whose hidden influence travels at a finite speed v > c in a privileged frame, and which reproduces QM in every configuration where the influence arrives in time. Then a four-party setup lets it signal (Barnea et al. 2013 report a three-party version).
  - For two parties the theorem does not apply. There a finite-speed model simply predicts S ≤ 2 when the measurements lie outside each other's v-cone: a testable deviation, not signalling.
  - Salart et al. (2008) and Yin et al. (2013) bound v above about 10⁴c, but only for privileged frames in which the Earth moves slower than about 10⁻³c. The cosmic rest frame, the natural candidate for CO's foliation, lies just outside that: the Earth moves at β ≈ 1.2×10⁻³ relative to it.
  - So a rule that reproduces QM in every configuration, multipartite included, must update simultaneously in its frame. That follows from Bancal's theorem, not from the experiments alone.
- **CO's own (an inference from A3, (C) and M3).** Whatever happens at the distant part must leave no stamp and no deposit there. A stamp makes the channels position-like (Note I §5), and a deposit is a draw at a time Alice could choose. Either would let Alice's choice change something Bob could, in principle, see.

### 3. The candidate rules

**(L) Each part commits on its own, from what is at its own place.** Local in Bell's sense, so CHSH ≤ 2 for any pattern (Note I Appendix A). The earlier essay's "locality without superdeterminism" and Paper 066's postulate that the cross-chain kernel vanishes at spacelike separation are of this type. **Excluded by Q3.**

**(F) The commitment travels to the other part at a finite speed.**
- At the hop speed this is an influence at c, which is (L): excluded by the loophole-free tests directly.
- At any finite v > c, it reproduces QM in every configuration only at the price of signalling in a four-party setup (Bancal et al.). In two-party tests it predicts S ≤ 2 outside the v-cone.

**Excluded,** as a rule meant to reproduce QM everywhere.

**(T2) One commitment at both places.** The pattern commits as one event with two places, as R2's commitment has two places: A's detection commits B too, stamped with B's local count and depositing its draw there.
- **The stamp.** Even a commitment that touches only B's spin, if stamped with B's local count, tells B's paths apart wherever their counts differ (A3; Note I §5). So Bob's interference visibility would depend on whether Alice measured.
- **The deposit.** M3 lays B's draw down at a time Alice chooses. That is a second, independent signal.
- **The size.** At localisation width r_C much larger than B's path separation, the visibility signal is unobservably small. So (T2) fails Q4 in principle, not by experiment.
- **No restriction saves it.** Dropping the stamp and the deposit leaves "committed at B" with no operational content, which is (T1).

**Excluded by Q4.**

**(T1) A commitment of one part updates the whole pattern, and commits only that part.**
- When part A commits, the pattern's whole state is updated at once in the foliation, with Born weights (A5). For route (a) at Alice's detector:
$$
|\Psi\rangle\ \to\ \frac{(\hat\Pi^A_{o}\otimes\hat 1)|\Psi\rangle}{\|(\hat\Pi^A_{o}\otimes\hat 1)|\Psi\rangle\|},\qquad p(o)=\langle\Psi|\hat\Pi^A_{o}\otimes\hat1|\Psi\rangle .
$$
- **Part B is not committed.** It gets no record, no stamp and no deposit. It stays between commitments until it meets matter or route (b) fires, and its later outcomes follow the conditional state.
- **How it relates to route (b).** Any collapse operator acting on a joint state updates it nonlocally, whether labelled, GRW-type or CSL-type; symmetrisation is about identical units and plays no part here. But route (b)'s hits are position-like, so they do not measure spin. GRW reproduces spin correlations only through a pointer whose position is correlated with the spin, and in CO that pointer is committed matter: route (a). So route (b) gives (T1) only for patterns entangled in position. For the Bell case, (T1) is a new ruling for route (a).
- **Predictions.** For the singlet measured along a and b,
$$
p(o_A,o_B\mid a,b)=\tfrac14\big(1-o_Ao_B\cos(a-b)\big),\qquad E(a,b)=-\cos(a-b),\qquad p(o_B\mid a,b)=\tfrac12 ,
$$
  so S = 2√2 at the optimal settings. Bob's reduced state is unchanged by Alice's measurement:
$$
\rho_B=\mathrm{Tr}_A\Big[\sum_o(\hat\Pi^A_o\otimes\hat1)\,|\Psi\rangle\langle\Psi|\,(\hat\Pi^A_o\otimes\hat1)\Big]=\mathrm{Tr}_A|\Psi\rangle\langle\Psi|
$$
  (verified numerically in the check, to 6×10⁻¹⁷).
- **The frame.**
  - The Bell statistics do not depend on the foliation, because local operations at A and B commute and the local dynamics is linear.
  - That does not make every statistic foliation-free. A rate defined in a frame, such as route (b)'s per-radian rate if M2 is read in the cosmic frame, is a preferred-frame observable, as in nonrelativistic GRW. Tumulka's relativistic GRW (2006), which needs no preferred slicing, covers only non-interacting distinguishable particles.
  - **(T1) gives the engine's global tick a physical job:** the moment of the update. R4 says the engine's tick is not physical time, and Note I §5 gives that as one reason for the local stamp. This is consistent only while no observable depends on the update's moment, which holds for the Bell statistics. The joint record itself carries only local counts (A3). Counts at two places run at different rates and carry no global order, so the update's ordering is used but recorded nowhere.

**(T3) The dissolved relation is kept: the two parts stay neighbours in the relational graph.**
- If the parts stay linked, an update across that link is local in the graph.
- Under reading (A), though, a relation is spatial adjacency, which is what lets the medium hop. A kept relation that "carries nothing but the pattern" would be a new kind of relation, needing its own ruling. A relation the medium could cross would be a shortcut, and so a signal and a gravitational anomaly.
- (T3) makes (T1)'s predictions only if the update crosses the link in the same engine tick. A one-hop delay would be (F), open in principle to Bancal's argument for events less than a tick apart.
- The closer precedent in the earlier papers is Paper 072 and the essay's "pre-metric" relation, which was paired with a local commitment and so failed Bell. Paper 071's echo is a postulate that one kernel object is shared between entanglement and black holes, not graph adjacency.

So (T3) is at most an interpretation of (T1)'s "at once", and only after a ruling on a new kind of relation.

### 4. What (T1) requires of CO's other rules

No-signalling inside CO needs more than the projector formula. The check found four places where it must be secured:

1. **Deposits branch by branch.** M3 deposits E_TK/λ_tot. If a deposit's size or timing used the current state's mean ⟨λ_tot⟩, B's shot noise would be nonlinear in B's state, and Alice's commitment, which changes B's conditional state, could signal through it. So the deposit has to be defined in operator form, branch by branch.
2. **A per-unit hold.** Reading I4's "stock the pattern itself carries" has to be counted per unit. If a two-part pattern's whole stock filled one hold, Bob could change A's commitment rate by changing B's energy.
3. **The operator rate leaks energy.** Under κ_bĤ/ħ per unit, branches of different energy are told apart at
$$
\Gamma\approx\frac{\kappa_b\,\Delta E^2}{8\hbar E}.
$$
   - So route (b) partly collapses a spin singlet in a magnetic field: for an electron in 1 T, Γ ≈ 9×10⁻¹¹ s⁻¹ at the Q7 cap and 1.3×10⁻²⁴ s⁻¹ at the lunar-laser-ranging cap. That is negligible, but it means route (b) is not wholly blind to spin.
   - Two things are not ruled: whether Ĥ in the rate is per unit or per pattern, and route (b)'s combined update for a hit with an operator rate (the square root of the rate operator times the localisation).
4. **The instantaneous field.** R4 re-solves the field on each slice, so when A's record and deposit happen is felt at B at once. This is the record's open item "signalling through the constraint". It is not specific to entanglement, but I3's no-signalling rule must include it or state that it is excluded.

**Two items that need nothing:**
- **The time-averaged count (A4)** only turns the redshift phase of energy-entangled pairs, as in standard QM.
- **Route (b) on position-entangled pairs.** The correlation is lost at
$$
\Gamma=\sum_k\lambda_k\big(1-e^{-D_k^2/4r_C^2}\big),
$$
  with D_k each part's branch separation, not the distance between A and B. The bare rate is up to about 0.4 s⁻¹ per nucleon at the lunar-laser-ranging cap, but that cap applies only for r_C ≳ 3×10⁹ m. There, D²/4r_C² ≈ 8×10⁻²¹ at D = 0.54 m, so Γ ≈ 5×10⁻¹⁹ s⁻¹ for an atom pair. At laboratory r_C, W's upper edge is lower still. Negligible.

### 5. Closing Reading I1's (R-a3)

(R-a3) deferred a route-(a) commitment until the carrier was itself recorded: "a photon's absorption commits a distant molecule". That is a (T2)-type rule. The molecule's deposit would happen when the photon is absorbed far away, at a time a remote party controls (absorb now, or delay the photon in a fibre loop). That signals through M3 and gravity, in principle. (Its visibility would not change, since coherence is lost at the entangling event.) So (R-a3) is excluded on the same grounds as (T2), and Reading I1's ruling 3, that the record is made at the interaction, stands.

### 6. What a test can check

- **Under (T1) the correlations are QM's.** An engine run implementing (T1) reproduces E = −cos(a − b) and S = 2√2. That is a consistency check and a relabelling risk (Note I §5's phrase for route (a)), not a prediction.
- **As first drafted, the kill rules could fail only through a coding error,** since (T1) puts in the formula it then checks. A run becomes informative only if it also shows that the rival rules fail. The check's design:
  - **Setup.** Two regions on the lattice, much more than a hop apart. A spin singlet, with B also on a two-arm path whose arms sit at different local counts (to probe A3).
  - **Alice's options:** settings {0, π/2}, or no measurement, at engine tick t_A. **Bob's options:** settings {π/4, 3π/4} at t_B, with t_B − t_A swept through both orderings, then B's arms recombined to read the visibility V_B. A probe near B logs the times and sizes of B's deposits.
  - **Rules run side by side:** (L) at its best; (F) at a range of v; (T2) with stamp and deposit at B; (T1); and two nonlinear controls (B's rate set by ⟨Ĥ_B⟩, and deposits set by ⟨λ_tot⟩).
  - **Statistics:**
    - S, over about 10⁶ trials (σ_S ≈ 0.003);
    - a χ² test of Bob's marginals across Alice's three conditions;
    - V_B with and without Alice measuring;
    - a Kolmogorov–Smirnov test of B's deposit times;
    - the joint distribution under both orderings;
    - any record at B that carries Alice's tick.
  - **Kill rules for (T1):** S outside 2√2 ± 3σ, or any 3σ (Bonferroni-corrected) dependence of those statistics on Alice's condition or on the ordering.
  - **The run counts only if** (T2), (F) inside the v-cone, and both nonlinear controls are detected as failing. Otherwise it is a tautology.
  - **A variant:** an energy-entangled pair (|eg⟩ + |ge⟩) with per-unit operator rates, to check §4's Γ and Bob's marginal.
- **What would make I3 more than a consistency check** is not in the record:
  - how a Note G dissolved relation, born between neighbouring places of the medium, becomes two separated massive parts in a singlet;
  - a derivation of the Born weights, which A5 borrows.

### 7. What this means

- **The record and three constraints force the form of the rule.** Bell excludes a local commitment (L). Reproducing QM everywhere excludes a travelling one (F). No-signalling, with A3, (C) and M3, excludes committing both places (T2). What survives is (T1): a commitment of one part updates the whole pattern at once in a foliation, and commits only that part.
- **(T1) is new for route (a).** Route (b) gives it only for position-entangled patterns.
- **Its numbers are QM's,** so I3 as an engine run checks consistency. It is informative only with the rival rules and nonlinear controls shown to fail.
- **No-signalling inside CO needs four further things:** deposits defined branch by branch, a per-unit hold, a ruling on the rate operator's Ĥ, and a decision on the instantaneous field.
- **(R-a3) is excluded,** so Reading I1's ruling 3 (at the interaction) stands.
- **The open items stay open:** how interactions make two-part patterns, and the Born rule.

### 8. Choices for a ruling

1. **The two-place rule:** (T1).
2. **(T3):** left as a possible interpretation, needing a new kind of relation; or set aside.
3. **The distant part:** no record, no stamp and no deposit from the other part's commitment.
4. **The frame:**
   - the engine's global tick, accepted as the update's moment and recorded nowhere;
   - whether it is the cosmic rest frame (tied to M2's open per-radian ruling, and outside Salart's and Yin's coverage);
   - whether giving the tick this job makes it physical, against R4.
5. **No-signalling inside CO:** deposits defined branch by branch (operator form); the hold counted per unit; the rate operator's Ĥ per unit or per pattern, and route (b)'s combined update; the instantaneous field, included in I3's kill rule or excluded explicitly.
6. **(R-a3) excluded,** closing Reading I1's open item.
7. **Whether to run I3:** as a registered engine run with the rival rules and controls of §6, or record (T1) as a reading only.
8. **How interactions make two-part patterns:** left open, or ruled to be ordinary entangling evolution between commitments (which makes the singlet an input).
9. **The Born rule:** stays borrowed (A5).

### Sources
- J. S. Bell, *Physics* 1, 195 (1964).
- B. Hensen et al., *Nature* 526, 682 (2015); S. Storz et al., *Nature* 617, 265 (2023).
- D. Salart et al., *Nature* 454, 861 (2008) (privileged frames with β < 10⁻³); J. Yin et al., *Phys. Rev. Lett.* 110, 260407 (2013).
- J.-D. Bancal et al., *Nat. Phys.* 8, 867 (2012) (four parties); T. J. Barnea et al., arXiv:1304.0532 (2013) (three parties).
- G. C. Ghirardi, A. Rimini and T. Weber, *Phys. Rev. D* 34, 470 (1986).
- R. Tumulka, *J. Stat. Phys.* 125, 821 (2006) (a relativistic GRW model, for non-interacting distinguishable particles).
- N. Gisin, *Phys. Lett. A* 143, 1 (1990).
- B. S. Tsirelson, *Lett. Math. Phys.* 4, 93 (1980).

### 9. Rulings (27 October, "as recommended")

1. **The two-place rule is (T1):** a commitment of one part of a pattern updates the whole pattern at once, with Born weights, and commits only that part.
2. **(T3) is set aside.** It would need a new kind of relation, one the medium cannot cross.
3. **The distant part gets no record, no stamp and no deposit** from the other part's commitment. It stays between commitments until it meets matter or route (b) fires.
4. **The frame.** The engine's global tick fixes the update's moment, which is recorded nowhere. Two things stay open: whether that tick is the cosmic rest frame (with M2's per-radian ruling), and whether this job makes the tick physical (R4).
5. **No-signalling inside CO:**
   - deposits are defined branch by branch, in operator form;
   - the hold is counted per unit;
   - the rate operator's Ĥ is per unit, consistent with units committing on their own;
   - the instantaneous field is excluded from I3 explicitly. It stays R4's open item, "signalling through the constraint".
6. **(R-a3) is excluded.** This closes Reading I1's open item: a route-(a) record is made at the interaction.
7. **I3 is run as a registered engine run,** with the rival rules and nonlinear controls of §6, and counts only if they are detected as failing.
8. **Two-part patterns come from ordinary entangling evolution between commitments.** The singlet is therefore an input, not derived.
9. **The Born rule stays borrowed (A5).**
