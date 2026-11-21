# The payoff test at longer wavelength: independent displacements of 0.15 hops; four neighbours (best weights) against eight (exact weights nearest the even grid's).
# Stated beforehand (c15e_firstpass.py): exact weights lose at least 5 times more slowly at long wavelength, and go as k^5 (5 +/- 1) against k^3.
import numpy as np, time
from c15w import *
L=256; ks=(0.15,0.2,0.3); d=make_d(L,0.15,0); tab={}
for nm,offs in (("four neighbours",FOUR),("eight neighbours",EIGHT)):
    t0=time.time(); H,V,res=weights(L,d,offs); print(f"{nm}: conditions' leftover {res:.1e} (weights in {time.time()-t0:.0f} s)",flush=True)
    for k in ks:
        k0,r=residual(H,L,V,d,k); k0,rate,out=loss_rate(H,L,V,d,k,28.0,(100,200,300),win=0.06); tab[(nm,k)]=(k0,rate,r)
        print(f"   k = {k0:.3f}: plane-wave leftover {r:.2e}; loss rate {rate:.3e}; forward share "+" ".join(f"{o:.5f}" for o in out),flush=True)
for nm in ("four neighbours","eight neighbours"):
    print(f"{nm}: power of k in the loss rate {np.polyfit(np.log([tab[(nm,k)][0] for k in ks]),np.log([tab[(nm,k)][1] for k in ks]),1)[0]:.2f}")
for k in ks: print(f"k = {tab[('four neighbours',k)][0]:.3f}: four over eight, loss rate {tab[('four neighbours',k)][1]/tab[('eight neighbours',k)][1]:.1f}, leftover squared {(tab[('four neighbours',k)][2]/tab[('eight neighbours',k)][2])**2:.1f}")
