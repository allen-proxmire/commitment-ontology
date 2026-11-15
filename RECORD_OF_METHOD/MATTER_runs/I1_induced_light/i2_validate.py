import numpy as np,sys,time; sys.path.insert(0,'.')
from i2 import *
w=5*np.pi/16; th=0.3; q=2*np.pi/64
# same sampling as I1: kx on 64-grid, ky,kz 24x24 midpoints
kx=2*np.pi*np.arange(64)/64; ks=2*np.pi*(np.arange(24)+.5)/24
t=time.time()
for f in 'BE':
    tot=sum(pair_shift((a,b,c),q,th,w,f) for a in kx for b in ks for c in ks)/(64*24*24)
    print(f, tot, time.time()-t)
print("I1 n=1: C_B=-7.855132e-05 C_E=+8.556936e-05")
