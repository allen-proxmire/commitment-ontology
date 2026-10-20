## 9m. Run 20: β measured directly in ED's engine

**Question.** Run 10 reached Mercury's perihelion only with the multiplicative budget ($N=e^{-U}$, β = 1). Run 19 inferred, from knots of different shapes, that ED's engine as adopted makes linear wells ($N=1-U$, β = ½). This run measures β the way Run 10 measured it on its lattice, on one source shape, in the engine. Pre-registration: `PREREG_20.md` (`beta_run.zip`).

**Method.**
- ED's benchmark ball (radius 3) in the adopted engine (box 60, density 8, 9,000 ticks), each of its pairs holding k = 1, 2, 3 reserved commitments. Seeds 1 and 2, against seed-matched controls.
- With $U=D\,g(r)$ at first order, the clock rate $N=1-U+b_2U^2$ gives, shell by shell,

$$
\frac{\delta_k(r)}{D_k}=g(r)-b_2\,g(r)^2D_k,\qquad \beta=\tfrac12+b_2
$$

  So a straight line of δ/D against the measured draw D, at each shell r = 5–12, gives $b_2$. Shells are weighted by inverse variance.

**Results.**

| k | draw D (seeds 1 / 2) | δ at r = 5 | δ at r = 8 |
|---|---|---|---|
| 1 | 15.13 / 15.26 | 0.136 / 0.139 | 0.071 / 0.071 |
| 2 | 23.21 / 23.45 | 0.208 / 0.212 | 0.109 / 0.111 |
| 3 | 28.28 / 28.56 | 0.254 / 0.257 | 0.133 / 0.134 |

- Per shell, $b_2$ = 0.030, −0.004, −0.005 at r = 5, 6, 7, where the second-order term is largest. The farther shells are noisier and lean negative.
- Weighted: **$b_2$ = −0.028 ± 0.025** (the error is the larger of the formal error, 0.021, and the seed-to-seed spread; seeds alone give −0.005 and +0.044).

$$
\beta=0.47\pm0.03\qquad\Rightarrow\qquad\text{Mercury: }42.98''\times\frac{4-\beta}{3}=50.5''\ \text{per century},\qquad\eta=4\beta-\gamma-3=-2.1
$$

| Prediction | Expected | Measured | |
|---|---|---|---|
| $b_2$ | 0.00 ± 0.10 (linear well) | −0.028 ± 0.025 | **pass** |
| the multiplicative budget | $b_2$ = 0.50 | excluded by about 20 standard errors | |

**Reading.**
- **Confirmed directly: ED's engine with the adopted rules has β ≈ ½.** The well per unit of draw does not shrink as the source grows (figure, panel a); a multiplicative well would have shrunk by 7–15% at these strengths.
- With the pattern rule (γ = 1) that puts Mercury at about 50.5″ per century (observed 42.98″) and the Nordtvedt parameter at about −2 (σ = 4.4×10⁻⁴). **Both excluded.**
- **Where this came from:** Runs 14–15's rules were adopted on first-order evidence. Run 10's second-order requirement was never carried into those tests. §11b now makes it a standing check.
- **Why it is structural:** while clocks count passing possibility and possibility wanders on its own, the passing count is a linear field whatever the hop rule (§11c). The fix must change what clocks read, not only how possibility wanders.

![Run 20](figures/20_beta.png)
