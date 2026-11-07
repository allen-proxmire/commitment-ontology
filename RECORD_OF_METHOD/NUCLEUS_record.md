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

**Cost, named.** One event at two places needs an ordering, which is a preferred foliation. CO's gravity sector already carries one (khronometric class, preferred frame), so the price has been paid once; it must be the same foliation. No signal passes, as in collapse theories. Candidate, not yet needed.

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
- A commitment that engages possibility in transit resolves that pattern. Only patterns commit, so this is always one pattern engaging another: a measurement is contact. The vacuum never commits; it is timeless stock.
- An entangled pair is one pattern whose transit is in two places; engaging it anywhere resolves it everywhere, since it is one stock ("a pattern sampled twice").

**Two test readings.** *Refraction:* light through glass hops on the glass's clock-rate field h, a property of place; it never draws on the glass's in-transit possibility. Route, not resolution; no measurement. Holds. *Elastic scattering:* two electrons engage each other's transit; both are resolved (directions decided); the record is the change in each one's transit, and nothing else need be permanent. Holds as a reading.

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
