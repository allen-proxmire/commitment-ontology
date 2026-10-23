## 9zw. Run 51: a controlled departure from scale-free, and a larger box

*20 October 2026. Registered and hashed with every imported module before the run (`medium51/PREREG_51.md`, 07:35 UTC; the medium run started seconds later). Code checks were limited to building the 120-cell Green's function and a syntax check. An independent agent checked the run; its corrections are included.*

**Question.** Run 48 showed that in a scale-free medium the fall defect is purely a grid effect. Post hoc, its check found that the leftover in the engine's real media follows the medium's departure from scale-free, g = c d ln R/dz − 1, through its change across the body, Δg. Does it, when that departure is set by hand?

**(a) The controlled medium.**
$$
R(z)=p_s\big(e^{z/c}-\alpha\big)\quad\Rightarrow\quad g=\alpha\,p_s/P\ \text{exactly}.
$$
The engine is Run 48's at h = ⅓, with αp_s/P₀ = 0, 2×10⁻³ and 4×10⁻³. It uses Run 46c's body model, which Run 50 has since replaced. The fall defects come from direct outside potentials (U_ext = ±0.005, centred).

| αp_s/P₀ | U_self | pattern by far field | by frequency | body's own |
|---|---|---|---|---|
| 0 | 0.21765 | −0.3386×10⁻³ | +1.0319×10⁻³ | −0.1074×10⁻³ |
| 2×10⁻³ | 0.21809 | +0.4959×10⁻³ | +1.6736×10⁻³ | +0.1641×10⁻³ |
| 4×10⁻³ | 0.21852 | +1.3324×10⁻³ | +2.3162×10⁻³ | +0.4357×10⁻³ |

**Verdicts, as registered: PASS.**
- **K51c (control).** At α = 0 the direct method reproduces Run 48's identity values to ≤ 5×10⁻⁸.
- **K51a (linearity).** Ratios 2.002, 2.001 and 2.001 (registered 2 ± 0.1).
  - At departures this small, a ratio of 2 is close to automatic for any smooth dependence, so K51a is a weak test.
- **K51b (size).** The slopes per unit αp_s/P₀ are 0.418, 0.321 and 0.136, against the registered 0.409, 0.315 and 0.133: within 2.1% (registered 15%).
  - They match Run 46c's *uncorrected* slopes per unit p_s/P₀ (0.418, 0.323, 0.136) to 0.2–0.5%.
  - The registered division by 1.023, a correction for the media's measured g, is what creates the 2% offset.

**(b) The larger box.** Run 48's h = ⅓ point was repeated in a 120-cell box. The fall defects changed by ≤ 2×10⁻¹⁰ and the pull by 10⁻¹¹.
- The field uses the free-space Green's function, so it never had a box. This tests only the pattern's periodic box, and a difference that small was expected.
- It was tested at h = ⅓ only.

**Reading.**
1. **For a 1/P departure from scale-free, the fall shifts linearly, matching Run 46c's media to about 2%.** With Run 48:
$$
\Delta=\underbrace{-\frac{d\ln e}{d\ln h}}_{\to\,0\ \text{(continuum)}}+\;A'\,\Delta g ,
$$
   with Δg = g(0.8P₀) − g(P₀). At U ≈ 0.22, A′ ≈ 1.67, 1.28 and 0.54 (far field, frequency, body), 2.5% above Run 48's estimate. So Δg at 0.8P₀ is a universal variable only to about 3%.
2. **Only one family of departures was tested.** For it, Δg, g(P₀) and p_s/P₀ are proportional, so "only through Δg" is not yet distinguished from those alternatives. A second family, for example g ∝ 1/P², would test it.
3. **The fall test at neutron-star strength now measures ED's medium.**
   - In the scale-free part, bound matter falls exactly like its energy.
   - The pulsar triple bounds how far the medium departs from scale-free across a star.
   - The coefficients A′ were measured with the old body model. Run 50's check also notes that in a non-scale-free medium the engine's draw is not variational (it lacks a factor 1 + g). The Δg fall defect may partly be that.
