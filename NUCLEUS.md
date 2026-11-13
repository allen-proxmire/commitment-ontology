# Nucleus

What the two primitives do not reach, and why. Results only; every route tried is in [`RECORD_OF_METHOD/`](RECORD_OF_METHOD/).

## The three open problems

The particle masses, the strength of the electromagnetic coupling (1/137), and colour. Each needs something not in the two primitives; C9 now adds colour (candidate).

## Colour is not space

Colour is a three-component internal arrow whose orientation is a convention at each point. The only three-valued structure the primitives supply is spatial, the three lines through a place, and an SU(3) acting on that triad rotates with space: SO(3) is a subgroup of SU(3), not a factor. **The three lines of space are not colour.**

## The four carries only charge

The matter sector's internal state is four-dimensional, an irreducible representation of the Clifford algebra. By Schur's lemma the only operators commuting with the walk's dynamics are scalars, so the only internal symmetry it supports is U(1), charge. Under rotations it splits as two spin-½ doublets, with no triplet. Colour would need a new factor, an internal three added to the inventory ([`clifford_commutant.py`](RECORD_OF_METHOD/NUCLEUS_notes/clifford_commutant.py)).

## The wall

On the network, CO carries real quantities (held share, stretch, one-way part, shear, ratio) and one non-commuting matching, space's frame. On patterns it carries one complex phase (charge) and the four. Every three-valued thing in it is a spatial vector. The nucleus needs, on each quark, a three-component *complex* scalar that leaves space alone, and on each relation a unitary 3 × 3 matching between them. Two primitives supply neither. Six routes to that three were tried and closed, each finding the three had been put in by hand: possibility in sorts; the Clifford four; the three lines of space; tiles with a tile mass; one pattern three times on a shared cycle (gives flavour, not colour); parallel relations (removed at formation).

**From the two primitives alone, CO's only non-abelian matching is space's; the nucleus needs one that is not. C9 (below) adds it.**

The earliest place the rules say "one" where the nucleus needs "three" is the amplitude rule: possibility in transit carries one complex amplitude. A transit carrying a complex triplet would be the object; nothing in the two primitives supplies it, and nothing forbids it; C9 does.

The count is measured, not free: the e⁺e⁻ → hadrons ratio and the π⁰ → γγ rate both give three, with charges ⅔ and −⅓. Any route must give exactly three.

## Colour as a split (C9, the author's ruling, candidate)

Matter in transit may be a split whole: parts alike in colour, held at one place. If the whole is a fermion and its parts are fermions, their number must be odd. One part is no split, and two would make a boson. C9 takes three as the first complete split: among parts that all relate to each other, three is the first count whose relations close a loop, so that the three are tied by one closure (ε^{abc}) that no pair can make (the author's contrast principle; `OPEN_DIRECTIONS_notes/contrast.md`). Three is also the least odd split, so the parts can all be fermions. Larger splits are not forbidden. Rotating the parts' colour labels by any unitary of unit determinant leaves the whole unchanged, c = (1/3!) ε^{abc} f_a f_b f_c, so the rotation is an SU(3) redundancy at each place, carried on the relations as a matching. Unit determinant follows (ε is preserved by SU(3), not by U(3)), and the label lives on-site, so it can carry a gauge field. A physical state is a singlet, with flux on the relations between separated parts.

What C9 still takes: the matching's own quadratic cost and its coupling (posited, as in the standard theory, where Λ_QCD is an input; a field induced only by the parts would be strongly coupled at the hop scale), flavours (parts alike in everything give spin 3/2; a spin-½ nucleon needs two), the flavours' charges (+⅔, −⅓, which wait on a kind label, not ruled; with it, anomaly cancellation fixes them, given no right-handed neutrino or one with a Majorana mass), and confinement (named, not obtained). Leptons are unsplit. Without a hidden label, walk patterns are ordinary fermions; colour is the gauged form of what Greenberg's order-3 paraquarks first expressed. Colour's loops fall under the tuning accepted for species' speeds. Prior art: partons (Jain 1989; Wen 1999, 2002).

## What a third primitive would cost (before C9)

*(Record before C9; see Colour as a split and Quarks and gluons for what C9 changes.)* A third primitive is admissible on a named contradiction (the rules make the proton elementary; experiment makes it composite) and worth admitting only if it cascades to a second open problem. Filling the slot would take at least four posits: which transit carries the triplet; a 3 × 3 unitary matching on relations with its cost; unit determinant (else a ninth massless vector couples to baryon number, excluded at 10⁻⁴⁷); and a scale. With those, Yang–Mills is the unique quadratic cost. Even then the proton is unbuilt: one triplet gives spin 3/2, not ½; the exchange sign of a triplet is not built; confinement is named, not obtained; the gluon field would need second quantisation; the fractional charges need charge to become a rational multiple. It cascades to the hadron spectrum and no further. Not earned.

## Quarks and gluons (shape; the spectrum by identification)

Quarks are the parts of a split whole (C9); gluons are patterns of the colour field on the relations, as light is of the which-way field. A proton is three parts bound by that field. A linear binding cost needs the relations between quarks to hold one quantum per grain a: E = (ħc/a²)L, the strong-coupling flux string (Kogut–Susskind 1975), with a = ħc/√σ ≈ 0.45 fm, the QCD scale renamed. By identification (candidate; conditional on C9, the tuning accepted for loops, the colour field quantised with its posited cost and coupling, and the quark masses as inputs): CO's colour sector has lattice QCD's continuum limit (ℓ ≪ ħc/Λ_QCD, so it is effectively at it; real time against Euclidean does not matter, the spectrum belongs to the theory), so confinement and the hadron spectrum follow as lattice QCD computes them, the nucleon's mass included (about 940 MeV; the quark masses supply about 10%, and in the trace decomposition the rest is the gluon trace anomaly). Electromagnetic and isospin splittings (the neutron–proton difference) need the quarks' charges, which wait on the kind label. Confinement there is established numerically, not proved (compare the open Yang–Mills mass gap). CO adds nothing of its own to these numbers.

## Three kinds of wall

- **Silences.** Nothing selects N = 3. Passable only by a new rule; C9 is that rule.
- **Representation theorems.** The four carries only U(1) (Schur). No lattice premise; not passable from inside.
- **Continuum no-gos.** Nielsen–Ninomiya and Coleman–Mandula assume premises that fail at the hop, so they have loopholes; using the Coleman–Mandula loophole lands on Schur. Hold-and-release is chirality-blind (checked to 10⁻¹⁴, [`hold_chirality_check.py`](RECORD_OF_METHOD/NUCLEUS_notes/hold_chirality_check.py)).

## Entanglement (candidate)

An entangled pair is one pattern sampled twice: one stock, two point commitments, one joint law. Each end's commitment finds the stock as it stands in its own past cone, conditioned on the commitments there (Tumulka's structure, with Born on the pair). Inherited, not supplied: the joint law, the commutation of spacelike engagements, the marginal at one place. A foliation fixed by the state is not excluded by relativity; setting it aside is CO's choice.

References: Gell-Mann (1964), Zweig (1964), Kogut and Susskind (1975), Wilson (1974), Lee and Yang (1955), Utiyama (1956), Tumulka (2006), Dürr et al. (2014), Bedingham et al. (2014).
