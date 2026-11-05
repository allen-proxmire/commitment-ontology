# R9 result — a retarded hop removes the three doublers; the eight γ⁵ modes survive it; the damping version kills the electron

Script `r9_retarded_hop.py`, output `r9_result.json`. Zone scanned on a 40³ grid; a point counts as gapless if some eigenvalue has |quasi-energy| < 0.08 and |λ| within 0.02 of 1.

| version | massless gapless points | massive (θ = 0.3) |
|---|---|---|
| baseline CO automaton | 12 (origin, 3 zone-edge, 8 at (±½π)³) | 8 (the γ⁵ modes; origin and edges gapped by θ) |
| (A) unitary Wilson mass, r = 0.5 | 9 (origin + 8 γ⁵) | 8 (γ⁵ modes, shifted to (±0.47π)³, still gapless) |
| (B) non-unitary damping, ε = 0.5 | 1 (origin) | — |

**(A) Unitary Wilson mass** ("flip rate rises with alternation"): removes the three zone-edge doublers, as a Wilson term does. It does not touch the eight γ⁵ modes: a β-type term anticommutes with γ⁵ there, so they move but stay gapless at every θ and r. Confirms the structure argument.

**(B) Damping** (the literal retarded difference, e^{ik} − 1): leaves only the origin, but the decay rate per hop is εk²/2 at low k, measured: 2.5 × 10⁻³ at k = 0.1, 2.5 × 10⁻⁵ at k = 0.01, 2.5 × 10⁻⁷ at k = 0.001. With the hop at 1.1 × 10⁻¹⁸ m (3 × 10²⁶ hops/s) and an electron-scale pattern at k = ℓ/ƛ_C ≈ 2.8 × 10⁻⁶, the lifetime is **1.8 × 10⁻¹⁵ s**. The version that removes every extra mode also removes the electron. Excluded.

**Reading.** "Commitment gives transit a direction" works in its unitary form and buys exactly what the Wilson term buys: the three doublers. It is a ruling of the same kind as the flip-rate rule and costs nothing at low k. The eight γ⁵ modes are not doublers in the Wilson sense and are immune to every mass-type term; they are a property of the split-step ordering (at (±½π)³ the hop product is ∝ γ⁵). Removing them means changing the walk's structure, not its mass term, or accounting for them.

**Rulings.** (A) candidate: retarded hop as Wilson mass, removes the zone-edge doublers; needed if the identification is kept. (B) excluded. The eight γ⁵ modes: open.
