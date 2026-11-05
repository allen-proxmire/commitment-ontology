"""Check: what internal symmetry survives on the matter sector's Clifford four?
Computes the commutant of the Dirac coin set {alpha_1, alpha_2, alpha_3} (massless)
and {alpha_i, beta} (massive) acting on C^4, and the spin content of C^4 under rotations.
Result: massless commutant dim 2 (1, gamma5); massive commutant dim 1 (scalars only);
C^4 under SO(3) is 2+2, no triplet."""
import numpy as np
from scipy.linalg import null_space
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]
beta=np.block([[I2,Z],[Z,-I2]])
def commutant_dim(mats):
    M=np.vstack([np.kron(np.eye(4),A.T)-np.kron(A,np.eye(4)) for A in mats])
    return null_space(M).shape[1]
print("commutant dim, massless (alpha only):", commutant_dim(alpha))
print("commutant dim, massive (alpha+beta): ", commutant_dim(alpha+[beta]))
S=[(1j/4)*(alpha[j]@alpha[k]-alpha[k]@alpha[j]) for j,k in [(1,2),(2,0),(0,1)]]
print("Casimir S^2 eigenvalues:", np.round(np.linalg.eigvalsh(sum(Si@Si for Si in S)),4))
