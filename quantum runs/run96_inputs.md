## Run 96 inputs: the window's top edge from dilute-gas heating (unreviewed)

*28 October 2026. Gathered for Run 96's pre-registration (`inputs96/REPORT.md`, with `igm_leoT96.py`). Not registered and not yet checked independently.*

*Note, 28 October: reviewed in `checkPre96/` and superseded by Run 96 (`run96_section.md`). The registered top edge uses a combined one-sided test over 20 points, with Hu et al.'s errors in log units and Walther et al.'s published z = 1.8 error: κ_b < 7.29×10⁻¹⁹ r_C². The "z = 0.2" single-point value here is kept as a variant.*

**Why.** Reading I6 §6 puts the window's top edge, for r_C ≳ 4×10⁻⁷ m, at Run 92's B7 (IGM heating), κ_b < 6.7×10⁻²⁰ r_C². B7 assumed the heating over the universe's age reaches (3/2)k_B(10⁴ K) with no cooling, and was compared with no measurement.

**The heating per particle.** From model92: each hit adds ħ²/(2r_C²) to ⟨p_x²⟩, at λ = κ_b mc²/ħ. So every free particle, whatever its mass, gains
$$
P=\frac{3\kappa_b c^2\hbar}{4r_C^2}=7.11\times10^{-18}\,\frac{\kappa_b}{r_C^2}\ \text{W},\qquad \frac{dT}{dt}\Big|_b=\frac{2P}{3k_B},
$$
and a bound on P maps to κ_b,max = 1.407×10¹⁷ P_max r_C². Atoms and nuclei are much smaller than r_C, so their centres of mass gain the same P.

**The IGM, against measurement.**
- **Model.** The temperature equation is integrated from z = 200, conservatively without photoheating: dT/dt = −2HT + Γ_C(T_γ − T) − (recombination and free-free cooling) + 2P/(3k_B).
- **Data.** It is compared with Lyman-α-forest T₀(z) at the criterion T_b ≤ T₀ + 2σ:
  - Gaikwad et al. 2021, z = 2–3.8;
  - Boera et al. 2019, z = 4.2–5;
  - Walther et al. 2019, z = 1.8;
  - Hu et al. 2026, z = 0.1–0.4.
- **What B7 itself implies.** At B7's own limit the IGM would reach only about 3.6×10³ K by today, not 10⁴ K.
- **The bound.**
$$
\kappa_b<6.5\times10^{-19}\,r_C^2\quad(\text{z = 0.2; range }6.2\times10^{-19}\text{ to }1.1\times10^{-18}\ \text{across data choices}),
$$
  about 10× looser than B7.
- **With standard photoheating assumed** to explain T₀, the bound is 1.5–2.3×10⁻¹⁹ r_C². That rests on a photoheating model which fails by about 7σ at z ≈ 0.1.

**Leo T.**
- **Inputs:** gas at about 6000 K; n_H from 0.03 to 0.2 cm⁻³, with a mean of 0.07; [Fe/H] of −1.74 to −1.99.
- **Cooling:** Ċ = n_H²Λ(T)·10^[Fe/H].
- **Criterion:** P ≤ Ċ/[n_H(1.08 + x_e)].
- **Result:** 1.8×10⁻¹⁹ to 2.7×10⁻¹⁸ r_C², no tighter than the IGM.
- **A units slip, resolved.** The earlier claim that Leo T could be "up to 40× tighter" came from a slip in the literature: a cooling rate printed as 7×10⁻³⁰ GeV cm⁻³ s⁻¹ is 7×10⁻³⁰ erg cm⁻³ s⁻¹ (Kim 2021).

**Other dilute gas.**
- The Galactic warm neutral medium, cold clouds and cluster gas are 10³–10⁵× looser.
- A confirmed 21-cm absorption at z ≈ 17 would give 4.1×10⁻²⁰ r_C², but no detection is robust.
- GRW-type symmetrisation suppresses none of these: nV_s ≪ 1 for each.

**Effect on Reading I6 §6's window,** if registered as the primary top edge (B7′):
$$
3.6\text{–}5.6\times10^{-36}<\kappa_b<\min\!\big(0.94\,r_C^5,\ 6.5\times10^{-19}r_C^2\big),\qquad 8.3\text{–}9.0\times10^{-8}\lesssim r_C\lesssim5.1\times10^{-5}\ \text{m}.
$$
- SNO hands over to heating at 8.8×10⁻⁷ m.
- κ_b ≤ 1.7×10⁻²⁷ at the cap (1.6–2.8×10⁻²⁷), so a·P∞ ≳ 5.9×10²⁶.
- The photoheated form would give 0.4–0.6×10⁻²⁷ at the cap.

**Choices for the pre-registration:**
1. Which form is primary: the conservative one (no photoheating; recommended) or the photoheated one. The choice moves the cap by about 3×.
2. Firm up Walther et al.'s z = 1.8 errors (one of the two points that set the bound).
3. An independent check of the heating rate, the composition-independent dT/dt, and the temperature integration, against model92's B7.
