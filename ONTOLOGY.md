# The commitment ontology, as it stands

Allen Proxmire · 21 October 2026 · after Runs 1–74 of the lattice record

This page states, in one place, what the lattice record tests: the commitment ontology's rules as they stand today. For each rule it gives:
- its formula;
- when it was adopted, and by whom;
- the runs behind it.

Some terms used throughout:
- **Rulings** are Allen's choices. Several were made on Claude's recommendation, and the page says so where they were.
- **Provisional** rulings are marked, with the grounds for going back where these were set in advance.
- **Borrowed:** an input taken from established physics, tracked rather than derived.

The full record (`writeups/commitment_ontology_simulations.md`) holds the evidence for every statement here, and the history of what was tried and dropped. The engine is a model built from these rules, not the whole of Event Density (ED).

---

## 1. The picture in one paragraph

- **Commitments.** The world is made of commitments: irreversible updates that happen at **places** and are never undone. Time at a place is the count of commitments there, so at the bottom time runs one way.
- **Possibility.** Between commitments, places hold possibility, a conserved stuff that hops between related places. It never commits by itself: the vacuum carries no commitment.
- **Matter** is commitment that keeps re-making itself. Each renewal draws on the possibility around it, so matter thins the possibility near it.
- **Clocks are matter.** A clock ticks in proportion to the possibility present where it sits, so clocks near matter run slow. That clock-rate gradient is gravity.
- **Light and quantum matter** are patterns of possibility in transit. They hop on their place's ticks, so they bend and fall in the same field.
- **Where possibility runs low, infalling matter commits for good.** Under the current ruling this happens at about twice the medium's crossover scale. That is the core of a black hole, where what falls in becomes record.

---

## 2. Primitives

| Primitive | What it is |
|---|---|
| **Commitment (event)** | One irreversible update. Time at a place is the count of commitments there. A commitment is never undone. |
| **Place, relation** | Space is who relates to whom. Sliding places costs nothing. In the engine, places form a 3D lattice with nearest-neighbour relations. |
| **Possibility** | A conserved quantity held at places, P units per place. It hops between related places. **The vacuum carries no commitment** (ruled 15 October, after Run 14). |
| **Matter** | Commitment that keeps re-making itself. In the engine it is a reserved pair of places that takes one unit from each, holds, and renews. Mass is the upkeep. |
| **Clock** | Matter that counts its own commitments (**clocks are matter**, ruled 15 October). What a clock reads was ruled on 18 October (R2). |
| **Pattern** | A pattern of possibility in transit: light, and quantum matter. |
| **Record** | What has been committed: the history. It is kept, never undone. |

---

## 3. The rules

### R1. The medium (ruled 18 October, provisional; Runs 21–26)
A place holding P units sends out, on average,
$$
f(P)=c\,\ln\!\Big(1+\frac{P}{p_s}\Big)\quad\text{units per tick},\qquad c=\frac{0.99}{\ln(1+1/p_s)} .
$$
- The outflow is linear in P below a crossover scale p_s, and compares ratios above it.
- Far from matter the medium holds P∞ units per place. Older runs call this P₀.
- **Why it is provisional:**
  - it was designed to give β = 1;
  - p_s was brought in after the first version's clocks failed (Run 22);
  - both scales are set by observational bounds, not by ED.
- What it achieves is surviving the independent checks that followed (Runs 23–26).

### R2. The presence clock (ruled 18 October, provisional; Runs 22–24)
A commitment holds until the possibility present at its two places, summed over ticks, reaches a fixed amount:
$$
\sum_{\rm ticks}\big(P_a+P_b\big)\;\ge\;H=2\,\hbar_t\,P_\infty ,
$$
where ħ_t is the hold's length in ticks far from matter. So a clock's rate is proportional to the possibility around it:
$$
N=\frac{P}{P_\infty}.
$$
- This replaced the 16 October **flow clock**, which counted possibility *passing*.
- **Clocks of different design agree only if p_s is large.**
  - A clock depletes its own places. Their disagreement falls as p_s^(−0.85) (Run 24).
  - Agreement to 10⁻⁶ needs p_s ≳ 4×10⁵, extrapolated.
- **On lattices with imposed curvature,** clocks follow the zero-range theory: Run 70 at p_s = 4, Run 72 at p_s = 1.
  - Universality, and the p_s^(−0.85) convergence, on a space curved by the medium's own stress are untested.

### R3. The field (derived; Runs 14, 21–22)
Conservation makes the mean outflow z = ⟨f(P)⟩ an exactly linear, unscreened field of matter's draw s. On the lattice, with six neighbours:
$$
\tfrac16\sum_{y\sim x}z_y\;-\;z_x\;=\;s_x-\bar s .
$$
The clock reads P = R(z), the medium's equation of state, not z itself. The second-order coefficient is then
$$
\beta=1+\frac{y''}{2y'^2},\qquad y(z)=\ln R(z),
$$
- β → 1 once P∞/p_s ≳ 256 (Runs 22–23).
- Two bodies' wells multiply (f = 1.12 ± 0.19, Run 26).

### R4. The field's dynamics (ruled 19 October; Runs 31, 34, 35)
- **The clock field is fixed each tick:** the medium's stationary law, drawn afresh. So a moving body keeps its well, with no diffusion lag.
- **Patterns ride possibility's flow.**
- **The engine's tick is not physical time.**

### R5. What draws (rulings 19–20 October; Runs 30, 33, 36, 40–42, 49–55)
Every source draws by its redshifted Tolman/Komar weight, times a factor that makes the theory variational in a medium with a scale:
$$
d=T\,(1+g),\qquad T=(e+3p)\,N\sqrt\gamma,\qquad g=c\,\frac{d\ln R}{dz}-1\;\approx\;\frac{p_s}{P}.
$$
- **Rest mass deep in a well pulls by its local clock rate.** This is GR's Tolman term, and it is derived (Run 30).
- **A pattern's energy draws** (ruled 19 October; Runs 33, 36).
- **Stress pulls, with weight 1 per direction.** Every part of a source draws by α(T⁰⁰ + ΣT^ii). This is the Lorentz input in its full form (ruled 19 October; Runs 42, 44).
- **A body is matter in exact hydrostatic balance** (rule correction, 20 October, after Runs 49–50):
$$
N\,h(n)=\tilde\mu,\qquad h=1+\epsilon_{\rm int}+p/n ,
$$
  where ε_int is the internal energy per unit rest mass.
- **The variational draw d = T(1 + g)** (ruled 20 October, after Runs 52–54). Field, matter and patterns are then the Euler–Lagrange equations of one action, so the first law and passive = active mass hold exactly.

### R6. The pattern rule (ruled 17 October, provisional; full form 20 October; Runs 9, 17, 45–46)
A pattern hops on its place's ticks and needs free capacity there. So light's coordinate speed is N², which gives γ = 1.
- **It is provisional** because γ = 1 is put in by the rule's two factors rather than derived.
- **Massive patterns** obey the wave equation in the metric this gives light, with the Tolman/Komar draw:
$$
-N^4\nabla^2\psi+m^2N^2\psi=\omega^2\psi,\qquad d=\kappa\big(4\omega^2N^{-4}-2m^2N^{-2}\big)\psi^2 .
$$

### R7. Twist and particles (ruled 17 October, provisional; Runs 12–13, 18, 18b)
**Twist is charged on every closed loop of the history,** including loops made of one relation and one tick, with ticks and relations priced alike.
- Equal pricing is what makes a knot's inertia equal its energy, and MICROSCOPE requires it.
- It is **Lorentz invariance put in by hand:** borrowed, not derived.
- **Particles as knots of commitment** hold when twist lives on closed loops of relations that tile space as faces (Runs 12–13).

### R8. Motion and inertia (rulings 19–20 October; Runs 16, 34, 52, 55, 63)
- **Patterns ride possibility's flow:**
$$
g_{0i}=-u_i .
$$
- **The Lorentz input** (borrowed, 19 October): a moving body's field is its boosted rest field. It gives α₁ = α₃ = 0 and GR's frame dragging (Run 34).
- **Bodies move as point particles,** with action −m∫dτ in the total metric minus their own field (ruled 20 October, after Run 63).
- **Inertia = total energy** (ruled 20 October, borrowed): a compact body's energy and momentum form a four-vector, m_inertial = E_H.
- **Relations shear,** and only the shear radiates: two polarisations at c, with no breathing or dipole mode. Matter sets capacity and isotropic stretch at each moment (Run 11b).

### R9. Space and the metric
The static metric is written on the space the medium lives on, γ̃_ij = N²g_ij:
$$
ds^2=-N^2dt^2+N^{-2}\,\tilde\gamma_{ij}\,dx^i dx^j .
$$
- **ED's original rule** (option 1, with R6) kept γ̃ flat.
  - With ED's field equation this gives the exponential metric e^(∓2U): γ = β = 1 at first post-Newtonian order, and no horizons.
- **Option 3** (Allen, 21 October, provisional): binding tension curves the medium's space, in GR's form.
  - At ε = 0 (no medium scale), GR's static equations are exactly:
$$
\tilde\Delta U=-4\pi\,(e+3p)\,e^{2U},\qquad
\tilde R_{ij}=2\,\partial_iU\,\partial_jU-16\pi\,p\,e^{2U}\,\tilde\gamma_{ij},\qquad hN=\text{const}.
$$
    The first is ED's own field equation, written on γ̃ (Run 65).
- **With ED's medium** (Run 66), the transported field is φ = z∞ − z. It is linear on the lattice, and the clock is
$$
N=\frac{P}{P_\infty}=(1+\varepsilon)\,e^{-\varphi}-\varepsilon,\qquad \varepsilon=\frac{p_s}{P_\infty},\qquad \frac{dU}{d\varphi}=1+g,\quad g=\frac{\varepsilon}{N}.
$$
  - φ's stress curves γ̃:
$$
\tilde R_{ij}=2\,\partial_i\varphi\,\partial_j\varphi-16\pi\,p\,e^{2U}\,\tilde\gamma_{ij}.
$$
    That is a recorded choice. With U's stress instead, β = 1 exactly; with φ's, β − 1 = −ε/[2(1+ε)].
  - **Under option 3 and that choice, ε sets every static departure from GR.** ED's static stars and holes are GR's to O(ε) (Runs 65–67).
  - The clock stops where GR's lapse would be about ε, with no event horizon (Run 67).
- **Going back to option 1** (grounds set in advance): if option 3 cannot be written to all orders as one consistent theory, or if it loses a result or fails data that option 1 passes.

### R10. The current field and rotation (rulings 21 October, provisional; Runs 34, 69)
- **Option 3 covers the current field.** g₀ᵢ and its back-reaction take GR's nonlinear form.
  - This was adopted on Claude's recommendation; Allen confirmed it at 09:04.
- **The input current field is a flow of possibility** (Allen, 12:50, on Claude's recommendation). Around a spinning body, possibility circulates and carries patterns along, so the medium's frame is the zero-angular-momentum frame.
  - Its clock is that frame's lapse α ("reading Z", adopted provisionally after Run 69).
  - Then spinning holes are Kerr outside the horizon to O(ε/α).
- **Cost:** reading Z interprets an input; ED's rules do not imply it.
  - The engine's possibility flow is a gradient, and cannot circulate.
  - When rotation is built in, the flow needs a part that moving matter drags around (a curl part).
- **Going back:** if ED's dynamics cannot carry a circulating flow, or if reading Z fails a test that the alternative (reading K, places held fixed) passes.

### R11. Black holes: option A and the core (rulings 19–21 October; Runs 28, 43, 67, 68, 71, 73, 74)
- **Option A** (borrowed; 19 October, extended 20 October): outside black holes the field is GR's, with ED's core inside.
  - Option A now carries binary-black-hole inspirals and mergers.
  - Under option 3, static holes (Runs 65–67) and spinning exteriors (Run 69) follow from ED's own equations instead.
- **The core commits what reaches it** (19 October). It is a total absorber, so there are no echoes, and what falls in becomes record (Run 43).
- **Where:** infalling matter commits where the medium's possibility per place falls to k·p_s, with k = 2 (Allen, 21 October, 14:00, on Claude's recommendation). Since N = P/P∞, that is where the clock has fallen to 2ε.
  - **It catches all causal matter.** In a thin-shell model at physical ε, the stiffest causal matter turns back at most at 1.27p_s (Run 73). Ordinary dense matter (w ≲ 0.6) turns back below about 0.75p_s.
  - **Any k above about 1.34 would work.** k = 2 is twice the medium's crossover.
  - **The core's areal radius is 2m(k + 1)/k,** which is 3m at k = 2 (Run 74, computed post hoc with the corrected conversion).
- **ED's holes are stable** (Allen, 21 October: "it follows from the rules with nothing added"). This replaced his 19 October ruling that black holes evaporate (Runs 68, 71, 74; §5).
- **Going back:**
  - if the exterior's own dynamics, once written, give a conflicting bounce or commitment rule;
  - if matter is found that turns back above 2p_s;
  - if the discrete regime below one unit per place re-emits;
  - if an evaporating primordial black hole is seen.

### Withdrawn or superseded

| Rule | Status |
|---|---|
| The vacuum commits (ED's original event layer) | dropped 15 October (Run 14); ED's event-layer results 20–22 and 27 were obtained with it and have not been re-tested |
| The flow clock (16 October): a hold lasts while a fixed amount of possibility *passes* | replaced by the presence clock, 18 October |
| Slowing possibility's own hops by the local clock | not adopted: the medium froze (Run 17) |
| Bodies keep their proper size (19 October, Claude's choice at Allen's instruction) | superseded for static bodies by hydrostatic balance, 20 October |
| Defaults (c2), (c3) for binding tension | suspended, then replaced by option 3 (21 October) |
| Black holes evaporate (19 October), with two tracked assumptions | withdrawn 21 October: ED's holes are stable |

---

## 4. What is derived, what is ruled, what is borrowed

| Observed | How the ontology gets it | Runs |
|---|---|---|
| Newton: 1/r², linear in the source, no screening | **derived:** matter's draw on a medium that never commits | 1, 14 |
| Gravitational redshift | **derived:** the presence clock | 22 (15 under the flow clock) |
| Patterns fall at the clock-set rate, all masses alike | **derived:** a pattern turned by the committed world's count, with no coupling | 16, 27 |
| Wells obey the medium's equation of state | **derived:** local equilibrium | 22, 25 |
| Rest mass in a well pulls by its clock rate (Tolman) | **derived:** a body's pull is its ticking | 30 |
| No preferred-frame effect from the flow (α₂ = ζ₁ = ξ = 0) | **derived** from conservation, given R4 and R8 | 34 |
| Time runs one way; time-averaging shrinks the order | **derived:** commitments are never undone. Order in a clock's record falls about as 1/T, 26× down but not zero | 29, 35, 37 |
| Light bending, Shapiro delay (γ = 1) | **ruled:** the pattern rule (R6) | 9, 17, 46 |
| Mercury; β = 1; wells multiply | **ruled:** the medium and clock (R1–R2), designed for β = 1 | 22–26 |
| Clocks of different design agree; ζ₂; the pulsar triple | **scales chosen within data bounds:** p_s ≳ 4×10⁵, P∞/p_s ≳ 1.6–1.9×10⁵ | 23, 24, 30, 45, 48, 55, 57, 66 |
| Bound and composite matter fall alike (MICROSCOPE) | **borrowed:** twist on loops that include a tick (R7), plus the full pattern rule | 18, 18b, 46–48, 52, 54 |
| α₁, α₃, frame dragging, the Earth–Moon test | **borrowed:** the Lorentz input | 34 |
| At weak field a bound system pulls by its total energy | **ruled** (pattern energy draws) **and borrowed** (momentum flux draws) | 36, 40c |
| Internal binding pulls like rest mass (ζ₄) | **borrowed:** the Lorentz input in full form (stress pulls) | 42, 44, 49, 50 |
| A compact body's inertia is its total energy | **borrowed** | 52, 55 |
| Binary-pulsar energy loss | **ruled:** relations shear (a reading fixed in advance) | 11b |
| Static black holes and neutron stars as GR's; ringdowns, shadows | **ruled:** option 3, plus reading Z for spin; before that, option A | 28, 39, 41, 65–67, 69 |
| Binary-black-hole inspirals and mergers | **borrowed:** option A | 63 (the ruling) |
| Holes absorb, leave no echoes, are stable | **ruled:** the core commits, at 2p_s | 43, 67, 68, 71, 73, 74 |

**The two scales are bounds from data, not predictions:**
- p_s ≳ 4×10⁵ units per place, so that clocks agree to 10⁻⁶;
- P∞/p_s ≳ 1.6–1.9×10⁵, from the pulsar triple PSR J0337+1715 (2.5–2.9×10⁵ with the planet model; Run 66).

Nothing in ED's papers fixes either.

---

## 5. Where ED speaks and GR is silent (not yet tested as predictions)

1. **Time's direction is fundamental, not a boundary condition.**
   - The engine's bottom is one-way.
   - A clock's time-averaged record loses most of the order, falling as 1/T. What leaks goes as 1/T times a coefficient that is unknown at physical scales.
   - So this is an instance of Allen's coarse-graining claim, not yet a test of nature (Run 29).
2. **The quantum vacuum's energy does not draw,** because the vacuum never commits.
   - That is in line with how small the cosmological constant is. Its coefficient is not computed.
   - The classical vacuum drawing nothing is not distinctive: GR without Λ has it too.
   - With rotation, the clock equation gains a vacuum source (Run 69).
3. **Compact bodies slightly break the strong equivalence principle.** A neutron star's gravitational mass exceeds its inertia:
$$
\Delta=\frac{\varepsilon\,C}{1+\varepsilon},\qquad \varepsilon=\frac{p_s}{P_\infty},\qquad C\approx0.37\text{–}0.44\ \text{(pulsar of PSR J0337+1715)} .
$$
   - GR gives zero.
   - The sign is fixed (Δ > 0), the effect grows with compactness, and it is not additive. Its size waits on ε.
   - This depends on inertia = total energy (borrowed) and on Run 66's choice that φ curves γ̃ (Runs 52, 55, 57, 65, 66).
4. **No point of infinite density is reached.**
   - The mean-field geometry is singular at P = 0 (Run 67).
   - Under the ruling, matter commits first, at P = 2p_s and areal radius 3m (Runs 73–74).
   - The hole has no event horizon, and it is cold (κ = 0).
5. **Black holes do not evaporate.**
   - **A collapse emits GR's Hawking flux only as a transient,** for about 8M ln(P∞/p_s). That is about one quantum in the 1+1 model, about 10⁻² in 4D (Run 68).
   - **When the matter commits,** a cold core gives one flash of about ħ/δu and then silence; a continued state gives a faint negative tail instead (Run 74). δu, how long commitment takes as seen from far away, is not fixed by ED's rules.
   - **So primordial black holes never evaporate,** and the bounds on them that assume evaporation do not apply. A detected evaporating primordial black hole would count against ED.
   - **Black-hole thermodynamics** (S = A/4, T = κ/2π) does not carry over without a new argument.
6. **Under ED's original rule for space only** (withdrawn under option 3), heavy neutron stars need matter near the causal limit above about twice nuclear density. Heavy-ion collisions allow this only at the edge of their bounds (Runs 57–62).

---

## 6. How the record tests it

**Each run states a consequence of these rules and a measurement to compare it with.**
- Most of Runs 1–13 were exploratory and not pre-registered.
- From Run 14 most runs were pre-registered with kill rules and the analysis.
- From about Run 22 the registrations were hashed with the code before running.
- From about Run 29 most runs were re-checked by an independent agent.
- The scorecard and Appendix A of the record say which runs were registered, hashed and checked. Verdicts are reported as registered, and post hoc work is labelled.

| Runs | What they test |
|---|---|
| 1–13 | Newton's field; clocks keeping time together; radiation; light bending; Mercury; particles as knots |
| 14–20 | the vacuum that never commits; the clock rule; free fall of patterns and knots; light's hop rule; the engine's β = ½ problem |
| 21–30 | the medium and clock that give β = 1; clock universality; the strong field (shadow, ringdown); the arrow of time; sourcing |
| 31–38 | the field's dynamics; horizons; whether a pattern's energy pulls; preferred-frame tests and frame dragging; the engine on the adopted rules |
| 39–44 | the strong field with spin; binding inside bodies; the core |
| 45–64 | bound matter at neutron-star strength; the first law; the strong equivalence principle; neutron-star masses, radii and nuclear matter; binaries beyond first order |
| 65–69 | GR's clock equation in ED; option 3; static and spinning black holes; evaporation |
| 70–74 | clocks on curved lattices; collapse through a hole's throat; where infalling matter commits, and what that radiates |

---

## 7. Open

**The medium and its scales**
- What fixes p_s and P∞.
- ED's hop: the engine needs it to be about 10^2.5–10^3 Planck lengths. That is an open tension with the corpus's P08 (ℓ_ED = ℓ_P), decided 20 October.
- Whether φ's or U's stress curves the medium's space (it sets β − 1).

**The medium on a stress-curved space**
- The medium's dynamics there: the dynamical completion with ε ≠ 0.
- A lattice whose curvature comes from the medium's own stress, and clock universality on it.
- The seeds for Run 72's design-gap contrast (Run 72b, running).

**Rotation**
- The rotating near-horizon shell, and option 3's stationary equations with the medium.
- A curl part of the engine's flow, so it can carry frame dragging.

**Black holes**
- A collapse whose surroundings have their own dynamics.
- What commitment does in detail: how long it takes, and the core's quantum state.
- Black-hole thermodynamics without evaporation.

**The strong field and binding**
- The strong-field binding miss (Run 40b).
- Re-reading the strong-field engine numbers (Runs 44–56) where they feed a prediction.

**Foundations**
- Signalling through the field fixed each tick, beyond first post-Newtonian order.
- Deriving the borrowed inputs: Lorentz invariance (including twist across ticks) and inertia = total energy.
- Whether ED's event layer itself charges twist across ticks.
- The vacuum energy's coefficient.
- Particles as knots built from the engine's own commitments.
