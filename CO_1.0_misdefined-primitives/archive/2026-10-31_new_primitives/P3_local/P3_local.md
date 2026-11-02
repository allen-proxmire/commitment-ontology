## P3: is local commitment (A') manifold-like? Kill rule, fixed before the run

*31 October 2026. Follows P2 (A FAILS AS STATED; its check found A non-local, like transitive percolation; Reading I14's finite-valency result
rules out a Lorentz-invariant manifold-like order with at most H parents per element). Under the PI-weak ruling a preferred slicing is allowed,
so locality can be tried. Code and this text hashed before the run (`P3.sha256`). No pre-check (disclosed); one post-run check.*

**Growth (A').** Element 0 is a root; M = ⌈U/H⌉ initial elements are its children and hold the U units (H each). A birth picks a seed unit
uniformly; with s its holder, the pool is the units (seed excluded) held by elements within r links of s (links = parent–child edges, either
direction). The other H − 1 units are drawn uniformly without replacement from the pool (all of it if smaller). Parents = the drawn units'
holders; the units move to the newborn. Configurations: U ∈ {64, 256}, H ∈ {2, 3, 4}, r ∈ {2, 3}; n = 4000; seeds 1–2; burn-in 500.

**Diagnostics, controls, pass rule and readings:** as P2 (`P2_manifoldlike.md`), unchanged: Myrheim–Meyer d_MM in bins N ∈ [50,100],
[200,400], [800,1600]; midpoint dimension in the largest bin; pass = spread of median d_MM ≤ 0.3, |d_MM − d_mid| ≤ 0.5, 1.5 ≤ d_MM ≤ 6 and
≥ 30 intervals per bin. Sprinkled 2D and 4D diamonds must pass; transitive percolation is the negative control. **A' SURVIVES** if any
configuration passes; **A' FAILS AS STATED** if none does with both positive controls passing.

**One change from P2, disclosed:** the interval's top y is drawn among x's descendants (first descendant at index ≥ x + g, g log-uniform), as
in the P2 check's independent code, since P2's blind choice of y finds few intervals in sparse orders.

**Disclosed:** the smoke test (`p3_smoke.log`; n = 1500, U = 64, H = 2, r = 2) found no intervals of size ≥ 50: with H = 2 the order is
nearly a forest (1.1 parents per birth). A diagnosis at n = 1500 (unregistered) gave H = 3, r = 3 pasts of ~640 and intervals up to ~560.
