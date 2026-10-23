## Run 15: the clock rule (on CO's own event-layer engine)

**Question.** In Run 14, CO's clocks stopped noticing a shortage wherever possibility was plentiful: at 8 units per place, probe rates read 0.2000 with and without matter. Real clocks show the full gravitational redshift in nearly empty space. This run asks which matter rule gives a clock that does that.

**Target, fixed in advance (standard physics).** In a weak field, a clock runs at

$$
\frac{\nu(\mathbf x)}{\nu_\infty}=1+\frac{U(\mathbf x)}{c^2}
$$

This has three measured properties:
- **Linear in the potential:** Pound–Rebka 1%; Gravity Probe A about 10⁻⁴; the eccentric Galileo satellites 2.5×10⁻⁵ (Delva et al. 2018).
- **The same for every kind of clock:** local position invariance (Will 2014, §2.4).
- **Present where clocks are alone in nearly empty space:** GPS, about 38 µs/day net.

The pre-registration (`PREREG.md` in the bundle) was written before any run of the new rule.

### Why the engine's clock saturates

In CO's engine, matter is a reserved pair. Its commitment spends one unit from each place, **holds for ħ = 5 global ticks**, and renews at once if both places hold a unit. A clock is its count of completed commitments. So its rate is

$$
\text{rate}=\frac{1}{\hbar+\bar w},\qquad \bar w=\text{mean wait for both places to hold a unit}
$$

Only the wait $\bar w$ can respond to a shortage. Where places are rich, $\bar w\to0$ and the rate sits at $1/\hbar$ whatever the shortage. **The global tick is acting as a clock outside the committed world.**

### The flow rule

A commitment holds while a fixed number $H$ of possibility units **pass into** its two places; it does not hold for a fixed number of ticks. When the count is reached the commitment completes (one count of the clock), and the pair renews at once if both places can pay, as before.

**Possibility keeps no time. The committed world counts what passes.**

The number of units passing into a place each tick is $\text{PHOP}\times\bar P_{\rm nb}$, where $\bar P_{\rm nb}$ is the mean possibility of the place's neighbours. So when nothing waits to pay:

$$
\text{rate}_F=\frac{\text{PHOP}\,\big(\bar P_{\rm nb}(a)+\bar P_{\rm nb}(b)\big)}{H}
\quad\Rightarrow\quad
1-\frac{\text{rate}_F(\mathbf x)}{\text{rate}_F(\infty)}=\frac{\Delta\mu(\mathbf x)}{\mu_\infty}\equiv\epsilon(\mathbf x)
$$

The far-away possibility $\mu_\infty$ plays the role of the potential's zero, and the fractional shortage $\epsilon$ plays $-U/c^2$.

- $H$ is fixed per run so that a hold lasts about ħ ticks far from matter: $H_1=\mathrm{round}(2\hbar\,\text{PHOP}\,d)$, which gives 10, 20, 79 and 317 at $d$ = 1, 2, 8, 32.
- Units passing in on the completing tick carry over, which removes the tick's granularity.
- The same rule applies to the ball and to every probe, because clocks are matter.

**What is built in and what is tested.** The proportionality is built into the rule. The run tests whether the engine's other rules spoil it:
- paying a unit at each place to renew
- each clock depleting its own places
- matter's own draw changing under the rule
- the fluctuations of discrete possibility

It also tests whether the shortage stays unscreened.

### Method

- **Engine:** CO's `run_event_layer.py`, imported unmodified.
- **Vacuum:** arm V of Run 14, where the vacuum never commits.
- **Box and settings:** 30³, periodic, PHOP = 0.99. Densities 1, 2, 8 and 32 units per place; seeds 1 and 2; 12,000 ticks, read over the last 9,000.
- **Matter:** the published ball (radius 3, 54 reserved pairs), with a matched control for every run (same seed, same probes, no ball).
- **Probe clocks:** 96 reserved pairs, 12 per shell at shells 5–12, at least 2.5 places apart.
  - Two designs alternate: a **short hold** (ħ ticks under the old rule, $H_1$ under the flow rule) and a **long hold** (2ħ, or $2H_1$).
  - The layout is identical in every run.
- **Rules compared:** the old rule (CO's engine, hold in global ticks) and the flow rule. Each applies to the ball and to the probes alike.
- **Readings:**
  - Fractional shortage $\epsilon(r)=\Delta\mu/\mu_{\rm ctrl}$, averaged over each shell (excluding the ball's and probes' places).
  - Probe slowing $1-\text{rate}_{\rm ball}/\text{rate}_{\rm ctrl}$.
  - **Response** $\kappa$: the least-squares slope through the origin of slowing against $\epsilon$ over shells 5–10, by design. Errors are bootstrap over probes.
  - **Universality ratio** $U_{21}=\kappa_{\rm long}/\kappa_{\rm short}$.
  - **Drift** of κ from shell 5 to shell 10, as a fraction of its mean.
  - The unscreened shortage fit of Run 14.
- **Code check:** the old rule with Run 14's probe layout reproduces Run 14's arm V **bit for bit**, both the possibility field and every count, over 800 ticks at three settings.

### Results

**Pooled response, shells 5–10** (both seeds; ± bootstrap standard error):

| rule | density | mean possibility (control) | κ, short hold | κ, long hold | long ÷ short | time waiting to pay (short / long) | ball's draw per tick | unscreened misfit |
|---|---|---|---|---|---|---|---|---|
| flow | 1 | 0.82 | 1.249 ± 0.022 | 1.122 ± 0.028 | 0.898 ± 0.027 | 20% / 11% | 3.40 | 2.4% |
| flow | 2 | 1.76 | 1.098 ± 0.016 | 1.091 ± 0.016 | 0.993 ± 0.020 | 4.5% / 2.2% | 6.77 | 1.3% |
| flow | **8** | 7.70 | **1.030 ± 0.014** | **1.026 ± 0.020** | **0.996 ± 0.023** | 0 / 0 | 14.89 | 0.6% |
| flow | **32** | 31.69 | **1.040 ± 0.019** | **1.022 ± 0.023** | **0.983 ± 0.028** | 0 / 0 | 19.58 | 0.8% |
| old | 1 | 0.79 | 0.948 ± 0.022 | 0.580 ± 0.022 | 0.611 ± 0.027 | 37% / 22% | 3.51 | 1.7% |
| old | 2 | 1.72 | 0.387 ± 0.011 | 0.205 ± 0.007 | 0.530 ± 0.023 | 10% / 5% | 8.28 | 0.4% |
| old | 8 | 7.69 | 0.005 ± 0.001 | 0.000 | — | 0 / 0 | 21.69 | 0.2% |
| old | 32 | 31.68 | 0.000 | 0.000 | — | 0 / 0 | 21.80 | 0.4% |

**Against the clock's own neighbourhood.** The places next to each probe are where its passing possibility comes from. Measured against their shortage instead of the shell's, the flow rule gives:

| density | κ, short hold | κ, long hold |
|---|---|---|
| 8 | 0.997 | 1.005 |
| 32 | 1.010 | 0.995 |
| 2 | 1.07 | 1.06 |
| 1 | 1.23 | 1.12 |

The 3–4% excess against the shell average comes from each clock depleting its own surroundings.

**Shell by shell, flow rule** (slowing %, short hold | long hold, against the shortage ε %):

| shell | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|
| density 8: ε | 9.63 | 6.56 | 4.67 | 3.21 | 2.11 | 1.26 | 0.61 | 0.09 |
| density 8: slowing | 9.49 \| 9.66 | 7.20 \| 6.31 | 4.71 \| 4.58 | 3.19 \| 3.15 | 2.11 \| 2.30 | 1.35 \| 1.48 | 0.55 \| 0.44 | −0.05 \| 0.37 |
| density 32: ε | 3.11 | 2.19 | 1.58 | 1.09 | 0.68 | 0.37 | 0.16 | 0.00 |
| density 32: slowing | 3.14 \| 3.09 | 2.25 \| 2.13 | 1.78 \| 1.65 | 1.18 \| 1.01 | 0.61 \| 0.69 | 0.26 \| 0.49 | 0.20 \| −0.06 | −0.10 \| −0.14 |

Typical errors are ±0.1–0.3% at density 8 and ±0.1% at density 32.

**Linearity** (drift of κ from shell 5 to shell 10, as a fraction of its mean):
- **Flow rule:**
  - density 8: +0.00 ± 0.06 (short), +0.08 ± 0.09 (long)
  - density 32: +0.12 ± 0.07, −0.01 ± 0.09
  - density 2: +0.12 ± 0.06, +0.02 ± 0.08
- **Old rule:**
  - density 1: −0.34 ± 0.13, −0.25 ± 0.18
  - density 2: −0.72 ± 0.10, −0.59 ± 0.17

So the old rule responds more than proportionally where the shortage is large.

**Does passing possibility alone set the rate?** The ratio rate × H ÷ (units passing in) in the controls reads:
- 1.000 at densities 8 and 32
- 0.95 / 0.98 at density 2
- 0.79 / 0.88 at density 1

That is the share of each cycle not spent waiting to pay.

### Against the pre-registration

| Prediction | Expected | Measured | |
|---|---|---|---|
| **F1** flow rule responds at any richness (densities 8, 32) | κ = 1.00 ± 0.10, both designs | 1.030, 1.026; 1.040, 1.022 | **pass** |
| **F2** universal | $U_{21}$ = 1.00 ± 0.10 at 8, 32; ± 0.15 at 2 | 0.996, 0.983; 0.993 | **pass** |
| **F3** linear (densities 8, 32) | drift within ±10% beyond error | +0.00 ± 0.06, +0.08 ± 0.09, +0.12 ± 0.07, −0.01 ± 0.09 | **pass** |
| **F4** lean-medium limit (estimate, not pass/fail) | κ ≈ 1.3 / 1.2 at density 1, ≈ 1.1 / 1.05 at density 2; universality off up to ~10% at density 1 | 1.25 / 1.12; 1.10 / 1.09; $U_{21}$ = 0.90 | as estimated |
| **F5** shortage still unscreened | misfit ≤ 5% | 0.6–2.4% | **pass** |
| **O1** old rule, rich media | \|κ\| < 0.05 | 0.005, 0.000 | **pass** (as predicted, no response) |
| **O2** old rule not universal (densities 1, 2) | $U_{21}$ < 0.8 | 0.61, 0.53 | **pass** (as predicted) |
| **O3** old rule, lean media (estimate) | κ ≈ 0.7 (density 1), ≈ 0.2 (density 2) | 0.95, 0.39 | **missed** |

**Why O3 missed.** The estimate took Run 14's shell-8 value. The pooled κ is weighted toward the inner shells, where the old rule responds more strongly (it is not linear: κ falls by 34–72% from shell 5 to shell 10). Twice as many probes also made the medium leaner: mean possibility was 0.79 against Run 14's 0.86. The miss does not touch any pass/fail call.

### Reading

**1. With the hold counted in passing possibility, CO's clocks behave like real clocks at every richness tested.**
- They slow by the fractional shortage: 1.02–1.04 against the shell average, and 1.00 against their own neighbourhood.
- Two different clocks agree to 1–2%.
- The response is linear in the shortage across shells 5–10.

**2. CO's original rule cannot do this, and not just where possibility is plentiful.**
- At densities 8 and 32 it does not respond at all.
- At densities 1 and 2 it responds, but:
  - more than proportionally (κ falls 34–72% from shell 5 to 10)
  - differently for different clocks: the long-hold clock slows only 53–61% as much as the short-hold clock at the same place
- Different atomic clocks show the same redshift, so the old rule's clock-dependent slowing would violate local position invariance at the level atomic-clock comparisons test.
- The reason is the same in every case: only the waiting responds, and how much of a cycle is waiting depends on the clock.

**3. What changes in CO's terms.** *A commitment holds for ħ ticks* becomes *a commitment holds while a fixed amount of possibility passes its places*.
- The global tick then times nothing that matter does.
- This matches the point that possibility keeps no time and the committed world counts what passes.
- **In standard terms:** a clock's rate is proportional to the local possibility, which plays $1+U/c^2$.
- **Relabelling check:** the proportionality is designed into the rule, not discovered. What the run shows is:
  - that nothing else in CO's engine spoils it where possibility is plentiful
  - that CO's original rule cannot produce it at all

**4. The lean-medium limit.** Where places are often empty (densities 1–2), waiting to pay adds to the response (κ = 1.1–1.25) and breaks universality by about 10% at density 1. A clock that has to wait to pay responds extra, and by an amount that depends on the clock. **So real clocks must never wait to pay:** the places they sit in must be rich compared with what a commitment costs.

**5. Matter slows in its own well.**
- Under the flow rule the ball's draw falls relative to the old rule:
  - by 31% at density 8 (21.7 → 14.9 per tick)
  - by 10% at density 32
- The ball's own places are short, so its holds last longer.
- The source's strength therefore depends on the potential at the source. That is a second-order effect, and it has not been compared with GR's second-order terms.

**6. The vacuum decision's gain survives.** The shortage still fits the unscreened solution, to 0.6–2.4%.

**7. Costs, if adopted:**
- One of CO's event-layer rules changes.
- Result 26's bookkeeping (clock rate = committed share ÷ (ħ − 1)) has to be re-derived. Under the flow rule, a clock's rate is passing possibility ÷ H.
- The global tick still drives possibility's wandering (PHOP per tick). It is the last background clock in the engine. Whether wandering can be made tick-free (asynchronous updates) is the next relational question.

**8. Not addressed: falling.** CO's engine still has nothing that falls (EVENT_LAYER.md: free patterns step *away* from matter). A clock rule that reads the shortage correctly is the prerequisite for testing falling with inertia, since the max-count path depends on the clock rates along it.

![Run 15](figures/15_clock_rule.png)

---

