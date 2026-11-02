# CO 2.0

A restart from the primitives. Nothing from [`CO_1.0_misdefined-primitives/ONTOLOGY.md`](CO_1.0_misdefined-primitives/ONTOLOGY.md) is assumed; what is kept is re-derived or re-ruled here. No runs. Conversation only, until the rulings settle.

**Method.** A rule is added only where the primitives are silent, and only if it retires at least one thing previously added by hand. A rule may also be added when the ruled set contradicts itself or the world, with the contradiction named. A rule whose prerequisites are not yet ruled stays **candidate**.

## Primitives

| primitive | what it is |
|---|---|
| **Possibility** | the conserved stuff |
| **Commitment** | one irreversible act on it |

**Renewal.** A commitment, on completing, engages adjacent free possibility into its next commitment, releases what the last one held, and adds one to its count. Any commitment does this if free possibility is adjacent to engage; it halts when none is. Nothing more is needed (ruled; the alternatives, a predecessor required or a probability, leave the beginning without matter or add a number).

## Consequences, not primitives

| term | what it is |
|---|---|
| **Matter** | a commitment that keeps being fed. Not a kind of thing but a commitment's condition; the same commitment, starved, is a record. Mass is renewal frequency |
| **Time** | matter's count. Read only by ratio: N_A / N_B. Nothing says "what time it is" |
| **Record** | a commitment matter carries forward by renewing. Kept by being renewed; nothing else keeps anything |
| **Pattern** | possibility between commitments |
| **Place, relation** | the adjacency along which possibility moves. No claim that space comes from it |

**Space:** one candidate, forced by a contradiction (see Gathering and space).

## Rulings

| ruling | statement |
|---|---|
| vacuum | possibility with no commitment. Timeless and scaleless by construction: zero commitments, zero count. Flow is undefined there; it becomes a fact only against matter's count |
| hold-and-release | a renewal engages possibility, completes, releases it. Nothing is consumed. P_free = P(1 − h), h the fraction engaged |
| (B) one quantum per renewal | every renewal engages the same amount, ħ. Mass is renewal frequency: ω = mc²/ħ. The first scale is an action, and it arrives with the first renewal |
| g linear | renewal rate = (m/ħ)(1 − h). h = 1 is the hole: everything local engaged, nothing free, renewal starves and matter becomes record. A ceiling approached, not a point reached; with pooling as a share of what is there, both renewal and retention vanish together as P_free → 0 |
| gravity | possibility moves toward where it is being engaged; that inflow is what sets h around matter. Patterns fall by **refraction**: a pattern hops on its place's ticks, ticks are slower where h is higher, so a pattern's wavefront turns toward matter. For a matter wave with ω = mc²/ħ this gives g = −c²∇h exactly, mass-independent: Newton. (Earlier wording, "patterns ride possibility," is withdrawn as the mechanism: the inflow's drift speed falls as 1/r² and is suppressed by the hop length, so it cannot give Newton's 1/r² acceleration. The flow sets the field; refraction moves the pattern) |
| inertia | possibility in transit keeps its direction until a commitment redirects it; refraction on the clock-rate field bends it on the way. A pattern between commitments goes on as it was going. Free fall is inertia plus refraction. Retires 1.0's borrowed inertia |
| relations carry an occupancy | a relation carries one number, symmetric in direction: how much possibility is spoken for in transit across it. The length of a route is the product of (1 + occupancy) along it; at rest the occupancies are set by the places and the route factor is P∞/P_free = e^{U}. Away from rest a relation can be out of step with its ends. (This replaces "relations carry a ratio": a ratio is antisymmetric, R_ji = 1/R_ij, a 1-form, and a 1-form's waves are spin-1, Maxwell's, not gravity's; see Derivation) | **ruled** (forced by radiation; a ratio cannot carry spin-2; the slide check below passes) |
| sliding costs nothing | relabelling or sliding places changes nothing physical; the cost of relations being out of step depends only on how they fit together, not on any backdrop. 1.0's "sliding places costs nothing", now with its job: it is the symmetry that fixes the cost | **ruled** (it is the first primitive's content: space is who relates to whom, nothing else) |
| ratio hopping | the substrate is scaleless, so a hop compares neighbours by ratio, never by difference; the field is linear in ln P_free, N = e^{−U} | **ruled** (forced by scalelessness; Mercury excludes difference hopping) |

**Why (B).** The alternative, universal rate with varying engagement, cannot give universal redshift without an extra assumption, and gives E = ħω no reading. (B) gives both:

$$\frac{N_A}{N_B}=\frac{1-h_A}{1-h_B},\qquad h\propto\sum_i m_i\ \text{over adjacent matter}.$$

The quantity that slows clocks and the quantity that gravitates are the same, counted the same way.

**Clock mechanism vs clock reading.** A clock's mechanism references the possibility around it; a clock's reading references another clock. Neither needs a background tick.

**Perihelion, and the exterior.** The precession per orbit is (6πGM/c²a(1 − e²))·(2 + 2γ − β)/3; γ = 1 is in hand, and Mercury fixes β = 1 to a part in a thousand. The difference-linear field (P_free = P∞ − k/r) gives N = 1 − U with no second-order term, N² = 1 − 2U + U², β = ½: Mercury at 7/6 of GR, excluded. What fixes it was ruled first: the substrate is scaleless, so a hop can compare neighbours only by ratio, P_j/P_i, never by difference. Ratio hopping equalises ln P, and the steady field is

$$\nabla^2\ln P_{\text{free}}=\sigma\,\delta(\mathbf r)\ \Rightarrow\ N=\frac{P_{\text{free}}}{P_\infty}=e^{-U}=1-U+\tfrac{U^2}{2}+\dots,$$

so N² = 1 − 2U + 2U², β = 1, and the route factor P∞/P_free = e^{U} keeps γ = 1. Newton, bending and the Shapiro delay are unchanged; Mercury is right. **Ruled:** hops compare by ratio (forced by scalelessness; Mercury excludes the alternative). The exterior is then the exponential metric,

$$ds^2=-e^{-2U}c^2dt^2+e^{2U}d\mathbf x^2 ,$$

γ = β = 1, no horizon (N → 0 only as r → 0): the hole as a ceiling approached, with its metric. This is what 1.0 borrowed as R9. **Kill test (R3, [`CO_2.0_runs/R3_strong_field/`](CO_2.0_runs/R3_strong_field/R3_result.md)):** the exponential metric departs from Kerr in the strong field. Photon sphere at ρ = 2M; shadow radius 2eM against 3√3M, **4.6% larger**; ISCO frequency **7% lower**. EHT: M87* δ = −0.01 ± 0.17, Sgr A* about −0.08 ± 0.09; not excluded, about 1σ on Sgr A*, and the departure is the size of Kerr's own spin dependence. Next-generation EHT at a few percent tests it. The first place 2.0 says GR is wrong rather than reproduced, with a sign: shadows slightly larger, ISCO frequencies slightly lower. Ringdown not computed.

**Gravitational radiation.** What 2.0 has is one field, h, with inertia for possibility in transit, so the dynamical field equation is a scalar wave equation, □ ln P_free = σ. That radiates, at the hop speed, and conservation kills the monopole and dipole terms, leaving the quadrupole. But a scalar quadrupole is not GR's:

$$P_{\text{scalar}}=\frac{G}{60c^5}\Big[(\dddot Q_{ii})^2+2\,\dddot Q_{ij}\dddot Q_{ij}\Big],\qquad P_{\text{GR}}=\frac{G}{5c^5}\Big[\dddot Q_{ij}\dddot Q_{ij}-\tfrac13(\dddot Q_{ii})^2\Big],$$

and for a circular binary (trace constant) the ratio is **1/6**. The Hulse–Taylor decay is GR's to 0.3%. Excluded. Independently, a scalar ripple is a breathing mode, and LIGO–Virgo polarization tests favour tensor over pure scalar by large factors. Excluded twice. **Result:** gravitational waves are not ripples in free possibility. They must be ripples in the routes themselves, transverse and traceless, which needs the adjacency to carry dynamics of its own. 2.0 says nothing about that; it is the geometry question, now with a measured number attached. Statics (R3 and the classical tests) are untouched: they depend on h alone.

**Derivation: what a relation must carry, and what its mismatch costs.**

1. *A ratio will not do.* Write ℓ_ij = ln R_ij. A ratio reverses with direction, ℓ_ji = −ℓ_ij: a 1-form on the network. With rest value ℓ = dφ (φ = ln P), the mismatch m = ℓ − dφ splits into a gradient part and a loop part. Ratio hopping with inertia gives, linearised,
 $$\ddot m=-\beta\nu P\,m-\nu\,d(\operatorname{div}m),$$
 so the gradient part is the scalar sound of possibility (the □ ln P wave already excluded for radiation) and the loop part oscillates in place without propagating. Coupling neighbouring loops gives at best a curl-of-curl theory: Maxwell's, spin-1. A loop product ≠ 1 is a holonomy, not a curvature. Vector waves are excluded by LIGO–Virgo polarization and give dipole, not quadrupole, radiation. So the relation's number must be **symmetric** in direction: an occupancy, a length. Lengths along the directions a place has determine a quadratic form per cell, g_ij, and that is spin-2's home. (The 1-form structure is not wasted: a ratio on relations is the shape of a gauge field, and is left as a candidate home for charge. Not pursued.)

2. *The cost is fixed by sliding.* With occupancies as edge lengths, a cell's lengths that cannot be laid out flat have a deficit: discrete curvature. The cost of mismatch must be a function of the occupancies alone that does not change when places are relabelled or slid, because there is no backdrop against which sliding could cost. In the continuum that symmetry is diffeomorphism invariance, and Lovelock's theorem (borrowed mathematics, as Dilworth was) says the only local, second-order, slide-invariant cost in three space dimensions plus time is

 $$S=\frac{1}{16\pi G}\int (R-2\Lambda)\sqrt{-g}\,d^4x ,$$

 Einstein–Hilbert with a constant. On the network its discrete form is Regge's deficit-angle action. There is no other choice, so the cost is not a reading.

3. *What follows.* Regge's action reproduces linearised GR: tensor waves, two polarizations in three dimensions, the quadrupole formula with GR's coefficient. **Hulse–Taylor is met** (0.3%); the polarization tests are met. G is the stiffness of the relations against mismatch, already fixed by the statics (G ∝ δ/P_max). Λ is the one constant the symmetry allows and does not fix: it was an input and it stays one, now with its place named.

4. *The slide check.* The hop rule on occupancies: a hop across a relation is driven by the ratio of its ends and slowed by the relation's length, rate ∝ (P_j/P_i − 1)/ℓ_ij. That is a conductance network with conductance 1/ℓ. It refers to nothing but the places' P and the relations' ℓ, so relabelling is exact invariance. Sliding a place along a chain, ℓ₁ + ℓ₂ fixed, leaves the series conductance 1/(ℓ₁ + ℓ₂) unchanged: exact. Sliding a place inside a cell changes several lengths at once, and the discrete rule is invariant only to the order at which the network approximates its continuum, where ratio hopping becomes the metric Laplacian ∇²_g ln P, which is diffeomorphism-invariant exactly. This is the same level of invariance Regge's own action has under vertex displacement. So the hop rule is slide-invariant to the order the whole framework holds, and the cost follows. **Occupancy: ruled.**

5. *What is not derived.* That the network's continuum limit is three-dimensional (Lovelock's uniqueness is dimension-dependent; in two dimensions the action is trivial, in five there is a second term). The polarization count, two, is therefore a statement about the adjacency 2.0 has not yet earned; it is the handle on dimension. And the step from "ratio hopping on occupancies" to "the deficit-angle cost" is made by the symmetry, not by the hop rule; whether the hop rule is itself slide-invariant is the check that closes it.

**Consequence for the wave rule.** "Wave crests tip edge places" took a gravitational wave to be a surplus of free possibility. If waves are route ripples, there is no surplus to tip, and the births-by-wave candidate, and the Λ term with it, lose their mechanism. They stand only if route ripples also move free possibility, which nothing yet says. Marked accordingly below.

**Light bending.** A pattern crossing a region of engaged fraction h has its ticks slowed by (1 − h) and, under "route lengthens", its path stretched by (1 + h). Its coordinate speed is

$$c(h)=c\,\frac{1-h}{1+h}\approx c\,(1-2h),\qquad n\approx 1+2h ,$$

with h = GM/(c²r) outside a body. Fermat's principle on that index gives a deflection of 4GM/(c²b), twice Newton's, and the Shapiro delay, both as measured. Slow massive patterns feel only the tick half (Newton, g = −c²∇h); light, moving at the hop speed, feels both halves. This is the isotropic weak-field metric of GR, N² = 1 − 2U and spatial factor 1 + 2U, read as "one h, counted twice." With the tick half alone the bending is half GR's: the route half is what 1.0 borrowed as R9 and 2.0 states as a reading.

## The balance

Strict local hold-and-release gives no field outside matter: a renewal engages at its adjacency and releases at the same adjacency, net zero per cycle. A clock a metre above the ground would run at full rate. So matter must be a **net sink** of free possibility. A steady point sink into a conserved, diffusing stock gives

$$\nabla^2 P_{\text{free}}=\sigma\,\delta(\mathbf r)\ \Rightarrow\ P_{\text{free}}(r)=P_\infty-\frac{k}{r},\qquad k\propto\sigma ,$$

Newton's potential, linear and unscreened, from conservation alone. The question is what makes matter a sink. (At second order the difference-linear form fails; see Perihelion. The field is linear in ln P_free, which agrees at first order.)

| option | statement | status |
|---|---|---|
| **pooling** | a renewal releases a fraction (1 − δ) of what it engaged; the rest stays engaged. The body's engaged stock grows, free possibility is drawn in to meet the deficit, and that draw is the field. The hole is where pooling finishes: h → 1 | **ruled** |
| circulation | engage from the near side, release to the far side, through a channel patterns do not ride | candidate |
| nothing | strict local release, no net sink | excluded: no field outside matter |

**Pooling, in one sentence.** A renewal keeps a share of what is there: it retains δħ·(P_free/P_max) as the body's record and releases the rest. (Ruled in this form; the earlier form, a fixed δħ, is superseded. See Today's expansion for why.)

**The retained fraction is the record.** Of the three readings of "the rest," *destroyed* breaks conservation and leaves no ceiling (the engaged stock would not grow, so h could not reach 1); *leaves* is circulation under another name. *Stays engaged* keeps both, and says what a record is made of: possibility withdrawn from the free stock and held. "It is kept" means "it is still engaged." The hole is a body that is all record and no renewal. The count rising and the free stock falling are one process; the record only grows because δ > 0 (void record may become space; see Today's expansion; it never returns to free).

**What pooling costs.** δ is 2.0's first constant that is not ħ and not borrowed, the same for every renewal. Sink strength is

$$\sigma=\delta\,mc^2\,\frac{P_{\text{free}}}{P_{\max}} ,$$

so in the weak field G ∝ δ/P_max, with no dependence on the floor P∞. In the strong field a body's sink is screened by its own depletion, (1 − h_self); linear and unscreened to first order, different from GR beyond it, untested.

**The vacuum far away.** Conservation gives

$$\dot P_{\text{free}}=-\dot P_{\text{engaged}}=-\delta\sum_i m_ic^2 .$$

- A uniform fall in P∞ makes no gradient: no force, and **not Λ**. Λ is not sourced by the floor.
- With pooling as a share of what is there, the deficit around a body scales with the floor, so h(r) = (k/r)/P∞ does not depend on P∞. **G is constant.** The floor is unobservable: neither pooling nor any dilution of free possibility shows in G or in clock ratios. (The earlier form of pooling gave Ġ/G = −Ṗ∞/P∞ > 0 and a window on δ from Ġ/G bounds; that result is retired with it, and δ is no longer bounded by data.)
- With no infinities the free stock is finite, so the record has a finite capacity and the process has an end: everything engaged.

**Second leg.** "Possibility moves toward engagement" is a flow statement and needs the sink. If the sink failed, attraction would still follow from a static gradient: patterns hop on free possibility, hop slower where it is scarce, and so linger near matter. Not needed under pooling; noted.

## The beginning

At the start everything is free: no matter, no renewal, no count. Under the rulings above that state is stable; nothing makes free possibility commit. The first commitment cannot be a renewal.

| option | statement | status |
|---|---|---|
| threshold | an adjacency holds at most P_max of free possibility; above that it commits. Retires "the vacuum never commits" (today P∞ < P_max); the start commits everywhere at once; the first epoch ends when P_free ≤ P_max everywhere, so P∞ ≲ P_max today | **ruled** |
| steep rate | r = r₀(P_free/P*)ⁿ with n chosen large | set aside: an exponent nothing fixes |
| boundary condition | the record has a first line; CO does not ask why | superseded by the threshold |

**Prerequisites for the threshold.** Both met.
- ~~Does a bare commitment renew?~~ Ruled: yes, if fed (see Renewal). The beginning makes matter at once, everywhere.
- ~~What lowers P_free to P_max?~~ Ruled: pooling. Every renewal retains δħ as record; P_free falls until it reaches P_max and new commitments stop. What remains is a uniform primordial record,
 $$h_0 = 1-\frac{P_{\max}}{P_0},$$
 P₀ the free possibility per adjacency at the start. Uniform h is unobservable (every clock slowed alike; only ratios are read); its one trace is P∞ ≲ P_max today. The alternative, more adjacencies (space grows), was not taken: it needs a rule about space, and nothing forces one.

**What the beginning leaves.** Fed matter at every adjacency, and a uniform record. Today matter is sparse.

## Gathering and space

Gathering (possibility toward engagement, patterns following) amplifies unevenness and creates none. Even matter stays even. A slightly denser spot engages more, draws more, grows: a runaway on

$$t\sim\frac{1}{\sqrt{G\rho}} .$$

In fixed adjacency with no dilution the runaway does not stop at clumps; everything falls into everything, fast at the start's density. **Contradiction:** the ruled set with no space rule gives a universe of holes. Gathering needs seeds and a brake.

| rule | statement | status |
|---|---|---|
| new relations | released possibility that finds no room opens a new relation | candidate |

**What it gives.** While places are over capacity, every renewal releases possibility with nowhere to go, so relations open at the renewal rate of all matter: rapid dilution. It stops by itself when places drop under capacity. Fast growth with a built-in end, started and ended by P_max: inflation with a graceful exit. Seeds: places tip the threshold one by one, not at one instant; the unevenness is spread by the growth. Afterward, gathering.

**What it owes.**
- Today's expansion. Under this rule space grows only over capacity; today is under. See below.
- Geometry. The rule opens a relation; it does not say to where. Dimension and the shape of adjacency are untouched.

## Today's expansion

Space is route count: distance is hops, dimension is how the neighbourhood grows with hops. Two things change the hop distance between galaxies: matter moving, and new places between old ones. A new *relation* is a shortcut and shrinks distance; only new *places* expand space.

**Expansion is recession, braked, plus births.** (This replaces an earlier reading in which expansion was births alone; R2 showed births give only a Λ-like term, and the decelerating eras were missing.) During the first epoch possibility poured from over-capacity places into newborn ones, an outward flow, and matter rode it. When births stopped the flow stopped, but by inertia the matter kept receding. Gathering brakes it. For a uniform cloud of density ρ, Newton (derived above) on a shell of radius a gives

$$\ddot a=-\frac{4\pi G}{3}\rho\,a\quad\Rightarrow\quad H^2=\frac{8\pi G}{3}\rho-\frac{k}{a^2},$$

Friedmann's equation and the matter era, H ∝ a^{−3/2}, with nothing borrowed. Births in the voids (below) add a flat term: Λ.

| rule | statement | status |
|---|---|---|
| transit draws | possibility in transit is not free; a pattern's transit draws as its renewal would, in proportion to its frequency ħω. What draws is frequency, renewing or in transit | **ruled** |

With it, radiation draws by its energy; frequency falls as 1/a and number as a⁻³, so ρ_rad ∝ a⁻⁴, and the same shell argument gives H ∝ a⁻², the radiation era. The ρ + 3p of the deceleration equation follows by differentiating H² with ρ ∝ a⁻⁴; it is bookkeeping, not a borrowed weight. Owed: why a non-renewing pattern draws by its frequency (a reading, not a derivation); and light's bending at twice Newton (γ = 1), which is about how light rides, not how it draws, and is untouched.

| rule | statement | status |
|---|---|---|
| places are born | a place is born by its first commitment. A pattern that commits mid-transit makes a new place where it commits | candidate |
| born of record | a wave crest tips a near-full place; the place is born and filled from void record, not from the free stock, so the floor does not fall as places are born. Only void record converts: near matter, places are depleted, not near-full, so no crest tips them and matter's record, the hole's included, stays put. Free possibility never returns | **ruled** (forced by R1) |

**What it gives.**
- Where: inside bound systems patterns commit at matter at once, so no new places; bound things do not expand. Across voids there is nothing to commit at, so that is where places are born. Voids grow.
- The hole is untouched: nothing here turns record into anything.
- The edge: space is made wherever there is transit and no matter: the voids and the horizon.

**The wall, and the door.** A newborn place holds about ħ of free possibility against a floor of P∞; free possibility flows in and the floor falls everywhere at about the expansion rate. Under pooling as a fixed δħ this gave Ġ/G ≈ H₀ ≈ 7×10⁻¹¹ yr⁻¹ against a bound near 10⁻¹³ yr⁻¹: excluded by about 10³. The one door is pooling as a share of what is there, δħ·(P_free/P_max), which makes the floor unobservable (see The vacuum far away). Checked against the ruled set: conservation, (B), g linear, universal redshift and free fall, Newton in the weak field, the primordial record and the beginning are unchanged; the hole's approach slows; the strong field gains self-screening; the Ġ/G result is retired. Nothing ruled breaks. The door is taken.

**The third way to commit.** Patterns commit at matter, or by the threshold. Voids have no matter and are under capacity, so a mid-transit commitment needs a third way. It carries the number: births per time is the expansion rate.

| third way | statement | status |
|---|---|---|
| wave crests tip edge places | a gravitational wave is a ripple in free possibility (a massless pattern). Voids sit just under capacity, P∞ ≲ P_max. A crest larger than the gap P_max − P∞ pushes a place over capacity, and over capacity a place commits. The threshold, already ruled, does the work | candidate; with the free stock conserved, **excluded** by R1; survives only with "born of record"; and its premise, that a gravitational wave is a surplus of free possibility, is **undercut** by the radiation result (waves are route ripples). Stands only if route ripples move free possibility |
| massive patterns commit at a rate | λ = ε mc²/ħ per pattern between commitments; ε a new constant. Births ∝ mass in transit: constant, so a falling Hubble rate | set aside: a constant nothing fixes, and no acceleration. A massive pattern arriving at an edge place tips it anyway, without ε |
| light commits spontaneously | | excluded: distant sources are not dimmed, the CMB is a blackbody |
| free possibility commits on its own | births ∝ free stock ∝ places: Λ | excluded: the vacuum commits, against the threshold |

**What the wave rule gives.** A background of waves fills space, so every place has a chance per time of a crest clearing the gap: births ∝ places, exponential growth, which is what Λ describes. The vacuum never commits on its own; it commits only when pushed over the line. The gap widens slowly as births dilute the floor, so the rate per place decays slowly: in Λ language, w just above −1, drifting. (A pattern-based rate alone gives no acceleration: births ∝ patterns in transit, which is constant; a longer crossing gives more chances per pattern and fewer crossings per time, and the two cancel.)

**Kill tests.**
- Wave attenuation. A crest that tips a place commits part of itself there, so waves lose amplitude crossing voids. GW170817's wave distance matched its light to about 10%, and amplitudes match GR; the per-crest tipping probability must be tiny.
- Light must pass. A photon carries ħ; if the gap were under ħ, light would commit in voids. So the gap exceeds ħ, and a crest must move more than ħ per place. A crest's displacement per place is of order strain × P∞, with strains near 10⁻²¹, so roughly P∞/ħ ≳ 10²¹: a bound on P_max. The strain-to-possibility mapping is rough; the shape of the argument is not.

**Why now.** Standard cosmology has a "why now" problem: dark energy takes over at roughly the era structure finishes forming, and nothing in ΛCDM says why those should coincide. Here they would have to coincide if the thing that makes space late in the game is the wave background and the wave background is made by structure: acceleration begins when mergers begin. **Withdrawn by R2:** on the rms reading the astrophysical background is ~10⁹ below the primordial, so mergers do not set the late crest. It returns only with a per-place crest definition that weights short wavelengths, which needs the hop scale.

**The gap's history (sketch).** With Δ = P_max − P∞, and possibility in units of ħ,

$$P_\infty=\frac{P_{\text{free,total}}}{N},\qquad \frac{dN}{dt}=N\,r_b,\qquad H=r_b=\nu\,\Pr(\text{crest}>\Delta),$$

ν the crest rate per place and the probability set by the wave amplitude A(t). Expansion is a race between crest size and gap size. Epochs: fast births right after the first epoch (Δ ≈ 0⁺, primordial ripples), slowing as the gap opens and the ripples fade; births return when structure forms and mergers make new waves; late, a settled rate. Constraints already on it: the gap exceeds ħ by recombination (light passes; the CMB is a blackbody); per-crest tipping is rare (waves survive); P∞ ≥ ħ always (matter keeps renewing), so expansion ends before that. A curve needs A(t), ν and the tail shape, and P_max.

**R1 ([`CO_2.0_runs/R1_gap_history/`](CO_2.0_runs/R1_gap_history/R1_result.md)).** With the free stock conserved, every birth lowers the floor and shrinks crests with it; H falls as about a⁻⁹ and expansion stops. The rule as written is excluded as today's expansion. It survives if newborn places are born at the floor with content drawn from record. Under that, H(a) ∝ A(a)³, A the wave amplitude per place: the expansion history is the cube of the wave-background history. A test against real inputs, not run.

**The arrow, restated.** Record grows or becomes space; it never returns to free. The one-way quantity is record plus space; free possibility only falls. What has happened and the room it happens in are one stock in two forms.

**R2 ([`CO_2.0_runs/R2_H_vs_A3/`](CO_2.0_runs/R2_H_vs_A3/R2_result.md)).** H ∝ A³ against the measured history. No real wave background has the required shape: the radiation and matter eras need A falling as a^{−2/3} then a^{−1/2}; primordial rms is flat, a single mode falls as a^{−1}, the astrophysical background rises. **As the sole driver of expansion the wave rule is excluded.** It fits only the late era: a flat primordial crest gives H ≈ constant, matching ΛCDM at z < 1 to about 30%. The mechanism can play Λ; it cannot play the decelerating eras.

**What it owes.**
- A per-place crest definition tied to the hop scale, without which "why now" cannot be evaluated.
- Matterless record in voids: newborn places carry a speck of record and no matter. Record gravitates. Not identified with anything; dark matter sits in halos, not voids.
- Geometry, as before.

## Open

- **The masses.** What sets each pattern's renewal frequency.
- **Relations.** Whether the hop rule on occupancies is itself slide-invariant (then the Regge cost follows with nothing further); and the dimension of the adjacency, which the polarization count fixes at three.
- **Charge.** A ratio on relations is a gauge field's shape. Not pursued.
- **Space.** The per-place crest definition; geometry beyond the above.
- **δ.** Its value, and whether it is one number for every renewal. No longer bounded by Ġ/G.
- **P_max.** Its value; roughly P_max/ħ ≳ 10²¹ if the wave rule holds.
