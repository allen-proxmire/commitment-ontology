# Nucleus

What the two primitives do not reach. The working record is in [`RECORD_OF_METHOD/`](RECORD_OF_METHOD/).

## The three open problems

The particle masses, the strength of the electromagnetic coupling (1/137), and colour. Each needs something not in the inventory.

## Colour

Colour is a three-component internal arrow whose orientation is a convention at each point; the gluon field compares conventions between neighbouring points. The only three-valued structure the primitives supply is spatial (the three lines through a place), and an SU(3) acting on the triad rotates with space: SO(3) is a subgroup of SU(3), not a factor, so no internal remainder survives. **The three lines of space are not colour.** An internal three-dimensional space is outside the inventory; the three conditions of possibility (free, in transit, engaged) are not interchangeable and cannot be one either.

## The bar for a third primitive

A third primitive is admissible on a named contradiction with the world: the rules make a proton an elementary pattern, while experiment makes it composite, bound by a force the rules lack, with most of its mass in the binding. It is worth admitting only if it cascades, bringing a second open problem with it. In the standard theory, colour with one coupling does cascade to the whole hadron spectrum; it does not reach the lepton masses or 1/137. The one geometric route to an internal three is Kaluza–Klein's: places with an inside.

### Sorts of possibility, already costed

The obvious candidate is possibility in sorts: N kinds of possibility, indistinguishable under the rules, conserved together. That candidate has been run, in an earlier program by the same author, and its cost is known.

- **What it buys.** N indistinguishable, jointly conserved sorts force the gauge group U(N) = (SU(N) × U(1))/Z_N by uniqueness. Posit three sorts and SU(3) follows. This is a textbook result (the symmetry group of N identical conserved channels), restated; it is not a derivation of colour.
- **What it does not buy.** The count N is the input. No rule selects {1, 2, 3}; a symmetric N-sort multiplet is stable for every N, so nothing picks three. And the counts as posited give U(1) × U(2) × U(3), three abelian factors where the standard theory has one. The route does not land on the standard group without a further rule.
- **The one structural lead.** The three multiplicities reduce to one number: the most mutually orthogonal sorts an internal state of dimension d can carry is d (the Welch bound), so d = 3 gives groups up to SU(3) and nothing stable above it. The question "why three sorts" becomes "why is the internal state three-dimensional." The matter sector already fixes an internal state of dimension four (Clifford), so the check is whether that four can carry the three. It cannot. The four is an irreducible representation of the Clifford algebra; by Schur's lemma the only operators commuting with the walk's dynamics (α₁, α₂, α₃, β) are scalars, so the only internal symmetry the four supports is U(1), charge. (Massless, the commutant is two-dimensional, 1 and γ₅: two chiral U(1)s. The mass term reduces it to one.) Under rotations the four splits as 2 ⊕ 2, spin ½ twice, with no triplet. So the Clifford four is exhausted by charge; colour would need a new tensor factor, an internal three added to the inventory, not found in it. This sharpens the stop: two primitives give exactly one internal symmetry, U(1), and no more. Falsifier of the reduction: a stable SU(N ≥ 4) gauge symmetry. Check script: [`RECORD_OF_METHOD/NUCLEUS_notes/clifford_commutant.py`](RECORD_OF_METHOD/NUCLEUS_notes/clifford_commutant.py).
- **Independent confirmation of one closure.** That run also found the internal three distinct in kind from the spatial three, not reducible to it. Same conclusion as above, reached by a different route.

Net: sorts cascade exactly as far as SU(N) and stop. By the bar set here, a third primitive of this form is not yet earned.

## Three kinds of wall

The walls around the nucleus are not all the same kind, and only one kind can be got round.

- **Silences.** Nothing selects N = 3. Not a theorem; the primitives do not speak. Passable by one thing only, a new rule, and the cascade bar decides whether it is earned.
- **Representation theorems.** The Clifford four carries only U(1) (above). Schur's lemma has no lattice premise. A relational lattice does not touch it; a time-dependent dynamics (hold-and-release) can only shrink a commutant, never enlarge it.
- **Continuum no-gos.** Nielsen–Ninomiya assumes a fixed translation-invariant lattice; Coleman–Mandula assumes Poincaré invariance and an S-matrix. Neither premise holds at the hop scale, so both have loopholes on a relational lattice. The Coleman–Mandula loophole is where "the three lines of space are colour" could have lived; at the hop scale the triad is three link labels, and mixing them with phases is the walk's own coin, which is the Clifford structure, which is the second wall. The loophole is real; using it lands on Schur.

One loophole with content was checked and is empty. If hold-and-release treated the two chiralities differently, the held phase would carry structure the transit phase lacks. It does not: hold scales hop and flip alike, the flip is parity-even, and the hop rule (symmetric occupancy, antisymmetric ratio 1-form) has no handedness. A chiral asymmetry would need an axial 1-form, which the inventory lacks. Checked numerically on the three-dimensional walk with a hold bump: L→R and R→L transfer equal to 10⁻¹⁴ ([`hold_chirality_check.py`](RECORD_OF_METHOD/NUCLEUS_notes/hold_chirality_check.py)). Ruled: hold-and-release is chirality-blind; mass alone reduces the two chiral U(1)s to one.

## Two walls faced

- **Bell.** A commitment is a local, irreversible, definite event, and Born is read as an identification. Two entangled patterns committing at spacelike separation must then correlate beyond anything a local rule gives. Either commitment is not local, and "a commitment happens at a place" needs a rule it does not have, or CO is a hidden-variable account and Bell excludes it short of superdeterminism. No lattice property evades this; Bell has no lattice premise. CO has no account of entangled commitment. Open.
- **Doublers.** Faced and closed. The Dirac automaton as published carries three zone-edge doublers and, in its sequential step ordering, eight further massless modes. A relational lattice alone does not remove them (R8); a one-way non-unitary hop removes them and the electron with them (R9, excluded); symmetrising the step removes the eight (R10) and a flip rate rising with alternation, the Wilson term in unitary form, removes the three (R9, R10). Two rulings, recorded in the matter sector. Closed.

## Status

**CO is a reconstruction of physics up to 1930 from two primitives.** It covers gravity, electromagnetism and the electron, and stops at the nucleus.
