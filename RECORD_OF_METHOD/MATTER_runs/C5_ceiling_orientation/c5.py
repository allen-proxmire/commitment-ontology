# Photon ceiling against sky directions: what present photons say about the cube's orientation.
# E_th = C(n) sqrt(m_e c^2 hbar c / l); C(n) = min over x of the root of (|c2|/3) g(x) C^4 - (r/2) C^2 - 1/(2x(1-x)) = 0,
# c2(n) = 3(r^2/8 - sum n^4/6), g = x^3 + (1-x)^3 (speed excess kept).
import numpy as np
from scipy.spatial.transform import Rotation as Rot
r=0.5; xs=np.linspace(0.02,0.5,241)
def C(n):
    n=np.asarray(n)/np.linalg.norm(n); c2=abs(3*(r*r/8-np.sum(n**4)/6)); g=xs**3+(1-xs)**3
    a=c2/3*g; b=r/2; c=1/(2*xs*(1-xs)); return np.sqrt(((b+np.sqrt(b*b+4*a*c))/(2*a)).min())
print("C axis/face/body:",[round(C(v),3) for v in ((1,0,0),(1,1,0),(1,1,1))])
def unit(ra,dec):
    ra,dec=np.radians(ra),np.radians(dec); return np.array([np.cos(dec)*np.cos(ra),np.cos(dec)*np.sin(ra),np.sin(dec)])
hc=1.97327e-7; me=0.511e6
lb=lambda Cv,E: hc*me*Cv**2/E**2      # bound on l (m) from a photon of energy E (eV) seen unsplit
cyg=unit(308.107,40.958); crab=unit(83.633,22.014); E1=3.32e15
print(f"Cyg X-3 alone: l < {lb(C((1,1,1)),E1):.2e} m (body diagonal, worst case) to {lb(C((1,0,0)),E1):.2e} m (axis)")
rots=Rot.random(20000,random_state=1)
c1=np.array([C(v) for v in rots.apply(cyg)]); b1=lb(c1,E1)
print(f"over random orientations: median bound {np.median(b1):.2e} m; 10% of orientations give l < {np.percentile(b1,10):.2e} m")
print(f"a second photon matters only above E1*C_axis/C_body = {E1*C((1,0,0))/C((1,1,1))/1e15:.2f} PeV (Crab's record is 1.1 PeV)")
print(f"angle Cyg X-3 to Crab: {np.degrees(np.arccos(cyg@crab)):.1f} deg")
c2=np.array([C(v) for v in rots.apply(crab)])
for E2 in (1.12e15,2.0e15,2.5e15,3.3e15):
    b=np.minimum(b1,lb(c2,E2)); print(f"second photon from the Crab's direction at {E2/1e15:.2f} PeV: worst-case bound {b.max():.2e} m (from {b1.max():.2e}); orientations it tightens: {np.mean(lb(c2,E2)<b1)*100:.0f}%")
# at the candidate neutrino bound
l=1.0e-32; print(f"at l = 1.0e-32 m the ceiling is {C((1,0,0))*np.sqrt(me*hc/l)/1e15:.1f}-{C((1,1,1))*np.sqrt(me*hc/l)/1e15:.1f} PeV: no observed photon reaches it in any orientation")
