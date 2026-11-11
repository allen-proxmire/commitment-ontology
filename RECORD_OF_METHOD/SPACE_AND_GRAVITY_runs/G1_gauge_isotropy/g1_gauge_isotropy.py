"""G1: count quadratic two-derivative costs on h_{mu nu} invariant under linearised
diffeomorphisms and under (a) the cubic group or (b) full rotations, plus time reversal."""
import numpy as np, itertools
rng=np.random.default_rng(0)
pairs=[(m,n) for m in range(4) for n in range(m,4)]           # 10 components of h
kk=[(m,n) for m in range(4) for n in range(m,4)]              # 10 monomials k_m k_n
AB=[(a,b) for a in range(10) for b in range(a,10)]             # 55 symmetric pairs
def hvec(H): return np.array([H[m,n] for (m,n) in pairs])
def feat(H,k):
    h=hvec(H); return np.array([h[a]*h[b]*k[m]*k[n] for (a,b) in AB for (m,n) in kk])
def sym(A): return (A+A.T)/2
def rot(axis,ang):
    a=np.array(axis,float); a/=np.linalg.norm(a)
    K=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    R=np.eye(3)+np.sin(ang)*K+(1-np.cos(ang))*K@K
    L=np.eye(4); L[1:,1:]=R; return L
P=np.eye(4)[[0,2,3,1]]; S=np.eye(4)[[0,2,1,3]]; F=np.diag([1,-1,1,1.]); T=np.diag([-1,1,1,1.])
cubic=[P,S,F,T]; rotation=cubic+[rot([1,2,3],0.7),rot([3,-1,2],1.1)]
def solve(gens,nsamp=2500):
    rows=[]
    for _ in range(nsamp):
        H=sym(rng.normal(size=(4,4))); k=rng.normal(size=4)
        for L in gens:   # invariance: Q(L H L^T, L k) = Q(H,k)
            rows.append(feat(L@H@L.T, L@k)-feat(H,k))
        xi=rng.normal(size=4); dH=np.outer(k,xi)+np.outer(xi,k)   # gauge
        rows.append(feat(H+dH,k)-feat(H,k))
    A=np.array(rows); s=np.linalg.svd(A,compute_uv=False)
    _,_,Vt=np.linalg.svd(A); null=Vt[np.sum(s>1e-8*s[0]):]
    return null
def Mof(c,k):
    M=np.zeros((10,10)); i=0
    for (a,b) in AB:
        v=sum(c[i*10+j]*k[m]*k[n] for j,(m,n) in enumerate(kk)); i+=1
        if a==b: M[a,a]+=v
        else: M[a,b]+=v/2; M[b,a]+=v/2
    return M
def tt_speeds(c,khat):
    # find omega where M(omega,k) has a non-gauge null vector, k=|1|
    k=np.array(khat,float); k/=np.linalg.norm(k); out=[]
    ws=np.linspace(0.05,3,3000); dets=[]
    for w in ws:
        M=Mof(c,np.r_[w,k]); ev=np.sort(np.abs(np.linalg.eigvalsh(M)))
        dets.append(ev[4])            # 4 gauge zero modes always; next smallest
    dets=np.array(dets); idx=np.where((dets[1:-1]<dets[:-2])&(dets[1:-1]<dets[2:])&(dets[1:-1]<1e-3*np.max(dets)))[0]
    return [round(ws[i+1],3) for i in idx]
for name,g in [('rotations',rotation),('cubic',cubic)]:
    null=solve(g); print(name,'dimension of gauge-invariant cost space:',len(null))
    for i,c in enumerate(null):
        print('  solution',i,'zero-speed along axis:',tt_speeds(c,[1,0,0]),'diagonal:',tt_speeds(c,[1,1,1]))
