# A smooth wiggle on the bare grid: four neighbours, displacement alike over about xi hops (Gaussian-smoothed), best weights (c15f's conditions, least squares).
# Not registered. Expected: the conditions' leftover, the plane-wave leftover and the loss all fall steeply as xi grows.
import numpy as np
from c15w import *
L=96; ks=(0.33,0.46,0.59)
for delta,xi in ((0.15,0),(0.15,2),(0.15,4),(0.6,4),(0.15,8)):
    d=make_d(L,delta,xi); strain=np.std(np.roll(d,-1,0)-d)
    H,V,res=weights(L,d,FOUR)
    line=[]
    for k in ks:
        k0,r=residual(H,L,V,d,k); k0,rate,out=loss_rate(H,L,V,d,k,12.0,(40,80,120,160)); line.append(f"k={k0:.2f}: leftover {r:.1e}, loss rate {rate:.1e}")
    print(f"displacement {delta}, alike over {xi} hops (neighbour-to-neighbour {strain:.3f}): conditions' leftover {res:.1e}; "+"; ".join(line),flush=True)
