## 9k-2. Run 18b: the tick-loop knot on the fine grid, measured properly

**Question.** In Run 18 the knot with Str also charged on loops that include a tick (reading T, adopted provisionally on 17 October) fell at 0.92–0.93 of the universal rate on the fine grid. That missed the registered 1.00 ± 0.03. Is the shortfall the lattice knot's own weight-to-inertia ratio, which should tend to 1 as the grid is refined, or something else?

The pre-registration is `PREREG_18b.md` in `matter_run.zip`. It was written after the diagnostics below and before any registered drop, and it lists everything already seen.

### What the diagnostics found first

**1. The first suspect was wrong.** The first diagnosis was that twist across a tick and twist across a relation use different lattice formulas. They don't: both build each square face from its corners in the same way. A tick is simply taken as infinitely short. The literal alternative, a tick of finite length h priced exactly like a relation, is unstable on a cubic grid at one hop per tick.

**2. Run 18's inertia estimate was too crude.** It boosted the knot with central differences. A smooth rigid boost uses the exact derivative of the knot's band-limited field, projected onto the sphere's tangent plane:

$$
\dot n=-v\,\partial_x n,\qquad M_{\rm spec}=\frac{2T(\dot n)}{v^2}
$$

The force on a smooth rigid translation is

$$
F_{\rm spec}=\sum_i\frac{\partial V_N}{\partial n_i}\cdot\partial_xn_i .
$$

Together they give the lattice knot's own fall, and the universal fall is the reference:

$$
a_{\rm lat}=N_c\,\frac{F_{\rm spec}}{M_{\rm spec}},\qquad a_{\rm univ}=N_c\,\langle\partial_uN\rangle_e
$$

| | h = 0.2 | h = 0.1 |
|---|---|---|
| $E/M_T$, central boost (Run 18) | 0.982 | 0.989 |
| $E/M_T$, smooth boost | **0.907** | **0.973** |
| $E/M_S$, central / smooth | 3.360 / 3.198 | 3.096 / 3.062 |
| $F_{\rm spec}/(E\langle\partial_xN\rangle_e)$ | 0.993 | 0.992 |

Along z (the knot's own axis) at h = 0.1, $E/M_{T,\rm spec}$ = 0.993.

**3. The fall is not steady over short windows.** At h = 0.2, even with the field switched on smoothly, the knot's local acceleration wobbles by about ±5% over several time units. Run 18's 4- and 8-unit windows could not measure it to 3%.

### Method

Run 18's model, unchanged. Three changes to the measurement and the code:
- **Smooth switch-on.** The field is switched on over $T_r$ = 4 time units, holding the clock rate at the knot's centre fixed:
$$
N(\mathbf x,t)=N_c+r(t)\big(N(\mathbf x)-N_c\big),\qquad r=3s^2-2s^3,\ s=t/T_r
$$
  The steady fall is then fitted with a quadratic (free offset and velocity) over the next $T_w$ = 12 units. The two half-windows are fitted separately.
- **Centre** about one fixed reference, which fixes Run 18's bug.
- **Code.** The space-time acceleration is in C (`kmass.c`, equal to Run 18's numpy to 10⁻¹⁵). dt = 0.02, checked against 0.01: the tracks agree to 7×10⁻⁶.

Fine grid only (h = 0.1, 128³). The engine field is the smoothed one (Run 16 d8 s1, Gaussian over 2 places), because Run 18 showed its raw noise scatters a knot of radius ~2 by up to ±19%.

### Results

| drop | $a/a_{\rm univ}$ | registered prediction | $a/a_{\rm lat}$ | half-windows ($a/a_{\rm univ}$) |
|---|---|---|---|---|
| T, clean field, along x | **0.942** | 0.965 ± 0.03 | **0.976** | 0.926, 0.965 |
| T, clean field, along z | **0.983** | 0.991 ± 0.03 | **0.992** | 0.988, 0.981 |
| T, engine field, 12 out | **0.961** | 0.965 ± 0.03 | **0.996** | 0.928, 0.988 |
| T, engine field, 18 out | **0.955** | 0.966 ± 0.03 | **0.989** | 0.934, 0.984 |
| S, clean field, along x | **2.884** | 3.04 ± 0.09 | 0.950 | 2.79, 2.94 |
| S, engine field, 12 out | **3.062** | 3.04 ± 0.09 | 1.008 | 2.88, 3.23 |
| T, no field (control) | centre drift 1.7×10⁻⁵ places over 16 units | < 1×10⁻⁴ | | |

- **The tick-loop knot falls at its own lattice weight ÷ inertia:** 0.976, 0.992, 0.996 and 0.989 of $a_{\rm lat}$ (mean 0.988), in the clean field and in the engine's field alike.
- **Its shortfall from universal is the lattice knot's excess inertia.**
  - Along x it falls at 0.94–0.96 of universal, where $E/M_{\rm spec}$ = 0.973.
  - Along z, the knot's axis, it falls at 0.98, where $E/M_{\rm spec}$ = 0.993.
- **Along x the fall wobbles.** The local acceleration oscillates by about ±5% with a period of about 5.5 time units (panel a). Most likely this is a mode of the knot rung by a pull across its axis, which the 4-unit switch-on is too quick to avoid. Along z it is steady. The 12-unit window covers about two periods, and the half-windows (0.93 against 0.96–0.99 of universal) show what is left of the spread.
- **The space-loop knot still falls about 3× too fast:** 2.88 and 3.06 × universal. Its acceleration varies even more across the window (half-windows 2.79–3.23).
- **No field, no motion:** the control knot's centre drifts by 1.7×10⁻⁵ places in 16 time units.

### Against the pre-registration

| Prediction | Expected | Measured | |
|---|---|---|---|
| P1: tick-loop knot ÷ its own lattice prediction | 1.00 ± 0.03 | 0.976, 0.992, 0.996, 0.989 | **pass** |
| P2: tick-loop knot ÷ universal | 0.965, 0.991, 0.965, 0.966 (± 0.03) | 0.942, 0.983, 0.961, 0.955 | **pass** (offsets −0.023 to −0.004) |
| P3: space-loop knot ÷ universal | 3.04 ± 0.09 | 2.88, 3.06 | **fail, 1 of 2.** It still falls about 3× too fast; the band was tighter than its wobble |
| P4: engine field against clean field | within 0.03 | +0.020, +0.012 | **pass** |
| P5: no-field control | drift < 1×10⁻⁴ | 1.7×10⁻⁵ | **pass** |

The reading written in advance for P3 failing ("the space-loop knot falls near universal") does not apply: it falls at 2.9–3.1×.

### Reading

**1. On the fine grid the tick-loop knot falls at its own lattice weight ÷ inertia,** to 1–2% on average and 2.4% at worst, in a clean field and in the engine's field alike. Its shortfall from the universal rate is the lattice knot carrying a little more inertia than energy:

$$
\frac{E}{M_{T,\rm spec}}=0.907\ (h=0.2)\ \to\ 0.973\ (h=0.1)\quad\text{along }x;\qquad 0.993\ \text{along }z\ (h=0.1)
$$

**2. Where Run 18's "8%" went.**
- About 3 points are the lattice knot's excess inertia, which Run 18's crude boost missed.
- About 1 point is the force on a lattice translation (0.992 of the energy-weighted force).
- The rest, about 3 points, was measurement: short windows that caught the wobble, and a sudden release. (Run 18's 8% was already corrected for the centre bug.)

**3. The continuum.**
- The excess inertia shrinks from 9.3% to 2.7% as h halves, a factor of 3.4, close to the factor of 4 of an error going as h². Extrapolated that way it gives $E/M$ = 0.995 at h → 0.
- Field theory says exactly 1 in the continuum (Lorentz invariance plus Derrick's theorem). Extrapolating linearly would give 1.04, inertia below energy, which the continuum theory does not allow.
- With two grids this is **supported, not established.** A third grid (h = 0.05) would settle the rate. It needs a rewrite of the energy kernel's memory use, since its buffer would be ~10 GB at 256³.

**4. The decision stands.** The space-loop knot still falls about 3× too fast. The tick-loop knot falls with the patterns up to a lattice effect that shrinks with the grid. The provisional rule (twist charged on every closed loop, ticks and relations priced alike) passes the test it was given.

**5. Flag, unchanged.** Inertia = energy here is Lorentz invariance in lattice form. And the knot still moves by a field equation, not by the engine's commitments.

![Run 18b](figures/18b_finegrid.png)
