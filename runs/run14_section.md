## Run 14: the vacuum test (on CO's own event-layer engine)

**Question.** CO's event layer finds that a mass's clock well can have **reach** or **strength** but not both (`EVENT_LAYER.md` result 25; "the hardest open item"). The proposed cause is that every vacuum place commits and so spends possibility. That spending refills the shortage around matter and screens it. The test removes vacuum commitment and nothing else.

**Pre-registered** before any run (`PREREG.md`): predictions V1–V4 and O1, and what would count against the claim.

### Why vacuum spending screens

A shortage $s$ of possibility spreads by wandering and is refilled by the medium's own consumption:

$$
D\,\nabla^2 s-\frac{\chi R}{\rho}\,s=-S\,\delta(\mathbf x),\qquad s\propto\frac{e^{-r/\lambda}}{r},\qquad \lambda=\sqrt{\frac{D\rho}{\chi R}},\qquad D=\frac{\text{PHOP}}{6}.
$$

CO's clock *is* a place's count of its own commitments. So χ, the clock's response to a shortage, is also the medium's marginal consumption. A responsive clock means a short λ: that is the trade-off.

If the vacuum carries no commitment, the vacuum term vanishes:

$$
D\,\nabla^2 s=-S\,\delta(\mathbf x)+\bar S\quad\Longrightarrow\quad\lambda=\infty .
$$

Clocks are then pieces of matter, sampling the shortage where they sit.

### Method

**Engine.** CO's `run_event_layer.py`, imported unmodified. The subclass reproduces the original engine **bit for bit** when its additions are switched off (checked over 300 ticks: possibility, blinks and matter states identical).

**Arms.**
- **O:** the original tick. Every place commits by Born choice and mutual proposal, spending one unit from each place.
- **V:** identical, with the vacuum's commit step skipped. Places hold possibility and pass it on, but never commit. Matter's reserved commitments and universal return are unchanged.

**Matter.** The published ball, radius 3, 54 reserved pairs.

**Probe clocks.** Reserved pairs under matter's own rule, renewing the moment they end if both places hold possibility. A probe's clock is its count of completed renewals.
- Six per shell at r = 5–12.
- The same layout in every matter run and its control.

**Settings.** Box 30, PHOP 0.99, densities 1, 2 and 8, seeds 1 and 2, 12,000 ticks read over the last 9,000. Plus a reach check: arm V, box 60, density 2, probes to r = 27, 20,000 ticks, two seeds.

**Shape fit.** The measured shortage was fitted to the periodic lattice solution of $D\Delta_{\rm lat}$, sourced by the measured matter draw with its mean removed (universal return). The fit was done unscreened, and screened with λ scanned.

### Results

**Shape of the shortage (box 30).**

| Arm | Density | Background μ₀ | Unscreened misfit | Best-fit λ (seeds) |
|---|---|---|---|---|
| O | 1 | 0.56 | 12.5% | 1.5, 1 |
| O | 2 | 1.38 | 5.7% | **3, 3.5** (CO published 3.4–4) |
| O | 8 | 7.21 | 0.2% | ≥ 40 (unscreened, as published) |
| V | 1 | 0.86 | 1.0% | 10, 10 |
| V | 2 | 1.81 | **0.5%** | **20, 15** |
| V | 8 | 7.79 | 0.2% | ≥ 40 |

**Box 60 (arm V, density 2):** the shortage matches the unscreened periodic solution to **0.3%** of its shell-4 value, out to the box's own zero crossing at r ≈ 23.

**Probe clock slowing (%) at shells 8, 9, 10 (box 30), against CO's result-25 ceiling $0.043\,(S/R)/r^3$ for the same drain S and clock rate R:**

| Arm, density | r = 8 | r = 9 | r = 10 | Ceiling at 8, 9, 10 | Response χ (per unit shortage) |
|---|---|---|---|---|---|
| O, 1 | −1.0 ± 0.9 | −0.2 ± 0.7 | −0.6 ± 1.1 | 0.61, 0.43, 0.31 | — (no measurable shortage there) |
| O, 2 | 0.95 ± 0.30 | 0.27 ± 0.31 | 0.17 ± 0.33 | 0.59, 0.42, 0.30 | 0.29–0.33 |
| **V, 1** | **4.86 ± 0.59** | **3.55 ± 0.49** | **2.17 ± 0.47** | 0.26, 0.18, 0.13 | 0.77–1.07 |
| **V, 2** | **1.94 ± 0.25** | **1.37 ± 0.16** | **0.93 ± 0.11** | 0.42, 0.30, 0.22 | 0.13–0.22 |
| O, 8 / V, 8 | 0.01 / 0.02 | 0.02 / 0.00 | −0.02 / 0.01 | — | ≈ 0 in both |

- Arm V draws *less* than arm O at density 2 (S = 9.2 against 11.7 units per tick), yet its clocks at shells 8–10 slow **3.1×** as much (pooled 1.41 ± 0.10% against 0.46 ± 0.18%).
- Arm V **exceeds CO's ceiling by 4.2–4.6× at density 2 and 17–20× at density 1.** Arm O sits at or under its ceiling.

**Reach of the clocks (box 60, arm V, density 2), probe slowing in %:**

| r | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 | 21 |
|---|---|---|---|---|---|---|---|---|---|
| Slowing | 14.9 ± 0.4 | 7.1 ± 0.1 | 4.1 ± 0.1 | 2.5 ± 0.2 | 1.75 ± 0.17 | 0.86 ± 0.18 | 0.56 ± 0.12 | 0.44 ± 0.11 | 0.03 ± 0.10 |

- The slowing follows the measured unscreened shortage through one smooth clock response, $\text{slowing}=c_1s+c_2s^2$.
- With CO's density-2 screening (λ = 3.5) and the same response, the slowing at r = 17 would be about 0.06%. The measured value is 0.56 ± 0.12%.

**Sanity checks on arm O.**
- CO's own benchmark (`python run_event_layer.py well`), run unmodified in this workspace, reproduces the published table exactly: 4.36, 1.85, 1.11, 0.69, 0.56 and 0.25% at shells 4–9.
- The subclass is bit-identical to that engine when the probes are off.
- With probes in the box and a read three times longer, arm O's medium-blink well reads 5.0, 2.2, 1.1, 0.5, 0.3 and 0.1%. That is the same shape and depth, within about 0.6 points.

### Against the pre-registration

| | Prediction | Outcome |
|---|---|---|
| V1 | Arm V unscreened at every density, misfit ≤ 5%, λ ≥ 10 | **Pass.** Misfit 0.2–1.0%; λ 10–20 in box 30 (≥ 40 at density 8); 0.3% in box 60 |
| V2 | Arm V's probes at shells 8–10 ≥ 3× arm O's at density 1–2; χ ≥ 0.1 | **Pass.** Density 2: 3.1× pooled (shell 8 alone 2.0×); density 1: arm O is zero within noise. χ = 0.13–1.07 |
| V3 | Box 60: slowing follows the unscreened shape to r ≈ 20 | **Pass.** Nonzero at 4σ at r = 17 and 19; ~10× the screened expectation |
| V4 | Density 8: weak in both arms (the clock saturates) | **As predicted.** Every probe renews at exactly 1/HBAR in both arms |
| O1 | Arm O screened at density 1–2, unscreened but unfelt at 8 | **Pass** |

### Reading

- **The trade-off belongs to the vacuum, not to the mechanism.** With the vacuum committing, CO's own engine reproduces its own finding: λ ≈ 3, a ceiling on far slowing. With the vacuum holding possibility but never committing, the same engine gives an unscreened shortage at every density. Clocks made of matter then slow by **4–20× more than the ceiling allows** at the same distance, out to the edge of a 60-place box.
- **Strength is now the clock's business alone.** In this engine a clock renews when both its places hold at least one unit. Where every place holds about eight, it never waits, so it cannot notice a shortage in either arm. Real gravitational slowing is tiny (about 10⁻⁹ at the Earth's surface), so what a clock needs is a response that stays **linear and nonzero** at small shortage. A threshold rule in a rich medium gives an exponentially small one, of order $e^{-\mu_0}$. This is the next thing the clock rule has to supply.
- **What it costs CO:**
  - The One Being medium that commits and settles (results 20–22, 27) runs on vacuum commitment. Adopting "the vacuum carries no commitment" means re-reading those results: in particular the arrow-of-time age relic, which is measured on vacuum clocks.
  - "Clocks are matter" becomes a statement of the ontology.
- **Not tested here:** whether a bigger mass reaches further (expected, since the amplitude scales with the drain while the shape stays fixed); motion ("nothing falls" is a separate question, §2.2 of the map); and any density between 2 and 8.

![Run 14](figures/14_vacuum_test.png)
