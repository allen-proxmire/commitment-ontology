## 9zb. Run 35: the engine on the adopted rules (a construction run)

*19 October 2026. Allen: "adopt, clock field fixed each tick, and patterns ride possibility's flow… the lattice tick is not physical time", and on the input, "you chose". Pre-registered and hashed before any registered run (`adopted/PREREG_35.md`, 10:10 UTC), with the engine, the theory and the analysis. An independent agent re-ran the analysis (byte-identical), checked the engine against engine22 and the registration's timing, and re-derived the physics claims; its corrections are included.*

**What this run is.**
- The rules are adopted by ruling, so nothing here can refute them. Every check compares the engine with what the rules imply, computed beforehand. A failed check would have meant the build was wrong, so there is no kill rule.
- One item (D35) bears on a claim from an earlier run: Run 29's post-hoc reading that the clock record's long one-way tail needs memory in the medium.

**The engine on Candidate A″** (`engine35.py`, `zrp35.py`).
- **The medium (part 1).** The wander rule is a zero-range process: a place holding n units sends out $f(n)=c\ln(1+n/p_s)$ a tick on average, evenly to its six neighbours. For given draws its stationary state is the product measure
  $$
  \pi_x(n)\;\propto\;\frac{z_x^{\,n}}{\prod_{k\le n}f(k)},\qquad \tfrac16\sum_{y\sim x}z_y-z_x=s_x-\bar s ,
  $$
  where the fugacity $z_x=\langle f(P_x)\rangle$ solves the engine's exact outflow equation (Run 31) for the current draws $s_x$.
  - "Possibility relaxes completely between commitments" means: each tick the medium is an independent draw from π, conditioned on the conserved total. Units held by live commitments are off the lattice, as before.
  - The draws are each pair's expected draw, $(\bar P_a+\bar P_b)/\text{hold}$ at each of its places, solved self-consistently (theory27's method). A rigid body's relaxed field translates with it.
- **Unchanged:** matter as reserved pairs under the presence clock, the order within a tick, and a vacuum that never commits.
- **Patterns riding a flow** (C1, and the input's current field). A pattern is carried by the flow $\mathbf v=-g_{0i}$ in the convective form
  $$
  D\psi=\nabla^2\phi-m^2N^2\phi,\qquad \psi=D\phi,\qquad D=\partial_t+\mathbf v\cdot\nabla ,
  $$
  which is Run 16's equation when v = 0. Possibility's conservation flow and the input's current field are computed by `flow_u` and `current_V` for later runs.

**Runs.** P₀ = 64, p_s = 1, seed 1 (clocks: seeds 1 and 2).
- **V:** the vacuum, box 40, 2,000 ticks.
- **S:** Run 26's ball (radius 3, 54 pairs), box 40, 20,000 ticks.
- **M1:** the ball stepping +1 in x every 667 ticks ($w=1.5\times10^{-3}$, as in Run 31), 40,000 ticks.
- **MF:** the ball stepping every 4 ticks ($w=0.25$, about 167 times faster), 20,000 ticks. It went round the box about 125 times (119 within the read window).
- **K:** Run 29's 125 lone probe clocks, box 30, 2 × 200,000 ticks.

**Results against the registration.**

| | check | measured | predicted (before any run) | verdict |
|---|---|---|---|---|
| C35a | the relaxed vacuum | mean 64 exactly, total fixed every tick; var/mean **4.1021** | 4.1044 (the diffusive engine: 3.975) | pass |
| C35b | static ball | draw **8.5492** per tick; shell means r = 4–15 within a relative **1.7×10⁻⁴** of theory | 8.5451 (Run 26 measured 8.54) | pass |
| C35c | moving ball, $w=1.5\times10^{-3}$ (moved 59) | α **−0.0020**; lateral ratio **1.0008**; draw ratio **0.9997** | 0, 1, 1. Run 31 (diffusive): **+0.672, 0.537, 1.085** | pass |
| | moving ball, $w=0.25$ (moved 4,999) | α **−0.0024**; lateral **1.0013**; draw ratio **0.9990** | 0, 1, 1 | pass |
| D35 | clock rate | **0.16641** per tick | 0.16641 (mean field) | pass |
| **D35a** | presence leads completions by one tick | D(1) = **+0.0857 ± 0.0002** | +0.0857 ± 0.0002 (model). Run 29: +0.0343 | **pass** |
| **D35b** | **the long one-way tail** | mean D over τ = 20–120: **(+0.1 ± 0.2)×10⁻⁵** | 0. Run 29: **+8.3×10⁻⁴** | **pass**: the tail is gone |

**Notes on the table.**
- The static ball's own α is −0.0018, so the moving balls' −0.002 comes from the ball's layout, not from motion.
- The model behind D35 is an integrate-and-fire clock fed an independent presence each tick. It shares no code with the engine's clock step.
- C35a's 4.1021 against 4.1044 is about 4σ. It is the expected bias of the approximate conditioning on the total, about −0.06%, well inside the criterion.

![Run 35](figures/35_adopted.png)

**Reading.**
1. **The build does what the rulings say.**
   - The static ball agrees with the zero-range steady state to 0.05% in draw and a relative 1.7×10⁻⁴ in its shells. That is agreement with the theory the build implements.
   - **Against the diffusive engine** (Run 26's same ball, two seeds; post hoc, not registered):
     - the draw agrees to 0.1%
     - the deficit agrees to 0.4% at r = 4
     - Run 35's deficit is 2–4% deeper at r = 7–13, and about 10% at r = 15, where it is under one unit
     - The difference may be Run 26 not quite reaching the steady state at box scale (relaxation time about 10⁴ ticks), or the two media's slightly different single-place laws (var/mean 4.10 against 3.98). The run does not separate them.
   - A moving body keeps its well and its draw at both speeds. Run 31's wake and its 8.5% excess draw are gone, at about 167 times Run 31's speed as well.
   - All of this follows from the rules by construction. The run checks the build, not ED.
2. **What D35 shows about Run 29's tail.**
   - With presence drawn independently each tick, D(τ ≥ 2) = 0 is what an integrate-and-fire clock must give. So D35b mainly confirms that the build's presence is independent, and that the clock alone carries no long tail.
   - It follows that Run 29's tail needed memory in the medium between ticks. Two such memories were present in Run 29:
     - ambient fluctuations of possibility
     - the clock's own reservation hole: each renewal takes a unit from each of its places, and the hole relaxes over tens of ticks, exactly the τ = 20–120 window
   - Part 1 removes both, and this run does not separate them. What remains is the clock's own lead: presence at one tick raises the chance of a completion at the next (D(1) = 0.086).
3. **Averaging over time still removes the order.** For a clock fed independent presence the window statistic is, to a good approximation,
   $$
   A_T\approx\frac{q}{\sqrt{T\,(Tq^2+g_T)}},\qquad q=\frac{\mathrm{sd}(X)}{H}=\frac{20.4}{640},\qquad g_T=f(1-f),\ f=\mathrm{frac}(rT),
   $$
   where r is the clock rate, and $g_T\to\tfrac16$ once the window count spreads. This formula was derived by the independent check after the run.
   - It reproduces T = 1–16: 0.0854, 0.0477, 0.0335, 0.0235 and 0.0163, against 0.0857, 0.0474, 0.0334, 0.0244 and 0.0159 measured.
   - So $A_T$ falls as $T^{-1/2}$ while $Tq^2\ll\tfrac16$ (to T ≈ 100), then as 1/T.
   - At T = 1024 and 2048 the measured −0.0036 ± 0.0021 and −0.0042 ± 0.0018 sit 2.1σ and 2.6σ below that expectation (+0.0009, +0.0005). The independent model, with the same estimator, scattered +1.8σ at T = 1024. With about ten windows per jackknife segment, the errors at large T are rough.
   - Either way the order fades with averaging, as K29 required.
4. **Where the arrow lives under the adopted rules** (derived, not run).
   - A vacuum redrawn independently each tick has no arrow at tick resolution by construction. The question is whether the relaxed law itself hides a current. It does not: in the vacuum it is in detailed balance with the wander rule's continuous-time process,
     $$
     \pi(\eta)\,\frac{f(\eta_x)}{6}=\pi(\eta^{x\to y})\,\frac{f(\eta_y+1)}{6},
     $$
     because $\pi(\eta^{x\to y})/\pi(\eta)=f(\eta_x)/f(\eta_y+1)$ for the product measure at uniform fugacity.
   - Run 29's T1 (the vacuum's wandering one-way at 2.7×10⁻³ per place per tick) is then attributable to updating every place at once. A synchronous update need not be reversible even when its continuous-time version is. Part 1 replaces that update with the relaxed law.
   - The arrow then lives in three places:
     - commitments, which are one-way by rule
     - the steady inflow of possibility into matter, a driven current that detailed balance does not cover
     - how clocks integrate presence (D35a)
   - That is in line with "the vacuum never commits": time's direction belongs to commitment, not to the medium.
5. **Ready for later runs.** The engine now has a field that is the steady state at every tick, moving bodies, possibility's flow, and the input's current field, all available to patterns.
   - The pattern–flow coupling was checked only on given flows. These checks are deterministic and were run before registration as code checks: in a uniform flow the drift is 0.990 of $v_0T$ (the lattice gradient takes 1%); in a sheared flow it is 0.970 of the starting density-weighted flow, as the packet spreads into slower flow.
   - Not done here: frame dragging on a pattern near a rotating body, signalling through the constraint, pattern energy, the strong field.

**Corrections to the registration's disclosures** (`PREREG_35.md` is hashed and unchanged).
- The smoke-test outputs (seeds 98 and 99) were deleted from `runs35/`. Renamed copies used to test `analyse35.py` (named `_s1`, `_s2`) remained in a scratch folder until after this check. They are not the registered streams: their clock presence matches the registered records on 1.4% of entries.
- The unconditioned draw's total varies by about ±4,100 units (one standard deviation), not ±1,500.
- `analyse35.py` labels Run 29's tail error "reported only", but it enters D35b's criterion. The margin is about 220σ, so this changes nothing.
