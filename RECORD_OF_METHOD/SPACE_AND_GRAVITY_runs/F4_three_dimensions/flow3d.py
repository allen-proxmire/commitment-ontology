import numpy as np, scipy.sparse as sp
s0=np.eye(2); sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]).astype(complex)
A=[np.kron(sx,s) for s in (sx,sy,sz)]; B=np.kron(sz,s0); I4=np.eye(4)   # Dirac alpha_j, beta
def ring(L):
    S=sp.diags([np.ones(L-1)],[1],shape=(L,L),format='lil'); S[L-1,0]=1; return S.tocsr()
def build(L,m,r,N,D):
    I=sp.identity(L); S=[sp.kron(sp.kron(ring(L) if a==0 else I, ring(L) if a==1 else I), ring(L) if a==2 else I).tocsr() for a in range(3)]
    Id=sp.identity(L**3); K=sum(sp.kron((S[a]-S[a].T)/(2j),A[a]) for a in range(3))+r*sp.kron(3*Id-sum((S[a]+S[a].T)/2 for a in range(3)),B)
    Dm=sp.kron(sp.diags(np.ravel(D)),I4); return (0.5*(Dm@K+K@Dm)+sp.kron(sp.diags(np.ravel(m*N)),B)).tocsr()
def h(k,m,r): return sum(np.sin(k[a])*A[a] for a in range(3))+(m+r*sum(1-np.cos(k[a]) for a in range(3)))*B
def packet(L,m,r,k0,sig):
    ks=2*np.pi*np.fft.fftfreq(L); ph=np.zeros((L,L,L,4),complex); w=lambda k,c:((k-c+np.pi)%(2*np.pi)-np.pi)
    for i,a in enumerate(ks):
        if abs(w(a,k0[0])*sig)>5: continue
        for j,b in enumerate(ks):
            if abs(w(b,k0[1])*sig)>5: continue
            for l,c in enumerate(ks):
                amp=np.exp(-((w(a,k0[0])*sig)**2+(w(b,k0[1])*sig)**2+(w(c,k0[2])*sig)**2)/2)
                if amp<1e-8: continue
                e,v=np.linalg.eigh(h((a,b,c),m,r)); u=v[:,3]+v[:,2]*0  # top state of the positive pair
                # positive-energy subspace is 2-dim (spin); take a fixed spin by projecting a reference spinor
                P=v[:,2:]@v[:,2:].conj().T; u=P@np.array([1,0,0,0],complex); u/=np.linalg.norm(u)+1e-30
                ph[i,j,l]=amp*u
    p=np.fft.ifftn(ph,axes=(0,1,2)); p=np.roll(p,(L//2,L//2,L//2),axis=(0,1,2)); return (p/np.linalg.norm(p)).reshape(-1)
def dens(p,L): return (np.abs(p.reshape(L,L,L,4))**2).sum(3)
