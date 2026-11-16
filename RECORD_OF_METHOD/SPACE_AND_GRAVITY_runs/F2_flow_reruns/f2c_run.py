# F2c (G12 on the flow step): rotating shift -> Coriolis push; curl-free shift -> zero-momentum packets ride the flow.
import numpy as np,sys; sys.path.insert(0,'.')
from flow2ds import *
from scipy.sparse.linalg import expm_multiply
tau=0.4; r=0.5; ok=True
# rotating: b = omega(-y, x), periodic sine form
L=240; w=1e-3; T=200; t=tau*T; one=np.ones((L,L))
X=(np.arange(L)-L//2)[:,None]*np.ones((1,L)); Y=X.T.copy()
bx=-w*L/(2*np.pi)*np.sin(2*np.pi*Y/L); by=w*L/(2*np.pi)*np.sin(2*np.pi*X/L); dbydx=w*np.cos(2*np.pi*X/L)
for m in (0.0,0.25,0.5):
    for ky in (0.3,-0.3):
        p=packet(L,L,m,r,(0.,ky),12); H=build(L,L,m,r,one,one,bx=bx,by=by); k0=mean_k(p,L,L,(0.,ky))
        pred=0.0; n=20; dt=t/n; q=p
        for i in range(n):
            qm=expm_multiply(-1j*dt/2*H,q); pred+=-np.sin(ky)*np.sum(dens(qm,L,L)*dbydx)*dt; q=expm_multiply(-1j*dt*H,q)
        dkx=mean_k(q,L,L,(0.,ky))[0]-k0[0]; dev=dkx/pred-1; ok&=abs(dev)<=0.02
        print(f"rotating w={w}: m={m}, ky={ky:+}: dk_x = {dkx:+.6f} vs {pred:+.6f} ({dev:+.4f})",flush=True)
# curl-free: b_y = g y (linear over the region the packets visit; first pass used a sine form, see f2c_out_firstpass.txt)
Lx,Ly=64,1024; g=0.005; T=400; t=tau*T; one=np.ones((Lx,Ly))
Yl=(np.arange(Ly)-Ly//2)[None,:]*np.ones((Lx,1))
# b_y = g y exactly for |y| <= 320 (the packets stay inside 260), returning smoothly to 0 at the boundary
a=np.abs(Yl); prof=np.where(a<=320,a,320-(a-320)*320/(512-320)*0.0)
s_=np.clip((a-320)/(512-320),0,1); prof=np.where(a<=320,a,320*(1-s_)**2*(1+2*s_))
byl=g*np.sign(Yl)*prof
for m in (0.1,0.25,0.5):
    for y0 in (40,80):
        p=packet(Lx,Ly,m,r,(0.,0.),10,c0=(0,y0)); H=build(Lx,Ly,m,r,one,one,by=byl)
        ys=centre(dens(p,Lx,Ly),Ly,1); n=40; dt=t/n; q=p; ypred=ys
        for i in range(n):
            qm=expm_multiply(-1j*dt/2*H,q); ypred+=np.sum(dens(qm,Lx,Ly)*byl)*dt; q=expm_multiply(-1j*dt*H,q)
        ye=centre(dens(q,Lx,Ly),Ly,1); kk=mean_k(q,Lx,Ly)[1]; dev=(ye-ypred)/(ypred-ys); ok&=abs(dev)<=0.01
        print(f"curl-free g={g}: m={m}, y0={y0}: y {ys:.2f} -> {ye:.3f} vs {ypred:.3f} ({dev:+.4f} of distance); straight y0 e^(gt) = {ys*np.exp(g*t):.2f}; <k_y> = {kk:+.1e}",flush=True)
print("F2c",'PASS' if ok else 'FAIL')
