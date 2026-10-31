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

## 6. Grade
- **The circulant form and √m = amplitude:** a reading. Brannen's parametrisation, with CO's possibility = |amplitude|².
- **Q = 1/(3 p_stay), and Koide ⇔ p_stay = ½:** derived (algebra).
- **"A renewal is two fair binary commitments":** a reading, not derived from CO's primitives.
- **δ = 2/9 as counted action:** a reading. It fits to 10⁻⁶. Many fractions can be built from 2s and 3s, so it is not evidence.
- **3 as the unique strand number with a non-abelian braid group and no commuting generators:** derived (braid-group fact). That it explains three families is a reading.
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
