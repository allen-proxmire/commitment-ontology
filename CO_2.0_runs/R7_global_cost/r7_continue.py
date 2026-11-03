"""Continuation legs for R7: load/save the relation set so annealing can run in legs."""
import json, sys, numpy as np
src = open("r7_global_cost.py").read().split('if __name__ == "__main__":')[0]
ns = {}; exec(src, ns)
n, d, sweeps, T, state = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
try:
    edges = json.load(open(state)); adj = {i: set() for i in range(n)}
    for u, v in edges: adj[u].add(v); adj[v].add(u)
except FileNotFoundError:
    adj = ns["random_regular"](n, d)
log = []
adj, kap = ns["anneal"](adj, sweeps, T, log)
json.dump([list(e) for e in ns["all_edges"](adj)], open(state, "w"))
g = ns["growth"](adj)
res = {"T": T, "sweeps": sweeps, "mean_kappa": float(np.mean(list(kap.values()))), "growth": g[1], "N_within_r": g[0],
       "frac_4cycles": ns["frac_in_4cycles"](adj), "log": log}
json.dump(res, open(state.replace(".json", "_last.json"), "w"), indent=1)
print({k: v for k, v in res.items() if k != "log"}); print(log[-1])
