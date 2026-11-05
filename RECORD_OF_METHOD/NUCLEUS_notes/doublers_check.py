"""Check: does the cubic Dirac automaton used in Q1 (psi <- M Pz Py Px psi) have fermion doublers?
Bloch operator U(k) = M * prod_j (Pp_j e^{ik_j} + Pm_j e^{-ik_j}). Count gapless points in the Brillouin zone.
Result: massless, 12 gapless points at quasi-energy 0 (origin; three zone-edge points (pi,pi,0) etc.;
eight points (±pi/2,±pi/2,±pi/2)). With mass theta, the origin and the three zone-edge points gap by theta;
the eight (±pi/2)^3 points stay gapless."""
import numpy as np, itertools
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
def U(k,theta):
    u=np.eye(4)
    for j in range(3): u=(Pp[j]*np.exp(1j*k[j])+Pm[j]*np.exp(-1j*k[j]))@u
    return (np.cos(theta)*np.eye(4)-1j*np.sin(theta)*beta)@u
gap=lambda k,th: np.min(np.abs(np.angle(np.linalg.eigvals(U(k,th)))))
pts=[(0,0,0),(np.pi,np.pi,0),(np.pi,0,np.pi),(0,np.pi,np.pi)]+[tuple(np.pi/2*np.array(sg)) for sg in itertools.product([1,-1],repeat=3)]
for th in (0.0,0.3):
    print("theta =",th); 
    for k in pts: print("  k/pi =",np.round(np.array(k)/np.pi,2),"gap =",round(gap(k,th),3))
