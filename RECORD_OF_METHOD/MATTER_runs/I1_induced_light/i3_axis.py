import numpy as np,sys; sys.path.insert(0,'.')
from i2 import *
from scipy.linalg import schur
def pair_E_axis(k,q,th,w,ax):
    k=np.array(k,float); k2=k.copy(); k2[ax]+=q
    def Ufull(kk): return Ak(0,kk[0],w)@Ak(1,kk[1],w)@Ak(2,kk[2],w)@Fb(th)@Ak(2,kk[2],w)@Ak(1,kk[1],w)@Ak(0,kk[0],w)
    U=const(bd(Ufull(k),Ufull(k2)))
    D=(np.eye(8,dtype=complex), od(-1j/4,np.eye(4)), -np.eye(8)/32)
    U0,U1,U2=mul(mul(D,U),D)
    T,V=schur(U0,output='complex'); lam=np.diag(T); A1=V.conj().T@U1@V; A2=V.conj().T@U2@V; tot=0.
    FILLED=np.angle(lam)<0
    for n in range(8):
        if np.angle(lam[n])>=0: continue
        d=lam[n]-lam; m=(np.abs(d)>1e-12)&~FILLED; tot+=np.imag((A2[n,n]+np.sum(A1[n,m]*A1[m,n]/d[m]))/lam[n])
    return tot
w=5*np.pi/16; th=0.03; p,wt=shells(th,12)
for ax in (0,1,2):
    cs=[]; 
    for q in (th/20,th/10):
        cs.append(sum(t*pair_E_axis(k,q,th,w,ax) for k,t in zip(p,wt))/(2*np.pi)**3/(2*np.sin(q/2))**2)
    qh=[(2*np.sin(q/2))**2 for q in (th/20,th/10)]; c2=cs[0]+(cs[0]-cs[1])*qh[0]/(qh[1]-qh[0])
    print("axis",ax,"Z_E(long)",-4*c2,flush=True)
