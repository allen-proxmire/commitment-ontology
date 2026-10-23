## Run 50: a star in exact hydrostatic balance — does a quantum raise its far field by exactly ħω?

*20 October 2026. Registered and hashed with every imported module before the run (`firstlaw/PREREG_50.md`, 07:43 UTC; the main run started seconds later). Disclosures:*
- *One code check ran before registering, at h = 1, which is not a registered grid. Its numbers are in the registration (`check50.json`, hashed).*
- *Run 49's check motivated the run.*
- *The radius scans (`posthoc50.py`; the checker's h = ⅕ scan in `check5051/`) are post hoc, made after K50b came out undecided.*
- *The reported extras did not finish (below).*
- *An independent agent checked the derivation, and its corrections are included.*

**Question.** With the body model of Runs 42–46c, a bound pattern's pull at neutron-star strength was 4% short of its energy. That model had three parts: a stress sized by the virial with the rest draw as weight, a proper-size rule, and a fixed homologous shape. Post hoc, Run 49 traced most of the 4% to the stress weight.

In GR, adding a quantum of Killing energy ħω to a static star raises its mass by exactly ħω (the first law). Here a star is built in exact point-by-point hydrostatic balance, with no stress rule, no proper-size rule and no assumed shape, and the same question is asked.

**The claim (registered; the check confirms the signs, factors and normalisation).** Take an exactly scale-free medium (N = e^{−U}, U = (6/c) G∗d_total, with G the inverse of the lattice Laplacian). Model the matter as a polytrope, p = Kn^Γ, with n = νN³ and √γ = N⁻³.

**(i) The engine's statics, with this matter, come from one action.**
$$
\mathcal L=-\frac{c}{12}\sum_{\rm links}(\Delta U)^2-k_0\sum\nu N\,(1+\epsilon)+\kappa\sum\Big[\omega^2N^{-4}|\psi|^2-|\nabla\psi|^2-m^2N^{-2}|\psi|^2\Big]
$$
- **Varying U gives the field law.** The draws come out as follows:
  - matter: k₀νN(1 + ε + 3p/n), Tolman's (ρ + 3p)N√γ;
  - the pattern: its Tolman/Komar draw, κ(4ω²N⁻⁴ − 2m²N⁻²)|ψ|².
- **Varying ν at fixed count gives hydrostatic balance:**
$$
N\,h(n)=\tilde\mu,\qquad h=1+\epsilon+p/n ,
$$
  which is ∂p = −(ρ + p)∂ ln N.
- **Varying ψ gives the full pattern rule.**

**(ii) Discrete first law.** dE/dκ = ω at fixed count and entropy, where
$$
E=W_f+k_0\sum\nu N(1+\epsilon)+\kappa\omega,\qquad W_f=\tfrac12\sum U\,d_{\rm total}.
$$

**(iii) Virial identity (continuum).** Stationarity under dilation gives
$$
W_f=3\!\int\!pN\sqrt\gamma+2\kappa\!\int\!|\nabla\psi|^2,
$$
so the far-field mass D equals E.

**(iv) Far-field first law.** dD/dκ → ω as h → 0. The check adds the conditions: on any smooth equilibrium branch that exists, with the box growing.

**The star.** Γ = 2, calibrated at h = ½ to U_self = 0.2178 and a surface radius of 4.0 (base units). The same physical star is used at h = ⅓, ¼, ⅕ (N_b ∝ 1/h, K ∝ h^{−2}). The pattern is as in Run 48.

**Results** (Γ = 2, U ≈ 0.215–0.218).

| h | U_self | b | discrete first law, ΔE/κω̄ − 1 | far-field miss, (ΔD/κω̄ − 1)/b | lattice virial defect (D − E)/D |
|---|---|---|---|---|---|
| ½ | 0.2178 | 0.202 | +7.9×10⁻⁹ | −0.006 | 6.7×10⁻⁴ |
| ⅓ | 0.2158 | 0.199 | +7.7×10⁻⁹ | −0.028 | 3.1×10⁻⁴ |
| ¼ | 0.2150 | 0.199 | +4.1×10⁻⁹ | −0.002 | 1.7×10⁻⁴ |
| ⅕ | 0.2147 | 0.198 | +7.4×10⁻⁹ | +0.015 | 1.1×10⁻⁴ |
| *for comparison: the old body model (Run 48), h = ½* | 0.2179 | 0.202 | — | *−0.196* | — |

**Verdicts, as registered.**
- **K50a passes.** The discrete first law holds at every grid: 4–8×10⁻⁹ at the registered points and ≤ 5×10⁻⁸ across all scan points, the floor set by the solver tolerance.
  - The check confirmed this is a real test. Altering the matter draw's 3p/n to 2p/n breaks it by 2×10⁻².
  - But the first-order cancellation holds for any fixed source. Replacing the pattern's Komar draw with another draw moves the residual only to 3×10⁻⁶. So the registered 10⁻⁶ threshold barely tests the pattern's draw; the achieved 10⁻⁸ does.
- **K50b: undecided.** The registered smooth fits give c₀ = +0.044 (two finest) and +0.050 (three finest). Both are under the 0.05 falsification line and above the 0.02 pass line.
  - The four misses oscillate rather than converge smoothly.
  - D − E itself falls as h², but its change when the pattern is added carries a surface-cell term that oscillates with the star's radius in cells. So smooth power-law fits were the wrong tool from the start, and the registration should have said so.
- **K50c (reported).** The lattice virial defect falls as h², with (D − E)/D·h⁻² = 2.70, 2.79, 2.68, 2.66 ×10⁻³.
- **The star's own fall at h = ½** is +3.8×10⁻³. By Run 48's identity it is the grid derivative of the star's energy, but it was computed at one grid only and not shown to converge.
- **The extras did not finish.**
  - The Γ = 3 calibration made no progress in 45 CPU-minutes and was stopped, so the weak-field case never ran.
  - The calibration's starting guess had a sign error (−0.5 where R ∝ K^{+½} implies +0.5), harmless for Γ = 2.
  - The check also found that a softer Γ = 1.5 star has no equilibrium near U ≈ 0.22 on this lattice. So whether a Γ = 3 equilibrium exists there is unverified.

**Post hoc: the scatter is the star's surface on the lattice.**
- At fixed h, K was varied by ±2–6%. That moves the surface across about one cell while the star stays the same.
- The miss swings with the exact set of surface cells, a 3D lattice effect.

| h | points | mean miss | spread (sd) | standard error |
|---|---|---|---|---|
| ⅓ | 7 | +0.026 | 0.037 | 0.014 |
| ¼ | 7 | +0.017 | 0.015 | 0.006 |
| ⅕ (the checker's scan plus the registered point) | 9 | +0.010 | 0.010 | 0.003 |

- **The spread and the mean both shrink with the grid.**
  - Before h = ⅕ was run, c₀ = 0 + ah² predicted +0.012 there, and a constant offset predicted +0.018. The measured +0.010 favours zero.
  - Fits over the three means give c₀ = +0.000 ± 0.009 b (c₀ + ah²), −0.015 ± 0.019 (c₀ + ah) and +0.005 ± 0.006 (c₀ + ah³).
  - A constant +0.012 ± 0.003 still has χ² = 2.1 for 2 degrees of freedom, so it is not excluded.
  - The scan points are samples of a quasi-periodic function, not independent draws, so the standard errors are approximate.
- **Post hoc, c₀ lies between about −0.015 and +0.012 b across fit forms (≲ 0.3% of κω), against −0.20 b with the old body model.** A residual of +0.02 b is disfavoured at about 2σ; +0.01 b is not excluded.

![Runs 50 and 51](figures/50_51.png)

**Reading.**
1. **With matter in exact hydrostatic balance and a scale-free medium, the engine has an energy principle, and its discrete first law holds (K50a).**
   - The field law sourced by Tolman draws, the full pattern rule, and matter whose draw includes its internal energy and pressure are the Euler–Lagrange equations of one action.
   - The new ingredient is the matter rule, N h = μ̃. It replaces the old stress and proper-size rules.
   - In CO's own medium, which is not exactly scale-free, the engine's draw lacks a factor (1 + g), g = c d ln R/dz − 1. So it is not variational at order Δg, the same quantity Run 51 measures.
2. **The far field obeys the same first law as GR to within the lattice noise:** a quantum raises it by ħω to ≲ 0.3% of κω (post hoc). As registered, K50b is undecided.
   - Analytically, (iii) makes it exact in the continuum: the far-field mass equals the action's energy, as Komar = ADM does in GR.
   - **So the 4% "active-mass deficit" was the old body model.** Run 49's post hoc analysis points mainly at its stress weight.
3. **What this does not imply.** This is the first law of the engine's own action, dE = ω dQ + μ̃ dN at fixed entropy, which has GR's form. It does not give:
   - GR's mass–radius relation, total binding or maximum mass;
   - the metric beyond first post-Newtonian order (the engine's is exponential);
   - anything about dynamics, radiation or inertia.

   J0737−3039B's binding energy remains a possible test of the engine's second-order field law, through a star's total binding.
4. **For Run 47:** the 4% deficit is gone in the scale-free continuum. On the grid, post hoc, any residual is ≲ 0.3% of κω.
   - The fall question is separate and stays open. That includes the ζ₂-type gap between the draw-based and frequency-based falls, and the star's own fall, which was not shown to converge.
5. **What carries over:**
   - every first-order result;
   - Runs 48 and 51 on the fall;
   - the rule correction recorded in §3: bodies are matter in hydrostatic balance.
