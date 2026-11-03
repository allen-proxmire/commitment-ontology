"""R7b: same cost, targeted proposals (a search heuristic, not physics):
the first relation is drawn with weight kappa^2 (worst first), the second from relations
within two hops of its ends, so swaps can close short loops. Metropolis as before."""
import json, sys, time, numpy as np
src = open("r7_global_cost.py").read().split('if __name__ == "__main__":')[0]
ns = {}; exec(src, ns); rng = ns["rng"]
kappa, edges_near, all_edges, growth, frac4, bfs = ns["kappa"], ns["edges_near"], ns["all_edges"], ns["growth"], ns["frac_in_4cycles"], ns["bfs"]

def anneal_t(adj, sweeps, T, log):
    E = list(all_edges(adj)); kap = {e: kappa(adj, *e) for e in E}; t0 = time.time(); acc = 0
    for s in range(sweeps):
        E = list(kap.keys()); w = np.array([kap[e]**2 + 1e-3 for e in E]); w /= w.sum()
        (a, b) = E[rng.choice(len(E), p=w)]
        near = {v for u in (a, b) for v in bfs(adj, u, 2)} - {a, b}
        cand = [(u, v) for u in near for v in adj[u] if v in near and u < v and len({a, b, u, v}) == 4]
        if not cand: continue
        (c, d) = cand[rng.integers(len(cand))]
        if rng.random() < 0.5: c, d = d, c
        if d in adj[a] or b in adj[c]: continue
        ne = edges_near(adj, [a, b, c, d], 1); old = {e: kap[e] for e in ne if e in kap}
        adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
        adj[a].add(d); adj[d].add(a); adj[c].add(b); adj[b].add(c)
        ne2 = edges_near(adj, [a, b, c, d], 1); new = {e: kappa(adj, *e) for e in ne2}
        dE = sum(k*k for k in new.values()) - sum(k*k for k in old.values())
        if dE <= 0 or rng.random() < np.exp(-dE / T):
            for e in old: kap.pop(e, None)
            kap.update(new); acc += 1
        else:
            adj[a].discard(d); adj[d].discard(a); adj[c].discard(b); adj[b].discard(c)
            adj[a].add(b); adj[b].add(a); adj[c].add(d); adj[d].add(c)
        if (s + 1) % max(1, sweeps // 4) == 0:
            log.append({"step": s + 1, "accepted": acc, "mean_kappa": float(np.mean(list(kap.values()))), "secs": round(time.time() - t0)})
    return adj, kap

n, d, sweeps, T, state = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
try:
    edges = json.load(open(state)); adj = {i: set() for i in range(n)}
    for u, v in edges: adj[u].add(v); adj[v].add(u)
except FileNotFoundError:
    adj = ns["random_regular"](n, d)
log = []; adj, kap = anneal_t(adj, sweeps, T, log)
json.dump([list(e) for e in all_edges(adj)], open(state, "w"))
g = growth(adj); res = {"T": T, "sweeps": sweeps, "mean_kappa": float(np.mean(list(kap.values()))),
    "frac_kappa_zero": float(np.mean([abs(k) < 0.05 for k in kap.values()])), "growth": g[1], "N_within_r": g[0], "frac_4cycles": frac4(adj), "log": log}
json.dump(res, open(state.replace(".json", "_last.json"), "w"), indent=1)
print({k: v for k, v in res.items() if k != "log"}); print(log[-1])
