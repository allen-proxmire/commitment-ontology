# F2b (G8 on the flow step): light past a 1/r mass, with the stretch vs clock only. Geometry as G8.
import numpy as np,sys; sys.path.insert(0,'.')
from flow2ds import *
from scipy.sparse.linalg import expm_multiply
tau=0.4; r=0.5; Lx,Ly=512,1024; A=0.6; rc=5.0; B=120; Y0=-440; K0=0.5; sig=40
X=(np.arange(Lx)-Lx//2)[:,None]*np.ones((1,Ly)); Y=(np.arange(Ly)-Ly//2)[None,:]*np.ones((Lx,1)); one=np.ones((Lx,Ly))
w0=omega=lambda kx,ky: np.sqrt(np.sin(kx)**2+np.sin(ky)**2+(r*(2-np.cos(kx)-np.cos(ky)))**2)
h=1e-5; vy=(omega(0,K0+h)-omega(0,K0-h))/(2*h); t=2*abs(Y0)/vy
res={}; ends=[]
for side in (1,-1):
    Phi=A/np.sqrt((X+side*B)**2+Y**2+rc**2)    # mass at x = -side*B, packet at x = 0
    p=packet(Lx,Ly,0.0,r,(0.,K0),sig,c0=(0,Y0)); kref=(0.,K0)
    for label,D in (("none",one),("clock",1-Phi),("full",(1-Phi)/(1+Phi))):
        N=one if label=="none" else 1-Phi
        q=expm_multiply(-1j*t*build(Lx,Ly,0.0,r,N,D),p); kx=mean_k(q,Lx,Ly,kref)[0]
        res[(label,side)]=kx*side; ends.append(centre(dens(q,Lx,Ly),Ly,1))
        print(f"side {side:+d} {label}: <kx>*side = {kx*side:+.6e}, y end {ends[-1]:.1f}",flush=True)
ang={l:-np.mean([(res[(l,s)]-res[("none",s)]) for s in (1,-1)])/K0 for l in ("clock","full")}   # toward the mass is negative kx*side
y1=np.mean(ends); geo=(abs(Y0)/np.hypot(Y0,B)+y1/np.hypot(y1,B))/2; cont=4*A/B*geo
ratio=ang["full"]/ang["clock"]; size=ang["full"]/cont
print(f"angles: clock {ang['clock']:.5e}, full {ang['full']:.5e}; ratio {ratio:.4f}; full / continuum 4A/b over the path ({cont:.5e}) = {size:.4f}; sides differ by {abs(res[('full',1)]-res[('full',-1)])/abs(res[('full',1)]-res[('none',1)]+1e-30):.3f} (raw)")
print("F2b",'PASS' if abs(ratio-2)<=0.05 and 0.85<=size<=1.20 else 'FAIL')
