"""Check: does the retained record per renewal (share delta) destroy interference?
Each renewal leaves a record at its place with weight delta; two paths leave records at different
places, so the vacuum overlap after N renewals is (1-delta)^N and fringe visibility V = (1-delta)^N.
Compare with large-molecule interferometry (fringe visibility observed at the ~tens of percent level)."""
import numpy as np
hbar=1.0546e-34; c=2.998e8; u=1.6605e-27
cases={'electron (1 s flight)':(9.109e-31,1.0),
       'C70 fullerene, Arndt 1999 (~5 ms)':(840*u,5e-3),
       '25 kDa oligoporphyrin, Fein 2019 (~10 ms)':(25000*u,1e-2)}
delta=1e-32
print("delta =",delta)
for name,(m,t) in cases.items():
    N=m*c**2/hbar*t; V=np.exp(-delta*N)
    print(f"{name:45s} renewals N={N:.2e}  V=exp(-delta N)=1-{delta*N:.1e}   bound delta < 1/N ~ {1/N:.0e} for V>1/e")
