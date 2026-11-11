"""G3 post-run check: the long-wavelength limit of every invariant lattice cost, compared with G1's
continuum family (linearised Einstein-Hilbert up to strength and speed)."""
import numpy as np
exec(open('g3_lattice_gauge.py').read().split("nf=len(AB)")[0])
basis=np.load('g3_basis.npy'); rng=np.random.default_rng(11)
# map lattice components to a symmetric 4x4 h (continuum labels)
def H_of(h):
    H=np.zeros((4,4)); H[0,0]=h[0]
    for i in range(3): H[0,1+i]=H[1+i,0]=h[1+i]; H[1+i,1+i]=h[4+i]
    for (i,j),a in off.items(): H[1+i,1+j]=H[1+j,1+i]=h[a]
    return H
g1=open('../G1_gauge_isotropy/g1_gauge_isotropy.py').read().split("for name,g in")[0]
ns={}; exec(g1,ns)
cnull=ns['solve'](ns['rotation'],1500)          # G1 continuum family (dimension 2)
eps=1e-3; X=[]; Y=[]
for n in range(1500):
    kv=rng.normal(size=4); h=rng.normal(size=10)
    lat=np.array([feat(h,eps*kv)@b for b in basis])/eps**2     # leading-order limit of each lattice cost
    X.append(ns['feat'](H_of(h),kv)@cnull.T); Y.append(lat)
X=np.array(X); Y=np.array(Y)
coef,res,_,_=np.linalg.lstsq(X,Y,rcond=None)
resid=np.linalg.norm(X@coef-Y,axis=0)/np.maximum(np.linalg.norm(Y,axis=0),1e-30)
lead_rank=np.linalg.matrix_rank(Y,tol=1e-6*np.abs(Y).max())
print('lattice invariant costs',len(basis))
print('rank of their long-wavelength limits',lead_rank)
print('max relative residual against G1 family',resid.max(),' median',np.median(resid))
print('how many costs vanish at leading order (pure lattice-scale terms):',int(np.sum(np.linalg.norm(Y,axis=0)<1e-6*np.linalg.norm(Y))))
