"""R5: thinning an all-to-all start with few quanta per place.

Regime R4 missed: n0 places >> quanta per place. Every pair starts related.
Each step a place sends each of its quanta across one relation; a relation that
carries nothing for W steps is gone.

Variant A (no pairing): the quantum picks a uniformly random surviving relation.
Variant B (pairing by first passage): a quantum arriving by relation r leaves by
the relation paired with r at that place; if r has no partner yet, a random
unpaired relation is chosen and the pair is recorded (kept). A quantum with no
incoming relation (initial step) picks at random.

Measured on the largest component: mean degree, spectral dimension from the
random-walk return probability, neighbourhood growth exponent.
Registered expectation: A gives a random graph of degree ~P/hbar, expander-like,
spectral dimension large. B gives a union of lines; dimension unknown, which is
the point. No mismatch cost in either: this run isolates what thinning and
pairing do on their own.
"""
import numpy as np, json
rng = np.random.default_rng(3)

def run(n0=400, q=6, W=4, T=120, pairing=False):
    alive = np.ones((n0, n0), bool); np.fill_diagonal(alive, False)
    idle = np.zeros((n0, n0), int)
    # quanta: list of (place, came_from or -1)
    quanta = [(i, -1) for i in range(n0) for _ in range(q)]
    partner = {}  # (place, rel) -> rel
    for t in range(T):
        crossed = np.zeros((n0, n0), bool)
        nq = []
        for (i, frm) in quanta:
            nb = np.flatnonzero(alive[i])
            if len(nb) == 0: nq.append((i, -1)); continue
            j = None
            if pairing and frm >= 0 and alive[i, frm]:
                key = (i, frm)
                if key in partner and alive[i, partner[key]]:
                    j = partner[key]
                else:
                    # pick an unpaired relation (not frm) if possible
                    paired = {partner[k] for k in partner if k[0] == i} | {k[1] for k in partner if k[0] == i}
                    cands = [x for x in nb if x != frm and x not in paired]
                    if not cands: cands = [x for x in nb if x != frm] or list(nb)
                    j = int(cands[rng.integers(len(cands))])
                    partner[(i, frm)] = j; partner[(i, j)] = frm
            if j is None:
                j = int(nb[rng.integers(len(nb))])
            crossed[i, j] = crossed[j, i] = True
            nq.append((j, i))
        quanta = nq
        idle[~crossed & alive] += 1
        idle[crossed] = 0
        dead = alive & (idle >= W)
        alive[dead] = False
    return alive

def analyse(alive):
    n = alive.shape[0]
    # largest component
    seen = np.zeros(n, bool); best = []
    for s in range(n):
        if seen[s]: continue
        comp = [s]; seen[s] = True; k = 0
        while k < len(comp):
            u = comp[k]; k += 1
            for v in np.flatnonzero(alive[u]):
                if not seen[v]: seen[v] = True; comp.append(v)
        if len(comp) > len(best): best = comp
    idx = np.array(best); A = alive[np.ix_(idx, idx)].astype(float)
    deg = A.sum(1); deg[deg == 0] = 1; Pm = A / deg[:, None]
    m = len(idx); M = np.eye(m); pt = []
    for t in range(1, 121):
        M = M @ Pm; pt.append(np.trace(M) / m)
    pt = np.array(pt); ts = np.arange(1, 121)
    # spectral dimension from the window before saturation (p(t) -> 1/m)
    sat = 2.0 / m
    win = (pt > sat) & (ts >= 4)
    ds = float('nan')
    if win.sum() > 6:
        s_ = np.polyfit(np.log(ts[win]), np.log(pt[win]), 1)[0]; ds = -2 * s_
    # growth
    counts = np.zeros(8)
    for s in idx[:150]:
        dist = {s: 0}; fr = [s]
        for r in range(1, 8):
            nx = []
            for u in fr:
                for v in np.flatnonzero(alive[u]):
                    if v not in dist: dist[v] = r; nx.append(v)
            fr = nx
        for r in range(8): counts[r] += sum(1 for d in dist.values() if d <= r)
    counts /= min(150, m)
    rs = np.arange(1, 8); ge = np.polyfit(np.log(rs[:4]), np.log(counts[1:5]), 1)[0]
    return {"component": int(m), "of": int(n), "mean_degree": float(A.sum(1).mean()),
            "spectral_dimension": float(ds), "growth_exponent_r1_4": float(ge),
            "N_within_r": [round(c, 1) for c in counts]}

out = {}
for name, pr in [("A_no_pairing", False), ("B_pairing", True)]:
    out[name] = analyse(run(pairing=pr))
    print(name, out[name])
json.dump(out, open("r5_result.json", "w"), indent=1)
