### Run 93: route (b)'s window under the rulings after Readings I1 and I4 (a calculation)

*Note, 28 October (Reading I6, ruled 28 October; `reading_I6_matter_and_pattern.md`): B13 loses its premise: it assumed a solid's internal records deposit gravity at fine resolution, and under the rulings of 27–28 October they deposit none. So a·P∞ ≳ 3.7×10²⁴ and "route (b) viable under every ruling to date" lapse; the run stands as a calculation. The current window is Reading I6 §6.*


*27 October 2026.*
- *Registered and hashed before the run (`quantum93/PREREG_93.md`, 10 files, 16:16:21 UTC), after Allen's review ("go") and an independent pre-registration check (`check93/REPORT.md`), whose corrections were adopted before the hash.*
- *Validated beforehand (V1–V7, all PASS).*
- *A second independent agent checked the registered run (`check93b/REPORT.md`). Its corrections are adopted below as a post hoc addendum; K93 is unchanged. A third agent checked its gas self-gravity inference (`checkGas/REPORT.md`), with G1 ruled after it.*

**Why.** Three things changed Run 92's window W for route (b)'s κ_b (with λ = κ_b E/ħ) and coarseness r_C:
- **Run 92's checks:** the CMB ceiling, a stricter radiation-gravity edge, and the lunar-laser-ranging argument.
- **Reading I4's rulings:** κ_b = 1/(aP∞), and a pattern's phase turned by the time-averaged count.
- **Reading I1's rulings:**
  - route (a) needs which-path information kept by committed matter, and is filled by the matter's possibility;
  - route (a)'s rate in bulk is per unit;
  - route (b) is symmetrised GRW-type;
  - Q7 counts an electron's energy.

Run 93 recomputes W under all of these.

**What is added to Run 92's bounds** (`model93.py`; Run 92's `model92.py` imported unchanged):
- **B13, lunar laser ranging.** A fraction f = λ_b/(λ_a + λ_b) of a body's draw is deposited smeared at r_C. With λ_a depending on the material, the crust–mantle difference in f is taken as λ_b/λ_a and bounded by Singh et al. 2023 (|Δ(m_a/m_p)| < 3.9×10⁻¹⁴):
$$
\kappa_b<\frac{\delta\,\lambda_a\,\hbar}{m_Nc^2}=2.7\times10^{-25}\qquad(\lambda_a=10^{13}\ \text{s}^{-1};\ r_C\ge10R_{\rm Moon}).
$$
  - For 'com', the atom is the unit (mean A ≈ 24), so the cap is 1.1×10⁻²⁶; for 'body', B13 is not computed.
  - It rests on the route-(a) ruling that route-(a) deposits land at fine resolution. Only route-(b) deposits are smeared at r_C.
- **B14, Q7** (the ⁸⁸Sr tweezer clock; ΔE = 1.7751 eV; a 33 s lower bound on single-atom coherence; ΔE shared by two valence electrons):
$$
\kappa_b<\frac{16\hbar m_ec^2}{\Delta E^2\tau}=5.2\times10^{-11}.
$$
- **B6 per population, strict:** shot noise below 10⁻⁶ also at horizon entry of the CMB's modes up to ℓ = 3000, giving κ_b > 2.5×10⁻⁹³. Per pattern at horizon entry (reported): κ_b > 2.6×10⁻²⁶.
- **The ceiling:** r_C ≤ 1.5×10¹⁸ m.
- **Symmetrisation.** The bounds are computed labelled. Under GRW-type symmetrisation (Λ = Σ_k g_k):
  - heating is termwise no larger;
  - emission and centre-of-mass diffusion are no larger (Cauchy–Schwarz);
  - decoherence is subadditive;
  - B13, B6 and the weak-field edge are unchanged.

  So the ruled W is at least as wide as the labelled one.

**Results (registered: K93 PASS).** In the primary case ('indep', per population, the primary B13), W is open from r_C = 2.32×10⁻¹⁰ m (2.52×10⁻¹⁰ m on the grid) to 1.5×10¹⁸ m:

| r_C | lower edge | upper edge, and what sets it |
|---|---|---|
| 10⁻⁷ m | 2.6×10⁻⁵⁶ (weak field) | 9.0×10⁻⁴⁶ (SNO) |
| 1 m | 2.6×10⁻⁷⁰ | 9.8×10⁻³⁴ (HST) |
| 10⁸ m | 2.6×10⁻⁸⁶ | 3.3×10⁻²⁸ (RadioAstron) |
| ≥ 3.1×10⁹ m | 2.5×10⁻⁹³ (strict B6, above about 3×10¹¹ m) | 2.7×10⁻²⁵ (lunar laser ranging) |

- **Q7 never binds.**
- **Every reported variant passes:** the other lunar-laser-ranging settings, 'com' (from 5.3×10⁻¹² m), 'body' (from 2.5×10⁻¹³ m), and the primary without Q7.
- **Per pattern ('indep'),** W opens at 9.5×10⁸ m (1.04×10⁹ m on the grid).
- **Under κ_b = 1/(aP∞),** W requires
$$
aP_\infty\gtrsim3.7\times10^{24}\ \text{at every } r_C\quad(\gtrsim1.1\times10^{45}\ \text{at }100\text{ nm}),
$$
  against gravity's P∞ ≳ 6.4×10¹⁰. Across the B13 variants the minimum ranges from 3.6×10²² to 3.7×10²⁵. This is arithmetic on W, not a registration of I4.

**Post-run check and post hoc addendum** (`check93b/REPORT.md`; `analyse93_posthoc.py`):
- **Integrity.** The hashes hold, and the run, validation and smoke test reproduce byte for byte. K93 follows the registered rule.
- **The per-pattern reading against B13** (not reported in the registration):

| case | B13 setting | cap ÷ per-pattern lower edge | verdict |
|---|---|---|---|
| 'indep' | primary (λ_a = 10¹³) | 10.4 | open from 9.5×10⁸ m |
| 'indep' | λ_a = 10¹² | 1.04 | open, barely |
| 'indep' | λ_a = 10¹⁴; Bartlett–van Buren δ | 10²–10³ | open |
| 'com' | primary | 0.43 | **closed everywhere** |
| 'com' | λ_a = 10¹² | 0.04 | **closed** |
| 'com' | λ_a = 10¹⁴; Bartlett–van Buren δ | 4–45 | open |

  So the per-pattern reading survives only for 'indep' with λ_a ≳ 10¹² s⁻¹, and by a margin smaller than its own factor of 10. Run 92's 'com' per pattern PASS does not survive B13.
- **A gas self-gravity bound above about 10¹⁵ m** (the check's inference, then checked independently in `checkGas/REPORT.md`). B13's mechanism also applies to gas that holds itself together by gravity. When r_C exceeds the structure, the smeared share f of its draw is missing from its self-gravity.
  - **Route (a)'s rate in molecular gas** is the H₂/He collision rate, good to a factor of about 2:
$$
\lambda_a=n\,\sigma\,\bar v_{\rm rel}\,(1+0.2\cdot0.7),\qquad \bar v_{\rm rel}=\sqrt{8k_BT/\pi\mu},
$$
    with σ ≈ 5×10⁻¹⁵ cm² at 10 K. That is about 2.6×10⁻⁵ s⁻¹ in prestellar cores (10⁵ cm⁻³) and 3×10⁻⁸ s⁻¹ in clouds (10² cm⁻³). Dust, ions, cosmic rays and photon scattering are six or more decades smaller, and H₂ barely radiates.
  - **It rests on interstellar gas being committed matter.** Ruled 27 October (G1), consistent with Reading I1's use of gas as the recorder in Hornberger's experiment. If only solids were committed matter (G2), the caps would be about 6.5 decades tighter, but Reading I1's laboratory check would fail. If gas renewed at mc²/(aħ) (G3, the reading already rejected for bulk matter), there would be no bound.
  - **Geometry.** The smeared share keeps a fraction w_v = 0.17, 0.029, 0.009 of its virial term at r_C/R = 1, 2, 3, falling as 0.27(R/r_C)³. So r_C ≥ 2R is enough to treat it as missing.
  - **The criterion.** The draft's f ≲ ½ is not robust: dust opacity, N_H/A_V, X_CO and distances each carry factors of 1.5–3. The check proposes an active fraction A = (1 − f) + f·w_v ≥ 0.2, so
$$
f_{\max}=\frac{1-A_{\min}}{1-w_v}\approx0.82,\qquad \kappa_b\le\frac{f_{\max}}{1-f_{\max}}\,\frac{\lambda_a\hbar}{m_Nc^2}.
$$
  - **The caps** ('indep'; 'com' is half):

| structure | applies for r_C ≥ | κ_b cap at A ≥ 0.2 | at A ≥ 0.5 | a·P∞ ≳ | confidence |
|---|---|---|---|---|---|
| prestellar core (0.06 pc, 10⁵ cm⁻³) | 3.7×10¹⁵ m | 9×10⁻²⁹ (5×10⁻²⁹–1.7×10⁻²⁸) | 6×10⁻³⁰ | 10²⁸ | medium–high |
| clump (0.5 pc, 10⁴ cm⁻³) | 3×10¹⁶ m | 1×10⁻²⁹ | 7×10⁻³¹ | 10²⁹ | medium |
| giant molecular cloud (10 pc, 3×10² cm⁻³) | 6×10¹⁷ m | 3×10⁻³¹ | 2×10⁻³² | 3×10³⁰ | low (virial status disputed) |

  - **What it changes.** Per population, nothing in K93: W stays open, and the smallest a·P∞ anywhere is still 3.7×10²⁴. Per pattern, whose lower edge is 2.6×10⁻²⁶, W would close above about 4×10¹⁵ m.
  - **What gives no bound on κ_b.** Intracluster and intergalactic gas are far larger than the ceiling. Dark matter is recorded only by route (b), so it bounds r_C, not κ_b, and no more strongly than the CMB ceiling (B12 at 100 pc; a GD-1 perturber estimate of about 10¹⁸ m is low confidence).
  - **Carried to the next run:** the core leg as a registered bound (B15), with the clump and cloud legs reported.
- **Minor corrections:**
  - **B14 for 'com':** the registration states 1.7×10⁻⁵, and the code halves Γ there too. The correct value (the atom carries ΔE; 33 s) is 4.15×10⁻⁶. It never binds.
  - **B13 is probably conservative.** Singh et al. bound a per-element S_Al,Fe, while the self-force limits the rock-level crust–mantle difference, which is smaller.
  - **§3's parenthetical** explains why B13 applies above 10 R_Moon, not why it is off below it.

**Reading.**
- **Under every ruling to date, route (b) is viable.** A window is open from 2.3×10⁻¹⁰ m. Its upper part is capped by lunar laser ranging, and, under G1, further above 3.7×10¹⁵ m by the gas self-gravity bound (to be registered next).
- **With κ_b = 1/(aP∞), CO's vacuum possibility per place must exceed about 10²⁴ (with a of order one),** whatever r_C is. That is fourteen decades beyond gravity's bound. If a rule put r_C in the laboratory, it would need about 10⁴⁵ at 100 nm.
- **What r_C is remains the open question.** It turns this into a sharp statement about P∞.

**Carried forward:**
- a rule for r_C;
- the gas self-gravity bound, registered as B15 (core leg, A ≥ 0.2, under G1), with its virial factor and threshold checked first; *done in Run 94 (27 October): K94 PASS, κ_b ≲ 4.2×10⁻²⁸ well above a core's radius, with the cross-sections corrected to the total ones (about 6× the draft's);*
- Singh et al.'s composition contrast;
- `B14_q7` for 'com' in later runs. *Done in Run 94.*

*Note (30 October): P∞ ≳ 6.4×10¹⁰ was p_s's bound times the pulsar triple's ratio bound; with ε = 0 in gravity the ratio bound and this figure lapse (Reading I17). What remains is p_s ≳ 4×10⁵ (conditional) and route (b)'s a·P∞ ≳ 2.5–5×10²⁷ (Run 96 with its relic-neutrino addendum). The upper bound p_s ≲ 1.1×10³⁰/a (Reading I11) rested on the same pulsar-triple ratio and lapses too (corrected 30 October after Reading I18's check).*
