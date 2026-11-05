# R10 result — the eight γ⁵ modes are an artefact of the step ordering; ~~a symmetrised walk with the retarded-hop mass has one species~~

**Corrected 2026-11-05 after blind review; see `R10d_result.md`.** The 'one species' headline was a threshold artefact (gapless = |E| < 0.08 while the extra modes sit at 0.14–0.33 at r = 0.5); the unitary Wilson angle is periodic and r = 0.5 is outside its window; the π-sector was not counted; the massless palindrome has 32 zero points, not four. The ordering finding (the eight γ⁵ modes belong to the sequential order) stands.

Scripts `r10_split_order.py`, `r10b_strang_wilson.py`; outputs `r10_result.json`, `r10b_result.json`. Zone scanned on 40³; gapless = |quasi-energy| < 0.08.

**Orderings of the same three hops (massless / θ = 0.3):**

| walk | massless gapless points | with mass |
|---|---|---|
| sequential P_z P_y P_x (baseline) | 12 | 8 (the γ⁵ modes) |
| symmetrised P_x^½ P_y^½ P_z P_y^½ P_x^½ (Strang) | 4 (origin + 3 zone-edge doublers) | **0** |
| palindrome P_x P_y P_z P_z P_y P_x (double step) | 32 | 0 |
| simultaneous exp(i Σ α_j sin k_j) (reference) | 8 (naive) | 0 |

The eight γ⁵ modes exist only in the sequential ordering. ~~In every ordering that is symmetric under reversal, the mass term gaps everything.~~ Corrected: at r = 0 every doubler takes mass θ, the same as the physical mode; nothing is gapped relative to it. They were an artefact of doing x, then y, then z, in that order, which no CO ruling asks for.

**Symmetrised walk + retarded-hop mass (R9-A, r = 0.5):** ~~massless, **one** gapless point, the origin; with mass, none.~~ Corrected: see R10d; at r = 0.5 there are extra species at 0.158 (π-sector) and 0.331. Low-k dispersion at θ = 0.3: E(k) = 0.3046, 0.3181, 0.3671 at k = 0.05, 0.1, 0.2 against √(θ²+k²) = 0.3041, 0.3162, 0.3606; the difference is the expected r k²-type shift, vanishing as k → 0. One species, the Dirac dispersion at low k, unitary throughout.

**Reading.** Two choices do it, both of the kind CO already makes: (1) the three hops are taken in no preferred order (symmetrised), which is what the primitives say, the three lines being equivalent; (2) the flip rate rises with alternation between neighbours (the unitary retarded hop, R9-A). Neither is a derivation; both are rulings. With them the identification "the one pattern is a Dirac walk" describes one pattern.

**Rulings.** γ⁵ modes: **retired** (ordering artefact). ~~Symmetrised ordering: needed. Alternation-dependent flip rate: needed. The doubler item moves to closed.~~ Regraded after review (R10d): both rulings candidate; doubler item open, as a bound on the hop length.
