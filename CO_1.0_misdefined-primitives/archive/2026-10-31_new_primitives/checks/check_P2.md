**P2 post-run check: OK. The reading A FAILS AS STATED stands. There is one minor code error, and it does not affect the reading.**

**(1) Hashes and timing: OK.** All four registered files verify against `P2.sha256` (stamp 2026-10-31T11:40:19Z, which is 12:40:19 local). `p2_result.json` and `p2_run.log` were written at 12:41:16, after the stamp. The smoke log is older than the stamp, but it is itself one of the hashed inputs, which is correct.

**(2) Implementation: OK, with one error.**
- **Myrheim–Meyer formula:** correct. f(d) = Γ(d+1)Γ(d/2)/(2Γ(3d/2)) is Meyer's ⟨R⟩/N² = Γ(d+1)Γ(d/2)/(4Γ(3d/2)) rescaled to R/C(N,2). It gives f(2) = 1/2 and f(4) = 1/10, and the diamond controls come out at 2.00 and 4.01.
- **Midpoint estimator:** correct. The two half-intervals are taken as `anc[z]&desc[x]` and `desc[z]&anc[y]`, and d_mid = log₂(N/N_half) follows from the half-diamond holding 2^(−d) of the volume. The 4D control gives 4.15.
- **Closure bitsets:** correct. Ancestors are built forward and descendants backward, which works because parents always carry smaller indices.
- **Interval sampling:** correct. If x is not below y, `desc[x]&anc[y]` is empty by transitivity. The burn-in offset includes M.
- **Longest-chain DP:** correct. Every covering relation is a parent link, and the DP runs over sorted indices with intervals convex, so it is exact.
- **Sprinkling:** correct. Rejecting box samples outside the diamond gives a uniform distribution in the diamond.
- **ERROR (minor):** when H does not divide U (the three H = 3 runs: U = 16, 64, 256), the code sets `M = U//H` and `holder = u//H`. Unit U−1 then starts out "held" by element M, which is the first newborn and does not yet exist. If that first birth draws unit U−1, it becomes its own parent and its ancestor set contains itself. This touches only element M, which sits inside the burn-in, so it has no effect on the result. The registration's "M = U/H" also leaves the non-integer case undefined. The fix is ceil(U/H) initial elements.
- **Small biases, all in the conservative direction:** fractions at or above f(1.0001), i.e. exact chains, return NaN and drop out of the medians, which nudges d_MM up. The diamond controls use 50 intervals per bin against 200 for the growth runs. Both are within what was registered.

**(3) Independent re-implementation: OK.** `/home/claude/checkP2/indep.py` uses a numpy reachability matrix, a different interval sampler (y is a descendant at a log-uniform index gap), bisection on lgamma, and ceil(U/H) initial elements. It ran 40 intervals per bin at n = 4000. Median d_MM by bin, with the registered run's values in brackets:

| Config | U/H² | d_MM, N 50–100 | d_MM, N 200–400 | d_MM, N 800–1600 |
|---|---|---|---|---|
| U=64, H=2 | 16 | 2.32 [2.33] | 1.87 [1.84] | 1.27 [1.23] |
| U=64, H=4 | 4 | 1.35 [1.34] | 1.10 [1.09] | 1.03 [1.02] |
| U=256, H=2 | 64 | 2.58 [2.64] | 3.16 [3.22] | 2.45 [2.39] |
| U=144, H=3 (not in run) | 16 | 2.40 | 1.79 | 1.21 |

The falling trend toward 1 at larger intervals is confirmed, and d_mid tracks d_MM.

**(4) The diagnosis: a sound inference, with one caveat.**
- **Why fixed U acts as a spatial volume.** Each unit traces a chain of holders, so the live "slice" has at most U members. A birth hits one of a given element's H units with probability about H²/U. So U/H² is the effective spatial volume, counted in births per direct child. Once an interval runs much longer than the time influence takes to cross that volume, its ordering fraction goes to 1 and d_MM to 1. That is the standard behaviour of a tall diamond in a spacetime with compact space.
- **Small-interval scaling (a new statement, inference grade).** The smallest-bin median d_MM collapses onto the single variable U/H², not U/H. Two pairs show it:
  - U/H² = 4: (16,2) gives 1.40 and (64,4) gives 1.34.
  - U/H² = 16: (64,2) gives 2.33, (64,4)… no, (144,3) from the independent run gives 2.40.
- **The shape of that dependence.** Across U/H² = 1.8 / 4 / 7 / 16 / 28 / 64, the medians are 1.08 / ≈1.37 / 1.73 / ≈2.34 / 2.66 / 2.64. The rise in d − 1 is roughly linear in log(U/H²), then levels off near 2.6, which is close to transitive percolation's small-bin value of 2.48.
- **Caveat.** Removing the width cut-off does not make the order local. Draws are uniform over all U, so nothing like spatial neighbourhoods exists. At U = 256, H = 2 the medium bin (3.2) sits above the small bin (2.6). That is the pattern of transitive percolation and other non-local random orders, where dimension changes with interval size, not a flat-spacetime value being approached.
- **The follow-up.** A run with U/H² much larger than the interval sizes is the fair way to separate the width effect from the growth law itself. It needs n much larger than U/H (times a log factor) for the order to connect, so at N up to 1600 that means n of order 10⁵ or more. The likely outcome is still a scale-consistency failure of the transitive-percolation kind. A pass would probably need locality in the unit draws, and that would be a new primitive, not A as stated.

**(5) Wording: OK.** There is no first person and no "lead". "A SURVIVES" and "A FAILS AS STATED" are registered reading labels, not grade words.

**Files:** `/home/claude/checkP2/indep.py` (the independent check), plus copies of `p2_manifold.py` and `p2_result.json` in the same folder.

**Recommended next steps:**
1. Fix the initial-holder count to ceil(U/H). This is cosmetic, and changing the hashed code means a version note.
2. If the width question matters for the ruling, register a large-U run with U/H² ≫ 1600 and n ≫ U/H. State in advance that a transitive-percolation-like failure is the expected outcome.
3. Record U/H² as the effective spatial volume of C7, with the saturation near 2.6, as an inference-grade note on A.