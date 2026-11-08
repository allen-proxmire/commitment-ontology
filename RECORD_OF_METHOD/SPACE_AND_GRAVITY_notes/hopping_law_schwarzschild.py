"""Which transport law does the exact Schwarzschild exterior satisfy (isotropic coordinates)?
N = (1 - M/2r)/(1 + M/2r) (clock rate), psi = 1 + M/2r (g_ij = psi^4 delta).
Flux through a sphere, times r^2, must be constant for a conserved steady state with a point sink."""
import math
M=1.0
N  =lambda r:(1-M/(2*r))/(1+M/(2*r))
psi=lambda r:1+M/(2*r)
d  =lambda f,r,h=1e-5:(f(r+h)-f(r-h))/(2*h)
lnN=lambda r:math.log(N(r))
for r in [0.6,1.0,2.0,5.0,20.0,100.0]:
    flat      = r**2*d(lnN,r)                       # ratio hopping, flat network (the ln P law)
    curved    = r**2*psi(r)**2*d(lnN,r)             # ratio hopping, curved network (conductance psi^2)
    weighted  = r**2*psi(r)**2*N(r)*d(lnN,r)        # ratio hopping, curved network, hops at the local clock rate N
    print(f"r={r:6.1f}  flat={flat:.6f}  curved={curved:.6f}  curved+clock={weighted:.6f}")
# only curved+clock is constant (= M): Schwarzschild satisfies d(psi^2 N dlnN) = d(psi^2 dN) = 0, i.e. D^2 N = 0
