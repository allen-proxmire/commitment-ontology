## 9q. Run 24: do clocks of different make agree once the crossover is large?

**Question.** Run 22's registered clock check failed at $p_s=1$: two clock designs (hold H and 2H) disagreed by 4–6% near matter. Run 23 showed a lone clock's self-dip falls as $p_s^{-0.94}$. Does the disagreement fall with it? This is pre-registered with a kill rule (`PREREG_24.md`, hashed before any run; `clockuni_run.zip`).

**Why a uniform-media test, not a well.** A well test had been proposed at $p_s$ = 4 and 16. Working out its resolution before registering showed it could not work: with Run 22's layout the design ratio in a well carries about ±0.02 per 2 hours, against expected gaps of 0.024 and 0.007.

Near matter a clock mostly just sits in less possibility, and Run 22's T1b showed the wells obey the uniform medium's equation of state. So the same clocks are compared in two uniform media, with check C tying the result to Run 22's well.

**Method.**
- **Media:** box 36, no matter, at ambient $P_0=64\,p_s$ and $0.6\,P_0$.
- **Clocks:** 216 probe clocks on a 6 × 6 × 6 grid with spacing 6, two designs on a checkerboard. Their H is fixed by the richer medium, so they are identical in both.
- **Runs:** $p_s$ = 1, 4, 16; seeds 1 and 2; 20,000 ticks, read over the last 15,000. The vectorised probe step is bit-identical to engine22's loop.
- **Estimator:** with ambient shortage $\varepsilon=1-\bar P_{\rm amb}({\rm low})/\bar P_{\rm amb}({\rm high})\approx0.40$,

$$
\kappa_j=\frac{1-\bar r_j({\rm low})/\bar r_j({\rm high})}{\varepsilon},\qquad g=1-\frac{\kappa_1}{\kappa_2}.
$$

  Errors are bootstrapped over probes.

**Results.**

| $p_s$ | κ, design 1 (theory) | κ, design 2 (theory) | design gap g (theory) |
|---|---|---|---|
| 1 | 0.895 ± 0.002 (0.877) | 0.948 ± 0.002 (0.929) | **0.056 ± 0.003** (0.056) |
| 4 | 0.960 ± 0.002 (0.951) | 0.978 ± 0.002 (0.974) | **0.018 ± 0.002** (0.024) |
| 16 | 0.988 ± 0.001 (0.986) | 0.993 ± 0.001 (0.993) | **0.0049 ± 0.0011** (0.0071) |

| test | registered | measured | verdict |
|---|---|---|---|
| K | slope of ln g against ln $p_s$ (1–16) ≤ −0.5 | **−0.85 ± 0.07** (theory −0.74) | **pass** |
| C | $\kappa_1/\kappa_2$ at $p_s$ = 1 within 0.03 of Run 22's well (0.951) | 0.944 | **pass** |

**Reading.**
- **Clocks of different make converge as the crossover grows.** The gap between designs falls as $p_s^{-0.85}$, a little faster than the theory's −0.74, and both designs approach κ = 1. At $p_s$ = 1 the uniform test reproduces the well's design ratio (0.944 against 0.951) and the theory's gap exactly (0.056). So it measures what Run 22's well measured.
- **The theory's absolute κ runs about 2% low at $p_s$ = 1.** It is close from $p_s$ = 4 up, and the gap is what the kill rule tests.
- **What real clocks require (an extrapolation of three points over five decades).** Agreement to ~10⁻⁶ needs $0.056\,p_s^{-0.85}\lesssim10^{-6}$, i.e. **$p_s\gtrsim4\times10^5$**. With Run 23's β, Nordtvedt then needs $P_0\gtrsim2000\,p_s\approx10^9$ units of possibility per place.
- **Where Candidate A′ now stands.** It has passed every test it has faced:
  - **β = 1:** the medium's β is inside Mercury's band once $P_0/p_s\gtrsim256$ (Runs 22–23).
  - **The wells:** they obey the medium's equation of state (Run 22, $p_s$ = 1).
  - **Clock universality:** clocks of different make converge as $p_s$ grows (Run 24).
  - **Carried over unchanged:** the first-order checks of how patterns and knots move in a given clock field (Runs 16–18b), since Candidate A′ changes only how the field is made.

  **Not yet tested:**
  - a well at large $p_s$ and $P_0/p_s\gtrsim256$, where Mercury's band holds
  - Nordtvedt directly
  - whether ED accepts a place holding ~10⁹ units with a crossover at ~10⁵

![Run 24](figures/24_clocks.png)
