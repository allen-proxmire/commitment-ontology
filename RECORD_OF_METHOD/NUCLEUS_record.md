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
