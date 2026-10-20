## 9w. Run 30: the sourcing weight the static engine can reach (rest mass in a potential), against GR's Tolman mass

*18 October 2026. Allen: "do the recommended steps".*
- *This is a derivation, not a new engine run, and it was not pre-registered because no new data were taken.*
- *Its engine check is Run 26's W3, measured before this derivation existed.*
- *An independent agent checked the algebra against Will (2014) and Tolman, and its corrections are included.*

**Question.** In GR every form of energy pulls, each with a fixed weight. The Earth–Moon test (lunar laser ranging) measures a combination of those weights:
$$
\eta_N=4\beta-\gamma-3-\tfrac{10}{3}\xi-\alpha_1+\tfrac23\alpha_2-\tfrac23\zeta_1-\tfrac13\zeta_2 .
$$
Run 25 tested only the β part. The engine's matter is reserved pairs held at fixed places. Which weights can it reach, and what does it give?

**Prior record (checked first).**
- **ED_Attempt_01** (`Nordtvedt_Check.md`, C206–C208). A linear budget gives η_N = 10/3 (rest mass only) or 17/6. "A linear budget cannot pass post-Newtonian tests, whatever it counts."
- **ED_Attempt_03** (`Self_Feedback_Question.md`, F2, C42). An active density $\rho e^{-U}(1-v^2/2)$, a source slowed by its own ticks, gives ζ₁ = −5, ζ₂ = −3, η_N = 13/3, "further from GR."
- **ED_Attempt_04.**
  - R1: GR's bar is (2, 2, 1, 3) for (motion, potential, internal energy, pressure). C6 notes that per-direction counting "restates the Tolman–Whittaker active mass".
  - R4 part 2, K1: with β = γ = 1, no preferred frame, and action = reaction, the weights are forced to 2, 2, 1, 3 and η = 0. That was recorded as "consistent, not derived".
- No file includes the redshift factor in Tolman's integrand.

**The engine's active mass (from the adopted rules).**
- **The draw tracks the clock rate.**
  - A reserved pair renews each time the possibility present at its two places, summed over ticks, reaches H. This is the presence clock, adopted on 18 October for clock universality.
  - Each renewal takes 2 units. So a pair's draw is $D=2\langle P_a+P_b\rangle/H=(4P_0/H)\,N$, where N is the clock rate at the pair's own places.
  - **Draw ∝ local clock rate** is therefore an identity.
- **The far field counts the sum of draws.** The deficit is linear in the draws (the exact outflow equation), and in the β = 1 regime ln N is linear in the deficit. So the field far away counts
$$
M_{\rm act}\;\propto\;\sum_{\rm pairs}N_{\rm local}.
$$

**GR's active mass for static matter.**
- For a static, asymptotically flat solution, Tolman's active mass is $M=\int(\rho_E+3p)\sqrt{-g}\,d^3x$, in signature (−+++) with G = c = 1 (Tolman 1934, §92).
- In any static metric $-N^2dt^2+h_{ij}dx^idx^j$:
  - $\sqrt{-g}=N\sqrt h$
  - the conserved rest-mass density is $\rho^*=\rho\,u^0\sqrt{-g}=\rho\sqrt h$
  - so:
$$
\rho\sqrt{-g}\;=\;\rho^*N ,\qquad \int\rho\sqrt{-g}\,d^3x=\sum_{\rm rest\ mass}N_{\rm local}.
$$
- The rest-mass part of Tolman's integrand is each bit of rest mass weighted by its local clock rate. No choice of coordinates is involved, because $\rho^*d^3x=\rho\,dV_{\rm proper}$ counts the matter itself.

**The match.**
- The engine's pairs are a count of matter, so $\sum_{\rm pairs}N_{\rm local}$ is the rest-mass term of Tolman's integrand.
- **The match is in the form of the integrand, at any depth.** Two caveats:
  - Each pair's own lattice dip makes its draw slightly less than proportional to the external clock rate. The draw goes as $N_{\rm ext}^{1/(1+\kappa D_0)}$, which shifts ζ₂ by about $+0.3/p_s$, at most 8×10⁻⁷ at $p_s\gtrsim4\times10^5$.
  - Tolman's integral equals a body's total mass only for solutions of Einstein's equations, and the exponential metric differs from Schwarzschild beyond first post-Newtonian order.

**In PPN terms.**
- Reading the engine's metric in PPN form needs isotropic coordinates. For the engine these are inferred from the clock rate N and the pattern rule's light speed $N^2$ (γ = 1), not from rods.
- With $g_{ij}=(1+2\gamma U)\delta_{ij}$, the engine's source is $\rho^*N=\rho\,[1+(3\gamma-1)U]$. So $U_{\rm eff}=U+(3\gamma-1)\Phi_2$ and $g_{00}=-1+2U+2(3\gamma-1)\Phi_2-2\beta U^2$.
- Will's static $g_{00}$ has Φ₂ coefficient $2(3\gamma-2\beta+1+\zeta_2+\xi)$, plus a $-2\xi\Phi_W$ term. The engine has no Φ_W term, so ξ = 0, and
$$
\zeta_2=2(\beta-1).
$$
- With the medium's $\beta-1\approx-0.45\,p_s/P_0$, this gives $\zeta_2\approx-0.9\,p_s/P_0$.
- The premise matters. β here comes from the clock reading P = R(z) pointwise, with z exactly linear in the draws. Had β instead come from a $(\nabla\psi)^2$ term in the field equation, the result would be $\zeta_2=4(\beta-1)$.
- `sourcing30.py` expands $\rho^*N/\rho$ numerically. That checks the series, not the mapping.

**Why Attempt 03's F2 failed and this does not.**
- F2 read the active density with ρ as the *proper* density. That gives a source $\rho(1-U)$ and ζ₂ = −3.
- The engine's draw is a count of matter, the conserved density. The same rule then gives $\rho(1+2U)$ (at γ = 1) and ζ₂ = 2(β − 1), which is zero at β = 1.
- The conversion $\rho^*=\rho(1+3\gamma U)$ is the whole difference. Read as proper, the same arithmetic reproduces F2's numbers exactly (ζ₁ = −5, ζ₂ = −3, η = 13/3).

**Engine check (already measured; Run 26 W3).** Two bodies each redshift the other's draw.

| | seed 1, A | seed 1, B | seed 2, A | seed 2, B |
|---|---|---|---|---|
| draw ratio in the pair, measured | 0.976 | 0.986 | 0.980 | 0.983 |
| predicted from "draw ∝ total local clock rate", solved self-consistently from the solo runs | 0.975 | 0.987 | 0.972 | 0.985 |

- The gaps are 0.1–0.8%, on shifts of 1.4–2.8%.
- **One cell misses: seed 2, body A,** which shifts 2.0% against a predicted 2.8%, a 29% miss of the shift.
- **The self-consistency matters at the engine's scale.** The measured response to the other body's well is about half: 0.976 against N_other = 0.953.
- That needs the body's whole self-well, about 1 in ln N at its pairs. A lone pair's 0.19 self-dip alone would give about 0.83.
- At the adopted $p_s$ the pair-scale part is negligible. A real body's self-well is its own gravitational potential, which Tolman's formula also includes.

**What the static engine cannot reach.**
- **Motion.**
  - GR's source for moving matter, in conserved terms, is $\rho^*(1+\tfrac32v^2-U)$.
  - If a moving body's draw followed only its own time-dilated ticking, it would be $\rho^*(1-\tfrac12v^2)(1-U)$. In proper-density terms that is a Φ₁ coefficient of 0 against GR's 4, which means $\zeta_1+\alpha_3=-4$.
  - Read as ζ₁, the Earth–Moon term is $-\tfrac23\zeta_1=+\tfrac83$, about 6,000× the 1σ bound (3,000× the 2σ). Read as α₃, it is excluded by pulsar bounds at 4×10⁻²⁰.
  - Either way, **ED's moving matter must draw more than its ticking alone gives, by a factor 1 + 2v².** The engine has no rule for moving matter yet.
- **Pressure and stress (the weight 3).**
  - The engine's bodies are held by rule, not supported by stress. Their total active mass, $\int\rho^*N$, is $M^*+2\Omega$, with $\Omega=-\tfrac12\int\rho U<0$.
  - A self-supported GR body gets $M^*+E_{\rm int}+\Omega$, because its stress pulls with weight 3 and, by the virial theorem, gives back $3\!\int\!p=-\Omega$. For a monatomic gas that is $M^*+\Omega/2$.
  - GR has no static stress-free body, so the two are not like for like.
  - Whether ED's stresses pull is open. The knots of Runs 12 and 18 satisfy $M=E$ (their stresses integrate to zero) in a field equation, not on the event layer.
- **The preferred-frame terms α₁ and α₂.** These need moving bodies or a moving frame. ξ, the preferred-location parameter, is static and zero in the engine.
- **The η_N formula itself assumes PPN fluid bodies.** Applying it to bodies held by rule assumes a stress and motion sector the engine does not yet have.

**Outcome.**
- **One weight settled: rest mass in a potential pulls with GR's weight.** It holds exactly at β = 1, and with $\zeta_2=2(\beta-1)$ otherwise (up to the $+0.3/p_s$ pair residual).
- **A tighter bound on an input.**
  - The binary-pulsar bound $|\zeta_2|<4\times10^{-5}$ (Will 2014, Table 4, PSR 1913+16) needs $P_0/p_s\gtrsim2.3\times10^4$. That is about 11× above the 2000 that Nordtvedt's β part needed.
  - With $p_s\gtrsim4\times10^5$, it means $P_0\gtrsim9\times10^9$ units per place.
- **The Earth–Moon test now reads**
$$
\eta_N=\tfrac{10}{3}(\beta-1)-\tfrac23\zeta_1-\alpha_1+\tfrac23\alpha_2 ,
$$
  with ζ₁, α₁ and α₂ open. At $P_0/p_s=2.3\times10^4$ the first term is −6.5×10⁻⁵.
- **Allen's exit rule (Attempt 04, R1)** records a weight that "hits … only because it restates Tolman's formula" as "consistent, not derived".
  - The rule behind this result, the presence clock, was fixed on 18 October for clock reasons, before this weight was computed.
  - Its match to Tolman's rest-mass term follows from that rule, not the other way round.
  - Allen decides the label.
- **Next, if pursued:** a rule for moving matter, checked against the 1 + 2v² requirement before it is adopted. That is Attempt 04's "action = reaction" in engine form.
