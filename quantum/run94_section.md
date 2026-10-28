### Run 94: route (b)'s window with the gas self-gravity bound (a calculation)

*Note, 28 October (Reading I6, ruled 28 October; `reading_I6_matter_and_pattern.md`): B15 stands as a calculation but lies wholly in r_C now excluded (above about 5×10⁻⁵ m); the a·P∞ minimum quoted here falls away with B13 (Run 93's note).*


*27 October 2026.*
- *Registered and hashed before the run (`quantum94/PREREG_94.md`, 12 files, 19:06:13 UTC), after Allen's review and an independent pre-registration check (`checkPre94/REPORT.md`), whose corrections were adopted before the hash.*
- *Validated beforehand (V1–V8, all PASS).*
- *A second independent agent checked the registered run (`check94/REPORT.md`). Its corrections are adopted below as a post hoc addendum; K94 is unchanged.*

**Why.** A pattern draws only where and when it commits. Between commitments it carries no draw of its own, and route (b), a random "commit and continue" at λ = κ_b E/ħ, moves its draw along with it. So large bodies, whose units commit very often in total, draw continuously, and small patterns draw rarely.

The smeared share of a body's draw is f = λ_b/(λ_a + λ_b). Run 93's post-run check found that this mechanism also bounds route (b) in gas that holds itself together by gravity. A third check (`checkGas/REPORT.md`) confirmed route (a)'s rate in molecular gas. It replaced the criterion f ≲ ½ with a defensible one, and recommended registering only the prestellar-core leg. G1 was then ruled: interstellar gas is matter, so its collisions are route-(a) records. Run 94 registers the bound as B15, and corrects B14 for 'com'.

**B15, a prestellar core's self-gravity** (`model94.py`; Runs 92–93's registered files imported unchanged).
- **The smeared share.** Route-(a) deposits land at fine resolution. Route-(b) deposits are smeared with model92's construction: a deposit of standard deviation r_C about the record's centre, which itself lies within r_C/√2 of the unit. So the mean deposit has standard deviation √1.5 r_C per axis. For each species s (H₂, He):
$$
f_s=\frac{\lambda_{b,s}}{\lambda_{a,s}+\lambda_{b,s}},\qquad\lambda_{b,s}=\frac{\kappa_b m_{\rm unit}c^2}{\hbar}.
$$
- **What survives.** The smeared part of a uniform ball of radius R keeps a fraction w_v of its virial term:
$$
w_v=\frac{\int_0^R\rho\,r\,g_s\,4\pi r^2dr}{\int_0^R\rho\,r\,g_0\,4\pi r^2dr}=0.105,\ 0.0166,\ 0.0052\quad(r_C/R=1,2,3),
$$
  falling as 0.145(R/r_C)³.
- **The criterion.** The active fraction, weighted by mass fraction X_s, must be at least A_min = 0.2:
$$
A=\sum_sX_s\big[(1-f_s)+f_sw_v\big]\ge A_{\min}\iff\sum_sX_sf_s\le\frac{1-A_{\min}}{1-w_v}.
$$
- **Route (a)'s rates** are total elastic collision rates, since a collision at any angle resolves position far below R:
$$
\lambda_{a,\rm H_2}=n\sigma_{\rm HH}\bar v_{\rm HH}+x_{\rm He}n\sigma_{\rm HHe}\bar v_{\rm HHe},\qquad\lambda_{a,\rm He}=n\sigma_{\rm HHe}\bar v_{\rm HHe},\qquad\bar v=\sqrt{8k_BT/\pi\mu}.
$$
- **Registered inputs,** chosen so the cap is weaker than the best estimate:
  - R = 0.0737 pc: Barnard 68 at the Pipe Nebula's 3D-dust distance, 152 pc (an assumption);
  - n = 10⁵ cm⁻³ (3.7× B68's mean) and T = 10 K;
  - σ_HH = 4×10⁻¹⁴ cm² and σ_HHe = 1.4×10⁻¹⁴ cm² (above the computed 3.2 and 1.1×10⁻¹⁴);
  - x_He = 0.2.

  So λ_a = 1.94×10⁻⁴ s⁻¹ per H₂.
- **B14 for 'com', corrected.** The atom carries ΔE, so κ_b < 4.15×10⁻⁶. It never binds.

**Results (registered: K94 PASS).** In the primary case ('indep', per population), W is open from 2.32×10⁻¹⁰ m (2.52×10⁻¹⁰ m on the grid) to 1.5×10¹⁸ m:

| r_C | lower edge | upper edge, and what sets it |
|---|---|---|
| 10⁻⁷ m | 2.6×10⁻⁵⁶ (weak field) | 9.0×10⁻⁴⁶ (SNO) |
| 1 m | 2.6×10⁻⁷⁰ | 9.8×10⁻³⁴ (HST) |
| 10⁸ m | 2.6×10⁻⁸⁶ | 3.3×10⁻²⁸ (RadioAstron) |
| 3×10⁹ – 1.7×10¹⁵ m | 2.5×10⁻⁹³ (strict B6, above about 3×10¹¹ m) | 2.7×10⁻²⁵ (lunar laser ranging) |
| R = 2.27×10¹⁵ m | 2.5×10⁻⁹³ | 9.0×10⁻²⁸ (B15) |
| ≥ 2R | 2.5×10⁻⁹³ | 4.6×10⁻²⁸ falling to 4.2×10⁻²⁸ (B15) |

- **B15 sets the upper edge from r_C = 0.751 R = 1.71×10¹⁵ m,** where w_v falls to A_min.
- **Under κ_b = 1/(aP∞),** the smallest a·P∞ anywhere is unchanged, 3.66×10²⁴ (between 3×10⁹ and 1.7×10¹⁵ m). Above, W requires
$$
aP_\infty\gtrsim1.1\times10^{27}\ (r_C=R),\qquad\gtrsim2.2\times10^{27}\ (r_C\ge2R),\qquad\gtrsim2.4\times10^{27}\ (\text{large }r_C).
$$
- **Every reported variant passes:**
  - the central cross-sections;
  - A_min = 0.4 (Barnard 68's hydrostatic fit) and A_min = 0.5;
  - the clump and cloud legs;
  - the lunar-laser-ranging variants;
  - 'com' (from 5.3×10⁻¹² m) and 'body'.
- **Per pattern ('indep'),** W is open only from 9.55×10⁸ m (1.04×10⁹ on the grid) to 1.72×10¹⁵ m. Above, B15 lies below the per-pattern lower edge, 2.6×10⁻²⁶. 'com' per pattern stays closed.

**Post-run check and post hoc addendum** (`check94/REPORT.md`):
- **Integrity.** The hashes hold, and validation, smoke test and run reproduce byte for byte. K94 follows the registered rule. An independent recomputation of B15 (closed-form smeared density, its own constants) matches to four digits.
- **Exact edges.** B15 starts constraining at 0.7514 R = 1.709×10¹⁵ m and falls below B13 at 1.710×10¹⁵ m. Per pattern, W closes at 1.723×10¹⁵ m.
- **No step at the onset.** With f_max = (1 − A_min)/(1 − w_v), f_max → 1 as w_v → A_min, so the cap falls continuously from infinity (2×10⁻²⁶ at 1% above the onset, 1×10⁻²⁷ at 25%). Below the onset even a fully smeared core keeps A_min of its binding. Where the onset lies depends on the model:

| change | onset |
|---|---|
| registered (uniform ball, virial measure, A_min 0.2) | 0.751 R |
| edge-force measure | 0.722 R |
| central-density measure | 0.814 R |
| Bonnor–Ebert profile of B68 | 0.607 R = 1.38×10¹⁵ m |
| A_min = 0.4 | 0.51 R (uniform), 0.40 R (Bonnor–Ebert) |
| A_min = 0.5 | 0.43 R (uniform), 0.34 R (Bonnor–Ebert) |

  So the per-pattern window closes somewhere between 0.97×10¹⁵ and 1.72×10¹⁵ m across the variants; σ does not move it.
- **Corrections to the registration's text** (no verdict changes):
  - at the registered spread, the r_C = R cap depends on the binding measure by only about ±15% (8.5–10.6×10⁻²⁸), not "by tens"; the steep dependence lies at 0.72–0.82 R;
  - a Bonnor–Ebert model of B68 at 152 pc (n_c = 1.73×10⁵ cm⁻³, contrast 16.6), with the central σ, gives 2.2×10⁻²⁸ at large r_C. The registered cap is weaker than this best estimate by 1.9×, not 1.6×. With the registered σ the Bonnor–Ebert cap is 2.8×10⁻²⁸, 1.5× below the uniform ball's, not 1.7×;
  - leaving out the electrons makes the cap 0.24% too strong, not weaker. Leaving out He–He collisions makes it 2–5% too strong;
  - for mostly para-H₂, the symmetrised total cross-section counts each collision twice, so the per-molecule rate may be up to 2× lower than registered. That only weakens the registered cap further.
- **'body' should take B15.** Gas molecules are free particles, which model92 treats as their own units in every case. With molecule and atom as units, 'body' takes the 'com' caps above 1.71×10¹⁵ m (1.9×10⁻²⁸ at large r_C, a·P∞ > 5.2×10²⁷); as run, that range was capped only by RadioAstron. 'body' stays PASS.
- **The clump and cloud legs** (reported, not registered; at the registered σ, which overstates σ at 12–15 K, so these caps are on the weak side):

| leg | applies from | 'indep' cap (≫ R) | 'com' cap | a·P∞ ≳ |
|---|---|---|---|---|
| clump (0.5 pc, 10⁴ cm⁻³) | 1.16×10¹⁶ m | 4.6×10⁻²⁹ | 2.1×10⁻²⁹ | 2.2×10²⁸ |
| giant molecular cloud (10 pc, 3×10² cm⁻³) | 2.32×10¹⁷ m | 1.5×10⁻³⁰ | 7.1×10⁻³¹ | 6.5×10²⁹ |

  Registered alongside the core, they would leave K94 PASS and the per-pattern reading unchanged.

**Reading.**
- **Under every ruling to date, route (b) is viable.** The window is still open from 2.3×10⁻¹⁰ m to the ceiling.
- **Above about 1.7×10¹⁵ m, the coarseness costs about three more decades of P∞.** If r_C is large, CO's vacuum possibility per place must exceed about 2×10²⁷ (with a of order one). Below that it must exceed 3.7×10²⁴.
- **The bound rests on** G1, on route-(a) deposits landing at fine resolution, on B68 being in hydrostatic equilibrium with A ≥ 0.2, and on B68's distance.

**Carried forward:**
- a mechanism for r_C (Reading I5: none in the record);
- the Singh et al. composition contrast (whether B13 is conservative);
- the model-dependence of B15's onset (0.34–0.81 R);
- 'body' with B15 (and B7) for free gas particles, in later runs' code;
- a Bonnor–Ebert-profile variant of B15, if the per-pattern closure becomes a headline.
