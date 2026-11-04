"""R7: a global curvature cost on which relations are kept.

Relations are kept, not made: any pair may survive. Quanta per place are fixed, so the
count of relations is fixed and the degree is fixed. The cost is the sum over relations
of Ollivier curvature squared, E = sum_e kappa_e^2, flat = 0. Dynamics: degree-preserving
swaps of two relations, (a,b),(c,d) -> (a,d),(c,b), accepted by Metropolis at low
temperature. Start: a random regular graph (what thinning leaves, R5 A).

Reference: kappa on a true grid of the same degree (2D grid for degree 4, 3D for 6),
computed with the same definition, so the target value is known rather than assumed.

Measured on the annealed graph: mean kappa, fraction of relations in 4-cycles,
neighbourhood growth N(r) and its ratios, against the start and the reference grid.
Registered expectation: unknown. If annealing drives kappa to the grid value and growth
toward polynomial with ratios like the grid's, a global cost supplies locality. If kappa
falls but growth stays exponential, the cost finds something flat that is not a lattice.
"""
import numpy as np, json, sys, time
from scipy.optimize import linprog
rng = np.random.default_rng(7)

def neighbors(adj, i): return adj[i]

def bfs(adj, src, maxd):
    d = {src: 0}; fr = [src]
    for r in range(1, maxd + 1):
        nx = []
        for u in fr:
            for v in adj[u]:
                if v not in d: d[v] = r; nx.append(v)
        fr = nx
    return d

def kappa(adj, i, j, cache=None):
    Ni = sorted(adj[i]); Nj = sorted(adj[j])
    if not Ni or not Nj: return -1.0
    C = np.zeros((len(Ni), len(Nj)))
    for a, u in enumerate(Ni):
        d = bfs(adj, u, 3)
        for b, v in enumerate(Nj): C[a, b] = d.get(v, 4)
    n, m = C.shape
    A = np.zeros((n + m, n * m)); b = np.concatenate([np.full(n, 1/n), np.full(m, 1/m)])
    for a in range(n): A[a, a*m:(a+1)*m] = 1
    for bb in range(m): A[n + bb, bb::m] = 1
    r = linprog(C.ravel(), A_eq=A, b_eq=b, bounds=(0, None), method="highs")
    return 1.0 - (r.fun if r.success else 4.0)

def edges_near(adj, nodes, hops=1):
    S = set(nodes)
    for _ in range(hops):
        S |= {v for u in list(S) for v in adj[u]}
    E = set()
    for u in S:
        for v in adj[u]: E.add((min(u, v), max(u, v)))
    return E

def total_cost(adj, kap):
    return sum(k * k for k in kap.values())

def all_edges(adj):
    return {(min(u, v), max(u, v)) for u in adj for v in adj[u]}

def random_regular(n, d):
    # configuration model with rejection of loops/multi-edges (simple retry)
    while True:
        stubs = np.repeat(np.arange(n), d); rng.shuffle(stubs)
        adj = {i: set() for i in range(n)}; ok = True
        for a, b in zip(stubs[::2], stubs[1::2]):
            a, b = int(a), int(b)
            if a == b or b in adj[a]: ok = False; break
            adj[a].add(b); adj[b].add(a)
        if ok: return adj

def grid(dims):
    import itertools
    shape = dims; idx = {p: k for k, p in enumerate(itertools.product(*[range(s) for s in shape]))}
    adj = {k: set() for k in idx.values()}
    for p, k in idx.items():
        for ax in range(len(shape)):
            q = list(p); q[ax] = (q[ax] + 1) % shape[ax]; adj[k].add(idx[tuple(q)]); adj[idx[tuple(q)]].add(k)
    return adj

def growth(adj, rmax=6, sample=120):
    nodes = list(adj); counts = np.zeros(rmax + 1)
    for s in nodes[:sample]:
        d = bfs(adj, s, rmax)
        for r in range(rmax + 1): counts[r] += sum(1 for x in d.values() if x <= r)
    counts /= min(sample, len(nodes))
    return [round(c, 1) for c in counts], [round(counts[r+1]/counts[r], 2) for r in range(1, rmax)]

def frac_in_4cycles(adj):
    E = all_edges(adj); c = 0
    for (u, v) in E:
        if any(len((adj[w] & adj[v]) - {u}) > 0 for w in adj[u] if w != v): c += 1
    return c / len(E)

def anneal(adj, sweeps, T, log):
    E = all_edges(adj); kap = {e: kappa(adj, *e) for e in E}
    cost = total_cost(adj, kap); edges = list(E); t0 = time.time(); acc = 0
    for s in range(sweeps):
        (a, b) = edges[rng.integers(len(edges))]; (c, d) = edges[rng.integers(len(edges))]
        if len({a, b, c, d}) < 4 or d in adj[a] or b in adj[c]: continue
        near = edges_near(adj, [a, b, c, d], 1)
        old = {e: kap[e] for e in near if e in kap}
        # apply swap
        adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
        adj[a].add(d); adj[d].add(a); adj[c].add(b); adj[b].add(c)
        near2 = edges_near(adj, [a, b, c, d], 1)
        new = {e: kappa(adj, *e) for e in near2}
        dE = sum(k*k for k in new.values()) - sum(k*k for k in old.values())
        # edges that left 'near' set but changed: ignore (approximation)
        if dE <= 0 or rng.random() < np.exp(-dE / T):
            for e in old: kap.pop(e, None)
            kap.update(new); cost += dE; acc += 1
            edges = list(all_edges(adj))
        else:
            adj[a].discard(d); adj[d].discard(a); adj[c].discard(b); adj[b].discard(c)
            adj[a].add(b); adj[b].add(a); adj[c].add(d); adj[d].add(c)
        if (s + 1) % max(1, sweeps // 5) == 0:
            mk = np.mean(list(kap.values()))
            log.append({"step": s + 1, "accepted": acc, "mean_kappa": float(mk), "secs": round(time.time() - t0)})
    return adj, kap

if __name__ == "__main__":
    n, d, sweeps = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (256, 4, 3000)
    out = {}
    ref = grid((16, 16)) if d == 4 else grid((6, 6, 6))
    rk = [kappa(ref, *e) for e in list(all_edges(ref))[:60]]
    out["reference_grid"] = {"mean_kappa": float(np.mean(rk)), "growth": growth(ref)[1], "frac_4cycles": frac_in_4cycles(ref)}
    adj = random_regular(n, d)
    E0 = all_edges(adj); k0 = [kappa(adj, *e) for e in list(E0)[:60]]
    out["start_random_regular"] = {"mean_kappa": float(np.mean(k0)), "growth": growth(adj)[1], "frac_4cycles": frac_in_4cycles(adj)}
    log = []
    adj, kap = anneal(adj, sweeps, T=0.02, log=log)
    out["annealed"] = {"mean_kappa": float(np.mean(list(kap.values()))), "growth": growth(adj)[1],
                       "N_within_r": growth(adj)[0], "frac_4cycles": frac_in_4cycles(adj), "log": log}
    json.dump(out, open(f"r7_result_n{n}_d{d}.json", "w"), indent=1)
    for k, v in out.items(): print(k, {kk: vv for kk, vv in v.items() if kk != "log"})
    print("log", log)
