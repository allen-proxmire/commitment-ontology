import numpy as np,sys; sys.path.insert(0,'.')
from i2 import Ak,Fb,Pp,Pm,bd,od,mul,const,shells
from scipy.linalg import schur
def ops(k,q,th,w,prop,link,field):
    # pair (k, k+q e_prop). field 'B': phase a cos(q x_prop) on link-axis hops; 'E': scalar potential a cos(q x_prop)
    k=np.array(k,float); k2=k.copy(); k2[prop]+=q
    fac=[]
    for j in range(3):
        if field=='B' and j==link:
            e=np.exp(1j*k[j]); e2=np.exp(1j*k2[j])
            Sp=(bd(Pp[j]*e+Pm[j],Pp[j]*e2+Pm[j]), od(1j/2,Pp[j]*e), bd(-Pp[j]*e/8,-Pp[j]*e2/8))
            Sm=(bd(Pp[j]+Pm[j]/e,Pp[j]+Pm[j]/e2), od(-1j/2,Pm[j]/e), bd(-Pm[j]/e/8,-Pm[j]/e2/8))
            fac.append(mul(mul(mul(Sp,const(bd(Fb(w),Fb(w)))),Sm),const(bd(Fb(-w),Fb(-w)))))
        else: fac.append(const(bd(Ak(j,k[j],w),Ak(j,k2[j],w))))
    U=fac[0]
    for M in (fac[1],fac[2],const(bd(Fb(th),Fb(th))),fac[2],fac[1],fac[0]): U=mul(U,M)
    if field=='E':
        D=(np.eye(8,dtype=complex), od(-1j/4,np.eye(4)), -np.eye(8)/32); U=mul(mul(D,U),D)
    return U
def shift(k,q,th,w,prop,link,field):
    U0,U1,U2=ops(k,q,th,w,prop,link,field)
    T,V=schur(U0,output='complex'); lam=np.diag(T); A1=V.conj().T@U1@V; A2=V.conj().T@U2@V; FILLED=np.angle(lam)<0; tot=0.
    for n in np.where(FILLED)[0]:
        d=lam[n]-lam; m=(np.abs(d)>1e-12)&~FILLED; tot+=np.imag((A2[n,n]+np.sum(A1[n,m]*A1[m,n]/d[m]))/lam[n])
    return tot
def coeff(th,w,prop,link,field,p,wt):
    qs=np.array([th/20,th/10,th/5]); qh=(2*np.sin(qs/2))**2
    Cs=np.array([sum(t*shift(kk,q,th,w,prop,link,field) for kk,t in zip(p,wt))/(2*np.pi)**3 for q in qs])
    C0,c2,c4=np.linalg.solve(np.vstack([np.ones(3),qh,qh**2]).T,Cs); return c2
