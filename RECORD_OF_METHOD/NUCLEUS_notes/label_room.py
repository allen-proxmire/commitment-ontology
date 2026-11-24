# Room at a place for a second two-way label, and whether the proton's count needs a rule beyond the exchange sign. Desk checks.
import numpy as np
sx=np.array([[0,1],[1,0]])/2; sy=np.array([[0,-1j],[1j,0]])/2; sz=np.array([[1,0],[0,-1]])/2; I2=np.eye(2)
# 1b. The same count with up and down as two species and only the exchange sign: like quarks symmetric in spin (colour antisymmetric, one orbital).
#     uuu, ddd: spin 3/2 (4 each); uud, udd: the like pair has spin 1, with the third 1/2 or 3/2 (2 + 4 each).
print("1b. two species, exchange sign only: uuu 4 + ddd 4 + uud (2 + 4) + udd (2 + 4) =",4+4+6+6,"; spin 1/2: 4 (proton, neutron), spin 3/2: 16. The same 20: no rule beyond the exchange sign.")
# 3. Is there room at a place for a second two-way label? Operators at a place that commute with the pattern's own set (the alphas and beta).
from scipy.linalg import null_space
def commutant(mats):
    d=mats[0].shape[0]; M=np.vstack([np.kron(np.eye(d),A.T)-np.kron(A,np.eye(d)) for A in mats]); return null_space(M)
Z2=np.zeros((2,2)); s=[2*sx,2*sy,2*sz]
a4=[np.block([[Z2,si],[si,Z2]]) for si in s]; b4=np.block([[I2,Z2],[Z2,-I2]])
print("3. the step's four (C6): operators at a place commuting with alpha_x, alpha_y, alpha_z, beta:",commutant(a4+[b4]).shape[1],"(1 = multiples of the identity: no room for a label)")
X=2*sx; Y=2*sy; Zm=2*sz; k3=lambda a,b,c: np.kron(np.kron(a,b),c)
a8=[k3(X,I2,I2),k3(Zm,X,I2),k3(Zm,Zm,X)]; b8=k3(Zm,Zm,Zm); tau=[k3(I2,X,Y),k3(X,Y,I2),k3(X,Zm,Y)]
C=commutant(a8+[b8]); print("   the staggered cell's eight: commuting operators:",C.shape[1],"(4 = the identity and three more: one two-way label)")
ok=max(np.linalg.norm(t@A-A@t) for t in tau for A in a8+[b8]); S8=[(-1j/2)*a8[j]@a8[k] for j,k in ((1,2),(2,0),(0,1))]
su2=max(np.linalg.norm(tau[i]@tau[j]-tau[j]@tau[i]-2j*tau[k]) for i,j,k in ((0,1,2),(1,2,0),(2,0,1))); su2m=max(np.linalg.norm(tau[i]@tau[j]-tau[j]@tau[i]+2j*tau[k]) for i,j,k in ((0,1,2),(1,2,0),(2,0,1)))
print(f"   the three tau commute with the alphas and beta to {ok:.0e}; with the spin to {max(np.linalg.norm(t@S-S@t) for t in tau for S in S8):.0e}; they close as a two-way label's rotations to {min(su2,su2m):.0e}; spin S(S+1) on the eight: {sorted(set(np.round(np.linalg.eigvalsh(sum(S@S for S in S8)),6)))}")
