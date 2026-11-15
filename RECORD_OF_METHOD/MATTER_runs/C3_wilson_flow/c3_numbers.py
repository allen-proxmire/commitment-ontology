import numpy as np
from scipy.optimize import brentq
# Flow step: quasienergy per tick = tau * E_H(k) exactly, so the dispersion is H_W's.
# Massless: E^2 = sum sin^2 k_j + (r sum(1-cos k_j))^2 = k^2 + (r^2/4 - sum n_j^4/3) k^4 + ...
# group-velocity quadratic coefficient (v = 1 + c2 k^2, the convention of the record's -sin^2 w/8): c2 = 3*(r^2/8 - sum n^4/6)
dirs={'axis':1.0,'face':0.5,'body':1/3}
lamC=3.8616e-13; hc_p=1.97327e-7/2.31e15; smax=2.45e-20     # electron Compton length (m); hbar c / 2.31 PeV (m); Li-Ma bound on v-1
f=max(x*(1-x)*(x**3+(1-x)**3) for x in np.linspace(0.01,0.5,4901))
print(f"split factor f_max = {f:.5f}")
# check numerically against the exact H_W dispersion
def E(k,r): return np.sqrt(np.sum(np.sin(k)**2)+(r*np.sum(1-np.cos(k)))**2)
for r in (1.0,0.5):
    print(f"--- r = {r}: speed excess s = r m l / 2;  extra species masses 2r, 4r, 6r (flow units)")
    for d,S in dirs.items():
        c2=3*(r**2/8-S/6)
        n={'axis':np.array([1,0,0.]),'face':np.array([1,1,0.])/np.sqrt(2),'body':np.ones(3)/np.sqrt(3)}[d]
        ks=np.array([0.01,0.02,0.04]); v=np.array([(E((k+1e-5)*n,r)-E((k-1e-5)*n,r))/2e-5 for k in ks]); c2num=np.polyfit(ks**2,v,1)[0]
        line=f"  {d}: c2 = {c2:+.4f} (numeric {c2num:+.4f})"
        if c2<0: line+=f"; photon splitting (s absorbed) C = {(1/((2/3)*abs(c2)*f))**0.25:.2f}"
        # Crab: v-1 = s + c2 (p l)^2 < smax at 2.31 PeV (s kept / s absorbed)
        g=lambda l,sk: (r*l/(2*lamC) if sk else 0)+max(c2,0)*(l/hc_p)**2-smax
        for sk in (True,False):
            try: lb=brentq(lambda l: g(l,sk),1e-40,1e-28,xtol=1e-48,rtol=1e-10); line+=f"; Crab bound ({'s kept' if sk else 's absorbed'}) l < {lb:.2e} m"
            except ValueError: line+=f"; no Crab bound ({'s kept' if sk else 's absorbed'})"
        print(line)
