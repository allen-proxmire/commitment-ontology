# The ontology

The primitives and rules as they stand, with their formulas. Each rule is marked **derived**, **added** (chosen when a run raised a question the primitives did not answer) or **borrowed** (taken from established physics and tracked), and **provisional** where the grounds for going back are set in advance. The full version, with the history of each rule and what was tried and dropped, is [`record/ONTOLOGY_full.md`](record/ONTOLOGY_full.md); the order in which rules were adopted is [`record/RULINGS.md`](record/RULINGS.md).

## Primitives

| primitive | what it is |
|---|---|
| **Commitment** | one irreversible update at a place. Time at a place is the count of commitments there |
| **Place, relation** | space is who relates to whom; sliding places costs nothing |
| **Possibility** | a conserved quantity held at places, P units per place, hopping between related places. The vacuum carries no commitment |
| **Matter** | commitment that keeps re-making itself; mass is the upkeep |
| **Clock** | matter counting its own commitments. Clocks are matter |
| **Pattern** | possibility in transit between commitments: light, and quantum matter |
| **Record** | what has been committed. It is kept |

Principles added to the primitives: **the vacuum never commits**, and **no infinities** (every physical quantity is finite). Three dimensions of space are assumed.

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

**R7. Twist** (borrowed). Twist is charged on every closed loop of the history, ticks and relations priced alike. This is Lorentz invariance put in by hand; it makes a knot's inertia equal its energy. Particles are knots of commitment.

**R8. Motion and inertia.** Patterns ride the flow, g₀ᵢ = −uᵢ. A moving body's field is its boosted rest field (borrowed). Bodies move as point particles, action −m∫dτ (added). Inertia = total energy (borrowed). Relations shear, and only the shear radiates (added).

**R9. Space** (borrowed, provisional: "option 3"). Binding tension curves the medium's space in GR's form. On that space, γ̃ = N²g,
$$
ds^2=-N^2dt^2+N^{-2}\tilde\gamma_{ij}dx^idx^j,\qquad \tilde R_{ij}=2\,\partial_i\varphi\,\partial_j\varphi-16\pi\,p\,e^{2U}\tilde\gamma_{ij},\qquad N=(1+\varepsilon)e^{-\varphi}-\varepsilon .
$$
ε sets every static departure from GR. Deriving this rule from the primitives is the main open problem.

**R10. Rotation** (added, provisional). Frame dragging is possibility's own circulating flow, so the medium's clock is the zero-angular-momentum frame's lapse; spinning holes are Kerr outside.

**R11. Black holes** (added; GR's exterior for mergers borrowed). Infalling matter commits where the medium's possibility falls to 2p_s, before any causal matter can turn back; the core absorbs what reaches it, at areal radius 3m. Holes are stable.

## Quantum rules

**Q1. Patterns draw only through their records.** A pattern between commitments has no gravity of its own; it lays its draw down where it is recorded. The medium holds no branches, so gravity cannot entangle masses.

**Q2. Matter and pattern are states, not kinds.** A free body between records is a pattern. A renewal records nothing. Deposits land only where a record fixes position, at its Born outcome, as an impulse with no reaction partner, and a body's own deposits act on it.

**Q3. Route (a): records by interaction.** A pattern is recorded when committed matter keeps which-path information, with the standard coherence kernel.

**Q4. Route (b): commit and continue.** Matter also commits at random, at a rate set by its proper phase, localising with coarseness r_C:
$$
\lambda=\frac{\kappa_b\,mc^2}{\gamma\hbar},\qquad L(x)=(\pi r_C^2)^{-3/4}e^{-(q-x)^2/2r_C^2},\qquad \kappa_b=\frac{1}{aP_\infty}\ \text{(a definition)}.
$$
The rate is zero for light, which commits only through route (a). Each record deposits E/λ_tot, smeared at √1.5 r_C. Identical units are symmetrised GRW-type, and r_C is a primitive scale bounded by data.

**Q5. Two places.** A commitment of one part of a pattern updates the whole pattern at once and commits only that part. Bell's correlations are QM's, and no setting can signal. The Born rule is borrowed.

## Inputs

| input | kind | what it buys |
|---|---|---|
| R1 outflow, R2 clock | added, provisional | β = 1; redshift |
| R5 variational draw, pattern energy draws, hydrostatic balance | added | the first law, passive = active mass, the Tolman pull |
| R5 vacuum draws nothing | added | no vacuum-energy problem; Λ from data |
| R6 pattern rule | added, provisional | γ = 1; quantum matter falls as in GR |
| R8 point particles, shear of relations | added | orbits; binary-pulsar radiation |
| R10 rotation, R11 the core | added | Kerr outside spinning holes; no singularity, no evaporation |
| R7 twist, R8 Lorentz input and inertia = total energy, R9 option 3, GR's exterior for mergers, matter's masses and nuclear equations of state | borrowed | composite free fall; frame dragging; stars and holes as GR's; mergers |
| Q4 GRW-type symmetrisation; the Born rule | added; borrowed | an open quantum window; outcome weights |
| p_s ≳ 4×10⁵ per place; P∞/p_s ≳ 1.6–1.9×10⁵ | from data | clocks agreeing to 10⁻⁶; the pulsar triple |
| r_C, κ_b | bounded by data | 0.09 μm ≲ r_C ≲ 51 μm |
| G, c, ħ, Λ | measured | strengths and scales |

## Open

- How space curves, from the primitives (replacing R9).
- What fixes p_s, P∞ and ε; the hop's size (the engine needs about 10^2.5–10³ Planck lengths).
- What fixes r_C and κ_b; whether commitment depends on internal complexity; the Born rule.
- Rotation from the engine's own flow; the core's quantum state; black-hole thermodynamics without evaporation.
- Field order 3 of the relations' constraint algebra, where Regge's symmetry is expected to break.
- What sources Λ; where three dimensions come from; why the beginning starts to commit.
- Whether any added rule can be derived from the others, so the list of inputs shrinks.
