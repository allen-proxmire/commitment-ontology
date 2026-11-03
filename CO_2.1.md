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

## Open
- Which sizes are realised, and why: the spectrum. The counts above say how many kinds each size allows, not which sizes exist.
- Whether a loop and its mirror are one kind or two.
- The Born weights from the phase.
- Charge, spin, the forces.
