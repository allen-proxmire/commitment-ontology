import sys, itertools
import numpy as np
def classes(n, L):
    """Union-find over all positive words of length L in sigma_1..sigma_{n-1} (letters 0..n-2), closing under the
    positive braid relations (far commutation, braid triple) and single-letter cyclic rotation. Returns (n_classes, n_sustaining)."""
    k = n - 1; N = k ** L
    parent = np.arange(N, dtype=np.int64)
    def find(x):
        r = x
        while parent[r] != r: r = parent[r]
        while parent[x] != r: parent[x], x = r, parent[x]
        return r
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb: parent[max(ra, rb)] = min(ra, rb)
    pw = [k ** (L - 1 - i) for i in range(L)]
    def enc(w): return sum(c * pw[i] for i, c in enumerate(w))
    words = itertools.product(range(k), repeat=L)
    for idx, w in enumerate(words):
        # rotation
        union(idx, enc(w[1:] + w[:1]))
        for i in range(L - 1):
            a, b = w[i], w[i + 1]
            if abs(a - b) >= 2:
                v = list(w); v[i], v[i + 1] = b, a; union(idx, enc(v))
        for i in range(L - 2):
            a, b, c = w[i], w[i + 1], w[i + 2]
            if a == c and abs(a - b) == 1:
                v = list(w); v[i], v[i + 1], v[i + 2] = b, a, b; union(idx, enc(v))
    # class properties
    roots = {}
    for idx, w in enumerate(itertools.product(range(k), repeat=L)):
        r = find(idx)
        info = roots.get(r)
        if info is None:
            letters = set(w)
            p = list(range(n))
            for g in w: p[g], p[g + 1] = p[g + 1], p[g]
            x = 0; c = 0
            while True:
                x = p[x]; c += 1
                if x == 0: break
            info = [len(letters) == k, c == n, True]
            roots[r] = info
        if info[2]:
            for d in range(1, L):
                if L % d == 0 and w == w[:d] * (L // d): info[2] = False; break
    tot = len(roots); sus = sum(1 for v in roots.values() if all(v))
    return tot, sus
if __name__ == "__main__":
    for spec in sys.argv[1:]:
        B, n = map(int, spec.split(','))
        L = B - n
        if L < n - 1: print(f"B={B} n={n}: -"); continue
        t, s = classes(n, L); print(f"B={B} n={n} L={L}: classes {t}, sustaining {s}, share {s/t:.4f}", flush=True)
