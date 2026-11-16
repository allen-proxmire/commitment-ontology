# C4 desk check: on the flow step, a light fermion's energy at E >> m carries a term k r m/2 (the speed excess s = r m/2),
# so two mass states differ by k r (m3 - m2)/2 on top of the standard (m3^2 - m2^2)/2k. Hop units (hbar = c = l = 1).
import numpy as np
r=0.5
def E(k,n,m):
    kk=k*np.asarray(n)/np.linalg.norm(n)
    return np.sqrt(np.sum(np.sin(kk)**2)+(m+r*np.sum(1-np.cos(kk)))**2)
m2,m3=1e-9,5e-9
for n in ((1,0,0),(1,1,0),(1,1,1)):
    for k in (1e-3,1e-2,3e-2):
        d=E(k,n,m3)-E(k,n,m2); std=(m3**2-m2**2)/(2*k); lat=k*r*(m3-m2)/2
        print(f"n={n}, k={k:g}: E3-E2 = {d:.6e}; standard {std:.3e} + lattice k r dm/2 {lat:.6e} = {std+lat:.6e} (ratio {d/(std+lat):.6f})")
# physical numbers
hbarc=1.9733e-7  # eV m
dm=0.041  # normal ordering, m1 ~ 0
th=np.pi/4; bound=2.7e-28   # IceCube 2018, |c(4)_mutau| < 2.7e-28 (90%), 0.4-18 TeV
for l in (2.4e-31,3.2e-32):
    El=hbarc/l; c=r*dm*np.sin(2*th)/(4*El); print(f"l = {l:.1e} m: E_l = {El:.2e} eV, c_eff = r dm sin2th23/(4 E_l) = {c:.2e}")
El_min=r*dm/(4*bound); print(f"bound: E_l >= {El_min:.2e} eV, l <= {hbarc/El_min:.2e} m; delta >= {6e-8*(2.4e-31/(hbarc/El_min))**2:.1e}")
for dmx,lab in ((0.027,"normal, m1~0.03"),(0.05,"inverted, lightest~0"),(0.0028,"quasi-degenerate at KATRIN")):
    print(f"  dm = {dmx} eV ({lab}): l <= {hbarc/(r*dmx/(4*bound)):.2e} m")
El=r*dm/(4*bound); Eeq=np.sqrt((0.0086+0.0507)*El/r); print(f"at the bound the lattice term equals the standard one at E = {Eeq:.2e} eV")
for C in (2.92,5.10): print(f"photon ceiling at that l, C={C}: {C*np.sqrt(0.511e6*El)/1e15:.1f} PeV")
