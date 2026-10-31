## P2: is C7 growth manifold-like? Kill rule, fixed before any run

*31 October 2026. Tests primitive A of P1. The code and this text are hashed before the run (`P2.sha256`). Lean protocol: no pre-check (disclosed), one post-run check.*

**Growth (A).**
- **Start:** U units, held H each by M = U/H initial elements.
- **Births:** n new elements. Each draws H units uniformly at random, without replacement, from all U. Its parents are the units' current holders, and the units move to it.
- **The order** is the transitive closure of the parent relations.
- **Runs:** U ∈ {16, 64, 256}, H ∈ {2, 3, 4}, n = 4000, seeds 1–2. Burn-in: the first 500 births are discarded.

**Diagnostics** (standard in causal-set work), on intervals I(x, y) = {z : x < z < y} sampled from the grown order:
- **Myrheim–Meyer dimension d_MM.** The ordering fraction of the interval, R/C(N, 2), is set equal to the flat-space value
$$
f(d)=\frac{\Gamma(d+1)\,\Gamma(d/2)}{2\,\Gamma(3d/2)}\qquad(f(2)=\tfrac12,\ f(4)=\tfrac1{10}),
$$
  and solved for d.
- **Midpoint-scaling dimension d_mid** (Reid). In the largest bin, take N_half = max over z of min(|I(x, z)|, |I(z, y)|), and set d_mid = log₂(N/N_half).
- **Chain dimension d_L** (reported, not tested). Fit L ∝ N^{1/d_L}. The smoke test showed it biased at these sizes: 4D sprinkles give about 3.1.
- **Size bins:** N ∈ [50, 100], [200, 400], [800, 1600], with up to 200 intervals per bin (fewer where the order has none).

**Controls.**
- **Positive:** N points sprinkled uniformly in a causal diamond of 2D and of 4D Minkowski space, in the same three size bins. Both must pass.
- **Negative:** transitive percolation with p = 0.05 and n = 4000, the best-known covariant growth law. It is expected to fail.

**Pass, for a given (U, H)** (a growth is manifold-like at these sizes if all three hold):
1. **Scale-consistent.** The median d_MM in the three bins varies by at most 0.3.
2. **Estimator-consistent.** |median d_MM − median d_mid| ≤ 0.5, both in the largest bin.
3. **Non-degenerate.** 1.5 ≤ d_MM ≤ 6, and every bin has at least 30 intervals.

**Readings.**
- **A SURVIVES** if at least one (U, H) passes. The dimension it shows is then A's first output, which was not put in.
- **A FAILS AS STATED** if none passes while both positive controls pass.
- **Bug signal:** a positive control fails. Then no reading is made.

**Disclosed.**
- Reading I14 suspected that C7 orders are not manifold-like.
- **Smoke test** (`p2_smoke.log`; n = 1500, U = 16, H = 2, only 8 diamonds per bin). The chain estimator failed the 4D control, so it was replaced, before hashing, by the midpoint dimension. The smoke test also showed C7 at U = 16, H = 2 with d_MM ≈ 1.0–1.4, near one-dimensional.
- The thresholds 0.3 and 0.5 are judgement calls, fixed here before the run.
