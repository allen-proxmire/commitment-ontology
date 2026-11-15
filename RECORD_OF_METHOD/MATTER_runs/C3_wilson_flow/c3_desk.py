import numpy as np, itertools
from scipy.linalg import expm
from scipy.optimize import minimize
# Candidate cubic step: U = exp(-i tau H_W), H_W = sum_j alpha_j sin k_j + beta (m + r sum_j (1 - cos k_j))  (Wilson-Dirac, cubic by construction)
I2=np.eye(2); Z2=np.zeros((2,2)); s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z2,si],[si,Z2]]) for si in s]; beta=np.block([[I2,Z2],[Z2,-I2]])
def H(k,m,r): return sum(alpha[j]*np.sin(k[j]) for j in range(3))+beta*(m+r*sum(1-np.cos(k[j]) for j in range(3)))
def U(k,m,r,tau): return expm(-1j*tau*H(k,m,r))
tau=0.4; r=1.0; m=0.03/tau
print("max |E| of H over the zone (bandwidth):", max(np.abs(np.linalg.eigvalsh(H(k,m,r))).max() for k in itertools.product(np.linspace(-np.pi,np.pi,21),repeat=3)))
print("tau*bandwidth (must stay below pi for a gap at quasienergy pi):", tau*max(np.abs(np.linalg.eigvalsh(H(k,m,r))).max() for k in itertools.product(np.linspace(-np.pi,np.pi,21),repeat=3)))
for corner in itertools.product((0,np.pi),repeat=3):
    e=np.abs(np.angle(np.linalg.eigvals(U(np.array(corner),m,r,tau)))).min(); print("corner",np.round(np.array(corner)/np.pi).astype(int),"smallest |quasienergy|",round(e,4))
rng=np.random.default_rng(0)
f=lambda k: np.abs(np.angle(np.linalg.eigvals(U(k,m,r,tau)))).min()
g=lambda k: np.pi-np.abs(np.angle(np.linalg.eigvals(U(k,m,r,tau)))).max()
for name,fun in (("0-gap",f),("pi-gap",g)):
    starts=sorted(rng.uniform(-np.pi,np.pi,(3000,3)),key=fun)[:5]
    best=min(minimize(fun,k0,method='Nelder-Mead').fun for k0 in starts); print(name,"smallest found:",round(best,4))
# cubic symmetry: spectrum under axis permutation and the existence of a spinor rotation
k=np.array([0.3,-0.7,1.1]); print("permutation check: |spec(k)-spec(Pk)| =",np.abs(np.sort(np.angle(np.linalg.eigvals(U(k,m,r,tau))))-np.sort(np.angle(np.linalg.eigvals(U(k[[1,2,0]],m,r,tau))))).max())
# tails: amplitude to hop n places along x in one step
N=64; ks=2*np.pi*np.arange(N)/N
amps=np.array([np.linalg.norm(sum(U(np.array([kk,0,0]),m,r,tau)*np.exp(1j*kk*n) for kk in ks)/N) for n in range(8)])
print("amplitude reach along an axis, n = 0..7 places:",np.array2string(amps,precision=2))
# low-energy speed and speed excess
ks2=np.array([0.01,0.02,0.04]); E=[np.abs(np.angle(np.linalg.eigvals(U(np.array([q,0,0]),0,r,tau)))).min() for q in ks2]
print("massless speed per step:",np.round(np.array(E)/ks2,6))
# spinor rotation for the cyclic permutation x->y->z: 120 degrees about (1,1,1) in each 2x2 block
from scipy.linalg import expm as ex
n=np.ones(3)/np.sqrt(3); rot2=ex(-1j*(2*np.pi/3)/2*sum(n[i]*s[i] for i in range(3))); R=np.block([[rot2,Z2],[Z2,rot2]])
err=max(np.abs(R@U(k,m,r,tau)@R.conj().T-U(k[[2,0,1]],m,r,tau)).max() for k in rng.uniform(-3,3,(50,3)))
err2=max(np.abs(R@U(k,m,r,tau)@R.conj().T-U(k[[1,2,0]],m,r,tau)).max() for k in rng.uniform(-3,3,(50,3)))
print("R U(k) R^dag = U(Pk) for the cyclic permutation: max error",min(err,err2))
# the palindromic walk fails the same test with any R (I4 cold read); here it holds as an operator identity
