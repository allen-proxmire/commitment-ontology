# The commitment ontology, as it stands

Allen Proxmire · 25 October 2026 · after Runs 1–89 (with 81b) of the lattice record

This page states, in one place, what the lattice record tests: the commitment ontology's rules as they stand today. For each rule it gives:
- its formula;
- when it was adopted, and by whom;
- the runs behind it.

Some terms used throughout:
- **Primitives** are the original ontology (§2): commitments, places and relations, possibility, matter, clocks, patterns and the record.
- **Added** inputs are everything adopted after the primitives, whether called a rule or a ruling: rules and choices not in the original ontology, each added, with a date, when a run raised a question the primitives did not answer. The record calls the act of adding one a ruling. Whether any can be derived after all, from the primitives or the other added inputs, is open (§7, Foundations).
- **Provisional** added inputs are marked, with the grounds for going back where these were set in advance.
- **Borrowed:** an input taken from established physics, tracked rather than derived.

The full record (`writeups/commitment_ontology_simulations.md`) holds the evidence for every statement here, and the history of what was tried and dropped. The engine is a model built from these rules, not the whole ontology. The project was formerly titled Event Density.

---

## Inputs, in one list

Everything that goes in, and what each input buys. The primitives, the inputs added along the way, and the borrowed pieces are all inputs: each could have been made differently. What comes out is in §4.

**The ontology**

| input | kind, date | what it buys |
|---|---|---|
| Commitments: irreversible updates at places; time at a place is their count | primitive | one-way time; clocks (Runs 29, 35, 37) |
| Places and relations; sliding places costs nothing | primitive | space as who relates to whom; places can be relabelled freely |
| Possibility: conserved, held at places, hopping between related places | primitive | Newton's unscreened 1/r² (Runs 1, 14) |
| The vacuum never commits | added, 15 October (Run 14) | an unscreened field; the arrow lives in matter |
| Clocks are matter | added, 15 October | redshift, with R2 |
| No infinities | added (a principle), stated 23 October, adopted 24 October | finite counts everywhere; no point of infinite density (§5, item 4) |
| Three dimensions of space | assumed | the lattice; where they come from is open (§7) |

**The rules (§3)**

| input | kind, date | what it buys |
|---|---|---|
| R1: outflow f(P) = c ln(1 + P/p_s) | added, 18 October, provisional | β = 1, which it was designed for (Runs 21–26) |
| R2: the presence clock, N = P/P∞ | added, 18 October, provisional | gravitational redshift (Run 22) |
| R4: the clock field fixed each tick; patterns ride possibility's flow | added, 19 October | a moving body keeps its well (Run 31); no preferred-frame effect from the flow (Run 34) |
| R5: the variational draw, d = T(1 + g), T = (e + 3p)N√γ | added, 19–20 October | the first law and passive = active mass (Runs 52–54); the Tolman pull is derived (Run 30) |
| R5: a pattern's energy draws | added, 19 October | a bound system pulls by its energy (Runs 33, 36) |
| R5: a body is in exact hydrostatic balance, N h(n) = μ̃ | added (a correction), 20 October | static stars (Runs 49–50) |
| R5: the undisturbed vacuum draws nothing; energy is measured from it | added, 24 October | quantum field theory's vacuum energy never enters gravity |
| R6: a pattern hops on its place's ticks and needs free capacity there, so c = N² | added, 17 October, provisional | γ = 1, put in by the rule's two factors (Runs 9, 17, 46) |
| R6: massive patterns obey −N⁴∇²ψ + m²N²ψ = ω²ψ | added, 20 October | quantum matter falls and draws as in GR (Runs 45–46) |
| R8: bodies move as point particles, with action −m∫dτ | added, 20 October | orbits; binaries beyond first order (Run 63) |
| R8: relations shear, and only the shear radiates | added (a reading fixed in advance) | binary-pulsar energy loss (Run 11b) |
| R9: φ's stress, not U's, curves the medium's space | added, Run 66 | β − 1 = −ε/[2(1 + ε)] |
| R10: frame dragging is possibility's own flow (reading Z) | added, 21 October, provisional | Kerr outside spinning holes (Run 69) |
| R11: the core commits what reaches it, where P = 2p_s | added, 19 and 21 October | no echoes; no singularity; a core at areal radius 3m (Runs 43, 73–74) |
| R11: holes are stable | added, 21 October: "it follows from the rules with nothing added" | no evaporation (Runs 68, 71, 74) |

**Borrowed from GR or standard physics**

| input | kind, date | what it buys |
|---|---|---|
| R9: option 3, binding tension curves the medium's space in GR's form | borrowed, 21 October, provisional | static stars and holes as GR's (Runs 65–67) |
| R8: the Lorentz input, a moving body's field is its boosted rest field; in R5, stress pulls with weight 1 per direction | borrowed, 19 October | α₁ = α₃ = 0 and frame dragging (Run 34); binding pulls like rest mass (Runs 42, 44) |
| R7: twist charged on every closed loop, ticks priced like relations | borrowed, 17 October | composite bodies fall alike, as MICROSCOPE requires (Runs 18, 18b) |
| R8: inertia = total energy | borrowed, 20 October | compact bodies' inertia (Runs 52, 55) |
| R11: option A, GR's exterior for merging holes | borrowed, 19–20 October | inspirals and mergers |
| Matter's content: particle masses and charges, nuclear equations of state | borrowed | stars and neutron stars (Runs 45–64) |

**Scales and constants**

| input | kind, date | what it buys |
|---|---|---|
| p_s ≳ 4×10⁵ units per place | from data, Run 24 | clocks of different design agree to 10⁻⁶ |
| P∞/p_s ≳ 1.6–1.9×10⁵ | from data, Run 66 | the pulsar triple PSR J0337+1715 |
| The hop, about 10^2.5–10^3 Planck lengths | from the engine | an open tension with ℓ_ED = ℓ_P (§7) |
| G, c and ħ | measured | the draw's strength, light's speed far from matter, a hold's length |
| Λ, with Λℓ_P² = 3Ω_Λ(H₀t_P)² ≈ 2.9×10⁻¹²² | from data, 24 October (R5) | the observed acceleration; the rules give Λ = 0 |

**The engine** (choices about the model, not claims about nature)

| input | kind, date | what it buys |
|---|---|---|
| A cubic lattice, nearest-neighbour relations, one global hop rate | engine | most runs |
| Note H's carrier: a Kuhn-triangulated lattice with Regge's energy, the corner-metric kinetic form for the relations' stretch, and Regge's end-average lapse coupling; at the first nonlinear order, each shear term's kinetic energy timed by the lapse averaged along its face diagonal, and a field-dependent sliding reaching one place in every direction; at the second lattice correction, a kinetic term coupling neighbouring places and an order-a² change of the first-order energy's lapse coupling (Run 89; fixed only in part) | construction, Runs 83–89 | GR's two polarisations, healthy at the linear level (Run 84); GR's constraint algebra, all three brackets, at the first nonlinear order (Runs 85–86); at field order 2, GR's algebra exactly at the continuum degree, and at the first lattice correction only in a changed constraint basis (Run 87, the basis post hoc); at the second lattice correction, no closure of the kinetic sector in any basis for Run 85's dressing (Run 88), and closure once the a² kinetic term and lapse coupling are free, with the graviton dispersion then forced to be relativistic through a² (Run 89) |

**Not yet used by any run**

| input | kind, date | what it would buy |
|---|---|---|
| The beginning: the One Being, fully in step | stated 23 October | the low-entropy start (§5, item 1) |
| The ripples' size (about 10⁻⁵) and spectrum | from data | any cosmological run |

---

## 1. The picture in one paragraph

- **Commitments.** The world is made of commitments: irreversible updates that happen at **places**. Time at a place is the count of commitments there, so at the bottom time runs one way.
- **Possibility.** Between commitments, places hold possibility, a conserved stuff that hops between related places. It never commits by itself: the vacuum carries no commitment.
- **Matter** is commitment that keeps re-making itself. Each renewal draws on the possibility around it, so matter thins the possibility near it.
- **Clocks are matter.** A clock ticks in proportion to the possibility present where it sits, so clocks near matter run slow. That clock-rate gradient is gravity.
- **Light and quantum matter** are patterns of possibility in transit. They hop on their place's ticks, so they bend and fall in the same field.
- **Quantum mechanics is the study of what happens before ticking** (stated 23 October): patterns of possibility that have not committed. A pattern keeps no clock of its own; the time that elapses in its phase belongs to the committed world around it. A measurement is a pattern meeting the committed world and being forced to commit to one channel.
- **Where possibility runs low, infalling matter commits for good.** Under the current ruling this happens at about twice the medium's crossover scale. That is the core of a black hole, where what falls in becomes record.
- **No infinities** (stated 23 October; adopted 24 October). Every physical quantity is finite: counts, densities, energies, and the number of places in any finite region. Continuum mathematics is an approximation to finite counts. Whether the universe as a whole has finitely many places is open (§7).

---

## 2. Primitives

| Primitive | What it is |
|---|---|
| **Commitment (event)** | One irreversible update. Time at a place is the count of commitments there. |
| **Place, relation** | Space is who relates to whom. Sliding places costs nothing. In the engine, places form a 3D lattice with nearest-neighbour relations. |
| **Possibility** | A conserved quantity held at places, P units per place. It hops between related places. **The vacuum carries no commitment** (ruled 15 October, after Run 14). |
| **Matter** | Commitment that keeps re-making itself. In the engine it is a reserved pair of places that takes one unit from each, holds, and renews. Mass is the upkeep. |
| **Clock** | Matter that counts its own commitments (**clocks are matter**, ruled 15 October). What a clock reads was ruled on 18 October (R2). |
| **Pattern** | A pattern of possibility in transit: light, and quantum matter. |
| **Record** | What has been committed: the history. It is kept. |

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
  - both scales are set by observational bounds, not by CO.
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
- **On lattices with imposed curvature,** clocks follow the zero-range theory: Run 70 at p_s = 4, Runs 72–72b at p_s = 1.
  - The gap between two clock designs shifts with the sign of the curvature by the amount the theory predicts. It is detected at 5.1σ and matches the prediction to 0.5σ (Run 72b).
  - The zero-range theory's apparent underestimate of these clocks' own dips, about 0.25% for one design and 0.5–0.6% for the other (Runs 72b, 75, 76), is mostly its ambient normalisation; evaluated at the ambient the conserved total gives, the offsets fall to about zero (Run 78's check, post hoc). Run 80 confirmed this on the flat lattice with predictions registered beforehand.
  - A lattice curved by the medium's own stress can be built exactly in planar symmetry (design note Note F). On it the engine's medium carries the flux the lattice was built with, to about 0.2% (Run 77). With option 3's clock the planar solution is flat (Rindler) spacetime.
  - With one global hop rate on a regular equal-place lattice, such a lattice exists only while the source's draw times the distance to the reservoir stays small (Run 77). It comes from the representation: it disappears if clocks slow with the hops, so CO's rules are not shown to impose it. Where large stress curvature can be carried, it sits next to a strong source, at a slow medium.
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
- With R1's outflow, y''/(2y'²) = −1/[2(1 + P/p_s)]. So at large p_s
$$
\beta-1=-\frac{\varepsilon}{2(1+\varepsilon)},\qquad \varepsilon=\frac{p_s}{P_\infty},
$$
  and β is inside Mercury's band (|β − 1| ≤ 0.003) once P∞/p_s ≳ 166 (Runs 22–23).
- Two bodies' wells multiply (f = 1.12 ± 0.19, Run 26).

### R4. The field's dynamics (ruled 19 October; Runs 31, 34, 35)
- **The clock field is fixed each tick:** the medium's stationary law, drawn afresh. So a moving body keeps its well, with no diffusion lag.
- **Patterns ride possibility's flow.**
- **The engine's tick is not physical time.**

### R5. What draws (rulings 19–20 and 24 October; Runs 30, 33, 36, 40–42, 49–55)
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
- **The undisturbed vacuum draws nothing; energy is measured from it** (ruled 24 October).
  - A body or pattern draws by its energy above the undisturbed vacuum. That includes any change it makes to the vacuum's zero-point energy (the Lamb shift, binding energies), which equivalence-principle tests show must draw (Polchinski 2006).
  - So quantum field theory's vacuum energy, about 10¹²⁰ times the observed value, never enters gravity, as in unimodular gravity.
  - **Λ is then an input.** The rules give Λ = 0, and the observed value is taken from data:
$$
\Lambda\,\ell_P^2=3\,\Omega_\Lambda\,(H_0t_P)^2\approx2.9\times10^{-122}.
$$
    Unimodular gravity takes Λ the same way, as a constant of integration.

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
- **CO's original rule** (option 1, with R6) kept γ̃ flat.
  - With CO's field equation this gives the exponential metric e^(∓2U): γ = β = 1 at first post-Newtonian order, and no horizons.
- **Option 3** (ruled 21 October, provisional): binding tension curves the medium's space, in GR's form.
  - At ε = 0 (no medium scale), GR's static equations are exactly:
$$
\tilde\Delta U=-4\pi\,(e+3p)\,e^{2U},\qquad
\tilde R_{ij}=2\,\partial_iU\,\partial_jU-16\pi\,p\,e^{2U}\,\tilde\gamma_{ij},\qquad hN=\text{const}.
$$
    The first is CO's own field equation, written on γ̃ (Run 65).
- **With CO's medium** (Run 66), the transported field is φ = z∞ − z. It is linear on the lattice, and the clock is
$$
N=\frac{P}{P_\infty}=(1+\varepsilon)\,e^{-\varphi}-\varepsilon,\qquad \varepsilon=\frac{p_s}{P_\infty},\qquad \frac{dU}{d\varphi}=1+g,\quad g=\frac{\varepsilon}{N}.
$$
  - φ's stress curves γ̃:
$$
\tilde R_{ij}=2\,\partial_i\varphi\,\partial_j\varphi-16\pi\,p\,e^{2U}\,\tilde\gamma_{ij}.
$$
    That is a recorded choice. With U's stress instead, β = 1 exactly; with φ's, β − 1 = −ε/[2(1+ε)].
  - **Under option 3 and that choice, ε sets every static departure from GR.** CO's static stars and holes are GR's to O(ε) (Runs 65–67).
  - The clock stops where GR's lapse would be about ε, with no event horizon (Run 67).
- **Going back to option 1** (grounds set in advance): if option 3 cannot be written to all orders as one consistent theory, or if it loses a result or fails data that option 1 passes.

### R10. The current field and rotation (rulings 21 October, provisional; Runs 34, 69)
- **Option 3 covers the current field.** g₀ᵢ and its back-reaction take GR's nonlinear form.
- **The input current field is a flow of possibility**. Around a spinning body, possibility circulates and carries patterns along, so the medium's frame is the zero-angular-momentum frame.
  - Its clock is that frame's lapse α ("reading Z", adopted provisionally after Run 69).
  - Then spinning holes are Kerr outside the horizon to O(ε/α).
- **Cost:** reading Z interprets an input; CO's rules do not imply it.
  - The engine's possibility flow is a gradient, and cannot circulate.
  - When rotation is built in, the flow needs a part that moving matter drags around (a curl part).
- **Going back:** if CO's dynamics cannot carry a circulating flow, or if reading Z fails a test that the alternative (reading K, places held fixed) passes.

### R11. Black holes: option A and the core (rulings 19–21 October; Runs 28, 43, 67, 68, 71, 73, 74)
- **Option A** (borrowed; 19 October, extended 20 October): outside black holes the field is GR's, with CO's core inside.
  - Option A now carries binary-black-hole inspirals and mergers.
  - Under option 3, static holes (Runs 65–67) and spinning exteriors (Run 69) follow from CO's own equations instead.
- **The core commits what reaches it** (19 October). It is a total absorber, so there are no echoes, and what falls in becomes record (Run 43).
- **Where:** infalling matter commits where the medium's possibility per place falls to k·p_s, with k = 2 (21 October, 14:00). Since N = P/P∞, that is where the clock has fallen to 2ε.
  - **It catches all causal matter.** In a thin-shell model at physical ε, the stiffest causal matter turns back at most at 1.27p_s (Run 73). Ordinary dense matter (w ≲ 0.6) turns back below about 0.75p_s.
  - **Any k above about 1.34 would work.** k = 2 is twice the medium's crossover.
  - **The core's areal radius is 2m(k + 1)/k,** which is 3m at k = 2 (Run 74, computed post hoc with the corrected conversion).
- **CO's holes are stable** (ruled 21 October: "it follows from the rules with nothing added"). This replaced the 19 October ruling that black holes evaporate (Runs 68, 71, 74; §5).
- **Going back:**
  - if the exterior's own dynamics, once written, give a conflicting bounce or commitment rule;
  - if matter is found that turns back above 2p_s;
  - if the discrete regime below one unit per place re-emits.

### Withdrawn or superseded

| Rule | Status |
|---|---|
| The vacuum commits (CO's original event layer) | dropped 15 October (Run 14); CO's event-layer results 20–22 and 27 were obtained with it and have not been re-tested |
| The flow clock (16 October): a hold lasts while a fixed amount of possibility *passes* | replaced by the presence clock, 18 October |
| Slowing possibility's own hops by the local clock | not adopted: the medium froze (Run 17) |
| Bodies keep their proper size (19 October) | superseded for static bodies by hydrostatic balance, 20 October |
| Defaults (c2), (c3) for binding tension | suspended, then replaced by option 3 (21 October) |
| Black holes evaporate (19 October), with two tracked assumptions | withdrawn 21 October: CO's holes are stable |

---

## 4. What is derived, what is added, what is borrowed

| Observed | How the ontology gets it | Runs |
|---|---|---|
| Newton: 1/r², linear in the source, no screening | **derived:** matter's draw on a medium that never commits | 1, 14 |
| Gravitational redshift | **derived:** the presence clock | 22 (15 under the flow clock) |
| Patterns fall at the clock-set rate, all masses alike | **derived:** a pattern turned by the committed world's count, with no coupling | 16, 27 |
| Wells obey the medium's equation of state | **derived:** local equilibrium | 22, 25 |
| Rest mass in a well pulls by its clock rate (Tolman) | **derived:** a body's pull is its ticking | 30 |
| No preferred-frame effect from the flow (α₂ = ζ₁ = ξ = 0) | **derived** from conservation, given R4 and R8 | 34 |
| Time runs one way; time-averaging shrinks the order | **derived:** commitments are never undone. Order in a clock's record falls about as 1/T, 26× down but not zero | 29, 35, 37 |
| Light bending, Shapiro delay (γ = 1) | **added:** the pattern rule (R6) | 9, 17, 46 |
| Mercury; β = 1; wells multiply | **added:** the medium and clock (R1–R2), designed for β = 1 | 22–26 |
| Clocks of different design agree; ζ₂; the pulsar triple | **scales chosen within data bounds:** p_s ≳ 4×10⁵, P∞/p_s ≳ 1.6–1.9×10⁵ | 23, 24, 30, 45, 48, 55, 57, 66 |
| Bound and composite matter fall alike (MICROSCOPE) | **borrowed:** twist on loops that include a tick (R7), plus the full pattern rule | 18, 18b, 46–48, 52, 54 |
| α₁, α₃, frame dragging, the Earth–Moon test | **borrowed:** the Lorentz input | 34 |
| At weak field a bound system pulls by its total energy | **added** (pattern energy draws) **and borrowed** (momentum flux draws) | 36, 40c |
| Internal binding pulls like rest mass (ζ₄) | **borrowed:** the Lorentz input in full form (stress pulls) | 42, 44, 49, 50 |
| A compact body's inertia is its total energy | **borrowed** | 52, 55 |
| Binary-pulsar energy loss | **added:** relations shear (a reading fixed in advance) | 11b |
| Static black holes and neutron stars as GR's; ringdowns, shadows | **added:** option 3, plus reading Z for spin; before that, option A | 28, 39, 41, 65–67, 69 |
| Binary-black-hole inspirals and mergers | **borrowed:** option A | 63 (the ruling) |
| Holes absorb, leave no echoes, are stable | **added:** the core commits, at 2p_s | 43, 67, 68, 71, 73, 74 |

**The two scales are bounds from data, not predictions:**
- p_s ≳ 4×10⁵ units per place, so that clocks agree to 10⁻⁶;
- P∞/p_s ≳ 1.6–1.9×10⁵, from the pulsar triple PSR J0337+1715 (2.5–2.9×10⁵ with the planet model; Run 66).

Nothing in the earlier papers fixes either.

### The same accounting in other programs

No approach to gravity derives it from nothing. Each takes some of known physics as input, and is judged by two things: being clear about what goes in, and what comes out that was not put in.

| program | what goes in | what comes out that was not put in |
|---|---|---|
| **Loop quantum gravity** | GR's own action, quantized. Classical GR is the starting point, not a result. | Quantum geometry: discrete spectra of area and volume (Rovelli & Smolin 1995). Getting smooth GR back out is its main open problem. Its black-hole entropy matches Hawking's only once a free parameter (the Barbero–Immirzi parameter) is set to make it match (Ashtekar, Baez, Corichi & Krasnov 1998). |
| **Causal dynamical triangulations** | GR's action in discrete form, plus a rule that keeps causal order. | A four-dimensional universe emerges from gluing simplices, and the dimension drops toward two near the Planck scale (Ambjørn, Jurkiewicz & Loll 2004, 2005). |
| **Causal sets** | Discreteness and causal order: "order plus number equals geometry" (Bombelli, Lee, Meyer & Sorkin 1987). | A cosmological constant of roughly the observed size, predicted by Sorkin before it was measured. Its "sequential growth" dynamics, with events added one by one, is the closest relative of commitment (Rideout & Sorkin 1999). |
| **Spacetime thermodynamics** | Known physics: the Unruh temperature, entropy proportional to horizon area, and the Clausius relation δQ = T dS. | Einstein's equations, as an equation of state (Jacobson 1995). |
| **This ontology** | Commitments, possibility and its outflow, the presence clock, matter's draw, the pattern rule (§3), plus the tracked borrowings in the table above; every input is listed at the top of this page. | Newton's law, redshift, universal free fall, the Tolman pull, no preferred-frame effect, and one-way time, from the rules (Runs 1, 14, 16, 22, 27, 29, 30, 34). |

The comparison is one of method, not of maturity. Each program states its inputs and is held to what it gets out. Here the main borrowed input, option 3's rule for how the medium's space curves, is also the main open problem: replacing it with a rule from the ontology's own primitives (§7).

---

## 5. Where CO speaks and GR is silent (not yet tested as predictions)

1. **Time's direction is fundamental, not a boundary condition.**
   - The engine's bottom is one-way.
   - A clock's time-averaged record loses most of the order, falling as 1/T. What leaks goes as 1/T times a coefficient that is unknown at physical scales.
   - This is one of the ontology's coarse-graining claims, not yet a test of nature (Run 29).
   - **Why averaged laws cannot tell forward from backward** (stated 23 October).
     - **Average a one-way process at a steady state, and the direction-telling terms cancel, leaving only the even ones.**
     - The picture is standing on top of a bell curve. The slope there is zero, and the ground falls away the same in every direction. Near the top the height is h₀ − ½kx², unchanged under x → −x: the one term that could tell directions apart, the slope, has cancelled.
     - In time, an equation tells forward from backward only through terms odd in time, such as a first time-derivative (friction is the everyday case). GR's field equations have none: running time backward turns every solution into another solution. GR does not run time both ways; it cannot tell the two apart.
     - **In the engine, at a steady state:**
       - every commitment and every hop is one-way, yet the averaged field (R3) has no time in it at all;
       - a clock's time-averaged record loses its order as 1/T (Run 29);
       - under R4 the vacuum's law is in detailed balance, so the arrow lives in commitment (Run 35).
       - One average keeps its direction even at a steady state: the steady inflow of possibility into each clock (Run 29). A current reverses when time is reversed. So the arrow survives where matter keeps re-committing.
     - **Off the steady state.**
       - The engine's medium as first built (R1's wander rule, Runs 21–31) spreads by diffusion. From the mean-current identity, ⟨J⟩ = W(z_x − z_y)/6 on every link (R3; Note G), with the hop length and the tick as units,
$$
\frac{\partial P}{\partial t}=\frac{W}{6}\,\nabla^2 z\;\approx\;D\,\nabla^2P,\qquad D=\frac{W f'(P)}{6}.
$$
       - That is a first time-derivative, so diffusion tells forward from backward: a moving body trails its well (Run 31).
       - R4 replaced it. The clock field is fixed afresh each tick, so its equation has no time in it, while things change as at a steady state. **This is GR's own structure for the well.** In linearised GR the potentials obey Poisson-type equations with no time derivatives of the fields, and only the shear part obeys a wave equation (Flanagan & Hughes 2005, §2.2, Eqs. 2.62–2.65, in units G = c = 1):
$$
\nabla^2\Theta=-8\pi\rho,\qquad \nabla^2\Phi=4\pi\big(\rho+3P-3\,\partial_tS\big),\qquad \nabla^2\Xi_i=-16\pi S_i,\qquad \Box\,h^{TT}_{ij}=-16\pi\,\sigma_{ij}.
$$
       - R4 was ruled, not produced by averaging. In GR the reason is the constraint (gauge) structure, not averaging, so the match is one of structure only.
       - **So the open question is the waves.** GR's gravitational waves are two-way while they travel, and so are CO's patterns. In CO both wave equations were adopted: the shear of relations (Run 11b) and the wave equation for patterns (R6, Runs 45–46).
       - **Run 81: averaging a one-way process can give a two-way wave, if a current is conserved.**
         - The run's measure for a wave, a(t) ≈ C e^{−γt} cos(ωt + φ), is the direction-telling share Q⁻¹ = γ/ω: the decay tells direction, the oscillation does not.
         - In a medium whose units keep their direction of travel and swap it only in one-way, momentum-conserving collisions, Q⁻¹ falls in proportion to 1/wavelength, as k^(1.00 ± 0.03). So it is two-way at large scales, while things change.
         - CO's medium as first built (random hops) has no current and stays one-way at every scale. Losing the current at random sends the large scales back to one-way.
         - **A conserved current is needed for waves at all scales.**
         - This is ordinary lattice-gas sound. An exactly reversible bottom gives the same large-scale wave (Run 81b). So at large scales it does not locate the arrow, as above.
         - **The averaged wave does not show the arrow (Run 81b).** Its damping follows each rule's local collision response, reversible or not. The one-way cycle shows in that local response, as a relaxation that rotates, not in the wave. The arrow lives at the bottom, and averaging to large scales hides it.
         - These waves are longitudinal sound. GR's are shear, which needs a restoring force as well: in CO's terms, the relations' tension. Relations with Regge's energy supply it: they carry GR's two shear polarisations at light's speed, healthy at the linear level (Runs 83–84).
         - A medium carrying sound would radiate scalar waves, which Run 11b bounds. So the current belongs to the carriers of CO's waves (the relations, patterns), not to the well.
     - **The engine's medium is itself an average** (stated 23 October). A scaleless substrate has no direct model, so the engine uses an averaged medium as its stand-in.
       - The diffusion belongs to that stand-in: units hopping at random, with no memory of direction. It is not shown to belong to the substrate.
       - Which averaged medium the substrate gives while things change is open.
     - Standard physics gets the same two-way averages from two-way micro-laws, so at a steady state the two accounts agree. They part in the leftover (Run 29's 1/T) and in how things change.
   - **The beginning, and the past hypothesis** (stated 23 October).
     - Standard physics explains the arrow by a very special low-entropy start. Penrose put the chance of starting that smooth at 1 in 10^(10^123), measured against every state the universe could have started in.
     - The ontology removes the menu. The beginning is a timeless, scaleless whole of uncommitted possibility, fully in step: "the One Being".
     - Before any commitment there is nothing differentiated to choose between. This follows from the ontology being relational, a matter of contrast: a thing is what it is only against what differs from it, so with no differences there is nothing yet to relate. So a smooth, ordered start is not a lucky draw: it is the only state with zero becoming.
     - **The low-entropy start stops being improbable, because there was nothing else it could have been.**
     - This matches where Penrose's number comes from. It is gravitational entropy: the early universe is special because gravity had not yet clumped anything. In the ontology gravity is clock-rate gradients, and a state fully in step has none.
     - **Open:**
       - why the One Being begins to commit;
       - why the first commitments leave near-uniform ripples, about one part in 10⁵, with the measured spectrum;
         - **One proposal** (stated 23 October): the first commitments happen at virtually the same moment at every place of the One Being, rather than spreading from one seed. A single seed would give the universe a centre, and the CMB shows none.
         - The ripples would then be the small offsets in when places first commit. Standard cosmology has the same reading in the time-delay picture of inflation, where the curvature ripple is the local delay of the start, ζ ≈ H δt (Guth & Pi 1982).
         - What sets the offsets' size and their nearly scale-free spectrum (n_s ≈ 0.965) is not worked out.
       - whether the universe also ends at the One Being.
2. **The quantum vacuum's energy does not draw** (R5, ruled 24 October).
   - The vacuum carries no commitment. Under R5 neither the undisturbed medium nor the undisturbed vacuum's zero-point energy draws, so quantum field theory's vacuum energies (about 10¹²⁰ times too large) never enter gravity, as in unimodular gravity. Changes that matter makes to the zero-point energy still draw, as equivalence-principle tests show they must (Polchinski 2006).
   - This removes the old cosmological-constant problem but not the new one: the rules give Λ = 0, while Λ is observed to be positive (Ω_Λ ≈ 0.69). Λ is taken from data as an input; what sources it in CO is open.
   - The classical vacuum drawing nothing is not distinctive: GR without Λ has it too.
   - With rotation, the clock equation gains a vacuum source (Run 69).
3. **Compact bodies slightly break the strong equivalence principle.** A neutron star's gravitational mass exceeds its inertia:
$$
\Delta=\frac{\varepsilon\,C}{1+\varepsilon},\qquad \varepsilon=\frac{p_s}{P_\infty},\qquad C\approx0.37\text{–}0.44\ \text{(pulsar of PSR J0337+1715)} .
$$
   - GR gives zero.
   - The sign is fixed (Δ > 0), the effect grows with compactness, and it is not additive. Its size waits on ε.
   - This depends on inertia = total energy (borrowed) and on Run 66's choice that φ curves γ̃ (Runs 52, 55, 57, 65, 66).
4. **No point of infinite density is reached,** as the no-infinities principle requires (§1).
   - The mean-field geometry is singular at P = 0 (Run 67).
   - Under the ruling, matter commits first, at P = 2p_s and areal radius 3m (Runs 73–74).
   - The hole has no event horizon, and it is cold (κ = 0).
5. **Black holes do not evaporate.**
   - **A collapse emits GR's Hawking flux only as a transient,** for about 8M ln(P∞/p_s). That is about one quantum in the 1+1 model, about 10⁻² in 4D (Run 68).
   - **When the matter commits,** a cold core gives one flash of about ħ/δu and then silence; a continued state gives a faint negative tail instead (Run 74). δu, how long commitment takes as seen from far away, is not fixed by CO's rules.
   - **Black-hole thermodynamics** (S = A/4, T = κ/2π) does not carry over without a new argument.
6. **Under CO's original rule for space only** (withdrawn under option 3), heavy neutron stars need matter near the causal limit above about twice nuclear density. Heavy-ion collisions allow this only at the edge of their bounds (Runs 57–62).
7. **Matter over antimatter** (stated 23 October, not tested).
   - In the beginning, commitments formed in a saturated space, with no room for a second pattern to form. So one kind of matter committed and its mirror did not.
   - Standard cosmology instead has matter and antimatter almost entirely annihilating, leaving a small excess, by a mechanism (Sakharov's conditions) not yet identified.
   - **To hold up, the idea has to answer two things:**
     - why antimatter forms readily today, in accelerators and in cosmic rays;
     - where the cosmic background's photons, about 1.6 billion per proton (η ≈ 6×10⁻¹⁰), come from, if antimatter never formed at the start.

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
| 65–69 | GR's clock equation in CO; option 3; static and spinning black holes; evaporation |
| 70–80 (with 72b) | clocks on curved lattices, and how accurate the clock theory is; collapse through a hole's throat; where infalling matter commits, and what that radiates; the medium on space curved by its own field; the engine's own equation of state; a local rule for the medium's space |
| 81, 81b | whether averaging a one-way process can give a two-way wave; a reversible control |
| 82 | the speed of the relations' stretch waves in a well: which formulation gives light's cone (a calculation) |
| 83 | the normal modes of a lattice of relations carrying their own stretch: mode count, speed and stability on both routes (a calculation) |
| 84 | a kinetic form for the relations that keeps GR's constraint structure exactly: both routes healthy at the linear level (a calculation) |
| 85 | GR's constraint algebra at the first nonlinear order on that lattice: how the lapse must multiply the kinetic energy (a calculation) |
| 86 | the rest of that algebra, {H, D} and {D, D}, at the same order: whether one local field-dependent sliding closes both (a calculation) |
| 87 | the whole algebra at field order 2, order by order in the lattice spacing: whether the sliding, the kinetic metric and the structure functions extend so that all three brackets still close (a calculation) |
| 88 | the kinetic part of that algebra at the second lattice correction, in any constraint basis: whether it is first class at order a² (a calculation) |
| 89 | the same, with the theory's own a² freedoms: whether a kinetic term coupling neighbouring places, and a² changes of the energies' lapse couplings, make the kinetic sector first class at order a² (a calculation) |

---

## 7. Open

**The medium and its scales**
- What fixes p_s and P∞.
- CO's hop: the engine needs it to be about 10^2.5–10^3 Planck lengths. That is an open tension with the corpus's P08 (ℓ_ED = ℓ_P), decided 20 October.
- Whether φ's or U's stress curves the medium's space (it sets β − 1).

**The medium on a stress-curved space**
- The medium's dynamics there: the dynamical completion with ε ≠ 0.
- Clock universality on a lattice whose curvature comes from the medium's own stress. The planar lattice is built and self-consistent (Run 77); spherical symmetry is untested.
- Whether the clock theory's error depends on the lattice. A replication was undecided (Run 76); after the ambient normalisation, design 2 at negative curvature is still 2.0σ off the other lattices (Run 78's check).
- How the engine should represent a strongly curved γ̃. With one global hop rate on a regular equal-place lattice, a self-consistent planar lattice exists only while the source's draw times the distance to the reservoir stays small (Run 77). Slowing clocks with the hops, isotropic cells, or a local tick would avoid that; which is right is a choice about the representation, possibly about the hop rule.
- How the medium's space curves: two readings, both to be tested (22 October).
  - **(A) Space is the pattern of relations.** Curving it means relations form, dissolve or rewire. In the engine: shells whose place counts follow option 3's areas, with all relations equal.
  - **(B) Relations are fixed; space is a reading of the medium's state across them,** as time is read from commitment and light's geometry from the pattern rule. In the engine: the medium's hop across a relation depends on its own state, directionally, since stress is directional. This needs a ruling, and must avoid the freezing found in Run 17. The local rule fixed by option 3's planar solution is excluded by light bending (Run 79); rules using second derivatives, or a state carried by the relations, remain. Note H proposes that the state is the relations' own stretch, which would also carry the waves.
  - Relations can dissolve: a dissolved link goes back to possibility, as a two-part possibility pattern (stated 22 October). So (A) is open, with 3D space assumed. A spherical hole can be built under either reading; the readings separate only in how the geometry forms (design note Note G).

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
- Whether CO's waves (the shear of relations, and patterns) come out two-way from the one-way layer, as GR's are. Both wave equations were adopted. Run 81: averaging a one-way process gives a two-way wave at large scales if a current is conserved; shear also needs a restoring force, which Regge's energy on the relations supplies (Runs 83–84; §5, item 1).
  - **Note H (design note):**
    - **What a carrier needs:** relations with their own stretch and an exactly conserved current, on a face-centred or triangulated relation graph (the engine's cubic relations carry only 3 of the 6 strain components), Regge's energy, and GR's two constraints enforced every tick: sliding at every moment, and isotropic stretch fixed by matter, which stability requires.
    - **Light's speed needs a second factor of N** beyond the ticks.
    - **What fails:** places that move (any displacement medium) and momentum fluids cannot carry the TT waves.
    - **The proposal for testing:** the relations' stretch is option 3's γ̃, which would make it one object for the static space and the waves.
    - **Two routes (Note H §8, after reading GR-I–IV and KM-I–II):**
      - GR's: no extra scalar, with both constraints every tick.
      - The khronometric route of the earlier papers: a healthy fast scalar, allowed after GW170817 for ξ = 1, |α| ≲ 10⁻⁷ and 0 ≤ λ − 1 ≲ 0.1.
    - **The speed (Run 82):** stretch updates on place ticks alone give c_h = N and γ_GW − γ_EM = −1, excluded by GW170817 about 3.8×10⁶ times over. A second factor of N is required. It may sit in the space (the waves on physical space g = N⁻²γ̃), in the stiffness, or in the clock (the stretch's rate gated by ticks and free capacity, as light's is in R6); all three give light's cone. The registered numerical tolerances failed (dispersion, and second-order terms in the statistic); the physics did not.
    - **The mode count (Run 83, Kuhn-triangulated lattice, Regge's energy, a per-tetrahedron DeWitt kinetic form):**
      - **The counting works.** On both routes the relations carry exactly two TT modes at c² = 1, isotropically. On the khronometric route the long wavelengths are the continuum's: the scalar at its continuum speed, and the extra non-metric mode gapped at ω² = 6 and healthy.
      - **Stability does not.** For every λ > 1 the khronon is unstable above |k| ≈ √(2(λ−1)/μ_L), at wavelengths of about 2.1/√(λ−1) spacings. Only λ < 1/3 is healthy throughout, and observation excludes it.
      - **GR's route** fails at long wavelengths with the lapse averaged over each relation's ends. A tuned local weighting removes most of it (post hoc). Run 84 showed that the same end-average coupling is exactly right once the kinetic form meets the criterion, so the fault was the kinetic form's.
      - **The common root is the kinetic form.** Its longitudinal-shift term carries a k⁴ correction (μ_L ≠ 0).
      - All seven registered tests failed, partly because the registered solver lost precision at small k.
    - **The kinetic form (Run 84, the corner metric: the DeWitt form of the metric read from the six relations arriving at a place):**
      - **GR's route works at the linear level.** With no inertia for the body diagonal (N0), the relations carry exactly the two TT modes, with ω² = |δ|², |δ|² = Σ4sin²(k_a/2), at every k: the continuum's linear theory with forward differences. The Hamiltonian constraint is first class, and the lapse coupling is Regge's own end-average coupling.
      - **The khronometric route is healthy exactly when α < 2ξ,** as in the continuum, for every λ > 1 tested (1 + 10⁻⁶ to 2). An exact Regge identity, q_w†Vq_w = −4|δ|², decides it.
      - **Run 83's failures were its kinetic form's:** the two runs share the potential and the lapse coupling exactly.
      - Giving the body diagonal its own inertia (N1) fails on a closed curve near the zone corners, where that inertia vanishes and the extra mode's frequency diverges. N0 is the version to carry forward.
      - The kinetic form is constructed, not derived, and it breaks lattice inversion (mirrors are kept). Everything is linear, around flat space.
      - **Next:** whether the linear gauge symmetry survives at second order (the cubic action), where Regge-type lattices are known to fail; a parity-even construction; then H3 (the source), H4 (β) and H5 (a one-way engine).
    - **Second order, the {H, H} bracket (Run 85):**
      - At the first nonlinear order the Hamiltonian constraints close onto the momentum constraints,
$$
\{H[N],H[M]\}=D[\xi U],\qquad U_a(x)=N(x)M(x+e_a)-M(x)N(x+e_a)\;\to\;\xi\,(N\nabla M-M\nabla N),
$$
        once each shear term's kinetic energy is timed by the lapse averaged along its face diagonal. The three natural timings fail at O(ka). The closing one is unique up to canonical transformations, and works through an exact twisted Leibniz rule.
      - **It adds no independent evidence (the check):** on this kinetic form at λ = 1, this closure is equivalent to Run 84's linear first-class structure. No timing closes it at λ ≠ 1.
      - N0's body diagonal is ill-defined beyond first order; higher orders need it fixed by its N = 1 equation (N0′), or N1.
      - The check named the decisive test: whether one local field-dependent sliding closes both {H, D} and {D, D} at this order (Run 86).
    - **Second order, {H, D} and {D, D} (Run 86):**
      - **Both close, with one local sliding.** With the body diagonal fixed by its N = 1 equation (N0′), a field-dependent sliding D[u] = Σπ·(Γu + S_u h) closes both brackets at first order in the fields:
$$
\{H[N],D[u]\}=-H[L(u,N)],\qquad\{D[u],D[v]\}=D\big[[u,v]\big].
$$
        - S couples u and h within one place of each other in every direction (the box(1) stencil).
        - The check verified the closure in real space with explicit Poisson brackets: {H, D} to 3×10⁻¹³, {D, D} to 5×10⁻¹⁶.
        - The axis-only stencil fails, with an O(a²) defect already in {H, D}.
      - **GR's structure is forced, not chosen.** The basis-independent leading-order content of the structure functions is GR's: L → u·∇N and [u, v] → the Lie bracket. The equations force it. What remains free is a choice of basis, plus one O(a) parameter in [u, v].
      - **The sliding is not unique:** it is one member of a large family, and it has not been identified with a geometric action.
      - **What is new beyond Runs 84–85:** the local closure of {D, D}'s two TT components jointly with {H, D}. The rest was guaranteed by the linear structure (the check).
      - **Against the registered expectation,** which leaned toward failure. That expectation's rationale does not apply at this order: near flat space Regge's diffeomorphism symmetry breaks quadratically in the curvature (Bahr & Dittrich 2009). That enters the action at fourth order in the fields, so breaking of Regge's own vertex-displacement symmetry would show in the constraint algebra at field order 3 (Run 87's check). Other discreteness effects can appear at field order 2 (Run 88).
      - **Two structural facts.**
        - The lapse coupling to the body diagonal vanishes identically, so N0′'s nonlinear part drops out at this order.
        - The kinetic form does not enter at this order.
      - **So GR's route passes the first nonlinear test that Run 84 does not decide.** With Run 85, all three brackets close at field order 1. The khronometric route stays a fallback.
      - **Field order 2:** Run 87, below.
    - **Field order 2, all three brackets (Run 87):**
      - **The test.** Regge's third-order energy (with N0′'s second-order body diagonal), the kinetic metric's dependence on h, a second-order sliding and h-dependent structure functions, solved order by order in the wavevectors with free moments. Two truncations: the continuum degree (D0) and the first lattice correction (D1, order a).
      - **At the continuum degree, GR's algebra exactly (K87a PASS).** The solution found is GR's own continuum constraint algebra, to 1.5×10⁻¹⁴ (the check), and its kinetic part is unique. This confirms Regge's third-order energy, the body diagonal's second-order term and the DeWitt kinetic metric. It was expected once the lattice's continuum limit is GR's, so it is not evidence of a lattice gauge symmetry.
      - **At order a, as registered: FAIL (K87b).** The kinetic sector, {H, D} at order π² with {H, H} at order πh, has no solution with structure functions independent of π. The check certified this: the sector is linear, and LAPACK finds the same inconsistency with a clean rank gap. The potential sector closes.
      - **What fails is the constraint basis, not the algebra (post hoc, confirmed by the check).** In the basis
$$
\tilde H[N]=H[N]-D[X(N;\pi)],\qquad X_a=\tfrac14N\,(2\pi_{aa}-\operatorname{tr}\pi)=\tfrac14\dot h_{aa},
$$
        all three brackets close at order a with structure functions that depend on h only. X is unique. The change is triangular, so the constraint surface and the first-class property are the same, and Runs 85–86 stand. The registered reading, that GR's algebra breaks at order a and the khronometric route becomes operative, is not supported.
      - **A geometric reading (a heuristic).** Each place's metric is read from its links; as an axis link lengthens, the point it measures moves by half the change, ¼ḣ_aa. The GR-form basis subtracts that drift. Why the face diagonals contribute nothing is not explained.
      - **What field order 2 fixes.** Run 86's free O(a) bracket parameter is fixed at the Lie value. The first-order family shrinks from 87 directions to 20, all trivial redefinitions. The kinetic metric's continuum h-dependence is forced to be DeWitt's; its order-a part is not the simple lattice DeWitt form.
      - **The constraint basis that closes is not a D4 dressing.** Its momentum-squared part couples neighbouring places, outside Run 85's class of dressings.
      - **So GR's route survives field order 2 through order a,** with a changed constraint basis. Formal: at the origin of momentum space only.
      - **The next lattice order:** Run 88, below.
    - **Field order 2, the kinetic sector at order a² (Run 88):**
      - **The test.** The four kinetic conditions ({H, D} at orders h and π², {D, D} at order π, {H, H} at order πh) at the second lattice correction, in two forms:
        - first class, with the π-linear structure functions that time reversal allows (V in {H, H}, Y in {H, D}). Any triangular change of constraint basis produces these, so this form fixes no basis;
        - a slide basis H̃ = H − D[X], X free through order a.
      - **Both fail (K88a, K88b FAIL; certified by the check).** For the registered lattice Hamiltonian (D4's dressing, Regge's energy with the end-average lapse), no local first-class closure exists at order a² in the kinetic sector. The check found the test complete for that Hamiltonian, and the solver able to close planted D2 problems.
      - **Where it breaks.** In {H, D} at order π², i.e. the kinetic dressing's covariance under the sliding at order a²:
$$
W^{(1)}(N;\Gamma u)=S_u\Omega(N)+\Omega(N)S_u^\dagger-\Omega(L^0)+\big(\Gamma Y+(\Gamma Y)^\dagger\big)
$$
        has no solution once the first-order conditions fix the sliding. {H, H} with the first order alone still closes.
      - **What removes part of it (post hoc, the check).** A non-ultralocal order-a² dressing, coupling π at neighbouring places beyond D4, closes the spatial-covariance part exactly. {H, H} at order πh then fails under every freedom tested, including the general a² lapse coupling of Regge's second-order energy; 0.43–0.50 of the obstruction remains. The freedom left untested, the first-order energy's a² lapse coupling, is what closes it (Run 89, below).
      - **Reading.**
        - Within the tested family, this lattice can be made spatially covariant at a², but not first class. (Superseded by Run 89: with the first-order energy's a² lapse coupling free, it is first class in the kinetic sector.)
        - The khronometric route, which does not need {H, H}, faces the same obstruction as registered. With the dressing change its kinetic sector closes, but that change has to be registered first. (Run 89's check: this statement of the route is incomplete. The route proper has λ > 1 and an α term in the lapse gradient, and {H, H} still supplies its lapse equation.)
        - The breaking is of relative order (ak)², far below measurement. It bears on the theory's consistency (extra modes), not on a direct observable.
        - It is consistent with the literature: discrete constraint algebras generically fail to close in 4D away from flat and homogeneous sectors.
        - It counts, modestly, toward reading (A) of how space curves (relations that form and dissolve) over Note H's fixed-relation carrier. (Withdrawn at this order after Run 89.)
      - **The freedoms registered:** Run 89, below.
    - **Field order 2, the kinetic sector at order a², with the theory's freedoms (Run 89):**
      - **The test.** Run 88's first-class form, with freedoms of the theory added at order a²:
        - a kinetic term coupling neighbouring places, the general symmetric local π² term linear in N,
$$
\Omega_2(k,s)_{il}=P(k,s)_{il}+P(k,-k-s)_{li},
$$
          with U⁰'s matching change;
        - in the full form, the a² lapse couplings of both energies: δM for Regge's second-order energy, and δC for the first-order energy, with δC(k)·G(−k) = 0. Together they are an energy change E → E − Σ∂N·V(h).
      - **Both close (K89a, K89b PASS; certified by the check).** The spatial-covariance sector with {H, H} at order π closes with the dressing alone; the full kinetic sector closes with the lapse couplings too (against the registered expectation). The first-order energy's lapse coupling δC is what closes {H, H}: without it the fit stalls at 1.9×10⁻².
      - **What closure forces.** At constant lapse the closing Hamiltonian's graviton waves obey
$$
\omega^2_{TT}=s^2+O(s^5)\qquad\text{instead of Run 84's}\qquad \omega^2=s^2-\tfrac1{12}\textstyle\sum_a s_a^4+O(s^6).
$$
        The lattice's a² anisotropy is removed exactly; the dressing's forced coefficients are the ±1/24 that cancel it. With the spatial sector only, the a² dispersion is birefringent, and that form cannot keep Run 84's dispersion (post hoc).
      - **Why (the check's interpretation, not proved).** GR's algebra contains the boost relation {H[1], H[x^a]} = D[e_a]. At field order 2 it holds only for Lorentz-invariant linear dynamics, so first-class closure at a² requires an order-a² (Symanzik-type) improvement of the graviton dispersion. This ties the waves' Lorentz invariance to GR's constraint algebra, which is imposed here; it does not derive it from the primitives.
      - **Reading.**
        - GR's route survives in the kinetic sector at a², for a changed lattice Hamiltonian: a non-ultralocal kinetic term, an a² lapse coupling of the first-order energy, and a π-linear D[Y] at a². The solution is a family; only part of it is fixed, and no simple geometric identification of the dressing was found.
        - The khronometric route proper (λ > 1, with its α term in the lapse gradient) is untested; at λ = 1 the spatial sector closes with direction-dependent waves.
        - The effects are of relative order (as)², far below measurement.
      - **Not yet tested:**
        - the dispersion mechanism as a registered statement (closure ⇔ ω²_TT = s² + O(a³));
        - the potential sector at a², the decisive test for GR's route, which needs a sparse engine;
        - the khronometric route proper;
        - locality where one momentum vanishes;
        - field order 3.
- Deriving the borrowed inputs: Lorentz invariance (including twist across ticks) and inertia = total energy.
- **Whether any of the added inputs, the rules and choices adopted after the original ontology, can be derived after all,** from the primitives or from the other added inputs, so that the list of inputs shrinks (stated 24 October). More rulings are likely as the runs continue. Candidates so far:
  - the undisturbed vacuum draws nothing (R5), from the earlier added input that the vacuum never commits;
  - holes are stable (R11), from "commitments are never undone" together with a cold core (the core's state is open, §5);
  - infalling matter commits at about 2p_s (R11), from the presence clock (R2).
- Whether CO's event layer itself charges twist across ticks.
- What sources Λ. Under R5 the rules give Λ = 0, while Λ is observed to be small and positive; it is taken from data as an input.
- Whether the universe as a whole has finitely many places (the no-infinities principle, §1, read globally). If it does, space closes on itself, and searches of the CMB for repeated patterns bound how small it can be.
- Where three dimensions come from. The engine assumes them. Stated 23 October: dimension comes from how commitments relate, and the first commitments, all blinking at the same rate, together with an early inflation, set the lattice and the hop.
- Particles as knots built from the engine's own commitments.
