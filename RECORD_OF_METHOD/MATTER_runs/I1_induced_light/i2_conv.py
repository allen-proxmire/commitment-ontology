import numpy as np,sys,time; sys.path.insert(0,'.')
from i2 import *
w=5*np.pi/16
for th,q in [(0.3,2*np.pi/64),(0.01,0.0005)]:
    for n in (9,12):
        p,wt=shells(th,n); t=time.time()
        print(th,n,len(p),"C_E=",C(q,th,w,'E',p,wt),f"{time.time()-t:.0f}s",flush=True)
