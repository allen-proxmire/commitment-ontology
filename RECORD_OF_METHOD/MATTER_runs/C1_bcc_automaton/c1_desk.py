import numpy as np
from scipy.optimize import minimize
# Bisio-D'Ariano-Perinotti BCC Weyl automaton (Found. Phys. 2015, arXiv:1601.04832, Eq. 15), sign choice +.
def un(k,sg=+1):
    c=np.cos(np.asarray(k)/np.sqrt(3)); s=np.sin(np.asarray(k)/np.sqrt(3))
    u=c[0]*c[1]*c[2]+sg*s[0]*s[1]*s[2]
    n=np.array([s[0]*c[1]*c[2]-sg*c[0]*s[1]*s[2], -sg*c[0]*s[1]*c[2]-s[0]*c[1]*s[2], c[0]*c[1]*s[2]-sg*s[0]*s[1]*c[2]])
    return u,n
sig=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1.,-1])]
def A(k,sg=+1):
    u,n=un(k,sg); return u*np.eye(2)-1j*sum(n[i]*sig[i] for i in range(3))
rng=np.random.default_rng(0)
# unitarity check
print("unitarity:",max(np.abs(A(k)@A(k).conj().T-np.eye(2)).max() for k in rng.uniform(-3,3,(200,3))))
# BZ: |k_i +- k_j| <= sqrt3 pi. Zeros of the Weyl spectrum (u=+-1) inside the BZ
def inBZ(k): return all(abs(k[i]+t*k[j])<=np.sqrt(3)*np.pi+1e-9 for i in range(3) for j in range(i+1,3) for t in (1,-1))
best=[]
for target in (+1,-1):
    pts=[k for k in rng.uniform(-np.sqrt(3)*np.pi,np.sqrt(3)*np.pi,(60000,3)) if inBZ(k)]
    f=lambda k: (target-un(k)[0])**2
    cand=sorted(pts,key=f)[:40]; sols=[]
    for k0 in cand:
        r=minimize(f,k0,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-16})
        if r.fun<1e-12:
            kk=r.x
            if not any(np.allclose(kk,s,atol=1e-3) for s in sols): sols.append(kk)
    print(f"points with u={target:+d} found (k/sqrt3 pi):",[np.round(s/(np.sqrt(3)*np.pi),3).tolist() for s in sols][:8])
# reciprocal lattice of BCC with primitive vectors (+-1,+-1,+-1)/sqrt3 ... check whether those points are equivalent to 0 by a reciprocal vector
# rotational covariance: is n(Pk) = R n(k) for a fixed rotation R, P = cyclic permutation (x->y->z) or swap x<->y ?
def test(P):
    K=rng.uniform(-2,2,(300,3)); N1=np.array([un(k)[1] for k in K]); N2=np.array([un(k[P])[1] for k in K])
    U1=np.array([un(k)[0] for k in K]); U2=np.array([un(k[P])[0] for k in K])
    # Procrustes: N2 ~ N1 R^T
    M=N1.T@N2; Us,S,Vt=np.linalg.svd(M); R=(Us@Vt).T
    return np.abs(U1-U2).max(), np.abs(N2-N1@R.T).max(), np.round(R,3)
for name,P in [('cyclic x->y->z',[1,2,0]),('swap x<->y',[1,0,2]),('inversion',None)]:
    if P is None:
        K=rng.uniform(-2,2,(300,3)); print(name, "u(-k)-u(k) max:",max(abs(un(-k)[0]-un(k)[0]) for k in K)); continue
    du,dn,R=test(P); print(f"{name}: max|u(Pk)-u(k)|={du:.1e}  max|n(Pk)-R n(k)|={dn:.1e}  R=\n{R}")
# small-k dispersion: speed and isotropy
for d in [np.array([1,0,0]),np.array([1,1,0])/np.sqrt(2),np.array([1,1,1])/np.sqrt(3),np.array([1,-1,1])/np.sqrt(3)]:
    ks=np.array([0.01,0.02,0.04,0.08]); om=np.array([np.arccos(un(k*d)[0]) for k in ks])
    p=np.polyfit(ks**2,om/ks,1); print("dir",np.round(d,3),"speed",round(p[1],6),"quadratic coeff",round(p[0]/p[1],4))
# odd-in-k part of the dispersion along a body diagonal
d=np.array([1,1,1])/np.sqrt(3)
for k in (0.01,0.02,0.04):
    wp=np.arccos(un(k*d)[0]); wm=np.arccos(un(-k*d)[0]); print(f"k={k}: omega(+k)-omega(-k) = {wp-wm:+.3e}  ratio to k^2: {(wp-wm)/k**2:+.4f}")
# Dirac automaton (n A on one block, n A^dagger-type partner): dispersion arccos(n u_k); same odd part
