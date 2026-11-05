# R10 result — the eight γ⁵ modes are an artefact of the step ordering; a symmetrised walk with the retarded-hop mass has one species

Scripts `r10_split_order.py`, `r10b_strang_wilson.py`; outputs `r10_result.json`, `r10b_result.json`. Zone scanned on 40³; gapless = |quasi-energy| < 0.08.

**Orderings of the same three hops (massless / θ = 0.3):**

| walk | massless gapless points | with mass |
|---|---|---|
| sequential P_z P_y P_x (baseline) | 12 | 8 (the γ⁵ modes) |
| symmetrised P_x^½ P_y^½ P_z P_y^½ P_x^½ (Strang) | 4 (origin + 3 zone-edge doublers) | **0** |
| palindrome P_x P_y P_z P_z P_y P_x (double step) | 32 | 0 |
| simultaneous exp(i Σ α_j sin k_j) (reference) | 8 (naive) | 0 |

The eight γ⁵ modes exist only in the sequential ordering. In every ordering that is symmetric under reversal, the mass term gaps everything. They were an artefact of doing x, then y, then z, in that order, which no CO ruling asks for.

**Symmetrised walk + retarded-hop mass (R9-A, r = 0.5):** massless, **one** gapless point, the origin; with mass, none. Low-k dispersion at θ = 0.3: E(k) = 0.3046, 0.3181, 0.3671 at k = 0.05, 0.1, 0.2 against √(θ²+k²) = 0.3041, 0.3162, 0.3606; the difference is the expected r k²-type shift, vanishing as k → 0. One species, the Dirac dispersion at low k, unitary throughout.

**Reading.** Two choices do it, both of the kind CO already makes: (1) the three hops are taken in no preferred order (symmetrised), which is what the primitives say, the three lines being equivalent; (2) the flip rate rises with alternation between neighbours (the unitary retarded hop, R9-A). Neither is a derivation; both are rulings. With them the identification "the one pattern is a Dirac walk" describes one pattern.

**Rulings.** γ⁵ modes: **retired** (ordering artefact). Symmetrised ordering: needed. Alternation-dependent flip rate: needed, if the three zone-edge doublers are to be removed. The doubler item in `NUCLEUS.md` moves from "open" to "closed by two rulings," pending the author's reading.
