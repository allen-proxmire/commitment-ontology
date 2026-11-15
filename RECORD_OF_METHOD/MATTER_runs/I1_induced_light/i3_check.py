import numpy as np,sys,time; sys.path.insert(0,'.')
from i3 import *; from i2 import C
w=5*np.pi/16; th=0.03; p,wt=shells(th,9)
q=th/20
t=time.time(); s=Cdyn(q,0.0,th,w,p,wt); print("static check: dyn(om=0)",s," static",C(q,th,w,'B',p,wt), f"{time.time()-t:.0f}s",flush=True)
for om in (th/5,-th/5):
    c=Cdyn(q,om,th,w,p,wt); print("om",om,"C",c,flush=True)
