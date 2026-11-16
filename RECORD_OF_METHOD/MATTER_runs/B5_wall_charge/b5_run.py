import numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import eigsh
s0=np.eye(2); sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]).astype(complex)
A=[np.kron(sx,s) for s in (sx,sy,sz)]; B=np.kron(sz,s0); G5=1j*A[0]@A[1]@A[2]; A4=1j*G5@B
r=0.5; M=0.5; Lx=120; L=14; n=2*L; qB=2*np.pi/Lx
def ring(N):
    S=sp.diags([np.ones(N-1)],[1],shape=(N,N),format='lil'); S[N-1,0]=1; return S.tocsr()
Sx=ring(Lx); Ss=ring(n); Ix=sp.identity(Lx); Is=sp.identity(n)
X=np.arange(Lx)
mass=np.where(np.arange(n)<L,M,-M)
def H(ky,kz):
    kyx=ky-qB*X
    Hx=sp.kron(sp.kron((Sx-Sx.T)/(2j),Is),A[0])+r*sp.kron(sp.kron(Ix-(Sx+Sx.T)/2,Is),B)
    Hy=sp.kron(sp.kron(sp.diags(np.sin(kyx)),Is),A[1])+r*sp.kron(sp.kron(sp.diags(1-np.cos(kyx)),Is),B)
    Hz=sp.kron(sp.identity(Lx*n),np.sin(kz)*A[2]+r*(1-np.cos(kz))*B)
    Hs=sp.kron(sp.kron(Ix,(Ss-Ss.T)/(2j)),A4)+r*sp.kron(sp.kron(Ix,Is-(Ss+Ss.T)/2),B)+sp.kron(sp.kron(Ix,sp.diags(mass)),B)
    return (Hx+Hy+Hz+Hs).tocsc()
G5f=sp.kron(sp.identity(Lx*n),G5)
def low(ky,kz,k=10):
    e,v=eigsh(H(ky,kz),k=k,sigma=1e-4,which='LM'); o=np.argsort(np.abs(e)); return e[o],v[:,o]
ok=True; E1=np.sqrt(2*qB)
for ky in (0.0,0.7):
    slopes={}
    for kz in (0.05,-0.05):
        e,v=low(ky,kz); light=[(e[i],np.real(np.vdot(v[:,i],G5f@v[:,i]))) for i in range(len(e)) if abs(e[i])<E1/2]
        cnt=len(light); ok&=cnt==2
        print(f"ky={ky}, kz={kz:+}: states below half the first level: {cnt}: "+"; ".join(f"E={a:+.5f} <g5>={g:+.3f}" for a,g in light),flush=True)
        for a,g in light: slopes.setdefault(np.sign(g),[]).append(a/kz)
    for chi,sl in slopes.items():
        print(f"   chirality {chi:+.0f}: E/k_z = {np.round(sl,4)}")
        ok&=all(abs(abs(s)-1)<=0.02 for s in sl)
    if len(slopes)==2: ok&=np.sign(np.mean(slopes[1.0]))!=np.sign(np.mean(slopes[-1.0]))
    e,v=low(ky,0.0,k=16); lev=np.sort(np.abs(e)); first=lev[lev>E1/2][0]
    d=first/E1-1; ok&=abs(d)<=0.03; print(f"   next level at k_z=0: {first:.5f} vs sqrt(2qB) = {E1:.5f} ({d:+.4f})",flush=True)
print("B5",'PASS' if ok else 'FAIL')
