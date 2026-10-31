## Reading I21: route (b)'s window against the newest short-range gravity and levitated-particle data 

*31 October 2026. Allen: "do as recommended" (close or confirm route (b)'s window, 0.09–51 μm, against the newest short-range gravity and levitated-particle data). A reading of the record and the literature, plus arithmetic (`i21_numbers.py`; numbers in `i21_numbers.log`). Not a registered test; it encodes no new rule. Revised after one independent check, whose corrections are adopted.*

**In plain terms.** The window stands. No test of Newton's law at full strength has gone below Lee et al.'s 52 μm, so the 51 μm cap is unchanged. Levitated particles, cantilevers and free test masses cannot reach route (b). CO's route (b) is GRW-type, so a body's centre of mass is heated by each nucleon's hits separately, with no coherent gain. Per nucleon, that heating is already bounded by the intergalactic gas. The best force sensor, LISA Pathfinder, falls short of it by about 4×10⁵ in power. The collapse-model bounds from levitated particles assume CSL's coherent gain, which CO does not have, so they do not transfer as collapse bounds.

### 1. The window (Run 96 with addendum 2)
$$
5.62\times10^{-36}<\kappa_b<\min\!\big(0.948\,r_C^5,\ 7.29\times10^{-19}r_C^2,\ 2.82\times10^{-27}\big),\qquad 0.090\ \mu\text{m}\le r_C\le 51\ \mu\text{m},
$$
with B16-NR at κ_b < 7.6×10⁻²⁰ r_C² from 9.67 μm up to the cap.

| edge | set by | data |
|---|---|---|
| floor | the test mass's own deposits, κ_b ≥ 4ħJ/(c²M²ASD²) | LISA Pathfinder, 1.74 fm s⁻² Hz⁻¹ᐟ² (final, 2018) |
| lower r_C | SNO's deuteron break-up under GRW-type symmetrisation, meeting the floor | SNO |
| top | B7′ (IGM heating) above 0.92 μm; B16-NR from 9.67 μm | Lyman-α T₀(z) to 2026; DESI DR2 Σm_ν |
| cap | Lee et al. 2020 inverse-square test, interior gravity smeared at √1.5 r_C | 52 μm separations |

### 2. Short-range gravity: the cap stands
- **Lee et al. 2020** (Eöt-Wash, separations down to 52 μm) remains the shortest test of Newton's law at full strength. A 2026 review of the field (Murata, arXiv:2605.18212) was consulted, and no newer O(1) result below 52 μm was located.
- **Casimir-range experiments (below about 10 μm)** bound only Yukawa strengths far above one. A solid's departure inside r_C is of order one, so they do not reach it (**inference**).
- **The cap is unchanged at 51 μm.** A test with O(1) sensitivity at separations d ≲ 50 μm would lower it to about d (Lee's 52 μm gave 51 μm); the exact cap needs each experiment's geometry and sensitivity.

### 3. Force-noise sensors: they cannot reach route (b) (derived, on the record's model)
**The signal.** Each hit adds ħ²/(2r_C²) to ⟨p_x²⟩ at the per-nucleon rate λ = κ_b m_N c²/ħ (model92). Labelled, for a body of N nucleons of any size, the one-sided force PSD is
$$
S_F=2\,\frac{d\langle p_x^2\rangle}{dt}=N\,\frac{\kappa_b}{r_C^2}\,m_Nc^2\hbar .
$$
This is B2's formula (model92). Route (b) is GRW-type (Reading I1 ruling 5), with operator Λ^{1/2}, Λ = Σ_k g_k. The centre-of-mass diffusion it gives is no larger than the labelled form's, by Cauchy–Schwarz:
$$
\int\frac{\big|\sum_k\partial_x g_k\big|^2}{4\sum_k g_k}\ \le\ \sum_k\int\frac{|\partial_x g_k|^2}{4g_k},
$$
with equality for a body much smaller than r_C, and strict inequality for one much larger (**inference**). The record supports it: model92's B2 adds kicks incoherently in every case, and Reading I6 §4 says 'indep' and 'com' share one window. So the formula is an upper bound on the signal.

**The window caps it.** Over the window, κ_b/r_C² ≤ 7.29×10⁻¹⁹ m⁻² (B7′; SNO gives the same value at the handover):
$$
\frac{S_F}{N}\ \le\ 1.16\times10^{-62}\ \text{N}^2\,\text{Hz}^{-1},
$$
or 1.2×10⁻⁶³ above 9.67 μm under B16-NR.

**What sensors measure.** A sensor of mass M and per-mass acceleration noise S_a reaches S_F/N = S_a M m_N. LISA Pathfinder's 1.74 fm s⁻² Hz⁻¹ᐟ² is differential, so each mass carries half its power, as in B2.

| sensor | S_F/N (N² Hz⁻¹) | short by, in power |
|---|---|---|
| LISA Pathfinder (1.93 kg, 1.74 fm s⁻² Hz⁻¹ᐟ² differential) | 4.9×10⁻⁵⁷ | 4.2×10⁵ |
| LISA requirement (3 fm s⁻² Hz⁻¹ᐟ² per mass) | 2.9×10⁻⁵⁶ | 2.5×10⁶ |
| LIGO test mass at 100 Hz (illustrative) | 1.0×10⁻⁵⁴ | 9×10⁷ |
| milligram levitated mass, 10⁻¹⁷ N Hz⁻¹ᐟ² (illustrative) | 3.9×10⁻⁵⁵ | 3.4×10⁷ |
| cantilever, 10⁻¹¹ kg at 10⁻¹⁸ N Hz⁻¹ᐟ² (illustrative) | 1.7×10⁻⁵² | 1.4×10¹⁰ |
| levitated nanosphere, 10⁻¹⁷ kg at 10⁻²⁰ N Hz⁻¹ᐟ² (illustrative) | 1.7×10⁻⁵⁰ | 1.4×10¹² |

- **For LISA Pathfinder this is Run 96's B2, which never binds** (a restatement): B2 gives κ_b/r_C² ≤ 3.08×10⁻¹³, against B7′'s 7.29×10⁻¹⁹.
- **For the rest it is a reading.** The illustrative rows are orders of magnitude, not specific data. Smaller sensors do worse: the needed reach is S_F/N = F² m_N/M, which worsens as F²/M.

**CSL bounds do not transfer as collapse bounds.**
- The levitated-particle and cantilever limits on CSL (Vinante et al. 2017 and 2020; proposals to 2026, such as Dey, Barker and Datta, arXiv:2604.21705, projected sensitivities λ_CSL ≈ 10⁻¹³–10⁻¹⁴ s⁻¹ at 10⁻⁷ m) rest on CSL's coherent gain, ∝ N² for bodies smaller than r_C.
- Under GRW-type symmetrisation that gain is absent: identical units within r_C share a localisation (Reading I6 §4).
- Read naively as a CSL rate, CO's floor λ ≥ 8×10⁻¹² s⁻¹ (1.35×10⁻¹¹ at 0.1 μm) would sit above such projected sensitivities, though the two rates are defined by different conventions. It would not conflict with them, because the signal they assume is not CO's (**inference**). Without the coherent gain, these experiments reduce to the force-noise comparison above.

### 4. The other edges
- **Floor:** LISA Pathfinder's final noise is still the best free-fall figure. LISA's requirement is about 6× looser in power per mass; only a better achieved noise would raise the floor.
- **Lower edge:** no newer deuteron break-up data. The edge is r_lo = (floor/0.948)^{1/5}, so it moves as floor^{1/5} and C_SNO^{−1/5}: a ×10 tighter SNO bound or a ×10 higher floor raises it ×1.6. B7′ and B16-NR do not move it.
- **Top:** the IGM data run to 2026 (Hu et al.), and B16-NR uses DESI DR2. No newer data was located.

### 5. Finding
- **The window stands at 0.09–51 μm.**
- **Mechanical sensors are not a route to it** (derived on the record's GRW-type model, with the upper-bound step an inference): the best is short by about 4×10⁵ in power.
- **Collapse-model bounds from levitated particles do not apply,** because they assume CSL's coherent gain.
- **What would move the window:**
  - an O(1) gravity test below about 50 μm (the cap);
  - a top edge about 3.4×10⁸ tighter (registered primary) or 3.5×10⁷ tighter (with B16-NR), or a LISA-type noise about 3.5×10³ lower (closure, Run 96).

### 6. Choices for a ruling
1. Record the finding: the window is confirmed against current data; force-noise sensors cannot reach route (b) under GRW-type symmetrisation. *A reading.*
2. Record, in the window's notes, that CSL-based mechanical bounds do not apply to CO's route (b) as collapse bounds.

### Sources
- J. G. Lee et al., [arXiv:2002.11761](https://arxiv.org/abs/2002.11761) (PRL 124, 101101, 2020).
- J. Murata, [arXiv:2605.18212](https://arxiv.org/abs/2605.18212) (review, 2026).
- A. Vinante et al., [arXiv:1611.09776](https://arxiv.org/abs/1611.09776) (2017); [arXiv:2002.09782](https://arxiv.org/abs/2002.09782) (2020).
- S. Dey, P. Barker and A. Datta, [arXiv:2604.21705](https://arxiv.org/abs/2604.21705) (2026, proposal).
- LISA Pathfinder, Armano et al., PRL 120, 061101 (2018).
- The record: `quantum/run96_section.md` (window, B2, addendum 2); Reading I6 §4 (symmetrisation); `quantum/run92_section.md` (GRW-type heating ≤ labelled); Reading I1 ruling 5.

### Ruling (30 October 2026)

Allen: "do as you recommend or see fit."
1. **The window is confirmed against current data** (recorded). Force-noise sensors cannot reach route (b) under GRW-type symmetrisation.
2. **CSL-based mechanical bounds do not apply to route (b) as collapse bounds** (noted in the window's record).
