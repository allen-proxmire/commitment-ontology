### Run 93: route (b)'s window under the rulings after Readings I1 and I4 (a calculation)

*27 October 2026.*
- *Registered and hashed before the run (`quantum93/PREREG_93.md`, 10 files, 16:16:21 UTC), after Allen's review ("go") and an independent pre-registration check (`check93/REPORT.md`), whose corrections were adopted before the hash.*
- *Validated beforehand (V1–V7, all PASS).*
- *A second independent agent checked the registered run (`check93b/REPORT.md`). Its corrections are adopted below as a post hoc addendum; K93 is unchanged.*

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
- **An open, unreviewed bound above about 10¹⁵ m** (the check's inference). B13's mechanism also applies to gas that holds itself together by gravity:
  - For interstellar gas, λ_a is about the collision rate: about 10⁻⁵ s⁻¹ in dense cores, 10⁻⁸ s⁻¹ in molecular clouds.
  - When r_C exceeds the structure, its self-gravity is cut by f. Collapsing cores and virialised clouds then need roughly:
    - κ_b ≲ 10⁻²⁹ for r_C ≳ 3×10¹⁵ m;
    - κ_b ≲ 10⁻³² for r_C ≳ 3×10¹⁷ m.
  - This would lower the upper edge at large r_C, and raise the required a·P∞ there to about 10³². It would not change K93, nor the smallest a·P∞ anywhere (3.7×10²⁴, reached between 3×10⁹ and about 10¹⁵ m).
  - It needs λ_a for molecular gas, and the self-gravity criterion, checked independently.
- **Minor corrections:**
  - **B14 for 'com':** the registration states 1.7×10⁻⁵, and the code halves Γ there too. The correct value (the atom carries ΔE; 33 s) is 4.15×10⁻⁶. It never binds.
  - **B13 is probably conservative.** Singh et al. bound a per-element S_Al,Fe, while the self-force limits the rock-level crust–mantle difference, which is smaller.
  - **§3's parenthetical** explains why B13 applies above 10 R_Moon, not why it is off below it.

**Reading.**
- **Under every ruling to date, route (b) is viable.** A window is open from 2.3×10⁻¹⁰ m. Its upper part is capped by lunar laser ranging, and possibly much further above about 10¹⁵ m by the gas self-gravity bound, which has not yet been reviewed.
- **With κ_b = 1/(aP∞), CO's vacuum possibility per place must exceed about 10²⁴ (with a of order one),** whatever r_C is. That is fourteen decades beyond gravity's bound. If a rule put r_C in the laboratory, it would need about 10⁴⁵ at 100 nm.
- **What r_C is remains the open question.** It turns this into a sharp statement about P∞.

**Carried forward:**
- a rule for r_C;
- the gas self-gravity bound (an independent check of λ_a in molecular gas);
- Singh et al.'s composition contrast;
- `B14_q7` for 'com' in later runs.
