# Matter (working record)

*Working record; formerly CO 2.1.*

**Corrections after outside reading, 2026-11-04.**
- *Q1's "geometric ratio" was inverted.* (√3/6)/(1/4) = 1.155, not 0.866, and the post-run check's "computed independently and matches" was false. A smooth field gives hexagon/square ≈ 1.06–1.15 on these loops; the measured 0.87 is below that, so squares carry more circulation per edge than a smooth vortex would. The qualitative finding (no hexagonal dominance; the chair is not the orbit) stands; the "smooth vortex" reading does not. Corrected in the result note.
- *The hop length had two values.* The top-quark bound, ℓ ≲ 1.1×10⁻¹⁸ m, is the one that stands; the δ ≈ 10⁻³⁷ estimate used 10⁻¹⁶ m and is replaced by δ ≈ 10⁻³² at the top-quark hop. The relation ℓ = ℓ_P√(4πP_max/δ) defines δ in terms of ℓ; it removes no unknown, it renames one, and δ has no observational handle.
- *Wrong theorem for amplitudes.* Lamperti's isometry does not do the job; the derivation of complex amplitudes from associativity and scaling is Goyal, Knuth and Skilling (2010). The premises as stated (a zero-mean cross term scaling as √(p₁p₂)) already carry the √ structure, so "forced, not assumed" overstates; the honest status is "forced given those premises."
- *"g = 2 follows from Dirac"* requires the minimal coupling of a charge to the which-way field, which is candidate. g = 2 is conditional on it.
- *"Born for free"* is the identification of the committing stuff with the conserved stuff; a reader may fairly call it the Born postulate restated, and the doc should not call it a derivation.

Continues from [`SPACE_AND_GRAVITY_record.md`](SPACE_AND_GRAVITY_record.md), which stops where the two primitives stop forcing. Matter opens with the first addition to the inventory. Same method: a rule is added only where the primitives are silent and only if it retires something; a rule whose prerequisites are not ruled stays candidate.

## The one question

What structure inside a commitment gives both the count of particle kinds and the quantum sector.

## Inventory

**A commitment has:** a place; one quantum engaged; a fixed share retained; a direction, inherited from the transit that arrives. Nothing cyclic. Matter repeats with period 1/ω, so it has a phase whether or not the theory names it; the theory has not.

**The quantum sector needs:** spread over routes (Space and Gravity has it literally: a pattern is possibility in transit); localisation (commitment); interference; a rule for where commitment happens (the Born weights); a pattern over two places committing as one. Three of the five need a phase that routes carry and compare.

**The masses need:** a kind and a size. A repeat is one crossing of the pattern's extent (the Compton relation, ω = c/L), so size is the extent L in hops. Kind needs shape; shape needs corners; only a commitment turns possibility.

## The addition (candidate)

| addition | statement | status |
|---|---|---|
| a commitment has a loop | possibility runs around a closed walk of L hops, turning at commitments, returning to its start, once per repeat | candidate |

**What follows, if so.**
- Mass is the loop's length: ω = c/L, m = ħ/(cL), L a count.
- Kind is the loop's shape, up to the lattice's symmetries. Closed walks on the cubic lattice: one at L = 4, two at L = 6, a handful at L = 8.
- Phase is where on the loop the possibility is. A route of n hops advances it by n; routes of different length arrive at different phases.
- Interference: a commitment needs ħ of possibility; possibility arriving at different points of the cycle is not the same possibility to engage. In phase it adds, out of phase it does not. For a moving pattern the loop phase seen from outside is Doppler-shifted as in de Broglie's clock argument, giving λ = h/p.

**What it costs.**
- The hop length becomes a constant: L is a count, and masses in physical units need it. Space and Gravity's hints (a few quanta per place, not 10²¹) put it far above the Planck length, near the shortest Compton wavelength that is a particle, about 10⁻¹⁶ m. Not yet ruled.
- "Out of phase does not add" is a reading until the Born weights are derived from it.

**Precedents, named.** De Broglie (1924): a particle as an internal clock whose phase wave gives the matter wavelength. The zitter models (Schrödinger; Hestenes): the electron as a circulation at the Compton frequency. Matter reaches both from "a repeat is one crossing," with the circulation made of hops and the corners made of commitments. A new route to known destinations, not new destinations.

## The hop length is not a new constant

Newton's constant in hop units, from Space and Gravity's rulings. A body of mass M renews at ω = Mc²/ħ and retains δ(P∞/P_max) quanta per renewal, so it is a sink of strength σ = δ Mc² P∞/(ħ P_max) quanta per second. Possibility hops at rate ν = c/ℓ per relation, ℓ the hop length; on the cubic lattice the steady deficit at r hops is σ/(4πνr) quanta per place, so h = σ/(4πνP∞ r). Setting h = GM/(c² rℓ):

$$G=\frac{\delta\,c^{3}\,\ell^{2}}{4\pi\,\hbar\,P_{\max}}\qquad\Longleftrightarrow\qquad \ell=\ell_{P}\sqrt{\frac{4\pi P_{\max}}{\delta}},\quad \ell_P=\sqrt{\frac{\hbar G}{c^3}} .$$

The hop length, the capacity and the retained share are one relation apart. Given any two, the third follows. If the hint holds (P_max a handful of quanta) and the hop is at the top-quark Compton wavelength (ℓ ≈ 1.1×10⁻¹⁸ m, ℓ/ℓ_P ≈ 7×10¹⁶), then δ ≈ 10⁻³²: a renewal retains about 10⁻³² of a quantum as record. (An earlier line used ℓ ≈ 10⁻¹⁶ m and gave 10⁻³⁷; corrected 2026-11-04.) Pooling is as slow as every bound required. The relation renames one unknown as another; δ has no observational handle of its own.

So Matter introduces no fourth constant: ℓ replaces δ, or δ replaces ℓ, and the set of the theory's own constants stays at three (P_max, Λ, and one of δ or ℓ).

## The shapes, counted

Closed self-avoiding loops on the cubic lattice, up to the lattice's 48 symmetries and translation (a hand count done by machine, [`MATTER_notes/sap_count.py`](MATTER_notes/sap_count.py)):

| L (hops) | shapes | planar | non-planar |
|---|---|---|---|
| 4 | 1 | 1 (square) | 0 |
| 6 | 3 | 1 (2×1 rectangle) | 2 (the chair and the boat, as in cyclohexane) |
| 8 | 11 | 3 | 8 |

Small at small L, growing fast. Reflections are identified in this count; if a loop and its mirror are different kinds, the non-planar counts roughly double, and that distinction is where handedness would enter.

## Mass, with corners as commitments

Each corner is a commitment and each commitment engages ħ (ruling (B)), so a loop of L hops with k corners commits at rate kc/L and

$$m=\frac{\hbar}{c\,\ell}\cdot\frac{k}{L},\qquad \frac{k}{L}\le 1 .$$

- **A maximum mass.** The all-corner loop is the heaviest pattern there can be: m_max = ħ/(cℓ). The hop length is the Compton wavelength of the heaviest particle. Not the proton's (the τ, W, Z, Higgs and top exist); at or below the top quark's, ℓ ≲ 1.1×10⁻¹⁸ m.
- **No selection.** The allowed masses are the rationals k/L (later f/L; see Chirality). Any ratio can be matched with enough hops, so this must not be used to fit the known masses; a formula that fits anything explains nothing. The loop gives a scale and a bound, not a spectrum.
- **Self-gravity cannot select sizes.** A loop's own deficit is of order δ ≈ 10⁻³⁷. Whatever makes some loops stable and others not is not in the inventory. **The masses are blocked on the forces, not on gravity; charge comes first.**

**Mirrors (candidate).** A reflection is a lattice symmetry, but a loop is traversed, and inertia makes the direction physical: reversing the traversal is not reflecting the shape, so a chiral loop has four versions. A loop and its mirror are two kinds. A choice about what "the same" means, not a derivation; it is where a left/right label can sit.

## Charge (candidate)

A relation carries how much (occupancy, symmetric) and which way (a ratio, antisymmetric: r_ji = 1/r_ij, a 1-form). Gravity took the first; the second was set aside in Space and Gravity. Around a closed loop the ratios multiply to a holonomy e^Φ, equal to 1 while ratios are slaved to places. Let relations be out of step in this number too.

| | statement | status |
|---|---|---|
| cost | sliding costs nothing, so the cost of a 1-form out of step depends only on holonomies; the unique local quadratic cost in 3+1 is Maxwell's, ∫F². Same uniqueness as Einstein's, on the other number a relation carries | candidate |
| source | a traversed loop is a current loop: a circulation, which sources the which-way field as a **magnetic dipole**, not as a charge. Charge is a monopole and cannot be any shape or traversal property: mirror is P and reversal is T, and a time-even scalar is invariant under both; C is not a spacetime operation. So charge is a sign the loop **carries**, the sign of the which-way bias on the relations it runs on. **An antiparticle is the same loop with the opposite carried sign.** (Earlier "run backward" withdrawn: that flips the moment, not the charge) | candidate |
| quantization | a loop's phase must return to itself after a circuit, so the holonomy it carries and the holonomy it sits in combine to a multiple of 2π: the Aharonov–Bohm / Dirac argument as a closure condition on repeats | candidate |
| strength | the 1-form's stiffness relative to ħc (1/137) is not given; a fourth constant unless tied to the others | open |

## One pattern (candidate, from Allen)

One loop carries a sign (charge: particle or antiparticle, invariant under every boost) and has a sense seen along its motion (helicity: flips when overtaken, undefined at rest, as a massive particle's does). Both behave under boosts as their Dirac counterparts do. **Correction (from the 4×4 comparison):** Dirac's four components are (chirality) × (spin); particle versus antiparticle is the sign of a solution's frequency, not a component. So (carried sign) × (helicity) are two correct labels, not the component basis. The carried sign maps to the frequency sign. Chirality at the level of a loop is not yet defined; for a chiral loop, shape against mirror is a candidate for it.

"The face going forward is the identity": the loop's sense seen from where it is going is its helicity; with the carried sign, and its handedness if chiral, that is the identity. The loop's circulation is a magnetic moment, and a Dirac particle's moment is a number (set by its charge and mass) the picture can be asked to produce: a sharper test than the count of four. On a lattice with three lines through each place, which line a moving loop's plane is set against is a three-valued label that costs nothing and leaves mass unchanged. Three-valued, free, invisible to mass, carried by every loop: the shape of colour. Whether it is colour depends on how such labels couple; not done.

So, in one sentence: mass is size and corners (k/L); charge is the carried sign; helicity is the running sense seen along the motion; handedness is shape against mirror; a three-valued orientation label comes free. **Ruled as Matter's direction: one pattern.**

**Selection (candidate).** A charged loop sits in its own holonomy, and closure relates its length, its corners and its own flux. Only some (k, L) close. The first rule on the board that could pick sizes where gravity cannot. Not worked.

## Spin and moment of the one pattern

The square, L = k = 4, side ℓ, m = ħ/(cℓ). One quantum circulates at radius ℓ/2 with momentum mc:

$$S=mc\cdot\frac{\ell}{2}=\frac{\hbar}{2}.$$

Spin one-half, for the square. **Withdrawn as a general result** (see The chair's spin below): it is the square's geometry, and the square is not a pattern. As a current loop, I = ec/(Lℓ), A = ℓ²:

$$\mu=\frac{ec\ell}{4}=\frac{e\hbar}{4m},\qquad g=\frac{\mu}{(e/2m)S}=1 .$$

**Dirac has g = 2 (measured 2.0023). The loop gives half.** The same factor separates every classical circulating-charge model, the zitter models included, from Dirac; non-planar loops cannot close it (k ≤ L and the isoperimetric bound). Spin right, moment wrong by two.

**The factor is structural.** Redefining the repeat (crossing or circuit) cannot move it: the mass is the commitment rate kc/(Lℓ) and the current is ec/(Lℓ), both fixed by the geometry, so μ = eħ/(4m) and S = ħ/2 for any planar loop of any size. Closed as a route. Underneath is a classical theorem: charge and mass distributed alike and circulating together give μ/S = e/2m, g = 1. Dirac's g = 2 says the electron's charge and inertia are distributed differently.

**Which is what Matter already says.** Mass is the commitments: the corners and the circulating quantum. Charge is a which-way bias on the relations: the whole perimeter, at all times, whether or not the quantum is there. The computation above treated the sign as riding on the quantum (a point charge going round); that is not Matter's charge. The moment of a loop whose charge is a bias on its relations, from the field that bias sources through the 1-form's cost. Three readings, each worked: static on all perimeter relations (a charged ring at rest: μ = 0); riding with the quantum (the point-charge current: g = 1); a holonomy threading the loop (a charge–flux composite: μ unchanged, so g = 2 would need S = ħ/4, impossible). **Under classical Maxwell sourcing no reading gives g = 2.** As is known: no classical current does. The factor is Dirac's, from the four components mixing under the field.

## The one pattern is a Dirac walk (candidate)

What the loop does: possibility moves at c always; it turns only at a commitment; its mass is the turning rate, kc/L. That is Feynman's checkerboard (1965): a particle at light speed reversing at a rate set by its mass, whose path sum is the Dirac equation in 1+1. Mass-as-turn-rate, reached here from "corners are commitments," is Feynman's mass-as-reversal-rate. In 3+1 a walk on the cubic lattice at hop speed with a four-component internal state mixed at each step has the Dirac equation as its continuum limit (Bialynicki-Birula 1994; the quantum-walk literature since). The four components are the four versions. Dirac gives g = 2 and spin ½ together.

Between candidate and ruling: the walk needs amplitudes with phases (a walk of possibility without phases is diffusion); the loop's phase, where on the loop, is the candidate. And the turning rule must be shown to be Dirac's mixing matrix and not another.

**1/137** goes in from data, as Λ did: the which-way field's stiffness relative to ħc. Not to be sought among the others until the factor of two is understood.

## Phase, and what happens when routes meet

A pattern in transit carries where it is on its loop, θ, advancing 2π/L per hop. Two routes from A to B of n₁, n₂ hops arrive with Δθ = 2π(n₁ − n₂)/L and amounts p₁, p₂. Required of the rule for the amount at B: **conservation** (over unrelated phases the average is p₁ + p₂, so the cross term has zero mean); **scalelessness** (invariant under a common scaling, so the cross term is √(p₁p₂)·h(p₁/p₂)·f(Δθ)); **associativity** (three routes combine the same whichever pair first). These force h constant and f the cosine (Goyal, Knuth and Skilling 2010, borrowed mathematics; an earlier citation of Lamperti was wrong):

$$p_B=\left|\sqrt{p_1}\,e^{i\theta_1}+\sqrt{p_2}\,e^{i\theta_2}\right|^2 .$$

Amplitudes with phases, added and squared: forced given the three premises, which themselves carry the √ structure (review of 2026-11-04).

**Born, for free.** What commits is possibility; the chance of a commitment at B is the possibility present; possibility is conserved, so the chances sum to one. "Probability is the amplitude squared" is the amount of possibility at B in the forced representation. Rule and interpretation are one sentence. Status: an identification (committing stuff = conserved stuff), which a critic may fairly call the Born postulate restated; not a derivation.

**The walk is quantum.** Possibility hops at c carrying phase and turns at commitments with an amplitude the mass rule fixes: corner density k/L = mcℓ/ħ is turns per hop, so

$$\text{turn amplitude per hop}=i\,\frac{mc\ell}{\hbar}=i\,\frac{k}{L},$$

Feynman's checkerboard weight. Dirac's mass term is the turning, with its coefficient supplied by the loop.

## The 4×4 comparison

**1+1: exact.** The checkerboard's two components are the two directions of motion, which are the two chiralities; a reversal is a turn and a chirality flip at once. The corner with amplitude i·k/L is Feynman's mass term. **Ruled in one dimension.**

**3+1: not established.** Two obstacles, named.
- In the three-dimensional Dirac walk, direction changes at every hop, free, through the α-projections (the state splits into ±x, ±y, ±z movers and recombines: the zitter, at zero mass). The mass term β flips chirality at rate mc²/ħ without changing direction. So "mass is the turning rate" holds only if a corner is a chirality flip, not merely a change of direction. A loop-level chirality that a corner commitment flips is not defined.
- Space and Gravity's inertia ("possibility in transit keeps its direction") must be read as a statement about the mean direction, not the hop, to be compatible with the α-splitting. A reading of a ruling, to be made explicitly.

Status: **the one pattern is a Dirac walk** is ruled in 1+1 and candidate in 3+1.

## Chirality at the level of a loop (candidate)

At a corner the loop's local plane is spanned by the direction in and the direction out. Planar loops keep one plane; non-planar loops twist through corners, and the twist has a sign: the torsion. **Chirality is the torsion sign; a corner where it changes is a chirality flip.** Square and 2×1 rectangle: no flips. Chair: flips at all six corners. Boat: at four of six.

**Mass is the flip rate, not the turn rate.** The Dirac walk has direction changes free (α, at zero mass) and mass as chirality flips (β). So

$$m=\frac{\hbar}{c\,\ell}\cdot\frac{f}{L},$$

f the torsion-sign changes per circuit (replacing k/L). Chair 1, boat 2/3, planar 0.

**Closed loops must twist.** A planar loop would be massless, but a closed loop circulating at c is at rest, with a repeat and a count; a massless pattern has none. So massless patterns are open (never close, never repeat, no proper time: light) and closed loops have f > 0. The square and rectangle are not patterns; **kinds begin at six hops, with the chair and the boat.**

**What it settles.** Turning is free; a commitment is a flip ("corners are commitments" becomes "flips are commitments"). Inertia reads as the mean direction, with free turns as the hop-level splitting, now for a reason.

**To watch.** Torsion is the change of the local plane, whose normal is the three-valued label that looked like colour's shape. Chirality flips and that label are one geometric fact seen twice: a hint, or a sign one reading is wrong. Undecided.

## The chair's spin, and the 4×4 in the flip reading

Chair vertices (0,0,0),(1,0,0),(1,1,0),(1,1,1),(0,1,1),(0,0,1); vector area (1,−1,1)ℓ², magnitude √3ℓ². For possibility circulating with momentum mc, S = 2mc|A|/perimeter:

$$S_{\text{chair}}=\frac{mc\ell}{\sqrt3}=\frac{\hbar}{\sqrt3}\approx0.577\,\hbar\quad(\text{boat: }0.31\,\hbar;\ \text{square: }\hbar/2).$$

**Orbital circulation does not give ħ/2 for the loops that are patterns.** Spin ½ is the internal two-valuedness of the Dirac walk's state, the global sense about the loop's axis, not the size of an orbit.

**β.** A torsion-sign change at a corner swaps chirality; the global sense about the axis is the same on every edge, so the flip leaves spin alone: (swap chirality) ⊗ (identity on spin), which is β in the Weyl basis.

**α.** Projection of the chair's axis (1,−1,1) onto its edges in order: +1/√3, −1/√3, +1/√3, −1/√3, +1/√3, −1/√3; the torsion sign alternates likewise. On each edge spin-along-motion has the sign of chirality: right-handed with spin along the motion, left-handed against. The Weyl correlation.

Both of Dirac's structures are present on the chair with the right signs. **Structural match; explicit matrix equality not written** (the walk's amplitudes on the six edges).

## The propagator: identification, not a new calculation

The chair is a path; the propagator is the one-step operator on the whole lattice. The question is whether Matter's rules are the one-step operator of the three-dimensional Dirac automaton (Bialynicki-Birula 1994), whose continuum limit is the Dirac equation by theorem.

| Matter rule | automaton |
|---|---|
| hop at c, the internal state deciding the direction; an aligned state keeps going, an unaligned one splits (**inertia**, Space and Gravity) | the α-structure: the α_j = ±1 component moves ±j |
| flips at amplitude i·f/L per hop, with f/L = mcℓ/ħ (mass as flip rate) | the mass step exp(−iβmε) ≈ 1 − iβ·mcℓ/ħ |
| amplitudes with phases, added and squared (forced) | a unitary walk |

Inertia and the α-terms are one statement once the internal state exists. With the three rules the one-step operator is the automaton's; **spin ½ follows from Dirac**, and g = 2 follows from Dirac *with minimal coupling to the which-way field*, which is candidate (review of 2026-11-04).

**Derived:** the amplitude rule; mass as flip rate; inertia as α. **Assembled:** the four-dimensional internal state as (torsion sign) × (sense about the axis), which the chair exhibits with the right sign correlations but which is a reading for a general pattern in transit. **Status: the one pattern is a Dirac walk, ruled in 3+1 conditional on the internal-state reading.** An identification with a construction known to yield Dirac, not an independent derivation of it.

**Q1 ([`MATTER_runs/`](MATTER_runs/Q1_result.md)):** the automaton's rest-frame state on the cubic lattice, and where its current flows. It circulates about the spin axis (the zitter) as a smooth vortex; circulation per edge around the cube's hexagons against its squares is 0.87 at every mass and step count, which is the geometric ratio for a smooth field. **No chair structure. The chair is not the electron's orbit.** The loop supplied the internal state and the mass as flip density, and the walk carries those; the loop as a literal path is not what the dynamics does. "One pattern" stands as one walk with one internal state. The chair remains an illustration of maximal flip density and the Weyl sign correlations.

## The internal state is forced

**Meyer's no-go (1996).** A walk of amplitudes on a lattice that is homogeneous (sliding costs nothing), unitary (amplitudes forced, conserved) and moves (patterns are in transit) cannot be scalar: one amplitude per site can only rest or shift rigidly. An internal space is the only way possibility can move as amplitudes at all. Not a reading.

**Four, by the Clifford count.** Three directions of motion whose coin operators anticommute (so the continuum limit is first-order and direction-independent), plus a mass step that changes the internal state without moving it and anticommutes with all three (so the massive limit stays relativistic): four mutually anticommuting generators, whose smallest representation is C⁴. The direction operators are α, the mass operator is β, chirality × spin is the standard labelling. The loop's labels named what the algebra already had.

**Status: the one pattern is a Dirac walk, ruled.** The chain: amplitudes (conservation, scalelessness, associativity) → internal state (Meyer) → four components with α, β (Clifford) → mass as the β amplitude i·mcℓ/ħ → Dirac's equation in the limit (Bialynicki-Birula) → spin ½ and g = 2. Borrowed mathematics acknowledged; no physics borrowed. Dirac's equation from the two primitives, the rulings of Space and Gravity, and "commitments happen at a rate."

**Limits.** Lorentz invariance is broken at the hop scale and recovered in the limit, as on any lattice. Why commitments happen at the rate they do (the masses) is open. Charge's strength is from data. The colour-like label has no algebra behind it.

## Where Matter stands

**In:** everything Space and Gravity ruled, and one addition: commitments happen at a rate (the loop was the ladder to it; the walk is what stands).

**Out:** amplitudes with phases and the Born rule, forced; an internal state, forced, four-dimensional; the Dirac equation in the continuum limit, with spin ½ and g = 2; mass as the rate of commitments, with a maximum mass that sets the hop length; the hop length tied to δ and P_max through G, so no new constant; charge as a carried sign, with antiparticles as the opposite sign; the Weyl sign correlations exhibited by the first allowed shape.

**Withdrawn along the way, with reasons kept:** spin ½ from an orbit (the square's geometry; the square is not a pattern); charge as the traversal sense (a circulation is a dipole; C is not a spacetime operation); the four versions as Dirac's components (two correct labels, not the basis); the chair as the electron's orbit (Q1: the current is a smooth vortex).

**Where a fair critic pushes:** the theorems do the work (Meyer, Clifford, Bialynicki-Birula, Lamperti) and the primitives supply hypotheses; associativity of combining is assumed; "the limit must be relativistic" is what forces β; 1/137 is from data; nothing selects a mass; the colour-like label has no algebra.

**Matter stops here**, complete as far as the one addition forces. What remains needs something new each: a selection mechanism for the masses, a number for the field's strength, an algebra for colour. That is Nucleus.

## Open
- The spectrum: why these flip rates.
- The 1-form's strength (1/137). In CO's words it is the which-way stiffness in quanta per hop, about 137: the field of a carried sign reaches 1/137 of its pattern's extent before holding one pattern's worth (r_e : ƛ : a₀ = α² : α : 1). An input with a seat, as Λ is.
- The gravity/electromagnetism hierarchy (about 10⁴³ for the electron) is, in CO, the smallness of δ: gravity is weak because pooling is rare; charge is not pooling. A story, not a number; δ as estimated is in the neighbourhood and not on it.
- Whether the three-valued orientation label couples as colour does.
- The spectrum: which (k, L) close under their own holonomy.
- The 1-form's strength (1/137).
- Whether the three-valued orientation label couples as colour does.
- The Born weights from the phase.
- The Born weights from the phase.
- Charge, spin, the forces.

## 2026-11-05 — doublers closed; Q1 re-run on the symmetrised step

The Dirac automaton as published carries doublers (found 2026-11-05 while surveying no-go loopholes; record in `NUCLEUS_record.md`, runs R8–R10 in `NUCLEUS_runs/`). Closed by two rulings entered in `MATTER.md`: hops in no preferred order (symmetrised step), and a flip rate rising with alternation (Wilson term, unitary). The relational lattice alone does not do it (R8); the one-way non-unitary hop kills the electron (R9). Q1 re-run on the symmetrised step (`MATTER_runs/Q1b_symmetrised.md`): chair finding unchanged; the L_z ≠ 0 reading withdrawn as an ordering artefact.

## 2026-11-06 — two patterns, one stock: merge or exclude? (question opened)

**Why.** A Bose–Einstein condensate is cheap in CO's words: cold means few commitments, so each atom's transit spreads far; when the spread exceeds the spacing the atoms' transit overlaps and they are one pattern sampled many times (the single macroscopic wavefunction). But a Fermi gas at the same overlap refuses to merge and stacks one per state; that pressure holds up a white dwarf. CO's "overlap → one pattern" would condense both. The matter sector has one-pattern Dirac and no rule for two patterns engaging the same possibility. Statistics is a silence.

**What the rules give on reading.**
- If patterns of one kind are identical (the "one pattern" ruling), two of them live on *unordered* pairs of places; in three dimensions exchange is a Z₂ (Leinaas–Myrheim 1977), so only a sign ±1 is available: bosons or fermions, nothing else. The rules do not pick the sign.
- Capacity (P_max, one quantum per renewal) gives a hard-core exclusion at a place, not a sign; in three dimensions hard-core bosons are not fermions. Not the mechanism.
- Mass as renewal (massless patterns never draw a quantum) splits photons from electrons but puts He-4 on the wrong side: composite bosons need a sign that cancels in pairs, not an absence of drawing. Not the mechanism.
- The one route that uses what CO has: the internal four is a spinor and takes −1 under a 2π rotation. Berry and Robbins (1997) construct exchange of two spin-½ particles so that it is a 2π rotation of the internal state, giving the fermionic sign from the spinor alone, without Lorentz invariance; the construction is not unique and is not a theorem. Candidate shape, not a ruling: *exchange of two patterns is a 2π turn of the internal state; the four turns to −1; tiles with the four are fermions, patterns with an even count of them are bosons; massless patterns with no four are bosons.*

**What it must split.** BEC (He-4, Rb-87) merges; a Fermi gas (He-3, electrons) excludes; the photon condenses in a cavity. Any rule has to put each on its side.

**Grade.** Question open; one candidate shape; no run (nothing to measure until the exchange construction is written on the lattice). Prior art first: Leinaas–Myrheim 1977; Berry–Robbins 1997; Duck–Sudarshan 1998 on what the spin–statistics theorem actually needs.

**Read, 2026-11-06 (Berry–Robbins 1997; Harrison–Robbins 2003; Duck–Sudarshan 1998, 2003; Shaji–Sudarshan 2003).** The Berry–Robbins sign comes from a postulate (single-valuedness in a transported spin basis); Harrison and Robbins show other admissible choices give the wrong statistics or parastatistics, and only the completely symmetric SU(2n) representations give nature's, "a matter of judgement" in their words. Duck and Sudarshan examine every kinematic non-relativistic argument, construct a counterexample to the family, and conclude the connection is dynamical: a positivity requirement on how the fields enter the action, not a property of configuration space. Consequence for CO: the 2π-turn shape above relocates the choice rather than removing it, the same failure as the second-order argument of 2026-11-05; downgraded from candidate to shape-known-insufficient. The live route is the dynamical one, and CO has a positivity it did not choose: commitments are a count. Whether positivity of the count, applied to two patterns sharing one stock, forces the exchange sign is the question. A construction, not a reading; not begun.

## 2026-11-06 — a pattern that commits but never measures (dark matter, first reading)

**Question.** What would a pattern have to be to give what is attributed to dark matter: mass; no charge; no colour; gravity only; stable; cold; present from the beginning; about five times the baryons.

**Translation.** Mass: a pattern that renews. No charge: a pattern carrying no sign on its relations; charge is a carried sign and nothing in the rules requires every pattern to carry one. No colour: one tile. Gravity only: it pools possibility, as every renewing pattern does. Never seen: under "a commitment resolves exactly what it engages," a pattern that engages only free stock renews, has mass and bends h, and never engages another pattern's transit, so it never resolves anything, is never resolved, and leaves no readable record: *a pattern that commits but never measures.* Stable: nothing lighter without a sign to decay into. Cold and abundant: made when everything was made, never exchanging with the hot stuff after.

**Status.** Permitted by the rules as written; the first win on this route. Not predicted: nothing picks its mass, its abundance, or the number of kinds. CO's gravity sector is GR's, so CO needs invisible mass for the reasons GR does and offers no MOND of its own.

**One consequence, weak.** A pattern with no sign has nothing to carry a which-way ratio, so it cannot be measured even in principle, only felt through its pooling. If that is what dark matter is, direct detection is null by rule, not by weakness of coupling. Confirmed only by continued absence; stated for the record.

**Grade.** Shape, entered in `OPEN_DIRECTIONS.md`.

## 2026-11-06 — statistics, first rung: positivity of the count forces exclusion (candidate)

The Dirac walk has a forward branch (positive quasi-energy) and a backward branch (negative). For one pattern the backward branch is the anti-pattern, reinterpreted. For many patterns, if the backward branch could be filled without limit the total would run away; in standard physics "energy unbounded below." In CO the primitive speaks directly: the count cannot go down, so a backward-renewing pattern is a commitment un-happening. The backward branch must be closed, and the only closure is Dirac's: already full, one pattern per state. That is exclusion, from the count. First rung: *positivity of the count forces exclusion for every pattern whose backward branch is independent of its forward one.*

What makes the backward branch independent: in the standard theory a complex (charged) field; a real (neutral) field's negative-frequency modes are conjugates of its positive ones, not new states. In CO words: a pattern carrying a sign has an independent backward branch. Hence, candidate: *patterns that carry a sign are fermions.* Elementary charged patterns (electron, tiles) are fermions; the photon carries no sign and is not forced. One-directional.

**Next rung and test.** A neutral spin-½ pattern (Majorana-type; the neutrino in nature) is a fermion by spin–statistics. If a signless walk's backward branch is conjugate to its forward one, CO would not force it, and the rule would need the internal four rather than the sign to carry the load. Construction: write the signless walk and determine whether its backward branch is independent. Unknown outcome; changes a ruling; to be registered.

Entered in `OPEN_DIRECTIONS.md` under statistics.

## 2026-11-06 — S1: the signless spin-½ pattern is a fermion by existence

Registered (`MATTER_runs/S1_signless_walk/`), unknown outcome. Result: the Majorana bilinear kernel of the adopted walk is purely antisymmetric (symmetric part 10⁻¹⁵, antisymmetric ≥ 0.82 across the zone), so a commuting signless pattern with the four has no generator and does not move; only anticommuting components walk. Second rung: a signless pattern with the four must be a fermion to exist. With the first rung (signed: fermion by count positivity): candidate, *every pattern carrying the four is a fermion.* The Majorana test that could have knocked the route down passed. Next rung: patterns without the four (the photon's walk), and whether bosonic statistics is then forced or merely allowed. OPEN_DIRECTIONS updated.

**Cold reading, same day; regraded.** The two rungs restate Pauli 1940. Rung 1: "the count cannot go down" is the number operator, non-negative under either statistics; the argument gets its force only by identifying commitment rate with quasi-energy, at which point it is positivity of energy minus two of Pauli's premises (positive norm, locality), and "the only closure is already-full" assumes exclusion to conclude it. Its sign criterion is refuted by the W boson (charged, bosonic, second-order dynamics): what carries the load is the first-order two-branch walk with the four, not the sign. **Withdrawn: "patterns that carry a sign are fermions."** Rung 2: the antisymmetry of C G(k) is an algebraic identity for every C-symmetric Hermitian generator (K(−k)ᵀ = −K(k) from G Hermitian, C real symmetric, C² = 1); S1's measured quantity and its control are the same fact, so the registration's "unknown outcome" was not unknown. "Does not move" is false of the first-quantised pattern (a c-number Majorana packet moves; checked) and true only of the bosonic Fock Hamiltonian, where it is the vanishing Majorana Lagrangian. Branch choice: "backward" is defined only while the band stays inside |ε| < π, which fails where the π-sector doublers live.

**What survives: a consistency condition.** Given a Fock quantisation with positive norm and the identification frequency = commitment rate, the four-component first-order walk is consistent only with anticommutators, as in standard field theory. The matter sector is now checked compatible with Fermi statistics, which it had not been; it does not force them. Grade: consistency condition (restates Pauli 1940). The rung that still stands is the count primitive supplying positivity of the generator; the other two premises Pauli needs (positive norm, locality) are not yet CO's, and that is where the next step is. Prior art to carry: Dirac 1930; Pauli 1940; Majorana 1937; Weinberg vol. 1 §5.5–5.7; Berezin 1966; Bisio–D'Ariano–Perinotti 2016 (fermionic QCA Fock construction).

## 2026-11-06 — the two missing premises, read against the rules (candidate: statistics as a consistency condition on CO's own inputs)

**Positive norm.** The squared amplitude is the possibility at a place (amplitude rule + Born identification), and possibility is a non-negative conserved amount. Negative norm would be negative possibility. Positive norm is the primitive, not a premise; Pauli's indefinite-metric escape is closed by what possibility is.

**Locality.** The walk hops to adjacent places: a strict light cone. On such a lattice both brackets vanish outside the cone for either statistics, so Weinberg's microcausality argument does not discriminate here. Locality's job on CO's lattice is narrower: it forbids discarding the backward branch (a forward-band-only field is non-local on the lattice), so the local field carries both branches.

**The three inputs, all CO's.** (i) Adjacency keeps both branches in the field (ruling, gravity sector). (ii) Possibility ≥ 0 forbids negative norm (primitive). (iii) Commitment rate = quasi-energy, so filling the backward branch without limit is a count running backward, forbidden (the mass-as-renewal identification). With both branches, positive norm, and a generator bounded below, the four-component walk admits only anticommutators. Pauli's conclusion on CO's premises.

**Grade.** Consistency condition on CO's own inputs, the grade 3D has: not forced by the primitives alone, the only option consistent with the rules as they stand. The step a reader will press is (iii). Hole kept open: where the quasi-energy-π sector is populated (the doublers), "backward branch" has no clean meaning; the argument covers the light species and needs the doubler item settled to cover the band. To be cold-read before `MATTER.md`.
