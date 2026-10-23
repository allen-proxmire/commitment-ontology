## Run 52: should ED's draw be the variational one?

*20 October 2026. Registered and hashed with every imported module before the run (`vardraw/PREREG_52.md`, 11:40 UTC). One code check (h = 1, not a registered grid) is disclosed; it motivated recalibrating every star. The identity reading is post hoc, and the independent check sharpened it; its corrections are included.*

**Question.** Run 50's energy principle holds exactly only in a scale-free medium. ED's field is linear in z, φ = z₀ − z = 6G∗d, and matter feels it through N = R(z)/P₀. So
$$
\frac{dU}{d\phi}=\frac{1+g}{c},\qquad g=c\,\frac{d\ln R}{dz}-1 .
$$
The draw that makes field, matter and pattern the Euler–Lagrange equations of one action, with field term −(1/12c)Σ_links(∇φ)², is
$$
d_V=T\,(1+g),
$$
where T is the Tolman/Komar draw. The engine's rule is d_E = T. Which should ED use?

**Setup.**
- **Star and pattern:** Run 50's star in exact hydrostatic balance (Γ = 2) and its pattern, at h = ½ and ⅓.
- **Medium:** Run 51's controlled medium, g = αp_s/P, at αp_s/P₀ = 4×10⁻³, under rule E and rule V, plus α = 0 as the control.
- **Every star is recalibrated** to Run 50's U_self and surface radius. The α = 0 rows reproduce Run 50 to 10⁻⁸.
- **The kink.** At h = ½ the radius target, 8.000 cells, puts six surface cells exactly at the matter threshold, so the absolute ω and far-field falls there average two branches. The *shifts* between configurations are robust (the check).

**Results.**

| h = ½ / ⅓ | α = 0 | rule E (engine) | rule V (variational) |
|---|---|---|---|
| first law, ΔE_H/κω̄ − 1 (trapezoid; about 10⁻⁹ with exact quadrature, Run 53's check) | 1.0 / 0.8 ×10⁻⁸ | −3.2 / −3.0 ×10⁻³ | 0.9 / 0.8 ×10⁻⁸ |
| active/passive (by construction) | 1 | 1/(1 + ḡ) = 0.99503 | 1 |
| (ΣT − E_H)/ΣT | 6.74 / 3.10 ×10⁻⁴ | 12.2 / 8.5 ×10⁻⁴ | 6.75 / 3.11 ×10⁻⁴ |
| far-field miss (b) | −0.006 / −0.028 | −0.004 / −0.026 | +0.024 / +0.001 |
| shift of the star's energy-based fall | — | +9.84 / +9.74 ×10⁻⁴ | +9.91 / +9.79 ×10⁻⁴ |
| shift of the star's far-field fall | — | +4.6 / +4.4 ×10⁻⁴ | +0.1 / −0.1 ×10⁻⁴ |
| shift of the pattern's ω fall | — | +3.0 / +2.9 ×10⁻³ | +6.2 / +6.0 ×10⁻³ |

**Verdicts, as registered.**
- **K52a passes.** Rule V is variational: its first law holds to 10⁻⁸ in the non-scale-free medium.
- **K52c passes.** Under V the virial identity holds in any medium: (ΣT − E_H)/ΣT is unchanged by the medium to 8×10⁻⁷. The dilation argument never involves R(z).
- **K52b: PARTLY.** The star's far-field-fall shift vanishes under V (class DRAW), and the pattern's ω-fall shift doubles (2.07×).
- **Reported:** V's far-field miss shifts by +0.0306 / +0.0295 b, as predicted from M_far = E_H(1 + ḡ)/(1 + g_bg).

**What the check established.**
1. **The exact relation under V.** E_H is the stationary value of the energy, and the outside potential enters only through the background, so
$$
\frac{dE_H}{dU_{\rm ext}}=-\frac{\sum d}{1+g_{\rm bg}}=-M_{\rm far}
$$
   (Hellmann–Feynman). Hence, if inertia equals E_H (an assumption, since the static action fixes no inertia), the equivalence-principle violation is exactly:
$$
\Delta_{\rm SEP}=\frac{M_{\rm far}}{E_H}-1=\frac{(1+\bar g)\,(\Sigma T/E_H)}{1+g_{\rm bg}}-1\;\approx\;\bar g-g_{\rm bg}\ \ (\text{continuum}).
$$
   - With the lattice part included it predicts the shifts as 9.909 / 9.793 ×10⁻⁴, against measured 9.911 / 9.792.
   - The remaining residuals are finite-difference error in ε.
   - ḡ − g_bg is the body's draw-weighted excess of g over the background's: about 0.25 g_bg for this star.
2. **V does not remove the medium's fall shift; it makes it well defined.**
   - The DRAW class for the far-field fall reflects how the far-field mass is normalised and the g ∝ 1/P shape: S_V(M_far) ≈ (1 − s)(ḡ − g_bg) with s = −d ln g/d ln P = 1. Run 54 confirmed this for s = 2.
   - E's energy fall shifts by nearly the same amount (S_V/S_E = 1.007 and 1.005). But under E there is no conserved energy, so that agreement at O(g) is forced (Run 54's check) and is not a statement about E's physics.
   - The rules disagree for a bound quantum by a factor of about 2.
3. **Under E there is no stationary energy.** ∂ℰ/∂φ ≠ 0, so E_H's derivative is not a passive mass, and comparing identities under E is empty.
4. **Active/passive are definitions in the code, not measurements.** Action = reaction under V is analytic only; no two-body run was made.
   - The earlier claim that E would make binaries self-accelerate is **wrong at Newtonian order**: the centre of mass only wobbles (about 6 cm/s for a neutron star with a white dwarf).
   - A secular effect arises only at first post-Newtonian order, ζ₂-like and of size ~g_bg, marginal against |ζ₂| < 1.3×10⁻⁵. It is not a strong argument for V.
5. **Why the ω fall doubles under V.** V has a Maxwell relation, ∂ω/∂U = −∂M_far/∂κ. So a bound quantum's ω fall is its own passive/inertial − 1, equal to b × its far-field miss (6.19 / 5.99 against 6.17 / 5.88 ×10⁻³).
   - Its shift is the g-weighting of the draw the quantum adds, including the star's restructuring: about 2.5 g_bg.
   - G_eff ∝ (1 + g_bg)² under V, against (1 + g_bg) under E.
   - **So Δ_SEP is not additive:** a bound quantum's violation is about 6 times its host star's. This is not a defect of V.

![Runs 52–54](figures/52_54.png)

**Reading.**
1. **Rule V is the self-consistent one.** From one action it has:
   - an exact first law;
   - passive = active mass, exactly;
   - the virial identity in any medium;
   - a symmetric interaction energy.

   Rule E breaks the first law at about 0.7 g.
2. **The medium's equivalence-principle violation is physics of the medium's scale, well defined only under V:** Δ_SEP = M_far/E_H − 1 ≈ ḡ − g_bg. It is not additive (point 5).
   - The pulsar triple (|Δ| ≲ 2.3×10⁻⁶) with Δ ≈ 0.25 g_bg for a star like this one gives g_bg ≲ 9×10⁻⁶, i.e. P₀/(αp_s) ≳ 10⁵ in this toy medium: ED's stated range.
3. **Recommendation, as registered: adopt V, on consistency grounds.** The check adds a condition, and the choice needs a ruling:
   - V assumes the field stays linear in z;
   - a second self-consistent option keeps E's draw and makes the field linear in U instead, which takes the medium out of gravity altogether;
   - inertia = E_H remains an assumption.
