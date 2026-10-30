# The ontology

The primitives and rules as they stand, with their formulas. Each rule is marked **derived**, **added** (chosen when a run raised a question the primitives did not answer) or **borrowed** (taken from established physics and tracked), and **provisional** where the grounds for going back are set in advance. The full version, with the history of each rule and what was tried and dropped, is [`record/ONTOLOGY_full.md`](record/ONTOLOGY_full.md); the order in which rules were adopted is [`record/RULINGS.md`](record/RULINGS.md).

## Primitives

| primitive | what it is |
|---|---|
| **Commitment** | one irreversible update at a place. Time at a place is the count of commitments there |
| **Place, relation** | space is who relates to whom; sliding places costs nothing |
| **Possibility** | a conserved quantity held at places, P units per place, hopping between related places. The vacuum carries no commitment |
| **Matter** | commitment that keeps re-making itself; mass is the upkeep. Between records a body is a pattern: its renewals keep its rhythm but record nothing, and its draw on the medium is carried, on average, by its records |
| **Pattern** | possibility in transit between commitments: light, and quantum matter |
| **Record** | what has been committed. It is kept |

Principles added to the primitives: **the vacuum never commits**; **clocks are matter** (a clock is matter counting its own commitments); and **no infinities** (every physical quantity is finite). Three dimensions of space are assumed.

## Gravity rules

**R1. The medium** (added, provisional). A place holding P units sends out, on average,
$$
f(P)=c\,\ln\!\Big(1+\frac{P}{p_s}\Big),
$$
linear below the crossover p_s, comparing ratios above it. Far from matter the medium holds P∞ per place. Chosen to give β = 1.

**R2. The presence clock** (added, provisional). A commitment holds until the possibility present at its places, summed over ticks, reaches a fixed amount, so a clock runs at
$$
N=\frac{P}{P_\infty}.
$$
The hold and the clock apply where a body's records fix its state. A clock keeps time while its records fix it; between records its phase is turned by the committed world's count.

**R3. The field** (derived). Conservation makes the mean outflow z an exactly linear, unscreened field of matter's draw s:
$$
\tfrac16\sum_{y\sim x}z_y-z_x=s_x-\bar s,\qquad \beta-1=-\frac{\varepsilon}{2(1+\varepsilon)},\quad \varepsilon=\frac{p_s}{P_\infty}.
$$

**R4. The field's dynamics** (added). The clock field is fixed afresh each tick, so a moving body keeps its well; patterns ride possibility's flow; the engine's tick is not physical time.

**R5. What draws** (added). Every source draws by its redshifted Tolman weight, times a factor that makes the theory variational:
$$
d=T\,(1+g),\qquad T=(e+3p)\,N\sqrt\gamma,\qquad g\approx\frac{p_s}{P}.
$$
A pattern's energy draws; stress pulls with weight 1 per direction (borrowed, the Lorentz input); a body is in exact hydrostatic balance, N h(n) = μ̃. **The undisturbed vacuum draws nothing**: energy is measured from it, so quantum field theory's vacuum energy never enters gravity, and Λ is taken from data.

**R6. The pattern rule** (added, provisional). A pattern hops on its place's ticks and needs free capacity there, so light's coordinate speed is N² and γ = 1. Massive patterns obey
$$
-N^4\nabla^2\psi+m^2N^2\psi=\omega^2\psi .
$$

**R7. Twist** (borrowed, provisional). Twist is charged on every closed loop of the history, ticks and relations priced alike. This is Lorentz invariance put in by hand; it makes a knot's inertia equal its energy. Particles are knots of commitment when twist lives on closed loops of relations that tile space as faces; building knots from the engine's own commitments is open.

**R8. Motion and inertia.** Patterns ride the flow, g₀ᵢ = −uᵢ. A moving body's field is its boosted rest field (borrowed; exact, since ε = 0 in gravity, ruled 30 October after T-I15d). Bodies move as point particles, action −m∫dτ (added). Inertia = total energy (borrowed). Relations shear, and only the shear radiates (added).

**R9. Space** (borrowed, provisional: "option 3"). Binding tension curves the medium's space in GR's form. On that space, γ̃ = N²g,
$$
ds^2=-N^2dt^2+N^{-2}\tilde\gamma_{ij}dx^idx^j,\qquad \tilde R_{ij}=2\,\partial_i\varphi\,\partial_j\varphi-16\pi\,p\,e^{2U}\tilde\gamma_{ij},\qquad N=(1+\varepsilon)e^{-\varphi}-\varepsilon .
$$
That φ's stress, not U's, curves γ̃ is an added choice: with U's, β = 1 exactly. ε sets every static departure from GR. Deriving this rule from the primitives is the main open problem.

**R10. Rotation** (added, provisional). Frame dragging is possibility's own circulating flow, so the medium's clock is the zero-angular-momentum frame's lapse; spinning holes are Kerr outside (exactly, with ε = 0 in gravity). This interprets an input; the rules do not imply it.

**R11. Black holes** (added; GR's exterior for mergers borrowed; re-ruled 30 October, Reading I17). With ε = 0 in gravity, holes are GR's: a horizon, Hawking evaporation. Infalling matter's commitment relabels it as a record and does not hold it; possibility runs out at r = 2m, and the 2p_s surface sits about 8mε_med² outside it (ε_med = p_s/P∞, a medium quantity). The earlier core at 3m, the throat and horn, and "no horizon, no evaporation" are withdrawn.

**ε in gravity is zero** (ruled 30 October, after T-I15d). The medium's scale does not enter the metric: outside matter it is GR's, and the medium is read as a slicing condition. CO's preferred-time completions bound ε ≲ 10⁻⁹ (α₂, pulsars) and 1.3×10⁻⁷ (GW170817), where its gravity departures are unobservable. p_s and P∞ keep their roles in clocks and the quantum sector. R9's choice of φ's stress becomes empty (φ = U), and R11's statements are to be re-read under this.

## Quantum rules

All added unless marked. Route (b)'s rate is κ_b M̂c²/ħ per unit proper time, an operator, so each branch commits at its own rate.

**Q1. Patterns draw only through their records.** A pattern between commitments has no gravity of its own; it lays its draw down where it is recorded. A commitment's stamp and place are those its record fixes: the local count where it happens. A renewal carries no stamp. The medium holds no branches, and a pattern's phase is turned by the time-averaged count; together these make gravity unable to entangle masses.

**Q2. Matter and pattern are states, not kinds.** A free body between records is a pattern. A renewal records nothing. Deposits land only where a record fixes position, at its Born outcome, as an impulse with no reaction partner, and a body's own deposits act on it.

**Q3. Route (a): records by interaction.** A pattern is recorded when committed matter keeps which-path information, with the standard coherence kernel. Interstellar gas is committed matter, so its collisions are route-(a) records.

**Q4. Route (b): commit and continue.** Matter also commits at random, at a rate set by its proper phase, localising with coarseness r_C:
$$
\lambda=\frac{\kappa_b\,mc^2}{\gamma\hbar},\qquad L(x)=(\pi r_C^2)^{-3/4}e^{-(q-x)^2/2r_C^2},\qquad \kappa_b=\frac{1}{aP_\infty}\ \text{(a definition)}.
$$
The rate is zero for light, which commits only through route (a). Every massive pattern commits this way, relic neutrinos included; the units of ordinary matter are electrons and nucleons, each committing on its own. Each record deposits E_TK/λ_tot, smeared at √1.5 r_C. Identical units are symmetrised GRW-type. κ_b = 1/(aP∞) is a definition, and r_C, one for every species, is a primitive input bounded by data.

**Q5. Two places.** A commitment of one part of a pattern updates the whole pattern at once and commits only that part. Bell's correlations are QM's, and no setting can signal. Two-part patterns come from ordinary entangling evolution, so the singlet is an input. Born weights follow from Q6.

**Q6. Noncontextual reading** (ruled 30 October, Reading I16). A record's chance for an outcome with effect E is F(⟨ψ|E|ψ⟩), one F for every record. With one outcome per record and A5's √P amplitudes, F(w₁) + F(w₂) = F(w₁ + w₂), so Pr(E) = ⟨ψ|E|ψ⟩: the Born rule. Route (c)'s unravelling constant c is a fixed field, not read from the state. A restatement of Logiurato–Smerzi; it predicts nothing new.

## Inputs

| input | kind | what it buys |
|---|---|---|
| R1 outflow, R2 clock | added, provisional | β = 1; redshift |
| R4 the clock field fixed each tick | added | a moving body keeps its well; no preferred frame from the flow |
| R5 variational draw, pattern energy draws, hydrostatic balance | added | the first law, passive = active mass (the Tolman pull is derived) |
| R5 vacuum draws nothing | added | no vacuum-energy problem; Λ from data |
| R6 pattern rule | added, provisional | γ = 1; quantum matter falls as in GR |
| R8 point particles, shear of relations | added | orbits; binary-pulsar radiation |
| R9 φ's stress curves space | added | β − 1 = −ε/[2(1 + ε)] |
| R10 rotation (provisional), R11 commitment in holes | added | Kerr outside spinning holes; holes as GR's (Reading I17) |
| R7 twist (provisional), R8 Lorentz input and inertia = total energy, R9 option 3, GR's exterior for mergers, the boost relation and GR's constraint algebra (Runs 85–91, 101–102), matter's masses and nuclear equations of state | borrowed | composite free fall; frame dragging; stars and holes as GR's; mergers |
| Q1–Q5 the quantum rules | added | gravity only from records; the quantum window |
| Q6 noncontextual reading | added | the Born weights |
| Q4 GRW-type symmetrisation | added | an open window (without it, it closes) |
| amplitudes √P with phases; the singlet | borrowed; input | the state structure; entangled pairs |
| P∞/p_s: no longer bounded by gravity (ε = 0 in gravity, 30 October); the earlier bounds (pulsar triple ≳ 1.6×10⁵; with a preferred time ≳ 4×10⁵, 7.7×10⁶, 1.25×10⁹) are what forced it | — | — |
| p_s ≳ 4×10⁵ per place; the hop (P∞ ≳ 6.4×10¹⁰ was p_s's bound times the pulsar-triple ratio and lapsed with ε = 0 in gravity, 30 October) | from data and the engine; conditional since Reading I6 (physical clocks do not dip themselves). No upper bound on p_s from gravity (Reading I11's p_s ≲ 1.1×10³⁰/a rested on the pulsar-triple ratio and lapsed, 30 October); route (b) gives a·P∞ ≳ 2.5–5×10²⁷ | clocks agreeing to 10⁻⁶ |
| r_C, κ_b | bounded by data | 0.09 μm ≲ r_C ≲ 51 μm |
| G, c, ħ, Λ | measured | strengths and scales |

## Open

- How space curves, from the primitives (replacing R9).
- What fixes p_s, P∞ and ε; whether ε has a covariant form (Reading I15a: at weak field it needs a ghost, an unusual scalar sector or a TeVeS-type coupling; a cuscuton-type form is being tested, T-I15c); the hop's size (the engine needs about 10^2.5–10³ Planck lengths).
- What fixes r_C and κ_b; whether commitment depends on internal complexity; whether one-way commitment forces Q6 (Reading I16: it does not, as the record stands).
- Rotation from the engine's own flow; the core's quantum state; what commitment does in a collapse (Reading I17: a registered collapse under maximal slicing).
- Field order 3 of the relations' constraint algebra, where Regge's symmetry is expected to break.
- What sources Λ; where three dimensions come from; why the beginning starts to commit.
- Whether any added rule can be derived from the others, so the list of inputs shrinks.
