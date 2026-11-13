# E, first step: does a Regge cost on CO's lattice reduce, at weak field, to G1's linear cost (linearised Einstein-Hilbert, Fierz-Pauli)?
# Euclidean 4D hypercubic lattice, each cube cut into 24 4-simplices (Kuhn: one per ordering of the axes), edge lengths from a metric
# carried at edge midpoints, l^2 = D.g.D (axes: edge displacements; face diagonals: angles, i.e. shear; longer diagonals fixed by the
# same metric). Cost S = sum over triangles of area x deficit. Plane wave g = 1 + eps*e*cos(k.x).
# Fail: S2/Q_FP not one constant across polarisations and directions as k -> 0, or gauge modes costing at order k^2.
import numpy as np, itertools
perms=list(itertools.permutations(range(4)))
def simplex_vertices(pm):
    v=[np.zeros(4,int)]
    for a in pm: w=v[-1].copy(); w[a]=1; v.append(w)
    return np.array(v)
SIMP=[simplex_vertices(pm) for pm in perms]
# triangle multiplicities n_t: count each triangle type (translation class) over the 24 simplices of one cube
def tkey(tri):
    tri=sorted(map(tuple,tri)); base=np.array(tri[0]); return tuple(tuple(np.array(t)-base) for t in tri)
from collections import Counter
cnt=Counter()
for V in SIMP:
    for tri in itertools.combinations(range(5),3): cnt[tkey(V[list(tri)])]+=1
def action(L,n,e,eps):
    k=2*np.pi*np.array(n)/L; S=0.0
    a0=[i for i in range(4) if n[i]!=0][0]
    # representatives: cubes at x = j*unit along an axis where n has an entry coprime... use all j in 0..L-1 along axis a0 scaled
    reps=[]
    seen=set()
    for j in range(L*abs(n[a0])):
        x=np.zeros(4); x[a0]=j; ph=int(round(np.dot(n,x)))%L
        if ph not in seen: seen.add(ph); reps.append(x)
    for x in reps:
        for V in SIMP:
            P=V+x
            def l2(i,j):
                D=(P[j]-P[i]).astype(float); mid=(P[i]+P[j])/2; g=np.eye(4)+eps*e*np.cos(k@mid); return D@g@D
            L2=np.array([[l2(i,j) for j in range(5)] for i in range(5)])
            G=np.array([[(L2[0,i]+L2[0,j]-L2[i,j])/2 for j in range(1,5)] for i in range(1,5)])
            Gi=np.linalg.inv(G)
            grads=np.zeros((5,5)); # <grad lambda_a, grad lambda_b>
            M=np.zeros((5,4)); M[1:]=np.eye(4); M[0]=-1
            Bm=M@Gi@M.T
            for a,b in itertools.combinations(range(5),2):
                th=np.arccos(-Bm[a,b]/np.sqrt(Bm[a,a]*Bm[b,b]))
                tri=[i for i in range(5) if i not in (a,b)]
                la,lb,lc=L2[tri[0],tri[1]],L2[tri[1],tri[2]],L2[tri[0],tri[2]]
                A=0.25*np.sqrt(max(4*la*lb-(la+lb-lc)**2,0))
                nt=cnt[tkey(V[tri])]
                S+=A*(2*np.pi/nt-th)
    return S
def Q(e,k):
    tr=np.trace(e); ek=e@k
    return 0.5*(k@k)*np.sum(e*e)-ek@ek+(k@e@k)*tr-0.5*(k@k)*tr**2
def S2(L,n,e,eps=1e-4): return (action(L,n,e,eps)+action(L,n,e,-eps)-2*action(L,n,e,0))/eps**2
rng=np.random.default_rng(0)
def sym(a): return (a+a.T)/2
for L in [16,32,64]:
    rows=[]
    for n in [(1,0,0,0),(1,1,0,0),(1,1,1,0),(1,2,0,0)]:
        k=2*np.pi*np.array(n)/L
        for trial in range(3):
            e=sym(rng.normal(size=(4,4)))
            r=S2(L,n,e)/Q(e,k)/L  # per representative cube count ~ L
            rows.append(r)
        xi=rng.normal(size=4); eg=np.outer(k,xi)+np.outer(xi,k)
        print(f"L={L} n={n}: gauge mode S2/(eps^2 |k|^2 |xi|^2) = {S2(L,n,eg)/(k@k)/(xi@xi)/L:+.2e}")
    rows=np.array(rows); print(f"L={L}: S2/Q per cube across polarisations and directions: mean {rows.mean():.5f}, spread {rows.std()/abs(rows.mean()):.2e}")
