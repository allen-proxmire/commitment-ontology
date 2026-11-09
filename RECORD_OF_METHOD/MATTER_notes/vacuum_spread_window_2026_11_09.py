"""Vacuum-spread window recomputed at the current constants (fixed share; q = P_max; l <= 1.3e-31 m).
delta = 4 pi l_P^2 P_max / l^2 (units of hbar for P_max); taking l at its bound gives the smallest delta.
Dent: Gamma = (delta*hbar/sigma)^2 * omega  (fixed share: dent = delta*hbar).  Clock: sigma <~ P_max sqrt(N)/(omega t)."""
import math
hbar=1.055e-34; c=3e8; lP=1.616e-35; m_n=1.67e-27; m_e=9.11e-31
l=1.3e-31
for Pmax in (1.0,3.0,100.0):                       # P_max in units of hbar
    delta=4*math.pi*lP**2*Pmax/l**2
    om_n=m_n*c**2/hbar; om_e=m_e*c**2/hbar
    low=delta*math.sqrt(om_n/1e-17)                # sigma lower bound, units of hbar
    ups=[]
    for m,om in ((m_e,om_e),(m_n,om_n)):
        N=(hbar/(m*c)/l)**3; ups.append(Pmax*math.sqrt(N)/(om*1.0))
    print(f"P_max={Pmax:g} hbar: delta={delta:.1e}; dent needs sigma >~ {low:.1e} hbar ({low/Pmax:.0e} P_max); "
          f"clock: electron sigma <~ {ups[0]:.1e}, nucleon sigma <~ {ups[1]:.1e} hbar; window empty by {low/ups[1]:.0e}")
