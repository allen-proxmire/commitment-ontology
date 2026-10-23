## Run 17: slowing hops as well as ticks (light bending and Shapiro delay)

**Question.** Run 16's test pattern carried only the clock half of gravity: its phase slowed near matter, its hops did not. So it could not bend light. Run 9 found the other half in the continuum: possibility needs free capacity to hop as well as to tick, which takes light bending from half to the full observed value. This run puts that half into ED's engine.

**Target, fixed in advance.** A ray passing a mass is deflected by $\alpha=(1+\gamma)\,2GM/(bc^2)$, and the Shapiro delay also scales as $1+\gamma$.
- GR: γ = 1. Cassini: γ − 1 = (2.1 ± 2.3)×10⁻⁵.
- In terms of the clock rate N, the light speed is $c=N^{1+\gamma}$. Clock slowing alone gives $c=N$; GR gives $c=N^2$.

The pre-registration and its amendment are in `PREREG.md`. The amendment was written after the engine runs failed and before any pattern was evolved in an engine field.

### Part 1. The engine rule as agreed: possibility's own hops slowed by its place's clock

**The rule tried:**

$$
p_{\rm hop}(\mathbf x)=P_0\,N_a(\mathbf x)\,N_b(\mathbf x)\qquad(\text{mean }P_0N^2)
$$

- $N_{a,b}$ are the place's own counts of passing possibility over two consecutive 10-tick windows, relative to the far value.
- One factor is because hops happen on the place's ticks; the other is because a hop needs free capacity.
- $P_0$ = 0.5 leaves headroom so the chance stays below 1, and holds are rescaled to match.
- With the rule off, the code reproduces the Runs 15–16 engine bit for bit.

**Result: the medium froze.** No possibility was moving by tick 200. Diagnostic at density 8 with the ball (box-mean passing count per tick; 4.0 is a healthy medium):

| variant | tick 200 | tick 2,000 | spread of N across places |
|---|---|---|---|
| as pre-registered: N², N against the fixed far value | **0.000** | 0.000 | frozen |
| one factor of N | 3.99 | 3.71, still falling | 0.21 |
| N², N against the box-wide mean | 2.7 | 2.8 | **1.1 (clumped)** |
| no slowing (reference) | 4.00 | 4.00 | 0.18 |

**Why.** The medium's possibility *is* the clock: N is its own passing count. Put a power $g$ of N into its hop chance and, for the uniform mode, a fractional change δ in the flow comes back as $g\,\delta$ one window later.
- $g$ = 2 runs away to zero.
- $g$ = 1 is neutral and drifts.
- Normalising to the box mean removes only the uniform mode; long-wavelength modes still grow, and the medium clumps.

A linear analysis (not simulated beyond the four variants) says stability needs $g<1$. Then the medium's own propagation has speed $N^g$, so $\gamma=g-1<0$: light would bend *less* than clock slowing alone.

> **The possibility that carries the clock field cannot have its own wander timed by that field.** The engine rule is not adopted. The pre-registered engine predictions (shortage shape, hop exponent, stock pile-up) are void.

### Part 2. The same rule applied to patterns, not to the medium

The medium keeps the adopted engine's wander (Runs 15–16), and the field is the Run 16 seed-1 field (box 60). The rule moves to the pattern:

**a pattern of possibility hops on its place's ticks and needs free capacity there**, so its hop factor is $H=N^2$.

The pattern obeys the wave equation of the static field $ds^2=-N^2dt^2+S^{-2}dx^2$, in conservative form:

$$
w\,\ddot\phi=\sum_{\rm links}\kappa_{\rm link}(\phi_y-\phi_x)-m^2u\,\phi,\qquad w=\frac1{NS^3},\ \kappa=\frac NS,\ u=\frac N{S^3},\qquad c_{\rm massless}=NS
$$

Three couplings are compared in the same field:

| coupling | hop factor S | massless speed |
|---|---|---|
| **A, full rule** | N | N² |
| **B, clock only** | 1 | N |
| **C, Run 16's** | — | 1 (light does not couple) |

**Relabelling flag.** γ = 1 is put in by the pattern rule. This part checks that patterns in the engine's real field bend and are delayed as the rule predicts. It does not derive γ.

**Light.**
- **Pulses:** massless, carrier $k_0$ = 0.8, width 6, launched 22 places before the ball. They pass at $b$ = 15 and 21 on four sides, at densities 8 and 32.
- **Deflection:** the centroid's inward velocity as it crosses a plane 42 places on, with coupling C subtracted. C removes a spurious 0.0005, which is the measurement floor.
- **First-order (Born) prediction:**

$$
\alpha=\frac{1}{\cos^2(k_0/2)}\Big\langle\int\hat u_\perp\!\cdot\!\nabla\ln c\,dx\Big\rangle_{\rm beam}
$$

- **Weak-field reading (pre-registered):** the field is log-scaled, $N\to N^{1/4}$. For log-scaled fields the predicted A/B ratio is exactly 2.00.

**Weak-field results** (measured A/B ratio ÷ predicted ratio; band ±3%):

| | density 32, b = 15 | density 32, b = 21 | density 8, b = 15 | density 8, b = 21 |
|---|---|---|---|---|
| bending | 1.002–1.003 | 1.003–1.007 | 0.973–0.988 | 0.986, **1.084, 1.085, 1.181** |
| Shapiro delay | 0.992–1.014 | **0.935, 0.938**, 0.980, 0.987 | **1.101–1.108** | 1.016, 1.028, **1.073, 1.097** |

- **Direction:** every deflection is toward the matter, 64 of 64.
- **The ratio itself:** the measured A/B bending ratio averages **2.010** at density 32 and 2.067 at density 8.

**Full field strength (reported, not judged).** The A/B bending ratio is 1.92–2.31, against a first-order 2.00–2.02. Deflections reach 0.22 rad at density 8, b = 15. The A/B delay ratio grows to 2.2–3.2, strongly nonlinear in this strong field.

**Slow fall (pre-registered F1′, failed as written).**
- The prediction weighted the second-order factor $H^2$ by the pattern's charge, which gave 0.76 and 0.92.
- **Measured** $a_A/a_C$: 0.89–0.93 at 12 out and 0.95–0.99 at 18 out.
- A synthetic-field check run afterwards shows the charge weighting was the mistake. The geodesic factor $N^4$ *at the pattern's centre* is what the full rule produces: 91–96% of the predicted second-order effect, in a clean field.
- In the engine's periodic, rippled box the absolute normalisation of N, which this factor needs, is uncertain by as much as the effect. So the second-order fall is not judged here.
- At first order the fall is unchanged.

### Against the pre-registration

| Prediction | Expected | Measured | |
|---|---|---|---|
| E1–E3 (engine with slowed hops) | — | the medium freezes | **void: the rule is unstable** |
| L1′ bending ratio, weak field | Born ± 3% | density 32: all 8 within 0.7%; density 8: b = 15 within 2.7%, b = 21 three of four off by 8–18% | **pass at density 32 and near beams; fail at density 8, far beams** |
| S1′ delay ratio, weak field | Born ± 3% | density 32: 6 of 8 (the 2 misses have the smallest delays); density 8: 2 of 8 | **fail at density 8** |
| L2 coupling C | no coupling | zero, apart from the 0.0005 floor | pass |
| F1′ second-order fall | charge-weighted $H^2$ ± 2% | formula wrong (synthetic check) | **fail as written** |

The density-8 misses are not explained by sub-wavelength counting noise: recomputing the predictions from a smoothed field changes nothing. The likeliest cause, not established, is the measurement itself. The full rule's charge weight, $N^{-4}$, makes the charge centroid a poor stand-in for the ray where signals are small and the medium's ripples are largest.

### Reading

**1. The main result is a constraint on ED.**
- The medium of possibility, which *is* the clock, cannot have its own wander timed by that clock: the feedback freezes, drains or clumps it.
- So the slowing of hops near matter cannot belong to possibility at large. It has to belong to **patterns riding on the medium**: light, matter waves. This matches GR, where light moves through the metric without making it.
- In ED terms: possibility at large keeps no time and is the engine's update; a pattern of possibility hops on its places' ticks and needs free capacity there.

**2. With that pattern rule, light bends toward matter about twice as much as clock slowing alone** (2.010 ± 0.003 at density 32), and the Shapiro delay also doubles where it can be measured cleanly. This holds in the engine's real field, but it is a consistency check: γ = 1 was put in by the two factors.

**3. The tests are not clean everywhere.**
- At density 8 the far beams and the delays miss by up to 18%. The cause is not established.
- The second-order fall is not judged.

**4. What the engine decision now is.**
- No engine rule changed: the medium is as in Runs 15–16, and the base hop chance stays 0.99.
- The proposal is the **pattern rule**. It is ED's statement of why light bends with γ = 1, and adopting it needs a ruling.
- It also leaves the old "nothing falls when stepping by paying" result standing for committed matter. The stock pile-up that might have reversed it does not happen, because the medium is unchanged.

![Run 17](figures/17_hops.png)

---

