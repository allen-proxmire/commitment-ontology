# CO 2.1

Continues from [`CO_2.0.md`](CO_2.0.md), which stops where the two primitives stop forcing. 2.1 opens with the first addition to the inventory. Same method: a rule is added only where the primitives are silent and only if it retires something; a rule whose prerequisites are not ruled stays candidate.

## The one question

What structure inside a commitment gives both the count of particle kinds and the quantum sector.

## Inventory

**A commitment has:** a place; one quantum engaged; a fixed share retained; a direction, inherited from the transit that arrives. Nothing cyclic. Matter repeats with period 1/ω, so it has a phase whether or not the theory names it; the theory has not.

**The quantum sector needs:** spread over routes (2.0 has it literally: a pattern is possibility in transit); localisation (commitment); interference; a rule for where commitment happens (the Born weights); a pattern over two places committing as one. Three of the five need a phase that routes carry and compare.

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
- The hop length becomes a constant: L is a count, and masses in physical units need it. 2.0's hints (a few quanta per place, not 10²¹) put it far above the Planck length, near the shortest Compton wavelength that is a particle, about 10⁻¹⁶ m. Not yet ruled.
- "Out of phase does not add" is a reading until the Born weights are derived from it.

**Precedents, named.** De Broglie (1924): a particle as an internal clock whose phase wave gives the matter wavelength. The zitter models (Schrödinger; Hestenes): the electron as a circulation at the Compton frequency. 2.1 reaches both from "a repeat is one crossing," with the circulation made of hops and the corners made of commitments. A new route to known destinations, not new destinations.

## The hop length is not a new constant

Newton's constant in hop units, from 2.0's rulings. A body of mass M renews at ω = Mc²/ħ and retains δ(P∞/P_max) quanta per renewal, so it is a sink of strength σ = δ Mc² P∞/(ħ P_max) quanta per second. Possibility hops at rate ν = c/ℓ per relation, ℓ the hop length; on the cubic lattice the steady deficit at r hops is σ/(4πνr) quanta per place, so h = σ/(4πνP∞ r). Setting h = GM/(c² rℓ):

$$G=\frac{\delta\,c^{3}\,\ell^{2}}{4\pi\,\hbar\,P_{\max}}\qquad\Longleftrightarrow\qquad \ell=\ell_{P}\sqrt{\frac{4\pi P_{\max}}{\delta}},\quad \ell_P=\sqrt{\frac{\hbar G}{c^3}} .$$

The hop length, the capacity and the retained share are one relation apart. Given any two, the third follows. If 2.0's hint holds (P_max a handful of quanta) and the hop is near the shortest particle Compton wavelength (ℓ ≈ 10⁻¹⁶ m, ℓ/ℓ_P ≈ 6×10¹⁸), then δ ≈ 10⁻³⁷: a renewal retains about 10⁻³⁷ of a quantum as record, one quantum per 10³⁷ renewals. For an electron that is one quantum of record every few hundred million years. Pooling is as slow as every bound required, now with a number.

So 2.1 introduces no fourth constant: ℓ replaces δ, or δ replaces ℓ, and the set of the theory's own constants stays at three (P_max, Λ, and one of δ or ℓ).

## The shapes, counted

Closed self-avoiding loops on the cubic lattice, up to the lattice's 48 symmetries and translation (a hand count done by machine, [`CO_2.1_notes/sap_count.py`](CO_2.1_notes/sap_count.py)):

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
- **No selection.** The allowed masses are the rationals k/L. Any ratio can be matched with enough hops, so this must not be used to fit the known masses; a formula that fits anything explains nothing. The loop gives a scale and a bound, not a spectrum.
- **Self-gravity cannot select sizes.** A loop's own deficit is of order δ ≈ 10⁻³⁷. Whatever makes some loops stable and others not is not in the inventory. **The masses are blocked on the forces, not on gravity; charge comes first.**

**Mirrors (candidate).** A reflection is a lattice symmetry, but a loop is traversed, and inertia makes the direction physical: reversing the traversal is not reflecting the shape, so a chiral loop has four versions. A loop and its mirror are two kinds. A choice about what "the same" means, not a derivation; it is where a left/right label can sit.

## Charge (candidate)

A relation carries how much (occupancy, symmetric) and which way (a ratio, antisymmetric: r_ji = 1/r_ij, a 1-form). Gravity took the first; the second was set aside in 2.0. Around a closed loop the ratios multiply to a holonomy e^Φ, equal to 1 while ratios are slaved to places. Let relations be out of step in this number too.

| | statement | status |
|---|---|---|
| cost | sliding costs nothing, so the cost of a 1-form out of step depends only on holonomies; the unique local quadratic cost in 3+1 is Maxwell's, ∫F². Same uniqueness as Einstein's, on the other number a relation carries | candidate |
| source | a traversed loop is a current loop: a circulation, which sources the which-way field as a **magnetic dipole**, not as a charge. Charge is a monopole and cannot be any shape or traversal property: mirror is P and reversal is T, and a time-even scalar is invariant under both; C is not a spacetime operation. So charge is a sign the loop **carries**, the sign of the which-way bias on the relations it runs on. **An antiparticle is the same loop with the opposite carried sign.** (Earlier "run backward" withdrawn: that flips the moment, not the charge) | candidate |
| quantization | a loop's phase must return to itself after a circuit, so the holonomy it carries and the holonomy it sits in combine to a multiple of 2π: the Aharonov–Bohm / Dirac argument as a closure condition on repeats | candidate |
| strength | the 1-form's stiffness relative to ħc (1/137) is not given; a fourth constant unless tied to the others | open |

## One pattern (candidate, from Allen)

One loop carries a sign (charge: particle or antiparticle, invariant under every boost) and has a sense seen along its motion (helicity: flips when overtaken, undefined at rest, as a massive particle's does). (Carried sign) × (helicity) are **the four components of a Dirac fermion in the helicity basis, with the right behaviour under boosts. One pattern is one Dirac field.** For a chiral loop, shape against mirror is a further label, parity. The test "do the four versions mix under a boost as Dirac's do" is passed after the correction above, for the right reason.

"The face going forward is the identity": the loop's sense seen from where it is going is its helicity; with the carried sign, and its handedness if chiral, that is the identity. The loop's circulation is a magnetic moment, and a Dirac particle's moment is a number (set by its charge and mass) the picture can be asked to produce: a sharper test than the count of four. On a lattice with three lines through each place, which line a moving loop's plane is set against is a three-valued label that costs nothing and leaves mass unchanged. Three-valued, free, invisible to mass, carried by every loop: the shape of colour. Whether it is colour depends on how such labels couple; not done.

So, in one sentence: mass is size and corners (k/L); charge is the carried sign; helicity is the running sense seen along the motion; handedness is shape against mirror; a three-valued orientation label comes free. **Ruled as 2.1's direction: one pattern.**

**Selection (candidate).** A charged loop sits in its own holonomy, and closure relates its length, its corners and its own flux. Only some (k, L) close. The first rule on the board that could pick sizes where gravity cannot. Not worked.

## Spin and moment of the one pattern

The square, L = k = 4, side ℓ, m = ħ/(cℓ). One quantum circulates at radius ℓ/2 with momentum mc:

$$S=mc\cdot\frac{\ell}{2}=\frac{\hbar}{2}.$$

**Spin one-half, from the loop and nothing else.** As a current loop, I = ec/(Lℓ), A = ℓ²:

$$\mu=\frac{ec\ell}{4}=\frac{e\hbar}{4m},\qquad g=\frac{\mu}{(e/2m)S}=1 .$$

**Dirac has g = 2 (measured 2.0023). The loop gives half.** The same factor separates every classical circulating-charge model, the zitter models included, from Dirac; non-planar loops cannot close it (k ≤ L and the isoperimetric bound). Spin right, moment wrong by two.

The one place inside the picture it could come from: Dirac's internal clock runs at 2mc²/ħ, twice the Compton frequency. "A repeat is one crossing of the extent" and "a circuit is two crossings" were used interchangeably above and are not the same; if the carried sign goes around twice per repeat, g = 2. Which is the repeat is a ruling not yet made; g = 2 says which way, and the choice must be shown not to break the mass or the spin. Candidate.

**1/137** goes in from data, as Λ did: the which-way field's stiffness relative to ħc. Not to be sought among the others until the factor of two is understood.

## Open
- The factor of two: which of crossing and circuit is the repeat.
- The spectrum: which (k, L) close under their own holonomy.
- The 1-form's strength (1/137).
- Whether the three-valued orientation label couples as colour does.
- The Born weights from the phase.
- The Born weights from the phase.
- Charge, spin, the forces.
