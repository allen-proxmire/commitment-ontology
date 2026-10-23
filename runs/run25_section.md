## Run 25: the closing checks for Candidate A′ (a well where Mercury's band holds; Nordtvedt directly)

**Question.** Candidate A′ was adopted provisionally (§3). Two of its open checks can be run now:
- **(a)** Do matter wells obey the medium's equation of state where β is inside Mercury's band?
- **(b)** Does the medium's β get within reach of lunar laser ranging?

Pre-registered with kill rules (`PREREG_25.md`, hashed before any run; `close_run.zip`).

**Method.**
- **(a) Wells.** Run 22's recording engine, unchanged, with $p_s$ set first: box 40, CO's ball, $P_0/p_s$ = 256, seed 2, 20,000 ticks, read over the last 12,000.
  - $p_s$ = 4, $P_0$ = 1024: control, k = 1 and 2.
  - $p_s$ = 16, $P_0$ = 4096: control, k = 4 and 8.

  Each shell point is compared with the medium's curve (a quartic fit of z against ln ρ, from uniform boxes over $\rho=P_0e^u$, $u\in[-1,\,0.15]$) via $\Delta\ln P=(z_i-z_{\rm unif}(P_i))/(dz/d\ln\rho)$.
- **(b) Nordtvedt.** Run 22's matter-free β method, unchanged, at $p_s$ = 4 and 16, with $P_0/p_s$ = 2048 and 4096 (1024 from Run 23). The target is LLR's 2σ, $|\eta|=4|\beta-1|\le8.8\times10^{-4}$, i.e. $|\beta-1|\le2.2\times10^{-4}$.

**Results (a).**

| $p_s$ ($P_0$) | points | max \|Δ ln P\| | r.m.s. | depth at r = 4 | draw | K-a |
|---|---|---|---|---|---|---|
| 4 (1024) | 36 | 0.0013 | 0.0003 | 0.15, 0.24 | 14.8, 23.2 | **pass** |
| 16 (4096) | 36 | 0.0015 | 0.0003 | 0.16, 0.25 | 58.2, 90.2 | **pass** |

The wells are shallower than Run 22's (0.15–0.25 against 0.41–0.57). The medium diffuses slowly at this ratio, so they were still filling in. That makes the test coarser, as registered. The gap grows slightly with depth (to −0.0014 at the deepest shell), the same near-sink trend Run 22 showed.

**Results (b).** Errors are χ²-scaled.

| | $P_0/p_s$ = 1024 | 2048 | 4096 |
|---|---|---|---|
| $p_s$ = 4: β − 1 (theory) | −1.6 ± 0.4 ×10⁻⁴ (−1.9) | −5.9 ± 3.6 ×10⁻⁵ (−7.2) | −6.4 ± 3.0 ×10⁻⁵ (−2.6) |
| $p_s$ = 16: β − 1 (theory) | −4.2 ± 0.2 ×10⁻⁴ (−4.1) | −1.96 ± 0.19 ×10⁻⁴ (−2.01) | **−1.06 ± 0.06 ×10⁻⁴** (−0.98) |

| test | registered | measured | verdict |
|---|---|---|---|
| K-a, $p_s$ = 4 | max ≤ 0.005, r.m.s. ≤ 0.003 | 0.0013 / 0.0003 | **pass** |
| K-a, $p_s$ = 16 | max ≤ 0.005, r.m.s. ≤ 0.003 | 0.0015 / 0.0003 | **pass** |
| K-b, $p_s$ = 4 | \|β − 1\| falls at each step, and ≤ 2.2×10⁻⁴ at 4096 | 6.4×10⁻⁵ at 4096 (η = −2.5×10⁻⁴), but 2048 → 4096 does not fall (5.9 → 6.4 ×10⁻⁵) | **FAIL as registered** |
| K-b, $p_s$ = 16 | the same | falls 4.2 → 1.96 → 1.06 ×10⁻⁴; η = −4.2×10⁻⁴ | **pass** |

**Reading.**
- **The wells follow the medium where Mercury's band holds.** Matter wells at $P_0/p_s$ = 256 obey the matter-free equation of state to 0.0015 in ln P. The wells' β is therefore the medium's (to T1b's resolution, about 0.01 in β), and the medium's β is inside Mercury's band here.
- **Nordtvedt is met in the engine at $P_0/p_s$ = 4096.**
  - At $p_s$ = 16, β − 1 = −1.06×10⁻⁴, as the theory said beforehand (−0.98×10⁻⁴). That gives η = −4.2×10⁻⁴, about 1σ from lunar laser ranging's zero.
  - At $p_s$ = 4, |β − 1| is already 6×10⁻⁵ at 2048 and 4096, η = −2.5×10⁻⁴.
- **The registered fail at $p_s$ = 4 is in the kill rule as written, not in the medium.** The "falls at every step" clause cannot be met once the deviation is below the measurement error: the 2048 and 4096 values agree, with a difference of 0.5 ± 4.7 ×10⁻⁵. Both are well inside the bound. It stays a fail as registered.
- **For large $p_s$ the trend is the theory's** $\beta-1\approx-0.45\,p_s/P_0$. Nordtvedt at 2σ then needs $P_0/p_s\gtrsim2000$, which is what the adoption's constraint assumed.

**Correction (18 October, after Run 28): only the β part of Nordtvedt was tested.** The full Nordtvedt parameter, as set out in ED_Attempt_01 (C206), is

$$
\eta_N=4\beta-\gamma-3-\tfrac{10}{3}\xi-\alpha_1+\tfrac23\alpha_2-\tfrac23\zeta_1-\tfrac13\zeta_2 .
$$

- **What Runs 22–25 covered:** they measured β; γ is put in by the pattern rule.
- **What was never tested:** the preferred-frame terms (α₁, α₂, ξ; the lattice has a universal tick) and the sourcing terms (ζ₁, ζ₂: how motion, pressure and gravitational energy source gravity).
- **Why that matters.** ED_Attempt_01 (C207–C208) showed that a budget that simply counts its sources gives η_N = 10/3 (rest mass only) or 17/6 (everything counted linearly). That is more than 10⁴ times the lunar-ranging limit. Attempt 1 then adopted GR's weights by hand (RD37).
- **Untested in the engine.** Attempt 1's result is for a *linear* budget. Candidate A′ is not linear, and its sourcing ("active mass = redshifted draw", Runs 19 and 26) has not been measured against GR's weights. Whether it meets the same wall is open.
- **The claim "Nordtvedt is met" is withdrawn as stated.** What Run 25 shows is that the β contribution to η_N is within lunar ranging's bound at $P_0/p_s$ = 4096.

![Run 25](figures/25_closing.png)
