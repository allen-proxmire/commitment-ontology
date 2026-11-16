# F2a (G7 on the flow step): uniform shift -> drift and light's tilt; shear shift -> sideways push reversing with travel.
import numpy as np,sys; sys.path.insert(0,'.')
from flow2ds import *
from scipy.sparse.linalg import expm_multiply
tau=0.4; r=0.5; ok=True
# uniform b_x
L=200; b=0.05; T=200; t=tau*T; one=np.ones((L,L))
for name,m,k0 in (("matter m=0.5, k=0",0.5,(0.,0.)),("matter m=0.25, k=0",0.25,(0.,0.)),("light, k=(0,0.3)",0.0,(0.,0.3))):
    p=packet(L,L,m,r,k0,10); xs=[]
    for bb in (b,0.0):
        H=build(L,L,m,r,one,one,bx=b*one if bb else None); q=dens(expm_multiply(-1j*t*H,p),L,L); xs.append(centre(q,L,0))
    v=(xs[0]-xs[1])/t; pred=b*np.cos(k0[0]); dev=v/pred-1; ok&=abs(dev)<=0.01
    print(f"uniform b={b}: {name}: dx/dt = {v:.5f} vs {pred:.5f} ({dev:+.4f})",flush=True)
# shear b_x(y) = b1 (Ly/2pi) sin(2pi y/Ly)
Lx,Ly=300,240; b1=1e-3; T=200; t=tau*T
Y=(np.arange(Ly)-Ly//2)[None,:]*np.ones((Lx,1)); bx=b1*Ly/(2*np.pi)*np.sin(2*np.pi*Y/Ly); one=np.ones((Lx,Ly))
for m in (0.0,0.5):
    for kx in (0.3,-0.3):
        p=packet(Lx,Ly,m,r,(kx,0.),15); H=build(Lx,Ly,m,r,one,one,bx=bx); k_before=mean_k(p,Lx,Ly,(kx,0.))
        # prediction: -sin kx times b'(y) averaged over the packet (b' = b1 cos(2 pi y/Ly)), integrated in 20 chunks (midpoint)
        bp=b1*np.cos(2*np.pi*Y/Ly); pred=0.0; n=20; dt=t/n; q=p
        for i in range(n):
            qm=expm_multiply(-1j*dt/2*H,q); pred+=-np.sin(kx)*np.sum(dens(qm,Lx,Ly)*bp)*dt; q=expm_multiply(-1j*dt*H,q)
        dky=mean_k(q,Lx,Ly,(kx,0.))[1]-k_before[1]; dev=dky/pred-1; ok&=abs(dev)<=0.02
        print(f"shear b1={b1}: m={m}, kx={kx:+}: dk_y = {dky:+.6f} vs {pred:+.6f} ({dev:+.4f})",flush=True)
print("F2a",'PASS' if ok else 'FAIL')
