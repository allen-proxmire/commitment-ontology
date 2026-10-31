## Run 79: the local rule fixed by option 3's planar solution, against light bending and perihelion

*23 October 2026. Choice (iii) of the spherical design note (Note G), begun with one candidate rule for reading (B). A calculation, registered and hashed before it was run (`rule79/PREREG_79.md`, 10:29:13 UTC). The analytic result was derived before registration and is disclosed there; the run checks it numerically and scores it against measurements. An independent agent checked it; its corrections are included, including to the registration's own wording ("the simplest local rule").*

**Question.** Under reading (B) the relations stay fixed, and the medium's state across them carries option 3's curved space. One candidate rule sets each relation's hop weight from the medium's field at that relation, by direction. Option 3's planar solution fixes such a rule. On Run 77's equal-place lattice the x-links are B² and the y/z-links 1/B, with B² = e^{4(φ_sheet − φ)}, so
$$
W_\parallel=P_0\,e^{-4\varphi},\qquad W_\perp=P_0^{-1/2}\,e^{+2\varphi},
$$
with ∥ along ∇φ and ⊥ across it.
- **How unique.** Among rules that depend on φ alone, option 3's planar equations force P = W_∥ to satisfy P″ = 0 and P′ = ±4J (J the flux). That gives two branches:
  - W_∥ ∝ e^{−4φ}, Run 77's (Rindler) branch;
  - W_∥ ∝ e^{+4φ}, a Taub-type branch whose P reaches zero at a finite distance.
- **The constant P₀.** In planar symmetry P₀ is a gauge: a constant rescaling that keeps equal places. Far from a single mass it is physical: P₀ = 1 (φ → 0 far away) keeps space asymptotically flat; any other value makes it conical. γ does not depend on it.

**Applied to a single mass, does the rule pass the solar-system tests?**

**The calculation.** On a flat shell graph (4πρ² places per shell), the medium's radial flux is conserved, ρ²W_∥φ′ = −M, so on Run 77's branch
$$
e^{-4\varphi}=1-\frac{4M}{\rho}.
$$
- The medium's space read off the hop weights (equal places): γ̃_ρρ = 1/W_∥ = e^{4φ}, γ̃_θθ = ρ²/W_⊥ = ρ²e^{−2φ}. Fed option 3's own spherical weights, the same reading returns Schwarzschild (the check).
- Option 3's clock as ε → 0 is N = e^{−φ}. With the pattern rule's metric ds² = −N²dt² + N⁻²γ̃:
$$
ds^2=-\Big(1-\frac{4M}{\rho}\Big)^{1/2}dt^2+\Big(1-\frac{4M}{\rho}\Big)^{-3/2}d\rho^2+\rho^2d\Omega^2 .
$$
- ρ is the areal radius. In standard PPN form (−g_tt = 1 − 2M/r + 2(β − γ)M²/r², g_rr = 1 + 2γM/r), γ = 3 and β = 2.
- With the medium's scale: γ = (3 + ε)/(1 + ε) and β = (4 + ε)/(2(1 + ε)) (the check). Cassini would need ε > 2×10⁴, against Run 66's ε < 6×10⁻⁶, so ε does not rescue it.

**Results.**

| | γ | β | light deflection at the Sun's limb | Mercury's perihelion, per century |
|---|---|---|---|---|
| GR (option 3) | 1 | 1 | 1.751″ | 42.98″ |
| the rule, Run 77's branch | 3 | 2 | 3.502″ (2.0000×, exact geodesic integral) | 85.96″ (2.0000×) |
| the rule, the other branch | −1 | 0 | none at first order | none at first order |
| measured | γ − 1 = (2.1 ± 2.3)×10⁻⁵ (Cassini) | β − 1 = (0.2 ± 2.5)×10⁻⁵ (ephemerides; a 25% residual-change interval, not 1σ) | Eddington 1919: 1.98 ± 0.12″, 1.61 ± 0.30″ | about 43″ |

- **K79b PASSES:** the discrete solve matches e^{−4φ} = 1 − 4M/ρ to 2.8×10⁻⁵ for ρ = 20–1000. The check notes that 2.5×10⁻⁵ of this is the outer boundary (φ = 0 at ρ = 2×10⁵, so the solved problem is e^{−4φ} = 1 + 4M/R − 4M/ρ); against that the scheme's own error is 3×10⁻⁶. It is a quadrature check of the same equation, not an engine run.
- **K79c: RULE EXCLUDED.** The registered fit's γ = 2.93 is 8.4×10⁴σ from Cassini's value; γ = 3 is 8.7×10⁴σ. Put plainly: γ − 1 = 2, against a measured |γ − 1| below 10⁻⁴. The other branch, γ = −1, is excluded by the same margin.

**What the check added.**
1. **Independent reproduction.** The hashes match, and the files were written in order: script, then hash, then run 4 s later, then the post hoc refit. The analytic metric, γ = 3 and β = 2 were re-derived by hand, in both areal and isotropic form. Exact geodesic integrals give deflection and perihelion ratios of 2.0000063 and 2.0000002 against GR.
2. **The registered fit had two flaws; the verdict uses γ only and survives both.**
   - It took γ = b₁/2, assuming the fitted mass is exactly 1. The fitted mass was 0.977; normalised by it, the same fit gives γ = 2.99988.
   - It had no constant term, so the boundary offset (about 2M/R = 10⁻⁵) biased β to −12.8.
   - The controls (options 1 and 3) were fitted from exact forms, not through the same boundary and solver. Option 1 solved with the same boundary gives β = −13.7 under the registered fit, which would have exposed the flaw.
   - So `rule79.json`'s β (−12.8), z_β, perihelion factor (6.88) and deflection factor (1.966) are artefacts. The correct values are 2, (not a σ count), 2 and 2.
   - The post hoc refit is a fair fix: sub-range fits give γ = 3.0000000, β = 1.999999.
3. **The measurements.** Cassini's (2.1 ± 2.3)×10⁻⁵ is right. The β interval matches Verma et al.'s Table 5 (INPOP13a, all data), but it is an interval of violation (residuals change by less than 25%), not a 1σ error, and it comes from varying β and γ near 1.
4. **The planar rule is a gauge effect there and real curvature in spherical symmetry.**
   - In planar symmetry the first-order stretch of option 3's lattice is a linearised change of coordinates. On a flat shell graph, option 3's own weights are 1 + 2m²/r² and 1 − m²/r²: equal to 1 at first order, like option 1.
   - The rule's weights, 1 − 4M/ρ and 1 + 2M/ρ, give R̃_θθ = 2M/ρ and R̃_ρρ = −4M/ρ³ at first order. Option 3 requires R̃_θθ = 0 and R̃_ρρ = 2φ′², which is of order M².
5. **What the run does not show** (the check's main correction).
   - Within each symmetry, option 3's space *is* a function of the local field. In spherical symmetry it is a different function of φ, and for any spherical vacuum exterior it is (κ sinh φ/|∇φ|)^{4/3}, with κ the curvature of φ's level surfaces. So the run shows only that no single function of φ works in both symmetries.
   - **Rules also using |∇φ| (the check's extension).** Any such rule exact in planar symmetry has the form W_∥ = P₀(I)e^{−4φ}, with I = |∇φ|e^{−4φ}. A smooth P₀ leaves γ = 3 for every mass; a non-analytic one can set γ = 1 for one mass only.
   - **Rules using second derivatives** (such as κ) are not excluded by these two cases. A rule exact for every spherical exterior would have to be discontinuous as κ → 0, the planar limit. Without symmetry the question is open.
   - The rule depends on φ's absolute value, so a background potential from distant matter would enter local geometry. Run 79 does not address this.
   - **W = 1 (option 1) is a simpler local rule,** and it passes (γ = β = 1). So "the simplest local rule" in the registration was not a fair label.
6. **The planar post hoc check** (Run 77's measured field obeys the rule to 1–2%) only restates Run 77's construction. It is not evidence about the rule.

**Reading.**
1. **The local rule fixed by option 3's planar solution is excluded by light bending and by Mercury's perihelion.** It doubles both, and Eddington's 1919 eclipse already rules it out. Its other branch gives no first-order deflection and is excluded too.
2. **Why: no single function of the local field reproduces option 3's space in both planar and spherical symmetry.** Planar symmetry makes the first-order stretch look like geometry when it is only coordinates. Copied to a single mass, that stretch becomes real curvature at first order.
3. **What it means for reading (B)** (an inference). Under (B) the hop weights cannot be a function of φ alone. Nor, if they are to be exact in planar symmetry, can they be a function of φ and |∇φ|. Rules using second derivatives, such as the curvature of the field's level surfaces, remain open. A state carried by the relations that builds up across space (as relations already carry shear in Run 11b) is another possibility. The run does not choose between them.
4. **For reading (A),** nothing here is tested. The counts of relations would have to give option 3's space in both symmetries as well.
5. **Limits:**
   - one family of rules (functions of φ, by direction), and both of its branches;
   - first-derivative rules covered only by the check's argument;
   - second-derivative rules and configurations without symmetry untested;
   - the absolute-value dependence of the rule not addressed.
