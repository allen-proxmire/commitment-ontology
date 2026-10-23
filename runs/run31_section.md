## Run 31: does a well form at the pattern speed, and does it follow a moving body?

*19 October 2026. Pre-registered and hashed before any run (`moving/PREREG_31.md`, 05:43 UTC), with a kill rule. Step 1 was a rule for moving matter; working it out raised this prior question. An independent agent re-checked the hashes, numbers and verdicts and re-simulated the prediction; its corrections are included.*

**Question.** In the engine, the clock well around matter is a deficit of possibility, and possibility moves by random hops. In the mean, exactly,
$$
P_x(t+1)=P_x(t)+\tfrac16\sum_{y\sim x}z_y-z_x-s_x+\bar s .
$$
Linearised, $z\approx z_0+z'(P-P_0)$, every lattice mode relaxes as $d_k(t+1)=(1-D\lambda_k)\,d_k(t)-s_k(t)$, with $D=z'/6$ and $\lambda_k=6-2\sum\cos k_i$. That is diffusion. If it holds:
- a well forms at the diffusion rate, not at the pattern (light) speed
- a body moving through the lattice trails its well, with a wake behind it and the well cut down ahead and to the sides beyond about $2D/w$

GR, and every planetary and pulsar test, needs the field to follow its body to $O(w^2)$.

**Prior record (checked first).**
- **`Phase3_GR_MovingBinarySim.md`** solved $D\nabla^2B+\mathbf w\cdot\nabla B=\kappa\rho$ and found the wake "real, linear in w, dipolar". Its fix, a drain that screens only the wake, "*imposes* the split".
- **GR-III's review note:** "The rule is scalar diffusion… decays without travelling. The 'hyperbolic sector'… is written in by hand."
- **`ED_Attempt_01` C136** has the budget spreading only about 3×10³⁰ steps over the universe's age. C87 separately needs gravity unscreened to 10¹⁶ m. The two were never set side by side.
- **`STATE_OF_THE_ONTOLOGY.md`** calls universal return "an instant link across all of space".
- **No file tested a moving body on the adopted engine, or estimated how long a well takes to form at astronomical distances.** MovingBinarySim asks for the engine test.

**Runs.**
- **Rules and body.** The adopted rules, $p_s$ = 1, $P_0$ = 64, box 40. ED's radius-3 ball (Run 26's body A, 54 pairs) through engine22's World22, unchanged. Code check: bit-identical to Run 26's engine over 300 ticks.
- **Burn-in and switch-on.** 5,000 ticks of the medium alone, then the ball is switched on.
- **The runs:**
  - **M1:** the ball steps +1 in x every 667 ticks ($w=1.5\times10^{-3}$), for 90,000 ticks, read over the last 50,000 in the ball's frame. It moved 134 places.
  - **M2:** every 2,667 ticks ($w=3.75\times10^{-4}$), the same length. It moved 33 places.
  - **S:** static, 40,000 ticks.
- **Predictions** (`theory31.py`, before any run):
  - **D:** 0.00385 places² per tick, from Run 22's matter-free ladder at $P_0$ = 64.
  - **Sink shape:** Run 26's solo ball.
  - **The moving ball:** the periodic steady state in its frame, exact for the linear dynamics.

**Results against the registration.**

| | test | measured | predicted (diffusion) | a field that follows its body | verdict |
|---|---|---|---|---|---|
| **K31** | fore-aft asymmetry α, M1 | **+0.672** (halves 0.694, 0.650) | +0.748 (band 0.56–0.94) | 0 | in band |
| | sideways well, moving/static, M1 | **0.537** (halves 0.552, 0.521) | 0.443 (band 0.33–0.55) | 1 | in band |
| | α, M2 | **+0.321** (halves 0.321, 0.321) | +0.400 (band 0.30–0.50) | 0 | in band |
| | sideways, M2 | **0.928** (halves 0.919, 0.937) | 0.880 (band 0.66–1.10 in the code; the registration's text said 0.66–1.00) | 1 | in band under both |
| | | | | | **outcome A: killed.** The well is carried by diffusion |
| **B31** | build-up, measured/predicted deficit, median over 16 (r, t) points | **0.970** | 1.00 ± 0.15 | — | **pass** |
| | fraction of the well formed at r = 10, 1,000 ticks after switch-on | **0.036** | −0.029 | 1 (after 10 ticks) | **pass** |
| reported | draw, ball moving | **9.27** per tick (M1), **8.63** (M2) | — | — | static: 8.54 (Run 26), 8.49 (S, end) |

![Run 31](figures/31_moving.png)

**Reading.**
1. **The well is carried by diffusion, as the mean equation says (B31).**
   - At 10 places, 1,000 ticks after switch-on, 4% of the well has formed. A field keeping up with light would be complete after 10 ticks.
   - Over the whole build-up, measured and predicted deficits agree to a median 0.97. Individual points range from 0.83 to 1.75; the scattered ones are early or far out, where the deficit is small.
   - The linear theory over-predicts the well next to the ball: 0.83 of the predicted depth at r = 4 late on, much as Run 26's static well came in at 0.94 of theory. That is consistent with the mean-field $D(\rho)=c/(6(p_s+\rho))$ rising where the medium is depleted. This is an inference, not tested.
2. **A moving body trails its well (K31, outcome A).**
   - The well is lopsided toward behind the ball at both speeds, and cut down sideways. All four statistics are within the registered bands.
   - All four deviate toward a weaker wake than the linear prediction. Two sit near the band edges: M1 sideways 0.537 (edge 0.553) and M2 α 0.321 (edge 0.300). That is consistent with the same faster diffusion in the depleted well, which is untested.
   - Halves agree to 0.05 or better.
   - A field that followed its body would show 0 and 1.
3. **A moving body draws more.** It keeps stepping into medium its own well has not yet drained.
   - The excess is +8.5% at the faster speed and +1.05% at the slower: about 8× for a 4× change in speed, roughly $w^{1.5}$.
   - The slower figure is close to the spread between the two static references (8.54 and 8.49).
   - Diffusion makes the excess first order in w only in the small-speed limit. At physical speeds a body never sits in its own well, so the excess saturates: its pull would be that of a body with no self-redshift.
   - Either way a body's active mass depends on its speed through the lattice. That is another preferred-frame effect.
4. **What it means at the adopted scales (registered arithmetic).** This assumes one place is one Planck length and one tick one Planck time.
   - With $P_0/p_s\gtrsim2.3\times10^4$ (Run 30), D ≈ 7×10⁻⁶ places² per tick.
   - A well can spread only $\sqrt{6Dt}\approx$ 0.3 μm in the age of the universe.
   - A body moving at 370 km/s (the Sun against the CMB) keeps its well within about $2D/w\approx$ 0.01 of a place.
   - More generally, any carrier that random-walks at no more than the pattern speed fails. Its persistence length λ is the same for every body, and:
     - 1/r needs $r\gg\lambda$
     - following a body needs $r\ll2D/w\le\tfrac23(c/w)\lambda$
     - so the window is a factor of about $\tfrac23c/w\approx540$ at 370 km/s
   - Observation needs 1/r from laboratory torsion balances (sub-millimetre) to the Sun's field following it out to the outer planets (10¹³ m). The double pulsar's fields do so at $w\sim10^{-3}c$.
   - The closest classic analogue is Laplace's bound on the aberration of gravity. Le Sage's shadow models failed differently: by drag and heating, in the ballistic regime.

**What stands and what doesn't.**
- **Stands, as steady states:** the static results of Runs 14–30 (steady wells, β = 1, clocks, free fall in static wells, sourcing). They are properties of the engine's steady state, and B31 confirms that state is reached, by diffusion.
- **But the steady state is never reached at physical distances.** At the adopted scales diffusion takes it only about 0.3 μm in the universe's age, even for a body at rest, and no real body is at rest in the lattice. So the static results describe gravity only under a field-dynamics rule that reaches the same static limit at the pattern speed. A deficit carried as a wave does, and keeps every one of them.
- **Fails:** the engine's field dynamics as a model of gravity, for bodies at rest (formation) and in motion (the wake). Any test of a moving-matter draw rule (Run 30's 1 + 2v²) needs that rule first. Run 11b required "capacity set by matter at each moment", and the engine's medium does not supply it.

**Fixes in the record** (none built on the engine):
- **Screen the wake and keep the static part** (MovingBinarySim). The engine has one field, so a drain that screens its wake screens the static well too, which is Run 14's reach/strength trade-off. It needs two channels.
- **Carry the deficit as a wave** (HyperbolicBuild).
  - The static limit is the same: $\tfrac1{c^2}\partial_t^2\delta=\nabla^2\delta-s/D$ reduces to $D\nabla^2\delta=s$, so every static result carries over.
  - Changes travel at c, and a moving body's field follows it.
  - The deficit then needs inertia, a field (amplitude) rather than units hopping. Run 16's patterns already move this way.
- **Places move with matter** (Run 11b's "sliding places is free"). Relative motion becomes shear of relations, which Run 11b showed radiates GR's power at c.
- **An instantaneous constraint.** This follows steady motion, but it allows instant influence in the lattice frame, against the ontology's §10.
