## Run 78: does the engine's own equation of state explain the clock theory's offsets?

*23 October 2026. Step (0) of the spherical design note (Note G). Registered and hashed before any registered run (`eos78/PREREG_78.md`, 10:22:52 UTC). The raw offsets were already known from Runs 72b–76, and a rough expectation (that the correction would be too small for design 2) was stated in the registration. An independent agent checked the run (below).*

**Question.** Since Run 72, the zero-range clock theory of Run 72 has slightly underestimated the clocks' own dips. Pooled over five lattices (high medium, p_s = 1), the offsets are +0.238 ± 0.032% for design 1 and +0.359 ± 0.093% for design 2. The design note's check found that the engine's parallel update does not have the zero-range equation of state: at given z = ⟨f(P)⟩ the mean P falls below R(z), more at low P and in proportion to a place's total link weight S. A clock depletes its own places. **Does correcting the theory for the engine's own equation of state remove the offsets?**

**Part 1: the engine's equation of state.**
- **Setup:** uniform 24³ lattices, every link weight w, no clocks, the engine of Runs 70–76 unchanged.
  - S = 6w = 2.40, 2.68, 3.44, 4.5 and 6.0: the clocks' own S on the five lattices, and the range of ambient S.
  - P = 40–68; two seeds; 20,000 ticks, read over the last 18,000.
- **Measured:** z̄ = ⟨f(P)⟩ over places and ticks, and
$$
\delta(P,S)=\frac{P}{R(\bar z)}-1 .
$$

| P | S = 2.40 | 2.68 | 3.44 | 4.5 | 6.0 |
|---|---|---|---|---|---|
| 40 | −0.099% | −0.105% | −0.138% | −0.182% | −0.240% |
| 48 | −0.075% | −0.079% | −0.109% | −0.136% | −0.187% |
| 56 | −0.061% | −0.068% | −0.083% | −0.112% | −0.149% |
| 64 | −0.046% | −0.055% | −0.074% | −0.090% | −0.121% |

- Seeds and halves agree to about 0.01%. Conservation is exact.
- At S = 6, P = 64 this reproduces the design note's check (−0.12%). The departure grows roughly in proportion to S and as P falls.

**Part 2: the corrected theory.** In Run 72's theory P_own,j = R(z_amb + dz_j), with dz = M r and r_j = 2P_own,j/(jH). Corrected:
$$
R_{\rm eng}(z;S)=R(z)\,\big(1+\delta(R(z),S)\big).
$$
- The clocks' places use their own S. The ambient fugacity solves R(z_amb)(1 + ⟨δ(P_amb, S_x)⟩) = P_amb over the non-clock places.
- M is unchanged, since the mean-current identity is exact.
- Validation, before registration: with δ ≡ 0 the corrected theory reproduces theory72/75's dips to 10⁻⁶.

**Results** (off_j = measured dip / theory dip − 1; seed counts 5, 20, 60, 20, 20).

| cell | design 1, raw | design 1, corrected | design 2, raw | design 2, corrected |
|---|---|---|---|---|
| flat | +0.34 ± 0.13% | +0.27 ± 0.13% | +1.06 ± 0.64% | +0.99 ± 0.64% |
| s = +1 | +0.22 ± 0.05% | +0.19 ± 0.05% | +0.70 ± 0.22% | +0.70 ± 0.22% |
| s = −1 | +0.20 ± 0.05% | +0.18 ± 0.05% | +0.15 ± 0.12% | +0.19 ± 0.12% |
| a = e^−1 | +0.37 ± 0.11% | +0.31 ± 0.11% | +0.64 ± 0.24% | +0.58 ± 0.24% |
| a = e^+1 | +0.29 ± 0.12% | +0.19 ± 0.12% | +0.40 ± 0.31% | +0.31 ± 0.31% |
| **pooled** | **+0.238 ± 0.032%** | **+0.200 ± 0.032% (6.2σ)** | **+0.359 ± 0.093%** | **+0.361 ± 0.093% (3.9σ)** |
| χ² (4 dof) | 2.9 | 1.6 | 7.6 | 6.0 |

![Run 78](figures/78_eos.png)

- **K78a, design 1: NOT EXPLAINED.** The correction removes 16% of the offset; 6.2σ remains.
- **K78a, design 2: NOT EXPLAINED.** The correction removes none of it; 3.9σ remains.
- **Why the correction is small.** It changes a clock's dip by the difference between the departure at its own places and the ambient one. At the flat lattice that is −0.095% − (−0.055%) = −0.04% of P for design 1 and −0.02% for design 2, about 0.1% of the dip.

**What the check added.**

1. **Independent reproduction.** All 14 hashes match, and the hash came after every script and smoke file and 195 s before the first output. All 80 jobs ran once with the registered parameters; conservation is exact in all of them. The checker's own spot measurements of δ agree (−0.120% at S = 6, P = 64; −0.112% at S = 4.5, P = 56), seed pairs agree within their errors, and δ is proportional to S (fit intercepts within ±0.005%). Its own Green's function reproduces M to 10⁻¹⁵, and the corrected dips, pooled offsets and verdicts match.
2. **The verdict follows the registered rule; the reading was overstated.** The run tests one model: the uniform-lattice δ, applied with Run 72's ambient normalisation. It does not rule out the parallel update as a cause, and it does not show the offsets are a failure of the zero-range description.
3. **The offsets come mostly from the theory's ambient normalisation** (the check's calculation, after the offsets were known; not registered).
   - **Level.** Run 72's theory evaluates the clocks at P_amb = 64. But the total is conserved, Σ_x P_x + 2N_on = 64V, and the clocks' depleted places and held units push about 0.13 per place into the rest. The measured non-probe ambient is 64.13–64.15 (flat 64.1339 ± 0.0003). Since a clock's draw is proportional to its own P, the dip rises with the level: at 64.134 the theory's dips rise by 0.13% (design 1) and 0.16% (design 2), a second calculation reproduced in the record's own code.
   - **Mean over places.** The clocks' neighbours are depleted, so z varies over the non-probe places, and R is convex: the place-mean exceeds R(z̄) by ½R″·Var(dz), 0.02–0.05%.
   - **The consistent theory has no free parameter:** P_x = R_eng(z_a + Σ_l r_l g_l(x); S_x), with z_a fixed by the conserved total and the dip taken against the place-mean. It predicts the measured ambient to 0.0006 units in all five cells (and to 0.0002 in three low-medium cells Run 78 did not use), and the measured place-mean excess to within its error (+0.0142 ± 0.0003 against +0.0146, flat).

| pooled offset | raw | Run 78 (δ) | + ambient | + ambient + δ | + ambient + δ + clock-place term (item 4) |
|---|---|---|---|---|---|
| design 1 | +0.238 ± 0.032% | +0.200% | +0.039% | **+0.001 ± 0.032%** | −0.058 ± 0.032 ± 0.013% |
| design 2 | +0.359 ± 0.093% | +0.361% | +0.065% | **+0.066 ± 0.093%** | −0.097 ± 0.093 ± 0.017% |

   - **Design 2's lattice dependence remains.** At s = −1 against the four other lattices, design 2 differs by −0.38 ± 0.19% (2.0σ) after the normalisation, against −0.48 ± 0.19% raw. The normalisation removes a common part and leaves Run 76's question where it was.
4. **At a clock's own places δ is not the whole story, but the rest nearly cancels.** In the checker's own engine runs (36³, 216 clocks, 10 runs), each clock's draw follows r_j = 2⟨P_own⟩/(jH) to 10⁻⁵. Two effects at the clock places each exceed δ·P: the reading-time shift (+0.14 and +0.08 units) and a one-place law 9–12% narrower than the zero-range one. They have opposite signs and nearly cancel, leaving 0.015–0.023 units beyond δ. That moves the pooled offsets by −0.06 (design 1) and −0.16 (design 2) points.
5. **Minor.** The clocks' own S are grid points on three lattices; s = ±1's are interpolated, which is harmless since δ is linear in S. The δ grid stops at P = 40, so low-medium cells cannot be corrected with it.

**Reading.**
1. **As registered, the engine's own equation of state does not explain the clock theory's offsets.** Corrected place by place, it removes a sixth of design 1's offset and none of design 2's. This tests only the uniform-lattice part of the update's equation of state, applied with Run 72's ambient normalisation.
2. **The check found where most of the offsets come from: the theory's ambient level.** Evaluated at the ambient that the conserved total actually gives (64.13–64.15, not 64), and averaged place by place, the theory's offsets fall to +0.00 ± 0.03% (design 1) and +0.07 ± 0.09% (design 2). That is a calculation made after the offsets were known, not a registered result.
   - The statement in Run 76 (reading 2) and in §3 that the zero-range theory underestimates the clocks' own dips by 0.25% and 0.5–0.6% is **withdrawn as stated**: most of it is this normalisation.
   - A registered test would put the corrected theory where the ambient shift is larger, for example Run 72's dense layout of 864 clocks (about four times the shift), with its predictions hashed before running.
3. **Design 2 at negative curvature is still about 2σ off the other lattices** (−0.38 ± 0.19%). That is Run 76's open question, untouched by the normalisation.
4. **The engine's parallel update has a measured equation of state.** At the occupancies of Runs 70–76 it differs from the zero-range one by 0.05–0.24%, growing as P falls and in proportion to S. Any theory at low P, such as the spherical hole of Note G, needs it.
