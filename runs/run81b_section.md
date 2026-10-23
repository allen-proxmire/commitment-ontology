## Run 81b: a reversible control for Run 81

*23 October 2026.*
- *Registered and hashed before any run (`wave81b/PREREG_81b.md`, 17:38:35 UTC), with the engine, the theory, the analysis and the job list. Validation runs and smoke runs made before registration are disclosed there. One of them was a ripple run on a non-registered seed whose final amplitudes were printed.*
- *An independent agent checked the run (below).*

**Why.** Run 81's check left its reading open on two points.
1. **Its control (M2s) was not reversible,** so the claim that a two-way bottom gives the same large-scale wave was not tested.
2. **The lower damping of the one-way medium** (Γ 0.33 against 0.50) could belong to the one-way cycle or to M2s's own irreversibility.

**Question.** With a truly reversible control, and with no frozen sideways flow:
- does a reversible bottom give the same large-scale wave?
- is the one-way cycle's mark on the damping there, at the predicted size?
- does M2s's irreversibility leave a mark beyond its rates?

**Three media.** All on 512 × 4 × 4 places, P̄ = 64, with Run 81's ripple (A = 0.01) and 192 seeds each.

| | rule | bottom |
|---|---|---|
| **M2** | Run 81's, bit-identical: head-on pairs rotate x → y → z → x | one-way |
| **M2s** | Run 81's control, bit-identical: a rotating pair goes to either other axis with probability ½ | no preferred cycle, not reversible |
| **M2r** (new) | each tick, at each place, one axis pair is chosen and the split of its head-on pairs is redrawn from the stationary law, given what the move conserves: weight ∝ 1/[h_a! (h_a + \|p_a\|)! (H − h_a)! (H − h_a + \|p_b\|)!] | **reversible:** a Gibbs (heat-bath) step, in detailed balance and symmetric under velocity reversal |

**The start.** Every frozen line momentum is zero (n_y− := n_y+, n_z− := n_z+), which removes Run 81's sound-speed artefact.

**The theory, fixed beforehand.** Each rule conserves count and momentum at every place and treats the axes alike up to cyclic order. So its linear collision step is fixed by how it relaxes the axis anisotropy:
$$
d\;\to\;(A+B\,P)\,d,\qquad \mu=A+B\,e^{2\pi i/3},\qquad \Gamma=\tfrac13\,\mathrm{Re}\,\frac{1+\mu}{2(1-\mu)},
$$
with P the cyclic shift. B ≠ 0 only for the one-way cycle.
- **(A, B) were measured beforehand** on uniform lattices, from how a tilted anisotropy relaxes.
- This gave Γ = 0.323, 0.471 and 0.530, so the predicted ratios were Γ(M2)/Γ(M2r) = **0.610 ± 0.016** and Γ(M2s)/Γ(M2r) = 0.889 ± 0.022.
- The mean field gives 0.651 and 0.979; these were stated in the registration, not scored.

**Results** (conservation exact; line momenta zero and kept, in all 576 runs).

| | Γ measured | Γ registered | M2r slope of ln Q⁻¹ on ln k | frequency offset, m = 1 and 3 |
|---|---|---|---|---|
| M2 | 0.346 ± 0.006 | 0.323 | (M2: 0.925 ± 0.025, not scored) | +0.12 ± 0.04%, +0.05 ± 0.08% |
| M2s | 0.501 ± 0.012 | 0.471 | | +0.07 ± 0.06%, −0.03 ± 0.12% |
| M2r | 0.512 ± 0.009 | 0.530 | **1.009 ± 0.039** | +0.05 ± 0.07%, +0.16 ± 0.18% |

| ratio | measured | registered | mean field (not scored) |
|---|---|---|---|
| Γ(M2)/Γ(M2r) | **0.676 ± 0.021** | 0.610 ± 0.016 | 0.651 |
| Γ(M2s)/Γ(M2r) | 0.978 ± 0.043 | 0.889 ± 0.022 | 0.979 |

![Run 81b](../figures/81b_control.png)

**Verdicts as registered.**
- **K81b-A (headline), the one-way cycle's mark at the predicted size: FAIL.** The ratio is 27σ below 1, but 10.9% above the registered 0.610, outside the limit of max(5%, 3σ) = 9.4%.
- **K81b-B, M2s against M2r: PASS,** through its 3σ allowance (10.0% against 13.1%).
- **K81b-C, a reversible bottom gives the same large-scale wave: PASS.** M2r's Q⁻¹ falls as k^(1.01 ± 0.04), and its damping is within 3.3 ± 2.5% of prediction.
- **K81b-D, no frequency offset: UNDECIDED.** Five of six offsets pass at 0.15%. M2r at m = 3 (±0.18%) is too imprecise to score. Run 81's offsets were 0.4–0.6%.
- **Bookkeeping: PASS.** M2r's rotations balance both ways.

**What the check added.**
1. **Reproduction.**
   - All 63 hashes match. Every output follows the registration, and each of the 576 jobs ran once.
   - Two seeds per medium re-run byte for byte, and the analysis reproduces byte for byte.
   - M2 and M2s reproduce Run 81's registered outputs bit for bit. **All five verdicts stand as computed.**
2. **M2r is exactly reversible.**
   - 512,000 moves were checked against the exact conditional law, with no mismatch. Count and momenta are conserved.
   - Its move-level entropy production is zero: the path log-ratio reduces to a state function, to 4×10⁻¹⁴. The raw estimate is (6 ± 14)×10⁻⁴ per place per tick, against M2s's 0.025.
   - A stationary M2r history and its velocity-reversed time-reversal are equally probable.
3. **K81b-A failed because the registered prediction was wrong, not because of the wave.** The validation that measured (A, B) had three defects:
   - It fitted a constant offset during ticks 1–6, while the zero-line-momentum start's offset was still building up (0 to 0.20 per place by tick 10). This biases A, by more at small tilts.
   - It assumed a single exponential, while the measured k = 0 response has a longer tail.
   - Its 64 seeds gave M2r's A a +1.9σ fluctuation.

   The full k = 0 response, summed as a Green–Kubo integral (the same at T = 8), gives:
$$
\Gamma=\tfrac13\Big[\tfrac12+\sum_{n\ge1}g(n)\Big]:\qquad \Gamma_{M2}=0.341,\ \ \Gamma_{M2s}=0.507,\ \ \Gamma_{M2r}=0.528 .
$$
   So the correct predictions were 0.645 ± 0.006, or **0.652** with the registered fit's nonlinear bias, and 0.961 for M2s.
   - The measured 0.676 ± 0.012 is 3.6% from 0.652, within the registered rule.
   - Independent runs at T = 8 give **0.658 ± 0.018**.
   - The residual sits mostly in M2r's registered set, which is 4.1% low (2.5σ); two independent M2r sets are 0.0% and −1.7% from prediction.
   - The mean field came closer only because its errors for M2 and M2r (−4.4%, −5.3%) cancel in the ratio.
   - The verdict is also fragile: ending the m = 3 and 5 windows at 1,500 ticks would pass it.
4. **The damping ratio is not a sign of one-wayness** (the check's main caveat).
   - Any rule's longitudinal wave is damped as its local k = 0 collision response predicts, whether the rule is reversible or not. A reversible rule with real μ ≈ 0.32 would damp exactly like M2.
   - What is specific to the one-way cycle is in the local response: Im μ = 0.289 ± 0.001, a rotating relaxation of the anisotropy, against 0.000 ± 0.002 for M2s and M2r.
   - The wave shows only what that local response predicts. A forward-running and a backward-running cycle damp alike, by the y ↔ z mirror, so the wave cannot show the cycle's direction at all.
   - **So Run 81's "the one-way cycle leaves a trace in how much the wave is damped" is withdrawn as stated.** So is the registered reading of a K81b-A failure.
5. **K81b-B** checks that M2s's wave follows from its own local response: 1.8 ± 3.7% from the corrected 0.961. It does not test irreversibility as such.
6. **Not predicted.**
   - M2's longest waves (m = 3, 5) damp about 10% more than its shorter ones allow (+10.3 ± 2.4% over three independent sets), only in this 4 × 4, zero-line-momentum ensemble. The excess is absent at T = 8, with Run 81's Poisson start, and in M2r.
   - This is the source of M2's low unscored slope, 0.925. It is likely a mode-coupling effect of the narrow geometry, and is not resolved.
7. **Smaller corrections.**
   - The ratio errors were computed by pairing seed groups across independent media, not in quadrature as registered: 0.012 against 0.016 for K81b-A. With quadrature, K81b-A still fails narrowly (10.9% against 10.5%) and K81b-B passes.
   - A and B were sampled as independent in the theory error, though correlated (0.63 for M2).
   - The zero-line-momentum state is a constrained ensemble: y and z var/mean 0.75, and the x axis holding 0.17–0.20 more per place. All of Run 81b's damping values belong to it.

**Reading.**
1. **A reversible bottom gives the same large-scale wave in form.** It carries viscous sound whose direction-telling share falls as 1/wavelength, as the one-way bottom's does. Run 81's missing control is now run: at large scales the averaged wave is two-way whatever the bottom, so the §5 statement that the accounts agree there is tested in the engine.
2. **The averaged wave does not show the arrow.** Its damping is set by the collision step's local response, whatever the bottom.
   - The one-way cycle shows in that local response, as a relaxation that rotates (Im μ ≠ 0). It does not show in the wave.
   - Measured against a correct prediction, the wave agrees with its local response to 1–4%.
   - **The arrow lives at the bottom and in the local response, and averaging to large scales hides it.** That is §5's statement, in a changing situation.
3. **The registered headline failed on a bad prediction method.**
   - Future registrations of this kind should predict from the full k = 0 response (the Green–Kubo sum), measured from an equilibrated start.
   - The registered verdict stays FAIL.
4. **Limits.**
   - These are longitudinal sound on the six-direction HPP lattice in a narrow geometry, with an unexplained 10% long-wavelength excess for M2.
   - The damping values belong to the zero-line-momentum ensemble.
   - Shear, which is what GR's waves are, is untouched.
