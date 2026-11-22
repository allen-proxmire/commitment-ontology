# Three colours on the step, one space dimension, exact. Quarks: the flow step's two-component pattern in three colour states,
# H_W = sigma_x sin k + sigma_z (m + r (1 - cos k)), r = 1/2; the colour field fixed by Gauss's law (open ends): each link carries the energy
# (g^2/2) C2 of the total colour to its left. A tail of K further links to the right carries the chain's total colour away.
# H_E = (g^2/2) sum_{m,m'} W(m,m') Q_m . Q_m',  W = (links to the right of both places) + K,
# Q_m . Q_m' = (1/2) sum_c n_mc n_m'c - (1/6) n_m n_m' + (1/2) sum_{c != c'} [ delta_mm' n_mc - sum_{s,s'} A^c_(ms),(m's') A^c'_(m's'),(ms) ],  A^c_ab = c^dag_a c_b in colour c.
# Each colour's count is kept, so a sector is (k_r, k_g, k_b); the filled lower states are (N, N, N).
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl, itertools, sys
r=0.5
def popcount(v):
    v=v.astype(np.uint64); c=np.zeros(v.shape,np.int64)
    while v.any(): c+=(v&np.uint64(1)).astype(np.int64); v>>=np.uint64(1)
    return c
class Colour:                      # one colour's 2N modes (mode = 2*place + component) with k quarks
    def __init__(s,N,k):
        M=2*N; s.b=np.array(sorted(sum(1<<i for i in c) for c in itertools.combinations(range(M),k)),dtype=np.int64); s.D=len(s.b)
        s.occ=np.array([(s.b>>i)&1 for i in range(M)]).T.astype(float); s.nsite=s.occ[:,0::2]+s.occ[:,1::2]; s.sz=(s.occ[:,0::2]-s.occ[:,1::2]).sum(1); s.A={}
        for a in range(M):
            for b in range(M):
                if a==b: s.A[(a,b)]=sp.diags(s.occ[:,a]).tocsr(); continue
                m=((s.b>>b)&1==1)&((s.b>>a)&1==0); src=s.b[m]; dst=src^(1<<a)^(1<<b); lo,hi=min(a,b),max(a,b); mask=((1<<hi)-1)^((1<<(lo+1))-1)
                sgn=1-2*(popcount(src&mask)%2); s.A[(a,b)]=sp.csr_matrix((sgn.astype(float),(np.searchsorted(s.b,dst),np.nonzero(m)[0])),shape=(s.D,s.D))
        T={(0,0):-r/2,(1,1):r/2,(0,1):-0.5j,(1,0):-0.5j}; h=sp.csr_matrix((s.D,s.D),dtype=complex)
        for n in range(N-1):
            for (c,cp),t in T.items(): a=2*n+c; bb=2*(n+1)+cp; h=h+t*s.A[(a,bb)]+np.conj(t)*s.A[(bb,a)]
        s.hop=h
def build(N,ks,m,g,K):
    cols=[Colour(N,k) for k in ks]; D=[c.D for c in cols]; I=[sp.identity(d,format='csr') for d in D]
    W=np.array([[N-1-max(a,b)+K for b in range(N)] for a in range(N)],float)
    k3=lambda X,Y,Z: sp.kron(sp.kron(X,Y,format='csr'),Z,format='csr')
    H=k3(cols[0].hop,I[1],I[2])+k3(I[0],cols[1].hop,I[2])+k3(I[0],I[1],cols[2].hop)
    q=[np.einsum('im,mn,in->i',c.nsite,W,c.nsite) for c in cols]; lin=[c.nsite@np.diag(W) for c in cols]
    X=lambda a,b: cols[a].nsite@W@cols[b].nsite.T
    e=lambda v,ax: v.reshape([D[i] if i==ax else 1 for i in range(3)])
    diag=sum(e((0.5-1/6)*q[c]+lin[c],c) for c in range(3))+0*np.zeros(D)       # (1/2 - 1/6) n_c W n_c ; (N_c - 1)/2 = 1 times sum_m W_mm n_mc
    for a,b in ((0,1),(0,2),(1,2)):
        Xab=X(a,b); sh=[1,1,1]; sh[a]=D[a]; sh[b]=D[b]; diag=diag-(1/3)*Xab.reshape(sh)
    diag=0.5*g*g*diag+sum(e((m+r)*c.sz,i) for i,c in enumerate(cols))
    H=H+sp.diags(diag.reshape(-1))
    ex=None
    for a,b in ((0,1),(0,2),(1,2)):                      # unordered colour pairs, each counted twice
        P=sp.csr_matrix((D[a]*D[b],D[a]*D[b]))
        for x in range(2*N):
            for y in range(2*N):
                P=P+W[x//2,y//2]*sp.kron(cols[a].A[(x,y)],cols[b].A[(y,x)],format='csr')
        if (a,b)==(0,1): T3=sp.kron(P,I[2],format='csr')
        elif (a,b)==(1,2): T3=sp.kron(I[0],P,format='csr')
        else:
            # colours 0 and 2 with colour 1 between: permute the middle index
            T3=sp.kron(P,I[1],format='csr'); idx=np.arange(D[0]*D[1]*D[2]).reshape(D[0],D[1],D[2]); perm=idx.transpose(0,2,1).reshape(-1)   # position in (0,2,1) order -> index in (0,1,2) order
            T3=T3.tocoo(); T3=sp.csr_matrix((T3.data,(perm[T3.row],perm[T3.col])),shape=T3.shape)
        ex=T3 if ex is None else ex+T3
    return H-0.5*g*g*ex,D        # -(1/2) * 2 (ordered pairs) * (g^2/2)
def low(N,ks,m,g,K,k=3):
    H,D=build(N,ks,m,g,K); n=H.shape[0]
    if n<2500: return np.linalg.eigvalsh(H.toarray())[:k]
    w=spl.eigsh(H,k=k,which='SA',tol=1e-8,return_eigenvectors=False); return np.sort(w)
if __name__=="__main__":
    # checks: one place, no hopping energy scale (g^2/2 = 1, m = -r so the on-place term vanishes, K = 1 link): the Casimirs of one, two and three quarks
    for ks,expect in (((1,0,0),"4/3 x2"),((1,1,0),"4/3 x3, 10/3 x1"),((1,1,1),"0 x4, 3 x4")):
        H,D=build(1,ks,-r,np.sqrt(2),1); print(f"check, one place, quarks {ks}: field energies "+" ".join(f"{x:.4f}" for x in np.linalg.eigvalsh(H.toarray()))+f"   (expected {expect})")
    H,D=build(2,(2,2,2),0.0,1.0,0); print(f"check, two places, filled lower states: Hermitian to {abs(H-H.conj().T).max():.1e}, {H.shape[0]} states")
