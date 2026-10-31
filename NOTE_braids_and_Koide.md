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
- **Chirality from the arrow (a reading).** The whole-braid step is the full twist Δ² = (σ₁σ₂)³, which generates the centre of B₃. In the positive monoid only one handedness exists, because a full twist cannot be undone. So the weak change would be one-handed. ED's workbook records the weak force's chirality as underived (its ParityWall row).
- **Grade:** a reading. The label-to-group map follows Bilson-Thompson. No couplings, Higgs or W/Z masses come out of it. Exactly three independent changes, and the arrow making the weak one chiral, are CO's.

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
