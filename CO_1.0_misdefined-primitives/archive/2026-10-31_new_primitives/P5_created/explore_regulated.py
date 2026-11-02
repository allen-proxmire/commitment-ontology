"""Exploratory (not registered): A''' — local commitment (as A') that creates one unit at the newborn only if the units held within r links
of it number fewer than K (a capacity, as saturation's K). Reports slice growth exponent and order depth/width."""
import random, sys, math
import numpy as np
sys.dont_write_bytecode = True
sys.path.insert(0, '/home/claude/primitivesP5')
from p5_manifold import bitsets, growth_exponent, sample_intervals, summarize, d_mm, BINS
def ball(nbr, s0, r):
    b, f = {s0}, {s0}
    for _ in range(r):
        f = {w for v in f for w in nbr[v]} - b; b |= f
    return b
def grow_reg(U0, H, r, K, n, rng, W_out):
    M = -(-U0 // H); holder = [1 + u // H for u in range(U0)]
    parents = [[]] + [[0] for _ in range(M)]; nbr = [set(range(1, M + 1))] + [{0} for _ in range(M)]
    held = {}
    for u in range(U0): held.setdefault(holder[u], set()).add(u)
    for k in range(n):
        x = M + 1 + k; seed = rng.randrange(len(holder)); s0 = holder[seed]
        pool = sorted(u for v in ball(nbr, s0, r) for u in held.get(v, ()) if u != seed)
        S = [seed] + rng.sample(pool, min(H - 1, len(pool)))
        ps = sorted(set(holder[u] for u in S)); parents.append(ps); nbr.append(set(ps))
        for p in ps: nbr[p].add(x)
        for u in S:
            held[holder[u]].discard(u)
            if not held[holder[u]]: del held[holder[u]]
            holder[u] = x; held.setdefault(x, set()).add(u)
        if sum(len(held.get(v, ())) for v in ball(nbr, x, r)) < K:
            holder.append(x); held[x].add(len(holder) - 1)
        if (k + 1) % 100 == 0: W_out.append((k + 1, len(held), len(holder)))
    return parents
if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    for H in (3, 4):
        for r in (2, 3):
            for Kf in (2, 4):
                K = Kf * H; rng = random.Random(3); W = []; par = grow_reg(16, H, r, K, n, rng, W)
                g = growth_exponent([(a, b) for a, b, _ in W]); gu = growth_exponent([(a, c) for a, _, c in W])
                sb = sample_intervals(par, rng, 500, 40); sm = summarize(sb)
                print(f"H={H} r={r} K={K}: slice exp {g:.2f} (units exp {gu:.2f}, final units {W[-1][2]}), counts {sm['counts']}, "
                      f"d_MM {[round(v,2) if v==v else None for v in sm['d_mm']]}, d_mid {sm['d_mid_largest'] if sm['d_mid_largest']==sm['d_mid_largest'] else None}", flush=True)
