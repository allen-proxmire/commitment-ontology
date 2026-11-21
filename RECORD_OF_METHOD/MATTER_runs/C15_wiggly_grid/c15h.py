# c15g again with the eight-neighbour weights chosen nearest the even grid's (c15g's least-norm weights give the even grid itself extra slow states).
# The hand-drawn grid run with weights from c15f. 2D, massless, naive hops (r = 0). Places displaced by 0.15 hops rms per component, independently.
#  four neighbours: the best weights there are (least squares; they cannot meet the conditions, c15f).
#  eight neighbours: weights meeting the conditions exactly.
# Loss rate = slope of the forward share against time. Stated before running (c15e_firstpass.py): felt-like weights go as k^3 (3.0 +/- 0.6);
# exact weights go as k^5 (5 +/- 1) and at k = 0.3 lose at least 5 times more slowly.
import numpy as np, scipy.sparse as sp, sys
from c15f import solve
L=96; sig=12.0; dt=0.4; times=(40,80,120,160)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]])
def build(delta,offs,seed=5,near=False):
    res,sol,links,nl=solve(L,delta,offs,seed,near); V=sol[2*nl:]; rows=[];cols=[];vals=[]
    for l,(i,j,dx) in enumerate(links):
        A=sol[2*l:2*l+2]; m=-0.5j*(A[0]*sx+A[1]*sy)/np.sqrt(V[i]*V[j])
        for a in range(2):
            for b in range(2):
                rows+=[2*i+a,2*j+a]; cols+=[2*j+b,2*i+b]; vals+=[m[a,b],-m[a,b]]
    H=sp.csr_matrix((vals,(rows,cols)),shape=(2*L*L,2*L*L))
    rng=np.random.default_rng(seed); d=delta*rng.standard_normal((L,L,2))
    return H,V.reshape(L,L),d,res,abs(H-H.conj().T).max()
kk=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(kk,kk,indexing='ij')
def run(H,V,d,k0):
    k0=2*np.pi*round(k0*L/(2*np.pi))/L; xi=np.arange(L)-L/4; X,Y=np.meshgrid(xi,np.arange(L)-L/2,indexing='ij')
    env=np.sqrt(V)*np.exp(-(X**2+Y**2)/(4*sig**2)+1j*k0*(X+d[...,0]))
    p=np.stack([env,env],-1).reshape(-1)/np.sqrt(2); p=p/np.linalg.norm(p); win=np.hypot(KX-k0,KY)<0.12
    def fwd(p):
        q=p.reshape(L,L,2)/np.sqrt(V)[...,None]*np.exp(-1j*k0*d[...,0])[...,None]; f=np.fft.fft2(q,axes=(0,1)); P=(abs(f)**2).sum(-1); return P[win].sum()/P.sum()
    out=[fwd(p)]; n=0
    for T in times:
        while n<int(T/dt):
            term=p.copy(); acc=p.copy()
            for j in range(1,11): term=(-1j*dt/j)*(H@term); acc=acc+term
            p=acc; n+=1
        out.append(fwd(p))
    return k0,-np.polyfit((0,)+times,out,1)[0],out,np.linalg.norm(p)
four=[(1,0),(0,1)]; eight=four+[(1,1),(1,-1)]; ks=(0.3,0.45,0.6,0.8); tab={}
for nm,offs,delta in (("even grid, eight neighbours",eight,0.0),("four neighbours, displaced",four,0.15),("eight neighbours, displaced",eight,0.15)):
    H,V,d,res,herm=build(delta,offs,5,True); print(f"{nm}: leftover of the conditions {res:.1e}; Hermitian to {herm:.0e}",flush=True)
    for k in ks:
        k0,rate,out,nrm=run(H,V,d,k); tab[(nm,k)]=(k0,rate); print(f"   k = {k0:.3f}: loss rate {rate:.3e} per hop time; forward share "+" ".join(f"{o:.4f}" for o in out)+f"; norm {nrm:.6f}",flush=True)
for nm in ("four neighbours, displaced","eight neighbours, displaced"):
    xs=[tab[(nm,k)][0] for k in ks[:3]]; ys=[max(tab[(nm,k)][1]-tab[("even grid, eight neighbours",k)][1]*(nm[0]=='e'),1e-12) for k in ks[:3]]
    print(f"{nm}: power of k (first three) {np.polyfit(np.log(xs),np.log(ys),1)[0]:.2f}")
print(f"at k = 0.3: four-neighbour rate over eight-neighbour rate = {tab[('four neighbours, displaced',0.3)][1]/max(tab[('eight neighbours, displaced',0.3)][1]-tab[('even grid, eight neighbours',0.3)][1],1e-12):.0f}")
