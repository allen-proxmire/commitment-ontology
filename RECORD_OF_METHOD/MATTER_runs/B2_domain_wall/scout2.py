import numpy as np, sys; sys.path.insert(0,'.')
from dw import *
w=5*np.pi/16
for th in [0.5,0.8]:
  for L in [4,6,8,10,12,16,20]:
    ths=[th]*L+[-th]*L
    e=np.angle(np.linalg.eigvals(Ustrip(0.0,ths,w)))
    es=np.sort(np.abs(e))
    # speed of the edge mode: slope of the two smallest |E| at small k
    k=0.02; ek=np.sort(np.abs(np.angle(np.linalg.eigvals(Ustrip(k,ths,w)))))
    print(f"th={th} L={L:2d}  two smallest |E| at k=0: {es[0]:.3e} {es[1]:.3e}  next {es[2]:.3f}   |E|(k=.02) {ek[0]:.4f}")
