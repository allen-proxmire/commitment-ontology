"""G4: does the Wilson-Dirac lattice Hamiltonian admit an exactly conserved, exactly
symmetric stress tensor placed as CO's staggered carriers need (E, P_ii at places;
J_i on links; one P_ij = P_ji per face)?  Linear identities, real space, sparse lstsq.

usage: python3 g4_matter_coupling.py d R m variant
  d = 1, 2 or 3; R = patch range (Chebyshev); m = mass; variant = sym | nosym (control C2)
"""
import sys, itertools, time
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import lsqr

d = int(sys.argv[1]); R = int(sys.argv[2]); m = float(sys.argv[3]); variant = sys.argv[4]
r = 1.0
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex); I2 = np.eye(2)
if d == 1:
    gam = [sx]; beta = sz
elif d == 2:
    gam = [sx, sy]; beta = sz
else:
    gam = [np.kron(sx, s) for s in (sx, sy, sz)]; beta = np.kron(sz, I2)
n = beta.shape[0]
E_ = [tuple(int(a == i) for a in range(d)) for i in range(d)]
def add(a, b): return tuple(x + y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
O = tuple([0] * d)

# H = sum_x sum_disp |x> h[disp] <x+disp| ;  H(k) = sum h[disp] e^{i k.disp}
h = {O: beta * (m + r * d)}
for i in range(d):
    h[E_[i]] = gam[i] / (2j) - (r / 2) * beta
    h[neg(E_[i])] = -gam[i] / (2j) - (r / 2) * beta

# objects and their anchor sites
objs = [('E',)] + [('J', i) for i in range(d)] + [('P', i, i) for i in range(d)]
if variant == 'sym':
    objs += [('P', i, j) for i in range(d) for j in range(i + 1, d)]
else:
    objs += [('F', i, j) for i in range(d) for j in range(d) if i != j]
def anchor(o):
    if o[0] == 'E' or (o[0] == 'P' and o[1] == o[2]): return [O]
    if o[0] == 'J': return [O, E_[o[1]]]
    i, j = o[1], o[2]
    return [O, E_[i], E_[j], add(E_[i], E_[j])]
def patch(o):
    s = set()
    for a in anchor(o):
        for off in itertools.product(range(-R, R + 1), repeat=d):
            s.add(add(a, off))
    return sorted(s)

# variable indexing
var = {}
for o in objs:
    P = patch(o)
    for a in P:
        for b in P:
            for al in range(n):
                for be in range(n):
                    var[(o, a, b, al, be)] = len(var)
nv = len(var)
rows = {}; Ri = []; Ci = []; V = []
def row(key):
    if key not in rows: rows[key] = len(rows)
    return rows[key]
def put(eq, rs, cs, g, dd, col, val):
    Ri.append(row((eq, rs, cs, g, dd))); Ci.append(col); V.append(val)

def comm_contrib(eq, o, shift):
    """i[H, X] for every elementary X of object o translated by shift."""
    P = patch(o)
    for a in P:
        for b in P:
            A = add(a, shift); B = add(b, shift)
            for al in range(n):
                for be in range(n):
                    col = var[(o, a, b, al, be)]
                    # (H X)[c,B] = h[A-c] row c, X = |A al><B be|
                    for disp, hd in h.items():
                        c = add(A, neg(disp))          # H[c,A] = h[A-c] = h[disp]
                        for g in range(n):
                            if hd[g, al] != 0: put(eq, c, B, g, be, col, 1j * hd[g, al])
                        c2 = add(B, disp)              # (X H)[A,c2] = H[B,c2] = h[c2-B]
                        for dl in range(n):
                            if hd[be, dl] != 0: put(eq, A, c2, al, dl, col, -1j * hd[be, dl])
def plain_contrib(eq, o, shift, sign):
    P = patch(o)
    for a in P:
        for b in P:
            A = add(a, shift); B = add(b, shift)
            for al in range(n):
                for be in range(n):
                    put(eq, A, B, al, be, var[(o, a, b, al, be)], sign)

t0 = time.time()
# (I) at place 0
comm_contrib('I', ('E',), O)
for i in range(d):
    plain_contrib('I', ('J', i), O, +1); plain_contrib('I', ('J', i), neg(E_[i]), -1)
# (II_i) at link anchored 0 along i
for i in range(d):
    eq = ('II', i)
    comm_contrib(eq, ('J', i), O)
    plain_contrib(eq, ('P', i, i), E_[i], +1); plain_contrib(eq, ('P', i, i), O, -1)
    for j in range(d):
        if j == i: continue
        o = ('P', min(i, j), max(i, j)) if variant == 'sym' else ('F', i, j)
        plain_contrib(eq, o, O, +1); plain_contrib(eq, o, neg(E_[j]), -1)
# normalisation: sum_x E_x = H  ->  sum_a E0[a, a+disp] = h[disp]
bvals = {}
PE = patch(('E',))
for a in PE:
    for b in PE:
        disp = tuple(y - x for x, y in zip(a, b))
        for al in range(n):
            for be in range(n):
                put('N', O, disp, al, be, var[(('E',), a, b, al, be)], 1.0)
for disp, hd in h.items():
    for al in range(n):
        for be in range(n):
            if hd[al, be] != 0: bvals[row(('N', O, disp, al, be))] = hd[al, be]
nr = len(rows)
A = sp.csr_matrix((V, (Ri, Ci)), shape=(nr, nv))
b = np.zeros(nr, complex)
for k, v in bvals.items(): b[k] = v
# column scaling helps lsqr
res = lsqr(A, b, atol=1e-15, btol=1e-15, iter_lim=200000)
u = res[0]
resid = np.linalg.norm(A @ u - b) / np.linalg.norm(b)
print(f'd={d} R={R} m={m} variant={variant}: unknowns {nv}, equations {nr}, nnz {A.nnz}; '
      f'relative residual {resid:.3e}; lsqr stop {res[1]} after {res[2]} its; {time.time()-t0:.1f}s')
np.save(f'g4_sol_d{d}_R{R}_m{m}_{variant}.npy', u)
