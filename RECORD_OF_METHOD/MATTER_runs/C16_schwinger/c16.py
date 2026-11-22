# The Schwinger model on CO's step: one space dimension, charged massless patterns on the flow step's Hamiltonian
# H_W = sigma_x sin k + sigma_z (m + r (1 - cos k)), r = 1/2, coupled to the which-way field with charge g (units: hop = 1, hbar = c = 1).
# In one dimension the field has no waves of its own; Gauss's law fixes it from the charges, L_n = l0 + sum_{j<=n} q_j, energy (g^2/2) sum_n L_n^2
# (open ends, filled lower states: one of the two modes per place, q = occupation - 1). Exact diagonalisation, N places.
# Continuum answer (Schwinger): massless charges disappear from the spectrum; what is left is one free neutral pattern of mass g/sqrt(pi) = 0.5642 g,
# with E^2 = M^2 + p^2. The lifting term breaks the handedness symmetry, so the bare mass m* at which the charges are truly massless is shifted from 0;
# m* is found as the bare mass at which a background field l0 = 1/4 is fully screened in the middle of the chain.
# Stated before running, for g = 0.5, 0.75, 1.0 at m = m*: M/g = 0.564 within 15%; the levels' speed v (from E_n^2 = M^2 + v^2 (n pi/(N + d))^2 at N = 8, 10) = 1 within 15%.
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl, itertools, sys
r=0.5
def basis(N):
    M=2*N; b=np.array([sum(1<<i for i in c) for c in itertools.combinations(range(M),N)],dtype=np.int64); b.sort(); return b
def popcount(v):
    v=v.astype(np.uint64); c=np.zeros(v.shape,np.int64)
    while v.any(): c+=(v&np.uint64(1)).astype(np.int64); v>>=np.uint64(1)
    return c
class Chain:
    def __init__(s,N):
        s.N=N; s.b=basis(N); D=len(s.b); s.D=D; rows=[];cols=[];vals=[]
        T={(0,0):-r/2,(1,1):r/2,(0,1):-0.5j,(1,0):-0.5j}
        for n in range(N-1):
            for (c,cp),t in T.items():
                a=2*n+c; bb=2*(n+1)+cp                       # t c^dag_a c_bb + h.c.
                m=((s.b>>bb)&1==1)&((s.b>>a)&1==0); src=s.b[m]; dst=src^(1<<a)^(1<<bb)
                lo,hi=min(a,bb),max(a,bb); mask=((1<<hi)-1)^((1<<(lo+1))-1); sgn=1-2*(popcount(src&mask)%2)
                i=np.searchsorted(s.b,dst); j=np.nonzero(m)[0]
                rows+=[i,j]; cols+=[j,i]; vals+=[t*sgn,np.conj(t)*sgn]
        s.Hhop=sp.csr_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(D,D))
        occ=np.array([(s.b>>i)&1 for i in range(2*N)]).T.astype(float)        # D x 2N
        s.sz=(occ[:,0::2]-occ[:,1::2]).sum(1); q=occ[:,0::2]+occ[:,1::2]-1; s.Lcum=np.cumsum(q,1)[:,:N-1]
    def H(s,m,g,l0=0.0):
        d=(m+r)*s.sz+0.5*g*g*((s.Lcum+l0)**2).sum(1); return s.Hhop+sp.diags(d)
    def low(s,m,g,l0=0.0,k=6):
        Hm=s.H(m,g,l0)
        if s.D<3000: w,v=np.linalg.eigh(Hm.toarray()); return w[:k],v[:,:k]
        w,v=spl.eigsh(Hm,k=k,which='SA',tol=1e-9); o=np.argsort(w); return w[o],v[:,o]
    def field_mid(s,m,g,l0):
        w,v=s.low(m,g,l0,k=2); p=abs(v[:,0])**2; return (p*(s.Lcum[:,s.N//2-1]+l0)).sum()
def mstar(ch,g):
    ms=np.linspace(-0.6*g*g-0.05,0.1,8); F=np.array([ch.field_mid(m,g,0.25) for m in ms])
    i=np.nonzero(np.sign(F[:-1])!=np.sign(F[1:]))[0]
    if len(i)==0: return None,ms,F
    i=i[0]; return ms[i]-F[i]*(ms[i+1]-ms[i])/(F[i+1]-F[i]),ms,F
if __name__=="__main__":
    chains={N:Chain(N) for N in (8,10)}
    w,_=chains[8].low(0.0,0.0,k=3); print(f"check, no charge (g = 0), N = 8, m = 0: first gaps {w[1]-w[0]:.4f}, {w[2]-w[0]:.4f}",flush=True)
    for g in (0.5,0.75,1.0):
        rec={}
        for N in (8,10):
            ch=chains[N]; ms_,grid,F=mstar(ch,g)
            if ms_ is None: print(f"g = {g}, N = {N}: no sign change of the middle field on the grid; F = "+" ".join(f"{f:+.3f}" for f in F)); continue
            w,_=ch.low(ms_,g,k=6); w0,_=ch.low(0.0,g,k=4); rec[N]=(ms_,w-w[0],w0-w0[0])
            print(f"g = {g}, N = {N}: m* = {ms_:+.4f} (m*/g^2 = {ms_/g**2:+.3f}); gaps at m*: "+" ".join(f"{x:.4f}" for x in (w-w[0])[1:])+"; gaps at m = 0: "+" ".join(f"{x:.4f}" for x in (w0-w0[0])[1:]),flush=True)
        if len(rec)==2:
            # two levels at each N: E_n^2 = M^2 + v^2 (n pi/(N+d))^2, n = 1, 2  ->  M^2 from each N; v and d from the two slopes
            out=[]
            for N in (8,10):
                e1,e2=rec[N][1][1],rec[N][1][2]; slope=(e2**2-e1**2)/3; M2=e1**2-slope; out.append((N,M2,slope))
            (N1,M21,s1),(N2,M22,s2)=out; a1,a2=np.pi/np.sqrt(s1),np.pi/np.sqrt(s2)        # (N+d)/v
            v=(N2-N1)/(a2-a1); d=v*a1-N1
            print(f"   g = {g}: M/g = {np.sqrt(max(M21,0))/g:.3f} (N = 8), {np.sqrt(max(M22,0))/g:.3f} (N = 10); against 0.564; speed v = {v:.3f}, end correction d = {d:.2f}",flush=True)
