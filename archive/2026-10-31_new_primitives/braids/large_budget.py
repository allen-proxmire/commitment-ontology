"""Large-budget behaviour of principle S.
Counts positive braids (elements of the positive monoid B_n^+) of length L by their permutation,
using left-greedy (Garside) normal forms: s1 s2 ... sk, si non-trivial simple, S(s_{i+1}) subset of F(s_i).
Sustaining share (element level) = fraction whose permutation is an n-cycle (this forces every generator
to be used; proper powers are exponentially rare). Budget B = n + L."""
import itertools, sys, numpy as np

def setup(n):
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    inv = lambda w: sum(1 for i in range(n) for j in range(i+1, n) if w[i] > w[j])
    def mask_right(w):  # right descents: positions i with w[i] > w[i+1]
        return sum(1 << i for i in range(n-1) if w[i] > w[i+1])
    def mask_left(w):   # left descents: value i+1 appears before value i
        pos = [0]*n
        for k, v in enumerate(w): pos[v] = k
        return sum(1 << i for i in range(n-1) if pos[i+1] < pos[i])
    comp = lambda u, v: tuple(u[v[j]] for j in range(n))  # (u v)(j) = u(v(j))
    def ncycle(w):
        seen, j, c = set(), 0, 0
        while j not in seen: seen.add(j); j = w[j]; c += 1
        return c == n
    return perms, idx, inv, mask_right, mask_left, comp, ncycle

def shares(n, Lmax):
    perms, idx, inv, mr, ml, comp, ncycle = setup(n)
    m, M = len(perms), 1 << (n-1)
    ident = tuple(range(n))
    simples = [w for w in perms if w != ident]
    # right-multiplication index maps: new_perm_index[g] = idx(g * s)
    mul = {s: np.array([idx[comp(g, s)] for g in perms]) for s in simples}
    dp = np.zeros((Lmax+1, M, m))   # dp[L][F of last factor][accumulated perm]
    tot = np.zeros(Lmax+1); cyc = np.zeros(Lmax+1)
    full = M - 1
    dp[0, full, idx[ident]] = 1.0   # empty word: any first factor allowed
    iscyc = np.array([ncycle(p) for p in perms])
    for L in range(Lmax+1):
        tot[L] = dp[L].sum(); cyc[L] = dp[L][:, iscyc].sum()
        # superset sums over F
        G = dp[L].copy()
        for b in range(n-1):
            for T in range(M):
                if not T >> b & 1: G[T] += G[T | 1 << b]
        for s in simples:
            Ln = L + inv(s)
            if Ln > Lmax: continue
            src = G[ml(s)]
            np.add.at(dp[Ln, mr(s)], mul[s], src)
    return tot, cyc

if __name__ == "__main__":
    Bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 61
    t, _ = shares(3, 8)
    print("check B3+ counts:", [int(x) for x in t], "(expect 1,2,4,7,12,20,33,54,88)")
    res = {}
    for n in (3, 4, 5, 6):
        res[n] = shares(n, Bmax - n)
    print("B  " + "  ".join(f"n={n:>1}  " for n in (2, 3, 4, 5, 6)))
    for B in range(9, Bmax+1, 2):
        row = [0.0 if B > 3 else 1.0]  # n=2: only sigma1^L, primitive only at L=1
        for n in (3, 4, 5, 6):
            tot, cyc = res[n]; L = B - n
            row.append(cyc[L]/tot[L])
        best = (2, 3, 4, 5, 6)[int(np.argmax(row))]
        print(f"{B:<3}" + "  ".join(f"{x:.4f}" for x in row) + f"   max n={best}")
    print("even B: n-cycle needs L = n-1 mod 2, so B = n+L is odd; shares at even B are 0 for every n")
    for n in (3, 4, 5, 6):
        tot, cyc = res[n]
        print(f"n={n}: share at L={Bmax-n} is {cyc[Bmax-n]/tot[Bmax-n]:.4f}; 2/n = {2/n:.4f}")
