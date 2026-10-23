## Run 48: the dilation argument, made exact

*20 October 2026. Registered and hashed with every imported module before the run (`dilation/PREREG_48.md`, `PREREG_48_49.sha256`). Disclosures:*
- *The time stamp inside the hash file (06:16 UTC) is self-reported. The file was rewritten at 06:17 to move a note out, with the hashes unchanged. Every hashed file is older than the outputs.*
- *Runs 48 and 49 were first started as untracked processes, stopped within about 20 s with no output, and restarted as tracked jobs (`RESTART_NOTE.md`).*
- *One code check (h = 0.9, not a registered point) ran before registering.*
- *The argument came from Run 46c's independent check.*
- *The post hoc analyses (`posthoc48.py`) were written after the results.*
- *An independent agent checked the run; its corrections are included.*

**Question.** Run 46c closed the fall line at the engine's resolution, about 10⁻³. Its check suggested that a uniform outside potential only rescales everything. If that is exact, the fall defect is a grid effect plus a medium effect, and the pulsar triple tests only the medium.

**The claim (registered).**

**(i) Exact discrete dilation.** Take an exactly scale-free medium, R(z) = p_s e^{z/c}, and let λ = e^{−ε}. Then the engine at grid spacing h in an outside potential ε is the same lattice computation as the engine at spacing h e^{ε} with none: same draws, same radius in lattice units, P → λP, m → λm, ω → λ²ω, ψ² → λ²ψ², with amplitude κ′ = λ²κ. Hence
$$
E_{\rm body}(\varepsilon;h)=E_{\rm body}(0;he^{\varepsilon}),\qquad
\omega(\varepsilon;h)=e^{-2\varepsilon}\,\omega(0;he^{\varepsilon}),
$$
$$
E_{\rm pat}(\varepsilon;h;\kappa)=E_{\rm pat}(0;he^{\varepsilon};e^{-2\varepsilon}\kappa).
$$

**(ii) The fall defect is a grid derivative.** With e(h) the physical energy at U_ext = 0,
$$
\Delta=-\frac{d\ln e(h)}{d\ln h}.
$$
The ε slope is ½ dΔ/d ln h.

**(iii) Continuum.** Δ → 0 wherever e(h) converges. The check adds a condition: the limit must be h → 0 with the box growing (Lh → ∞). The engine's box is fixed at 80 cells, and its periodic pattern box shrinks in physical units as h → 0.

**(iv) The real medium.** The registration wrote Δ = Δ_lattice + A·p_s/P₀. That variable is wrong; see K48b.

**Results** (fall defects ×10⁻³ at U ≈ 0.22, scale-free medium).

| h | pattern by far field | by frequency | body's own | Run 46c targets (far field / frequency / body) | pull miss |
|---|---|---|---|---|---|
| 1 | +8.237 | +10.332 | +1.876 | +8.015 / +10.159 / +1.803 | −0.179 b |
| ½ | −0.531 | +2.314 | −0.151 | −0.747 / +2.144 / −0.223 | −0.196 b |
| ⅓ | −0.339 | +1.032 | −0.107 | −0.538 / +0.863 / −0.180 | −0.201 b |
| ¼ | −0.210 | +0.581 | −0.069 | — | −0.202 b |
| ⅕ | −0.140 | +0.371 | −0.047 | — | −0.203 b |

**Verdicts, as registered.**
- **K48a passes.** Case 1 (h = ½, ε = 0.01) and case 2 (h e^{0.01}, no potential, e^{−0.02}κ) agree:

| quantity | relative difference |
|---|---|
| E_body | 1.1×10⁻¹⁶ |
| ω | 4.4×10⁻¹⁶ |
| E_pat | 3.1×10⁻¹² |
| U_self | 1.1×10⁻¹⁶ |
| R | 0 |

  - The check confirmed (i) line by line in the code: the shift, the draws, the proper-size rule against its unshifted reference, the stress, and the pattern's mass and amplitude.
  - Nothing trivial makes the two cases coincide: they differ in h, R₀, count, m, κ, U_ext and starting guess.
  - The test shows the code has no hidden scale. It cannot catch an error common to both cases.
- **K48b: undecided** (worst point 2.45 tolerances).
  - Every point sits above its target by an offset that does not change with the grid: +2.0 to +2.2 (far field), +1.7 (frequency) and +0.7 (body) ×10⁻⁴.
- **K48c (reported):**
  - All three defects shrink from h = ⅓ to ⅕, as expected.
  - The frequency prediction missed by +28% and +35%. It was built on q = 2.244, an exponent taken from the offset targets. The miss splits exactly into the offset (×1.196) and the exponent (×1.07 and ×1.13).

**Post hoc (not registered; corrected by the check).**
1. **Why K48b missed: the targets were extrapolated in the wrong variable.**
   - Run 46c's media all had P₀ = 4096 and differed in p_s. Each departs from scale-free by g = c d ln R/dz − 1, with g·P₀ = 62.4, 13.7, 1.03 = p_s − (1.6, 2.3, 3.0).
   - g·P also rises as P falls inside the body, by an amount nearly independent of p_s.
   - To first order the outside shift breaks the dilation through the *change* of g across the body:
$$
\Delta=\Delta_{\rm lattice}(h)+A'\,\Delta g,\qquad \Delta g\equiv g(P_{\rm inside})-g(P_0).
$$
   - Extrapolating Run 46c in Δg, for any P_inside between 0.6P₀ and 0.9P₀, shrinks eight of the nine offsets to ≤ 1.5×10⁻⁵. The far field at h = ⅓ is −2 to −3×10⁻⁵, a quarter of its tolerance.
   - Extrapolating in g(P₀) alone overcorrects, with offsets proportional to A.
   - The U_self mismatch (+1.4×10⁻⁴) is not the explanation; its effect on Δ is about 10⁻⁶.
   - **With the right variable, the medium's departure from scale-free accounts for the leftover.**
2. **In the scale-free medium the frequency-based fall goes as h² exactly:** Δ_ω/h² = 9.26, 9.29, 9.30, 9.28 ×10⁻³ from ½ to ⅕. Run 46c's exponent of 2.24 came from the medium offset.
3. **Continuum limits.**
   - Fitting c₀ + ah² + bh⁴ to the four finest grids gives c₀ = +1.6, −1.1 and −1.5 ×10⁻⁶ (far field, frequency, body), with residuals ≤ 4×10⁻⁷.
   - Other forms spread the far field's limit by about 5×10⁻⁵, and the others' by about 10⁻⁵.
   - The far-field and body defects are not yet in the h² regime: Δ/h² is still drifting.
   - **Consistent with zero, about 100 times tighter than Run 46c, but not at the pulsar level.**
   - The pull miss goes to −0.2046 ± 0.0001 b.

![Runs 48 and 49](figures/48_49.png)

**Reading.**
1. **The dilation identity is exact in the engine (K48a).** So in a scale-free medium a body's fall defect, and a bound pattern's, is the grid derivative of its energy. It vanishes in the continuum, with the box growing. Numerically it is zero to 10⁻⁵–5×10⁻⁵.
   - In plain terms: at neutron-star strength the full pattern rule makes bound matter fall exactly like its energy. What was left in Runs 45–46c is the grid and the medium, not the rule.
   - For body A this is partly built in: the proper-size rule is what makes the body's size follow the potential.
2. **The registered medium attribution is undecided.** The post hoc analysis supports it with the right variable: the leftover is the medium's change of log-slope across the body, not p_s/P₀.
3. **The pulsar triple now tests CO's medium, not the engine.**
   - Published 95% bounds: |Δ| < 2.6×10⁻⁶ (Archibald et al. 2018) and |Δ| < 1.5–2.3×10⁻⁶ (Voisin et al. 2024).
   - Per unit Δg at 0.8P₀, A′ = 1.63, 1.26 and 0.53 (far field, frequency, body).
   - So the triple needs |Δg| ≲ 1.4×10⁻⁶ ÷ (the share of the star's energy in bound patterns) and |Δg| ≲ 4×10⁻⁶ from the body's own binding, whose share is 1.
   - In the engine's toy medium, Δg includes a part that does not depend on p_s. So this constrains CO only if that toy is CO's medium and nothing else breaks the dilation.
   - The coefficients were measured only at U ≈ 0.22, and the triple compares a neutron star with a white dwarf, not one body with nothing.
   - **CO's prediction is an equivalence-principle violation whose size is set by how far its medium departs from scale-free across a star's depth.**
4. **The fall line is no longer limited by the engine's resolution.** It is now a question about CO's medium.
