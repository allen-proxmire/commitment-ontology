## 9y. Run 32: can the adopted rules make a horizon? (and do ED's radiation papers apply?)

*19 October 2026. Pre-registered and hashed before any run (`horizon/PREREG_32.md`, 05:47 UTC), with a kill rule. (step 2: whether the surface where possibility runs out is a horizon).*

**Prior record (checked first).** Much of this was already found in other ED models. This run puts it on the adopted rules.
- **Attempt B, B-39** (O165, W103, W104): the body's slowing clock cuts its own draw. "The brake wins by a factor of ~30… the bandwidth seal OPENS". The clock slows as a power law, $t^{-0.55}$ to $t^{-0.67}$; "nothing freezes."
- **MODEL_RESULTS, result 17:** "ED's ingredients make neither [a horizon] nor an exact permanent cut."
- **Attempt C, C-O39:** "the draw is self-limiting… so clocks never reach zero."
- **`ED_Acoustic_Metric_Curvature.md`:** "κ = 0… ED horizons are generically cold."
- **ED's radiation papers** (039, 047, 050, 052; `BH_Thermal2Pi`; `ED10_Horizons`) all assume a horizon with κ > 0.

**Theory** (`theory32.py`, before any run).

(a) **The surface where possibility runs out is cold.**
- Outside a static body the outflow deficit is harmonic, $z=z_0-A/r$, and the logarithmic outflow gives $P=p_s(e^{z/c}-1)$. With $Q=P_0/p_s$ and $U=M/r$:
$$
N(r)=\frac{(1+Q)\,e^{-M/r}-1}{Q},\qquad N=0\ \text{at}\ r_e=\frac{M}{\ln(1+Q)} .
$$
- N falls to zero linearly. With the pattern rule's $g_{rr}=N^{-2}$, the time–radial metric is $-f\,dt^2+dr^2/f$ with $f=N^2$, a double zero. So
$$
\kappa=\tfrac12 f'(r_e)=N\,N'\big|_{r_e}=0,\qquad T=\kappa/2\pi=0 .
$$
- For Q = 64, 2000 and 2.3×10⁴:
  - κ is 10⁻¹⁸ to 10⁻²³ (rounding)
  - the proper distance to the surface grows as ln(1/ε), so it is infinite
  - the areal radius r/N diverges
  - a radial light ray reaches it at finite affine parameter
- This is an extremal-type end with infinite area and zero temperature, the same verdict as ED's acoustic-metric arc.

(b) **A static body cannot make that surface.**
- Its draw is its ticking (presence clock). For a thin shell of bare compactness μ (the U it would make if its clocks did not slow), the shell's clock rate solves
$$
N_b=\frac{(1+Q)\,e^{-\mu N_b}-1}{Q} .
$$
- At $N_b=0$ the right side is 1, so the root lies in (0, 1).
- More generally, outside matter $\tfrac16\nabla^2z=-\bar s<0$, so z is smallest on the matter and positive outside it.
- U at the surface grows only like ln μ, toward ln(1 + Q) ≈ 10 at Q = 2.3×10⁴, and never reaches it (figure, panel a).

**Engine check.** ED's radius-3 ball with k = 8, 32 and 128 commitments per pair, at $p_s$ = 1, $P_0$ = 64, box 40. Each run is 25,000 ticks, read over the last 12,000. The engine is unchanged.

| k | draw (theory) | mean P at the ball (theory) | lowest ball place | N at r = 4 (theory) | lowest shell P, r = 4–15 | lowest outflow outside the ball |
|---|---|---|---|---|---|---|
| 1 (Run 26) | 8.54 (8.55) | — | — | — | — | — |
| 8 | 20.05 (19.86) | 7.43 (7.36) | 4.19 | 0.310 (0.309) | 19.9 | 2.67 |
| 32 | 29.11 (28.20) | 2.70 (2.61) | 1.01 | 0.183 (0.186) | 11.7 | 1.31 |
| 128 | 36.49 (33.84, not converged) | 0.96 (0.83) | 0.12 | 0.113 (0.113) | 7.2 | 0.32 |

- **K32 (kill rule: no zero-clock surface outside matter): pass.**
  - Shell means at r = 4–15 are 7.2 or more, against the 0.5 threshold. The lowest single place at r = 4 holds 4.46.
  - Places without pairs, including those inside the ball's radius, keep an outflow of at least 0.32, against 0.059. The deepest of them holds 0.35 (N ≈ 0.005).
- **T32a (theory): pass.** At k = 8 and 32 the draw agrees to 1% and 3%, P at the ball to 1% and 3%, and N(r = 4) to 0.004.
- **T32b (saturation): as registered.** At k = 128 the draw is 36.5, below 45.
- **The draw saturates.** Sixteen times the commitments (8 → 128) gives 1.8× the draw. Per commitment the draw falls from 8.5 to 2.5, 0.91 and 0.29 (figure, panel b). Inside the ball P falls toward zero, to 0.12 at the lowest place, but outside it the clock rate never reaches zero.

![Run 32](figures/32_horizon.png)

**Reading.**
1. **Under the adopted rules a static body never makes a horizon.** Its draw is its ticking, so a deepening well slows the very draw that digs it. This is the Tolman self-consistency of Run 30, seen at full depth, and it matches Attempt B's B-39 and Attempt C's C-O39 on a different engine.
2. **Even the idealised end, where possibility runs out, is at zero temperature.** So ED's radiation papers, which derive $T=\kappa/2\pi$ from a horizon with κ > 0, do not apply to the engine's static solutions. A static engine body has no horizon, so standard Hawking radiation does not arise. The engine models no quantum fields, and its check ran only at Q = 64.
3. **What that leaves.**
   - **An ultra-compact body with a surface at finite redshift.** For $U_b>\tfrac12$ (thin shell: μ ≳ 0.9) the exponential metric's light ring, at $r=2M$ or U = ½, lies outside the body, so Run 28's shadow (+4.6%) and ringdown (about 4% low) apply. The registration's "$U_b>2$" was wrong.
   - **The missing surface glow of Sgr A*** (Attempt 03's closure, 25× over the limit at redshift e) applies to that surface. Whether a very large redshift, with its long equilibration time, escapes the steady-state argument has not been computed. The record does not try it either.
   - **Collapse.** Barceló et al.'s horizonless (quasi-Hawking) radiation needs a surface redshift that grows exponentially in time. Attempt B's B-39 found a power law. Not run here, and on Run 31's diffusive medium a collapse would in any case run at the diffusion rate.
4. **Information.** With no horizon there is nothing for information to be lost behind. ED's "records, not reversibility" reading is not needed for static solutions. It would matter only if a rule change brings back a horizon.
