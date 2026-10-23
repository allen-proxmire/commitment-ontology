## Run 54: a second family of media, both draw rules

*20 October 2026. Registered and hashed before the run (`family54/PREREG_54.md`, 11:49 UTC). Run 52's results motivated it, and the identity it tests was post hoc in Run 52. An independent agent checked the run; its corrections are included and retract two of the draft's readings.*

**Question.** Run 52, in one family of media (g ∝ 1/P), suggested two things:
- under the variational draw (V), a body's equivalence-principle violation is M_far/E_H − 1 ≈ Δḡ;
- under the engine's draw (E), the far-field fall follows Δg(0.8P₀).

Do these hold in a family with a different depth profile?

**The medium.**
$$
R=\sqrt{p_s^2e^{2z/c}-\beta P_0^2},\qquad g=\beta\,(P_0/P)^2,\qquad \beta=4\times10^{-3}.
$$
- The background g is Run 52's, but deeper in it grows twice as fast (s ≡ −d ln g/d ln P = 2).
- The star, pattern, recalibration and grids are Run 52's, so the h = ½ kink applies again. The shifts are robust, and h = ⅓ agrees.

**Results.**

| h = ½ / ⅓ | rule E (engine) | rule V (variational) |
|---|---|---|
| first law (trapezoid) | −4.1 / −3.9 ×10⁻³ | 0.9 / 0.8 ×10⁻⁸ |
| Δḡ = ḡ − g_bg | 2.244 / 2.217 ×10⁻³ | 2.245 / 2.217 ×10⁻³ |
| shift of the star's energy-based fall | 2.239 / 2.212 ×10⁻³ | 2.239 / 2.209 ×10⁻³ |
| shift of the star's far-field fall | +9.1 / +8.9 ×10⁻⁴ | −2.30 / −2.31 ×10⁻³ |
| shift of the bound pattern's ω fall | +7.2 ×10⁻³ (½) | +1.55 / +1.50 ×10⁻² |

**Verdicts, as registered.**
- **K54a passes.** Under V the energy fall's shift equals Δḡ (ratios 0.998 and 0.997), and E_H's fall equals M_far/E_H − 1 to 3×10⁻⁶.
  - The lattice form, (ḡ − g_bg)(1 + v)/(1 + g_bg) plus the change in the lattice virial term v, predicts 2.2390 and 2.2097 ×10⁻³, against measured 2.2393 and 2.2094. That fully explains the ratios.
  - The 3×10⁻⁶ is finite-difference error in ε (Run 52's check: 4×10⁻⁹ as ε → 0).
- **K54b passes, but its premise is retracted.** Under E the far-field-fall shift is 0.89 of the Δg(0.8P₀) prediction at both grids, inside the registered 15%.
  - The check shows the 0.89 is systematic: E's shift is Δḡ − s·δv_E, where δv_E is E's virial excess.
  - That predicts 4.51 / 9.08 ×10⁻⁴ (h = ½, the two families) against measured 4.55 / 9.14, and 4.46 / 8.98 against 4.43 / 8.87 (h = ⅓).
  - The family ratio is 2.0, not the 2.25 that Δg(0.8P₀) implies. **Δg(0.8P₀) is not the controlling variable.**
- **Confirmed, not registered.** For s = 2, V's far-field-fall shift is −Δḡ, as the check had predicted: −2.30 / −2.31 against −2.24 / −2.22 ×10⁻³.

**Reading.**
1. **Under V, a whole body's equivalence-principle violation is**
$$
\Delta_{\rm SEP}=\frac{M_{\rm far}}{E_H}-1\;\approx\;\bar g-g_{\rm bg},
$$
   where ḡ − g_bg is its draw-weighted excess of g over the background's. This holds in both families, assuming inertia equals E_H.
   - For a star at U ≈ 0.22, Δḡ/g_bg = 0.25 (s = 1) or 0.56 (s = 2).
   - The pulsar triple (|Δ| ≲ 2.3×10⁻⁶) then needs g_bg ≲ 9×10⁻⁶ (s = 1) or ≲ 4×10⁻⁶ (s = 2) in this toy medium.
2. **It is not additive.** A bound quantum's own violation is set by the g-weighting of the draw it adds, including the star's restructuring. Its ω-fall shift is about 6.9 times the star's here (6.2 in the first family), consistent with V's Maxwell relation (b·Δmiss: 1.55 / 1.47 ×10⁻²).
3. **The rules do not "agree on falling" (retracted).**
   - Under E there is no conserved energy, so E_H's fall is not a mass ratio. Its agreement with V at O(g) is forced: E's virial excess cancels the extra term.
   - The rules disagree for a bound quantum by a factor of 2.15.
   - Only under V is the medium's equivalence-principle violation well defined.
4. **The far-field fall is a convention-dependent measure** (≈ (1 − s)Δḡ under V). It should not be used as the equivalence-principle test.
