"""R6: R5's thinning and pairing, with the mismatch cost selecting among lines.

"Out of step" on a bare graph. Transporting a transverse line around a loop needs an
identification of lines at neighbouring places that a bare graph does not have, so
the pairing-only definition does not close. What a bare graph does carry is an
intrinsic curvature: Ollivier's, kappa(i,j) = 1 - W1(m_i, m_j)/d(i,j), with m_i the
uniform measure on i's neighbours and W1 the transport cost in graph distance.
Trees and expanders are negative, cliques positive, lattices near zero. It depends on
nothing but which relations exist (slide-invariant by construction). Candidate: the
mismatch cost is kappa^2, and flat means kappa = 0.

Selection: at a quantum's first passage through a place, among the unpaired relations
the one chosen as partner is the one whose kappa on the current graph is nearest zero.
Everything else is R5 (variant B).

Registered expectation: unknown. If selection for kappa = 0 makes neighbourhood growth
polynomial and the exponent stable with system size, locality has come from the cost
and the sentence closes; the exponent is then the dimension and can be set against the
quanta per place. If growth stays exponential, the cost as defined does not supply
locality and the definition is wrong or insufficient.
"""
import numpy as np, json, sys
from scipy.optimize import linprog
rng = np.random.default_rng(5)

def bfs_dist(alive, src, maxd=3):
    d = {src: 0}; fr = [src]
    if alive[src].sum() > 60:   # dense early graph: everything is within two hops
        for v in np.flatnonzero(alive[src]): d[v] = 1
        return d
    for r in range(1, maxd + 1):
        nx = []
        for u in fr:
            for v in np.flatnonzero(alive[u]):
                if v not in d: d[v] = r; nx.append(v)
        fr = nx
    return d

def kappa(alive, i, j):
    Ni = np.flatnonzero(alive[i]); Nj = np.flatnonzero(alive[j])
    if len(Ni) == 0 or len(Nj) == 0: return -1.0
    if len(Ni) > 10: Ni = rng.choice(Ni, 10, replace=False)
    if len(Nj) > 10: Nj = rng.choice(Nj, 10, replace=False)
    # distances from each of Ni to each of Nj (cap 3)
    C = np.zeros((len(Ni), len(Nj)))
    for a, u in enumerate(Ni):
        d = bfs_dist(alive, u, 3)
        for b, v in enumerate(Nj): C[a, b] = d.get(v, 4)
    # transport LP
    n, m = C.shape
    A_eq = np.zeros((n + m, n * m)); b_eq = np.concatenate([np.full(n, 1/n), np.full(m, 1/m)])
    for a in range(n): A_eq[a, a*m:(a+1)*m] = 1
    for b in range(m): A_eq[n + b, b::m] = 1
    res = linprog(C.ravel(), A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method="highs")
    W = res.fun if res.success else 4.0
    return 1.0 - W

def run(n0=400, q=8, W=6, T=150, select=True):
    alive = np.ones((n0, n0), bool); np.fill_diagonal(alive, False)
    idle = np.zeros((n0, n0), int)
    quanta = [(i, -1) for i in range(n0) for _ in range(q)]
    partner = {}
    for t in range(T):
        crossed = np.zeros((n0, n0), bool); nq = []
        for (i, frm) in quanta:
            nb = np.flatnonzero(alive[i])
            if len(nb) == 0: nq.append((i, -1)); continue
            j = None
            if frm >= 0 and alive[i, frm]:
                key = (i, frm)
                if key in partner and alive[i, partner[key]]:
                    j = partner[key]
                else:
                    paired = {partner[k] for k in partner if k[0] == i} | {k[1] for k in partner if k[0] == i}
                    cands = [x for x in nb if x != frm and x not in paired]
                    if not cands: cands = [x for x in nb if x != frm] or list(nb)
                    if select and len(cands) > 1 and len(nb) <= 30:  # dense phase: random; selection acts once thinning has begun
                        cs = cands if len(cands) <= 12 else list(rng.choice(cands, 12, replace=False))
                        ks = [abs(kappa(alive, i, int(x))) for x in cs]
                        j = int(cs[int(np.argmin(ks))])
                    else:
                        j = int(cands[rng.integers(len(cands))])
                    partner[(i, frm)] = j; partner[(i, j)] = frm
            if j is None: j = int(nb[rng.integers(len(nb))])
            crossed[i, j] = crossed[j, i] = True
            nq.append((j, i))
        quanta = nq
        idle[~crossed & alive] += 1; idle[crossed] = 0
        alive[alive & (idle >= W)] = False
    return alive

def analyse(alive):
    n = alive.shape[0]; seen = np.zeros(n, bool); best = []
    for s in range(n):
        if seen[s]: continue
        comp = [s]; seen[s] = True; k = 0
        while k < len(comp):
            u = comp[k]; k += 1
            for v in np.flatnonzero(alive[u]):
                if not seen[v]: seen[v] = True; comp.append(v)
        if len(comp) > len(best): best = comp
    idx = np.array(best); m = len(idx)
    deg = alive[idx].sum(1)
    counts = np.zeros(8)
    for s in idx[:150]:
        d = bfs_dist(alive, s, 7)
        for r in range(8): counts[r] += sum(1 for x in d.values() if x <= r)
    counts /= min(150, m)
    ratios = [round(counts[r+1]/counts[r], 2) for r in range(1, 5)]
    # mean |kappa| over a sample of surviving relations
    es = np.argwhere(np.triu(alive)); sample = es[rng.choice(len(es), min(150, len(es)), replace=False)]
    mk = float(np.mean([abs(kappa(alive, int(a), int(b))) for a, b in sample]))
    return {"component": int(m), "of": int(n), "mean_degree": float(deg.mean()),
            "N_within_r": [round(c, 1) for c in counts], "growth_ratios_r1_5": ratios,
            "mean_abs_kappa": mk}

if __name__ == "__main__":
    sizes = [int(x) for x in sys.argv[1:]] or [400]
    out = {}
    for n0 in sizes:
        rng = np.random.default_rng(5)
        out[f"select_n0={n0}"] = analyse(run(n0=n0)); print(n0, out[f"select_n0={n0}"], flush=True)
    json.dump(out, open("r6_result.json", "w"), indent=1)
