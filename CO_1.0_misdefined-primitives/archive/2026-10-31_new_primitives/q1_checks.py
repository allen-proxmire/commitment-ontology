# Q1 checks. (a) a mixing (non-permutation) invertible linear map preserves sum|a|^p for all states only at p = 2 (Aaronson 2004).
import numpy as np
rng = np.random.default_rng(1)
def haar(n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2); q, r = np.linalg.qr(z)
    return q * (np.diag(r) / abs(np.diag(r)))
U = haar(4); states = [ (rng.normal(size=4) + 1j*rng.normal(size=4)) for _ in range(200)]
for p in [1, 1.5, 2, 3, 4]:
    dev = max(abs(np.sum(abs(U@s)**p) - np.sum(abs(s)**p)) / np.sum(abs(s)**p) for s in states)
    print(f"(a) Haar-unitary hop, p={p}: max relative change of sum|a|^p = {dev:.2e}")
# a phase-permutation (no mixing) preserves every p-norm: the only exception
Pm = np.zeros((4, 4), complex); perm = [2, 0, 3, 1]
for i, j in enumerate(perm): Pm[i, j] = np.exp(1j * rng.uniform(0, 6.28))
print("(a) phase-permutation, p=3:", max(abs(np.sum(abs(Pm@s)**3) - np.sum(abs(s)**3)) for s in states))
# (b) see p7_phase.py. Joint statement: (a) fixes the conserved quantity to sum|a|^2; (b) fixes the outcome weight to |a|^2 independently.
