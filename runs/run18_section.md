## 9k. Run 18: does matter fall? (a knot of commitment in the engine's clock field)

**Question.** Every body that has fallen so far (Runs 16–17) is a **pattern of possibility**. ED's matter is **committed**: in Runs 12–13 a particle is a knot of commitments, a director field n held together by Coh (alignment between neighbours) and Str (twist held around closed loops). ED's own record says committed matter that moves by paying for commitments is pushed away from matter. So: does a knot fall, and does it fall *like everything else*?

**Target, fixed in advance.** Universality of free fall for composite bodies: a body's binding and internal energy must fall exactly like the rest of its mass.
- MICROSCOPE: titanium against platinum, η < ~10⁻¹⁵ (Touboul et al. 2022).
- Lunar laser ranging: the Earth's gravitational self-energy falls like the rest of it, to ~10⁻⁴ of that energy (the Nordtvedt effect).

A knot is the cleanest composite in the record. About half its energy is Str, so a rule that lets Str weigh but not resist (or the reverse) shows up at order one.

The pre-registration is `PREREG.md` in `matter_run.zip`, written before any knot was evolved in the engine's field.

### Model

**The knot.** The relaxed Q = 1 knot of Run 12 on a cubic grid (h = 0.2, 64³; and the refined h = 0.1, 128³), with one knot unit = one engine place. Run 12's lattice energy:

$$
E_{coh}=h\sum_i\sum_a|n_{i+a}-n_i|^2,\qquad E_{str}=\frac1h\sum_i\sum_{a<b}\frac14\sum_{s_a,s_b=\pm}\big|D^{s_a}_a n_i\times D^{s_b}_b n_i\big|^2,\qquad D^{\pm}_a n_i=n_{i\pm a}-n_i
$$

**Weight: every cost counted in local ticks.** A place whose clock runs at rate N pays its commitments' costs at N per global tick, so each term is weighted by the local clock rate:

$$
V_N=h\sum_{i,a}\tfrac12(N_i+N_{i+a})\,|n_{i+a}-n_i|^2\;+\;\frac1h\sum_i N_i\sum_{a<b}\tfrac14\sum_{s_a,s_b}\big|D^{s_a}_a n_i\times D^{s_b}_b n_i\big|^2
$$

(`kknot3.c`. At N = 1 it equals Run 12's kernel to 4×10⁻¹¹ in energy and 10⁻¹⁵ in gradient; the gradient matches central finite differences to 1.6×10⁻⁸.)

**Inertia: two readings of Str.** Motion is change of n between ticks, and a tick at a slow place is longer, so the kinetic energy carries 1/N:

- **(S) Str on spatial loops only,** as in Runs 12–13. Only Coh has a time part:

$$
T_S=\sum_i \frac{h^3}{N_i}\,k_c\,|\dot n_i|^2
$$

- **(T) Str also on loops that include a tick.** A square made of one relation and one tick carries twist $|\dot n\times D_a n|^2$, priced like the spatial squares:

$$
T_T=\sum_i\frac{h^3}{N_i}\,\dot n_i\cdot A_i\,\dot n_i,\qquad A_i=k_cI+\frac{k_s}{h^2}\sum_a\tfrac12\sum_{s=\pm}\Big(|D^s_an_i|^2I-D^s_an_i\,(D^s_an_i)^{T}\Big)
$$

  This is the lattice form of the Lorentz-invariant Faddeev–Skyrme kinetic term. k_c = k_s = 1 throughout.

**Equation of motion.** With |n| = 1 held by a Lagrange multiplier λ:

$$
\frac{2h^3}{N_i}A_i\,\ddot n_i=-\frac{\partial V_N}{\partial n_i}+\lambda_i n_i,\qquad \lambda_i\ \text{fixed by}\ n_i\cdot\ddot n_i=-|\dot n_i|^2
$$

(A = k_c I for reading S.) It is integrated by velocity Verlet on the sphere (renormalise, then project the velocity onto the tangent plane). Energy drift is 10⁻⁸–10⁻⁷ over 400 steps.

**What the model predicts.** Displace the static knot rigidly by **X**. Its energy density e(x) then sits in N(x + X), so

$$
V_N(\mathbf X)\approx\sum_x N(x)\,e(x)+\mathbf X\cdot\sum_x e(x)\,\nabla N(x)\quad\Rightarrow\quad\mathbf F=-E\,\langle\nabla N\rangle_e
$$

where ⟨·⟩_e is the energy-weighted average over the knot. A rigid boost $\dot n=-\dot{\mathbf X}\cdot\nabla n$ gives $T=\tfrac12M\dot X^2/\bar N$. So the knot accelerates toward slower clocks at

$$
a=\frac{E}{M}\,\bar N\,\langle\nabla N\rangle_e,\qquad a_{\rm univ}\equiv\bar N\,\langle\nabla N\rangle_e
$$

$a_{\rm univ}$ is the fall of a body of the knot's shape whose energy all both weighs and resists. It is the law the patterns obey in this metric: a pattern falls at $\langle N\nabla N\rangle$ (Run 17, coupling B).

**Where E/M comes from (continuum).** For a static knot, averaging over directions gives $\int|\partial_xn|^2=\tfrac13E_{coh}$ and $\int\sum_a|\partial_xn\times\partial_an|^2=\tfrac23E_{str}$. So

$$
M_S=\tfrac23E_{coh},\qquad M_T=\tfrac23E_{coh}+\tfrac43E_{str}
$$

Derrick's virial theorem for Faddeev–Skyrme gives $E_{str}=E_{coh}=E/2$ at the static knot, so

$$
\frac{E}{M_S}=3,\qquad\frac{E}{M_T}=1
$$

With spatial-only Str, all of the knot's energy weighs but only two-thirds of its Coh energy resists, so the knot falls three times too fast. With Str also on loops that include a tick, inertia equals energy.

**Masses of the lattice knots** (rigid boost along x; `check_kernel.py`):

| | h = 0.2 | h = 0.1 |
|---|---|---|
| $E=E_{coh}+E_{str}$ | 246.5 + 288.5 = **535.0** (virial 1.17) | **546.8** (virial 1.06) |
| $M_S$ | **159.2** (continuum $\tfrac23E_{coh}$: 164.3) | **176.6** |
| $M_T$ | **544.5** (continuum: 549.0) | **552.6** |
| $E/M_S$ | **3.36** | **3.10** |
| $E/M_T$ | **0.982** | **0.989** |

Along z (the knot's own axis) at h = 0.2, $E/M_S$ = 3.37 and $E/M_T$ = 1.003. As h halves, $E/M_S$ moves toward 3 and $E/M_T$ toward 1.

### Code checks (clean linear clock field)

Linear field $N=1-g\,x$ with g = 0.004 per unit, flattened beyond ±4.5. Measured $a/a_{\rm univ}$, with $E/M$ in brackets:

| | h = 0.2 along x, 4 units, quadratic (pre-registered) | h = 0.2 along x, 8 units, cubic (the runs' fit; after the fact) | h = 0.2 along z, 8 units, cubic (after the fact) | h = 0.1 along x, 4 units, quadratic (pre-registered; the runs' fit) | the same, t = 0 point corrected (after the fact) |
|---|---|---|---|---|---|
| (S) | 3.22 (3.36) | 3.40 (3.36) | 3.30 (3.37) | 3.16 (3.10) | 3.08 (3.10) |
| (T) | 0.845 (0.982) | 0.774 (0.982) | 0.938 (1.003) | 1.00 (0.989) | **0.916** (0.989) |

The pre-registered checks had two problems. Both were found after the engine drops, while looking for why they missed. Both are errors in the registration.

- **The wrong fit window.** The h = 0.2 bands for M1–M3 came from the first column, fitted over 4 time units. The engine drops were fitted over 8 time units with a cubic, as the pre-registration itself says. On the coarse grid the fitted value depends on the fit by up to 12%, because the knot's acceleration is not constant as it crosses grid cells.
- **A measurement bug at h = 0.1.** The knot's centre is the centroid of its Coh energy, taken with the minimal-image convention about a reference point.
  - The first point (t = 0) was taken about the box centre; every later point about the knot's own starting centre, 0.11 places away.
  - At h = 0.1 one row of grid points lies between the two cut lines, so the t = 0 centre came out 0.0023 places off along x and y (0.0005 along z). At h = 0.2 no grid point lies between them, and the offset is exactly zero.
  - The knot released with **no field at all** shows the bug as a step at the first record that never changes afterwards: −2.33×10⁻³ at t = 0.2 and −2.34×10⁻³ at t = 4, identical in both readings.
  - The step entered every h = 0.1 fit, including the pre-registered code check. In the clean field it opposed the fall and inflated reading T from 0.92 to 1.00. In the engine field it went with the fall and pulled the values down.
  - It is corrected by subtracting the no-field track. That is the same as taking the t = 0 point about the same reference as the rest.

The bands below are left as registered.

### Method

- **Field:** ED's engine with the adopted rules (Run 16 source: density 8, seed 1, box 60, the ball at the centre). It is read as $N=n/\lambda_0$ and interpolated trilinearly onto the knot grid. Knot coordinates are clipped at ±4.5 when reading N, so the knot box's periodic seam sits where the knot has almost no energy.
- **Releases:** at rest, at $r_0$ = 12 and 18 places from the ball.
  - h = 0.2: along +x, +y, +z, both readings (12 drops), 8 time units (400 steps of 0.02), cubic fit.
  - h = 0.1: along +x, both readings (4 drops), 4 time units (400 steps of 0.01), quadratic fit.
- **Centre:** centroid of the Coh energy density $\sum_a|D^+_an|^2$ (minimal image; see the bug above).
- **Reference:** $a_{\rm univ}$, from the static knot at its release point.
- **Comparison patterns:** Run 17's coupling B (clock-only metric, so the same law), m = 2, width 4, released at the same six places.
- **After-the-fact diagnostics (not pre-registered):**
  - every h = 0.2 drop, the patterns, and the two h = 0.1 drops with reading T, repeated in the engine field smoothed over 2 places (Gaussian, periodic). Reason: the field is a 6,000-tick average of a counting process and keeps noise at the scale of single places. A pattern of width 4 averages it out. A knot of radius ~2 places does not, and over its fall it samples a gradient that changes from place to place.
  - the clean-field checks with the runs' own fits, along x and z
  - the h = 0.1 knot released with no field (both readings), and every h = 0.1 track corrected with it
  - every track refitted with other polynomial fits, to measure how much the fit matters

### Results

All 42 releases fall inward.

**Acceleration ÷ universal** ($a/a_{\rm univ}$), with the registered fits. Directions are +x, +y, +z.

| | $r_0$ | raw field (pre-registered) | smoothed field (after the fact) | clean field, same fit | pre-registered band |
|---|---|---|---|---|---|
| (S) h = 0.2 | 12 | 3.57, 3.53, 3.45 | 3.41, 3.41, 3.28 | 3.40, 3.40, 3.30 | 3.2 ± 0.2 |
| (S) h = 0.2 | 18 | 3.72, 3.36, 3.39 | 3.41, 3.37, 3.27 | 3.40, 3.40, 3.30 | 3.2 ± 0.2 |
| (S) h = 0.1 | 12, 18 (x) | 3.03, 3.17 | — | 3.16 | 3.16 ± 0.15 |
| (T) h = 0.2 | 12 | 0.88, 0.92, 0.99 | 0.77, 0.78, 0.94 | 0.77, 0.77, 0.94 | 0.84 ± 0.05 |
| (T) h = 0.2 | 18 | 1.11, **0.51**, 1.01 | 0.81, 0.77, 0.93 | 0.77, 0.77, 0.94 | 0.84 ± 0.05 |
| (T) h = 0.1 | 12, 18 (x) | **0.906**, 1.029 | 0.859, 0.820 | 1.00 | 1.00 ± 0.03 |
| patterns (÷ own prediction) | 12 | 0.989, 0.989, 0.989 | 0.988, 0.988, 0.988 | — | 0.99 ± 0.03 |
| patterns (÷ own prediction) | 18 | 0.989, 0.988, 0.988 | 0.990, 0.988, 0.989 | — | 0.99 ± 0.03 |

(The clean-field check was run along x and z. y equals x by the knot's symmetry, since $E/M$ is identical along x and y. The h = 0.1 rows contain the measurement bug.)

**h = 0.1 with the bug corrected** (the registered fit: 4 units, quadratic from t = 0; after the fact):

| | E/M | clean field | raw engine field (12, 18) | smoothed engine field (12, 18) |
|---|---|---|---|---|
| (S) | 3.10 | 3.08 | 3.08, 3.23 | — |
| (T) | 0.989 | **0.916** | 0.960, 1.090 | **0.919, 0.929** |

On the fine grid the smoothed engine field gives what the clean field gives, to 1.5%. The raw field scatters more: reading T is 5% and 19% above the clean value.

**Mean ± spread over the six h = 0.2 drops:**

| | raw field | smoothed field |
|---|---|---|
| (S) | 3.50 ± 0.13 | 3.36 ± 0.07 |
| (T) | 0.90 ± 0.21 | 0.83 ± 0.08 |

The smoothed spread is almost all direction (x and y against z), and the clean field shows the same split. Once smoothed, the engine field gives what a clean field gives with the same measurement: within 1.5% in 11 of 12 coarse-grid drops (the twelfth, reading T at 18 along x, is 4.6% high). With a quadratic fit instead of the cubic, the coarse-grid values move by up to 12% (reading T to 0.85–0.96), and the engine field still matches the clean field to within 3%.

**Coarse against fine grid, one fit** (clean field along x, 4 time units, quadratic from t = 0, the bug corrected), measured ÷ the knot's own $(E/M)\,a_{\rm univ}$:

| | h = 0.2 | h = 0.1 |
|---|---|---|
| (S) | 0.958 | 0.995 |
| (T) | 0.860 | **0.926** |

Reading T's shortfall from its own E/M roughly halves as h halves (14% → 7%), as a first-order lattice error would. Two resolutions cannot establish that.

**M3, the same release under the two readings** ($a_S/a_T$), registered fits:
- raw h = 0.2: 4.06, 3.83, 3.50 (r = 12), 3.34, **6.59**, 3.37 (r = 18)
- smoothed h = 0.2: 4.42, 4.38, 3.48, 4.21, 4.35, 3.53
- raw h = 0.1: 3.34, 3.08 (bug corrected: 3.21, 2.97)

**The raw-field outlier** (reading T, 18 places out along y, 0.51). Its centre first jumps toward the ball, moving over the first 0.2 time units at 2.5 × the universal acceleration, and then slows. In the smoothed field the same drop gives 0.77, like its neighbours. The knot reshapes in response to the field's place-to-place noise, which moves its energy centroid. Reading T's knot falls ~4× more slowly, so the reshaping matters more.

### Against the pre-registration

Judged on the raw field, with the registered fits:

| Prediction | Expected | Measured | |
|---|---|---|---|
| M1 (S), h = 0.2 | 3.2 ± 0.2 | 3.36–3.72; 2 of 6 in band | **band missed** (registered from the wrong fit window); the effect, ≈3× too fast, holds in every drop |
| M1 (S), h = 0.1 | 3.16 ± 0.15 | 3.03, 3.17; corrected 3.08, 3.23 | **pass** |
| M2 (T), h = 0.2 | 0.84 ± 0.05 | 0.51–1.11; 1 of 6 in band | **fail as written** |
| M2 (T), h = 0.1 | 1.00 ± 0.03 | 0.906, 1.029; with the bug corrected 0.960, 1.090 | **fail: 1 of 2 as measured, 0 of 2 corrected** |
| M3, h = 0.2 | 3.8 ± 0.3 | 3.34–6.59; 3 of 6 | **3 of 6** |
| M3, h = 0.1 | 3.16 ± 0.15 | 3.34, 3.08; corrected 3.21, 2.97 | **1 of 2** |
| M4 patterns | 0.99 ± 0.03 | 0.988–0.989, 6 of 6 (12 of 12 with the smoothed field) | **pass** |
| all inward | | 42 of 42 | **pass** |

The two failure conditions written in advance:
- *"M1 fails: the spatial-only knot falls universally."* It does not. Every spatial-only drop, at both resolutions, in both fields and with every fit, falls 2.7–3.7× faster than universal.
- *"M2 fails beyond the lattice factor: even space-time Str does not make matter fall like patterns."*
  - Not triggered as written. In the engine's field the knot falls as it does in a clean field on the same lattice with the same fit: on the fine grid 0.919 and 0.929 against 0.916.
  - But the lattice factor registered at h = 0.1 (≈ 1.00) was inflated by the measurement bug. The real one is 0.93 of E/M.
  - So this run puts reading T **within about 8% of universal fall on the fine grid, not within the 3% registered.** The patterns beside it fall at 0.99.

### Reading

**1. Weight is automatic; inertia is not.** Counting every commitment cost in local ticks (the clock rule, Run 15) makes all of a knot's energy weigh: the force on it is $E\,\langle\nabla N\rangle$, whatever the energy is made of. Whether all of that energy also *resists* depends on where Str is charged.

**2. Str on spatial loops only is ruled out.** Then only the Coh part of the knot's change costs anything when it moves.
- $M_S=\tfrac23E_{coh}=E/3$ in the continuum, so the knot falls three times faster than a pattern beside it.
- Every drop shows it: 2.7–3.7× at both resolutions, in both fields and with every fit.
- The knot's binding energy (its Str) weighs without resisting. MICROSCOPE bounds such a difference at 10⁻¹⁵, and this one is of order one.
- **With Runs 12–13's Str as written, ED's matter fails the equivalence principle.**

**3. Charging Str also on loops that include a tick brings the knot to within about 8% of universal fall on the fine grid.**
- A square of one relation and one tick costs twist like a square of two relations. Then $M_T=\tfrac23E_{coh}+\tfrac43E_{str}$, which equals E at the static knot (Derrick's theorem).
- The knot falls at 0.77–0.96 of universal on the coarse grid, depending on direction and fit, and 0.92–0.93 on the fine grid. Each value is the same as in a clean field on the same lattice.
- The remaining shortfall is a lattice effect. It roughly halves as the grid spacing halves.
- In the continuum this model is the Faddeev–Skyrme field coupled to the static metric $-N^2dt^2+d\mathbf x^2$. There a small knot follows the same path as everything else: that is a theorem of field theory, not something this run shows. **This run shows it to about 8%, not to the registered 3%.**

**4. Relabelling flag.** This is the lattice form of a known result. In a Lorentz-invariant field theory a static soliton's inertia equals its energy, and in a static metric it falls universally. Nothing here derives Lorentz invariance from ED. What the run adds for ED is a requirement:
- In ED terms: **twist held across successive ticks must cost exactly as twist held across a relation does.**
- On Run 13's random cubical complex, Str lives on square faces. This asks that squares with one tick edge count as faces too. That fits the "squares, no triangles" contrast principle if a tick is an edge of the same standing as a relation. Whether ED's event layer works that way is not tested here.

**5. What this run is not.** The knot here moves by the lattice field equation, a Lagrangian whose costs are counted in local ticks. It does not move by the engine's commit-and-release events.
- So this answers "does a knot of ED's Coh and Str fall in the engine's clock field?", not "does a knot built from engine commitments fall?"
- ED's old event-layer finding, that committed matter which moves by paying for commitments is pushed away, is about a different law of motion and is untouched.
- Joining the two is open.

**6. Adopted provisionally on 17 October 2026: Str is charged on every closed loop of the history, including loops made of a relation and a tick, with ticks and relations priced alike.** It costs nothing elsewhere in the record (Runs 12–13 used only static knots). It is required for composite matter to fall like everything else, and it is Lorentz invariance of the twist cost, flagged as such. See §10.

**Open:**
- a smaller grid spacing (h = 0.05) or a better time–space discretisation, to see reading T's lattice factor reach 1
- a no-field control registered in advance (it would have caught the centre bug)
- knots built from engine commitments
- the hop half (the pattern rule) for knots; at first order it does not change the fall
- the Nordtvedt test, which needs a knot's own gravity and is not in this model

![Run 18](figures/18_matter.png)
