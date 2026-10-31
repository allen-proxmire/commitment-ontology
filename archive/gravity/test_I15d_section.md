### T-I15d: preferred-frame α₁ and α₂ of CO's lapse-coupled completion (a registered calculation, gravity sector)

*30 October 2026.*
- *Registered and hashed before the run (`testI15d/PREREG.md`, 12 files, 13:35:26 UTC), after four independent pre-registration checks (`checkPreI15d/`, `_b/`, `_c/`, `_d/`), whose corrections were adopted, and Allen's "go ahead". The last pre-hash code change (a dry-run case moved off the grid, the fourth check's D1) was reviewed before hashing only by the coordinator; the post-run check reviewed it and found it correct.*
- *A second independent agent checked the registered run (`checkI15d/REPORT.md`): the hashes verify, the run reproduces byte for byte, and an independently written derivation gives α₂ in closed form, matching all 40 registered points.*

**Why.** Reading I15's ruling keeps ε with a preferred time. Reading I15b showed CO's static sector is GR with matter on a metric depending on the foliation's lapse. This test computes the preferred-frame parameters of that completion.

**The class** (the α_E = 0 member). Gravity is GR plus a khronon with α_E = β_E = 0 (gravity waves at light speed; minimal Hořava) and λ_E free in [10⁻⁶, 10⁻¹]; matter couples to the lapse-dependent metric that reproduces Run 67's exterior. α_E = 0 is a choice: members with α_E ≠ 0 do not reduce to GR at ε = 0 (α₂(0) ≈ (α_E²/16)(3 + 2/λ_E), a fit), so requiring GR as ε → 0 selects α_E = 0 (an inference).

**Result.**
- **α₁** (recorded as a reading before the run; a gate in it):
$$
\alpha_1=\frac{8}{(1+\varepsilon)^2}-8=-4\alpha_\infty\approx-16\,\varepsilon\quad\text{for every }\lambda_E .
$$
- **α₂**, exactly (post-run check, closed form):
$$
\alpha_2=\frac{2\varepsilon\,[\varepsilon-\lambda_E(1-\varepsilon)]}{\lambda_E(1+\varepsilon)^2}=-2\varepsilon+\frac{2\varepsilon^2}{\lambda_E}+O(\varepsilon^2).
$$
  The khronon's O(ε/λ_E) tilt is pure slicing at first order and cancels, so at O(ε) α₂ = −α∞/2 = α₁/8, the same as the khronometric completion of Reading I15b.
- **The registered reading: EXCLUDED** (primary bound |α̂₂| < 1.6×10⁻⁹, Shao et al. 2013): untuned over the window, ε ≲ 8.0×10⁻¹⁰ (P∞/p_s ≳ 1.25×10⁹), below the registered floor of 10⁻⁸. Smaller ε is allowed; EXCLUDED means below that floor, not ε = 0.
- **Reported with equal prominence** (weak field, |α₂| < 4×10⁻⁷, Will 2001): ALLOWED, ε ≲ 2.1×10⁻⁷; the two-cone bound is tighter there.
- **A tuned curve.** α₂ = 0 exactly on λ_E = ε/(1−ε), which the registered strip search does not see (it is a zero at O(ε²/λ_E)). Inside the window the curve is excluded by the two-cone bound; below the window (λ_E ≈ ε < 10⁻⁶) it is untested.

**The bounds on ε in this completion.**

| bound | ε below | P∞/p_s above |
|---|---|---|
| α₁ (PSR J1738+0333) | 2.5×10⁻⁶ | 4×10⁵ |
| two-cone timing (GW170817, Eq. 4): γ_GW − γ_EM = −2ε/(1+ε) | 1.3×10⁻⁷ | 7.7×10⁶ |
| α₂ (pulsars), untuned | 8.0×10⁻¹⁰ | 1.25×10⁹ |

**Caveats.** The pulsar bound constrains strong-field α̂₂, not computed here (an O(1) sensitivity factor is an expectation). The α_E = 0 member is minimal Hořava, strongly coupled, which the record already doubts. Linear sources, first post-Newtonian order.

**What it means.** At ε ≈ 10⁻⁹ CO's gravity is observationally GR: β − 1 ≈ −4×10⁻¹⁰; Run 66's strong-equivalence violation ≈ 3×10⁻¹⁰; Run 67's exterior signatures (shadow +0.46ε, wave reflection) are nil. Run 67's throat and horn and R11's commitment surface (at N = 2ε) and core (at 3m) persist inside holes, but nothing outside depends on ε at a measurable level. *(Superseded 30 October: with ε = 0 in gravity, Reading I17 withdraws the throat, horn, commitment surface at 2ε and core at 3m, and the P∞ ≳ 5×10¹⁴ inference lapses.)*
