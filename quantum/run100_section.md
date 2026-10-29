### Run 100: the liquid-xenon window, and the engine-hop line against p_s (a calculation, quantum runs)

*29 October 2026.*
- *Registered and hashed before the run (`quantum100/PREREG_100.md`, 25 files, 11:03:46 UTC; runs from 11:04:17 UTC), after an independent pre-registration check (`checkPre100/`), whose corrections were adopted, and Allen's "go".*
- *Validated beforehand (37 checks, all PASS).*
- *Not blind: the verdict, and everything outside the two xenon rows, were known before hashing. The registered checks test the code and the transcription of the XENONnT datum, not the theory.*
- *A second independent agent checked the registered runs (`check100/REPORT.md`): the hashes verify, re-runs reproduce both outputs byte for byte, and its own code agrees at every point tested (to 10⁻¹⁵). Its wording points are adopted below.*

**Why.** Run 99 flagged liquid xenon as the next material whose radiation limit would open a density window, and Reading I10 (ruled) named the engine-hop minimal line as a candidate linking saturation to the gravity crossover p_s.

**The xenon window, H.**
- **The datum:** XENONnT (PRL 136, 120201, 2026), λ/r_C² < 3.7×10⁻³ s⁻¹ m⁻² at 95% CL, with the paper's own charge accounting (electron–proton cancellation; conservative).
- **The density:** liquid xenon at the detector's operating point, 2862 kg m⁻³.
- **The form:** inside the threshold band the channel is mass-proportional CSL, as for germanium:
$$
r_H^{*\,9}=\frac{c\,\big(S'(s_0)\,m_N/\delta\rho\big)^2}{(\lambda/r_C^2)\,2^{3/2}(2\pi)^3},\qquad s_0=\frac{\rho_{\rm Xe}-\rho_K}{\rho_K/10}+\tfrac12 .
$$
- **Everything else** is read from Run 99's hashed output and asserted equal.

**Result.**
- **K100: LEAD AT LABORATORY DENSITIES** (foregone).
- **All five registered statements agree:**
  - the predicted edge at 115 of 115 densities, with no holes;
  - the named rows exact: xenon #25 and #26, germanium #17, #21 and #20;
  - the survivor count, 4449 (29 removed by H);
  - the named line point, allowed, with H binding at 1.25×10⁵;
  - the engine-hop code check.

| quantity | value |
|---|---|
| edge at ρ_K = 2754 kg m⁻³ | 0.39 → 2.45 μm (#25; holds for xenon densities 2844–2868 kg m⁻³) |
| edge at ρ_K = 2884 kg m⁻³ | 0.39 → 2.79 μm (#26; holds for 2793–2975 kg m⁻³) |
| near zone (within 10× of present limits) | 376 (378 − 6 + 4) |
| XENONnT's 90% CL value | no change; Kim's 2022 reanalysis without cancellation removes 1 survivor |
| TeO₂ heat variant (an order-of-magnitude residual of about 10 pW kg⁻¹, reported only) | edge at 6026 kg m⁻³ moves to #14 (0.51 μm); 3 near-zone points would go |

**The engine-hop line against p_s** (reported, fitted through p_s, not verdict-bearing).
- **The line:** C1a, K = 1, a = 1, on the engine's hop:
$$
\ell=\ell_P\sqrt{0.99\pi\,p_s/3},\qquad \rho_K=\frac{\hbar}{c\,\ell\,V_c},\qquad N_{\rm cell}=\frac{\hbar}{c\,\ell\,m_N}.
$$
- **The scan:** 340 ladder values, p_s = 4×10⁵ × 1.1^k up to 4.3×10¹⁹, on Run 99's 49 r_C.
- **Survival:**
  - Every ladder p_s keeps laboratory survivors (18–46). No p_s is excluded as a whole.
  - On 206 of the 340, from 9.9×10⁸ up, some laboratory points are excluded, at the same small-r_C edge as Run 99.
- **The near zone** (some surviving point with q = Γ_max/Γ_K ≤ 10):
  - **continuous from 1.26×10¹² to the ladder's end:** 183 consecutive values, set by LISA Pathfinder (177) and Earth's heat (6);
  - **below that, only at isolated band crossings:** xenon at 2×10⁸–1.1×10⁹, enriched germanium at 3×10⁹–1.6×10¹⁰, natural germanium near 10¹¹.
  - The onsets are on the 49-point r_C grid. With r_C continuous they start lower, at 1.1×10⁸, 1.9×10⁹ and 5.3×10¹⁰.
- **Where improved bounds would bite first:**
  - **p_s ≈ 10¹³–1.3×10¹⁵:** the closest point sits at q ≈ 1.15–1.25 (median), minimum 1.003 at 1.2×10¹⁵ (0.385 μm, 684 kg m⁻³). An acceleration noise a few to ten per cent below LISA Pathfinder's would exclude those points.
  - **p_s ≈ 4–5×10⁸:** XENONnT alone sets the test, q_min 1.17, so a limit about 15% tighter would exclude it.
- **How to read it.** Being close to a bound is a statement about the experiments, not support for the line. At no p_s is every tested point within 10×, because the line's large-r_C points survive by large factors.

**Targets** (descriptive, from Run 99 and 100's stored outputs; `run100_targets.md`).
- A point with ratio q is tested when the binding measurement improves by q in its own quantity: √q in acceleration noise, q in a heat budget or a radiation limit.
- **The edge moves as:**
  - r\* ∝ ASD^{−2/5} where LISA sets it (one fine step needs ASD ×1.39);
  - r\* ∝ (λ/r_C²)^{−1/9} in the X-ray windows (×10 tighter moves r\* by ×1.29).
- **The fine near zone:**

| binding constraint | points | improvement that tests them |
|---|---|---|
| LISA Pathfinder | 346 | ASD ×1.00–3.2 |
| Earth's heat | 17 | ×1.04–5.1 |
| the germanium windows | 6 | ×1.6–7.2 |
| the xenon window | 4 | ×1.2–7.2 |
| the brown dwarf LHS 6343 C | 3 | ×4.7–5.0 |

**What it means.**
- **A second material window confirms the method.** Each detector material with a published radiation limit opens a row in which the onset edge jumps to micrometres, here 2.45–2.79 μm.
- **Along the engine-hop line, the onset of saturation would read p_s.** Present experiments sit at the line over p_s ≈ 10¹²–4×10¹⁹, and in narrow windows at 10⁸–10¹¹. That is a link between the quantum and gravity sectors, fitted through p_s, not a prediction.
- **Whether p_s is bounded from above** is taken up in Reading I11 (in preparation).
