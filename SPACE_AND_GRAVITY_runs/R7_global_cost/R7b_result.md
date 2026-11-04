# R7b: the open run. Longer anneal; degree 6; what the cost can and cannot choose

Scripts: [`r7b_targeted.py`](r7b_targeted.py) (targeted proposals: worst relation first, partner within two hops; a search heuristic, not physics). States: `r7_state_256_4.json`, `r7_state_216_6.json`; last-leg summaries in the matching `_last.json`.

**Registered before running.** Continue the degree-4 anneal toward the grid; start degree 6 and ask whether it goes to the cubic lattice (three dimensions) rather than the triangular one (two). If degree 6 gives three and degree 4 gives two, quanta per place and dimension are one number.

**Degree 4, 256 places** (about 60 000 targeted proposals in all).

| stage | mean κ | relations with κ ≈ 0 | shortest cycle through a relation | growth ratios r = 1…5 |
|---|---|---|---|---|
| start | −0.88 | — | mostly none short | 3.36, 2.94, 2.51, 1.78, 1.16 |
| end | −0.17 | 35% | 3: 279, 4: 228, 5: 3 | 2.67, 2.06, 1.88, 1.73, 1.58 |
| square grid | 0.00 | 100% | 4: all | 2.60, 1.92, 1.64, 1.49, 1.39 |

Growth exponent over r = 2–5: 2.06 (the 16×16 torus gives 1.69 on the same range, lowered by wrap-around). Still moving; acceptance about 1%.

**Degree 6, 216 places** (about 13 000 targeted proposals; compute-limited).

| stage | mean κ | shortest cycles | N(r), r = 1…4 |
|---|---|---|---|
| end | −0.35 | 3: 336, 4: 306, 5: 6 | 7, 28, 81, 169 |
| cubic 6³ | 0.00 | 4: all | 7, 25, 60, 108 |
| triangular 15² | 0.00 | 3: all | 7, 19, 37, 61 |

Not converged; between the expander and the two lattices.

**The finding that settles the question.** Under this exact definition, **the cubic lattice and the triangular lattice both have κ = 0 on every relation.** Both are flat. So the cost κ² has them as equal minima: a flatness cost cannot tell three dimensions from two at the same degree, because flatness is not dimension. The degree-4 and degree-6 anneals both drift toward mixtures of triangles and squares, which is what sampling among flat structures looks like.

**Reading.**
- The global cost supplies **locality** (short loops, slow growth, curvature toward zero). This is what R5 and R6 lacked, and R7/R7b show it arriving from a slide-invariant cost that depends only on which relations exist. The sentence's mechanism for locality is supported, though convergence to a clean lattice is not reached at this compute.
- The global cost does **not** supply dimension. Among flat adjacencies of a given degree, it is indifferent. The quanta-per-place sets the degree; the cost sets flatness; **which flat lattice is the consistency condition's job**, and it says three. Mechanism gives flat; method gives three. That is a clean division, and it means "quanta per place and dimension are one number" was wrong: degree 6 is cubic in three dimensions or triangular in two, and only consistency picks.

**Post-run check.** Reference κ values computed with the same code: cubic 1×10⁻¹⁶, triangular 7×10⁻¹⁷, square grid 0. A leg killed by a timeout before its state was saved resumed from the previous state; counts of proposals are approximate.
