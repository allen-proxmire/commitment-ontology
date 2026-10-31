**P3 post-run check: OK, with no errors and two wording points.** The reading "A' FAILS AS STATED" stands. The failure comes from the law itself, not from a bug.

**(1) Hashes and timestamps: OK.**
- All three hashed files verify against `P3.sha256`: `P3_local.md`, `p3_manifold.py` and `p3_smoke.log`.
- The stamp is 2026-10-31T11:45:41Z. The code (11:45:26Z) and smoke log (11:45:29Z) are older than the stamp. Both outputs, `p3_result.json` and `p3_run.log`, are from 11:46:21Z, after it.
- The outputs are not hashed, which is expected.

**(2) Code against spec: OK.**
- `grow_local` follows the spec:
  - Element 0 is the root, and M = ⌈U/H⌉ children hold the units.
  - The link sets are symmetric, and the BFS goes out to radius r. The ball includes s itself.
  - The pool leaves out the seed and draws H−1 units without replacement, or takes the whole pool if it is smaller.
  - Parents are the set of holders, the units move to the newborn, and `held`/`holder` are updated together.
- The interval sampler is correct:
  - It shifts `later = desc[x] >> (x+g)`.
  - The lowest set bit gives the first descendant at index ≥ x+g.
  - It then takes I = desc[x] & anc[y], the open interval.
- The rest is copied from P2 unchanged (ordering fraction, longest chain, midpoint, `summarize`). Both diamond controls pass (2D: 2.03/2.01/2.00; 4D: 3.93/4.02/4.01). Transitive percolation (TP) fails as it should, drifting 2.48→1.19.

**(3) Independent re-implementation (reading).** The code was written separately: BFS by distance map, unit lists, and a different way of choosing y. It used seeds 11 and 12, n = 4000, 40 intervals per bin.

| Config | Parents per birth | Median d_MM by bin | P3 registered |
|---|---|---|---|
| U=256, H=4, r=3 | 3.87 | 2.31→1.71→1.24 and 2.38→1.82→1.22 | 2.32→1.79→1.23 |
| U=64, H=2, r=2 | 1.03–1.04 | only the smallest bin is filled, d_MM = 1.0 (pure chains); the two larger bins are empty, since pasts are only about 115 | 200/0/0 |

The results match. The best configuration drifts toward 1 in the same way as the TP negative control, and the rest are chains or close to it.

**(4) Bug or property of the law: a property of the law.** The point is derived, not just inferred:
- Each newborn takes the seed unit's current holder as a parent. So each unit's path through its holders is a chain.
- Every non-root element sits on at least one of these chains, so the order (minus the root) is covered by U chains.
- By Dilworth's theorem, no set of mutually unrelated elements can be larger than U. An interval with N ≫ U elements therefore has an ordering fraction near 1, so d_MM → 1 for any law with a fixed number of units, local or not.
- Locality makes this worse at small sizes. The seed's holder already holds the other H−1 units it arrived with, and they are always in the pool. So draws keep picking units that travel together, and the parents collapse onto one element: 1.03 parents per birth at H=2.

One-line diagnosis: with a fixed number of units, each element is threaded on unit paths, so any antichain has at most U elements and large intervals become chains; local draws add co-moving units to this, which gives d≈1 threads.

**WORDING**
- The docstring of `p3_manifold.py` still says `p2_manifold.py`. This is cosmetic and the file is hashed, so it is noted here, not fixed.
- In the results, `d_mm` = NaN with a full bin (for example `U64_H2_r2`, counts 200/0/0) means the ordering fraction is exactly 1, a pure chain with d_MM = 1. It does not mean there is no estimate. The P3 write-up should say this, or the reading will look like it rests on missing data.
- The phrase "thin and chain-like, d≈1, or drifting" is supported by the data.

**Recommended next steps**
1. Add a dated note to P3 saying that NaN with a full bin means pure chains, d_MM = 1.
2. Record the bound "the order is covered by U chains, so large intervals become chains" as a new statement (derived). It also applies to P2's law A (`grow_c7`). It rules out every law with a fixed number of units, local or not, so the next primitive needs a growing number of units, or something else that lets the width grow.
3. Before writing P4, decide whether the number of units (U) should grow with n, for example by creating units at births.

The check's script is `/home/claude/checkP3/indep/indep.py`, and the checked copies are in `/home/claude/checkP3/`.