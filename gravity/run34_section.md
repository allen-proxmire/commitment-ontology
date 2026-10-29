## Run 34: a clock field fixed each tick, plus a current field — can it pass the preferred-frame tests? (a calculation)

*19 October 2026. The criteria and candidate rules were fixed and hashed before the numerical check ran and before the record search on frame dragging was read (`vector/PREREG_34.md`, 09:21 UTC). The general relation had been sketched in conversation while scoping, and was registered as a prediction. An independent agent re-derived the matching against Will (2014, Box 2 and Table 4) and GP-B's final result. It confirmed the algebra and found eight problems in how the result was stated; all are corrected below, and listed at the end.*

**Question.** Run 31 showed the engine's field is carried by diffusion. The proposed fix has three parts:
1. The clock field is fixed fresh each tick: possibility relaxes completely between commitments, so the field is the steady state for the current draws.
2. A current field ($g_{0i}$) is sourced by moving matter.
3. Radiation is shear of relations (Run 11b).

Part 1 keeps every static result and removes the wake. The question here is what part 2 must be for the preferred-frame tests to pass, and whether anything in CO supplies it.

**Prior record (checked after the registration, before writing up).** Much of this is already in CO's Phase-3 GR notes. Run 34 puts numbers to it and adds one derived piece.
- **`Phase3_GR_PPN_RouteB_EtaCrossCheck.md`:** "The scalar rule `ḃ = D∇²b − κρ`, by itself, sources no physical `g_{0i}`", because its current is curl-free, and "the conservative skeleton leans `α_1=O(1)`". Run 34 gives the number: α₁ = −8, α₂ = −1.
- **`Phase3_GR_DirectedFluxSector.md`:** a directed flux, $D\nabla^2A^i=\kappa_J\rho w^i$ with $g_{0i}=A_i$ and $\kappa_J=\lambda_J\kappa$, "kept symbolic". That is candidate C2.
- **`Phase3_GR_PinningLambdaJ.md`:** boosting the static metric gives $g'_{0i}=4w_iU$, so "α₁ = 0 ⟺ λ_J = 4". It adds that "ED's rule is not boost-covariant" and that the naive estimate is λ_J ~ O(1), "not computed". Run 34's $k_1=-4$ is the same condition.
- **`GR_SC_2_0_Consolidation.md`:** "No magnetic Weyl, no frame-dragging" in CO's static acoustic metric.
- **Paper 046** (Kerr twist): frame dragging is "INHERITED".
- **`Phase3_GR_Alpha2_Vanishes_Alpha1_Reconciled.md`** and **GR-IV:** α₂ = 0 and $\alpha_1=-4c_{14}\approx10^{-93}$, from khronometric formulas with both speeds tuned to c. The 12 September review marks α₂ = 0 "not established".
- **Not in the record:** α₂ = 0 coming out of possibility's own conservation (C1 below), given C1's principle and two stated premises.

**The calculation** (`run34.py`). In the lattice frame, taken as the PPN preferred frame, the engine family has:
- $g_{00}=-N^2$, $\ln N=-U_{\rm eff}$, with $U_{\rm eff}$ instantaneous (part 1). There are no $\mathcal A$, $\mathcal B$ or $\Phi_W$ terms, and the motion weight is $a_1$ in proper-density terms.
- $g_{ij}=N^{-2}\delta_{ij}$, so γ = 1.
- $g_{0i}=k_1V_i+k_2\chi_{,0i}$, with $V_i=\int\rho'v'_i/|x-x'|$, $\chi=-\int\rho'|x-x'|$ and $\chi_{,0i}=V_i-W_i$.

With isotropic $g_{ij}$ and no $\mathcal B$ term, the only time relabelling left at this order ($t\to t+\lambda\chi_{,0}$) would add a $\mathcal B$ term, so λ = 0: the lattice frame is already in Will's standard gauge, and coefficients can be read off directly. Matching term by term gives, exactly:
$$
\xi=0,\qquad \zeta_1=0,\qquad \alpha_1=-2k_1-8,\qquad \alpha_2=2k_2-1,\qquad \alpha_3=2a_1-4 .
$$
- **GR** is $k_1=-4$, $k_2=\tfrac12$, $a_1=2$ (conserved-density weight $\tfrac32$).
- **The bounds** (Will 2014, Table 4) are $|\alpha_1|<4\times10^{-5}$ (binary pulsar PSR J1738+0333; lunar laser ranging gives 10⁻⁴), $|\alpha_2|<2\times10^{-9}$ (millisecond pulsars) and $|\alpha_3|<4\times10^{-20}$ (pulsar period derivatives). Any rule, derived or chosen, must therefore give
$$
|k_1+4|<2\times10^{-5},\qquad |k_2-\tfrac12|<10^{-9},\qquad |a_1-2|<2\times10^{-20}.
$$
- **Frame dragging is the same test as α₁.** For a stationary rotating body $\chi_{,0}=0$, so $g_{0i}=k_1V_i$, and frame dragging is $k_1/(-4)=1+\alpha_1/8$ of GR's. Gravity Probe B measured 37.2 ± 7.2 mas/yr against GR's 39.2, a test of $k_1/(-4)$ to 19%. The α₁ bound tests the same number to about 5×10⁻⁶, some 10⁴ times tighter. The registration listed frame dragging as a separate test; it is not.
- **Checks.** The linear matching was also solved directly and agrees with the closed forms. The grid computations are consistency checks only:
  - $\chi_{,0i}=V_i-W_i$ holds to 2% on a free-space grid (finite-difference error);
  - the flow below matches its formula to 6%, which re-checks the identity $\nabla^{-2}\partial_tU=-\tfrac12\chi_{,0}$;
  - its curl is zero to 10⁻¹⁶ automatically, because the flow is built as a gradient;
  - the far-field form $W=U(\mathbf w\cdot\mathbf n)\mathbf n$, listed in the code's docstring, was not checked.

**The candidates.**

| | rule | k₁ | k₂ | α₁ | α₂ | frame dragging (fraction of GR) | status |
|---|---|---|---|---|---|---|---|
| C0 | part 1 with no current field ($g_{0i}=0$) | 0 | 0 | **−8** | **−1** | 0 | excluded |
| C1 | possibility's own flow carries patterns, $g_{0i}=-u_i$ (the acoustic metric) | 0 | **½** | −8 | **0** | 0 | k₂ derived (given the principle and premises below); excluded on α₁ |
| C2 | C1, plus matter's momentum sourcing a current field by the same Poisson law as the draw, strength k₁ | −4 if chosen | ½ | 0 | 0 | 1 | passes only with **k₁ = −4 put in** and $a_1=2$ put in |
| C3 | the field of a moving body is its boosted rest field | −4 | ½ only after relabelling time | 0 | 0 | 1 | GR put in by hand; in lattice time it conflicts with part 1 (below) |

For C0–C2, α₃ = 0 needs the motion weight $a_1=2$, which is Run 33's R-b (energy plus momentum flux); R-a gives α₃ = −2. C3 brings its own $a_1=2$ with the boost.

**C3 in lattice coordinates.** Boosting the rest field, with the lattice's own time, gives $g_{0i}=-4V_i$ (k₂ = 0) and an $\mathcal A$ term in $g_{00}$ from Lorentz contraction. The ½ in $g_{0i}$ and $a_1=2$ appear only after relabelling time, $t\to t-\tfrac12\chi_{,0}$, which removes the $\mathcal A$ term. If lattice time is physical, as CO's global tick says, that relabelling is not free, and C3's $g_{00}$ (with an $\mathcal A$ term) contradicts part 1's (none). So C3 is not a third route; it is GR assumed, at the cost of part 1 or of the tick's meaning. C2 has no such conflict: part 1, C1 and $k_1=-4$ together are GR's standard gauge written in lattice time.

**Why C1's k₂ = ½ is derived (given C1's principle).**
- Under part 1, a moving body's deficit $\delta P=-P_0U(x-wt)$ moves with it. Conservation then forces possibility to flow, with $\nabla\cdot\mathbf u=\partial_tU$ (u = flux/P₀).
- The engine's mean flux is always a gradient, $\mathbf J=-\tfrac16\nabla z$, so the flow is irrotational. That gives
$$
\mathbf u=-\tfrac12\nabla\chi_{,0}.
$$
- If patterns ride possibility's flow ($g_{0i}=-u_i$), this is exactly GR's $+\tfrac12\chi_{,0i}$, and α₂ = 0, with no number chosen.
- **Premises, stated.**
  - *Normalisation:* $\delta P/P_0=-U$, with the same U that sets $\ln N$. This is the presence clock's $N=P/P_0$ at linear order; a different normalisation would scale k₂ directly, and the bound allows 10⁻⁹.
  - *The steady inflow is dropped.* The registration defines u as the full drift J/P, which also includes the steady inflow into the sinks, $\mathbf J_s=DP_0\nabla U$. The derivation drops it. It is a static gradient, so it has no curl and is not of PPN form. It could be removed by relabelling time, but not freely if lattice time is physical. Its size is $D\,U/r$ in lattice units: about 7×10⁻⁶ U/r, which at a metre (6×10³⁴ places, if a place is a Planck length) is about 10⁻⁴⁰ U, and smaller further out. Negligible at the adopted scales, but a term the derivation sets aside, not one it removes.
- **The principle itself is not yet a CO rule.** EtaCrossCheck matched the acoustic form from outside, and the acoustic arc sets the flow to zero. Adopting C1 is a choice of principle, not of a number.

**Why that is not enough.** The same gradient structure means the engine's possibility flow can never circulate, in any time labelling. A stationary rotating body makes no flow at all ($\partial_tU=0$). So C1 has k₁ = 0: α₁ = −8 and no frame dragging. The missing piece is the transverse $-4V_i$: moving matter's momentum must source a circulating current. In GR the 4 is $2(1+\gamma)$, which is what boosting a static field gives.

**Outcome.**
- **K34: no derived candidate passes.** The kill rule as registered accepted candidates that are put in, and C3 is GR by construction, so it could not fire. That was a flaw in the registration. Read honestly: parts 1–3 pass the preferred-frame bounds **only by input**, through C2. That needs:
  - part 1 (possibility relaxes between ticks)
  - C1 (patterns ride possibility's flow), which makes α₂ = 0 derived, given its premises
  - a momentum channel with $k_1=-4$ to 2×10⁻⁵ (λ_J = 4), which is input
  - the motion weight $a_1=2$ to 2×10⁻²⁰ (Run 33's R-b), which is input
- **Part 1 with no current field fails the preferred-frame tests** (α₁ = −8, α₂ = −1). The engine as built, with its diffusive wake, is not of PPN form, so its α's are not defined. What holds for it regardless is that it has no frame dragging: any $g_{0i}$ it could carry is a gradient. That is §4 item 5, now with numbers.
- **Hypothesis: the momentum channel and R-b are one piece of physics.** Moving matter's momentum must act in two places: on the clock field's source ($\tfrac32v^2$, the Earth–Moon test) and on the current field (the 4, α₁ and frame dragging). In GR both come from the boost. Nothing in CO links them yet. CO's D30 ruling, "influence carries motion and energy", is a possible hook for both.
- **What would make the 4 derived.** A rule in CO that fixes how strongly a moving commitment imparts momentum to possibility, with no number chosen to match, landing within 2×10⁻⁵ of 4. PinningLambdaJ's naive estimate (λ_J of order 1) shows the rule is not yet there.
- **GR-II's falsifier** ("an additional vector mode") is not triggered by C2 if the current field is set each tick like part 1, a constraint rather than a travelling mode.

**The rulings (19 October, after this run) and the input chosen.**


- **Adopted:** part 1 (the clock field is fixed each tick) and C1 (patterns ride possibility's flow).
- **The tick is not physical time** (ruled 19 October). Physical time is what clocks read, which is commitments; the tick only orders updates. Consequences:
  - Relabelling the tick, $t\to t+\lambda\chi_{,0}$, is a choice of coordinates, not a change of physics.
  - C3 no longer conflicts with part 1. Its boosted field, relabelled by $t\to t-\tfrac12\chi_{,0}$, is part 1's field with $k_2=\tfrac12$, $k_1=-4$ and $a_1=2$. So C2 (with R-b) and C3 become one candidate.
  - The steady inflow that C1's derivation dropped is a static gradient, which a relabelling removes. It is pure coordinates.
- **The input chosen**. One input, not two numbers: **Lorentz invariance at first post-Newtonian order. A moving body's field is its boosted rest field, up to relabelling the tick.**
  - It fixes $k_1=-4$ (λ_J = 4) and $a_1=2$ together and exactly, so the tolerances are met by construction.
  - It is the input already tracked for Run 18 (twist charged on loops that include a tick), so the ledger gains no new kind of input.
  - It makes correction 8's hypothesis true by input: the momentum channel and the motion weight come from one source, as in GR.
  - **A check the derived piece passes.** In the slicing where part 1 holds (no $\mathcal A$ term), the boost requires $k_2=\tfrac12$. C1 derives $k_2=\tfrac12$ from conservation. Had conservation given any other value, this input would contradict CO's own flow. It does not.
  - **What future learning should look for:** one CO rule that makes physics independent of the lattice's rest frame. It would replace this input and Run 18's together.
- **The first post-Newtonian parameters under the adopted rules** (Candidate A″ = A′ + part 1 + C1 + this input):

| parameter | value | how |
|---|---|---|
| γ | 1 | the pattern rule $c=N^2$ (input; Runs 9, 17) |
| β | $1-$ about $2\times10^{-5}$ at $P_0/p_s=2.3\times10^4$ | the medium (Candidate A′; Runs 22–25, 30) |
| ξ | 0 | part 1: no $\Phi_W$ term (derived) |
| ζ₁ | 0 | part 1: no $\mathcal A$ term (derived) |
| ζ₂ | 2(β − 1) | Tolman sourcing (derived; Run 30) |
| α₂ | 0 | C1: possibility's conservation flow (derived, given C1) |
| α₁, α₃ | 0 | the Lorentz input |
| ζ₃, ζ₄ (internal energy, pressure) | open | whether pattern energy and stress draw (Run 33). The input covers kinetic pressure (moving particles) only |

*Note (29 October, after Reading I15's check): ζ₂ = 2(β − 1) is the value under the draw rule used before R5 (d = TN). Under the ruled variational draw d = T(1 + g) = −ρ* dN/dφ the static sector is Lagrangian, the Φ₂ coefficient is 2(4 − 2β), and ζ₂ = 0 exactly for every ε (an invariant action requires it; Will 2014 §3.2). Run 66's Δ = εC/(1+ε), the current scale input, already corresponds to this; the ζ₂-based scale bounds below are superseded.*


- **The Earth–Moon test is then met in full.** With these values,
$$
\eta_N=4\beta-\gamma-3-\tfrac{10}{3}\xi-\alpha_1+\tfrac23\alpha_2-\tfrac23\zeta_1-\tfrac13\zeta_2=\tfrac{10}{3}(\beta-1)\approx-6.5\times10^{-5}
$$
  at $P_0/p_s=2.3\times10^4$, against lunar laser ranging's σ = 4.4×10⁻⁴.
- **No scalar radiation.** A clock field fixed each tick is a constraint, so it carries no waves. Gravitational radiation is then only part 3's shear of relations (Run 11b, 0.98 of GR), with no scalar dipole radiation, which binary pulsars require.
- **Open: signalling through the constraint.** The field updates everywhere at once on each slice. It cannot carry a signal only if every change in the draws is one that conservation allows (as in GR, whose instantaneous potential in this gauge carries none). With the inputs that holds at first post-Newtonian order; it is untested beyond.

**Corrections from the independent check** (the registration is unchanged; these change only how the result is stated):
1. The α₁ bound of 4×10⁻⁵ is from the pulsar PSR J1738+0333, not lunar laser ranging (10⁻⁴). The registration mislabelled it.
2. Frame dragging is $1+\alpha_1/8$ of GR's, so it is the α₁ test, weaker by 10⁴; it is not a separate exclusion.
3. K34 could not fire as registered; restated as "no derived candidate passes".
4. C3's k₂ = ½ and $a_1=2$ need a time relabelling that conflicts with part 1 if lattice time is physical.
5. α₁ = −8, α₂ = −1 hold for part 1 with $g_{0i}=0$, not for the diffusive engine "independently of the wake". Only "no frame dragging" holds regardless.
6. The grid checks are consistency checks; the far-field W was not checked.
7. C1's premises (normalisation; the dropped steady inflow) and the tolerances on k₁, k₂ and $a_1$ are now stated.
8. "The momentum channel is the same physics as R-b" is a hypothesis.
