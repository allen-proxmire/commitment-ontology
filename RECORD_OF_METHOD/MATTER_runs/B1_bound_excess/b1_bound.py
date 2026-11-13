# B1 (see REGISTRATION.md): two patterns on CO's 1D walk bound by a linear potential; does the bound state's speed excess follow theta or M?
import numpy as np, sys
w=0.3; c0=2*np.cos(w)
sx=np.array([[0,1],[1,0]],complex); F=lambda a: np.cos(a)*np.eye(2)-1j*np.sin(a)*sx
def U1(k,th):
    A=np.diag([np.exp(-1j*k),1])@F(w)@np.diag([1,np.exp(1j*k)])@F(-w); return A@F(th)@A
def E1(k,th): return np.sort(np.abs(np.angle(np.linalg.eigvals(U1(k,th)))))[0]
def s_single(th):
    if th==0: return 0.0
    f=lambda h:(E1(h,th)**2-E1(0,th)**2)/h**2; h=0.05*th; a=(4*f(h/2)-f(h))/3; return np.sqrt(a)/c0-1
def setup(L):
    qs=2*np.pi*np.arange(L)/L; rr=np.arange(L); rr=np.where(rr>L//2,rr-L,rr)
    return qs,rr,np.exp(1j*np.outer(rr,qs))/np.sqrt(L)
def bound_E(K,th,sig,L,qs,rr,FT):
    blocks=np.zeros((L,4,4),complex); Ppp=np.zeros((L,4),complex)
    for i,q in enumerate(qs):
        Ua=U1(K/2+q,th); Ub=U1(K/2-q,th); blocks[i]=np.kron(Ua,Ub)
        ea,va=np.linalg.eig(Ua); eb,vb=np.linalg.eig(Ub)
        Ppp[i]=np.kron(va[:,np.argmin(np.angle(ea))],vb[:,np.argmin(np.angle(eb))])   # both positive energy (e^{-iE})
    M=np.einsum('rq,qab,sq->rasb',FT,blocks,FT.conj()).reshape(4*L,4*L)
    ph=np.exp(-1j*sig*np.abs(rr)/2); ph=np.repeat(ph,4)
    W=ph[:,None]*M*ph[None,:]
    ev,V=np.linalg.eig(W); E=-np.angle(ev)
    Vq=np.einsum('rq,rak->qak',FT.conj(),V.reshape(L,4,-1))       # to q basis
    wpp=np.abs(np.einsum('qa,qak->k',Ppp.conj(),Vq))**2/np.sum(np.abs(V)**2,0)   # crude: coherent overlap not needed; use per-q weight
    wpp=np.sum(np.abs(np.einsum('qa,qak->qk',Ppp.conj(),Vq))**2,0)/np.sum(np.abs(V)**2,0)
    ok=np.where((wpp>0.9)&(E>0))[0]
    j=ok[np.argmin(E[ok])]
    psi=np.sum(np.abs(V[:,j].reshape(L,4))**2,1); rms=np.sqrt(np.sum(psi*rr**2)/psi.sum())
    return E[j],wpp[j],rms
if __name__=="__main__":
    cases=[(0.005,0.0,200),(0.005,4e-4,600),(0.01,4e-4,600),(0.0,4e-4,600),(0.005,1e-3,400)]
    for th,sig,L in cases:
        qs,rr,FT=setup(L); Ks=[0,0.004,0.008]
        out=[bound_E(K,th,sig,L,qs,rr,FT) for K in Ks]
        Eb=np.array([o[0] for o in out]); a=np.polyfit(np.array(Ks)**2,Eb**2,1)[0]
        M=Eb[0]; sc=np.sqrt(a)/c0-1
        print(f"theta={th} sigma={sig} L={L}: M={M:.5f} (M/theta={M/th if th else float('inf'):.1f}) rms={out[0][2]:.1f} ++weight={out[0][1]:.3f}  s_comp={sc:+.6f}  s(theta)={s_single(th):+.6f}  s(M)={s_single(M):+.6f}")
        sys.stdout.flush()
