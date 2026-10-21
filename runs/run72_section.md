## 9zzt. Run 72: clocks on an equal-place curved lattice, both signs of curvature

*21 October 2026. Allen (12:50): "then run 3 and 4". Step 4 was the follow-up to Run 70 that its check recommended: the design gap with about ten times the statistics, an equal-volume discretisation, and clocks at minima of the curvature profile as well as maxima. Registered and hashed before any engine run (`curve72/PREREG_72.md`, 11:06 UTC), with the theory's predictions computed and hashed beforehand (`theory72.json`).*
- *Disclosed: the theory was explored first, at several curvatures, both p_s = 1 and 4, and two probe layouts. The choice of λ = 0.25, p_s = 1 and Run 24's layout was made for the gap's statistical power, before any engine run.*
- *Two 600-tick timing runs ended before the burn-in, so they produced no clock numbers.*
- *The first job runner hit the session's two-hour task limit after 32 of 50 runs. A resume script ran the rest of the same registered list.*
- *An independent agent checked the run. It confirmed the geometry, the theory (to 10⁻⁶ with its own solver), the statistics and the resume (the registration is intact). Its corrections narrow three statements, and they are included.*

**Question.** Run 70 found that the engine's clocks follow the zero-range theory on a lattice with curved-space conductances. Its check narrowed that in three ways:
- the size of the effect depended on how places were represented, because Run 70's places had unequal γ̃-volume;
- only one sign of curvature was tested;
- the robust quantity, the change in the design gap, was not resolved.

On a lattice where every place has the same γ̃-volume, and with clocks at both positive and negative curvature, do the clocks still follow the theory, and does the design gap move as predicted?

**The lattice: equal places.**
- **The metric** has unit volume per place:
$$
\tilde\gamma=B^{-4}dx^2+B^{2}(dy^2+dz^2),\qquad B=e^{\beta(x)},\qquad \sqrt{\tilde\gamma}=1.
$$
- **The profile:** β = s·λ·g(x), with g = −[1 − cos(2π(x − 3.5)/6)] and λ = 0.25. At each clock's midpoint β = 0 and β′ = 0.
  - *Corrected by the check:* only the clock's internal link is unit. Relative to the flat control, its outer x-links carry ×0.61 (s = +1) or ×1.65 (s = −1), and its y/z-links ×1.07 or ×0.94.
  - Places are equal in volume but not in shape: the aspect ratio is 1.11 or 0.90 at the clock, and 4.5 or 0.22 at the cell corners.
  - The curvature varies by order one across a clock: for s = +1, R̃ = 1.10 at the midpoint, 0.62 at the clock's own places, and −0.35 one place further out.
- **Curvature at the clocks.** The scalar curvature is
$$
\tilde R=-e^{4\beta}\big(14\beta'^2+4\beta''\big)=4s\lambda k^2=\pm1.10\ \text{per spacing}^2 .
$$
  - s = +1 puts the clocks at maxima of B (positive curvature).
  - s = −1 puts them at minima (negative curvature).
- **Conductances** (√γ̃γ̃^{ii}): B⁴ on x-links and B⁻² on y/z-links.
- **Normalisation.** Any volume-preserving anisotropy raises a place's total conductance above 6, so every lattice, including the flat control, carries one factor c_n = 0.4463. Relative to the clocks, the medium is slowed by the same factor everywhere: an explicit rescaling of time.
- **The engine and protocol** are Run 70's, with p_s = 1 (P₀ = 64 or 38), Run 24's 216 probes (designs H and 2H), and 20,000 ticks read over the last 15,000.
- **Statistics:** ten seeds per sign and medium, five per flat medium, 50 runs in all.
  - Each sign has its own seeds. Within a sign, the high and low runs share seed numbers, and at s = +1 they are anticorrelated (r ≈ −0.73; the check).

**The theory, fixed beforehand.** Run 70's zero-range theory, unchanged:
$$
\tfrac16\sum_yW_{xy}(z_y-z_x)=s_x-\bar s,\qquad P_{\rm own}=R(z_{\rm amb}+\Delta z),\qquad
\text{gap}=1-\frac{\kappa_1}{\kappa_2},\quad \kappa_j=\frac{1-r_j^{\rm low}/r_j^{\rm high}}{\varepsilon_{\rm amb}} .
$$

**Results** (own-dip 1 − P_own/P_amb, curved over flat).

| | R̃ = +1.10: measured (theory) | R̃ = −1.10: measured (theory) |
|---|---|---|
| high medium, design 1 | 1.0459 ± 0.0024 (1.0463) | 0.9655 ± 0.0024 (0.9676) |
| high medium, design 2 | 1.0726 ± 0.0075 (1.0733) | 1.0101 ± 0.0070 (1.0232) |
| low medium, design 1 | 1.0498 ± 0.0051 (1.0540) | 0.9561 ± 0.0045 (0.9611) |
| low medium, design 2 | 1.0799 ± 0.0099 (1.0828) | 1.0181 ± 0.0089 (1.0306) |
| design gap | 0.0830 ± 0.0026 (0.0840) | 0.0751 ± 0.0019 (0.0744) |

- **The flat control** (c_n on every link) gives own-dips 0.3004 / 0.1816 (high) and 0.2131 / 0.1194 (low), against the theory's 0.2994 / 0.1797 and 0.2120 / 0.1184. Its gap is 0.0803 ± 0.0035 (theory 0.0822).
- **At negative curvature the two designs move in opposite directions,** as predicted: design 1's dip falls by 3.4–4.4%, design 2's rises by 1.0–1.8%.
- **One amplitude** scaling all eight predicted excesses is A = 1.027 ± 0.020 with the registered covariance (χ² = 15.1 for the theory, on 8 degrees of freedom).
  - With the full seed-level covariance it is A = 1.000 ± 0.012 (χ² = 21.0; the check).
  - So the theory's amplitude is confirmed to about 2%. The fit quality is marginal.
- **All four negative-curvature rows sit below theory,** by 0.9–1.9σ.
  - Separate amplitudes: A₊ = 1.021 ± 0.022 and A₋ = 0.967 ± 0.030, which differ by 1.2σ (the check).
  - This is consistent with a sign-dependent theory error of about 1%, the same size as the theory's accuracy on the flat control (K72a). It is suggestive, not significant.
- **Charge is conserved exactly** in every run.

![Run 72](figures/72_equalplace.png)

**Verdicts, as registered.**
- **K72a PASSES:** the flat control matches the theory within 0.3–1.1%, inside the registered max(3σ, 3%).
- **K72b PASSES:** with no clocks, the places with the lowest and highest total conductance hold the same mean P to within −3×10⁻⁵ and −1×10⁻⁴ (±5×10⁻⁴), on both lattices.
- **K72c PASSES:** all eight ratios agree with the theory within 3σ; the largest deviation is −1.9σ.
- **K72d UNDECIDED:** the design-gap contrast gap(+) − gap(−) is +0.0079 ± 0.0032.
  - It has the predicted sign and size (theory +0.0096, a −0.5σ difference).
  - It is 2.5σ from zero (p ≈ 0.025), below the registered 3σ bar.
  - Neither sign's shift is resolved on its own: +0.0027 ± 0.0044 against a predicted +0.0018, and −0.0052 ± 0.0040 against −0.0078.
  - The error is the seed-paired one, which is right here. A bootstrap that resamples high and low runs independently gives ±0.0027 (3.0σ), but it ignores the correlation between same-seed pairs and must not be used to claim 3σ (the check).
  - The registered power estimate, σ ≈ 0.0031, matched the outcome.

**What the check added.**
1. **Confirmed with independent code:**
   - the geometry: volume per place 1 to 2×10⁻¹⁶; R̃ = ±1.09662 from a direct Christoffel–Ricci computation;
   - the theory: response matrices and predictions to 10⁻⁶;
   - the statistics: seed scatter over probe scatter has an rms of 1.00, so the errors are honest;
   - the resume: 50 runs, each exactly once; the killed runs left no file; everything is deterministic by seed; all hashes match.
2. **The clocks do not sit on a uniform neighbourhood.** Only their internal link is unit, and the lattice's conductances vary strongly within one spacing (above).
3. **The amplitude and fit quality depend on the covariance:** A = 1.027 ± 0.020 (registered) or 1.000 ± 0.012 (full). The negative-curvature shortfall is suggestive, consistent with about a 1% theory systematic.
4. **The run does not show that clock universality holds.** It confirms that the theory's design-dependent, non-universal responses to the medium's curvature are real at R̃h² ≈ 1.1. Their physical size scales as R̃hℓ_c, about 10⁻³⁹ for a neutron star (Run 70's check).
5. **K72b's block errors** may be about 1.5× low, because the blocks are about one relaxation time long. The margin is large.

**Reading.**
1. **On equal places, clocks follow the zero-range theory at both signs of curvature.**
   - The representation question of Run 70 is gone: every place has the same volume.
   - The predicted pattern, including the designs moving in opposite directions at negative curvature, is reproduced with a fitted amplitude of 1.00–1.03 (± 0.01–0.02, depending on the covariance).
2. **The design gap moves with the predicted sign and size, but not at the registered significance.** The contrast between the two signs is +0.0079 ± 0.0032 (2.5σ from zero), against a predicted +0.0096.
3. **What this does for clock universality on option 3's medium space.** Universality is not shown directly. The run shows that the zero-range theory predicts how clocks of different design respond to the medium's curvature, to about 1–2%, on an equal-volume lattice at both signs.
   - The design-dependent part is real at curvature radii of one spacing.
   - By the theory's own scaling it is about 0.01·R̃·h·ℓ_c, roughly 10⁻³⁹ for a neutron star (Run 70's check).
   - So universality at physical scales rests on a theory the engine now confirms, not on a direct measurement.
4. **Limits:**
   - the curvature is imposed, not solved from the medium's stress;
   - its radius is about one spacing, and the effect is non-local;
   - places are equal in volume but not in shape;
   - one geometry, at p_s = 1, with clocks oriented along the modulation;
   - about 1% theory systematic;
   - the gap contrast is at 2.5σ. Doubling the seeds for both signs (about two hours of CPU) would reach the registered bar if the predicted contrast is true.
