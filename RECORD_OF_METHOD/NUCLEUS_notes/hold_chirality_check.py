"""Check: does hold h treat the two chiralities differently?
3D Dirac walk with a hold bump h(x) scaling both hop amplitude and mass angle by (1-h).
Start pure L, record P_R(t); start pure R, record P_L(t). Result: equal to 1e-14."""
import numpy as np
N=32
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
I2=np.eye(2); Z=np.zeros((2,2))
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
g5=-1j*alpha[0]@alpha[1]@alpha[2]
x=np.arange(N); h=0.3*np.exp(-((x-N/2)**2)/(2*4**2)); H=h[:,None,None]*np.ones((N,N,N)); theta0=0.4
def step(psi):
    out=psi.copy()
    for ax,A in enumerate(alpha):
        Pp=(np.eye(4)+A)/2; Pm=(np.eye(4)-A)/2; r=(1-H)[...,None]
        out=out+r*0.25*((np.roll(psi,1,axis=ax)-psi)@Pp.T+(np.roll(psi,-1,axis=ax)-psi)@Pm.T)
    th=(theta0*(1-H))[...,None,None]; U=np.cos(th)*np.eye(4)-1j*np.sin(th)*beta
    out=np.einsum('xyzab,xyzb->xyza',U,out); return out/np.linalg.norm(out)
PR=(np.eye(4)+g5)/2; PL=(np.eye(4)-g5)/2
def run(P0,other):
    rng=np.random.default_rng(0); v=P0@(rng.normal(size=4)+1j*rng.normal(size=4)); v/=np.linalg.norm(v)
    psi=np.zeros((N,N,N,4),complex); psi[N//2,N//2,N//2]=v; rec=[]
    for t in range(40):
        psi=step(psi); rec.append(np.linalg.norm(np.einsum('ab,xyzb->xyza',other,psi))**2)
    return np.array(rec)
a=run(PL,PR); b=run(PR,PL); print("max |P_R(t|L) - P_L(t|R)| =",np.abs(a-b).max())
