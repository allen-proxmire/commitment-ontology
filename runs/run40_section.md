## 9zg. Runs 40, 40b, 40c: Run 36 with a body that keeps its proper size

*19 October 2026. Allen: "do as you recommend" (step 1). Three registered runs, each hashed before it ran:*
- *Run 40, in Run 36's periodic box (`adjust/PREREG_40.md`, 12:52 UTC);*
- *Run 40b, in an unbounded medium, after an independent check found Run 40's pass depended on the body model (`adjust/free/PREREG_40b.md`, 13:06 UTC);*
- *Run 40c, the same at weak field (`adjust/free/PREREG_40c.md`, 13:15 UTC).*

*Trial runs used to choose the patterns' masses are disclosed in each registration.*

**Question.** Run 36's kill rule fired. Under the adopted rule a bound pattern's far field overshot ħω by 13%. Part of the cause was a body held on fixed places, which responds to outside wells with weight 1/(1 + U_self) instead of 1. A GR body keeps its proper size, so in lattice (isotropic) coordinates it shrinks by $e^{-U_{\rm ext}}$. Two questions follow:
- Does a body that does the same respond with weight 1?
- With such a body, and a pattern that stays off it, does the far field count ħω once, binding included?

**Setup.** Run 36's engine and rules: the A″ relaxed medium's mean field, Run 16's pattern, drawing by energy plus flux (adopted) or energy only (contrast), at test strength.
- **The body:** a smooth ball of 54 pairs, radius 3, each committed place drawing 2P/H.
  - **Held:** R = 3.
  - **Adjusting:** $R=3\,e^{-\bar U_{\rm ext}}$, with its count of committed places conserved.
  - **Self-similar:** the edge also scales with R.
- **The pattern:**
  - **xy state:** odd in x and y about the ball, so it has nodes through the ball and stays mostly off it.
  - **Ground state:** overlaps the ball.

**A body's response to an outside well.** With the self-term's scaling $s=d\ln k/d\ln R$,
$$
\frac{d\ln D}{d(-U_{\rm ext})}=\frac{1-U_{\rm self}\,s}{1+U_{\rm self}} .
$$
This is 1 when s = −1, and 1/(1 + U_self) when the body is held. The independent check found the formula good to about 2%.

| medium | body | s | response: measured (formula) |
|---|---|---|---|
| periodic box 60, p_s = 1 (Run 40, C40a registered "1 within 1%") | adjusting, fixed edge | −0.94 | **0.962** (0.970): C40a **fails** |
| | held | — | 0.544 (0.535) |
| | adjusting, self-similar (post hoc; R = 3, 6, 10) | −1.18, −1.32, −1.61 | 1.09, 1.13, 1.17 |
| **unbounded, p_s = 1 (Run 40b, C40b registered "1 within 2%")** | **adjusting, self-similar** | −1.027 | **1.008** (1.013): C40b **passes** |
| | adjusting, fixed edge | −0.81 | 0.893 (0.909) |
| | held | — | 0.518 (0.515) |
| unbounded, p_s = 64 (Run 40c) | adjusting, self-similar | — | **1.001** |
| | held | — | 0.948 (U_self = 0.055) |

**A body that keeps its proper size responds with weight 1 in an unbounded medium.** Run 40's box gave it a self-term that does not scale as 1/R (s ≠ −1): the zero-mean field adds a constant.

**The bound pattern's pull.** ΔD_total/(κω), with misses also in units of the pattern's binding b = 1 − ω/m (against N = 1 at infinity; the periodic box has no clean reference). "Counted once" is ΔD_total = κω. A miss of −2b means the binding is counted three times.

| run | body | pattern | binding b | energy + flux (adopted) | energy only |
|---|---|---|---|---|---|
| 40 (box) | adjusting, fixed edge | xy, m = 0.7 | 3.9% (box mean), 7.4% (box corner) | **0.9986: K40 passes** | 0.833 |
| 40 (box) | held | xy | | 1.094 | 0.906 |
| 40 (box) | adjusting / held | ground, m = 0.3 | | 1.086 / 1.139 | 0.816 / 0.896 |
| 40 (box, post hoc by the check) | adjusting, self-similar | xy | | 0.969 | |
| **40b (unbounded, p_s = 1)** | **adjusting, self-similar** | xy, m = 0.7 | 12.3% | **0.882 (−0.96b): K40b fails** | 0.754 (−1.99b) |
| 40b | adjusting, fixed edge | xy | 12.3% | 0.916 (−0.68b) | 0.782 (−1.77b) |
| 40b | held | xy | 12.3% | 1.030 (+0.24b) | 0.874 (−1.02b) |
| 40b | adjusting, self-similar / fixed edge / held | ground, m = 0.3 | 14.8% | 0.951 (−0.33b) / 0.978 (−0.15b) / 1.068 (+0.46b) | 0.727 / 0.758 / 0.860 |
| **40c (unbounded, p_s = 64)** | **adjusting, self-similar** | xy, m = 2.0 | 0.52% | **0.99975 (−0.05b): K40c passes** (band ±0.25b) | 0.98945 (−2.01b) |
| 40c | held | xy, m = 2.0 | 0.52% | 1.00032 (+0.06b) | 0.99002 (−1.90b) |
| 40c | adjusting, self-similar / held | xy, m = 2.5 | 0.81% | 0.99929 (−0.09b) / 1.00018 (+0.02b) | 0.98381 (−2.00b) / 0.98468 (−1.89b) |

![Run 40](figures/40_adjust.png)

**Reading** (checked by an independent agent, whose corrections are included).
1. **Run 40's pass did not survive.**
   - Its registered C40a failed (0.962). The check showed the K40 pass depended on the body model (0.969 with a self-similar ball).
   - In an unbounded medium, where the field at the pattern is about three times stronger, the case fails (40b: 0.882).
   - The box and the field strength change together between Run 40 and 40b, so 40b alone does not separate them.
2. **At weak field the adopted rules count a bound pattern's binding once.**
   - In an unbounded medium at p_s = 64, the mean potential over the pattern is 0.0105. The adopted rule misses by 0.05 of the binding (0.09 at m = 2.5).
   - Energy-only misses by two bindings (it counts the binding three times), in every body model at weak field (−1.9 to −2.0b).
   - That is GR's first-order statement, a bound system pulls by its total energy. It holds because the pattern's momentum flux draws (the Lorentz input) and the body's redshift is counted.
   - It is the small end of a second-order term, not an exact closure (item 3).
3. **At strong field it does not close.**
   - At p_s = 1 the mean potential over the pattern is about 0.24 (binding 12%). With an ideal body, the adopted rule misses by about one binding (0.882).
   - The ideal-body response holds for the pattern's own near field too (1.010 at strong field, 1.0014 at weak).
   - The miss splits into two second-order pieces:
     - the flux draws $K/\omega^2=1.50b$ where weak field gives 2b, which is −0.50b;
     - the flux draw redshifts the body by a further −0.46b.
   - Across all the self-similar cases the miss scales as about $-(8\text{–}11)\,b^2$ (with $b\approx\bar U/2$). Two of those points share a medium, which partly controls for the change of medium between 40b and 40c.
   - In GR a test body adds exactly its Killing energy to the total mass at any field strength. So −0.96b is a real departure from GR, beyond first order.
   - At strong field the body model also moves the result by about 1.2b (−0.96, −0.68, +0.24b).
   - Linking the departure to the engine's nonlinear structure (the exponential clock map; Run 16's pattern equation), and to Runs 28 and 41, is interpretation.
4. **What carries to physical scales.**
   - Ordinary matter is weak-field. Body potentials GM/Rc² are 7×10⁻¹⁰ for Earth and 2×10⁻⁶ for the Sun. Each clock's own dip is about 0.3/p_s (Run 23), about 10⁻⁶ at the adopted p_s. There, under the adopted rules, energy pulls with binding counted once.
   - This run **suggests**, from one configuration (a test pattern bound to a separate ball), that compact bodies are where it fails.
   - A body held on fixed places also under-responds by 1/(1 + U_self). That is negligible for ordinary bodies and large for compact ones. A body that keeps its proper size fixes this part (C40b).
5. **Patterns inside a body** (the ground state) were tested only in the box and at strong field. Internal binding at weak field (atoms, nuclei: patterns inside patterns) has not been run.
   - Missing internal stresses is one explanation. Two others:
     - the adopted rule's local draw density turns negative where N < ω/(√2 m);
     - the outside potential is ill-defined for a source that overlaps the body.
