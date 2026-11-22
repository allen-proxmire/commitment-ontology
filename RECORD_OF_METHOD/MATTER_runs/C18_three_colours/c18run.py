# Three colours on the step: which sets of quarks are neutral, and what they weigh. Chains of 3 and 4 places, bare mass 0.
# Sectors by quarks added to the filled lower states: none (N,N,N); one (N+1,N,N); two (N+1,N+1,N); three (N+1,N+1,N+1).
# A tail of K links carries the chain's total colour away, so a set that is not neutral pays (g^2/2) C2 K.
# Stated before running: the energies of "none" and "three" do not move with K (to 1e-6); "one" and "two" both rise at (g^2/2)(4/3) per link of tail
# (two quarks as an antiquark, not at 10/3). These follow from the colour symmetry if the code is right; what the run adds is the neutral sets' energies.
import numpy as np, time, sys
from c18 import low
out=[]
for N in (3,4):
    for g in ((1.0,1.5,2.0) if N==3 else (1.5,)):
        res={}
        for nm,ks in (("none",(N,N,N)),("one",(N+1,N,N)),("two",(N+1,N+1,N)),("three",(N+1,N+1,N+1))):
            for K in ((0,2,4) if N==3 else (0,3)):
                t0=time.time(); w=low(N,ks,0.0,g,K,k=2); res[(nm,K)]=w; print(f"N = {N}, g = {g}, quarks added: {nm}, tail {K}: lowest two energies {w[0]:.6f} {w[1]:.6f}  ({time.time()-t0:.0f} s)",flush=True)
        Ks=sorted({K for (_,K) in res}); K1=Ks[-1]; E0=res[("none",0)][0]
        print(f"   N = {N}, g = {g}: vacuum moves with the tail by {abs(res[('none',K1)][0]-E0):.1e}; first excitation in the vacuum sector (quark and antiquark) {res[('none',K1)][1]-res[('none',K1)][0]:.4f}")
        for nm in ("one","two","three"):
            sl=(res[(nm,K1)][0]-res[(nm,0)][0])/K1/(0.5*g*g); print(f"   quarks added: {nm}: energy above the vacuum {res[(nm,0)][0]-E0:.4f} with no tail, {res[(nm,K1)][0]-E0:.4f} with a tail of {K1}; rise per link of tail {sl:.4f} x g^2/2")
