"""Sink shot noise at the current constants.
The mean field is G's: U = G m / (c^2 r). Renewals are Poisson at Gamma = m c^2 / hbar per nucleon, each retaining delta*hbar;
the field is proportional to the count, so over an averaging time tau its relative fluctuation is 1/sqrt(Gamma*tau).
A clock of frequency omega a distance r away accumulates phase noise dphi ~ omega * U * tau / sqrt(Gamma*tau) = omega*U*sqrt(tau/Gamma).
G is fixed by measurement, so delta drops out (delta sets the size of each deposit, the count sets G's field)."""
import math
G=6.674e-11; c=2.998e8; hbar=1.055e-34; m_n=1.675e-27; m_e=9.109e-31
Gam=m_n*c**2/hbar; om_e=m_e*c**2/hbar
for r in (1e-10,1e-15):
    U=G*m_n/(c**2*r)
    for tau in (1.0,):
        print(f"r={r:g} m: U={U:.1e}; electron-clock phase noise per nucleon over {tau} s ~ {om_e*U*math.sqrt(tau/Gam):.1e} rad")
