"""Q1: where does the Dirac automaton's current flow at rest?

The three-dimensional Dirac cellular automaton (Bialynicki-Birula 1994):
    psi <- exp(-i theta beta) * Pz Py Px psi,   P_j = P_j^+ T_j^- + P_j^- T_j^+,
P_j^± = (1 ± alpha_j)/2, T_j^± shifts by ±1 along j, theta = m c l / hbar = f/L.
Start: one site, spin-up positive-energy rest spinor (Dirac representation).
Evolve a few steps and compute the bond currents J_j(r) between r and r + e_j
(the automaton's own current: the amount of the alpha_j = +1 component moving
+j minus the alpha_j = -1 component moving -j across the bond).

Question: do the currents circulate around square faces, or around the cube's
Petrie hexagons (the chairs)? Measured: for every unit cube near the origin, the
circulation (sum of J . dl) around each of its 6 square faces and each of its 4
Petrie hexagons, per edge, averaged by |.|. Also the total angular momentum of the
current and the net current (should be zero at rest).
Registered expectation: unknown. The chair hypothesis says hexagonal circulation
dominates square circulation at theta near 1.
"""
import numpy as np, json, itertools, sys

I2 = np.eye(2); sx = np.array([[0,1],[1,0]]); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]])
Z = np.zeros((2,2))
beta = np.block([[I2, Z],[Z, -I2]])
alpha = [np.block([[Z, s],[s, Z]]) for s in (sx, sy, sz)]
Pp = [(np.eye(4) + a)/2 for a in alpha]; Pm = [(np.eye(4) - a)/2 for a in alpha]

def step(psi, theta, J=None):
    # psi shape (N,N,N,4). If J is given (list of 3 arrays) the conserved bond
    # currents of this step are accumulated into it, substep by substep:
    # across bond (r, r+e_j): +j mover leaving r minus -j mover leaving r+e_j.
    for j in range(3):
        plus = psi @ Pp[j].T          # component moving +j
        minus = psi @ Pm[j].T         # component moving -j
        if J is not None:
            pj = np.einsum('...a,...a->...', plus.conj(), plus).real
            mj = np.einsum('...a,...a->...', minus.conj(), minus).real
            J[j] += pj - np.roll(mj, -1, axis=j)
        psi = np.roll(plus, 1, axis=j) + np.roll(minus, -1, axis=j)
    M = np.cos(theta)*np.eye(4) - 1j*np.sin(theta)*beta
    return psi @ M.T

def run(N=14, steps=5, theta=1.0):
    psi = np.zeros((N,N,N,4), complex); c = N//2
    psi[c,c,c] = np.array([1,0,0,0], complex)
    for _ in range(steps-1): psi = step(psi, theta)
    J = [np.zeros((N,N,N)) for _ in range(3)]
    psi = step(psi, theta, J)        # currents of the last step (conserved by construction)
    rho = np.einsum('...a,...a->...', psi.conj(), psi).real
    # net current and angular momentum
    net = [float(J[j].sum()) for j in range(3)]
    xs = np.arange(N) - c; X, Y, Z_ = np.meshgrid(xs, xs, xs, indexing='ij')
    # bond midpoints
    L = np.zeros(3)
    for j in range(3):
        mid = [X.astype(float), Y.astype(float), Z_.astype(float)]; mid[j] = mid[j] + 0.5
        r = np.stack(mid, -1); v = np.zeros_like(r); v[..., j] = J[j]
        L += np.cross(r, v).reshape(-1,3).sum(0)
    # circulations around squares and Petrie hexagons for cubes within radius
    sq, hexs = [], []
    def Jb(r, j, sign):  # current along bond from r in direction sign*e_j
        r = tuple(np.mod(r, N))
        if sign > 0: return J[j][r]
        rm = list(r); rm[j] = (rm[j]-1) % N; return -J[j][tuple(rm)]
    def circ(path):  # path: list of (start, j, sign)
        return sum(Jb(np.array(s), j, sg) for s, j, sg in path)
    R = 3
    for ox, oy, oz in itertools.product(range(c-R, c+R), repeat=3):
        o = np.array([ox,oy,oz])
        # 6 square faces: for each pair of axes (a,b) and offset along third axis
        for a, b in [(0,1),(0,2),(1,2)]:
            k = 3 - a - b
            for off in (0,1):
                s0 = o.copy(); s0[k] += off
                ea = np.eye(3, dtype=int)[a]; eb = np.eye(3, dtype=int)[b]
                path = [(s0, a, 1), (s0+ea, b, 1), (s0+ea+eb, a, -1), (s0+eb, b, -1)]
                sq.append(circ(path)/4)
        # 4 Petrie hexagons: start at o, take axes in a cyclic order with signs
        ex, ey, ez = np.eye(3, dtype=int)
        for (p, q, w) in [(0,1,2),(0,2,1),(1,0,2),(1,2,0)]:
            e = [np.eye(3,dtype=int)[p], np.eye(3,dtype=int)[q], np.eye(3,dtype=int)[w]]
            s = o.copy(); path = []
            for j, sg in [(p,1),(q,1),(w,1),(p,-1),(q,-1),(w,-1)]:
                path.append((s.copy(), j, sg)); s = s + sg*np.eye(3,dtype=int)[j]
            hexs.append(circ(path)/6)
    return {"theta": theta, "steps": steps, "norm": float(rho.sum()), "net_current": net,
            "angular_momentum_of_current": L.tolist(),
            "mean_abs_circulation_per_edge_squares": float(np.sqrt(np.mean(np.square(sq)))),
            "mean_abs_circulation_per_edge_hexagons": float(np.sqrt(np.mean(np.square(hexs)))),
            "max_square": float(np.max(sq)), "max_hexagon": float(np.max(hexs))}

if __name__ == "__main__":
    out = {}
    for theta in (1.0, 0.5, 0.2):
        for steps in (4, 8):
            r = run(theta=theta, steps=steps); out[f"theta={theta},steps={steps}"] = r
            print(f"theta={theta} steps={steps}: sq={r['mean_abs_circulation_per_edge_squares']:.4f} "
                  f"hex={r['mean_abs_circulation_per_edge_hexagons']:.4f} ratio hex/sq={r['mean_abs_circulation_per_edge_hexagons']/r['mean_abs_circulation_per_edge_squares']:.2f} "
                  f"L={np.round(r['angular_momentum_of_current'],3)} net={np.round(r['net_current'],4)}")
    json.dump(out, open("q1_result.json","w"), indent=1)
