## 9zzz2. Run 77: a flat sheet of matter on a lattice bent by its own field

*22 October 2026. A registered run on a flat sheet of matter, with the possibility it releases returned at a far-away reservoir. It follows the design note (§9zzz). Registered and hashed before any engine run (`sheet77/PREREG_77.md`), with the theory's predictions computed and hashed beforehand (`theory77.json`).*
- *Amendment 1: the first launch ran no simulation. The driver's skip-finished-jobs filter indexed past the end of each job line, so its job list came out empty, and the rebuild steps then stopped while reading their arguments. The filter was fixed, a guard added, and everything re-hashed (05:20:06 UTC) before any run. Only the driver and the registration text changed; no data had been made.*
- *An independent agent checked the run (below). Its findings correct several statements made when the results first came in; the corrected statements are the ones given here.*

**Questions (as registered).**
1. On a lattice built so that the medium's space is curved by the stress of the medium's own field, as option 3 says, does the engine's medium carry the field the lattice was built from? Does that field have option 3's form rather than option 1's, and do clocks read it as option 3's clock?
2. Does the engine confirm the limit the design note found? With one hop per tick, a more stretched lattice forces a slower medium everywhere, which strengthens the field, which stretches the lattice further.

**The setup.**
- **Lattice:** 36³, periodic, p_s = 1, about 64 units per place.
- **The sheet:** all 648 pairs filling the plane x = 0. Each holds until the possibility present at its two places, summed over ticks, reaches kH (H = 640). The hold multiplier k sets the sheet's strength: smaller k, stronger draw.
- **The reservoir (a boundary condition, the one change to the engine):** possibility the sheet releases re-enters over the plane x = 18, standing in for infinity, instead of over the whole box.
- **Option 3's planar solution,** in Run 72's equal-place form, with ξ the distance from the sheet:
$$
\tilde\gamma=B^{-2}d\xi^2+B\,(dy^2+dz^2),\qquad B(\xi)^2=1+4F\xi,\qquad \frac{d\varphi}{d\xi}=-\frac{F}{B^2}.
$$
  - This gives R̃_ξξ = 2φ_ξ², R̃_yy = 0 and Δ̃φ = 0; the scalar curvature is R̃ = 2F²/B², and B²φ_ξ = −F is the conserved flux.
  - Links: x-links c_n·B², y/z-links c_n/B.
  - The one-hop-per-tick cap needs c_n·(total) ≤ 6 at every place, so a bent lattice runs at c_n = cn_max(F), set by the most stretched links, at the reservoir.
- **The flux the engine's medium carries.** Each unit hops with probability f(P)/P (never capped: its largest value, at P = 1, is 0.99) and takes link k with probability W_k/6, so the mean current along a link is W·[f(P) − f(P′)]/6. The sheet draws σ per place per tick, so the current across every x-link is J = σ/2, and
$$
J=\frac{c_nB^2}{6}\,\big[z(\xi)-z(\xi+1)\big]\quad\Rightarrow\quad B^2\,\big|\Delta\varphi\big|=F_{\rm eng}=\frac{3\sigma}{c\,c_n}.
$$
  A lattice is self-consistent when it is built with the flux it then carries, F = F_eng.
- **The theory** (`theory77.py`, fixed beforehand): the planar mean field, each plane at P = R(z) (Run 22's equation of state), with all units conserved and the sheet's draw responding to its own well (σ = 2P_sheet/kH).

**Results** (25,000 ticks per run, read over the last 15,000; every run stationary, the two reading halves agreeing in σ to 0.35%; conservation exact).

| test | prediction | engine | verdict |
|---|---|---|---|
| **K77a** weak sheet (k = 16): self-consistency | F* = 0.03159 (fixed beforehand) | F_eng = 0.03155: −0.13 ± 0.15% (two seeds) | **PASS** |
| **K77b** the field's shape, φ(ξ)/φ(1), ξ = 3–15 | option 3's log law on the bent lattice; option 1's straight line on the flat one (the two differ by up to 0.13) | deviations 0.0050 (bent) and 0.0041 (flat) | **PASS** |
| **K77c** clocks: P(ξ)/P(18) against the medium's equation of state R(z) | agreement to ≤ 0.003 | 1.0×10⁻⁴ | **PASS** |
| **K77d** stronger sheet (k = 8): self-consistency, x-conductance B² = 9.5 at the reservoir, c_n = 0.30 | F* = 0.11852 (fixed beforehand) | F_eng = 0.11848: −0.04 ± 0.18% | **PASS** |
| **K77e** strong sheet (k = 2), no fixed point on this box: rebuild each lattice from the previous one's measured flux | registered: F grows by ≥ 1.5× then ≥ 1.3×, each step within 10% of the theory's response for the lattice actually used (sequence fixed beforehand: 0.0872 → 0.2264 → 0.4405) | 0.0869 → 0.2256 → 0.4379: ratios 2.60, 1.94; −0.36%, −0.11%, −0.35% from the theory's response on the lattices used (0.0872, 0.2259, 0.4394) | **PASS** |

- **On the same sheet,** the bent lattice's field at the sheet is φ = 0.298 and the flat lattice's is 0.517 (theory 0.296 and 0.520).
- **Option 3's mean-field clock formula,** N = (1+ε)e^(−φ) − ε, differs from the clocks by 0.005 (reported). That is the expected effect of fluctuations: because P fluctuates, the mean P exceeds the fluctuation-free p_s(e^{z/c} − 1) by about 2 units at every plane, and the exact R(z) differs from the formula by the same 0.005.
- **On the k = 2 rebuild,** the hop rate the cap allows falls from 1 to 0.38 to 0.17 as the field grows.

![Run 77](figures/77_sheet.png)

**What the check added.**

1. **Independent reproduction.** Every verdict number was reproduced from the run files with the checker's own code, nothing imported from Run 77's analysis or theory. The checker's solver gives the same fixed points and responses as `theory77` to better than 10⁻⁷.
2. **Registration and runs are clean.**
   - The second hash matches all 13 registered files. Between the two hashes only the registration text and the driver changed (the filter index and a guard); engine, geometry, theory, theory output, analysis and job list are byte-for-byte unchanged. In the failed launch no simulation ran.
   - All nine runs post-date the second hash and have the registered parameters, with c_n = cn_max(F) exactly.
   - Each rebuild step's lattice used exactly F = 3σ/(c·c_n) from the previous run's file.
   - Conservation is exact in every run, and no two profiles are identical.
3. **The engine implements the construction.**
   - The checker computed the curvature of the planar solution numerically: R̃_ξξ − 2φ_ξ² and R̃_yy vanish to finite-difference noise (10⁻⁸ and 10⁻⁷), and Δ̃φ = 0.
   - The engine's x-links equal c_n·B² at the link midpoints exactly, and its y/z-links equal c_n/B to 10⁻¹⁶. The total reaches the cap of 6 at the reservoir on every lattice.
   - In the data, B²·|Δφ| / F_eng averages 0.99–1.02 over the links in every run.
4. **The warm start was needed and does not create the agreement.**
   - In the linearised mean field the slowest relaxation takes 6,300–12,600 ticks, comparable to the 10,000-tick burn-in.
   - Two cold-start runs (every place starting at 64, seeds 901–902, the checker's own driver around the unchanged engine) relax with time constants of 5,900 ± 500 and 9,500 ± 700 ticks, and extrapolate to −0.06% and −0.02% from theory: the same draw as the warm starts.
5. **What K77a–c test.**
   - **K77a and K77d** test the planar mean field's prediction of the sheet's draw. Since c_n is fixed by the lattice, F_eng/F* − 1 = σ/σ_theory − 1. It holds to within about 0.2%.
   - **K77b** confirms that the lattice was built as specified. The field's shape is set by the conductances through the exact current law, so it would pass on a lattice built with any flux. The bending itself was imposed from option 3's formula, not found by the engine.
   - **K77c** tests the medium's equation of state P = R(z) (Run 22). It does not depend on the geometry.
6. **With option 3's clock, the planar solution is flat spacetime.** In the ε → 0 limit the spacetime metric is −e^{−2φ}dt² + e^{2φ}γ̃. With φ = −½ ln B + const this is, up to constants, −B dt² + B⁻³dξ² + dy² + dz². Setting ρ = √B/F (so dρ = B^{−3/2}dξ):
$$
ds^2\;\propto\;-F^2\rho^2\,dt^2+d\rho^2+dy^2+dz^2 ,
$$
   which is Rindler space: uniform acceleration with no tidal curvature. Numerically the Riemann tensor vanishes to 5×10⁻⁵. So a static sheet under option 3 gives a uniform pull and no tides, one of GR's static plane-symmetric vacua. The other sign of the lapse would give Taub's planar solution.
7. **"No fixed point at k = 2" holds only for this box, and the limit is not a bound on stretch.**

| sheet (k) | fixed point on this box (reservoir at 18) | lattice there |
|---|---|---|
| 16 | F = 0.03159 | c_n 0.695, B² 3.3 at the reservoir |
| 8 | F = 0.11852 | c_n 0.302, B² 9.5 |
| 6 | F = 0.292 | c_n 0.137, B² 22 |
| 5 | F = 0.628 | c_n 0.066, B² 46 |
| 4 | F = 3.164 | c_n 0.0135, B² 229 |
| 3, 2 | none (for k = 2, none up to F = 10⁴) | |

   - **The boundary moves with the reservoir distance X_R.** The cap is set by the most stretched link, at the reservoir, where B² = 1 + 4F·X_R.

| X_R | sheets with a fixed point |
|---|---|
| 6 | all, including k = 2 (F = 0.861) |
| 9–18 | k ≥ 4 |
| 24–36 | k ≥ 8 |
| 54–108 | only k = 16 (at X_R = 108, B² ≈ 1085) |
| 144 | none |

   - So the limit is on the sheet's draw times the distance to the reservoir, not on how far the lattice stretches. For a fixed draw σ, a self-consistent lattice exists exactly when σ < c/(4X_R), however large B² becomes as σ approaches that bound. In an unbounded planar medium no self-bent lattice of this kind exists for any sheet, because the planar field does not fall off.
   - **The choice of c_n does not rescue k = 2 on this box.** cn_max gives the smallest F_eng (F_eng ∝ 1/c_n), so any other c_n within the cap makes F_eng larger.
   - **The runaway needs the sheet's clock to stay unslowed while the medium's hops slow.** If the hold were counted in the medium's slowed ticks (σ ∝ c_n, a uniform change of time unit for hops and clocks together), every sheet would have a fixed point: k = 2 at F = 0.139 (c_n 0.26, B² 11) on this box, and at F = 0.123 (B² 19) with the reservoir at 36.
8. **K77e's thresholds cannot detect a missing fixed point.** Run in theory from a flat lattice, the growth criteria pass for k = 6, 5, 4, 3 and 2, and k = 6, 5 and 4 have fixed points. So K77e's PASS shows growth over three steps, matching the theory's response to 0.4%. That k = 2 has no fixed point on this box rests on the theory, which the engine confirms only on lattices with c_n ≥ 0.17, far from k = 4's 0.0135.
9. **Wording corrected from the first draft.** "Space stretched 9.5×" was the x-conductance factor B²; the proper spacing at the reservoir is B⁻¹ = 0.32 along x and B^{1/2} = 1.76 across. k = 8 is not "near the limit": on this box k = 6, 5 and 4 also have fixed points.

**Reading.**
1. **The engine runs on option 3's planar lattice, self-consistently as built.** On a lattice built with option 3's planar geometry at the theory's fixed point, the engine's medium carries the flux the lattice was built with (−0.13 ± 0.15% for k = 16, −0.04 ± 0.18% for k = 8). The field's shape follows the lattice's conductances, and clocks read the medium's equation of state to 10⁻⁴.
   - What is tested is the planar mean field's prediction of the sheet's draw, and the construction. The bending was imposed from option 3's formula, not found by the engine.
   - With option 3's clock the solution is flat Rindler spacetime: a sheet gives a uniform pull and no tides (the check, a calculation).
2. **The hop-rate limit comes from this representation; ED's rules are not shown to impose it.** With one global hop rate on a regular equal-place lattice, a self-consistent planar lattice exists only while the sheet's draw times the distance to the reservoir stays small. Within that bound the lattice can stretch very far (B² up to 229 on this box). Whether ED's rules impose any such limit is not established:
   - the limit disappears if the sheet's clock slows with the medium's hops (a uniform change of time unit, allowed if the tick is not physical time);
   - an irregular graph of isotropic, equal-volume cells would need no slower hop rate, and a local tick would avoid it too;
   - spherical symmetry, where the stretch peaks near the source rather than at the far boundary, is untested, so nothing here bears on holes.
3. **This corrects the design note (§9zzz).** Its "B² ≲ 10" and its statement that the engine carries option 3 only in weak and moderate fields, not near holes, are withdrawn (corrections noted there).
4. **Limits:**
   - planar symmetry only;
   - p_s = 1, ε ≈ 1/70;
   - the reservoir stands in for infinity;
   - two seeds for each self-consistency test;
   - the alternatives (slowed sheet clock, isotropic cells, local tick) are calculations, not runs.
