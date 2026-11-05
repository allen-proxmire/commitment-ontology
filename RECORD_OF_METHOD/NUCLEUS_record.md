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
