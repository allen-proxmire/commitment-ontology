## Run 16: falling with inertia (on ED's own event-layer engine)

**Question.** ED's own record says **nothing falls**. A free pattern that moves by commitments, paid for by the places it lands on, is pushed *away* from matter. Matter gathers only under an added steering rule with a chosen coupling, and then it drifts rather than accelerates. The record names two missing pieces: *"a body falling through another's field"* and *"a reason the steering rule should take the form it does"*. It also says direction lives in phase. This run supplies both, with no steering rule and no coupling.

**Target, fixed in advance (standard physics).**
- **Inertia:** a free body keeps its state of motion.
- **Falling:** in a weak static field, a slow body accelerates at

$$
\mathbf a=-c^2\,\nabla\ln\frac{\nu(\mathbf x)}{\nu_\infty}
$$

  That is the same field that sets clock rates; this is Einstein's equivalence argument. Matter waves fall this way too: Colella–Overhauser–Werner (1975) measured gravity's phase shift on neutrons as the difference in elapsed time between two paths.
- **Universality:** all bodies fall alike. MICROSCOPE bounds the difference at about 10⁻¹⁵ (Touboul et al. 2022); rubidium-isotope atom interferometry at about 10⁻¹² (Asenbaum et al. 2020).

The pre-registration (`PREREG.md`) was written before any pattern was evolved in the engine's field. A note written after the density-8 results and before the density-32 ones (`NOTE_after_d8.md`) records two problems and a revised prediction.

### The source: ED's engine with the adopted rules

- ED's `run_event_layer.py`, imported unmodified.
- **The vacuum never commits** (Run 14), and **matter's hold is counted in passing possibility** (Run 15).
- The published ball (radius 3) in a 60³ periodic box. Densities 8 and 32; ball seeds 1 and 2, plus a control with no matter.

The **clock field** is the time-averaged count of possibility passing into each place, relative to the medium with no matter:

$$
N(\mathbf x)=\overline{n}(\mathbf x)/\lambda_0
$$

Under the adopted rule, this is the rate of matter's clocks. Run 15 measured clock slowing equal to the fractional shortage, 1.00 against the clock's own neighbourhood.

### The test pattern

A pattern of possibility carries an amplitude and a phase; ED's Born weighting already treats possibility as amplitudes √P with phases. It obeys three rules:
- It hops at most one place per tick.
- **Its phase is turned by the committed world's local count, never by a clock of its own.** At internal frequency $m$, it turns by $m\,N(\mathbf x)$ per tick at place $\mathbf x$.
- It has no steering rule and no coupling.

The simplest linear rule with these properties is the Klein–Gordon equation on the engine's lattice:

$$
\frac{\phi^{n+1}-2\phi^n+\phi^{n-1}}{\delta t^2}=\nabla^2_{\rm lat}\phi^n-m^2N(\mathbf x)^2\phi^n,\qquad \delta t=0.1\ \text{tick}
$$

Its charge is conserved exactly by the scheme:

$$
\rho^{n+1/2}=\mathrm{Im}\big(\overline{\phi^{n+1}}\,\phi^n\big)
$$

The pattern's position is its centroid of charge. Its dispersion relation is

$$
\Big(\tfrac{2}{\delta t}\Big)^2\sin^2\frac{\Omega\,\delta t}{2}=m^2N^2+\sum_i 4\sin^2\frac{k_i}{2}
$$

**Inertia and weight come from the same $m$.** Near rest, $\Omega\approx mN+k^2/(2m)$. So $m$ sets the inertia, through the one-hop-per-tick limit $c=1$. And $mN(\mathbf x)$ is a potential that is lower where clocks run slow.

**The derived steering rule.** ED's added steering rule makes each place lean toward the neighbour whose cadence lags. Here the same thing happens as interference, with no rule added:
- Where the count runs slow, the pattern's phase falls behind.
- Its wavefronts turn toward the lag.
- The pattern's velocity grows steadily in time (an acceleration), rather than drifting at a rate set by a chosen coupling.

**Parameter-free prediction.** For a pattern released at rest, rays of the lattice dispersion give

$$
a_{\rm in}=\big\langle\hat u\cdot\nabla\ln N\big\rangle_{\rho_0}\Big(1-\frac{\langle K\rangle}{m^2\bar N^2}\Big)\Big/\Big(1-\big(\tfrac{m\bar N\delta t}{2}\big)^2\Big)
$$

- The first factor is the clock-rate slope averaged over the initial charge.
- The second is the pattern's internal motion, at most 10%.
- The third is the time step, below 1%.

**Relabelling flag.** In standard terms, this is a relativistic matter wave in a weak static field; its fall is GR's Newtonian limit, as in the COW experiment. ED's own content here is:
- which count turns the phase: the committed world's passing possibility, the same count that times matter
- the field coming from ED's engine
- the steering coming out of phase alone, with no rule and no coupling

### Method

- **Masses:** $m$ = 0.7, 1.0, 1.4, 2.0 (rest frequency per tick). Charge width σ = 4 places.
- **Releases:** at rest, at $r_0$ = 12 and 18 places from the ball, along the six axis directions, in each ball field. That is 192 releases.
- **Measurement:** the inward centroid displacement, recorded every substep. The acceleration $a$ comes from a polynomial fit of order 4 over the first 16 ticks.
- **Controls:**
  - the ball field with the phase turned by **global ticks** ($N\equiv1$)
  - the medium with **no matter**, at the same 24 release points
- **Inertia:** packets at rest and moving ($k_0$ = 0.1, 0.2), followed for 60 ticks in the no-matter medium.
- **Exploratory:** the engine's **live** per-tick count instead of its average. Three 64-tick windows; $m$ = 1 and 2.
- **Code checks** (synthetic fields only, before the engine's field):
  - charge conserved to 10⁻¹⁶
  - group velocity matched to 5 digits
  - a synthetic 1/r well gives measured ÷ predicted = 0.987–0.989 at every mass

### Results

**Falling: measured ÷ predicted acceleration** (mean ± sd over the 6 directions):

| density | seed | released | m = 0.7 | m = 1.0 | m = 1.4 | m = 2.0 | acceleration, m = 1 (places/tick²) |
|---|---|---|---|---|---|---|---|
| 8 | 1 | 12 out | 0.961 ± 0.001 | 0.960 ± 0.001 | 0.958 ± 0.001 | 0.959 ± 0.001 | 5.4×10⁻³ |
| 8 | 1 | 18 out | 0.995 ± 0.002 | 0.990 ± 0.001 | 0.989 ± 0.000 | 0.988 ± 0.000 | 2.2×10⁻³ |
| 8 | 2 | 12 out | 0.960 ± 0.001 | 0.959 ± 0.001 | 0.958 ± 0.002 | 0.959 ± 0.002 | 5.6×10⁻³ |
| 8 | 2 | 18 out | 0.994 ± 0.002 | 0.990 ± 0.001 | 0.989 ± 0.001 | 0.988 ± 0.001 | 2.3×10⁻³ |
| 32 | 1 | 12 out | 0.980 ± 0.000 | 0.981 ± 0.000 | 0.983 ± 0.001 | 0.985 ± 0.001 | 1.75×10⁻³ |
| 32 | 1 | 18 out | 0.994 ± 0.003 | 0.991 ± 0.001 | 0.990 ± 0.001 | 0.990 ± 0.001 | 8.0×10⁻⁴ |
| 32 | 2 | 12 out | 0.979 ± 0.001 | 0.980 ± 0.000 | 0.983 ± 0.000 | 0.985 ± 0.000 | 1.78×10⁻³ |
| 32 | 2 | 18 out | 0.994 ± 0.001 | 0.991 ± 0.001 | 0.990 ± 0.000 | 0.990 ± 0.000 | 7.7×10⁻⁴ |

- **Direction:** every release falls inward, 192 of 192.
- **Universality:** at each release, masses 1.0, 1.4 and 2.0 agree to within 0.37% (density 8) and 0.58% (density 32). The lightest pattern, $m$ = 0.7 with internal velocity² ≈ 0.1, differs from them by +0.4% (density 8) and 0.0% (density 32).
- **Absolute rate:** the ratios sit 1–2% below 1. The synthetic-well code check showed the same 1% shortfall at every mass, so it comes from the prediction formula's weighting, not from the engine.

**The marginal case: density 8, released 12 places out (0.96).** The fitted *instantaneous* acceleration depends on the fit window here: for $m$ = 2, 0.983 at 8 ticks, 0.977 at 12, 0.963 at 16 and 0.938 at 24. The reason is that the pattern's inner edge reaches the matter ball, where the field's slope reverses.

As an after-the-fact check (not pre-registered), the **distance fallen in 16 ticks** can be compared with $\tfrac12a_{\rm pred}t^2$:

| | density 8, seed 1 | density 8, seed 2 | density 32, seed 1 | density 32, seed 2 |
|---|---|---|---|---|
| released 12 out | 1.008 ± 0.006 | 1.006 ± 0.007 | 0.997 ± 0.006 | 0.996 ± 0.007 |
| released 18 out | 1.005 ± 0.007 | 1.005 ± 0.006 | 0.995 ± 0.006 | 0.995 ± 0.004 |

**The distance fallen agrees with the clocks to within 1% everywhere, including the marginal case.** The 0.96 is a property of extracting an instantaneous acceleration where the pull changes quickly, not of the fall.

**Controls:**
- **Phase turned by global ticks:** $a$ = 2×10⁻¹⁰ and 3×10⁻¹³ (zero). Without the committed world's count turning the phase, nothing falls.
- **Medium with no matter:** at the release points, the measured acceleration is 2–10% of the ball's.
  - density 8: 2.3% at 12 out, 9.6% at 18 out
  - density 32: 4.5% at 12 out, 6.9% at 18 out
- **That small residual pull is itself falling.** The medium's own density ripples relax slowly (diffusively), so a 6,000-tick average keeps large-scale structure: the rms of N, smoothed over 6 places, is 0.08% at density 8. Patterns fall in those ripples at the formula's rate:
  - measured = 0.987 × formula (density 8) and 0.985 × formula (density 32)
  - correlation 1.000 over 48 releases each

**Inertia: as pre-registered, it fails at both densities.** In the no-matter medium:
- A resting pattern drifts 0.18–0.22 places in 60 ticks at density 8, and 0.12–0.17 at density 32. The bound was < 0.01.
- Moving patterns change speed by up to 13% (m = 1) and 74% (m = 0.7). The bound was 0.5%.

Two causes, found after the fact:
1. **The resting drift and the heavier patterns' slowdowns are the falling above.** The no-matter medium is not force-free on the pattern's scale. Its ripple forces at density 32 are 0.39× density 8's (rms over the control releases). The note written before density 32 predicted about ½.
2. **The large changes in the lightest patterns are a measuring error.** By tick 60 an m = 0.7 pattern is about 13 places wide, so its tails wrap around the 60-place periodic box and corrupt a centroid measured from the release point.

With a centroid that follows the pattern:

| field | m = 1.0, k₀ = 0.2 (speed late ÷ early) | m = 2.0, k₀ = 0.2 | resting m = 2.0, moved in 60 ticks |
|---|---|---|---|
| exactly uniform | 0.9995 | 0.9993 | 0.0000 |
| no-matter medium, density 8 | 0.978 | 0.916 | −0.21 |
| no-matter medium, density 32 | 0.996 | 0.977 | −0.15 |

Where the clock rate is uniform, a pattern keeps its velocity to within 0.07%: that is inertia. Where it is not, the pattern falls.

**Live counts (exploratory).** Turning the phase by the engine's per-tick count, rather than its average, adds noise:

| | overlap after 5 / 10 / 20 ticks | coherence loss rate Γ (fitted) | white-noise estimate $m^2\bar N/\lambda_0$ | fall in 16 ticks, live ÷ averaged |
|---|---|---|---|---|
| density 8, m = 1 | 0.85 / 0.74 / 0.54 | 0.030 | 0.122 | 0.69 |
| density 8, m = 2 | 0.25 / 0.05 / 0.002 | 0.30 | 0.49 | 0.06 |
| density 32, m = 1 | 0.96 / 0.92 / 0.85 | 0.008 | 0.031 | 0.93 |
| density 32, m = 2 | 0.69 / 0.46 / 0.20 | 0.083 | 0.125 | 0.43 |

- **Richer medium:** 4× more possibility per place cuts Γ by 3.6–3.8×, close to the expected 4.
- **Heavier pattern:** Γ grows about 10× for twice the mass, against the white-noise estimate's 4×.
- **Absolute rate:** Γ is 1.5–4× below the white-noise estimate, because counts at neighbouring places are correlated.
- **Effect on falling:** a pattern that stays whole falls nearly as in the averaged field (0.93). One that is shattered by the noise does not fall (0.06).

### Against the pre-registration

| Prediction | Expected | Measured | |
|---|---|---|---|
| **F1** falls inward | all 192 releases | 192 / 192 | **pass** |
| **F2** at the clock-set rate | a/a_pred = 0.99 ± 0.03 | density 32: 0.979–0.994; density 8 at 18 out: 0.988–0.995; **density 8 at 12 out: 0.958–0.961** | **pass, except a marginal miss at density 8, 12 out** |
| **F3** universal | masses 1.0–2.0 the same to ±1% | within 0.58% at every release | **pass** |
| **C1** phase by global ticks | a = 0 | 2×10⁻¹⁰ | **pass** |
| **C2** no-matter medium | \|a\| < 10% of the ball's | 2.3–9.6%, and equal to the formula (slope 0.985–0.987) | **pass** |
| **I1** at rest stays put | < 0.01 places in 60 ticks | 0.12–0.22 | **fail** (falls in the medium's ripples; exact in a uniform field) |
| **I2** uniform motion | speed constant to 0.5% | changes of 2–74% | **fail** (ripples, plus a box-wrap measuring error; 0.07% in a uniform field) |
| live counts (exploratory) | Γ ≈ $m^2\bar N/\lambda_0$ | 1.5–4× lower; scales as 1/λ₀ | reported |

### Reading

**1. A pattern whose phase is turned by the committed world's count falls toward matter at the rate the clocks set.**
- It needs no steering rule and no coupling.
- It accelerates; it does not drift.
- Every mass falls alike, to within 0.6%.
- This fills both gaps in ED's record: a body falls through another's field, and the steering rule has a reason. Direction lives in phase, and the phase is the committed world's count.

**2. Inertia and falling are one rule.**
- In a uniform clock field a pattern keeps its velocity (0.07%). Where the field varies, it falls.
- Both come from $m$: it sets the inertia through the one-hop-per-tick limit, and it sets the weight through how fast the count turns the phase.
- That is why every mass falls alike. Universality here is a consequence of the single speed limit, not a separate rule.

**3. Moving by paying versus moving by phase.**
- ED's earlier result stands: a pattern that moves by commitments paid for by the places it lands on is pushed away from matter.
- A pattern of possibility, moving as a phase, falls.
- So in ED terms, **free fall is a property of possibility in transit, not of committed matter stepping.** That fits "possibility keeps no time; the committed world counts what passes".

**4. The no-matter medium is not perfectly calm, and that is physics, not a defect.** The possibility gas has slowly relaxing density ripples, and patterns fall in them exactly as they fall toward matter. The ripple forces shrink as the medium gets richer (0.39× for 4× the density).

**5. Discreteness has a cost (exploratory).**
- A pattern's phase, turned by a discrete count, picks up noise. That costs it its coherence at a rate that rises steeply with its mass and falls as 1/(possibility per place).
- A pattern that loses coherence stops falling coherently.
- For real particles the rate per Planck tick is tiny ($m t_{\rm P}\sim10^{-19}$ for a proton), so this does not conflict with experiment unless possibility per place is small.
- But it ties possibility per place to the coherence of heavy matter waves. Matter-wave interferometry with large molecules could bound it.

**6. What this does not show.**
- **Only the clock half of gravity is in this test pattern.** Its hops are not slowed, so it cannot bend light (Run 9's spatial half). Its fall for fast motion is not GR's. A full test would include the hop slowing that Run 9 found necessary.
- **Patterns here are much heavier per tick than real particles,** so lattice corrections are visible (the time-step factor, about 1%).
- **Orbits are not tested:** a pattern in this box spreads before it could complete one.

![Run 16](figures/16_falling.png)

---

