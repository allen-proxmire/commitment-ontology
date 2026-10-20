## 9f. Run 13: knots on a relational graph with no grid

**Question.** Run 12's knots sat on a cubic grid. ED forbids a rigid lattice (Constraints: "a random web, not a grid"), and P06 now says the substrate is a graph and nothing more. Do Coh + Str knots survive when the relations are irregular, isotropic and ED-compliant?

**ED's requirements on the graph:**
- P06: three-dimensional in the discrete sense, no preferred direction.
- Contrast principle (models R18): no triangles, and no two short loops sharing more than one link.
- Particles step across squares (Attempt C, C-O20).

**Energy.** Coh on links, Str on the graph's loops, and optionally the uncuttable barrier, all with two global unit-conversion constants:

$$
E_{\rm coh}=\frac{1}{c_{\rm coh}}\sum_{\rm links}|\mathbf n_j-\mathbf n_i|^2,\qquad c_{\rm coh}=\frac{\sum|\mathbf e|^2}{3V}.
$$

Two forms of Str were tried.

*Open corners.* At a place c, two of its links (to a and b) that lie on a square:

$$
E_{\rm str}=\frac{1}{c_{\rm str}}\sum_{\rm corners}|(\mathbf n_a-\mathbf n_c)\times(\mathbf n_b-\mathbf n_c)|^2,\qquad c_{\rm str}=\frac{4\sum|\mathbf A_c|^2}{3V}.
$$

On the cubic lattice this is exactly Run 12's four-corner Str. The same code reproduces Run 12's energies to 10⁻¹⁴.

*Closed loops.* The solid angle enclosed by the four directors around a square $i\!-\!j\!-\!l\!-\!k$, averaged over the square's two diagonal splittings:

$$
E_{\rm loop}=\frac{1}{c_{\rm loop}}\sum_{\rm squares}\Omega_{\rm sq}^2,\qquad
\Omega_{\rm sq}=\tfrac12\big[W_{ijl}+W_{ilk}+W_{jlk}+W_{jki}\big],
$$

$$
W_{abc}=2\,\mathrm{atan2}\big(\mathbf a\cdot(\mathbf b\times\mathbf c),\;1+\mathbf a\!\cdot\!\mathbf b+\mathbf b\!\cdot\!\mathbf c+\mathbf c\!\cdot\!\mathbf a\big),\qquad c_{\rm loop}=\frac{\sum|\mathbf A_{\rm sq}|^2}{3V}.
$$

For a smooth field, $\Omega_{\rm sq}\approx\mathbf A_{\rm sq}\cdot\mathbf B$ with $B_c=\tfrac12\epsilon_{cab}\,\mathbf n\cdot(\partial_a\mathbf n\times\partial_b\mathbf n)$. Both forms therefore have the same continuum limit as Run 12, $\int\sum_{a<b}|\partial_a\mathbf n\times\partial_b\mathbf n|^2$.

Positions enter only when the graph is built and when the Hopf charge is measured (by interpolating to a probe grid). The energy uses only who is linked to whom and which links close squares.

### Substrates

| Substrate | How it is made | Triangles | Squares per link | Links per place | Isotropy | Single-link doors |
|---|---|---|---|---|---|---|
| Cubic grid (reference) | — | 0 | 4.00 | 6 | exact | 0 |
| Random triangle-free graph | Poisson points coloured black/white at random; each linked to its k nearest of the other colour (bipartite) | 0 | 5.1 (k = 4) to 23 (k = 8) | 5.1–9.6 | 0.2% | 0 |
| Random graph with triangles | Delaunay links of Poisson points (forbidden by the contrast principle; reference) | 13.5 per place | — | 15.5 | 0.3% | 0 |
| **Random cubical complex** | Each tetrahedron of a random Delaunay tessellation split into four hexahedra. Places are points, edge midpoints, face centres and cell centres; links join neighbouring dimensions; **every face is a square** | **0** | **3.90** | 5.1 mean (4 to 15.5) | 0.6% | **0** |

**The cubical complex meets ED's conditions:**
- Contrast principle: no triangles, and two squares share at most one link.
- Every link lies on at least three squares.
- It is irregular, with no grid.
- Walk-return probability falls as $t^{-1.60}$ (3D is $t^{-1.5}$).
- Hop-ball growth peaks at an exponent of about 4.4 at short range, because the original points are hubs with about 15 links each. It falls toward 3 (3.6 at 16 hops) as far as the box allows.
- **The random triangle-free graph** also passes P06's instruments (ball exponent 3.0–3.2, walk slope −1.48). But its squares do not tile space, and that turns out to matter.

### Results

**(a) Open-corner Str on the random triangle-free graph (k = 4): the knot unties at every spacing.** Q = 1 was seeded in box 9.6, with no cutting rule unless stated.

| Spacing (link length) | Places | FIRE, 2,000 steps | Plain flow, 4,000 steps | With the uncuttable rule (FIRE, 2,000) |
|---|---|---|---|---|
| 0.20 (0.21) | 110k | Q −0.95 → **0**, E → 0 | Q → **0** | Q → −0.49, still falling |
| 0.16 (0.17) | 216k | Q → **0** | Q → **0** | Q → −0.65, still falling |
| 0.12 (0.13) | 511k | Q → **0** | Q → −0.82, falling | Q → −0.83, falling |
| 0.10 (0.10) | 884k | Q → **0** | Q → −0.92, falling | Q → −0.83, falling |

- In every case the graph's Str collapses within a few hundred steps: the Coh/Str balance jumps from 1 to about 11–30.
- With Str gone, the knot behaves like Coh alone: it shrinks and unties. A finer graph only slows this down, and the 60° rule slows it but does not stop it.

**(b) Why: the graph hides the twist.** Starting from the same seed, 500 steps of plain flow; the graph's Str is compared with the continuum Str of the same field interpolated and smoothed over one cell.

| Substrate and Str | Str the graph charges | Str of the smoothed field | Fraction charged | Q = 1 knot |
|---|---|---|---|---|
| Cubic grid, corner Str | 0.752 | 0.768 | **0.98** | holds |
| Random triangle-free, corner Str, 5.1 links per place | 0.034 | 0.838 | **0.04** | unties |
| Same, 6.2 / 7.4 / 9.6 links per place | 0.076 / 0.145 / 0.314 | 0.86 / 0.88 / 0.88 | 0.09 / 0.16 / 0.36 | unties |
| Random triangle-free, **loop Str** | 0.013 | 0.828 | **0.02** | unties |
| Random graph with triangles (chord area) | 0.558 | 0.767 | 0.73 | holds |
| Random cubical complex, corner Str | 0.456 | 0.817 | 0.56 | **cut at step 2,000** (a link flips) |
| **Random cubical complex, loop Str** | 0.474 | 0.804 | 0.59 | **holds** |

- On the random triangle-free graph the knot is still there: the smoothed field keeps its full Str. But almost no square's loop encloses any twist (largest $|\Omega_{\rm sq}|$ = 0.03). The twist runs through the graph's longer cycles, which nothing charges.
- Adding links helps only slowly. Charging squares as closed loops does not help on this graph, because its squares do not close up into cells.
- **What works is a substrate whose faces tile space**: the cubic grid, a triangulation, or the cubical complex. Then every surface the twist could pass through is made of charged loops. Summed over a closed surface of squares, $\sum\Omega_{\rm sq}$ is $4\pi$ times an integer, so the twist can leave only through a square whose loop reaches $\Omega=\pm2\pi$. Open corners are not enough even then: the cubical complex with corner Str was cut by a flipped link.

**(c) Knots on the cubical complex with loop Str, no cutting rule.** Q = 1 in box 9.6, relaxed to convergence with FIRE on three independent random complexes:

| Complex | E (graph units) | Q (fine probe) | Core radius | Virial |
|---|---|---|---|---|
| Seed 2 | 0.810 | −0.945 | 0.93 | 0.58 |
| Seed 3 | 0.896 | −0.962 | 1.05 | 0.78 |
| Seed 4 | 0.864 | −0.936 | 0.91 | 0.65 |
| Spread | 0.857 ± 0.043 (±5%) | | | |

- Adding the uncuttable rule to the seed-2 knot changes its energy by 0.5%. Its barrier energy is 2×10⁻⁴, so the rule is almost never touched. **The knot is held by Str on closed loops, not by the rule.**
- Absolute energies sit about 30% below the continuum's 1.204, and knots are smaller (R ≈ 0.9–1.05 against 1.34). Both are what the disorder does: once places relax, the random complex is softer than its average link count suggests (κ_coh = 0.83 for Coh). That changes the units, not the physics, so the test that counts is the ratios.

**(d) Spectrum on the cubical complex** (box 14, 672k places, one complex, loop Str, no cutting rule, FIRE to convergence):

| Q | E (graph units) | Q (fine probe) | Core radius | Virial | $E_Q/E_1$ | Sutcliffe | Cubic grid (Run 12) |
|---|---|---|---|---|---|---|---|
| 1 | 0.8256 | −0.948 | 0.97 | 0.60 | 1 | 1 | 1 |
| 2 | 1.3933 | −1.938 | 1.40 | 0.71 | **1.688** | 1.634 | 1.643 |
| 3 | 1.9486 | −2.928 | 1.96 | 0.88 | **2.360** | 2.287 | 2.299 |
| 4 | 2.5538 | −3.869 | 1.79 | 0.83 | **3.093** | 2.861 | 2.914 |

- Every knot keeps its charge, and two Q = 1 knots still bind into one Q = 2 knot (by 16%).
- The ratios sit 3% above the continuum for Q = 2 and 3, and 8% above for Q = 4.
  - The Q = 4 relaxation had not fully converged (max |grad| = 0.02).
  - The Q = 1 knot is the smallest (about six places across), so it is the most under-resolved, which raises every ratio. The cubic grid at h = 0.2 shows the same sign at a smaller size.
  - The ±5% disorder between complexes in (c) applies to each knot separately.
- **Within that, the cubical complex reproduces the knot spectrum.**

**(e) Quench on the cubical complex** (box 9.6, 108k places, random field, 20,000 steps of gradient flow; energy evaluated with full Str):

| Protocol | Energy: start → 2,000 → 20,000 | Net Q in box | What is left |
|---|---|---|---|
| Loop Str at full strength from the start | 6,788 → 2,050 → **961**, still slowly falling | −0.78 | one tangle over **74%** of the box: **jammed** |
| Coh alone first, loop Str ramped in over 10,000 steps | 6,788 → 101 → **96.9**, flat | +0.17 | one tangle over **61%** of the box: jammed, at a tenth of the energy |

- On this substrate the protection *is* Str. So an instant quench behaves like Run 12's uncuttable quench: the random tangle cannot undo itself and jams.
- Letting Coh act alone first untangles most of it: the energy falls 70× before Str takes hold. What Str then freezes is still one extended tangle, not separate knots. Only one ramp rate was tried.

### Reading

- **On ED's own kind of substrate, particle-knots need one more structural fact.** The relations must close up into faces that tile space: every short loop a face, every face a square. And the twist must be charged on those closed loops, not at open corners.
  - A random triangle-free graph, even one that passes P06's instruments, lets a knot's twist hide in its uncharged longer cycles, and the knot unties.
  - A random **cubical complex** has none of these gaps. It satisfies both clauses of ED's contrast principle, and it holds knots with no cutting rule.
- **This turns "uncuttable" from a rule into a consequence.** On a cubical complex with loop Str, cutting a knot means some square's loop must enclose half the sphere ($\Omega=\pm2\pi$). That costs $(2\pi)^2$ in loop-Str units, so the protection is an energy barrier. ED's reservation rule (K2) is then not needed for knots built this way. The barrier was measured at 2×10⁻⁴ in (c), so the rule never acted.
- **It ties to ED's own record.** ED's particle line already found that "a particle needs two things from its medium: no single-link doors, and squares" (C-O20). This run adds a third: **the squares must tile, so that every loop is a face.** ED's grown glass has near-cubic local order (R18), which is the right local structure; its long-range maze is the open problem.
- **Quench.** Neither an instant quench nor a slow switch-on of Str left isolated knots: both freeze one extended tangle. Separate particles would need a regime this test did not find, such as a slower ramp, noise, or expansion.
- **What this is not.** The cubical complex was built from a random Delaunay tessellation: space was supplied (as in every ED model), not grown. Coh + Str on a cubical complex is still the Faddeev–Skyrme model, so a matching spectrum is a pass, not a prediction. The ED-specific content is the substrate condition: faces that tile, with the twist charged on closed loops.

![Run 13](figures/13_graph_knots.png)

