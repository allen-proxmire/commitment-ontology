## Run 21: probe of Candidate A (stability, and a first look at β)

**Question.** Candidate A (§6) makes two changes:
- possibility's outflow from a place grows as the logarithm of its holding
- a clock counts possibility *present*, not passing

Does the medium stay stable (Run 17's medium froze), and does β move from ½ toward 1? This is a probe before the full test. Predictions were written first (`PROBE_21.md`), but it was not pre-registered against the standing checks.

**Rules.**

$$
p(P)=\frac{c\,\ln(1+P/p_s)}{P},\qquad f(P)=P\,p(P)=c\,\ln(1+P/p_s),\qquad p_s=1,\ \ c=\frac{0.99}{\ln 2}
$$

A commitment holds until $\sum_{\rm ticks}(P_a+P_b)$ reaches $H=\hbar\cdot2\cdot\text{dens}$, so its rate is ∝ P. Everything else is the adopted engine.

**Method.** Box 40, seed 1, 20,000 ticks, read over the last 12,000. ED's ball at k = 1, 2, 3 commitments per pair, plus a control, at densities 8 and 32 (`engine21.py`).

**Results.**
- **Stable.**
  - Mean P is conserved, with no freezing or clumping.
  - Var/mean of P holds at 2.0 (density 8) and 3.2–3.6 (density 32). The prediction was "near 2.2" at density 8; that is the continuous-time theory's value, and the engine's discrete-time medium sits about 9% lower.
  - The maximum stays bounded: 41 (density 8) and 101 (density 32) over the run.
- **Draws:** 7.97, 10.70 and 12.40 per tick at density 8; 8.49, 11.89 and 13.92 at density 32.
- **The wells are deep.** The clock shortage at r = 4 is 0.41, 0.52 and 0.57 at density 8, against 0.18 for the adopted engine's ball. The medium diffuses about 6× (density 8) to 22× (density 32) more slowly, so the same draw digs a deeper well.
- **The written β predictions missed.** `PROBE_21.md` predicted β = 0.94 ± 0.05 (density 8) and 1.00 ± 0.05 (density 32) by Run 20's method. That method gave **0.805** and **1.080**. The method is a weak-field expansion ($N=1-U+b_2U^2$) and is not valid in wells this deep: its per-shell b₂ runs from +0.33 to −0.43 at density 8, and from 0.41 to 0.64 at density 32.
- **After the data were seen, the fit was switched to a deep-well fit:**

$$
N=(1-qU)^{1/q},\qquad \beta=1-q/2,
$$

  with q chosen so that the well's shape is the same at all three strengths. This gave **β = 1.01 ± 0.04** (density 8) and **0.96 ± 0.06** (density 32). The standard engine's Run 20 data give 0.55–0.60 by the same fit.

**Reading (written after Run 22's theory; see Run 22).**
- Stability passed.
- The deep-well fit's numbers were **partly luck**. Run 22's zero-range theory was written after this probe, so these are postdictions, not predictions. With no fitted parameter, it reproduces Run 21's wells: the draws to 1.6% and the profiles to within 0.011 at every shell from 4 to 15. On those same wells it says the deep-well fit should give 0.93 (density 8) and 1.02 (density 32). That fit summarises shape; it is not the weak-field β. Run 22 measures β properly.
