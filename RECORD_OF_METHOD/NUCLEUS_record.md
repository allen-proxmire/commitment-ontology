# Nucleus (working record)

*Working record; formerly CO 2.2.*

Continues from [`MATTER_record.md`](MATTER_record.md), which stops where its one addition stops forcing. Three questions remain: the masses, the field's strength, colour. Same method.

## Colour

**Candidate: the three lines.** As three directions gave spin through the Clifford algebra, three lines might give colour: with no backdrop, which line at a place is called first, second, third is a convention at each place, so a relation would carry how the triad at one end matches the triad at the other, a 3×3 unitary rather than a phase. Local relabelling is a gauge symmetry, its connection a gauge field, its cost Yang–Mills by uniqueness. U(3) = U(1) × SU(3): phase as charge, the rest as colour, colour's three as space's three.

**Excluded, by group structure.** Colour is internal: rotating space leaves a quark's colour unchanged. An SU(3) acting on the triad rotates with space. For it to work, SU(3) on the triad would have to split into the spatial rotations SO(3) and an internal remainder blind to them. It does not: SO(3) is a subgroup of SU(3), not a factor, and the five generators left over transform as a quadrupole and do not close. There is no internal part of the triad's unitary group. **The three lines are not colour.**

**Where that leaves it.** The only three-valued thing in the inventory is spatial; colour cannot be spatial. Colour needs an internal three-dimensional space that nothing in the inventory provides: a gap in the inventory, as the masses are. The Standard Model's other unexplained three, the generations, has no basis for identification with the lattice's three either. The inventory as it stands covers gravity, electromagnetism and the Dirac fermion; the strong and weak forces are internal-symmetry physics, which two primitives on a network of lines have not produced.

**The choice.** Either a third primitive that carries an internal space (nothing on the board forces one, so the method would need a named contradiction to admit it), or CO stops at the physics of 1930 and says so.

**The cascade criterion (Allen).** A third primitive is admissible on a named contradiction with the world (the ruled set makes the proton elementary; experiment makes it composite, bound by a force the ruled set lacks, with most of its mass in the binding). It is *worth* admitting only if it cascades: if positing it brings a second open problem with it. One primitive for one input is the trade the restart exists to refuse. Note for the record: in the standard theory, colour plus one coupling does cascade, to the whole hadron spectrum (lattice QCD computes hadron masses from α_s and the quark masses); it does not reach the lepton masses or α.

## Open
- Colour: an internal three, or a stop.
- The masses: a selection mechanism.
- The field's strength: an input with a seat.

## 2026-11-05 — the "sorts of possibility" candidate, costed from prior work

Searched the author's earlier program for everything on multiplicity. Findings folded into `NUCLEUS.md` ("Sorts of possibility, already costed") without citation; the source papers are private and are not linked from this repo.

Summary: N indistinguishable conserved sorts force U(N) = (SU(N)×U(1))/Z_N (textbook, restated); the count N is not selected (symmetric multiplet stable for all N); {1,2,3} as posited gives three U(1) factors, not one; the multiplicities reduce to internal dimension d via the Welch bound (d = 3 ⟹ nothing stable above SU(3); falsifier: stable SU(N≥4)); internal three found distinct from spatial three independently. The candidate cascades only as far as SU(N). Open check: compatibility of an internal d = 3 with the Clifford four of the matter sector.

## 2026-11-05 — check: can the Clifford four carry an internal three?

No. Computed (`NUCLEUS_notes/clifford_commutant.py`): commutant of {α₁,α₂,α₃,β} on C⁴ is 1-dimensional (scalars); massless, 2-dimensional (1, γ₅). Spin Casimir on C⁴ is 3/4 on every vector: 2 ⊕ 2, no triplet. Reading: the matter sector's internal space supports exactly U(1) as its internal symmetry (two chiral U(1)s before the mass term, one after); colour cannot sit inside it and must be a new tensor factor. Entered in `NUCLEUS.md`. Grade: ruled (it is a theorem about the representation, Schur's lemma, not a candidate). Consequence: "two primitives give one internal symmetry, U(1)" is now a statement, not a hope.

## 2026-11-05 — walls, loopholes, and two new open items

Survey of which no-go theorems CO's qualities bear on (relational lattice, hold-and-release, refraction gravity, scaleless hopping, local commitment). Entered in `NUCLEUS.md` as "Three kinds of wall" and "Two walls not yet faced."

- Hold vs chirality: outcome fixed by reading (hop and flip scale alike; β parity-even; no axial 1-form in inventory); not registered as a run; one numerical check, `NUCLEUS_notes/hold_chirality_check.py`, L→R = R→L to 1e-14. Ruled: chirality-blind.
- Bell: named as open. No account of entangled commitment.
- Doublers: `NUCLEUS_notes/doublers_check.py` on the Q1 automaton's Bloch operator. Massless: 12 gapless points. Massive: 4 gapped by θ, 8 at (±π/2)³ remain gapless. The Dirac identification on the cubic lattice carries eight massless extra species. Not caught by the 2026-11-04 review. Relational-lattice escape available, unused. Open; to be moved to the matter record when addressed.
- Weinberg–Witten: evaded by having no Lorentz-covariant local stress tensor at hop scale; CO claims no graviton, so not needed. Spin–statistics: lattice loophole available, but no multi-pattern statistics exist to use it. Neither entered in the clean doc.

## 2026-11-05 — R8: relational lattice vs doublers. Excluded.

Registered (`NUCLEUS_runs/R8_relational_doublers/REGISTRATION.md`), outcome unknown before the run. Cubic calibration gave 8.9 species (expected 8); random Delaunay lattice gave no E² regime at all, a broad peak of near-zero modes (nominal count hundreds, rising as E_c → 0). Removing translation invariance voids Nielsen–Ninomiya but does not yield one species. Candidate excluded; doublers stay open. Result note `R8_result.md`.

Doubler bullet in `NUCLEUS.md` corrected the same day: three true doublers (gapped by θ) plus eight massless two-component γ⁵ modes with speed c cos θ, not "eight massless Dirac species"; Gupta–Short 2026 and Arrighi et al. 2025 cited.

## 2026-11-05 — question opened: does commitment give transit a direction?

**Why.** The doublers (above) are removed in lattice physics by a Wilson term, and in the author's earlier program by a retarded (one-way) hop, which is the same term. CO has the ingredient (commitment is irreversible) and has not used it in the walk: the matter sector's transit rule is symmetric in the hop direction.

**What a retarded hop would retire.** The three zone-edge doublers, if the term is a β-coupled (Hermitian, unitary) Wilson mass: "the flip rate rises with how much the transit alternates between neighbours." The eight γ⁵ modes are a separate matter: a β-type term cannot touch them (β anticommutes with γ⁵ at those points), so they need something else or an account.

**What it costs.**
- A non-unitary (damping) version, the literal retarded difference e^{ik} − 1, damps every mode at a rate ∝ k² per hop. For a pattern of momentum k in hop units the lifetime is ~ 1/(εk²) hops; with the hop at 10⁻¹⁸ m and 3 × 10²⁶ hops per second, an electron-scale pattern (k ~ 10⁻⁶) would lose its amplitude in ~ 10⁻¹⁴ s. This version is dead on arrival unless the lost amplitude is accounted for, and it is 10²⁰ times the retained share δ. (This is also a check the earlier program's non-Hermitian arrow did not make.)
- A unitary Wilson-mass version costs nothing observable at low k (a mass shift ∝ k²) and is a ruling: "mass per hop depends on alternation," a new reading of the flip rate, not forced by the primitives but of the same kind as the existing flip-rate rule.

**What it must agree with.** Q1's rest current, g = 2 (conditional), the zitter, the Compton-scale structure: all are k ≈ 0 statements and survive a k² correction.

**Registered check R9.** Apply both versions to CO's own automaton and count the gapless, long-lived points in the zone. Unknown part: whether the γ⁵ modes survive the unitary Wilson mass (structure argument says yes; to be computed), and the low-k lifetime in the damping version (to be computed, not assumed).

## 2026-11-05 — R9: retarded hop. Wilson-mass form works for the doublers; damping form excluded; γ⁵ modes survive both

Computed on CO's automaton (`NUCLEUS_runs/R9_retarded_hop/`). Unitary Wilson mass r = 0.5: 12 → 9 massless gapless points (the three zone-edge doublers gone; origin + eight γ⁵ modes remain), 8 with mass. Damping ε = 0.5: only the origin survives, but low-k decay rate εk²/2 per hop gives an electron lifetime of 1.8 × 10⁻¹⁵ s; excluded. The eight γ⁵ modes are immune to any β-type term (structure argument confirmed numerically). Candidate: retarded hop in unitary form. Open: the eight γ⁵ modes, which belong to the split-step structure of the walk.

## 2026-11-05 — R10: the γ⁵ modes were an ordering artefact; symmetrised walk + alternation mass gives one species

`NUCLEUS_runs/R10_split_order/`. Sequential P_z P_y P_x has the eight γ⁵ modes; Strang-symmetrised, palindrome and simultaneous orderings do not, and in all of them the mass gaps everything but the origin and the three zone-edge doublers. Strang + R9-A Wilson mass (r = 0.5): exactly one gapless point massless, none massive, Dirac dispersion at low k. Two rulings close the doubler item: hops in no preferred order (what the primitives say anyway); flip rate rising with alternation (new, of the same kind as the flip-rate rule). Pending the author's reading before `NUCLEUS.md` and `MATTER.md` are changed.

## 2026-11-05 — Bell: a commitment belongs to the pattern, not the place ("a pattern sampled twice")

**The question.** A commitment is a definite irreversible event. Bell (and experiment) exclude any account in which two spacelike-separated outcomes are each fixed by what is local to its own end. CO cannot shrug as standard quantum mechanics does, because it says the event happens. So: does a commitment belong to a place, or to a pattern?

**Reading taken (author's, 2026-11-05).** An entangled pair is one pattern sampled twice. A commitment belongs to the pattern; when the pattern has two places, one commitment increments the count at both. The correlation is one event seen from two ends. This is the only route that keeps the primitive: superdeterminism forfeits free settings; many-worlds denies commitment outright.

**Cost, named.** One event at two places needs an ordering, which is a preferred foliation. ~~CO's gravity sector already carries one (khronometric class, preferred frame), so the price has been paid once; it must be the same foliation.~~ False on the day it was written: the gravity sector has no preferred frame (a conflation with the author's earlier program). Corrected 2026-11-05 and again 2026-11-07. No signal passes, as in collapse theories. Candidate, not yet needed.

**Check with teeth (passed).** If every renewal were a selection, nothing would interfere. CO's rulings already separate renewal (the clock; commitment that keeps the pattern) from selection (commitment on engagement, hold-and-release). In free transit the only trace is the retained record δħ per renewal. Two paths leave records at different places, so visibility after N renewals is V = (1 − δ)^N ≈ exp(−δN). With δ = 10⁻³²: electron over 1 s, N = 8 × 10²⁰, V = 1 − 10⁻¹¹; C₇₀ (Arndt et al. 1999), N = 6 × 10²⁴, V = 1 − 6 × 10⁻⁸; 25 kDa molecules (Fein et al. 2019), N = 3.5 × 10²⁶, V = 1 − 3.5 × 10⁻⁶. Observed visibilities are tens of percent, so interferometry bounds δ < ~10⁻²⁷ independently of the hop estimate; δ ≈ 10⁻³² passes by five orders. Script `NUCLEUS_notes/record_visibility_bound.py`. Note the direction: this is a bound that experiment places on a CO constant, and CO's value sits inside it; it is not a prediction.

**What is not settled.** Why selection happens on engagement and not on renewal is a ruling (hold-and-release), not a derivation; a critic will call it the measurement problem renamed, and will be partly right. What CO adds is only this: the event is real, it belongs to the pattern, and its free-flight trace is bounded and tiny.

## 2026-11-05 — constituent-count flow scaling as a constraint on the third primitive

ALICE O–O preliminary (2026; the RHIC pattern): baryon flow exceeds meson flow in the ratio of quark counts. Reading: the third primitive must supply three separable carriers (momentum carried singly inside the plasma, bound outside), not three labels on one pattern. "Possibility in sorts" is the wrong shape and is excluded as a candidate on this ground, on top of the costing above. What remains has the shape of a binding whose release depends on the surroundings; hold-and-release has that shape but nothing about its sign or strength is known. Entered in `NUCLEUS.md` under the bar. Reading only.

## 2026-11-05 — the shape of a third primitive: tiles and kinship

Vocabulary fixed. A **tile** is a piece of a pattern; a tile is not a pattern and does not renew alone. A **kinship** is the relation among the tiles of one pattern; distinct from a relation between places.

The shape (not a candidate): a proton is a pattern of three tiles. A tile's commitment completes only with its kin. Kinship is a relation whose length costs; it does not slide for free. Where kin are everywhere, any three complete and a tile moves freely between kin; where the only kin are a tile's own two, it never gets away.

Three requirements, from experiment: tiles separable as carriers (flow scaling); completion rising with density (deconfinement); separation cost linear in length (string tension). Cascade, on paper: a length-costing kinship is a string, and strings give the hadron spectrum; it does not reach the lepton masses or 1/137.

Open before candidate: is kinship CO's one relation in a second regime, or a second kind of relation? And nothing selects three.

## 2026-11-05 — three-tile patterns: candidate; the stretch cost computed

**Revival of (a).** "Inside a pattern" has a marker that is not record: the Bell ruling, a commitment belongs to the pattern. The tiles of one pattern commit together. So kinship is the inside of a three-tile pattern, a new kind of pattern (a ruling on what possibility in transit can be: three tiles in transit together), not a third primitive. A tile never commits alone; in a plasma it completes with whatever kin are near. Free quarks would falsify this.

**Colour.** Which tile completes with which is a convention; changing it is a slide, and sliding costs nothing: colour change is not an event. Colour is the bookkeeping of kinship; the gluon field is the ratio on kinships, as the which-way ratio on relations was the electromagnetic field. Three-way matching gives SU(3) by uniqueness; the three is unselected, as before. Candidate.

**Stretch cost (computed, `NUCLEUS_notes/kinship_stretch_cost.py`).** Under CO's own transit rule (ratio hopping at c), a pattern of size L renews once per round trip, T ≈ 2L/c, so mc² ≈ πħc/L: the cost *falls* with separation (zero-point scaling; ≈ 0.6 GeV at 1 fm). That is a bound state, not confinement. A linear cost needs the kinship to be *engaged* possibility along its length, one held quantum ħc/a per grain a, giving E = (ħc/a²)L, a string with tension σ = ħc/a². With the hop length (1.1 × 10⁻³ fm) σ = 1.6 × 10⁵ GeV/fm, five orders above QCD's 0.9 GeV/fm; QCD's tension needs a grain a ≈ 0.47 fm, which is a new length not in the inventory (it is Λ_QCD in disguise).

**Ruling.** Stretch cost under the ordinary transit rule: excluded as confinement. Kinship as engaged possibility along its length: candidate, at the price of one new length (≈ 0.5 fm). The three-tile pattern therefore costs exactly one constant beyond the matching count, the same count as the standard theory (σ or Λ_QCD). Not a derivation; the shape matches at the cost of the same input.

## 2026-11-05 — the grain: tiles' own renewals; σ = (m_tile c²)²/ħc

If the quanta held along a kinship are the tiles' renewals, the grain is the tile's Compton length and σ = (m_tile c²)²/ħc. m_tile = m_p/3 = 0.31 GeV gives 0.49 GeV/fm; measured ≈ 0.9 (↔ 0.42 GeV). Factor ~2; the constituent-quark model's usual gap. The tension is thereby not a new constant but the tile mass, already in the mass problem. "Three-tile patterns" entered in `NUCLEUS.md` as candidate.

## 2026-11-05 — corrections after outside reading

Errors confirmed by re-running and corrected:

1. "One species" (R10, MATTER, NUCLEUS) was a threshold artefact; the unitary Wilson angle is periodic, r = 0.5 outside its window; π-sector never counted; massless palindrome has 32 zero points. R10d added: for r ≲ 0.35 the extra species sit at 0.3–0.9 hop units in both sectors, the standard Wilson statement. With a physical hop these are predicted particles; their absence below ≈ 100 GeV bounds ℓ ≲ 6 × 10⁻¹⁹ m (r = 0.3). Doubler item regraded: open, as a bound on ℓ. The two walk rulings regraded from needed to candidate.
2. The "preferred foliation the gravity sector already carries" did not exist in CO; it was conflated with the author's earlier program. Withdrawn from NUCLEUS and the plain doc; the Bell cost is now stated as unpaid, with the flash-ontology alternative (Tumulka 2006) named.
3. "Gluon field is the ratio on kinships" was wrong (a ratio is abelian). Corrected to a 3 × 3 unitary per kinship.
4. Smaller: "Welch bound" misattribution removed; "three abelian factors" → three U(1) factors; r10c dispersion formula corrected to √(θ² + (2k)²); vacuous falsifiers (free quark, SU(N ≥ 4)) restated as consistency; ε = 0.5 dependence of the 10⁻¹⁵ s lifetime stated; `kinship_stretch_cost.py` now computes the m_p/3 figure it is cited for; hold-chirality check marked as a scheme symmetry, not an automaton result; chiral-U(1) statement qualified by the Wilson term's explicit chiral breaking; "engagement vs renewal" flagged as undefined in the rules table.
5. Three-tile section: cost line now lists the new objects (tile, non-sliding relation, completion rule, length cost) and says the cascade bar was restated, not met; flow scaling demoted to the weaker evidence behind DIS and three-jet events.
6. Prior art added to MATTER references: Karsten–Smit, Strang, Christ–Friedberg–Lee, Perantonis–Wheater, Bakircioglu–Arnault–Arrighi, D'Ariano–Perinotti.

Not changed: the ordering finding (eight γ⁵ modes belong to the sequential order; Q1b's L_z withdrawal), R8's direction, R9's exclusion of the damping hop, the Clifford-four commutant, the sorts costing.

## 2026-11-05 — one commitment, two stocks: what resolves what (candidate)

**The gap.** The review found "selection on engagement, not on renewal" undefined: renewal already engages. The author's correction: commitment *is* the act of resolving possibility; there is no second kind.

**The rule (candidate).** A commitment resolves exactly the possibility it engages. The rules already name two stocks: *free* possibility (the vacuum's) and possibility *in transit* (a pattern's).
- A renewal engages free possibility. It resolves the vacuum's stock at that place (engaged, counted, released) and nothing about the pattern, whose transit was not touched. So a free pattern keeps interfering while its clock ticks.
- A commitment that engages possibility in transit resolves that pattern. Only patterns commit, so this is always one pattern engaging another: a measurement is one pattern engaging another's transit. [Amended 2026-11-07: not every contact is an engagement, and which are is open.] The vacuum never commits; it is timeless stock.
- An entangled pair is one pattern whose transit is in two places; engaging it anywhere resolves it everywhere, since it is one stock ("a pattern sampled twice").

**Two test readings.** *Refraction:* light through glass hops on the glass's clock-rate field h, a property of place; it never draws on the glass's in-transit possibility. Route, not resolution; no measurement. Holds. ~~*Elastic scattering:* two electrons engage each other's transit; both are resolved (directions decided); the record is the change in each one's transit, and nothing else need be permanent. Holds as a reading.~~ [Withdrawn 2026-11-07: elastic e–e scattering is Coulomb scattering, a route on the which-way ratio, coherent (Mott 1930); the rule is left with no stated criterion for which contacts are engagements.]

**What stays resolved after release (the hold-and-release check).** Hold-and-release says engaged possibility is released, nothing consumed. What is left is in the relations: the pattern's in-transit stock elsewhere flows to where it was engaged ("possibility moves toward where it is engaged," the gravity sector's rule, here applied to one pattern's own stock), the ratios on the relations it used are set by that flow (which way it went), and one quantum's share is retained as record. After release the pattern goes on from the event, in transit again, with its ratios the fact of where it was. Consistent with the rules as stated.

**Cost, unchanged.** The flow of a pattern's stock to the engaging event must complete across spacelike separation for the two-place case; that is the Bell cost, still unpaid (ordering, or a flash-type account).

Not in the clean docs; candidate in the record.

## 2026-11-06 — entanglement: one pattern, two places, one undivided stock

An entangled pair is one pattern with two places and one undivided stock, made by a commitment that conserved something (a spin-zero parent into two halves; one photon into two with the parent's energy); the measurement is the cut. The pair does not acquire a correlation; it is born as one pattern whose conservation has not yet been divided. Distance is counted along relations; the two places are related to each other directly and to the world only through what they have engaged, so until one engages the world there is no relation along which to count a separation between them. The cut is one commitment and belongs to the pattern, not to an end. What this does not pay: in the world's bookkeeping two counts tick, and an account of that without a preferred frame is still owed. Candidate reading, under the entanglement candidate above.

**Shape noted.** The structure is the three-tile pattern's: places with a kinship, committing together. The pair's kinship can be cut; the proton's cannot. If that holds, entanglement and confinement are one object at two strengths. Shape only; in `OPEN_DIRECTIONS.md`.

## 2026-11-06 — three-tile section, cold reading; regraded to shape

Findings applied. (1) No gluon degrees of freedom: gluons carry colour, self-couple, carry ~half the proton's momentum, and pure SU(3) has a string tension (quenched √σ ≈ 440 MeV); "held quanta are the tiles' renewals" predicts zero tension without tiles and is falsified. (2) σ ∝ m_tile² is falsified by flavour-universality of the tension (one σ for charmonium and bottomonium); using current quark masses gives 5 × 10⁻⁵ GeV/fm; "tile mass" and √σ are both Λ_QCD by dimensional transmutation (NJL), so "not a new constant" was circular; and a tile has no mass under MATTER's definition (mass is a pattern's renewal rate; a tile does not renew alone). Struck. (3) "Never commits alone" is false of the quark–gluon plasma (deconfined, screened, interacting singly) and of DIS (one quark absorbs the photon); restated as "no tile is found alone at the end." (4) Gauge relabelling conflated with colour-changing emission; separated. (5) "3 × 3 unitary … which is SU(3)" is U(3); the determinant phase is the unselected U(1) already flagged; fixed. (6) "Not a third primitive" contradicted the cost line; now open. (7) The evidence paragraph: DIS and three-jet events are the evidence, and three-jet events are gluon evidence; constituent-count scaling demoted there too. (8) "One object at two strengths" dropped: state property vs Hamiltonian property, no parameter named; the Cooper-pair reading of the same day showed the only real dial is the bookkeeping the kinship carries (none / abelian / non-abelian), which is standard. Kept, narrowly: whether "one pattern" coincides with the colour-singlet (Gauss-law) constraint. Prior art added to `NUCLEUS.md`.

## 2026-11-06 — the wall, stated as a result; the gluon column as a reading

Entered in `NUCLEUS.md`. The inventory is abelian (sign, ratio, four); the nucleus needs a self-coupling three-way matching; four routes to the three closed by the same finding; a third primitive would be a labelled kinship, buying SU(3), self-coupling and confinement's shape at the standard price and cascading only to the hadron spectrum, so not earned.

"Record becomes relation," read for self-coupling: what makes gravity's comparison self-couple is that the occupancy compared is itself stock (possibility in transit). The ratio (charge's field) carries no stock and is abelian. A comparison of a three-way matching carried by a pattern whose internal state is a pair of labels carries what it compares, so it acts on itself: the adjoint. Candidate reading: self-coupling follows from carriers being patterns, given the label; it does not supply the label. Closes the "gluon column missing" gap at no extra price; the price remains the unselected three.

Author's next idea, noted for later: spinning disks with clear and black sectors (moiré / Benham-type patterns from superposed rotations) as a picture for how a three-way matching might arise from two simpler things turning against each other. Not examined.

## 2026-11-06 — shape, author's: one pattern, three times, sharing one cycle

A proton is not three patterns bound together but one pattern, the electron's kind of walk, present three times, the copies turning against each other; the three-fold structure is what the turning makes (the moiré picture: two spun disks make patterns neither has).

Read: the one thing a walk has that turns is its cycle (the flip; mass as renewal rate). Three copies sharing one cycle sit at offsets of a third of a turn; relabelling them without change is a shift of all three by a third. That is a three-fold symmetry arising from three copies on one cycle, not from a posited label: the first picture in which the three is a consequence. In the standard theory the thirds-shift is the centre of colour, Z₃ ⊂ SU(3), the piece that decides confinement versus deconfinement (Polyakov loop). So the picture, if it holds, supplies the three and the confining part of colour; the carriers-are-patterns reading supplies self-coupling; not supplied: the continuous matching (the eight gluons), which in the standard theory does not follow from the centre. Kinship here is sharing a clock: the three commit together because it is one cycle, so the inside marker is met without a new relation.

Grade: shape. Check with unknown outcome, to be registered if pursued: three interleaved Dirac walks on one cycle; is the thirds-shift a symmetry of the combined step, and does mismatch between the copies cost?

## 2026-11-06 — R11: three on one cycle. The three arises; sectors split in mass; no confinement from it

Registered (`NUCLEUS_runs/R11_three_on_one_cycle/`). Three copies of the walk with a shared flip passing around the cycle (one choice, flagged): the thirds-shift is a symmetry (10⁻¹⁶), its charge is triality; triality 0 has mass θ, triality 1 and 2 have mass θ/2 with reversed sign; all propagate. The moiré shape gives the three and the centre of colour as a consequence of sharing one cycle, plus a mass cost for being out of step; it does not give confinement. Upgraded to candidate for the origin of the three; the continuous matching still missing. OPEN_DIRECTIONS updated.

**R11, cold reading; excluded.** The thirds-shift is not the centre of colour (the centre is a scalar phase; the cyclic permutation is non-central and its eigenstates are one quark's three colours); the step's symmetry is U(1) × U(2), with Z₃ an inserted subgroup; the model is three decoupled free walks with a circulant mass texture (three flavours, Harari–Haut–Weyers), not colour; the three was an input (n copies give Z_n for every n); the mass sign was unmeasured and is unobservable. The sentence above, "in the standard theory the thirds-shift is the centre of colour," is withdrawn. What carries forward: no shared internal flip can produce colour, self-coupling or confinement, since it commutes with flavour-blind hops; a route to the three needs a position-dependent non-commuting internal coupling, i.e. a gauge field. The moiré shape as stated is excluded; what remains of the author's idea is the question whether "two things turning against each other" can produce a *position-dependent* comparison, which this construction did not have.

## 2026-11-06 — shape: channels (parallel relations between two places)

The wall asks for something on a relation, differing from relation to relation, with three-way structure, that does not commute with itself. The lattice-formation ruling ("a place keeps about as many relations as its quanta can feed") does not say two places share at most one relation. If neighbouring places share k parallel relations (channels), a hop is "leave by channel i, arrive by channel j": a k × k matrix on the link, varying with the link because k does, and non-commuting around a loop. Which channel a pattern occupies is a label it carries; crossing a link can change it; relabelling channels freely is the gauge redundancy. Meets three of the four clauses from an existing ruling, without positing a label.

Not met: why k = 3. The number of channels per link would be set by how many relations a place's quanta can feed (capacity, δ), a number the rules speak about but do not evaluate. Caveat from the author's earlier program: channels give U(N) by uniqueness with N inherited; the bar here is whether the lattice-formation ruling sets N, not whether N gives SU(N).

First reading needed: does "sliding costs nothing" let channels be distinguishable at all? If sliding relabels them freely, the matching is convention (gauge, good); if it also erases the count, there is no k.

Aside: record on a relation. If a renewal retained its share on the relation crossed rather than at the place, record would be a position-dependent, accumulating link quantity; but a count, so abelian. A second ratio-like field at most; not a matching.

Grade: shape.

## 2026-11-06 — channels: the sliding reading, and what the existing rulings already give

**Sliding.** Relabelling places costs nothing and there is no backdrop. Relabelling the channels between two places is the same kind of act: free. It does not erase how many there are; the count is combinatorial, invariant under relabelling. So sliding leaves k intact and makes the channel labels a convention: that is the gauge redundancy, and it comes out right.

**The matching is already a ruling.** "A quantum's first passage through a place pairs the relation it came by with the one it leaves by, and transit keeps to its pairs" (the lattice-formation rule). With k channels on each link, a place's pairing of incoming to outgoing channels is a matching; with the amplitude rule (transit draws by frequency and can split), the matching is a k × k unitary on the link. Around a loop the matchings compose, and for k ≥ 2 the unitaries do not commute. So the link matrix is not a new object: it is the pairing rule applied to parallel relations. On a relation, position-dependent, non-commuting: three clauses from existing rulings, given k > 1.

**The count.** k = 1 gives a single phase per link, charge's field; k = 2 and k = 3 give U(2) and U(3) by uniqueness (the author's earlier program's result; standard; the determinant phases are the extra U(1)s already flagged). Nothing here selects k. The lattice-formation runs (R4, R5) cannot speak to it: both start from a simple graph, every pair related once, so parallel relations were excluded by construction, not by the rules. Whether a place's quanta feed several relations to the same neighbour, and how many, is an unasked question of the formation model, and it is where k would be set if it is set at all (capacity P_max, δ).

**Grade.** Channels: shape with three of four clauses met by existing rulings; the fourth (k) is an open computation on the formation model, not a silence of the primitives. First time the count sits in a model CO owns rather than in a label. Prior: the earlier program posited the multiplicity; here it would be computed or not.

**Next.** A formation run that allows parallel relations (multigraph), with the pairing rule, and reads off the distribution of k per link as a function of quanta per place. Outcome unknown; would change a ruling (whether k is set by the rules). To be registered if pursued.

## 2026-11-06 — R12: channels do not survive formation. Excluded.

Registered (`NUCLEUS_runs/R12_channels/`), unknown outcome. Four channels per pair at the start, thinning and pairing per channel: at q = 6, 8, 12 the surviving multiplicity is 1 on more than 99% of pairs, none with three; m₀ = 1 reproduces R5-B. The pairing rule locks each quantum to one channel, and thinning removes the rest. The channel shape is excluded as the source of the link matching in CO's formation model; k is not supplied and is actively driven to one. Changing the formation rule would be a new ruling, and the pairing rule is load-bearing (lines, R5; locality, R7). The wall stands as stated.

## 2026-11-06 — the count as falsifier; the failed routes as a map

Entered in `NUCLEUS.md`: the e⁺e⁻ ratio and π⁰ → γγ measure three carriers with charges ⅔, −⅓; any CO route giving another count is falsified. Author's standing note: keep the failed routes in view, since a wrong turn is often earlier than the failure; and the three is real enough to guide new readings. Routes closed to date, with where each turned: sorts (the count posited; three U(1)s); the Clifford four (carries only charge; Schur); the three lines (SO(3) ⊂ SU(3), not a factor); tiles with tile mass (tension falsified; gluons missing); three on one cycle (flavour, not colour; non-central Z₃; three an input); channels (formation drives k → 1 by the pairing rule). Common turn: each put a three-valued thing on the pattern or the place; the wall says it must be on the relation, position-dependent and non-commuting, and the one candidate on the relation was removed by the formation rules.

## 2026-11-06 — reading: what may a relation carry, and why only two things

**The two things.** A relation is read from either end. Any scalar on an ordered pair splits into a symmetric part (occupancy: how much) and an antisymmetric part (ratio: which way), and that split is exhaustive for a scalar. "Two things" is not a choice; it is what one number per link can be. To carry more, a relation must carry something that is not a scalar.

**It already does.** In the matter sector a hop across a relation acts on the four by that relation's line: P±_j = (1 ± α_j)/2. So a relation carries a three-valued label (which line) and a non-commuting action (the α's anticommute). With no backdrop, which line is "x" at a place is a free relabelling (sliding), so the matching of line labels across a relation is position-dependent and non-commuting: a matching on relations. The pairing rule ("transit keeps to its pairs") is its holonomy. The inventory therefore does contain one position-dependent, non-commuting matching on relations: the **frame** (which line is which). Its continuum form is the local frame freedom of gravity (tetrads; the spin connection), and it is the reason gravity self-couples. The wall statement "everything in the inventory is abelian" is corrected: the inventory has exactly one non-abelian matching, and it is the spatial one.

**Why it is not colour, said precisely.** Every three-valued thing in the inventory is a spatial vector: the three lines, the three α's, the three components of a relation's mismatch (two transverse, one along). Colour transformations must leave space alone (the SO(3) ⊂ SU(3) closure, now seen from the other side: SO(3) is the frame group, and colour is what commutes with it). Colour is a three-valued *spatial scalar* whose matching is *unitary* (complex, U(3)), not a rotation (real, SO(3)). A real internal triad, places with an inside, would give SO(3) again, not SU(3); the Kaluza–Klein line in the earlier bar is corrected on that point.

**The wall, final form.** The nucleus needs, on each relation, a three-component *complex* spatial scalar with a unitary matching. The inventory has, on relations, one real scalar (occupancy and ratio) and one real spatial vector matching (the frame); on patterns, one complex phase (charge) and the four. There is no complex three-component scalar anywhere. Channels would have been one (R12: removed by formation); a complex three-vector would be space's three (excluded). Nothing in two primitives is a complex scalar triplet.

**Where the turn was.** Not in the nucleus. It is at the amplitude rule: possibility in transit carries one complex amplitude. A relation carrying three complex amplitudes, with the rule for how they add, would be the object. Why one and not three is a question the amplitude rule (Goyal–Knuth–Skilling) answers for one system; it does not say a relation cannot carry a triplet, but nothing says it does. That is the earliest point at which the theory says "one" where the nucleus needs "three," and it is a silence, not a ruling. Any future route starts there.

## 2026-11-06 — reading: can transit carry a triplet of amplitudes, and what does the amplitude rule say

**What the amplitude rule fixes.** Goyal, Knuth and Skilling derive, from associativity of combination, conservation and scalelessness, that the amplitude of one route is a complex number and that routes in parallel add and in series multiply. It fixes the algebra of *one* amplitude. It says nothing about how many amplitudes a transit carries.

**What the internal-state ruling fixes.** Meyer forces a non-scalar internal state for a walk that moves; the Clifford count makes the smallest one the four. It is a lower bound. A larger internal space, the four tensored with a further factor, is admissible under every rule in the sector: each component is a GKS amplitude, components add componentwise, the Born identification sums the squares over all components, and a unitary mixing of the factor is a slide if nothing in the dynamics distinguishes the components. Nothing forbids an extra factor; nothing supplies one.

**Consequence.** "Possibility in transit carries a complex triplet" is admissible and unselected. It is exactly the thing the wall asks for: a three-component complex scalar on the pattern, whose matching across relations is unitary and, by carriers being patterns, self-coupling. Given it: U(3) by uniqueness (the determinant phase the extra U(1) already flagged), the gluon column (carriers carry the matching), confinement's shape. Not given: the three, or that there is any factor at all.

**The third primitive, final form.** *Possibility in transit carries a complex triplet.* Admissible under the amplitude rule, unselected by it, and the single posit from which the nucleus follows at the standard price. This is where six closed routes converge: each tried to find the triplet inside something CO already had (a place, a line, a tile, a copy, a channel), and the reading shows it can only be a factor of the internal state, which the rules leave open. By the bar in `NUCLEUS.md` it is not earned (cascades only to the hadron spectrum). By the method it is stated, costed, and left.

**Where that leaves the thesis line.** Two primitives to 1930, with the nucleus requiring one admissible, unselected addition to what transit carries. Unchanged in substance; sharper in statement.

## 2026-11-06 — the triplet entered as candidate ruling

Entered in `NUCLEUS.md` with its four ways to fail. The author's check, recorded: at three tiles a ruling would have been at the wrong level (a composite) and was shown wrong on reading; this one is the output of elimination (relation: formation removes it; place: real inside gives SO(3); transit: the only slot, and the amplitude rule is silent there), not of a nudge. Correctness beyond that is owed to a cold reading with the brief: same standing as CO's electromagnetism, or worse.

**Cold reading of the triplet; returned to shape.** The defence "same standing as electromagnetism" failed on four counts: the EM connection (the ratio) is posited while the colour connection was claimed; 1/137 is a parameter while three is the group (N indistinguishable amplitudes ⇒ U(N) is tautology); the extra U(1) of U(3) couples to quark number and is a long-range fifth force excluded at 10⁻⁴⁷ (Lee–Yang 1955), removable only by a further rule; and "transit carries a triplet," unscoped, colours the electron, so scoping it is sorts returning. "Self-coupling is not a second posit" withdrawn: the photon is a pattern and does not self-couple; the adjoint internal state is a posit. "One coupling" withdrawn: U(3) has two. Omitted costs added: the scale; det = 1; fractional charge (which the EM sector's "charge is a sign" cannot carry); flavour. The proton remains unbuilt even with all of it (spin-3/2 without flavour; statistics open; singlet rule a consequence of confinement; second-quantised gluons; mass a lattice computation). Prior art: Utiyama 1956; Lee–Yang 1955; Nambu 1966; Bardeen–Fritzsch–Gell-Mann 1973; Wilson 1974. The elimination to the slot stands; the re-costing did not. The wall is the sector's last word.

## 2026-11-07 — Bell's cost as a choice: inside one tick, outside two events (candidate)

After the now ruling, "one commitment increments the count at both ends" cannot mean "at the same time." Two readings, each a known price:

- **A. Two events, one stock.** Each end has its own commitment with its own past cone; what is shared is the pattern's possibility in transit, one stock, which each end's commitment engages. The joint outcome is correlated through the stock, not through an order; neither end is first. Tumulka's flash model (2006; interacting distinguishable case 2020/21). Cost: the count ticks twice; "one event" is given up.
- **B. One tick of the pattern's count.** A pattern's count is a clock; "same tick" is well-defined for one pattern across its places. A two-place commitment is one tick; the simultaneity belongs to the pattern, not to space. The Dürr–Goldstein–Norsen–Struyve–Zanghì foliation (2014) restricted to one pattern. Cost: a lawlike slicing, invisible to observables; and when two patterns with different counts engage, "whose tick" is undefined.

**Candidate position.** Both, by vantage: from outside, any other commitment sees two point events, unordered, with a covariant joint law (A); from inside, the pattern's own ledger records one tick (B). Consistent with the now ruling because the pattern's count is its own bookkeeping, not a statement about other patterns' commitments.

**Open: measurement, the interacting case.** The resolver is another pattern with its own count; the two ledgers must agree on one event. Open for every relativistic collapse theory. CO's one sentence toward it: a commitment resolves exactly what it engages, so the count that ticks is the one whose stock was resolved. Whether that settles whose tick or only names the problem is the question; not pursued.

## 2026-11-07 — mined from the author's earlier program: knots, braids, mass

Looked for knots and mass in the earlier corpus and the archived CO 1.0 note. Findings, with their caveats, for ideas only:

- **Nothing there relates knot size or type to mass.** The earlier program's own card says so in those words; a knot's top speed scaling as 1/N was flagged there as a resemblance to "heavier is slower," not the relativistic relation. Not a lead.
- **"A particle is a moving pattern" (author's ruling in that program, 2026-10-03):** it is wherever its pattern of commitments is, and moves as a wave does, the places staying put. Same content as today's reading that a pattern never commits at the same place twice. Already CO's.
- **CO 1.0's braid note:** particles as closed braids of three renewing commitment chains (Bilson-Thompson 2005's helon model is the prior art: charge as twist), with Koide's relation read off a three-strand renewal operator, and an argument that three is the only strand number where the braid group is non-abelian with no two generators commuting (B₂ is abelian; B₃ the least that is not). Caveat that decides it: braid structure belongs to exchange in two spatial dimensions; in three, the configuration-space fundamental group is the permutation group and braids collapse (the earlier program's own anyon-prohibition paper, Leinaas–Myrheim). So a braid-based three would need the strands to live in an internal two-dimensional space, which is a posit of exactly the kind the wall names. Noted, not reopened.
- **Moiré in light (Nature Light Sci. Appl., 2026, "freespace twistronics"):** two structured beams overlaid at an angle produce polarization knots neither has, including topologies not seen elsewhere. The sharper form of the author's moiré question is therefore "can two abelian things turned against each other produce a knot," not "a three." Noted only.
- **The ground under matter:** relations persist only while possibility passes through them, and a pattern never commits at the same place twice, so the relations under a massive pattern are made and unmade at its renewal rate. Whether that is the pooling rule in other words or a sentence of its own is unread; the pairing rule and the renewal rule are the two to read together.

All noted; nothing entered as candidate.

## 2026-11-07 — consistency sweep of the results documents against the record

Twelve places where a results document still carried a sentence that a later entry had superseded, or a grade the record had changed. All corrected; no content changed. Grade words: three-tile patterns are shape, not candidate (README); entanglement is candidate, not ruling (NUCLEUS, plain doc); the two doubler rulings are candidate (MATTER opened "two rulings"); charge carries its grade in README and the plain doc; "lead" removed (NUCLEUS, sorts costing). Superseded sentences: the Kaluza–Klein line in the bar now carries its 11-06 closure (real inside gives SO(3)); the wall paragraph's "one coupling" now agrees with the triplet's posit (iv); the wall paragraph lists six closed routes, adding R11 and R12, which had been in the record only; the plain doc's "buys exactly SU(3)" is now U(3) with the ninth vector. Overclaims: "takes no physics as input" is now "no physical law"; measured constants and the two experimental exclusions (scalar wave; one-way hop) are itemised under "What goes in"; README's "two constants" is three, matching the gravity doc's Constants. Method: the dated outside-reading line and its correction-history sentence removed from the plain doc; the reading itself is the 11-05 entry above. Pattern: each correction had been entered at its own point and the sentence it superseded left standing nearby.

## 2026-11-07 — Bell, the interacting case: "whose tick" read against the now ruling (clarification; the open item relocated)

**The open item as posed.** The resolver is another pattern with its own count; "the two ledgers must agree on one event." Open for every relativistic collapse theory.

**The reading.** The item assumes a ledger the two patterns share. The now ruling says there is none: a count belongs to a pattern, and "what has committed" is defined per commitment by its past cone. So the question is answered by the rules already on the board, one tick per ledger, each for its own reason:

- The detector D commits. Its count ticks by one because *it* committed: a local, definite event with its own past cone. This renewal engaged not free possibility but the pair's possibility in transit (a measurement, by the rule that a commitment resolves exactly what it engages).
- The pair P's count ticks by one because *its* stock was resolved. One stock, one cut, one tick in P's own ledger, across both of its places (reading B of the entry above, inside the pattern).
- The far detector D′, when it commits, ticks its own count, for the same reason D did.

One physical fact, the cut of P's stock, recorded in three ledgers. The requirement "agree on one event" is replaced by "record one cut," and that is supplied: D's and D′'s commitments are each an engagement of the same undivided stock, so what they record is the stock's one outcome, not two outcomes to be reconciled. From any other commitment's vantage, D and D′ are two spacelike point events with a joint law through the shared stock (reading A); the interacting case adds no new vantage.

**What this changes.** "Whose tick" was misposed: it asked for an order between two counts that the ruling says have no common time. The cost that remains is the one already stated for the non-interacting case, A and B by vantage, and it is not increased by the resolver being a pattern.

**Costs, stated.** (i) The joint law (Born for the pair, covariant) is inherited, not derived; CO adds the location of the cut, not the law. (ii) "One stock, cut once" is doing the nonlocal work; its covariance rests on a stock being the pattern's, not a place's, which is a reading of the rules (candidate in the entry above), not a derivation. (iii) In D's ledger the chance that a given renewal lands on P's stock rather than free possibility is the possibility there, by the Born identification; what "the possibility there" means for an extended pattern in D's frame is unread. (iv) This answers the two-pattern case; a chain of resolvers (D measured by E) is the same answer repeated, each ledger ticking for its own commitment, but has not been written out.

**Grade.** Candidate: a dissolution of the open item by a ruling already made, with the costs above. Enters `NUCLEUS.md` and `OPEN_DIRECTIONS.md` after a cold reading.

**Cold reading, same day; regraded from dissolution to clarification.** One gain stands: "the two ledgers must agree on one event" did assume a shared ledger, and counts are per pattern, so no shared tick is owed. The rest relocated the open item rather than closing it. Corrections:

- *Reading B is a definition, not a slicing.* P's "one tick across both places" has no past cone of its own: at D's event nothing has happened to P in D′'s past cone, and symmetrically, so the tick is the count of cuts, which is one by the definition of one stock. The entry escaped the now ruling by exempting P's count ("its own bookkeeping"); an exemption is not a reconciliation. Stated honestly, B carries no physical content beyond A and no foliation cost either; all the physics sits in A.
- *"Already in the rules" was the wrong tone.* The rule doing the work, "engaging it anywhere resolves it everywhere" (11-05), is a nonlocal postulate with no signal, entered as a candidate reading, not a consequence of commitment being local. The entry equivocated between D engaging the whole stock and only the local part; it is the whole stock, and that must be named as the postulate it is.
- *The interacting case does add cost.* (iii) is not small: the stock "flows to where it was engaged" is process language across spacelike separation, and a process has frame content; either the flow is not a process, or it needs a hypersurface. The form consistent with the now ruling is Tumulka's: the stock at D's event is P's stock conditioned on the commitments in D's past cone. Candidate reading, not yet entered. (iv) is where the difficulty lives, not a formality: after the cut, D and P share a stock, so what later engages D engages both; this chain is where Tumulka's interacting construction needed the multi-time wavefunction and was restricted to distinguishable particles at fixed number.
- *Wording.* "This renewal engaged … the pair's possibility" clashes with the 11-05 rule (a renewal is by definition an engagement of free possibility; a measurement is a different commitment). "From any other commitment's vantage" should read "for any commitment with both in its past cone."
- *Attributions, here and in the entry above.* Dürr–Goldstein–Norsen–Struyve–Zanghì 2014 propose one global foliation fixed covariantly by the universal wavefunction, for Bohmian mechanics; there is no per-pattern foliation in that paper, and "restricted to one pattern" is CO's own move (it is what generated "whose tick": two per-pattern foliations crossing). Bedingham et al. 2014 is the collapse version. "Open for every relativistic collapse theory" is too strong: a general interacting law is open; Tumulka's exists for distinguishable particles at fixed number.

**Standing.** Clarification under the Entanglement candidate: no shared tick is owed. The open item is relocated to (i)–(iii): what P's stock is at D's place when D engages it, and why two spacelike engagements of one stock give one outcome covariantly; both inherited from standard quantum mechanics, not supplied by the rules. Entered in `NUCLEUS.md` and `OPEN_DIRECTIONS.md` in that form.

## 2026-11-07 — Bell: the now ruling applied to the stock; CO's account is the flash-type one (candidate)

**The step.** The relocated open item asks what the pair's stock is at the detector's place when the detector engages it (iii), and why two spacelike engagements of one stock give one outcome covariantly (ii). The now ruling already says what "has happened" for any commitment: its past cone. Applied to the stock, that is one sentence:

*For a commitment, the stock it engages is the pattern's possibility in transit given the commitments in its past cone.*

For D, D′'s spacelike event has not happened; for D′, D's has not. Each engages the stock as it stands for it. This is Tumulka's conditioning prescription (rGRWf), and under the now ruling it is not a choice but the only reading: a foliation (one slicing for all commitments) would be a now the ruling does not have.

**What follows.**
- *Reading B is withdrawn, not kept by vantage.* "One tick across both places" named the pair {D, D′}; it had no cone. CO's account of Bell is reading A alone: two point commitments, one stock, a joint law.
- *The flow language is withdrawn.* "The pattern's stock elsewhere flows to where it was engaged" (11-05) described a process across spacelike separation, which has frame content. Nothing flows. The stock is one; each commitment engages it as it stands in that commitment's past cone; the far end's stock is conditioned on D's event only for commitments with D in their past. What stays in the relations after release (the ratios set, the record retained) is unchanged.
- *The joint law.* The outcomes at D and D′ are not two draws in sequence; there is no sequence between them. They are one draw from the joint law on the one stock (Born for the pair). Order-independence is the fact that engagements at different places act on the stock's components at those places, so two spacelike engagements commute: D-then-D′ and D′-then-D are the same cut. That is tensor-product locality of the engagement, standard quantum mechanics, inherited.

**What CO supplies and what it inherits.** Supplied: *where* the cut is (a commitment, local, definite); *for whom* a cut has happened (past cone, the now ruling); and that the two paying options reduce to one (A). Inherited: the joint law (Born on the pair) and the commutation of spacelike engagements. "CO has not chosen" (plain doc) is no longer accurate: the now ruling chooses the flash-type account.

**Costs.** (i) The joint law is an input, as it is for Tumulka. (ii) Commutation of spacelike engagements is inherited; CO has no rule from which it follows, and a rule for it would be locality of engagement, a candidate at most. (iii) The interacting chain (D's pointer and P share a stock; what engages D engages both) is where Tumulka's construction needed a multi-time wavefunction and is restricted to distinguishable particles at fixed number; CO's "one stock" is the same object under another name and has the same restriction until shown otherwise. Not pursued.

**Grade.** Candidate. If it stands: `NUCLEUS.md` and the plain doc say CO's account is the flash-type one, selected by the now ruling, with the joint law and the commutation inherited; "both, by vantage" and "has not chosen" come out.

**Cold reading, same day; enters corrected.** Candidate for the shape (two point commitments, one stock, one joint law, each commitment engaging the stock as it stands in its past cone). Not as "the now ruling forces this and excludes a foliation." Corrections:

- *The foliation exclusion is a posit, not relativity's.* The now ruling was graded *ruled* because it adds nothing beyond relativity (Stein 1991; Rideout–Sorkin), and Stein's theorem says nothing about a slicing fixed by the *state*. DGNSZ 2014 and Bedingham et al. 2014 make exactly that move, covariantly; relativity does not exclude it. So setting a state-fixed foliation aside requires reading the ruling's third clause exhaustively (nothing spacelike is ordered, state-fixed or not), and that reading is CO's own, priced here. Withdrawing B (CO's per-pattern slicing) does not touch the real foliation accounts; the entry conflated the two.
- *The logic was inverted.* In Tumulka the joint law is primary and the past-cone-conditioned state is a derived, consistent description made possible by commutation. Conditioning on past-cone commitments yields marginals; it does not produce the correlation. The conditioning is CO's reading of what each commitment engages; the correlation lives entirely in the inherited joint law. And "Born for the pair" is not rGRWf's law (GRW's is Gaussian collapse at rate λ, width σ, with the cut at the pointer's many flashes); CO adopts the *structure*, not the dynamics.
- *Commutation is necessary, not sufficient.* [A⊗1, 1⊗B] = 0 gives order-independence of the joint probability and post-state. Covariance of a flash account also needs covariant transit between commitments, a covariant rule for *when* a commitment occurs (Tumulka: hyperboloids from the seed; CO: the per-pattern renewal clock, a lattice rule), and in the interacting chain a consistent multi-time state, since D engaging P is an entangling evolution, not a commutation of collapses. And Tumulka's model is exactly Lorentz-invariant in the continuum; CO's walk has a physical hop, so "covariant joint law, inherited" holds in the continuum limit only. Covariance is emergent and must be said so.
- *Withdrawing the flow broke the 11-05 reading unless replaced.* "The ratios on the relations it used are set by that flow" was load-bearing. Replacement, from the gravity rule as reworded 11-07 (net transit on each relation toward the end that engages more): ratios on D's relations are set link-locally by D's engagement, on D′'s by D′'s; the correlation between them is in the joint law, not in anything travelling. Link-local transit stays; cross-spacelike flow goes. Record retained unchanged.
- *"Supplies" overclaimed on two of three.* The cut's location is *located* by the 11-05 candidate reading (a commitment engaging in-transit stock), and what the pair's possibility is at one place is the marginal, standard quantum mechanics, unread in CO's terms. "For whom it has happened" is supplied, and is relativity's. "Two options reduce to one" is CO's selection under the exhaustive reading, not a derivation.

**Standing.** Candidate (shape of the account). Entered in `NUCLEUS.md`, the plain doc and `OPEN_DIRECTIONS.md` in the reader's wording: CO's reading of the now ruling selects the flash-type shape; the joint law, the commutation and the marginal are inherited; the foliation option is set aside, not excluded; covariance emergent; the interacting chain open.

## 2026-11-07 — the interacting chain, read against the rules: short at the cut, open before it (candidate)

**The question as left.** After a detector D cuts the pair's stock at L, D and the pair are said to "share a stock," so what later engages D engages both; this chain is where Tumulka's interacting construction needs a multi-time wavefunction and stops at distinguishable particles at fixed number.

**At the cut, the chain is one step long.** In CO a measurement is a commitment: definite, irreversible, retaining one quantum's share as record. There is no stage at which D's pointer is in superposition with the pair and waiting for a later collapse; the engagement *is* the collapse. So D's record carries the outcome as a definite fact; D's subsequent renewals engage free possibility and resolve nothing; a later E engaging D engages a definite stock. The multi-time problem does not arise at the cut, because the two-stage account (unitary entangling, then collapse) that creates it is not CO's account. "D and the pair share a stock after the cut" was standard quantum mechanics' description imported; under the rules there is no shared stock after a commitment.

**The weight moves to before the cut.** The same rules that make the chain short make a different question load-bearing: *which contacts are engagements (a commitment taking a quantum of another pattern's in-transit stock: irreversible, a cut) and which are routes (a pattern hopping on ratios another pattern has set: coherent, no event)?* The record has three readings and they do not sit together:

- Refraction: light hops on the glass's clock field; route, no event (11-05, holds).
- Elastic scattering of two electrons: "both are resolved, directions decided" (11-05, holds as a reading).
- Charge: a pattern hops on the which-way ratio, a 1-form on relations, a property of place; Coulomb scattering is therefore a route on the other pattern's field.

The second and third describe the same contact and give opposite answers. If every contact of two patterns were an engagement, no two interacting patterns would ever be coherent together: no bound two-electron state with correlation, no interaction-made entanglement. Observation decides this one: the helium atom. Two electrons on each other's c-number field give the mean-field (Hartree) energy, −77.9 eV; the measured ground state is −79.0 eV; the 1.1 eV difference is correlation, a property of a *two-electron* amplitude (Hylleraas 1929, within the period CO claims). So the third reading as stated, two patterns each walking on the other's ratio field, is mean-field and is excluded by helium at the 1% level; and the second reading, resolution at every contact, is excluded by the same atom (the electrons do not decohere each other).

**What the rules lack.** A rule for two patterns' walks coupled *coherently* through their fields: a two-pattern stock whose amplitude depends on both positions, with the ratio field acting as the coupling rather than as a c-number backdrop. In standard terms, the two-body Schrödinger equation with Coulomb coupling. Without it CO has one-particle quantum mechanics in external fields (Dirac 1928) and no many-body quantum mechanics (Heisenberg's helium 1926, Hylleraas 1929). This is the same gap as "how do two patterns become one stock" (entangled pairs are now born as one; they cannot be made by interaction) and the same gap as the interacting chain, in its oldest and simplest form.

**Grade.** Candidate finding. If it stands: (i) the 11-05 elastic-scattering reading is withdrawn as inconsistent with the charge sector; (ii) `MATTER.md`'s Open list and `OPEN_DIRECTIONS.md` gain a line: the two-pattern problem, a coherent coupling of two walks through their ratio fields, is not in the rules; mean-field is excluded by the helium ground state; interaction-made entanglement and the criterion for engagement versus route wait on it; (iii) the README's "physics to 1930" is read as one-particle quantum mechanics and is scoped accordingly, since the many-body equation is pre-1930 and not reached. The interacting chain is not harder than this and not easier: it *is* this.

**Cold reading, same day; enters corrected.** The finding stands: the interacting chain reduces to the missing two-pattern coherent coupling; the mean-field reading is the only one the rules as written give, and helium excludes it; the 11-05 elastic-scattering reading is wrong and is struck. Corrections:

- *The problem is relocated, not avoided, and both halves go in one sentence:* the multi-time problem does not arise at the cut; it arises before it, as the covariant coupled walk of two patterns, which the rules do not have. GRW's difficulty was never the definiteness of flashes but covariant interacting evolution between them.
- *The rules are silent, not negative.* "Under the rules there is no shared stock after a commitment" → the rules give no shared stock: hold-and-release returns P's engaged possibility to P's transit and D retains record; a joint D–P stock is not an object the rules define, before or after. D's record and P's remaining transit are classically correlated, which is not a joint quantum stock. A stock is never "definite"; a record is: E engaging D later finds D's *record* of the cut definite; D's own transit is still a pattern, and engaging it is a further cut.
- *Hidden dependence named:* "a measurement is a commitment" treats a macroscopic detector's record as one engagement of one quantum; nothing in the rules says why one engagement constitutes a stable macroscopic record. Not new; this entry leans on it.
- *Helium, said precisely.* E_Hartree(He 1s²) = −2.8617 Ha = −77.87 eV (Hartree equals Hartree–Fock for the closed shell); exact non-relativistic −2.9037 Ha = −79.01 eV; measured I₁ + I₂ = 79.005 eV; correlation 1.14 eV, 1.4% (not "1%"). The singlet spatial part is symmetric, so exchange does not enter and the 1.1 eV isolates Coulomb correlation cleanly; the statistics silence does not confound the test. "Excluded by helium" is earned for the *reading*, not for the project: the rules do not forbid a configuration-space object, they lack it. A field at x depending on the other pattern's position as a variable is the two-body operator on configurations (x, y), not a 1-form on relations.
- *The witness against "resolution at every contact"* is Mott interference between direct and exchanged amplitudes in e–e and α–α scattering (Mott 1930), coherent scattering observed; "the electrons do not decohere each other" was loose. Helium's binding is the witness against mean field.
- *Withdrawing the 11-05 scattering reading* removes the only worked example of a pattern–pattern engagement other than a detector, so the rule "a commitment that engages possibility in transit resolves that pattern" is left with no stated criterion for when it applies; "a measurement is contact" becomes false as stated. Both amended in the 11-05 entry.
- *"No many-body quantum mechanics" overstated.* P8 is already used on two-pattern configurations {x, y} in the statistics item (direct and exchanged routes); the record has a two-pattern amplitude on configuration space in embryo, free and identical, with no coupling and with P8's premises not re-derived on configurations. The gap is the coupling of two walks through their ratio fields.
- *Scoping "physics to 1930."* Schrödinger's 1926 equation was already N-body on configuration space; Heisenberg 1926 (ortho/para helium), Heitler–London 1927 (H₂), Hylleraas 1929 are all within the period. The sentence sits in four places (README ×2, NUCLEUS.md, plain doc) and all four take the same scoping: gravity and the one-particle sector of quantum mechanics.
- *"A property of place"* for the ratio → a property of the relation (MATTER.md puts it on relations).

**Standing.** Candidate finding. Entered: MATTER.md Open gains the two-pattern problem; OPEN_DIRECTIONS gains it under Matter and the Entanglement open clause points to it; NUCLEUS.md Bell clause likewise; the four "to 1930" sentences scoped; the 11-05 scattering reading struck with reason.

## 2026-11-07 — entanglement wording made single: two events, one stock

The Bell paragraphs in `NUCLEUS.md` and the plain doc said two things that cannot both stand: "two separate events, each finding the pair's possibility given its own past" and "one event increments the count at both ends." The second was reading B, withdrawn earlier today (no past cone of its own; no content beyond "one stock has one cut"), and left standing in the prose. Struck; the paragraphs now say: one stock, cut once; each end's commitment its own event, finding the stock as it stands in its own past cone. "A pattern sampled twice" survives as a description of the stock, not of the event. This is also what the no-signalling of the semiclassical back-action rests on (gravity record, same day): the local source stays the unconditioned marginal until the far event is in the local past cone. Falsifier wording in `SPACE_AND_GRAVITY.md` set as the author asked: if two masses become entangled through gravity alone, CO is wrong, not downgraded.

## 2026-11-08 — quarks commit: two kinds of commitment, gluons as colour on relations (the author's working picture, shape)

**The picture, in the author's words tightened.** A quark is a pattern that renews, as an electron does, but of a second kind; the "tile that never commits on its own" is dropped. Ordinary matter is two kinds of commitment: leptons and quarks. Gluons are patterns of the colour field on relations, as light is of the which-way field; the relations exist between any places, with or without quarks; a gluon's colour content is that of a quark–antiquark pair minus the singlet (the octet).

**Against the rules.** Mass is renewal frequency (C2, C4); quarks carry a mass parameter (current masses a few MeV for u, d, scheme-dependent; no pole mass for a confined quark), so by the table they commit; their renewal makes up ~1% of the proton's mass, and their standing as patterns cannot rest on that mass alone, since with massless quarks QCD still confines and the proton keeps most of its mass. The tile notion was introduced to account for confinement and never did; dropping it costs nothing on the books and leaves confinement owed to something else, which is the honest standing. "Two kinds" matches the standard split, leptons and quarks; what separates the kinds is colour, and the count three is not dropped (measured independently by the R-ratio, π⁰ → γγ, and the Z's hadronic width; the falsifier of every nucleus route). Tightest form: *two kinds of commitment (each in three generations, unselected); the second carries a three-component colour state, and its relations carry a 3 × 3 matching between those states.* That is where the wall puts it (the matching on a relation, position-dependent, non-commuting); weak isospin and anomaly cancellation, which tie the two kinds together through N_c = 3 and the fractional charges, are not in it.

**Gluons.** "Gluons are quarks" (the author's first wording) as an identity conflicts with data: gluons are massless, spin 1, and carry about half a proton's momentum (deep-inelastic sum rules; three-jet events at PETRA, 1979). As "the colour carried on the relations between quarks," it fits: a gluon's colour content is a quark–antiquark pair's (3 ⊗ 3̄ = 8 ⊕ 1, the octet), and the move is the one CO already makes for light (the travelling part of the which-way field on relations). The relations' colour field can exist with no quarks present, as the which-way field radiates with no charges present; pure-glue confinement (lattice pure gauge; glueballs, a lattice prediction) then does not contradict the picture, as it contradicted "tiles with tile mass"; nor does the picture reproduce it, since that needs the field to act on itself (three- and four-gluon vertices), which comes from the non-commuting matching and is not supplied. Free light does not interact with itself; free glue does, and that is where the analogy with the which-way field stops. What the picture does not supply: the three, the non-commuting matching on relations, confinement. Those are the wall, unchanged.

**Dark matter, a third chapter of threes (the author's).** If dark matter is matter, the kinds of commitment are leptons (charged leptons carry a sign; neutrinos carry neither sign nor colour and interact only weakly), quarks (sign and colour), and dark matter, which would have to differ from neutrinos as well (heavier, colder, or without even the weak interaction). Shape, as the dark-matter reading already is; no number attached.

**Grade.** Working picture, shape. It reorganises the nucleus vocabulary (tile retired; kinship becomes the colour-carrying relation) without moving the wall. Not entered in `NUCLEUS.md`; entering it requires retiring or regrading the three-tile sections there and in the plain doc ("a quark is not a pattern") in the same commit, and replacing "tile" with "quark" in the wall.

## 2026-11-08 — the range of a force as renewal cost (identification)

**The author's idea, tightened.** A force reaches far when whatever carries it does not renew, and stops short when the carrier must renew, each renewal costing along the way.

**Against the rules.** Light does not renew (no mass), so the which-way field falls off as 1/r with no end. The force between nucleons is carried by pions, which have mass and so renew; a renewing carrier's amplitude to reach distance r falls as e^{−r/λ}/r with λ = ħ/(m_π c) ≈ 1.4 fm, the nuclear range: Yukawa's construction, in the table's words (mass is renewal rate, C2). It is the carrier's renewal rate that sets the range, not crowding of the capacity P_max: an exchanged carrier has no energy to spare, so one with mass can be present for only about one renewal time, ħ/(mc²), and reaches about ħ/(mc). (A real pion, not exchanged, travels metres before it decays; the range is a property of exchange.) Cleaner case, elementary carrier: W and Z, range ħ/(m_W c) ≈ 2.5 × 10⁻³ fm; the pion's own size (~0.66 fm) is comparable to its range, the edge of the picture.

**Limits.** This is the force *between* nucleons, carried by a composite. The force *inside* them (between quarks) does not fall off: beyond a few tenths of a fermi it is constant (~1 GeV/fm) while the energy grows linearly, until a quark–antiquark pair forms and the string breaks (~1.2 fm). That is confinement, behind the wall. The nucleon–nucleon force is a leftover, colour-neutral force, and one-pion exchange is only its long-range tail (two-pion and σ exchange give the middle-range attraction, ω the short-range repulsion).

**Grade.** Candidate, by identification (Yukawa 1935, recognised in CO's terms); no new rule. Enters the plain doc as a sentence after a cold reading.

**Cold reading of both entries, same day; corrected before push.** Quark mass cited as a parameter, not a pole mass, with the chiral limit noted (QCD confines and the proton keeps most of its mass with massless quarks); the miscount fixed (the quark carries the three-component colour state, the relation carries the 3 × 3 matching: lattice quarks on sites, SU(3) on links); "Z width" corrected to the Z's hadronic width (the Z width counts light neutrinos). Gluons made patterns of the colour field, consistently with photons as patterns of the which-way field (the first wording, "no separate gluon pattern," conflicted with NUCLEUS's photon). "Does not falsify" softened to "does not contradict, nor reproduce": pure-glue confinement needs self-coupling, which the picture does not supply. Dark-matter triad redefined so it is not the neutrino; "a third chapter of threes" dropped. Yukawa: the mechanism restated (an exchanged carrier borrows mc² for about one renewal time), the inside-nucleon force corrected (it grows with distance until the string breaks), W and Z added as the cleaner elementary case. Pair creation: all additive charges, not electric charge alone (γ + p → n + π⁺ makes a neutron without an antineutron); a second body takes up momentum.

## 2026-11-08 — quarks commit entered in NUCLEUS.md (shape), tile sections retired; cold reading applied

"Three-tile patterns" replaced by "Quarks and gluons" in `NUCLEUS.md`, the plain doc, README and `OPEN_DIRECTIONS.md`. Cold reading corrections applied: the section contradicted itself (it granted an SU(3) matching and then listed "the non-commuting matching" as missing; what is missing is the matching as a dynamical object, posit (ii), from which the octet and self-coupling follow by the transformation law); the wall still put the triplet on the relation (it belongs on the quark, the 3 × 3 matching on the relation); "the force grows with distance" corrected (a linear potential is a constant force, ~1 GeV/fm; the energy grows), here and in the record; a = ħc/√σ ≈ 0.45 fm; "follows from the table" softened to "is read from"; "two kinds" stated as a split by colour, with the weak interaction and neutrinos named as not in CO; the dark-matter bullet now excludes the neutrino explicitly.

## 2026-11-09 — the colour field read again against the cascade bar, with the gravity sector's new debts (reading, after cold reading)

**Why it is asked.** The wall's standing (`NUCLEUS.md`, "The triplet") is that the colour posit is not earned by the cascade bar. Since then the gravity sector's interior-source entries (gravity record, 2026-11-08: pressure, binding, self parts) and the matter record's sea entry named debts that seemed to point at the colour field: (1) the gluon field's trace (QCD's trace anomaly), most of a nucleon's mass, must draw as turning for a nucleon's active mass to be right; (2) nuclear binding must satisfy active-equals-passive (Kreuzer 1968; Bartlett–van Buren 1986); (3) the lunar-ranging bound sits mainly on nuclear electrostatic energy balanced by strong-force stress; (4) the pressure rule's field clause has a colour half. In chat these were counted as four debts the colour posit would pay. The question: does it pay them, and does that change the bar's verdict?

**What the posit is, in CO's terms (unchanged).** (i) Some transit carries three indistinguishable complex amplitudes (which patterns, posited); (ii) relations carry a dynamical 3 × 3 unitary matching with a quadratic cost; (iii) unit determinant; (iv) a second measured input, the scale Λ. With them Yang–Mills is the unique quadratic cost, classical.

**Debt by debt.**
- *(1) The gluon trace.* T^μ_μ = (β(g)/2g) G^a_{μν}G^{aμν} + Σ m_q(1 + γ_m) q̄q. The first term is a quantum effect: classical massless Yang–Mills is traceless. It needs the gluon field second-quantised, a running coupling, and loops. None is in CO ("no field in CO is second-quantised", `NUCLEUS.md`), and loops on CO's lattice meet the Lorentz exposure (matter record: O(α/π) species-dependent speeds, here O(α_s/π)). Posits (i)–(iv) are necessary to pay this debt from beneath (not to take the nucleon's mass as an input), and not sufficient.
- *(4) The pressure rule's colour clause.* The same object: the nucleon's source is ∫(ρ + S) = ∫ρ = ∫T = M (∫S = 0, von Laue, for the total stress), and T is mostly the anomaly (the quark-mass σ terms give of order 10%; a statement about the trace, not about other decompositions of the mass). Not a separate debt.
- *(2), (3) Nuclear binding and lunar ranging.* One debt, (3) being its sharpest test. At the scale of nuclei the binding is carried by the nuclear force, described without colour by meson exchange with measured masses and couplings (pions at long range; two-pion, σ and ω exchange, or contact terms, at middle and short range): routes through added patterns, where the rules are silent (matter record, the sea). The electrostatic part between protons draws through the field-energy posit (candidate posit, conditional on closure, which is shape), and the pressure rule is shape. Colour enters only beneath the nucleon and the mesons, through those measured inputs (under the quarks-commit shape the pion is a quark–antiquark pair whose lightness comes from chiral symmetry breaking, which CO's Wilson walk breaks explicitly).

**So the count was wrong.** The four debts are two: the nucleon's internal source ((1) = (4)), and a nucleus's binding ((2), with (3) its sharpest test), which belongs mainly to other open items. The colour posit does not pay the first: it is needed to derive it from beneath, with second quantisation and loops (and so the Lorentz exposure) also required. The chat claim that the colour field "pays four debts" is withdrawn as an overclaim.

**The bar's verdict.** Unchanged. In the standard theory, colour with quantisation cascades to the hadron spectrum; in CO even posits (i)–(iv) leave the proton unbuilt ("The triplet"). The nucleon's gravitational source is that same cascade seen through gravity (with a gravity-side clause, that a field's trace draws as turning), not a second open problem. The colour posit's wider content (confinement, the spectrum, the proton's spin) is the cascade already counted, and equally needs quantisation; the fractional charges it does not pay. Gravity-side debts are open items, not among the three open problems the bar names (the masses, 1/137, colour); the verdict holds either way. Not earned.

**What gravity for dust assumes.** It takes the nucleon's measured mass as input, drawing as if one pattern renewing at mc²/ħ, which assumes the nucleon closed; that assumption is debt (1) taken on, not paid (gravity record, self parts: closure for nucleons takes on the gluon clause; under the quarks-commit shape the quarks' own renewals are about 1% of the mass). A universal error in the nucleon's draw would rescale G, so dust alone does not test it; composition-dependence (aluminium against iron) enters through binding fractions, where debt (2) sits.

**What lies beneath.** Traceable in the records: beneath the gravity, matter and nucleus debts recur (a) a rule for routes through added patterns and (b) second quantisation of a field, which are largely one (number-changing configurations, for patterns and for fields); (c) loops on the lattice, the exposure they bring once a vertex exists; and also the vertex itself, the exchange sign, chiral symmetry on the walk, and closure. The colour posit sits on top of all of them. Assessment, not a reading: each of (a)–(b) recurs under more open items than colour does; whether filling either would cascade is not shown (the sea entry: not yet), and the bar, stated for a third primitive, is here extended to rulings that fill silences.

**Cold reading, same day; corrected.** The anomaly formula completed (γ_m); "mostly the anomaly" qualified; nuclear binding read through the full meson-exchange force, not pions alone, with colour beneath nucleon and mesons; four debts are two, not three; the bar applied on even terms (the spectrum and the nucleon's source are one cascade, both needing quantisation); the dust claim corrected (measured nucleon mass assumes closure, debt (1) taken on; dust alone cannot test it); "necessary" narrowed to deriving from beneath; the roots' overlaps and missing items added and the comparative sentence marked an assessment.

**Grade.** Reading. The colour posit remains not earned; the count of four debts is withdrawn (two debts: the nucleon's source, for which colour is needed from beneath and not sufficient, and a nucleus's binding, which belongs mainly to the sea's silence and the field-energy posit). Nucleon closure joins elementary closure as an assumption gravity for dust makes.

## 2026-11-12 — price list: an on-site internal label (reading, for the author's decision; not ruled)

**Why now.** The 12 Nov particle thread (MATTER-side notes, `OPEN_DIRECTIONS_notes/how_patterns_combine.md`) narrowed colour, the weak interaction and the up–down charges to one missing piece. A gauge field couples consistently only to a label that acts at each place by itself (on-site; Wang–Wen; DeMarco–Wen). The labels CO's walk does have, its doublers' corners and tastes, are tied to momentum (the twist), so they can supply a generation's count but not its charges. The missing piece is an internal label at each place. The 9 Nov verdict (colour posit not earned) is read again below with what has changed since.

**The posit.** Each place carries, for matter in transit, an internal label space: amplitudes with a colour index (three values) and, for the left-handed parts, a kind index (two values). Relations carry the matching unitary for each, with a quadratic cost. Charges are then set by consistency, not posited one by one.

**What it would buy (cascade).**
1. *Colour as a gauge field* (SU(3) on relations): the 9 Nov posits (i)–(iv), now with an on-site home.
2. *The weak interaction's form*, now a silence: SU(2) on the left-handed kind label, the paired kind flips (Fermi's form, a shape since 12 Nov), with handedness allowed but not chosen.
3. *The charge values.* With exact gauge invariance, anomaly cancellation forces Q_u = ½ + 1/(2N_c), Q_d = −½ + 1/(2N_c), Q_ν = 0, Q_e = −1. With N_c = 3: +2/3, −1/3. The 9 Nov reading said the colour posit "does not pay the fractional charges"; with the kind label beside it, it does.
4. *Atoms neutral* to the measured 10⁻²¹, for any odd N_c, with nothing added.
5. *N_c odd* (Witten's global anomaly), matching the condition under which Skyrme's twisted baryon is a fermion (the baryons-as-twists shape).
6. *If one-handed fields come by mirror gapping* (symmetric mass generation): sixteen Weyl fields per generation, so a right-handed neutrino. This is a consequence of the route, not forced for the Standard Model group alone.

**What it would cost.**
- *The sizes by hand:* three colours, two kinds, and a hypercharge unit. The label space is imported, not derived; "three as dimension" does not supply it, since the on-site rule separates internal labels from directions of space.
- *A third kind of thing in CO:* an internal space at each place, beside possibility and commitment. Whether that is a third primitive or a quality of possibility in transit is itself a ruling.
- *Quantisation and loops,* which colour's cascade to the hadron spectrum needs (9 Nov). Number change is now ruled (C6: the walk as a field), so second quantisation is partly in hand. Loops bring the frame problem's exposure at O(α_s/π), much larger than electromagnetism's O(α/π).
- *A one-handed field on the lattice:* by Ginsparg–Wilson fermions (exponentially local; the locality ruling allows them; non-abelian established only to all orders in perturbation theory), or by mirror gapping (on-site; non-perturbative in 3+1D not yet shown). Either way an open problem of lattice physics, inherited.
- *What it still leaves open:* the weak interaction's symmetry breaking (a Higgs-type field, a silence), every mass, the mixing angles, three generations, confinement (shape only), the nucleon's mass from beneath.

**Against the cascade bar.** The bar admits a posit only on a named contradiction (the proton is composite; CO's ruled set makes it elementary), and calls it worth admitting only if it brings a second open problem with it. On 9 Nov the colour posit alone cascaded only to the hadron spectrum, and in CO not even that, since the proton stays unbuilt without quantisation. With the kind label beside it, the posit now reaches three further open items with data attached: the fractional charges, atomic neutrality and the weak interaction's form. On the bar's own terms that is a cascade, not one primitive for one input. Against it, the label space's sizes are imported, and most of what it buys is the Standard Model's own consistency, read in CO's terms, not CO deriving anything new.

**Reading, for the author.** The bar's verdict could now change, from "not earned" to "earned, at the price of an imported label space". What is gained would be structural: colour, the weak form and the charge values as one posit with consistency doing the rest. No new prediction comes with it beyond, conditionally, the right-handed neutrino. Three choices:
- *Hold*: keep the wall as it is, with this price list on file.
- *Rule as a candidate*: "matter in transit carries an on-site internal label space (colour, kind)". The cascade is entered, and every import is named in "What goes in".
- *Rule only the kind label*: the weak form and charge structure, colour still waiting. This is cheaper, but the charges then need N_c, so items 3–5 stay conditional.
Not ruled.

**Held (2026-11-12, the author).** The on-site label is held, not ruled; the price list stays on file. The next question is whether CO's own pieces supply the label instead of importing it.

## 2026-11-12 — poke: colour as the redundancy of splitting a fermion into alike parts (shape, ungraded)

**The author's hunch, restated.** "One tile alone is a design, two do not make a pattern, three completes it; the parts keep switching roles."

**Tiles held at one place, read as partons.** Let the whole be a fermion c at a place, and let it be made of N alike parts f_a, all at that same place:

c = (1/N!) ε^{a₁…a_N} f_{a₁} ⋯ f_{a_N}.

Because the parts are alike (kin), which part is which is not physical. Rotating the parts among themselves by any unitary with unit determinant leaves c unchanged, since ε is preserved by SU(N). So the splitting carries an SU(N) redundancy at each place. In condensed-matter physics this is the parton, or projective, construction: such a redundancy becomes an emergent SU(N) gauge field on the relations (Wen, *Quantum Field Theory of Many-Body Systems*, 2004). "The parts keep switching roles" is the redundancy itself.

**Why three.**
- The whole is a fermion. Parts that are all alike must then all be fermions.
- A product of N fermions is a fermion only for N odd.
- N = 1 is no splitting ("a design").
- N = 2 would give a boson ("two do not make a pattern").
- The least odd N above one is three ("three completes it").

The same oddness turns up twice already: Witten's global anomaly needs N_c odd, and Skyrme's twisted baryon is a fermion only for N_c odd.

**Why this meets today's constraint.** The label must act on-site to be gauged, and here it does: the parts sit at one place, so the SU(3) redundancy is local by construction. That is the property the corners and tastes lacked.

**One more match.** A physical state at a place must be a singlet of the redundancy (its Gauss law). That is the narrow point kept on 5 Nov: whether "one pattern" coincides with the colour-singlet constraint. Here it does, by construction.

**Leptons.** Unsplit (N = 1): no colour, the "design". This fits the author's three kinds of pattern: whole patterns (electron), three-fold patterns (quarks as the parts of a split whole), and dark.

**What it does not do.**
- "All parts alike" and "the least splitting" are two choices. The first is the kinship ruling's spirit; the second is a minimality posit (five would also be odd).
- Which whole is split, and with what charges, is not given. The anomaly conditions then set the parts' charges once the kind label is in hand. A proton of charge +1 split three ways gives the up and down charges only with the kind label beside it.
- An emergent gauge field from partons is an effective field below the lattice scale. Whether CO's split gives a confining SU(3) with QCD's running is open.
- The emergent field's dynamics (Yang–Mills) still needs quantisation and loops, so the frame problem's exposure is unchanged.

**Grade.** Shape, ungraded. It offers a reason for three (the least odd splitting of a fermion into alike fermions) and an on-site home for colour, which are exactly what the price list said would have to be imported. It turns "the sizes by hand" into "minimal splitting, a posit". Not ruled; read against the cascade bar only if the author wants to go on.

**Cold read of the poke, applied (2026-11-12).** What holds:
- The algebra is right: the redundancy is SU(N), not U(N); an overall phase sends c to e^{iNθ}c, and Z_N sits inside SU(N).
- The singlet sector at one site matches c's two states.
- "Least odd N above one" is sound for parts that are all fermions.

What is corrected:
- *Spin (error).* Parts alike in every respect make the colour part antisymmetric, so spin and position must be symmetric. Three such spin-½ parts at one site make spin 3/2 (Δ⁺⁺-like, the original argument for colour), not a spin-½ whole. So "alike" must mean *alike in colour only*: interchangeable in one label, free to differ in flavour and spin. The SU(3) redundancy acts on that one label, which is all the argument needs. A spin-½ nucleon then needs its parts to differ in flavour.
- *Charges (error).* Parts alike in charge carry Q/3 each, so +1 splits into thirds of +1/3, never +2/3 and −1/3. Up and down charges need the parts to differ in kind (flavour). With the kind label in hand, anomaly cancellation gives Q_u − Q_d = 1 from the kind label and the offset 1/(2N_c) = 1/6 from three colours, so uud = +1. The split supplies N_c = 3; the kind label supplies the difference. The leftover parton U(1) carries Q_c/3 (baryon number as one third of parton number, kept by the walk).
- *Gauss law (overstated).* On-site singlets hold only at infinite coupling. With a dynamical gauge field, Gauss's law includes flux on the relations, so separated parts joined by flux are physical states. The match with the 5 Nov "one pattern" point holds in that sense: one pattern equals a global singlet with its flux.
- *The coupling at the cutoff (the main missing caveat).* An emergent gauge field has no cost of its own at the hop scale, and the cost induced by integrating out the parts makes it strongly coupled there. Asymptotic freedom makes it stronger still at lower energies, so confinement would sit near the hop scale. That contradicts α_s ≈ 0.02 extrapolated to 10¹⁵ GeV and quarks resolved as pointlike up to TeV energies. Getting a weak coupling at the cutoff needs tuning or very many heavy species (the induced-QCD problem, Kazakov and Migdal 1993). So the field's own quadratic cost and its coupling (posits (ii) and (iv) of 9 Nov) are still needed. The split supplies the label and its size, not the dynamics.
- *Also:* the SU(3) is real only for a mean-field state that keeps it; otherwise it breaks to U(1)² or Z₃. Weinberg–Witten is evaded, since gauge currents are not gauge-invariant. 't Hooft anomaly matching applies.

Prior art: Jain 1989 (partons); Wen 1999 (projective construction) and 2002 (PRB 65, 165113), Wen's book (2004); Levin and Wen 2005; preon and rishon models (Harari 1979).

**Where it lands.** Against the price list, the split replaces the on-site label and its size three (posit (i), "the sizes by hand") with two choices: parts alike in colour, and the least odd split. The gauge field's cost and coupling (posits (ii) and (iv)) stay posited, as in the standard theory, where Λ_QCD is an input. The kind label is still needed for the charges. Net: one import becomes a minimality posit; the rest of the bill is unchanged. Grade: shape. The price list stays held.

## 2026-11-12 (evening) — the price list revised with the day's readings (for the author's ruling; not ruled)

**What changed since the price list was held.**
- *The size three is no longer imported outright.* The parton reading, after cold reading, gives three as the least odd split of a fermion into parts alike in colour. The choices that remain are "alike in colour" (the kinship ruling's spirit) and "the least split" (a minimality posit). The kind label's size two is still put in.
- *Statistics beyond two joins it.* Parastatistics is ordinary statistics plus a hidden internal label (Drühl–Haag–Roberts; Doplicher–Roberts), so "no parastatistics" and "no internal label" are one question. With the label, quarks carry what Greenberg's order-3 paraquarks first expressed; without it, every walk pattern is an ordinary fermion.
- *The frame problem is tuned* (the author's ruling, for now). Colour's loops (order α_s/π) fall under the same tuning, so the label no longer worsens an open wall. It adds counter-terms for one more sector.
- *The negative-space map* (refreshed after tuning) puts seven open items under the label: the weak interaction, the colour wall, confinement, baryons as twists, the up–down charges, the nucleon's mass from beneath, and statistics beyond two.

**The posit, revised.** Matter in transit may be a split whole: N parts alike in colour, held at one place, with N the least odd number above one (three). Their interchange is an SU(3) redundancy on the relations. Left-handed matter carries a two-valued kind label, also with its redundancy on the relations. The gauge fields' own costs and couplings are posited, as in the standard theory (Λ_QCD and the electroweak couplings are inputs).

**What it buys:** the seven items above, with consistency doing the rest: the charge values (+2/3, −1/3, 0, −1), neutral atoms for any odd N_c, N_c odd, and, conditionally, a right-handed neutrino.

**What it still costs.**
- Choices: "alike in colour", the least split, and the kind label's two.
- Inputs: the gauge couplings.
- Open problems inherited: a chiral gauge field on the lattice (Ginsparg–Wilson, which the locality ruling allows, or mirror gapping); the weak interaction's breaking (a Higgs-type field, a silence); the masses; three generations.
- One new sector to tune.

**Against the cascade bar.** It now reaches seven open items, three of them with data (the charges, neutrality, the weak form). That is a cascade by the bar's terms. Most of it is still the Standard Model's own consistency, read in CO's terms, and it predicts nothing beyond the conditional right-handed neutrino.

**For the author, three choices as before.**
- Hold.
- Rule both labels as a candidate, with the split as the reason for three.
- Rule only the colour split, keeping the kind label held. This is the cheaper, more CO-native half: it rests on the author's three-fold hunch. The charges then wait on the kind label.
Not ruled.
