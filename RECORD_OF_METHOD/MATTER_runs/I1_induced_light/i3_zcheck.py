import numpy as np,sys; sys.path.insert(0,'.')
from i2 import Ak,Fb
exec(open('i3_axis.py').read().split('w=5*np.pi/16; th=0.03')[0])
w=5*np.pi/16; th=0.3; N=16; q=2*np.pi/N; G=12
kp=2*np.pi*(np.arange(G)+.5)/G; kn=2*np.pi*np.arange(N)/N
def Uk(kk): return Ak(0,kk[0],w)@Ak(1,kk[1],w)@Ak(2,kk[2],w)@Fb(th)@Ak(2,kk[2],w)@Ak(1,kk[1],w)@Ak(0,kk[0],w)
def brute(ax,a):
    # real space along axis ax: build U on N sites via Fourier of momentum blocks, then apply potential
    tot=0
    F_=np.exp(-1j*np.outer(np.arange(N),kn))/np.sqrt(N)   # site x momentum
    for k1 in kp:
        for k2 in kp:
            blocks=[]
            for kk in kn:
                k=[0,0,0]; others=[i for i in range(3) if i!=ax]; k[others[0]]=k1; k[others[1]]=k2; k[ax]=kk; blocks.append(Uk(k))
            Um=np.zeros((4*N,4*N),complex)
            for i in range(N): Um[4*i:4*i+4,4*i:4*i+4]=blocks[i]
            W=np.kron(F_,np.eye(4)); Ur=W@Um@W.conj().T
            Dg=np.diag(np.repeat(np.exp(-0.5j*a*np.cos(q*np.arange(N))),4)); e=np.angle(np.linalg.eigvals(Dg@Ur@Dg)); tot+=e[e<0].sum()
    return tot/(N*G*G)
for ax in (0,2):
    e0=brute(ax,0); d=[(brute(ax,a)-e0)/a**2 for a in (0.05,0.1)]; bf=(4*d[0]-d[1])/3
    pm=sum(pair_E_axis([k1 if ax!=0 else kk, k2 if ax==2 else (kk if ax==1 else k1), kk if ax==2 else k2],q,th,w,ax) for kk in kn for k1 in kp for k2 in kp)/(N*G*G)
    print("axis",ax,"brute",bf,"pair",pm,flush=True)
