import numpy as np,sys,time; sys.path.insert(0,'.')
from i1 import *
w=5*np.pi/16; th=0.3; Nx=16; Nyz=8
t=time.time(); er=vac(Nx,th,w,Nyz); print("real-space vac",er,time.time()-t)
ks=2*np.pi*(np.arange(Nyz)+0.5)/Nyz; kx=2*np.pi*np.arange(Nx)/Nx; tot=0
for a in kx:
    for b in ks:
        for c in ks:
            e=np.angle(np.linalg.eigvals(Uk((a,b,c),th,w))); tot+=e[e<0].sum()
print("momentum vac",tot/(Nx*Nyz*Nyz))
# gauge check: constant Ay = shift of ky -> same vac (up to grid)
print("pi-gap check (min |E| distance from pi at a few k):", min(np.pi-np.max(np.abs(np.angle(np.linalg.eigvals(Uk(np.random.uniform(-np.pi,np.pi,3),th,w))))) for _ in range(2000)))
