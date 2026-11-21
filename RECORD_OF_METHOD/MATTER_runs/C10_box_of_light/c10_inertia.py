# Does a rigid-walled box of trapped massless pattern resist a push as a mass E0 would?
# Box carried by a heavy slow carrier (mass Mw): H = (K - p)^2/(2 Mw) + H_box. To second order the box adds inertia 2S,
# with E(lam) = E0 - lam^2 S the box's level under H_box - lam p. A mass E0 would add E0.
import numpy as np,sys,scipy.sparse as sp; sys.path.insert(0,'../../SPACE_AND_GRAVITY_runs/F1_flow_gravity')
from flow1d import build
r=0.5; L=900; w=240; x=np.arange(L); inside=(x>=L//2-w//2)&(x<L//2+w//2)
H0=build(L,1.0,r,np.where(inside,0.0,1.0),np.ones(L)).toarray()
S=np.roll(np.eye(L),1,axis=1); pk=np.kron((S-S.T)/(2j),np.eye(2))      # lattice momentum sin k
def E(lam):
    e=np.linalg.eigvalsh(H0-lam*pk); return np.sort(e[e>1e-9])[0]
E0=E(0); 
for lam in (0.02,0.05,0.1):
    Sx=(E0-E(lam))/lam**2; print(f"lam={lam}: S = {Sx:.6f} = {Sx/E0:.4f} E0; added inertia 2S = {2*Sx/E0:.4f} E0")
print("bouncing picture: round trip w/(1-lam) + w/(1+lam), so E = E0 (1 - lam^2), S = E0, added inertia 2 E0")
