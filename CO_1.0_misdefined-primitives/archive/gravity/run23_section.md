## Run 23: does matter become light, and β stay 1, as the crossover grows? (Candidate A′)

**Question.** In Run 22 the theory traced both Candidate A's success (β = 1) and its failure (a clock's own draw dips its own places by an order-one amount) to one exponential amplification. Candidate A′ keeps both rules, but lets the medium stay linear up to a holding $p_s$ and turn logarithmic only above it:

$$
f(P)=c\,\ln\!\Big(1+\frac{P}{p_s}\Big),\qquad c=\frac{0.99}{\ln(1+1/p_s)}\approx0.99\,p_s .
$$

If the theory is right, a clock's self-dip falls as about $1/p_s$ (matter becomes light), while β still tends to 1 once $P_0\gg p_s$. This run tests both cheaply, with a kill rule fixed in advance (`PREREG_23.md`, hashed before any run; `ps_run.zip`).

**Method.**
- **Self-dip:** box 36, no matter, 27 lone probe clocks on a grid 12 apart (designs hold H and 2H, alternating). $P_0=64\,p_s$, $p_s$ = 1, 4, 16, 64; 16,000 ticks, read the last 10,000. The dip is $1-P_{\rm own}/P_{\rm ref}$, with the reference ≥ 5 places from every probe.
- **β:** Run 22's matter-free method, unchanged, at $p_s$ = 4, 16, 64 and $P_0/p_s$ = 64, 256, 1024.

**Kill rule.**
- **K1:** the slope of ln(dip) against ln $p_s$ over 4–64 must be ≤ −0.7.
- **K2:** for each $p_s$, β must rise with $P_0/p_s$ and land within 0.003 of 1 at 1024.
- If either fails, the family is dead and clock-rule tuning stops.

**Results.**

| $p_s$ | 1 | 4 | 16 | 64 |
|---|---|---|---|---|
| dip, design 1 (theory) | 0.186 ± 0.003 (0.202) | 0.075 ± 0.002 (0.081) | 0.020 ± 0.001 (0.024) | 0.0060 ± 0.0008 (0.0064) |
| dip, design 2 (theory) | 0.105 ± 0.004 (0.117) | 0.042 ± 0.003 (0.043) | 0.008 ± 0.002 (0.012) | 0.0039 ± 0.0006 (0.0032) |

| β − 1 | $P_0/p_s$ = 64 | 256 | 1024 |
|---|---|---|---|
| $p_s$ = 4 | −0.0059 | −0.0011 | **−0.0002** |
| $p_s$ = 16 | −0.0073 | −0.0017 | **−0.0004** |
| $p_s$ = 64 | −0.0077 | −0.0019 | **−0.0005** |

β agrees with the theory to 0.0003 or better everywhere (errors below 0.00013, χ²-scaled).

| test | registered | measured | verdict |
|---|---|---|---|
| K1 | slope ≤ −0.7 | **−0.94 ± 0.04** (theory −0.92) | **pass** |
| K2 | β rises; \|β − 1\| ≤ 0.003 at 1024 | rises for every $p_s$; −0.0002, −0.0004, −0.0005 | **pass** |

**Reading.**
- **Matter becomes light as the crossover grows, and β stays 1.** Both kill tests pass, as the theory predicted. The self-dip falls about as $0.3/p_s$, and β depends only on $P_0/p_s$.
- **A correction to Run 22.** A lone clock at $p_s$ = 1 dips 0.186, not 0.24–0.32. Run 22's numbers were taken against the box mean, among 100 probes 2.5 apart, so they include the probes' collective depletion. For lone clocks the theory matches design 1 to 7–18%; design 2 is noisier (−38% to +22%, within about 2σ). Run 22's "underestimates by 1.5×" was that crowding. Run 22's T2 failure stands (it was measured against the shell ambient). Its size, a 4–6% design gap, roughly fits the self-dip difference of 0.08 between the designs here.
- **What this does not show.** It is a necessary condition, measured as a proxy: the self-dip of a lone clock. It is not the registered clock check in a well. Two things remain:
  - **The clock check in a well:** do two clock designs agree near matter at large $p_s$? Expected design gap ≈ the self-dip difference, about 1.2% at $p_s$ = 16 and 0.2% at 64.
  - **Real clocks** (~10⁻⁶) need a design gap of $\approx(0.1\text{–}0.2)/p_s\lesssim10^{-6}$, i.e. $p_s\gtrsim2\times10^5$, and Nordtvedt then needs $P_0/p_s\gtrsim2{,}000$. That is reachable only by extrapolating the measured scaling.

![Run 23](../figures/23_crossover.png)

*Note (30 October, Reading I18c):* R1 is amended beyond first order (a pure logarithm above p_c ≡ (1/p_s + 1/P∞)⁻¹, joined smoothly to f = 0.99P below). Results here that rest on g ≈ p_s/P, or on R1's curvature above the crossover, belong to the original R1; most had already lapsed as gravity results with ε = 0 in gravity. Where p_s sets a scale, read p_c.
