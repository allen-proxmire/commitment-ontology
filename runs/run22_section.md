## 9o. Run 22: Candidate A against the standing checks

**Question.** Does Candidate A deliver β = 1 while keeping every first-order result?

Pre-registered: `PREREG_22.md` was hashed before any run (in `ratio_run.zip`). It has two dated amendments:
- **Amendment 1** (the well test) was written before any Run 22 output existed.
- **Amendment 2** (the fall test) was written after the smooth-field code check had failed, but before any engine field was used in a pattern run.

A dated note (`NOTE_22_clocks.md`) recorded a prediction for the density-32 clocks. It was hashed after those runs had started but before any of them had finished.

### Theory (written after Run 21's probe and before Run 22; no parameter fitted to any run)

**Exact, by conservation.** Write the mean outflow from a place as $z_x=\langle f(P_x)\rangle$, with $f(P)=c\ln(1+P)$. In the steady state, inflow (the neighbours' outflows, one-sixth each) balances outflow, matter's draw $s_x$ and the uniform return $\bar s$:

$$
\tfrac16\sum_{y\sim x}z_y-z_x=s_x-\bar s .
$$

**The outflow is a linear, unscreened field for any hop rule.** This is §11c's structural fact. Under the flow clock, the clock read this field directly, which is why β = ½.

**What the presence clock reads.** It reads $\langle P\rangle$, a *nonlinear* function of z. If each place is in local equilibrium, it holds n units with the zero-range weights

$$
\pi_z(n)\propto\frac{z^n}{\prod_{j=1}^{n}f(j)},\qquad \langle P\rangle=R(z).
$$

**β.** Let $y(z)=\ln R(z)$, and write the outflow deficit as $\Delta z=z_0-z$ and the linear field, normalised, as $U=y'(z_0)\,\Delta z$. Expanding $N=R(z)/R(z_0)=e^{\,y(z)-y(z_0)}$ with $a=y''/(2y'^2)$:

$$
N=e^{-U+aU^2+\dots}=1-U+\big(\tfrac12+a\big)U^2+\dots\ \Rightarrow\ b_2=\tfrac12+a,\quad \boxed{\beta=\tfrac12+b_2=1+\frac{y''}{2\,y'^2}}
$$

This is the β of an ideal clock that reads the ambient $\langle P\rangle$. **β = 1 exactly when ln P is a straight line in the outflow**, which is the exponential clock. For $f=c\ln(1+P)$ that holds only when P is large, where $z\approx c\ln P$. The same formula can be read off a measurement with no theory at all. Fill a box uniformly at density ρ, measure z(ρ), and fit $z=z_0+g_1x+g_2x^2+g_3x^3$ with $x=\ln(\rho/P_0)$; then $\beta=1-g_2/g_1$.

**The wells, self-consistently.** Each pair renews at rate $(P_a+P_b)/H$. Solving the exact equation on box 40 with $\langle P\rangle=R(z)$ predicts every draw and every shell profile, parameter-free (`theory22.py`).

**Checked against Run 21's probe (postdictions: the theory was written after the probe).**
- draws: within 1.6%
- profiles: within 0.011 at every shell from 4 to 15
- the probe's deep-well fit: the theory says it should have given 0.926 and 1.024, not the 1.01 and 0.96 measured. That fit was demoted to "reported, not tested".

### Method

| set | what | ticks (read) |
|---|---|---|
| wells | box 40, ED's ball (radius 3) stacked k = 1, 2, 3, plus control. Density 8 (seeds 2, 3), 32 (seeds 2, 3), 4 (seed 2) | 20,000 (12,000); 30,000 (15,000) at density 32, which relaxes about 4× more slowly |
| uniform medium | box 20, no matter; ladders of 7–9 densities around P₀ = 4, 8, 16, 32, 64, 128, 512, 2048 | burn max(1500, 6(1+ρ)/c), read 5,000 |
| clocks | control and k = 1 with 100 probe clocks (Run 15's layout; designs hold H and 2H; shells 5–14); densities 8 and 32, seeds 2 and 3 | 20,000 (12,000) |
| patterns | Run 16's code, unchanged, in the k = 1 fields and in the theory's smooth field; released 10 and 14 out along six axes; masses 0.7–2.0 | 16 |

- **Recording.** The engine (`engine22.py`) records the mean outflow and the possibility at hop time, and each place's draw by matter.
- **Code check.** With nothing added, it is bit-identical to Run 21's engine.

### Results

**T1a. β of the medium, from its own equation of state (primary).**

| P₀ | 4 | 8 | 16 | 32 | 64 | 128 | 512 | 2048 |
|---|---|---|---|---|---|---|---|---|
| measured β | 0.8827 | 0.9427 | 0.9754 | 0.9924 | **0.9996** | **1.0015** | **1.0010** | **1.0005** |
| ± (χ²-scaled) | 0.0001 | 0.0003 | 0.0009 | 0.0005 | 0.0004 | 0.0003 | 0.0002 | 0.0001 |
| theory (fixed beforehand) | 0.872 | 0.942 | 0.980 | 0.996 | 1.0006 | 1.0017 | 1.0011 | 1.0004 |
| Mercury (″/century), γ = 1 | 44.66 | 43.80 | 43.33 | 43.09 | 42.99 | 42.96 | 42.97 | 42.97 |
| η = 4(β − 1) | −0.469 | −0.229 | −0.098 | −0.030 | −0.0018 | +0.0061 | +0.0038 | +0.0021 |

- **Mercury's band** (|β − 1| ≤ 0.003): **pass at every P₀ ≥ 64.**
- **β rises from 4 to 32:** every step is positive; 196σ overall. **Pass.**
- **The theory column:** within 0.03 at 4–32. **Pass.**

The engine reproduces the theory's overshoot above 1 near P₀ = 128, which the theory predicted in advance. At low density the theory is close but not exact: it misses by 0.0106 at P₀ = 4 (about 77σ), 0.005 at 16 and 0.003 at 32. That is inside the registered 0.03, but it is the discrete-time engine's medium departing from the continuous-time theory (see T1c).

**T1b. The wells obey the same equation of state (Amendment 1).** Each shell point of every well and control is compared with the uniform medium's curve at the same outflow.

| density | points | max \|Δ ln P\| | r.m.s. | verdict | reported: quadratic estimator (theory curve) |
|---|---|---|---|---|---|
| 8 | 96 | 0.0036 | 0.0007 | **pass** | 0.907 ± 0.003 (0.896) |
| 32 | 96 | 0.0037 | 0.0007 | **pass** | 0.992 ± 0.001 (0.989) |
| 4 | 46 (2 outside the ladders) | 0.0011 | 0.0003 | **pass** | 0.831 ± 0.004 (0.780) |

**The wells obey the matter-free medium's equation of state** to within the band, at densities 4, 8 and 32. The resolution matters. A gap of 0.004 in ln P across the wells' range corresponds to about 0.007–0.01 in β, so T1b ties the wells' β to the medium's at that level, not at Mercury's 0.003. No wells were run at P₀ ≥ 64, where Mercury's band passes.

The one visible trend is at the deepest shells (r = 4, where P/P₀ ≈ 0.43–0.5, k = 2 and 3). There the wells at densities 8 and 32 sit 0.002–0.004 below the uniform curve (figure, panel b). At density 4 the matching points fall outside the ladders and were dropped. The trend looks like an effect near matter's sinks, not a lean medium. It is within the band, and untested.

**T1c. The parameter-free theory.**
- **Draws** (seed means) are within 1.4% of theory: 7.95, 10.66, 12.32 against 8.00, 10.66, 12.21 at density 8, and 8.47, 11.77, 13.88 against 8.59, 11.89, 14.01 at density 32. **Pass.**
- **Profiles at density 32:** max 0.0034, r.m.s. 0.0015. **Pass.**
- **Profiles at density 8:** max **0.0101** against a limit of 0.010 (r.m.s. 0.0043). A **marginal FAIL**: near the ball, k = 2 and k = 3 wells are up to 0.010 deeper than predicted.

  A post-hoc diagnostic redid the prediction with the engine's measured equation of state (`diag_profiles22.py`). That cuts the k = 3 miss to 0.0064, so about 37% of the miss is the discrete-time engine's medium, which differs from the continuous-time theory by +0.8% in z at ρ = 8, +2% at ρ = 2 and 0.00% at ρ = 512. The rest is unexplained.
- **Reported (q-method):** 0.954 ± 0.018 at density 8 (theory 0.926) and 0.90 ± 0.07 at density 32 (theory 1.024). This is a shape summary, too noisy to mean anything at 32.

**T2. Clocks slow by the fractional shortage (Run 15's check): FAIL.**

| density | design 1 (hold H) κ | design 2 (hold 2H) κ | ratio | against own places |
|---|---|---|---|---|
| 8 | 0.931 ± 0.012 | 0.990 ± 0.014 | **0.941** | 1.005, 1.003 |
| 32 | 0.941 ± 0.018 | 0.980 ± 0.017 | **0.961** | 1.000, 1.000 |

The designs disagree by 6% (density 8) and 4% (density 32), against the registered 2%. Design 1 also misses the per-design band (1.00 ± 0.05) at both densities. **Every clock slows exactly with the possibility at its own two places**, but it drains those places itself.

- **A partial model** (`NOTE_22_clocks.md`, `clockself22.py`; worked out after density 8, hashed before any density-32 probe run finished). Its renewals are a sink $q=(P_a+P_b)/(jH)$ at each of its places. This lowers the outflow there by $\Delta z_{\rm self}=6(G_0+G_1)\,q$, with lattice Green's function $G_0=0.2527$ and $G_1=G_0-\tfrac16$. In a well q falls with $P_{\rm own}$, so the self-dip shrinks and the clock slows *less* than its surroundings:

  $$\kappa\approx\frac{1}{1+D_{\rm self}},\qquad D_{\rm self}=y'(z)\,\Delta z_{\rm self}.$$

  **What the model gets right and wrong:**
  - **Right:** the design ratio at density 8, 0.942 against 0.941 measured.
  - **Wrong in size:** its absolute κ values (0.870, 0.923) are about 6% low, and its own-place dips are too small (next bullet).
  - **Its density-32 prediction:** 0.936, with "above 0.97 means the mechanism is wrong". Measured 0.961 ± 0.025, between the two, so not decisive.
- **Direct measurement of the self-dip** (post hoc; `selfdip22.py`, in the control runs). A probe's own places sit below the surroundings by 0.32 (design 1) and 0.256 (design 2) at density 8, and by 0.305 and 0.242 at density 32.
  - **It does not fade with density:** four times the possibility per place shrinks it by only 4–6%. That is what the model claims.
  - **Against these numbers the model's sizes look wrong:** it gives 0.214 and 0.125 at density 8 (0.202 and 0.117 at 32), and a design-2 to design-1 ratio of 0.58 against 0.80 measured. *Corrected by Run 23 (§9p):* these dips were measured against the box mean, so they include the depletion that 100 probes 2.5 apart cause together. A lone clock in Run 23 dips 0.186 (design 1) and 0.105 (design 2), a ratio of 0.56. The model matches that to 8–10%.

  **Why it does not fade (theory, consistent with the measurement).** Since $y'\to1/c$, the logarithmic outflow refills a drained place only logarithmically, so one commitment's self-dip is $D_{\rm self}\approx6(G_0+G_1)\,q/c$ at every density. In the adopted (linear) medium the same dip would be $\approx2q/P$, vanishing as P grows. That may be why Run 15's flow clocks agreed; it is untested.

**T3. The outflow is unscreened and follows its draw (Runs 14 and 19).** The measured outflow deficit is set against the lattice solution of the exact equation, built from each run's recorded sinks, with no free amplitude.
- **Amplitudes** are 0.985–1.021 (mean 1.002, scatter ±1.0%, 15 runs). Misfits are 0.10–0.42% of the deficit at r = 4.
- **Verdict:** 14 of 15 runs pass (the three density-4 runs give 0.992, 0.990 and 0.998). One (density 8, seed 2, k = 2) is at **1.0205** against 1.00 ± 0.02, a **marginal FAIL**. That is 1.9 scatter-widths from the mean; one such run in 15 is about what chance gives.
- **Screening:** the best-fit length is at the scan's upper edge (unscreened) in 10 runs and 150–180 in 2. In 3 density-32 runs it is 30–36, improving misfits of 0.19–0.29% to 0.10–0.21%. The exact equation has no screening term. This is most likely the residue of incomplete relaxation (diffusion length $\sqrt{4Dt}\approx20$–30 over the window), not tested.
- **Flag:** T3 is exact by conservation; it checks the code.

**T4. Patterns fall (Run 16).**
- **The registered code check failed before any engine field was used.** In the theory's smooth field, $a/a_{\rm pred}$ is 0.85–0.98 (median 0.913), with masses up to 15% apart.

  **Likely causes (untested):** packets of width 4 span strongly curved field in these deep wells, and 14 out they reach within 6 places of the box face, where the gradient reverses. A larger box would fix the second but not the first, and no larger box was run. Shorter fit windows, radius 16 and heavier patterns did not restore Run 16's regime (`diag_fall22.py`). **T4 as registered therefore cannot test the clock-set rate in these wells**; that carries over from Run 16.
- **T4′ (engine noise, Amendment 2):** each engine-field release over the same release in the smooth field.

  | field | all inward | median ρ | range |
  |---|---|---|---|
  | density 8, seed 2 | yes | 1.0005 | 0.991–1.006 |
  | density 8, seed 3 | yes | 1.0024 | 0.990–1.010 |
  | density 32, seed 2 | yes | 1.0014 | 0.997–1.007 |
  | density 32, seed 3 | yes | 1.0029 | 0.986–1.011 |

  **Pass:** the engine's noisy field makes patterns fall as its smooth version does.

### Against the pre-registration

| test | registered | measured | verdict |
|---|---|---|---|
| T1a | \|β − 1\| ≤ 0.003 at P₀ ≥ 64; rising 4 → 32 | 0.9996, 1.0015, 1.0010, 1.0005; rise 196σ | **pass** |
| T1b (Amendment 1) | max \|Δ ln P\| ≤ 0.005, r.m.s. ≤ 0.003 | 0.0011 / 0.0003 (4), 0.0036 / 0.0007 (8), 0.0037 / 0.0007 (32) | **pass** |
| T1c | theory column ± 0.03; draws ± 3%; profiles max 0.010, r.m.s. 0.005 | all pass except density-8 profiles, max 0.0101 | **marginal fail** (profiles, density 8) |
| T2 | κ = 1.00 ± 0.05 per design; designs within 2% | 0.931 / 0.990 (8), 0.941 / 0.980 (32) | **FAIL** |
| T3 | A = 1.00 ± 0.02, misfit < 2% | 14 of 15 runs; one at 1.0205 | **marginal fail** |
| T4 (code check) | smooth field 0.96–1.00 | 0.85–0.98 | **fail: test not valid in box 40** |
| T4′ (Amendment 2) | median ρ 1.00 ± 0.01; every ρ 0.97–1.03 | 1.000–1.003; 0.986–1.011 | **pass** |

### Reading

- **Candidate A fixes β, for an ideal clock.** The matter-free medium's own equation of state puts β inside Mercury's band from 64 units of possibility per place upward. The zero-range theory predicted these β values beforehand: within 0.004 at every P₀ ≥ 32, and within 0.001 from 64 up. The wells at densities 4–32 obey the same equation of state to about 0.01 in β.

  This is the first engine rule in the record whose medium gives the exponential metric's second-order term. The adopted engine gave β = 0.47.

  **Two limits.**
  - No well was run where Mercury's band passes.
  - This is the β of a clock that reads the ambient ⟨P⟩. The clocks as built read their own drained places (T2), so no built clock's second-order response was measured.
- **Nordtvedt is not reached.** At 2048 per place, η = +0.0021 ± 0.0003, against σ(η) = 4.4×10⁻⁴. The theory brings it within 2σ only above about 5,000 per place, which is not measured.
- **But Candidate A breaks clock universality, and with p_s = 1 the break looks structural.** A presence clock reads the possibility at its own places, which its own draw depletes by 24–32%. Near matter that self-depletion shrinks, so a clock that draws more slows less. Clocks of different make disagree by 4–6% at both densities tested (8 and 32), and the self-dip shrinks by only 4–6% between them.

  Real clocks of different types redshift alike to about one part per million: null-redshift comparisons of rubidium, caesium, hydrogen and dysprosium clocks bound the difference near 10⁻⁶ (Will 2014, *Living Rev. Rel.* 17, 4, §2.1.3, arXiv:1403.7377). **As built, I judge Candidate A excluded:** T2 fails as registered, and the exclusion comes from setting that failure against the 10⁻⁶ bound, not from a registered rule.
- **The same exponential amplification does both.** It makes β = 1 ($P\propto e^{z/c}$), and it turns one commitment's small outflow deficit into an order-one dip ($\Delta\ln P=\Delta z/c$). With $c\approx1.4$, one commitment is never a small disturbance.

  **Untested way out:** make c large. With $p_s\gg1$, $c=0.99/\ln(1+1/p_s)\approx0.99\,p_s$, and the self-dip should fall as $\approx6(G_0+G_1)q/p_s$ (the theory's form; Run 23 confirmed it: slope −0.94 ± 0.04 over $p_s$ = 4–64). The medium is then linear below $p_s$ (the adopted engine) and logarithmic above it, so β = 1 would need $P_0\gg p_s$. That makes matter light compared with the medium, which is also what gravity's weakness needs. It is a hypothesis for Allen's decision (§11c), not a result.
- **What survives, whatever Allen decides:**
  - The β formula, $\beta=1+y''/(2y'^2)$, for a clock reading the ambient ⟨P⟩ in any zero-range medium.
  - The demonstration that the old flow clock could never reach β = 1.
  - A cheap, precise way to measure β with no matter at all.

![Run 22](figures/22_candidateA.png)
