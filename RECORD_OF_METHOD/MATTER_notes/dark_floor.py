"""Mass floor for a never-thermal dark fermion: exclusion at the start plus coldness.
Exclusion: at most one pattern per state, so for a given number the slowest packing is a
filled sphere of momenta, p_F = hbar (6 pi^2 n / g)^(1/3), mean momentum (3/4) p_F.
Occupancy is kept as space stretches, so this holds today."""
import math
hbarc = 1.97327e-5          # eV cm
rho_c = 0.120 * 1.05371e-5 * 1e9   # eV / cm^3, Omega_c h^2 = 0.120
g = 2                        # two spin states, patterns only (one sign)
kTx = 8.617e-5 * 2.7255 * (3.91/106.75)**(1/3)   # eV, the note's T_x
eta, mp = 6.1e-10, 0.93827e9
def vmin(m):                 # least mean speed today / c, m in eV
    n = rho_c / m
    return 0.75 * hbarc * (6*math.pi**2*n/g)**(1/3) / m
def fmin(m):                 # least start momentum in units of the light's (note's f)
    return vmin(m) * m / (3.15*kTx)
print("v_min(1 keV) = %.2e c ; f_min(0.13 keV) = %.2f ; f_min(1 keV) = %.2f" % (vmin(1e3), fmin(130), fmin(1e3)))
for name, vb in [("galaxy counts", 5e-8), ("Lyman-alpha, loose", 2.2e-8), ("Lyman-alpha, tight", 1.3e-8)]:
    m = 1e3 * (vmin(1e3)/vb)**0.75          # v_min ~ m^(-4/3)
    r = 5.36*mp/m
    for p in (1, 10):
        ratio = 1/(p*eta*(1+r))
        print("%-20s m > %.1f keV  r < %.1e  f_min %.2f  p=%2d: places x%.0f, length x%.1f" % (name, m/1e3, r, fmin(m), p, ratio, ratio**(1/3)))
