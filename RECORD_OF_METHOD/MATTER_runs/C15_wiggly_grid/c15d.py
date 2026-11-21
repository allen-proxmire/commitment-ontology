# Desk numbers for C15: how uneven can the hop strengths be, place to place, before far-travelled high-energy patterns are scattered away?
# 3D Rayleigh law (Born, checked in 2D by c15a: loss rate 0.5 eps^2 k^3): mean free path = 2 pi/(eps^2 k^4 l^3), to a factor of order one.
import numpy as np
hc=1.9733e-7
for E,L,lab in ((3.08e15,9*3.0857e19,"3.08 PeV photon, Cygnus X-3, 9 kpc (if light's carriers feel the unevenness as matter's hops do)"),
                (2.9e14,4.0e25,"290 TeV neutrino, TXS 0506+056, 1.3 Gpc (association at about 3 sigma)")):
    k=E/hc; print(lab)
    for l in (5.73e-35,1.0e-32,2.4e-31):
        print(f"   l = {l:.2g} m: k l = {k*l:.1e}; arrives unscattered only if eps < {np.sqrt(2*np.pi/(k**4*l**3*L)):.1e};  if only the next order scatters (rate ~ k^6 l^5): mean free path {1/(k**6*l**5):.1e} m against {L:.1e} m")
for R in (0.03,0.002): print(f"a seam turning back {R*100:.1f}% per crossing: half lost after {np.log(2)/R:.0f} seams")
