# R6: selection for flatness among lines

Script: [`r6_flat_selection.py`](r6_flat_selection.py); `r6_result.json` holds the last size run.

**The definition tried.** "Out of step" by pairings alone does not close: carrying a transverse line around a loop needs an identification of lines at neighbouring places that a bare graph does not have. What a bare graph does carry is an intrinsic curvature, Ollivier's, κ(i,j) = 1 − W₁(m_i, m_j)/d(i,j): negative on trees and expanders, positive on cliques, near zero on lattices, and dependent on nothing but which relations exist. Candidate: the mismatch cost is κ², flat is κ = 0.

**Registered before running.** Unknown. If choosing each pairing partner to bring κ nearest zero makes neighbourhood growth polynomial with an exponent stable in system size, the cost supplies locality and the sentence closes. If growth stays exponential, this cost, or this way of applying it, does not.

**Result** (q = 8, W = 6, 150 steps; selection acts once a place's degree is ≤ 30; neighbour measures sampled to 10).

| places | component | mean degree | N(r+1)/N(r), r = 1…4 | mean \|κ\| of survivors |
|---|---|---|---|---|
| 200 | — | 4.2 | 4.25, 3.14, 1.86, 1.18 | 0.62 |
| 400 | 290 | 3.5 | 3.88, 3.14, 2.36, 1.60 | 0.73 |
| 800 | — | 3.7 | 4.16, 3.56, 2.82, 1.91 | 0.85 |
| R5, no selection, 400 / 800 / 1600 | | 4.3 / 3.6 / 4.0 | 4.8, 3.7, 2.25, 1.3 / 4.1, 3.4, 2.8, Space and Gravity / 4.7, 4.2, 3.4, 2.3 | |

- The growth ratio at r = 3→4 rises with size (1.86, 2.36, 2.82), the same expander signature as R5. **Selection at pairing does not make growth polynomial.**
- The survivors' curvature is far from zero and grows more negative with size (|κ| 0.62 → 0.85): the network is tree-like and selection did not flatten it. Among the candidates at each pairing, all have κ ≈ −0.7 on a sparse random graph; there is nothing to choose between.

**Reading.** Choosing partners one place at a time cannot reach κ = 0, because flatness is a property of how loops close across many places, and a sparse random start has no short loops to select for. Either the cost must act globally (relations kept or dropped by their effect on loops, not at pairing), or the start must already carry the short loops that flatness needs, which is locality by another name. Ollivier curvature as the cost is not refuted; applying it locally is. **Inconclusive on the definition; negative on the mechanism as run.** Compute limited the sizes; the trend is clear at the sizes reached.

**Post-run check.** The sampled-neighbour approximation to κ was used both in selection and in the final measurement; it biases |κ| toward the tree value for high-degree places, which only matters in the dense early phase where selection was off.
