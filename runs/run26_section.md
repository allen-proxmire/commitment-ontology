## 9s. Run 26: two bodies under the adopted rules (Run 19's checks, and whether wells multiply)

**Question.** Run 19 found that in the old engine a well follows its body's draw, wells combine **additively** in the clock rate (β = ½), and two bodies redshift each other's draws. Under Candidate A′, ln N should follow the draw, and two wells should **multiply**:

$$
N_{AB}=N_A\,N_B\quad(\beta=1),\qquad\text{not}\qquad N_{AB}=N_A+N_B-1\quad(\beta=\tfrac12).
$$

This is Run 10's multiplicative budget, now with two bodies on the event layer. Pre-registered: `PREREG_26.md`, hashed before any run (`twowell_run.zip`).

**Method.**
- **Bodies.** A is ED's ball of radius 3 (54 pairs), centred at (13, 20, 20). B is a ball of radius 4 (114 pairs), centred at (27, 20, 20). The two share no places.
- **Engine.** Run 22's recording engine, unchanged, with $p_s$ = 1 and $P_0$ = 64 (measured β = 0.9996). Box 40, seed 1.
- **Runs.** ctrl, A, B and AB; 50,000 ticks, read over the last 20,000 in two halves.
- **Clock rate.** $N=\bar P/\langle\bar P_{\rm ctrl}\rangle$.
- **W2 fit.** The fields are binned in (x, ρ), where ρ is the distance from the axis through both centres. Each solo well is scaled by its body's draw ratio in the pair, $s_X=D_X^{AB}/D_X^{\rm solo}$, giving

$$
M_\times=s_A\ln N_A+s_B\ln N_B,\qquad M_+=\ln\!\big(1+s_A(N_A-1)+s_B(N_B-1)\big),\qquad \ln N_{AB}-M_+=f\,(M_\times-M_+)
$$

  f = 1 means the wells multiply; f = 0 means they add.

**Results.**

| | A (radius 3) | B (radius 4) |
|---|---|---|
| draw, solo | 8.54 | 14.55 |
| draw in the pair (ratio $s$) | 8.34 (0.976) | 14.34 (0.986) |
| predicted $s$ from the solo fields | 0.975 | 0.987 |
| depth per unit draw, $a/D$ (prediction $y'=0.695$) | **0.690** | **0.689** |
| outflow amplitude (exact; code check) | 1.008 | 0.990 |

| test | registered | measured | verdict |
|---|---|---|---|
| W1 | $a_A/a_B=1.00\pm0.02$, with $g$ per unit draw and prediction $a=0.695$ | as written: $a_A/a_B$ = 0.588; depth per unit draw: ratio **1.001** (halves 1.017, 0.986), each 0.69 | **specification self-contradictory (a registration error); see below** |
| W2 (kill) | f ≥ 0.8; prediction 1.00 ± 0.10 | **f = 0.91 ± 0.07** (halves 1.00, 0.88). That error is understated: see the second seed below, where both seeds give 1.12 ± 0.19 | **pass** |
| W3 (reported) | $s$ measured against predicted | 0.976 / 0.975 (A), 0.986 / 0.987 (B) | **agrees to 0.2%** |

**W1, as registered, cannot be scored cleanly.**
- **The flaw.** $g$ was defined "per unit draw". That makes the fitted $a$ equal to $y'\times D$, so the registered prediction ($a$ = 0.695 for both bodies) and the registered pass mark ($a_A/a_B$ = 1) could not both hold.
- **As literally written,** $a_A/a_B$ = 0.588 is a fail.
- **The consistent reading** is $a/D$, the standing check's "A ÷ draw the same for every body". Then the two bodies agree to 0.1%, and both match the medium's measured slope (0.695) to 0.8%.
- W1 is recorded as a registration error with that consistent result beside it, not as a pass.

**W3's registered solver** (plain fixed-point iteration) oscillated for B. The same equation solved by bisection gives the values in the table.

**Reading.**
- **Two different bodies' wells multiply.** Over two seeds the two-body field sits at f = 1.12 ± 0.19, where 1 means multiplying and 0 means adding; adding is excluded at about 6σ. Along the axis between the bodies the additive rule overshoots visibly; the multiplicative one does not (figure, panel b).
- **This is the multiplicative budget that Run 10 put in by hand and Run 19 found missing.** Under the adopted rules it now comes out of the event layer for two bodies.
- **Each well follows its own body's draw in ln N.** Depth per unit draw is the same for a radius-3 and a radius-4 body to 0.1%, and equals the medium's measured slope.
- **Each body redshifts the other's draw** by the amount the solo fields predict (to 0.2%). So active mass is still the redshifted draw, as in Run 19.
- **Limits.** One seed; f's halves differ by 0.12, so the error is dominated by noise. And $p_s$ = 1, not the large $p_s$ the adoption requires: two-body combination depends on β, which here is 0.9996, not on clock self-dips.

**Second seed (Run 26b; pre-registered in `PREREG_26b.md` before its runs, with W1's specification corrected to depth per unit draw).**

| | seed 1 | seed 2 | both |
|---|---|---|---|
| W1: $a/D$ for A, B (ratio) | 0.690, 0.689 (1.001) | 0.694, 0.685 (**1.013**, pass) | |
| W2: f (within-seed error) | 0.91 ± 0.07 | **1.29 ± 0.09** (pass) | **1.12 ± 0.19** |
| W3: $s_A$ measured vs predicted | 0.976 / 0.975 | 0.980 / 0.972 | |
| W3: $s_B$ measured vs predicted | 0.986 / 0.987 | 0.983 / 0.985 | |

- **Both seeds pass the kill rule** (f ≥ 0.8).
- **The within-seed errors were too small.** The two seeds differ by 0.37, about four times the error each seed gave itself (half-to-half and bin bootstrap). Those estimates miss the slow, run-level fluctuations of the wells, so the honest error on f is the seed-to-seed spread.
- **Pooled: f = 1.12 ± 0.19.** Adding (f = 0) is excluded at about 6σ, and multiplying (f = 1) agrees within 1σ. A third seed or a longer read would tighten this.

![Run 26](figures/26_twowell.png)
