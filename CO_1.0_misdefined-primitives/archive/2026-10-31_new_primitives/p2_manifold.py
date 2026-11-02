"""P2 (P2_manifoldlike.md): is C7 growth manifold-like? Myrheim-Meyer and chain dimensions on intervals, with sprinkled-diamond
(2D, 4D) and transitive-percolation controls. python3 -B p2_manifold.py [smoke|registered]"""
import sys, json, math, random
import numpy as np
from scipy.special import gamma
from scipy.optimize import brentq
sys.dont_write_bytecode = True
BINS = [(50, 100), (200, 400), (800, 1600)]
def f_of_d(d): return gamma(d + 1) * gamma(d / 2) / (2 * gamma(3 * d / 2))   # ordering fraction R/C(N,2); f(2)=1/2, f(4)=1/10
def d_mm(frac):
    if not (f_of_d(8.0) < frac < f_of_d(1.0001)): return float("nan")
    return brentq(lambda d: f_of_d(d) - frac, 1.0001, 8.0)

# ---------------- growth laws: return parent lists (natural labelling) ----------------
def grow_c7(U, H, n, rng):
    M = U // H; holder = [u // H for u in range(U)]; parents = [[] for _ in range(M)]
    for k in range(n):
        x = M + k; S = rng.sample(range(U), H); ps = sorted(set(holder[u] for u in S))
        parents.append(ps)
        for u in S: holder[u] = x
    return parents
def grow_tp(n, p, rng):
    parents = []
    for x in range(n):
        parents.append([a for a in range(x) if rng.random() < p])
    return parents

def bitsets(parents):
    N = len(parents); anc = [0] * N; ch = [[] for _ in range(N)]
    for x, ps in enumerate(parents):
        a = 0
        for p in ps: a |= anc[p] | (1 << p); ch[p].append(x)
        anc[x] = a
    desc = [0] * N
    for x in range(N - 1, -1, -1):
        d = 0
        for c in ch[x]: d |= desc[c] | (1 << c)
        desc[x] = d
    return anc, desc

def interval_stats(parents, anc, I):
    """I: bitmask of the open interval. Returns N, ordering fraction, longest chain (DP over parent links; exact by convexity)."""
    idx = [i for i in range(I.bit_length()) if I >> i & 1]; N = len(idx)
    if N < 2: return N, float("nan"), N
    R = sum(bin(anc[b] & I).count("1") for b in idx)
    L = {}
    for b in idx:                      # natural labelling: parents have smaller index
        L[b] = 1 + max((L[p] for p in parents[b] if I >> p & 1), default=0)
    return N, R / (N * (N - 1) / 2), max(L.values())

def midpoint_dim(I, anc, desc, x, y):
    """midpoint scaling: N_half = max_z min(|I(x,z)|, |I(z,y)|); d_mid = log2(N / N_half) (Reid)."""
    idx = [i for i in range(I.bit_length()) if I >> i & 1]; N = len(idx)
    best = max(min(bin(anc[z] & desc[x]).count("1"), bin(desc[z] & anc[y]).count("1")) for z in idx)
    return math.log2(N / best) if best > 0 else float("nan")

def sample_intervals(parents, rng, burn, per_bin, tries=6000):
    anc, desc = bitsets(parents); n = len(parents); out = {b: [] for b in BINS}
    for _ in range(tries):
        if all(len(out[b]) >= per_bin for b in BINS): break
        x = rng.randrange(burn, n - 1)
        # pick y by a geometric gap so that interval sizes span the bins
        g = int(math.exp(rng.uniform(math.log(2), math.log(max(3, n - x - 1)))))
        y = min(n - 1, x + g)
        I = desc[x] & anc[y]
        N = bin(I).count("1")
        for b in BINS:
            if b[0] <= N <= b[1] and len(out[b]) < per_bin:
                out[b].append(interval_stats(parents, anc, I) + (midpoint_dim(I, anc, desc, x, y),)); break
    return out

# ---------------- sprinkled diamonds ----------------
def sprinkle(N, d, rng):
    """N points uniform in the causal diamond |x| <= min(t, 1-t), t in [0,1], d-dim Minkowski. Returns relation matrix (i<j by t)."""
    pts = []
    while len(pts) < N:
        t = rng.random(); x = np.array([rng.uniform(-0.5, 0.5) for _ in range(d - 1)])
        if np.linalg.norm(x) <= min(t, 1 - t): pts.append((t, x))
    pts.sort(key=lambda q: q[0]); T = np.array([q[0] for q in pts]); X = np.array([q[1] for q in pts])
    dt = T[None, :] - T[:, None]; dx = np.linalg.norm(X[None, :, :] - X[:, None, :], axis=2)
    return (dt > dx)                  # rel[i, j]: i precedes j
def diamond_stats(N, d, rng):
    rel = sprinkle(N, d, rng); R = rel.sum(); L = np.ones(N, dtype=int)
    for j in range(N):
        prev = np.nonzero(rel[:, j])[0]
        if len(prev): L[j] = 1 + L[prev].max()
    past, fut = rel.sum(axis=0), rel.sum(axis=1); best = int(np.max(np.minimum(past, fut)))
    return N, R / (N * (N - 1) / 2), int(L.max()), (math.log2(N / best) if best > 0 else float("nan"))

def summarize(bins):
    med_d, logs = [], []
    for b in BINS:
        rows = bins.get(b, [])
        ds = [d_mm(r[1]) for r in rows]; ds = [v for v in ds if not math.isnan(v)]
        med_d.append(float(np.median(ds)) if ds else float("nan"))
        logs += [(math.log(r[0]), math.log(r[2])) for r in rows if r[2] > 0]
        if b == BINS[-1]:
            dm = [r[3] for r in rows if not math.isnan(r[3])]; med_mid = float(np.median(dm)) if dm else float("nan")
    counts = [len(bins.get(b, [])) for b in BINS]
    if len(logs) >= 3 and len(set(round(a, 3) for a, _ in logs)) > 1:
        A = np.array(logs); slope = np.polyfit(A[:, 0], A[:, 1], 1)[0]; dL = 1 / slope if slope > 0 else float("nan")
    else: dL = float("nan")
    ok_counts = all(c >= 30 for c in counts)
    spread = (max(med_d) - min(med_d)) if ok_counts and not any(math.isnan(v) for v in med_d) else float("nan")
    c1 = spread <= 0.3; c2 = (abs(med_d[-1] - med_mid) <= 0.5) if not (math.isnan(med_mid) or math.isnan(med_d[-1])) else False
    c3 = ok_counts and all(1.5 <= v <= 6 for v in med_d if not math.isnan(v)) and not any(math.isnan(v) for v in med_d)
    return dict(counts=counts, d_mm=med_d, d_mid_largest=med_mid, d_L_reported=float(dL), spread=spread, scale_ok=bool(c1), est_ok=bool(c2), nondeg_ok=bool(c3),
                PASS=bool(c1 and c2 and c3))

def main(tag):
    res = {}; per = 200 if tag == "registered" else 40
    reg = tag == "registered"
    configs = [(U, H) for U in (16, 64, 256) for H in (2, 3, 4)] if reg else [(16, 2)]
    n = 4000 if reg else 1500
    for d in (2, 4):
        rng = random.Random(1000 + d); bins = {}
        for b in BINS:
            k = per // 4 if reg else 8
            bins[b] = [diamond_stats(rng.randint(*b), d, rng) for _ in range(k)]
        res[f"diamond_{d}D"] = summarize(bins); print(f"diamond {d}D:", res[f"diamond_{d}D"], flush=True)
    rng = random.Random(7); par = grow_tp(n, 0.05, rng)
    res["TP_p0.05"] = summarize(sample_intervals(par, rng, 500 if reg else 200, per)); print("TP:", res["TP_p0.05"], flush=True)
    for U, H in configs:
        bins = {b: [] for b in BINS}
        for seed in (1, 2):
            rng = random.Random(seed * 100 + U + H); par = grow_c7(U, H, n, rng)
            sb = sample_intervals(par, rng, (500 if reg else 200) + U // H, per // 2)
            for b in BINS: bins[b] += sb[b]
        res[f"C7_U{U}_H{H}"] = summarize(bins); print(f"C7 U={U} H={H}:", res[f"C7_U{U}_H{H}"], flush=True)
    if reg:
        ctrl = res["diamond_2D"]["PASS"] and res["diamond_4D"]["PASS"]
        surv = [k for k in res if k.startswith("C7") and res[k]["PASS"]]
        R = ("A SURVIVES: " + ", ".join(surv)) if surv else "A FAILS AS STATED"
        if not ctrl: R = "BUG SIGNAL: a positive control failed; no reading"
        res["reading"] = R; print("READING:", R)
        json.dump(res, open("p2_result.json", "w"), indent=1)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "smoke")
