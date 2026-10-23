## Run 19: knots that dig their own clock wells (active mass, and how ED's engine combines wells)

**Question.** In Runs 16–18 every body fell in a clock well dug by ED's benchmark ball. Here a knot digs its own.
- **Committed side:** its places hold engine commitments where its cost lives, drawing possibility from the one budget.
- **Uncommitted side:** its orientation field moves as in Run 18, falling with inertia, with twist charged on every loop.

This follows the rulings of 6 October (phase memory on uncommitted channels, at the local clock rate) and avoids repeating Attempt D, whose commitment-only loops can only drift, and only with a steering constant of ours (D-O8, D-O15, `Engine_Motion.md`). Plan approved 17 October: the two-layer knot, both matter arms, and R1.

**R1 does not act in this engine.** R1 (adopted 11 October) says a failed try takes no time. Nothing here proposes: the vacuum never commits (Run 14), and matter's reserved pairs renew at once if both places can pay. So the engine is bit-identical with R1 on or off, and Runs 14–18 stand under R1. Checked: the Run 19 control reproduces Run 16's engine bit for bit.

### Model

**Engine:** Runs 14–16's adopted rules, box 60, density 8, 9,000 ticks, read over the last 6,000. Clock rate $N(\mathbf x)$ = time-averaged passing count ÷ the control's mean (the flow rule: a hold ends when $H_1$ = 79 units have passed its places).

**The knots:** Run 12's relaxed Q = 1, 2, 3 (h = 0.2, one knot unit = one engine place), with cost per place $e_p$:

| | Q = 1 | Q = 2 | Q = 3 |
|---|---|---|---|
| E | 533.8 | 877.1 | 1227.2 |
| ÷ E(Q = 1) | 1 | 1.643 | 2.299 |

**How many commitments a knot holds (two arms):**
- **Arm E, cost-paid (an added rule, flagged).** $\mathrm{round}(\lambda E/2)$ commitments spread over the knot's links with weight $e_p+e_q$, so place p holds about $\lambda e_p$ of them. λ = 0.2023 per unit of cost, fixed so that Q = 1 holds 54, as ED's ball does. That gives 54 / 89 / 124 commitments, up to 6 on one place (an addition, flagged).
- **Arm P, ED's current rule.** One reserved commitment per place with $e_p\ge\tau$, paired at random as ED pairs its ball. τ = 0.371 (ours) is fixed so that Q = 1 has 108 matter places. That gives 51 / 74 / 101 pairs.

**Active mass.** A body's well about its centre, $\delta(r)=1-\langle N\rangle_r/\langle N_{\rm ctrl}\rangle_r$ for r = 7–20, fitted to ED's ball's well: $A=\sum\delta\,t/\sum t^2$. Its draw is the possibility it spends per tick.

### S1: does a knot's well scale with its energy? (pre-registered, `PREREG_19_S1.md`)

| body | draw per tick | A (in ED balls) | A ÷ draw (×100) | holds per commitment per tick | clock rate over its cost |
|---|---|---|---|---|---|
| ED's ball | 15.13 / 15.26 | 1.00 | 6.58 | 0.140 | 0.70 (over its places) |
| Q1 E | 12.34 | 0.825 | 6.69 | 0.114 | 0.594 |
| Q2 E | 17.33 | 1.180 | 6.81 | 0.097 | 0.534 |
| Q3 E | 21.86 | 1.460 | 6.68 | 0.088 | 0.495 |
| Q1 P | 14.41 | 0.960 | 6.66 | 0.141 | 0.670 |
| Q2 P | 19.48 | 1.329 | 6.82 | 0.132 | 0.618 |
| Q3 P | 24.80 | 1.666 | 6.72 | 0.123 | 0.571 |

(Seed means; seeds agree to 0.2% in draw and 1–3% in A.)

| Prediction | Expected | Measured | |
|---|---|---|---|
| P0: A ÷ draw the same for every body | within 5% | 14 bodies within 3.0% | **pass** |
| P1: arm E, $A_{Q2}/A_{Q1}$, $A_{Q3}/A_{Q1}$ = energy ratios | 1.643 ± 0.08, 2.299 ± 0.12 | 1.429 ± 0.003, 1.770 ± 0.013 | **fail** |
| P2: arm P, ratios = pair ratios | 1.45 ± 0.08, 1.98 ± 0.10 | 1.384 ± 0.007, 1.735 ± 0.003 | **pass for Q2, fail for Q3** |

**Why both arms fall short: a body's own well slows its own commitments.**
- These bodies dig deep wells. Weighted by where their cost sits, their own clocks run at 0.50–0.67 of the far rate (ED's ball: 0.70 over its places).
- A commitment completes as possibility passes its places, so it completes more slowly inside its own body's well. Commitments stacked on one place also share that place's possibility.
- So a bigger body draws less per unit of cost. Draw per unit energy, ÷ Q = 1:
  - arm E: 0.855 (Q2), 0.771 (Q3)
  - arm P: 0.822, 0.749
- Because P0 holds, the well follows the draw exactly. **The engine's active mass is the redshifted draw:**

$$
D=\sum_{\rm commitments}\frac{\text{passing at its places}}{H_1}\;\approx\;\frac{2\,\lambda_0}{H_1}\sum_p n_p\,N_p
$$

**What the registered target got wrong.** "Active mass ∝ E" ignores binding. In standard physics a bound body's mass includes its negative binding energy, so it is *expected* to fall below the sum of its parts. What the equivalence principle needs is that active mass, passive mass and inertia are all reduced alike: the strong equivalence principle (SEP). P1's failure is therefore not by itself a violation. It is a binding effect of the size of the body's own well, and these bodies are strong-field (own clock halved). Real matter's own wells are ~10⁻⁹ deep.

### The finding that decides the next question: the engine's well is linear in its source

Outside matter, possibility only wanders and returns to random places, which is linear. So the shortage is a sum over sources with one Green's function G, and under the flow rule the clock rate *is* the passing count:

$$
\delta(\mathbf x)=\sum_bD_b\,G(\mathbf x-\mathbf x_b),\qquad N=1-\delta\equiv1-U\quad\text{exactly, outside matter}
$$

**Checked on S1's 14 bodies (after S1, before S2a was registered).** Each body's shell profile at r = 5–8 was scaled two ways and its deviation from the common shape regressed on source strength. An exactly linear engine predicts no trend in the linear form and about +0.035 per 10 units of draw in the log form; an exponential engine predicts the reverse.

| scaling | trend of shape with draw (per 10 units) | scatter |
|---|---|---|
| linear, $(1-N)/D$ | +0.017 ± 0.008 | 1.1% |
| logarithmic, $-\ln N/D$ | **+0.057 ± 0.008** | 1.1% |

The data favour linear. The exponential form ($\ln N$ adding, which gives β = 1) misses by 0.052, about 6.5 standard errors. The small residual trend in the linear form (2σ) is partly the ball's different shape. The strongest and weakest knots alone agree to 0.7–1.3% at r = 5–8 (panel b).

**What β that is.** With the clock as the time part of the metric and the pattern rule (Run 17) for the space part, $ds^2=-N^2dt^2+N^{-2}d\mathbf x^2$:

$$
g_{00}=-(1-U)^2=-1+2U-U^2\;\Rightarrow\;\beta=\tfrac12,\qquad g_{ij}=(1-U)^{-2}\delta_{ij}=(1+2U+\dots)\delta_{ij}\;\Rightarrow\;\gamma=1
$$

- **Mercury.** The perihelion advance per orbit is $\frac{2+2\gamma-\beta}{3}\cdot\frac{6\pi GM}{a(1-e^2)c^2}$, so this metric gives **7/6 of GR: 50.1″ per century against the observed 42.98″.** This is Run 10's additive budget with free capacity. Run 10 reached 42.97″ only by *assuming* the multiplicative budget ($c=c_0e^{-U}$), which the engine as adopted does not produce.
- **Nordtvedt.** $\eta=4\beta-\gamma-3=-2$, against σ(η) = 4.4×10⁻⁴ from lunar laser ranging (Williams et al. 2009). The formula is for theories without preferred-frame terms; ED's engine has a preferred frame, so other terms could add.
- **Both excluded.** The inference assumes the clock rate is the full time part of the metric and that orbits follow that metric, as Runs 16–17's patterns do. A direct orbit run on the engine field has not been done.

### S2a: two wells in one box (pre-registered, `PREREG_19_S2a.md`)

ED's ball at (30, 30, 30) and the Q1 arm-E knot 9.5 places away, seeds 1 and 2, each against its solo runs.

| Prediction | Expected | Measured | |
|---|---|---|---|
| Q1: knot's draw ÷ solo = ball's clock at the knot's commitments | 0.944 / 0.943 (± 0.01) | 0.943 / 0.946 | **pass** |
| Q1: ball's draw ÷ solo = knot's clock at the ball's places | 0.957 / 0.954 (± 0.01) | 0.955 / 0.959 | **pass** |
| Q2: field outside matter = linear sum with those draws, to 1% of δ | mean residual within 1% | +2.2%, +1.5% (seed 1); −0.2%, +0.8% (seed 2) | **mixed: seed 2 passes, seed 1 off by 0.5–1.2 points** |

- **Sources redshift each other:** each body's commitments complete more slowly in the other's well, exactly as predicted, against 1.00 for a plain additive engine.
- **The field is the linear sum of the redshifted sources.** Mean residual about each body over shells 6–20, from seeds 1 and 2:
  - linear sum with redshifted draws: +1.1% (four cases, ± 0.5%)
  - multiplicative composition, $\delta_b+\delta_k-\delta_b\delta_k$: −2.6%
  - plain additive: −3.9%
- The registered 1% tolerance was tighter than the noise between independent runs (shell rms 1–3%).

### Reading

**1. In ED's engine a body's active mass is its redshifted draw.** A bigger or denser body sits deeper in its own well, completes its commitments more slowly, and digs a well smaller than its cost. That is a binding effect, and by itself it is not a violation. Whether ED keeps the strong equivalence principle depends on its passive mass and inertia getting the same factor, and that depends on how its wells combine (point 2).

**2. The engine's wells are linear in their sources (β = ½), not exponential (β = 1).** With the adopted pattern rule (γ = 1), the engine therefore predicts Mercury's perihelion at 50.1″ per century and η = −2. **Both are excluded.**
- This is the parked "perihelion on the event layer", now answered by inference: Run 10's multiplicative budget is not what the adopted engine does.
- It follows from two adopted rules together: the vacuum never commits (so outside matter possibility only wanders, linearly), and the flow clock rule (so the clock rate is the passing count, linearly).

**3. What would fix it, stated, not chosen.** Clocks would have to slow as $N=e^{-\delta}$ rather than $1-\delta$, or the shortage would have to obey an equation linear in $\ln N$. For example, a hold could end after possibility equal to a fixed *fraction of what remains* has passed. That would be a change to the clock rule adopted on 16 October, and it would need Runs 15–18 re-checked. **Needs a ruling.**

**4. Not run, and why.** Taking Run 18's equations with S1's self-well, a knot in its own well would fall at 0.58 of a test body if wells add, or 0.37 if they multiply, and at 0.88 with the self-well 0.3× as deep. But Run 18's knot uses clock-only coupling (γ = 0), not the adopted pattern rule. So that SEP test would mostly measure the missing γ, and it was set aside in favour of measuring β directly.

**5. Flags.**
- Arm E's cost-paid rule and its stacked commitments are ours.
- The β inference identifies the clock rate with the metric's lapse and assumes geodesic orbits.
- These bodies are strong-field; the β result does not depend on that.

![Run 19](figures/19_ownwell.png)
