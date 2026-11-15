import numpy as np,sys; sys.path.insert(0,'.')
from i2 import *
w=5*np.pi/16; c0=2*np.cos(w)
for th in [1e-3,3e-3,1e-2,3e-2]:
    p,wt=shells(th,9); qs=np.array([th/20,th/10,th/5]); qh=(2*np.sin(qs/2))**2
    Cs=np.array([C(q,th,w,'E',p,wt) for q in qs]); C0,c2,c4=np.linalg.solve(np.vstack([np.ones(3),qh,qh**2]).T,Cs)
    print(f"th={th:.0e} Z_E={-4*c2:.5f}  C0={C0:+.2e} (C0/(c2 q0^2)={C0/(c2*qh[0]):+.1e})",flush=True)
