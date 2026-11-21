# The lattice's extra copies on the flow step (m = 0): every local minimum of E(k) over the zone, for several r.
# Near an n-flip corner, E^2 = (2rn)^2 + (1 - 2 r^2 n) q_flipped^2 + (1 + 2 r^2 n) q_unflipped^2 + ..., so it is a minimum iff 2 r^2 n < 1.
# E(k)^2 = sum sin^2 k_j + (r sum(1 - cos k_j))^2. At a corner with n components at pi: E = 2 r n.
import numpy as np
from scipy.ndimage import minimum_filter
n=96; g=np.arange(n)*2*np.pi/n; KX,KY,KZ=np.meshgrid(g,g,g,indexing='ij')
for r in (0.1,0.3,0.5,0.6,0.7,0.75,0.8,1.0,1.5):
    E=np.sqrt(np.sin(KX)**2+np.sin(KY)**2+np.sin(KZ)**2+(r*(3-np.cos(KX)-np.cos(KY)-np.cos(KZ)))**2)
    loc=(E==minimum_filter(E,size=3,mode='wrap')); vals=sorted(set(np.round(E[loc],4)))
    kept=[nn for nn in (1,2,3) if 2*r*r*nn<1]
    print(f"r={r}: local minima of E at {[float(v) for v in vals]}; rule (an n-flip corner is a minimum iff n < 1/(2 r^2)): n = {kept}, energies {[round(2*r*nn,3) for nn in kept]}")
