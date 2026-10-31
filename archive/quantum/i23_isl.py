# Reading I23: CO's route-(b) signal in a Lee-type inverse-square test, using Run 96's registered geometry functions (model96).
import sys, numpy as np
sys.dont_write_bytecode = True
sys.path.insert(0, "/home/claude/quantum96")
import model96 as M
from scipy.optimize import brentq
k0 = M.LEE["k"]; td, ta = M.LEE["td"], M.LEE["ta"]
def dev(rC, s, k=k0):
    TN = M._slab(lambda z: M._phiN(z, k), s, td, ta)
    TS = M._slab(lambda z: M._phiS(z, k, np.sqrt(1.5) * rC), s, td, ta)
    return (TS - TN) / TN
print("Run 96 cap reproduced:", M.lee_cap())
print("fractional change of the signal, Lee geometry (k = 120/22 mm), gap s:")
rs = [1e-6, 3e-6, 10e-6, 20e-6, 30e-6, 40e-6, 51e-6]
print("  r_C (um): " + "  ".join(f"{r*1e6:7.0f}" for r in rs))
for s in [52e-6, 30e-6, 20e-6, 10e-6]:
    print(f"  s={s*1e6:3.0f} um: " + "  ".join(f"{dev(r, s):+.1e}" for r in rs))
print("r_C at which |deviation| reaches a given precision, Lee geometry:")
for s in [52e-6, 30e-6, 20e-6, 10e-6]:
    out = []
    for e in [1e-1, 1e-2, 1e-3]:
        f = lambda l: abs(dev(10**l, s)) - e
        try: out.append(f"{e:.0e}: {10**brentq(f, -7, -3.5)*1e6:5.1f} um")
        except ValueError: out.append(f"{e:.0e}: none")
    print(f"  s={s*1e6:3.0f} um  " + ";  ".join(out))
# small r_C behaviour: tail argument
for r in [5e-6, 10e-6, 20e-6]:
    sig = np.sqrt(1.5) * r; print(f"  r_C={r*1e6:.0f} um, sigma={sig*1e6:.1f} um, exp(-s^2/2sigma^2) at s=52 um: {np.exp(-(52e-6)**2/(2*sig**2)):.1e}")
print("finer patterning (k x10, x30) at s = 10 um, Lee's plate thicknesses:")
for kf in [10, 30]:
    out=[]
    for e in [1e-2, 1e-3]:
        f = lambda l: abs(dev(10**l, 10e-6, k0*kf)) - e
        try: out.append(f"{e:.0e}: {10**brentq(f, -7, -3.5)*1e6:5.1f} um")
        except ValueError: out.append(f"{e:.0e}: none")
    print(f"  k x{kf} (wavelength {2*np.pi/(k0*kf)*1e6:.0f} um): " + ";  ".join(out))
