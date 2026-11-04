# R7: a global curvature cost on which relations are kept

Scripts: [`r7_global_cost.py`](r7_global_cost.py), [`r7_continue.py`](r7_continue.py) (legs with saved state). Numbers: `r7_result_n256_d4.json`, `r7_state_256_4_last.json`.

**Registered before running.** Relations are kept, not made; quanta per place fixed, so degree fixed. Cost E = Σ_e κ_e² with κ Ollivier's curvature; dynamics are degree-preserving swaps of two relations under Metropolis. Start: a random 4-regular graph on 256 places (what thinning leaves). Reference: the 16×16 grid under the same κ. Unknown outcome: if κ goes to the grid's value and growth to the grid's ratios, a global cost supplies locality; if κ falls but growth stays exponential, the cost finds something flat that is not a lattice.

**Reference, same definition.** The grid has κ = 0 on every relation, every relation in a 4-cycle, growth ratios N(r+1)/N(r) = 2.60, 1.92, 1.64, 1.49, 1.39.

**Result** (256 places, degree 4; 18 000 proposals in three legs at T = 0.02, 0.05, 0.02; about 24 minutes).

| stage | mean κ | relations in 4-cycles | growth ratios r = 1…5 |
|---|---|---|---|
| start (random regular) | −0.88 | 0.07 | 3.36, 2.94, 2.51, 1.78, 1.16 |
| after 6 000 | −0.41 | 0.52 | 3.03, 2.40, 2.14, 1.88, 1.50 |
| after 12 000 | −0.43 | 0.56 | 3.03, 2.42, 2.16, 1.88, 1.49 |
| after 18 000 | −0.36 | 0.67 | 2.94, 2.33, 2.10, 1.88, 1.55 |
| grid | 0.00 | 1.00 | 2.60, 1.92, 1.64, 1.49, 1.39 |

- The global cost moves the network the right way on every measure: curvature up from −0.88 toward 0, two-thirds of relations now in squares, growth ratios at small r moving from the expander's toward the grid's.
- It has not arrived. κ ≈ −0.36 against 0; acceptance has fallen to about 1% of proposals, so the anneal is slow near the end. Whether it reaches the grid, or stalls at a flat-but-not-lattice structure, is not decided at this compute.
- Swaps alone (fixed degree) are the right moves for "kept, not made": the stock per place never changes.

**Reading.** First positive signal on locality in Space and Gravity: a slide-invariant cost that depends only on which relations exist, acting on which are kept, drives a random start toward a lattice. Not conclusive; the direction is clear, the endpoint is not. The local version (R6) could not do this because flatness is a property of loops across many places; the global version can see them.

**Post-run check.** The reference grid's κ = 0 under this exact code validates the definition and the target. ΔE is computed on relations within one hop of the swapped places; relations further out that change κ are not re-evaluated until touched, so the running cost drifts from the true cost; the reported mean κ is from the stored values and may lag.
