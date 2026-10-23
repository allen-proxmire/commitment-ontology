## Run 81: can averaging a one-way process give a two-way wave?

*23 October 2026.*
- *Registered and hashed before any run with a ripple (`wave81/PREREG_81.md`, 14:39:34 UTC), with the theory, the engine, the analysis and the job list. Validation runs and noise-only smoke runs made before registration are disclosed there.*
- *One amendment, `AMENDMENT_81.md`, hashed at 15:22:49 UTC. All 64 runs of the first medium (M1) crashed at start-up, because the sampler's table did not reach the ripple's peak. The table range was widened and nothing else changed, and M1 was re-run.*
- *An independent agent checked the run (below).*

**Question.** ONTOLOGY §5, item 1 (stated 23 October): **average a one-way process at a steady state, and the direction-telling terms cancel, leaving only the even ones.**
- In the engine this holds at a steady state. Off it, the engine's medium as first built diffuses, and diffusion is one-way.
- GR's well needs no wave: its potentials obey Poisson-type equations (Flanagan & Hughes 2005, §2.2), and R4 has the same structure.
- What GR has, and CO has only adopted, is **waves that are two-way while they travel**.

So: **can a process that is one-way at the bottom, once averaged, carry a wave whose direction-telling part fades at large scales? And what does that take?**

**The measure.** A long density ripple starts with no momentum, and its Fourier amplitude a(t) is followed. For an oscillating mode,
$$
a(t)\approx C\,e^{-\gamma t}\cos(\omega t+\phi),\qquad Q^{-1}=\frac{\gamma}{\omega}.
$$
- Running time backward turns the decay into growth. So γ is the direction-telling part and ω the two-way part, and Q⁻¹ is the direction-telling share.
- A pure two-way wave has Q⁻¹ = 0. Pure decay with no oscillation (overdamped) has Q⁻¹ = ∞.

**Four media.** All have a mean of 64 units per place, a hop of one place per tick, and periodic lattices.

| | medium | bottom | lattice, modes m (k = 2πm/L), seeds |
|---|---|---|---|
| **M1** | CO's medium as first built: R1's wander rule. A place sends Binomial(P, f(P)/P) units, each to one of six neighbours | one-way: 2.7×10⁻³ per place per tick (Run 29) | 128 × 8 × 8; m = 3–25; 64 seeds, 12,000 ticks |
| **M2** | Momentum kept: each unit carries a direction and moves one place along it each tick. At each place, K_a head-on pairs (one +a unit, one −a unit) rotate x → y → z → x, with ⟨K_a⟩ = q n₊n₋/(N − 1) and q = 1. Count and momentum are conserved at every place | one-way absolutely: no rotation ever runs the other way (a driven cycle, chosen as the rule) | 512 × 4 × 4; m = 1–25; 128 seeds, 4,000 ticks |
| **M3** | M2, then each unit reverses with probability r = 0.026: momentum lost at random | one-way | as M2; 3,200 ticks |
| **M2s** | M2, but a rotating pair goes to either other axis with probability ½ | every move can run back and no direction of rotation is preferred, but not in detailed balance (0.025 per place per tick; the check) | as M2 |

M2, M3 and M2s are candidates built for this question, not CO rules.

**The theory, fixed beforehand.**
- **M1,** from the mean-current identity with local equilibrium (z̄ = 5.9158, R′ = 44.404):
$$
\lambda(k)=1-\frac{1-\cos k}{3R'(\bar z)} .
$$
  This is one real eigenvalue at every k, so M1 is overdamped at every scale.
- **The momentum media,** from the exact linearised one-tick map on the six direction channels, M(k) = F C S. S is streaming, C the collision Jacobian at the measured collision rate (registered as 0.987 of mean field; 0.984 on the check, item 6), and F the reversals (M3 only).
- **Large scales:**
$$
\omega\to c_s k,\quad c_s^2=\tfrac13,\qquad \gamma\to\Gamma k^2\quad\Longrightarrow\quad Q^{-1}=\frac{\Gamma}{c_s}\,k .
$$
  - With momentum kept, the direction-telling share falls in proportion to k, that is, to 1/wavelength.
  - Γ = 0.33 for M2 (one-way bottom) and 0.50 for M2s.
  - Without momentum conservation (M3), modes below a boundary between m = 3 and m = 5 are overdamped.

**Results** (conservation exact in every run).

| m | k | M2: Q⁻¹ measured | theory | M2s: Q⁻¹ measured | theory | M3: Q⁻¹ measured | theory |
|---|---|---|---|---|---|---|---|
| 1 | 0.0123 | 0.0076 ± 0.0005 | 0.0071 | 0.0104 ± 0.0006 | 0.0106 | overdamped | overdamped |
| 3 | 0.0368 | **0.0214 ± 0.0008** | 0.0212 | 0.0319 ± 0.0019 | 0.0318 | overdamped | overdamped |
| 5 | 0.0614 | 0.041 ± 0.002 | 0.035 | 0.056 ± 0.003 | 0.053 | 1.5 ± 0.5 | 1.28 |
| 9 | 0.1104 | 0.067 ± 0.005 | 0.064 | 0.093 ± 0.007 | 0.096 | 0.56 ± 0.05 | 0.55 |
| 15 | 0.1841 | 0.114 ± 0.006 | 0.108 | 0.143 ± 0.009 | 0.161 | 0.36 ± 0.04 | 0.38 |
| 25 | 0.3068 | 0.18 ± 0.02 | 0.19 | 0.24 ± 0.02 | 0.27 | 0.26 ± 0.04 | 0.36 |
| slope, m = 3–25 | | **0.990 ± 0.033** (weighted: 1.019 ± 0.033) | 1.029 | 0.936 ± 0.043 (weighted: 0.932 ± 0.040) | 1.013 | | |

- **M1** is overdamped at every mode: no ripple ever crosses zero, and the statistic is ≥ +4.5. Its decay rates match the theory to −1.1%, −0.3%, −0.3% and +1.0% at m = 3–15, within errors of 2–4%. At m = 25, five places per wavelength, it is −2.4% (reported).
- **Rotations.** M2 and M3 rotate 5.33 pairs per place per tick, all one way. M2s rotates 2.667 each way, balanced to within 1.5σ.

![Run 81](../figures/81_wave.png)

**Verdicts as registered.**
- **K81a, the headline: PASS.** M2's direction-telling share falls as k^(0.99 ± 0.03) (the weighted fit gives 1.02 ± 0.03), and Q⁻¹ = 0.021 at m = 3.
- **K81b, M2 against its theory: PASS.**
  - ω is within 0.9% at every mode.
  - γ is within its tolerance at every mode. The largest deviation is +17 ± 6% at m = 5, inside 3σ.
- **K81c, M1 overdamped and matching its theory: PASS.**
- **K81d, M3: UNDECIDED.**
  - Its structure holds:
    - overdamped at m = 1 and 3;
    - oscillating at every m from 5 to 25;
    - Q⁻¹ above M2's at m = 5–15 by more than 3σ.
  - But its ω at m = 5–25 (errors 4–13%) is too imprecise for the registered 3% tolerance, and at m = 25 M3 and M2 are not separated.
- **K81e, M2s: UNDECIDED** on one item. M2s's ω at m = 25 (±5%) is too imprecise for 2%. Every other item passes, and the slope is 0.94 ± 0.04.
- **Bookkeeping: PASS.**

**Not predicted (found in the results).**
- **Sound frequency.** M2's and M2s's sound frequencies sit 0.4–0.7% above the linear theory at the largest scales:
  - M2: +0.53 ± 0.05% at m = 1 and +0.62 ± 0.10% at m = 3;
  - M2s: +0.42 ± 0.07% and +0.61 ± 0.20%.
  That is inside the tolerance but not explained by the registered theory, whose deterministic nonlinear check gave below 0.04%. The check found the cause (item 2 below).

**What the check added.**
1. **Independent reproduction.**
   - Every hash matches, apart from the amended `engine81.py` as disclosed. Every output is later than the registration, and each of the 448 jobs ran once with the registered parameters.
   - The four aborted-launch outputs are byte-identical to their re-runs, and two seeds of each medium re-run byte for byte.
   - The checker's own linear maps reproduce all 23 registered predictions to 3×10⁻¹⁰. Its hand derivation of the large-scale limit gives Γ = 0.3319 (M2) and 0.4980 (M2s).
   - Re-running the analysis reproduces it exactly. **All six verdicts stand as computed,** and no correction below changes any of them.
2. **The sound-speed offset is a lattice artefact.**
   - The six-direction lattice conserves momentum on every lattice line and on each of two sublattices that never interact. So the random start freezes in a transverse flow that never relaxes, and that flow stiffens the sound:
$$
\frac{\delta\omega}{\omega}=\frac{3\big(\langle J_y^2\rangle+\langle J_z^2\rangle\big)}{4\bar P^{2}}=\frac{1}{T\bar P}=0.39\%\qquad(T=4,\ \bar P=64).
$$
   - Across nine run sets (no frozen flow, T = 2, 4, 8, a boosted flow), measured = (0.03 ± 0.02)% + (1.01 ± 0.05) × predicted, with χ² = 7.9 for 7 degrees of freedom.
   - Anything else that shifts ω, such as mode coupling, is at most about 0.08% at m = 1.
   - These are the defects of the three-dimensional HPP lattice gas (Hardy, Pomeau & de Pazzis 1973), which is what M2 is; FHP was designed to remove them. The registration cited FHP.
3. **M2s is not a reversible bottom.**
   - Its rotations have no preferred cycle (2.6665 each way per place per tick). But its moves are not in detailed balance: the move-level entropy production is 0.0247 ± 0.0003 per place per tick, about 9 times M1's.
   - So **K81e compares two irreversible bottoms** and does not test the §5 statement that the two accounts agree. A reversible control is still missing.
4. **The two bottoms can be told apart, through the damping's size.**
   - Γ(M2s)/Γ(M2) = 1.49 ± 0.10, against 1.500 from theory. The one-way cycle relaxes the medium's anisotropy with a rotation (a complex eigenvalue), which lowers the damping; a rule in detailed balance cannot do that.
   - What the two share is Q⁻¹ → 0 at large scales. The registered sentence "the averaged wave cannot tell which kind of bottom it came from" is withdrawn.
5. **Q⁻¹ → 0 at large scales is generic.**
   - Any medium that conserves a current gives it, whatever its bottom: γ = Γk², so Q⁻¹ ∝ k. So the run shows that averaging *can* give a two-way wave from a one-way bottom; it cannot show where the arrow lives.
   - Q⁻¹ = γ/ω is 1/(2Q) in terms of the standard quality factor.
   - The run shows a conserved current is enough. With the current lost at rate 2r, waves vanish at scales beyond k_c (M3), so the defensible wording is **"a conserved current is needed for waves at all scales"**, not "the condition".
6. **Corrections to the registration, none changing a verdict.**
   - The collision rate is 0.9842 of mean field, not 0.9872: the validation used one seed whose density happened to be 64.17. This raises the predicted γ by 0.4–0.5%.
   - The registered slope is the unweighted fit, with an error computed as if weighted. The weighted slopes are M2 1.019 ± 0.033 and M2s 0.932 ± 0.040; both pass.
   - "Combined 3σ" was coded as 3(σ₁ + σ₂), not in quadrature. M3's m = 25 item is undecided either way.
   - The amendment's "about 66 units per place" should read 72.4. The amended engine no longer reproduces the hashed M1 smoke file.
7. **Fragile items.**
   - M3's oscillation at m = 5 depends on the registered window: 8.2σ on it, 1.3σ on a longer one. The thermal noise at m = 5 does oscillate, so it is real.
   - "Overdamped" at M3's m = 1 and 3 excludes only strong oscillation.
   - M2's γ at m = 5 (+16.7%) passes only through its 3σ allowance.
8. **M1.**
   - Its decay rates agree with the theory to −0.2 ± 1.2%, weighted over m = 3–15.
   - Its stationary law is not exactly the product law (variance 3.4% low), but the coefficient the theory uses is right to 0.1%.
   - "Overdamped" holds by construction, since M1 has no momentum.
9. **The GR statement is confirmed** (Flanagan & Hughes 2005, §2.2, Eqs. 2.62–2.65), including ∇²Ξ_i = −16πS_i, which the ontology had left out. In GR the well needs no wave because of the constraint (gauge) structure, not because of averaging, so the comparison with R4 is one of structure only.

**Reading.**
1. **Averaging a process that is one-way at the bottom can give a wave that is two-way at large scales, while things change.**
   - In M2 the direction-telling share of a density wave falls as k^(1.00 ± 0.03), that is, as 1/wavelength, to 0.021 at the largest scored scale.
   - **What it takes: a current conserved through the one-way updates.** CO's medium as first built (M1, random hops) has none, and is one-way at every scale. Losing the current at random (M3) sends the large scales back to one-way.
   - So the §5 statement extends from steady states to changing ones, for a medium that keeps a current.
2. **This is ordinary lattice-gas sound, and the same happens with any bottom.**
   - The large-scale result does not depend on the bottom being one-way: lattice gases with reversible collisions give the same (known physics, not run here). So it does not locate the arrow, which fits §5: at large scales the averaged accounts agree.
   - The one-way cycle leaves a trace in how much the wave is damped (Γ 0.33 against 0.50), not in whether it is two-way.
   - A reversible control, to show that the leftover is the cycle's and not M2s's own irreversibility, was not run.
3. **What it does not reach.**
   - These are longitudinal sound waves at 1/√3 of a hop per tick. GR's waves are transverse shear at light speed.
   - A fluid carries shear only by diffusion, and this six-direction lattice does not move transverse momentum along x at all. A two-way shear wave needs, besides a conserved current, a restoring force for shear: in CO's terms, the relations' tension (Run 11b).
   - How a conserved current would arise from commitments is not addressed.
4. **For CO.**
   - The engine's medium (R1, R4) carries no current. A medium that carried sound would radiate scalar waves from binaries, which Run 11b bounds to at most about 10⁻⁴ of GR's radiation.
   - So the current belongs, if anywhere, to the carriers of CO's waves (the relations' shear, and patterns), not to the well.
   - The same current is what R10's circulating flow and Run 34's momentum channel need.
   - **Next:** whether the relations can carry a conserved current with a restoring force for shear (a design note).
