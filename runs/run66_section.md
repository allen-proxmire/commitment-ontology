## 9zzm. Run 66: option 3 in ED's own variables, and the strong-equivalence-principle formula under it

*21 October 2026. Allen: "go ahead as recommended" (08:02), step 1. Registered and hashed before the run (`sep66/PREREG_66.md`, 06:25 UTC; Amendment 1 at 06:27 UTC, before any result was seen). An independent agent checked it; its corrections are included.*
- *Disclosed: the claims were derived before registration, in my own working. Smoke tests on unregistered stars, whose results I saw, informed two thresholds (listed in the registration).*
- *Amendment 1: the registered Newton tolerance (10⁻¹³) was below the solver's noise floor, and the first star stopped at 7×10⁻¹³. It was set to 10⁻¹¹; no test threshold changed. The original files and the failed log are kept.*

**Question.** Run 65 found that ED's static field equation is GR's equation for the clock rate, and that option 3 changes only the rule for space. Under option 3, is the strong-equivalence-principle violation still Δ ≈ C p_s/P₀, with Run 65's C, or does the formula change? And what does the engine's medium need in order to carry option 3?

**1. Option 3 in ED's own variables (an identity).** Write a static metric on the *medium's space* γ̃_ij = N²g_ij, the space whose coordinate light speed is N² (ED's pattern rule):
$$
ds^2=-N^2dt^2+N^{-2}\,\tilde\gamma_{ij}\,dx^idx^j,\qquad N=e^{-U}.
$$
GR's static equations for a perfect fluid are then exactly three statements:
- **ED's field equation, on γ̃** (GR's R₀₀ equation):
$$
\tilde\Delta U=-4\pi\,(e+3p)\,e^{2U} ;
$$
- **γ̃ curved by stress** (GR's R_ij equations):
$$
\tilde R_{ij}=2\,\partial_iU\,\partial_jU-16\pi\,p\,e^{2U}\,\tilde\gamma_{ij} ;
$$
- **balance:** hN = const.

ED's original rule for space is γ̃ flat (g_ij = N⁻²δ_ij). Option 3 is γ̃ curved by stress: the field's own tension (2∂U∂U, the "binding tension" of §10's (c2)) and matter's pressure. Energy density does not curve it. So option 3 says, in ED's words, **binding tension shears the medium's space**, and that is all it changes.

**What this corrects.** Run 65 recorded that, under option 3, ruling 2's "the vacuum draws nothing" and "g₀₀ = −e^{−2U}" hold only at first order. That read them with the flat Laplacian of isotropic coordinates. On γ̃ both hold to all orders: in vacuum Δ̃U = 0 exactly, and g₀₀ = −e^{−2U} by construction. The pattern rule c = N² also holds, relative to γ̃. For Schwarzschild, γ̃ = dr² + (r² − 2Mr)dΩ² and r²(1 − 2M/r)U′ = −M, so U is harmonic on γ̃.

**2. ED's medium on γ̃.** Possibility hops on γ̃. Equivalently it hops on physical space at the local tick rate, since √γ̃ γ̃^{ij} = N√γ g^{ij}. The medium carries φ linearly (field action (1/8π)|∇̃φ|², whose stress ∂_iφ∂_jφ curves γ̃). The clock is the medium's occupancy. In the mean field of f(n) = c ln(1 + n/p_s),
$$
N=\frac{P}{P_\infty}=(1+\varepsilon)\,e^{-\varphi}-\varepsilon,\qquad \varepsilon=\frac{p_s}{P_\infty},\qquad \frac{dU}{d\varphi}=1+g,\quad g=\frac{\varepsilon}{N}=\frac{p_s}{P}.
$$
The variational draw (rule V, adopted 20 October) is T(1 + g), with T the Komar density (e + 3p)N√γ. With ε = 0 this is GR exactly.

**3. The energy and the formula.** At fixed baryon number the energy functional is stationary. On shell, by γ̃'s trace equation (R̃ = 2|∇̃φ|² − 48πpe^{2U}), its value is the Komar integral:
$$
E=\int\!\Big[\frac{|\tilde\nabla\varphi|^2}{8\pi}-\frac{\tilde R}{16\pi}+\frac{e}{N^2}\Big]\sqrt{\tilde\gamma}\,d^3x=\int T,
$$
which is the ADM mass when ε = 0. Inertia = E (Allen's ruling of 20 October). An outside potential enters only through the background, so by Hellmann–Feynman the passive mass is m_p = −dE/dU_ext = ∫(1 + g)T/(1 + g_bg), equal to the far-field mass. Hence
$$
\Delta=\frac{m_p}{E}-1=\frac{1+\bar g}{1+g_{\rm bg}}-1=\frac{\varepsilon\,C}{1+\varepsilon},\qquad C=\Big\langle\frac1N\Big\rangle_{T}-1 ,
$$
with the Komar weighting and N → 1 far away. **This is Run 55's formula unchanged.** Run 65's C is the right coefficient.

**Results** (the star with E = 1.438 M☉, PSR J0337+1715's pulsar).

| | SLy | APR4 | MPA1 |
|---|---|---|---|
| C, γ̃ solver at ε = 0 (Run 65's isotropic solver) | 0.425412 (0.425412) | 0.441910 (0.441910) | 0.374906 (0.374906) |
| Δ from the passive mass against the formula (relative): ε = 10⁻⁴ / 10⁻³ / 10⁻² | 4×10⁻⁶ / 5×10⁻⁷ / 2×10⁻⁷ | 4×10⁻⁵ / 3×10⁻⁷ / 2×10⁻⁶ | 4×10⁻⁵ / 2×10⁻⁵ / 2×10⁻⁷ |
| C(ε) = Δ(1 + ε)/ε at ε = 10⁻⁴, 10⁻³, 10⁻² | 0.42572, 0.42845, 0.45822 | 0.44223, 0.44492, 0.47421 | 0.37510, 0.37704, 0.39739 |
| extrapolated to ε = 0 (against Run 65) | 0.425411 (2×10⁻⁶) | 0.441927 (4×10⁻⁵) | 0.374889 (4×10⁻⁵) |
| dC/dε (the star's restructuring) | 3.0 | 3.0 | 2.1 |

**Verdicts, as registered.**
- **K66a FAILS as registered, on one of its four parts.**
  - The γ̃ solver reproduces GR: M_max and R(1.4 M☉) match TOV to 5×10⁻¹¹; the energy functional equals the Komar integral to 2×10⁻¹¹; the passive mass at ε = 0 gives Δ = 4×10⁻¹⁰.
  - The constraint check failed: a residual of 1.2×10⁻⁷ against the registered 10⁻⁹.
  - **Cause (post hoc, `posthoc66_limit.py`):** two diffuse, all-crust stars in the check list (h_c = 1.003 and 1.0251) are larger than 1000 km, the solver's integration limit. They stopped before their surfaces, where the residual equals the missing pressure term. With the limit raised, the worst residual is 5×10⁻¹¹. No compact star is affected.
- **K66b PASSES:** C agrees with Run 65's to 5×10⁻¹⁰.
- **K66c PASSES:** the passive mass, computed by varying the background at fixed baryon number and without the formula, agrees with Δ_formula to ≤ 2×10⁻⁵ (threshold 10⁻³) at ε = 10⁻³ and 10⁻² for all three.
- **K66d PASSES:** C(ε), extrapolated to ε = 0, matches Run 65's C to ≤ 4×10⁻⁵ (threshold 10⁻³).
- **K66e PASSES:** β − 1 = −ε/(2(1 + ε)) to 0.1%.

**Reported.**
1. **The bound, re-quoted** (Voisin et al. 2025, 95%: |Δ| < 2.3×10⁻⁶ with red timing noise, < 1.5×10⁻⁶ with a circum-ternary planet):
$$
\frac{P_\infty}{p_s}\gtrsim1.63\text{–}1.92\times10^5\ \ (\text{red noise}),\qquad 2.50\text{–}2.95\times10^5\ \ (\text{planet}),
$$
   from MPA1 to APR4. Under option 1 (Run 57) it was 1.7–2.1×10⁵. The formula is now derived under option 3, not assumed.
2. **β.** In vacuum (γ̃, φ) is Schwarzschild's whatever the medium, and N = (1 + ε)N_GR − ε. So γ = 1 and
$$
\beta-1=-\frac{g_{\rm bg}}{2(1+g_{\rm bg})},
$$
   the same as under option 1, because γ̃ departs from flat only at O(M²/r²). With the exact medium's g_bg = (p_s − b)/P₀ (Run 55), this gives −0.94×10⁻⁴ at p_s = 16, P₀/p_s = 4096, against Run 25's measured −1.06 ± 0.06×10⁻⁴ (its own theory: −0.98). At the bound above, |β − 1| ≲ 3×10⁻⁶.
3. **Active = passive.** The far-field mass F/(1 + g_bg), read from the field's flux at the surface, equals the passive mass's formula to ≤ 8×10⁻¹⁰.

![Runs 66–67](figures/66_67.png)

**What the check added.**
1. **The reduction is confirmed by hand.** For a static metric R_tt = N D²N and R_ij = ³R_ij − D_iD_jN/N; a perfect fluid gives R_tt = 4π(e + 3p)N² and R_ij = 4π(e − p)g_ij. With g = e^{2U}γ̃ and N = e^{−U}, D²N = −e^{−2U}NΔ̃U, and the spatial Ricci becomes R̃_ij − 2∂_iU∂_jU − Δ̃U γ̃_ij. That gives Run 66's two equations exactly. This is the standard static reduction (Stephani et al., *Exact Solutions*, ch. 18, for vacuum; the perfect-fluid uniqueness proofs, e.g. Beig & Simon 1992, use the same rescaled metric; the agent cited both from memory).
2. **The energy and the formula are confirmed.**
   - Varying the functional at fixed baryon number gives the field equation, γ̃'s Einstein equation and hN = const; on shell it is the Komar integral.
   - No boundary term is needed: γ̃ is flat to O(1/ρ²).
   - Hellmann–Feynman and G_eff ∝ (1 + g_bg)² are as in Run 52.
   - With its own solver and equation-of-state code (SLy, 1.438 M☉) the agent found Δ_HF = 4.2806×10⁻⁴ against the formula's 4.2804×10⁻⁴ at ε = 10⁻³, and C = 0.42848 and 0.45823 at ε = 10⁻³ and 10⁻² (Run 66: 0.42845, 0.45822). The small differences come from its slightly different constants.
3. **K66a's diagnosis is confirmed.** The two stars are on the white-dwarf branch and reach their surfaces at 1482 and 2604 km. The 1000 km cut stopped them inside matter, where the residual is 8πpa²/N² (8.7×10⁻⁸ and 1.2×10⁻⁷). With the limit raised they give 10⁻¹⁵ and 2×10⁻¹⁴.
4. **Its own Run 65 costs are withdrawn.** Cost (i) was tied to isotropic coordinates. Its inference behind cost (ii), that the clock would have to become linear in P, was wrong: the exponential clock with U harmonic on γ̃ is exactly GR.
5. **What remains is larger than "a curved lattice".**
   - γ̃ carries GR's whole spatial-geometry sector, with its own action term (−R̃/16π). The field's self-interaction moves from U's source into the medium's geometry.
   - Clock universality and p_s's role on a curved γ̃ are plausible, by locality, but not shown: the engine was never run there.
6. **A choice the run made, which sets β.** For ε > 0, Run 66 lets the medium's own field φ curve γ̃ (the stress of its action, the variational completion of rule V). That gives β − 1 = −ε/(2(1 + ε)) and Δ = εC/(1 + ε). Letting U's stress curve γ̃ instead gives β = 1 exactly. It is recorded as a choice.
7. **"The vacuum draws nothing" is not distinctive under option 3.** GR without a cosmological constant also has Δ̃U = 0 in vacuum. ED's distinct claim is that the quantum vacuum's energy does not draw, which needs its own argument.

**Reading.**
1. **Option 3 is ED's own statics with one change: the medium's space is curved by stress.** ED's field equation, its exponential clock, the vacuum that draws nothing and the pattern rule all hold to all orders, on γ̃. ED's original rule was that γ̃ is flat. GR says the field's tension and matter's pressure curve it.
2. **The two costs recorded with Run 65 are withdrawn.**
   - Ruling 2 holds to all orders on γ̃.
   - The engine's medium carries option 3 as built (logarithmic outflow, exponential clock, the crossover p_s). It needs only to hop on γ̃ instead of a flat lattice (§9zzo).
3. **The strong-equivalence-principle prediction stands, now derived under option 3:** Δ = εC/(1 + ε) with C = 0.37–0.44 for the pulsar, and P∞/p_s ≳ 1.6–1.9×10⁵ (2.5–2.9×10⁵ with the planet model). Its sign (Δ > 0), growth with compactness and non-additivity carry over.
4. **What option 3 still costs:** the medium's space becomes dynamical, curved by stress. That is GR's whole spatial-geometry sector, carried by the medium's lattice; the engine has none, and building it is the open task (§9zzo). Whether φ's or U's stress curves it is a choice (point 6 above); Run 66 took φ's, the variational one.
