## 9zc. Run 36: does a bound pattern's energy pull, with binding counted once?

*19 October 2026. Allen: "yes to 1": a pattern's rest energy (ħω, binding included) draws. Pre-registered and hashed before the run (`patternE/PREREG_36.md`, 11:25 UTC), with a kill rule. A trial computation of the ball alone and the unperturbed ground state at m = 0.3 was made while writing the code, and is disclosed there. The diagnostics after the kill rule fired are post hoc and labelled as such. An independent agent checked the hashes, numbers and physics; its corrections are included.*

**Question.** Energy in every form pulls with the same weight as rest mass. Materials with different binding fractions pull alike: the Moon's aluminium and iron agree in their active-to-passive mass ratio to 4×10⁻¹² (Bartlett & van Buren 1986). And a bound system's mass is its total energy, with binding counted once. Under the adopted rules, does the far field of the ball plus a pattern bound in its clock well equal the ball's own far field plus the pattern's ħω?

**Why it is a test.**
- Each body's draw is redshifted by the other's well. The ball's draw is its ticking (Run 30), so the pattern's well lowers it. The pattern's ω is lowered by the ball's well. Counting only energies would therefore count the binding about twice.
- GR's Tolman–Komar bookkeeping repairs this with the momentum-flux term. The bound pattern's internal motion contributes +2KE, which the adopted rule includes (R-b, required by the Lorentz input).
- Whether the engine's own response supplies the cancellation is not built in: the ball's draw falling by exactly the pattern's flux term.

**Setup** (`pattern36.py`, `run36.py`).
- **Engine:** Candidate A″'s relaxed medium in its mean field, which the stochastic engine follows (Run 35). Box 60, P₀ = 64, p_s = 1.
- **The ball:** Run 26's body A, 54 pairs under the presence clock, self-consistent. It draws 8.267 per tick in this box.
- **The pattern:** Run 16's pattern in its ground state, one quantum,
$$
-\nabla^2\psi+m^2N^2\psi=\omega^2\psi,\qquad N=\bar P/P_0 .
$$
- **Its draw:** κ times a local density.
  - **R-b, adopted:** $T^{00}+\sum_iT^{ii}=\psi^2(4m^2N^2-2\omega^2)+6g$, which totals $\kappa(\omega+K/\omega)$.
  - **R-a, contrast:** $T^{00}$ alone, totalling κω.
  - Here g is the local share of $|\nabla\psi|^2$ and $K=\sum|\nabla\psi|^2/\sum\psi^2$.
  - κ is set so the pattern draws 10⁻³ per tick (a test pattern). Doubling it changes the result by 10⁻⁵.
- **Self-consistency:** field and ground state are iterated to 10⁻¹¹.

**Kill rule K36.** Under R-b at m = 0.3, $|\Delta D_{\rm total}/(\kappa\omega)-1|\le0.02$, where $\Delta D_{\rm total}=D_{\rm ball}+D_{\rm pattern}-D_{\rm ball,0}$.

**Results (registered medium).**

| m | binding 1 − ω/m | flux term K/ω² | R-b: ΔD_total/(κω) | ball's change /(κω) | R-a: ΔD_total/(κω) |
|---|---|---|---|---|---|
| **0.3** | 6.0% | 0.193 | **1.134** | −0.058 | 0.911 |
| 0.2 | 1.5% | 0.051 | 1.041 | −0.010 | 0.978 |
| 0.4 | 12.0% | 0.258 | 1.152 | −0.106 | 0.855 |

**K36 fails.** Under the adopted rule the far field overshoots ħω by 13% at m = 0.3, while energy alone undershoots by 9%. Neither counts the binding once. The cancellation fails because the ball's draw falls by only 0.058 κω, against the 0.19 κω it would need.

![Run 36](figures/36_pattern_energy.png)

**Diagnostics (post hoc, not registered; checked by an independent agent).**
1. **The ball under-responds to outside wells.**
   - A weak, distant draw lowers the ambient at the ball by δU. The ball's draw then falls by a fraction 0.526 δU, not δU.
   - That is derived. For P ≫ p_s, ln P is linear in the outflow z (d ln P/dz is 0.698 at the ball, 0.694 far away). The ball's own deficit is linear in its draw D. So $P=P_{\rm amb}\,e^{-U_{\rm ext}}e^{-kD}$ with D ∝ P, which gives
   $$
   \frac{d\ln D}{d(-U_{\rm ext})}=\frac{1}{1+U_{\rm self}},\qquad U_{\rm self}=kD\approx-\ln N_{\rm ball}.
   $$
     Strictly, $U_{\rm self}$ is a draw-weighted average of $-\ln(P/P_{\rm amb})$ at the ball's places.
   - The registered ball sits at N = 0.38 at its own places, so 1/(1 + U_self) ≈ 0.50–0.51, depending on the definition and reference. Measured: 0.526, which agrees to about 4%.
   - **In GR the response is exactly 1, and the reason makes this testable.**
     - The static lapse equation $D^2N=4\pi N(\rho+\sum p)$ is homogeneous in N, so a uniform outside potential rescales a body's Tolman mass by exactly the lapse, at any compactness.
     - In these (isotropic) coordinates the body also shrinks by $e^{-U_{\rm ext}}$.
     - Within ED's own law, the self-coefficient k goes as 1/R. A body whose size and draw both scale by $e^{-U_{\rm ext}}$ keeps kD fixed, and so responds with exactly 1.
     - The engine's ball is held on fixed places and cannot shrink.
2. **The under-response is only part of the failure.**
   - Rescale the ball's change to a response of 1 (dividing by 0.526) and keep the flux term. That gives 1.082 at m = 0.3, 1.032 at m = 0.2 and 1.057 at m = 0.4. K36 still fails.
   - So the fixed places explain about 0.05 of the 0.13 excess. This is an estimate, since the pattern's potential at the ball is not uniform. The rest is unresolved.
   - It grows as the pattern overlaps the ball. That is consistent with the ball's internal adjustment (its stresses), which a body held by rule does not have, but it is not shown.
3. **With weaker-field matter (larger crossover), the adopted rule comes closer, and always closer than energy-only.**

| medium | ball's N at its places | response (1/(1+U_self)) | R-b at bindings | R-a, same patterns |
|---|---|---|---|---|
| P₀ = 64, p_s = 1 (registered) | 0.38 | 0.526 (≈0.51) | 1.041, 1.134, 1.152 (b = 1.5, 6.0, 12.0%) | 0.978, 0.911, 0.855 |
| P₀ = 1024, p_s = 16 | 0.83 | 0.849 (0.842) | 1.022, 1.009, 0.976 (b = 1.6, 5.4, 9.1%) | 0.962, 0.913, 0.876 |
| P₀ = 4096, p_s = 64 | 0.95 | 0.950 (0.948) | **0.996**, 0.984, 0.974 (b = 2.1, 3.3, 4.1%) | 0.965, 0.954, 0.948 |

   - **At p_s = 64:** the adopted rule misses by 0.2–0.6 times the binding (0.4–2.6%), and energy-only by 1.3–1.7 times.
   - **At p_s = 16:** the adopted rule misses by 0.2–1.4 times the binding, and energy-only by 1.4–2.4 times.
   - The adopted rule does not count binding once cleanly beyond the most diffuse pattern. Its miss grows with the pattern's overlap with the ball.
   - The far field sits at N = 1.036 in this periodic box, so "binding" carries a reference uncertainty of a few percent. The ratios themselves do not.

**Reading.**
- **The kill rule fired. The engine, under the adopted rules, does not count a bound pattern's binding energy once.** Under the adopted rule its far field overshoots ħω by 13% at the registered setting, and by 0.4–2.6% with weak-field matter.
- **Part of the cause is identified, post hoc.** A body held on fixed places, whose draw is its ticking, responds to outside wells with weight 1/(1 + U_self), not GR's 1. GR's bodies shrink in these coordinates, which keeps the response at 1. ED's law would do the same for a body that shrank, so a body that can adjust is the fix to try. The rest of the gap is unresolved.
- **The pattern rule Allen chose is closer to measured physics than energy-only at every setting**, but this run does not show it to be right.
- **This sharpens an open item already on the list:** bodies held by rule, not supported (Run 30, "whether stress pulls").
  - At physical scales $U_{\rm self}$ combines each clock's own dip (about 0.3/p_s ≈ 10⁻⁶ at p_s ≈ 4×10⁵) with a body's own potential: Earth 7×10⁻¹⁰, Sun 2×10⁻⁶, a neutron star about 0.2.
  - **Extrapolating from a ball held on lattice places** (not computed for any real body), a neutron star's active mass would respond to outside wells about 17% weakly. Strong-field pulsar tests bound related effects far below that. The PSR J0337+1715 triple bounds the passive-mass analogue to about 2×10⁻⁶.
  - So if ED's bodies really cannot adjust, that would very likely be excluded. A body that adjusts as GR's does avoids it.
- **Next, to register:**
  - the same test with a ball whose size scales with the outside well (shrinking by $e^{-U_{\rm ext}}$), to see whether that restores a response of 1 and closes the gap;
  - then a supported body, with stresses.
