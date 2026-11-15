import numpy as np
# CO's 3D walk (L1b form): 4 components, hops along alpha_j eigen-directions, flip beta.
I2=np.eye(2); Z=np.zeros((2,2)); s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
def Fb(a): return np.cos(a)*np.eye(4)-1j*np.sin(a)*beta
def Ak(j,k,w): return (Pp[j]*np.exp(1j*k)+Pm[j])@Fb(w)@(Pp[j]+Pm[j]*np.exp(-1j*k))@Fb(-w)
def Uk(k,th,w): return Ak(0,k[0],w)@Ak(1,k[1],w)@Ak(2,k[2],w)@Fb(th)@Ak(2,k[2],w)@Ak(1,k[1],w)@Ak(0,k[0],w)
def Ureal(Nx,ky,kz,th,w,Ay=None,V=None):
    # x real space (ring), y,z momenta; Ay(x): extra phase on y-hops; V(x): scalar potential (phase per step, split palindromically)
    X=np.eye(Nx); Tp=np.roll(X,1,0); Tm=np.roll(X,-1,0)   # Tp: psi(x)->psi at x+1  (momentum e^{-ik}); consistent with Ak up to k->-k
    Spx=np.kron(Tm.T,Pp[0])+np.kron(X,Pm[0]); Smx=np.kron(X,Pp[0])+np.kron(Tm,Pm[0])
    Ax=Spx@np.kron(X,Fb(w))@Smx@np.kron(X,Fb(-w))
    a=np.zeros(Nx) if Ay is None else Ay
    Spy=np.zeros((4*Nx,4*Nx),complex); Smy=np.zeros_like(Spy)
    for x in range(Nx):
        kk=ky+a[x]; Spy[4*x:4*x+4,4*x:4*x+4]=Pp[1]*np.exp(1j*kk)+Pm[1]; Smy[4*x:4*x+4,4*x:4*x+4]=Pp[1]+Pm[1]*np.exp(-1j*kk)
    Ayo=Spy@np.kron(X,Fb(w))@Smy@np.kron(X,Fb(-w)); Azo=np.kron(X,Ak(2,kz,w)); Fo=np.kron(X,Fb(th))
    U=Ax@Ayo@Azo@Fo@Azo@Ayo@Ax
    if V is not None: D=np.diag(np.repeat(np.exp(-0.5j*V),4)); U=D@U@D
    return U
def vac(Nx,th,w,Nyz,Ay=None,V=None):
    ks=2*np.pi*(np.arange(Nyz)+0.5)/Nyz; tot=0.
    for ky in ks:
        for kz in ks:
            e=np.angle(np.linalg.eigvals(Ureal(Nx,ky,kz,th,w,Ay,V))); tot+=e[e<0].sum()
    return tot/(Nx*Nyz*Nyz)
