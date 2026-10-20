## 9t. Run 27: patterns falling in Candidate A′'s deep wells (was box 40 the problem?)

**Question.** In Run 22, Run 16's pattern-fall code check failed in Candidate A′'s deep wells in box 40: $a/a_{\rm pred}$ was 0.85–0.98, with masses up to 15% apart. Amendment 2 named two suspected causes, both untested:
- **H-face:** packets 14 out reach within 6 places of the box face.
- **H-curv:** the deep well is strongly curved across a packet.

Pre-registered: `PREREG_27.md`, hashed before any calculation; `fall60_run.zip`.

**Method (no engine runs; Run 22's T4′ already showed the engine's noise does not matter).**
- **The well.** The theory's smooth Candidate A′ well for ED's ball (radius 3, k = 1) at $p_s$ = 1, $P_0$ = 64, built in box 40 and in box 60.
- **The releases.** Run 16's `release`, code unchanged: width 4, a 16-tick fit, released at rest at 10, 14 and 18 places out along six axes, masses 0.7–2.0.
- **The test.** Run 16's code check: median $a/a_{\rm pred}$ in 0.96–1.00, and the masses alike to 1%.

**Results.**

| box | r | median $a/a_{\rm pred}$ (range) | largest mass spread | mean ∂ ln N | mean fall in 16 ticks | verdict |
|---|---|---|---|---|---|---|
| 40 | 10 | 0.894 (0.859–0.983) | 13.6% | 0.021 | 2.07 | fail |
| 40 | 14 | 0.942 (0.904–0.969) | 6.1% | 0.010 | 1.11 | fail |
| 60 | 10 | 0.894 (0.871–0.976) | 11.6% | 0.022 | 2.16 | fail |
| 60 | 14 | 0.957 (0.954–0.972) | 1.9% | 0.013 | 1.35 | fail (narrowly) |
| 60 | 18 | **0.986** (0.985–0.990) | **0.5%** | 0.007 | 0.78 | **pass** |

**Against the registered readings.** None of the three outcomes occurred exactly.
- **r = 10 fails in both boxes** (H-curv at 10).
- **r = 14 improves sharply in box 60 but still misses:** the mass spread falls from 6.1% to 1.9%, even though the box-60 well is steeper there. So the box face was part of the problem at 14.
- **r = 18 passes in box 60.** Both causes contribute.

**Reading.**
- **Patterns fall at the clock-set rate in Candidate A′'s well,** wherever Run 16's protocol can measure it. At 18 out in box 60 the fall is 0.986 of the prediction with masses alike to 0.5%. That is the same as Run 16's synthetic check (0.987–0.989) in the old engine's wells.
- **Closer in, the protocol fails, not the physics as far as this shows.** With a width-4 packet fit over 16 ticks, the mass spread grows with how far the packet falls in the window: 0.8 place passes, 1.4 places misses, 2 places fails badly. In box 40 the nearby face adds to it (6.1% at a 1.1-place fall).
- **Not tested:** whether a protocol built for steep wells (a shorter window scaled to the gradient, or a trajectory compared with a ray-traced prediction) would confirm the fall at 10–14 out.

![Run 27](figures/27_fall60.png)
