"""S1: Majorana-type (signless) version of the adopted walk. See REGISTRATION.md."""
import numpy as np, itertools, json
from scipy.linalg import logm
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
gamma0=beta; gamma=[beta@a for a in alpha]
C=1j*gamma[1]                             # charge conjugation for this walk: C alpha_j^* C^-1 = alpha_j, C beta^* C^-1 = -beta
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
P=lambda j,k: Pp[j]*np.exp(1j*k)+Pm[j]*np.exp(-1j*k)
W=lambda k: sum(1-np.cos(kj) for kj in k)
def U(k,th=0.3,r=0.3):
    ang=th+r*W(k); M=np.cos(ang)*np.eye(4)-1j*np.sin(ang)*beta
    return P(0,k[0])@P(1,k[1])@P(2,k[2])@M@P(2,k[2])@P(1,k[1])@P(0,k[0])
G=lambda k: 1j*logm(U(k))                 # Hermitian generator
rng=np.random.default_rng(0); ks=[tuple(rng.uniform(-np.pi,np.pi,3)) for _ in range(200)]
# (1) C-symmetry of the walk: C U(k)^* C^-1 == U(-k)
csym=max(np.abs(C@U(k).conj()@np.linalg.inv(C)-U(tuple(-np.array(k)))).max() for k in ks)
# (2) symmetric / antisymmetric parts of the Majorana bilinear kernel
S=[];A=[]
for k in ks:
    M1=C@G(k); M2=(C@G(tuple(-np.array(k)))).T
    S.append(np.abs(M1+M2).max()/2); A.append(np.abs(M1-M2).max()/2)
out={'C_symmetry_residual':float(csym),'symmetric_part_max':float(max(S)),'antisymmetric_part_max':float(max(A)),
     'antisymmetric_part_min':float(min(A))}
print(out); json.dump(out,open('s1_result.json','w'),indent=1)
