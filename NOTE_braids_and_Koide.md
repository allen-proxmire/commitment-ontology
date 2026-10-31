# Note: particles as renewing braids, and Koide's relation

*31 October 2026. Worked out in conversation with Allen. A reading with arithmetic, not a registered test. Nothing here is derived from CO's primitives; it is a picture in CO's terms that puts the lepton mass relation on two simple statements about a renewal.*

## 1. The picture
- **Particles as braids.** A particle is a closed braid of three commitment chains, each re-making itself. It follows Bilson-Thompson (2005): with twist t_i ∈ {−1, 0, +1} on each strand, all non-zero twists of one sign, the charge is
$$Q_{\rm el}=\frac e3\sum_{i=1}^3 t_i ,$$
  which gives the electron (three −), the neutrino (none), the down quark (one −) and the up quark (two +). Which strand carries the odd twist gives three colours.
- **Why charge is conserved.** Removing a twist would undo a commitment, which the arrow forbids.
- **The middle strand.** The braid group's two crossings, σ₁ (strands 1–2) and σ₂ (strands 2–3), meet only at the middle position. That is Allen's earlier "the centre route sees the other two".

## 2. Renewal and mass
- **The renewal operator.** Over one renewal the closed braid σ₁σ₂ carries strands around 1 → 2 → 3 → 1. An amplitude can stay on its strand (a), move forward (b e^{iφ}) or move back (b e^{−iφ}):
$$R=a\,\mathbb 1+b\big(e^{i\varphi}S+e^{-i\varphi}S^{-1}\big),\qquad \lambda_k=a+2b\cos\!\Big(\varphi+\frac{2\pi k}{3}\Big).$$
- **Mass is upkeep.** The possibility consumed per renewal is |amplitude|² (conserved possibility under mixing hops; archive Q1(a)). So m_k ∝ λ_k², and √m is the amplitude. This is Brannen's form,
$$\sqrt{m_k}=\mu\Big(1+A\cos\big(\delta+\tfrac{2\pi k}{3}\big)\Big),\qquad \mu=a,\quad A=\frac{2b}{a},\quad \delta=\varphi .$$

## 3. Two statements about a renewal

**(i) Fair binary choice gives the amplitude.** Koide's relation is
$$Q=\frac{\sum m}{(\sum\sqrt m)^2}=\frac{1}{3\,p_{\rm stay}},\qquad p_{\rm stay}=\frac{a^2}{a^2+2b^2},$$
so Q = 2/3 holds exactly when p_stay = ½, that is when |a|² = 2|b|²: **the possibility that stays equals the possibility that moves.** The split (½, ¼, ¼) is what two unbiased binary commitments in sequence give: keep or pass, then, if passing, forward or back. A flat three-way split gives Q = 1.
- **Why fair (a reading):** places have no identity of their own ("sliding places costs nothing"), and lepton strands carry no net handedness.

**(ii) Counted action gives the phase.** A phase is action over ħ. If one commitment carries ħ, a phase from counted commitments is a plain fraction in radians, not a fraction of 2π. Over one renewal the braid visits 3 strands × 3 steps = 9 strand-steps, sharing one commitment's action between them. A forward hop passes the braid's 2 crossings:
$$\delta_{\rm leptons}=\frac{2}{9}\ {\rm rad}.$$
- **The fit:** δ = 0.2222220(19) from the measured masses, against 2/9 = 0.2222222.

**The two do not come from one count.** Sharing possibility by slot count gives a² = b² and Q = 1. The balance needs its own rule, (i).

## 4. Consequences and checks

**Charged leptons**

| assumption | predicted m_τ (with m_e, m_μ exact) | the other number |
|---|---|---|
| δ = 2/9 exact (counted action) | 1776.9665 MeV | Q − 2/3 = −1.4×10⁻⁷ |
| Q = 2/3 exact (Koide) | 1776.9690 MeV | δ − 2/9 = −1.8×10⁻⁷ |

- **Measured:** 1776.93 ± 0.09 MeV (world average).
- **The two exact claims are 2.5 keV apart**, beyond foreseeable precision. A correction of 10⁻⁷ is also the size of radiative effects, so a sharper statement would need to say which masses (pole or running) the counting applies to.

**Neutrinos** (A = √2 kept; NuFIT 6.0 normal-ordering splittings, Δm²₂₁ = 7.49×10⁻⁵ eV², Δm²₃₁ = 2.513×10⁻³ eV²)
- **There is one solution:** m₁ = 0.36 meV, m₂ = 8.66 meV, m₃ = 50.1 meV, Σm_ν = 59.2 meV, normal ordering.
- **This is Brannen's prediction, not CO's.** Brannen (2006) applied the Koide form to neutrinos and predicted about 0.38, 8.9 and 50.7 meV. The values here differ only through updated oscillation data. It tests the braid reading, not CO's rules, and so it is not listed in `TESTS.md`.
- **Kill tests:**
  - an inverted ordering (JUNO);
  - Σm_ν below 0.059 eV from cosmology. The current bound is about 0.064 eV (DESI DR2, ΛCDM).
- **The phase:** δ_ν = 0.4793 (1σ 0.4755–0.4829).

| candidate | δ_ν | pull |
|---|---|---|
| Brannen, 2/9 + π/12 | 0.4840 | 1.3σ |
| a count with 27 slots, 13/27 | 0.4815 | 0.6σ |
| 4/9 | 0.4444 | −8.4σ |
| 1/2 | 0.5000 | +6.0σ |

  A 1/27 grid lands inside the 1σ window by chance about 20% of the time, so this does not discriminate. It shows only that the neutrinos do not break the counted-action reading.

**Quarks** (Q = 1/(3 p_stay))

| triple | Q, standard masses | Q, running at M_Z | p_stay |
|---|---|---|---|
| e, μ, τ | 0.66666 | — | 0.5000 |
| u, c, t | 0.849 | 0.888 | 0.38–0.39 |
| d, s, b | 0.731 | 0.748 | 0.45 |
| c, b, t | 0.669 | 0.720 | 0.46–0.50 |

- **Quarks are not a fair binary at the root**, consistent with colour entering the renewal's first choice.
- **Near-fractions at M_Z:** Q(u, c, t) ≈ 8/9 and Q(d, s, b) ≈ 3/4. Quark masses depend on scale, so this is suggestive only.
- Brannen's quark phases, 2/27 and 4/27, fit the same counting with a factor of 3 for colour. His fits are loose.

## 5. Why three strands (a reading)
In the braid picture, the number of strands n is also the number of families: the renewal operator on n strands has n eigenmodes,
$$\lambda_k=a+2b\cos\!\Big(\varphi+\frac{2\pi k}{n}\Big),\qquad k=0,\dots,n-1,\qquad Q_n=\frac{1}{n\,p_{\rm stay}} .$$
So "why three families" and "why three strands" are the same question. The braid group gives a two-sided answer.
- **n = 2 is too few.** The braid group has one generator and is abelian: a pair can only twist. Forward and back are the same move, so a renewal's second fair choice (which way) does not exist. With two families a mixing phase can be removed, so there is no CP violation (Kobayashi–Maskawa).
- **n = 3 is exactly right.** There are two generators, and they do not commute: σ₁σ₂σ₁ = σ₂σ₁σ₂, but σ₁σ₂ ≠ σ₂σ₁. Every crossing involves the one middle strand, which sees both others, so the pattern cannot be split into parts that ignore each other.
- **n ≥ 4 is too many.** Distant crossings commute (σ₁σ₃ = σ₃σ₁), so a pattern can contain pieces that evolve independently, and it is no longer one irreducible pattern. There is also no single middle strand.

**So 3 is the only strand number** where the braid group is non-abelian and no two generators commute: the least that has structure and the most that stays one piece.
- **Linked statement (a reading).** The arrow forbids undoing a crossing (σᵢσᵢ⁻¹ = 1 would need an undone commitment), so renewal patterns live in the positive braid monoid, not the full group.

### A selection principle (an idea kept)
**Allen:** the world settles into the arrangement that maximises the number of patterns that can sustain themselves. In braid terms the candidate is: count, for each n, the distinct closed positive braids that renew without unravelling and do not split into independent parts. Then ask whether that count is greatest at n = 3. The criterion above says only n = 3 gives irreducible interacting patterns. A count would make the principle non-circular. It has not been done.

### The count (31 October)
**The rule, fixed before counting:**
- **A pattern:** a closed positive braid on n strands, identified up to cyclic rotation (a renewal has no start). Braid equality is checked through the faithful Artin action on the free group.
- **It sustains itself** if it is one piece (its permutation is a single n-cycle), unsplittable (it uses every generator) and primitive (not a power of a shorter word).
- **The cost of one renewal** is B = n + L: one commitment per strand plus one per crossing.
- **The principle:** the n with the most self-sustaining patterns at each budget.

**Result: the pre-stated principle does not select 3.** Only odd B gives patterns, for a parity reason.

| B | n = 2 | n = 3 | n = 4 | n = 5 | n = 6 |
|---|---|---|---|---|---|
| 5 | 0 | **1** | 0 | 0 | 0 |
| 7 | 0 | **2** | **2** | 0 | 0 |
| 9 | 0 | 5 | **10** | 4 | 0 |
| 11 | 0 | 8 | **40** | 32 | 8 |
| 13 | 0 | 17 | 153 | **198** | 89 |

- n = 2 never has a self-sustaining pattern: only powers of σ₁ exist.
- Raw counts favour more strands as the budget grows.

**A variant chosen after seeing the result** (post hoc, not a test): the share of all patterns at a budget that sustain themselves.

| B | n = 3 | n = 4 | n = 5 | n = 6 |
|---|---|---|---|---|
| 9 | **0.50** | 0.28 | 0.08 | – |
| 11 | **0.50** | 0.34 | 0.14 | 0.03 |
| 13 | **0.52** | 0.37 | 0.18 | 0.06 |

With three strands about half of everything that can be built holds together; with more strands most of it falls apart. On this reading the principle is "the arrangement in which patterns built at random most often last", not "the most patterns". Because it was chosen after the count, it counts as evidence only if it is stated in advance and holds on a test not yet run: larger budgets, or a different property.

*Correction (31 October).* The two tables above used a weaker equivalence: rotations of each word were compared separately, so some patterns that are the same braid were not merged. Recounted exactly, with the braid relations and rotation closed together and checked by an independent second method (free-group action plus rotation, as connected components), the shares are:

| B | n = 3 | n = 4 | n = 5 | n = 6 |
|---|---|---|---|---|
| 9 | **0.29** (2/7) | 0.11 (2/18) | 0.04 (1/28) | – |
| 11 | **0.27** (3/11) | 0.14 (6/43) | 0.04 (3/79) | 0.01 (1/101) |
| 13 | **0.35** (7/20) | 0.17 (20/116) | 0.05 (11/234) | 0.01 (4/326) |

Three strands still leads at every budget.

### Stated in advance (31 October, before the larger count)
**Principle S:** among strand numbers n ≥ 2, the share of patterns that sustain themselves at a given renewal cost B is largest at n = 3.
- **Patterns** are classes of positive braid words of length L = B − n, under the braid relations and cyclic rotation.
- **Sustaining** means one piece, unsplittable and primitive, with primitive meaning that no word in the class is a power.

**The test:**
- Exact enumeration with these equivalences built directly from the positive-monoid relations, checked first against the counts above at B ≤ 13.
- The cases: B = 15 for n = 2…7, and B = 17 for n = 3 and 4. Larger cases are too large to enumerate here.
- **Kill rule:** S fails if any n ≠ 3 has a share at least as large as n = 3 in any tested case.

### Result of the pre-stated test: S survives

| B | n = 2 | n = 3 | n = 4 | n = 5 | n = 6 | n = 7 |
|---|---|---|---|---|---|---|
| 15 | 0 (0/1) | **0.41** (17/41) | 0.23 (83/355) | 0.08 (66/845) | 0.02 (21/1165) | 0.004 (5/1379) |
| 17 | – | **0.49** (40/81) | 0.27 (331/1208) | – | – | – |

At every tested budget, three strands has the largest share of self-sustaining patterns, by a factor of about 1.8 over four and much more over five and up. Two strands never sustains.

**Limits:**
- Small budgets only.
- The shares for n = 3 and n = 4 are both still rising: 0.29 → 0.49 and 0.11 → 0.27. Whether four ever overtakes at large B is open; the ratio has fallen from 2.6 to about 1.8.
- "Sustaining" means one piece, unsplittable and primitive. Nothing about dynamics or mass is included.

**Allen (31 October): "nature picks the simplest."** On this reading the principle is a minimum principle: the simplest structure that can sustain itself. In the count, three strands is the fewest that can make a primitive, single-piece pattern.

### Why three colours ("works" fixed first: each generation is neutral in total charge)
With charges in thirds from three strands with unit twists (u: +2/3, d: −1/3, e: −1, ν: 0) and N colours per quark,
$$N\Big(\tfrac23-\tfrac13\Big)-1+0=0\ \Longrightarrow\ N=3 .$$
- **The braid supplies exactly three colours:** three places for the odd twist. So colour is not a separate input; it is the same 3 as the strands.
- **Consistent with:** a neutral three-quark state (the proton, antisymmetric in three colours), and three identical quarks in one state (the Δ⁺⁺).
- **Grade:** N = 3 from charge thirds and neutral generations is standard physics (anomaly cancellation). The reading, that families, colours and charge thirds all come from three strands, is CO's.

### Why three forces ("works" fixed first: a force is an independent change of a pattern's labels that keeps it self-sustaining and respects the arrow)
A three-strand twisted braid has three kinds of label, and each gives one kind of change:
1. **Its overall counted-action phase:** a one-number rotation, U(1).
2. **Where the odd twist sits:** amplitudes over three positions, with the overall phase already counted in 1, give SU(3), colour.
3. **Each strand's twist level:** with t ∈ {−1, 0, +1} and all non-zero twists of one sign, a one-unit step on every strand connects exactly two states (ν ↔ e, u ↔ d). Pairs give doublets: SU(2), the weak force.

- **No fourth label.** Gravity is not a label change; it is the counting itself, the clock rate.
- **Chirality from the arrow (a reading; excluded as stated, see below).** The whole-braid step is the full twist Δ² = (σ₁σ₂)³, which generates the centre of B₃. In the positive monoid only one handedness exists, because a full twist cannot be undone. So the weak change would be one-handed. ED's workbook records the weak force's chirality as underived (its ParityWall row).
- **Grade:** a reading. The label-to-group map follows Bilson-Thompson. No couplings, Higgs or W/Z masses come out of it. Exactly three independent changes, and the arrow making the weak one chiral, are CO's.

### The chirality hook, pressed: excluded as stated
**The facts it must give:**
- the weak force acts only on left-handed particles (and right-handed antiparticles);
- right-handed neutrinos are inert;
- right-handed e, u and d still feel electromagnetism and colour.

**Why it fails:**
1. **"Only forward" read as "only added" makes weak processes one-way.** Both beta decay and inverse beta decay are observed, and so are electron capture and beta emission.
2. **The only handedness label a positive three-strand braid has is its renewal orientation,** σ₁σ₂ or σ₂σ₁. The full twist is the same for both, since (σ₁σ₂)³ = (σ₂σ₁)³, so it cannot act on one handedness alone.
3. **Bilson-Thompson's own assignment of chirality uses mixed-sign braids,** which the arrow forbids.
4. **The neutrino's inert right-handed state needs a handedness label the weak step can see.** The positive braid has none.

**What survives:**
- Three forces from three independent changes.
- The arrow as the source of the weak force's chirality survives only with a new ingredient. The candidate is ribbon framing: a strand's twist about its own axis, read relative to the arrow. That would be a new statement, not yet tested.

### Ribbon framing, tested: excluded; two findings on the way
**The statement:** handedness is the sense of a ribbon's twist about its own axis, read relative to the arrow.

**Excluded.** A ribbon's twist is already its charge, Q = (e/3)Σtᵢ. The left- and right-handed electron have the same charge, so they have the same twists, so this statement gives them the same handedness. A second ribbon label would be the Standard Model's assignment of weak isospin put in by hand.

**Finding 1: the weak step as a uniform shift (a reading).** Bilson-Thompson's W± is a triplet of like charges on the trivial braid. In twist terms it adds ±1 to every strand at once:
$$
(t_1,t_2,t_3)\ \to\ (t_1\pm1,\ t_2\pm1,\ t_3\pm1),\qquad \Delta Q=\pm e .
$$
- ν (0,0,0) ↔ e⁻ (−,−,−); u (+,+,0) ↔ d (0,0,−).
- The odd strand stays the odd strand, so colour is kept: the weak force changes flavour, not colour.
- Twists stay in {−1, 0, +1}, so the shift closes on the fifteen states: e∓, ν, u, d, ū and d̄ in three colours each. No other charge appears.

**Finding 2: the neutrino is its own antiparticle (an inference).**
- In Bilson-Thompson's model the antiparticle is the top-to-bottom mirror of the braid. Mirroring turns positive crossings into negative ones, which the arrow forbids.
- So in CO an antiparticle can only be the same positive braid with its twists negated: e⁺ = (+,+,+), d̄ = (+,0,0), ū = (−,−,0).
- Negating (0,0,0) gives (0,0,0). So ν = ν̄: the neutrino is Majorana.
- **This removes one of the facts tested above.** The observed fact is that only ν_L and ν̄_R are seen, not that a right-handed neutrino exists and is inert. A Majorana neutrino needs no separate ν_R; its right-handed state is the antineutrino, which does feel the weak force.

**What it predicts.** Neutrinoless double beta decay must occur. With the Koide masses above (NuFIT 6.0: sin²θ₁₂ = 0.308, sin²θ₁₃ = 0.0222), the effective mass is
$$
m_{\beta\beta}=\Big|\,c_{12}^2c_{13}^2m_1+s_{12}^2c_{13}^2m_2e^{i\alpha}+s_{13}^2m_3e^{i\beta}\Big| = |\,0.24+2.61\,e^{i\alpha}+1.11\,e^{i\beta}|\ \text{meV}\ \in[1.3,\ 4.0]\ \text{meV}.
$$
- This is below every running and planned experiment (LEGEND-1000 and nEXO aim at about 10–20 meV), so it cannot be checked soon.
- It would be excluded if the neutrino were shown to be Dirac. A Dirac neutrino needs a second untwisted braid that negation does not reach, so it needs a label this picture lacks.
- **Grade: inference.** It rests on reading the antiparticle as twist negation, which follows from the arrow plus the braid picture. It is not a derivation from CO's rules.

**Still open:** why the weak shift acts only on left-handed states. This picture now has no handedness label at all, and no candidate for one has survived.

### Antiparticles as sign flips, checked: a fork, neither side free
**What works.** Sign-consistent twist patterns (all ≥ 0 or all ≤ 0) number 2·2³ − 1 = 15. Negating the twists maps them onto each other with the right charges:

| pattern | e⁻ (−,−,−) | ū (−,−,0) ×3 | d (−,0,0) ×3 | ν (0,0,0) | d̄ (+,0,0) ×3 | u (+,+,0) ×3 | e⁺ (+,+,+) |
|---|---|---|---|---|---|---|---|
| Q/e | −1 | −2/3 | −1/3 | 0 | +1/3 | +2/3 | +1 |

**The problem: 27 − 15 = 12 mixed patterns.**
- **The patterns:**
  - six arrangements of (+,−,0), with Q = 0;
  - three of (+,+,−), with Q = +1/3;
  - three of (+,−,−), with Q = −1/3.
- **They are isolated from the weak step.** Each holds both a +1 and a −1, so the shift by ±1 pushes one twist out of range.
- **They are not the right-handed states.** The right-handed weak singlets include e_R (Q = −1) and u_R (Q = +2/3), and no mixed pattern has either charge.

**Two ways to remove them, each with a cost:**
- **(A) Twists slide along their ribbons.** The framed relation σᵢtᵢ = t_{i+1}σᵢ stands on the same footing as the braid relations already used in the count.
  - A sustaining braid's permutation is a 3-cycle, so its closure is one ribbon. With rotation, any unit twist can then be walked round to the next strand: (+,−,0) ~ (0,0,0), and (+,+,−) ~ (+,0,0).
  - The mixed patterns disappear.
  - **The cost:** only Σtᵢ is invariant. Which strand carries the odd twist stops being a property of the braid, so colour, and the three-colour reading above, lose their ground.
- **(B) Twists cannot cross a renewal (records are kept).** This is a reason from CO itself.
  - Colour is kept.
  - The 12 mixed patterns remain as states that are not observed.
  - **The cost:** they must be forbidden by Bilson-Thompson's rule that the twists on a braid share a sign. That rule is added, not derived.

**What survives either way:** ν = ν̄. (0,0,0) is its own negation in both readings, so the Majorana inference stands on the arrow plus the braid picture, whichever way the fork goes.

### Colour and family from one source, tested: excluded. Ruling: (B)
**The statement:** under (A), the three renewal modes of the circulant supply both colour and family.

**Excluded, for two independent reasons:**
1. **The count.** A Z₃ source has three modes. Quarks need 3 families × 3 colours = 9 states of each charge, so one source supplies 3 and two are needed.
2. **Degeneracy.** Colour is exact: the three colours have equal mass. The circulant's eigenvalues are
$$
\lambda_k=a+2b\cos\!\Big(\varphi+\tfrac{2\pi k}{3}\Big),\qquad k=0,1,2,
$$
   which are equal for every φ only if b = 0, that is p_stay = 1. Then the pattern never hops, so it is not sustaining, and Q = 1/(3p_stay) = 1/3 instead of 2/3. Modes that are colours cannot also give Koide's split masses.

**Ruling** (Allen: "test the shared one source. if it doesnt work, we will go with B."): **(B)**.
- Twists are read at the renewal boundary and cannot cross it, because records are kept.
- Colour is the position of the odd twist.
- The 12 mixed patterns are removed by the added rule that the twists on one braid share a sign (Bilson-Thompson's rule).
- The three-colour reading above stands, given that rule. ν = ν̄ stands.

### A CO reason for the same-sign rule (a reading)
**The statement:** a twist is a committed winding of its ribbon, and a winding is never undone along the ribbon. This is the twist form of the rule that makes every crossing positive.

**Why it gives the rule:**
- A sustaining braid's permutation is a 3-cycle, so its closure is a single ribbon. In successive renewals that ribbon passes positions i, π(i), π²(i), and so picks up t_i, t_{π(i)}, t_{π²(i)} in turn.
- Its winding never reverses exactly when all of t₁, t₂, t₃ are ≥ 0, or all are ≤ 0.
- That is the same-sign rule. It leaves the 15 states and removes the 12 mixed ones: in (+,−,0), the one ribbon winds forward, then back, then rests, in every renewal.

**Consistent with the weak step.** In u (+,+,0) → d (0,0,−) + W⁺ (+,+,+), the twists are carried off by the W, not undone. The rule constrains a pattern's own renewal, not a transfer between patterns.

**Limits:**
- The arrow fixes the sign of a crossing absolutely, but the sign of a twist only along one ribbon. It cannot do more, because both signs of charge exist.
- The reading needs "a twist is a committed winding", which is a new statement.

**Grade:** a reading. It replaces an added rule with the arrow's own principle, applied to twists.

### Chirality under (B): not a braid property
**Two candidates, both excluded:**
1. **Orientation.**
   - Under (B) the renewal boundary is physical, so rotation is no longer an equivalence. The two orientations σ₁σ₂ and σ₂σ₁ are then distinct words, with inverse 3-cycles.
   - But σᵢ → σ_{n−i} with crossing signs kept is a turn of 180° about the arrow, a proper rotation. So the two orientations are one object seen from two sides, which is not a handedness.
   - Under (B), S counts braids rather than rotation classes, which is the element count above, and it passes to B = 61.
2. **The braid's own handedness as helicity** (Bilson-Thompson's identification).
   - A mirror reverses every crossing, and so does time reversal, so the arrow sends both outside the allowed set. PT, C (twist negation) and CPT keep it.
   - So every CO braid has the same handedness. If that were helicity, every fermion would have one helicity.
   - But electrons are seen in both helicities, and reactor antineutrinos are right-handed (for a Majorana ν, that is the neutrino's other helicity).

**What this settles:**
- The uniform weak shift is right at the level of species. Its links e⁻↔ν↔e⁺, u↔d and ū↔d̄ are exactly the Standard Model's vertices and their conjugates.
- What it cannot do is select helicity, because helicity is spin relative to motion and the braid carries no spin label.
- **Chirality therefore belongs to the pattern rule (how a pattern moves and spins, R6), not to the braid.** CO has no statement about spin, so this is open.

## Principle S at large budgets (`archive/2026-10-31_new_primitives/braids/large_budget.py`, `large_budget.log`)
**The count.** Positive braids (elements of the positive monoid) are counted by their permutation, using Garside left-greedy normal forms up to B = 61, for n = 2 to 6. The check against the known counts of B₃⁺ (1, 2, 4, 7, 12, 20, 33, …) passes.
- The sustaining share at element level is the fraction whose permutation is an n-cycle.
- An n-cycle forces every generator to be used, and proper powers are exponentially rare.

**The pass criterion, set before the run:** n = 3 has the largest share at every odd budget computed.

**Exact parity rule.** Each crossing is a transposition, so a word of length L has permutation parity L. An n-cycle has parity n − 1. So sustaining needs L ≡ n − 1 (mod 2), that is
$$
B=n+L\ \text{odd}.
$$
At even budgets there are no sustaining patterns for any n.

**Result (odd B):**

| B | n=2 | n=3 | n=4 | n=5 | n=6 |
|---|---|---|---|---|---|
| 9 | 0 | 0.546 | 0.255 | 0.081 | 0 |
| 17 | 0 | 0.613 | 0.368 | 0.189 | 0.081 |
| 31 | 0 | 0.653 | 0.449 | 0.290 | 0.166 |
| 61 | 0 | 0.666 | 0.493 | 0.370 | 0.264 |

- **n = 3 is largest at every odd B from 9 to 61, so S passes.**
- **The shares approach 2/n.** On the right parity the permutation spreads evenly over half of Sₙ, and n-cycles are (n−1)!/(n!/2) = 2/n of that half.
- **n = 2 is excluded throughout:** σ₁ᴸ is the only braid, and it is primitive only at L = 1.
- **So, in the limit:**
$$
\text{share}_n\ \to\ \frac{2}{n}\ (n\ge3),\qquad \text{share}_2=0 ,
$$
  which is largest at n = 3.

**Caveats:**
- Element shares are higher than the class shares counted earlier (0.60 against 0.41 at B = 15), because class sizes vary at small L. The order of n is the same in both, and the two converge at large L.
- n ≥ 7 is not computed. Its limit 2/n < 2/3, and its approach is slower.
- The 2/n limit is numerical. It agrees with the parity argument, but equidistribution is not proved.

**Grade: computed, and plainly understood.** S picks three because n-cycles are a fraction 1/n of permutations and two strands are abelian. In plain terms, S is "the smallest non-abelian braid", which is what "nature picks the simplest" says. The result is solid but not deep.

### What to expect at large budgets (heuristic, not checked)
For long positive braids, three things are expected:
- **The conditions become nearly automatic:** almost every long word uses every generator (unsplittable) and is not a power (primitive).
- **The permutation spreads evenly** over the permutations of the right parity.
- **The share of single loops tends to 2/n.** Among the n!/2 permutations of one parity, (n − 1)! are n-cycles.

The share of self-sustaining patterns should then tend to
$$
s_n\ \to\ \frac{2}{n}\qquad(n\ge3):\qquad s_3\to\tfrac23,\quad s_4\to\tfrac12,\quad s_5\to\tfrac25,\ \dots
$$
- **n = 2 has none at any size:** its only positive braids are powers of σ₁, never primitive.
- **So three strands would stay ahead at every size,** with the lead over four tending to 4/3. The measured ratio, 2.6 → 1.8, is falling toward that.
- **Read this way, the result is "the fewest strands that can make a primitive, single-piece, interacting pattern":** Allen's "3 is the least that works".
- **A check:** the number of positive braids of each length has an exact generating function (Deligne's formula over parabolic subgroups). Combined with the permutation statistics it would settle the large-B behaviour without enumeration.

Code and logs: `archive/2026-10-31_new_primitives/braids/`.

## 6. Grade
- **The circulant form and √m = amplitude:** a reading. Brannen's parametrisation, with CO's possibility = |amplitude|².
- **Q = 1/(3 p_stay), and Koide ⇔ p_stay = ½:** derived (algebra).
- **"A renewal is two fair binary commitments":** a reading, not derived from CO's primitives.
- **δ = 2/9 as counted action:** a reading. It fits to 10⁻⁶. Many fractions can be built from 2s and 3s, so it is not evidence.
- **3 as the unique strand number with a non-abelian braid group and no commuting generators:** derived (braid-group fact). That it explains three families is a reading.
- **Principle S (three strands maximise the share of self-sustaining positive braids):** stated in advance and survived its test at B = 15 and 17. That holds at small budgets only, with the large-B trend open.
- **Not addressed:** the overall scale μ (μ² ≈ 313.8 MeV for leptons); the selection count; the neutrino and quark phases from first principles.

**What would make it a result:**
- a CO reason that forces both fairness and counted action;
- a prediction not yet fitted that comes true. Candidates: the neutrino masses above, or a quark relation stated before it is checked.

## Sources
- S. O. Bilson-Thompson, [hep-ph/0503213](https://arxiv.org/abs/hep-ph/0503213) (2005); Bilson-Thompson, Markopoulou and Smolin, [hep-th/0603022](https://arxiv.org/abs/hep-th/0603022).
- Y. Koide (1983); C. Brannen's circulant form, δ = 2/9 and the neutrino-mass prediction (2006); R. Foot's 45° reading; M. Kobayashi and T. Maskawa (1973) on three families and CP violation. Summary: [Koide formula (Wikiwand)](https://www.wikiwand.com/en/articles/Koide_formula).
- The τ mass: Belle II, [publication 4397](https://b2-pubdb1.desy.de/pub_data/publications/4397/); world average from the Koide summary above.
- Neutrino splittings: NuFIT 6.0 central values (normal ordering). The cosmological bound: the [European Strategy 2026 Physics Briefing Book](https://arxiv.org/pdf/2511.03883).
- Quark masses: PDG standard values, and running values at M_Z (Xing et al., approximate).
