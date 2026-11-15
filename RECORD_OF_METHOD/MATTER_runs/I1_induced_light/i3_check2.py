import numpy as np,sys; sys.path.insert(0,'.')
from i3 import *
w=5*np.pi/16; th=0.03
for n in (12,):
    p,wt=shells(th,n); q=th/20; c0=Cdyn(q,0,th,w,p,wt)
    for om in (th/10,th/5):
        d=Cdyn(q,om,th,w,p,wt)-c0; print(n,om,"Z_E(dyn) estimate",-4*d/om**2,flush=True)
print("Z_E(static potential)=0.0286231")
