import numpy as np
from scipy.linalg import schur
# Exact O(a^2) vacuum-energy response by second-order perturbation of the walk's unitary on momentum pairs (k, k+q).
I2=np.eye(2); Z2=np.zeros((2,2)); s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z2,si],[si,Z2]]) for si in s]; beta=np.block([[I2,Z2],[Z2,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
Z4=np.zeros((4,4))
def Fb(a): return np.cos(a)*np.eye(4)-1j*np.sin(a)*beta
def bd(A,B): return np.block([[A,Z4],[Z4,B]])
def od(c,M): return np.block([[Z4,c*M],[c*M,Z4]])
def Ak(j,k,w): return (Pp[j]*np.exp(1j*k)+Pm[j])@Fb(w)@(Pp[j]+Pm[j]*np.exp(-1j*k))@Fb(-w)
def mul(P,M):
    return (P[0]@M[0], P[0]@M[1]+P[1]@M[0], P[0]@M[2]+P[1]@M[1]+P[2]@M[0])
def const(M): return (M,np.zeros_like(M),np.zeros_like(M))
def pair_ops(k,q,th,w,field):
    kx,ky,kz=k; k2=(kx+q,ky,kz)
    Ax=const(bd(Ak(0,kx,w),Ak(0,kx+q,w))); Az=const(bd(Ak(2,kz,w),Ak(2,kz,w)))
    Fw=const(bd(Fb(w),Fb(w))); Fmw=const(bd(Fb(-w),Fb(-w))); Ft=const(bd(Fb(th),Fb(th)))
    if field=='B':   # y-link phase a cos(qx): e^{iA}: offdiag i/2, diag -1/4 (halved per pair: -1/8)
        e=np.exp(1j*ky); Sp0=Pp[1]*e+Pm[1]; Sm0=Pp[1]+Pm[1]/e
        Sp=(bd(Sp0,Sp0), od(1j/2,Pp[1]*e), bd(-Pp[1]*e/8,-Pp[1]*e/8))
        Sm=(bd(Sm0,Sm0), od(-1j/2,Pm[1]/e), bd(-Pm[1]/e/8,-Pm[1]/e/8))
        Ay=mul(mul(mul(Sp,Fw),Sm),Fmw)
    else:
        Ay=const(bd(Ak(1,ky,w),Ak(1,ky,w)))
    U=Ax
    for M in (Ay,Az,Ft,Az,Ay,Ax): U=mul(U,M)
    if field=='E':   # D=e^{-iV/2}, V=a cos(qx): offdiag -i/4, diag -1/16 (halved: -1/32)
        D=(np.eye(8,dtype=complex), od(-1j/4,np.eye(4)), -np.eye(8)/32)
        U=mul(mul(D,U),D)
    return U
def pair_shift(k,q,th,w,field):
    U0,U1,U2=pair_ops(k,q,th,w,field)
    T,V=schur(U0,output='complex'); lam=np.diag(T)
    A1=V.conj().T@U1@V; A2=V.conj().T@U2@V; tot=0.
    FILLED=np.angle(lam)<0
    for n in range(8):
        if np.angle(lam[n])>=0: continue
        d=lam[n]-lam; mask=(np.abs(d)>1e-12)&~FILLED  # filled-filled pairs cancel exactly by unitarity; dropped to avoid round-off
        l2=A2[n,n]+np.sum(A1[n,mask]*A1[mask,n]/d[mask])
        tot+=np.imag(l2/lam[n])
    return tot
def shells(theta,n=9,inner=1/3.):
    # nested cubes around k=0: outer [-pi,pi]^3, each shell = cube minus inner cube (side/3), cells n^3 minus centre (n/3)^3, 2x2x2 Gauss per cell
    g=np.array([-1,1])/np.sqrt(3); pts=[]; wts=[]
    L=np.pi; 
    while True:
        h=2*L/n; last = L*inner < theta/4
        for i in range(n):
            for j in range(n):
                for l in range(n):
                    c=np.array([-L+(i+.5)*h,-L+(j+.5)*h,-L+(l+.5)*h])
                    m=n//3
                    if not last and m<=i<2*m and m<=j<2*m and m<=l<2*m: continue
                    for a in g:
                        for b in g:
                            for e in g: pts.append(c+np.array([a,b,e])*h/2); wts.append((h/2)**3)
        if last: break
        L*=inner
    return np.array(pts),np.array(wts)
def C(q,th,w,field,pts,wts):
    return sum(wt*pair_shift(p,q,th,w,field) for p,wt in zip(pts,wts))/(2*np.pi)**3
