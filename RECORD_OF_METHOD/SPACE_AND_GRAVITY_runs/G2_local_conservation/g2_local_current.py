"""G2 check: the free walk's energy and momentum densities change, tick by tick, by the divergence
of a finite-range current (1D Dirac walk, ring of 40 places). The current is built as the running sum of
the per-place change; it is local if perturbing a far place changes it only near that place."""
import numpy as np
rng=np.random.default_rng(3); N=40; w=0.3
C=np.array([[np.cos(w),-1j*np.sin(w)],[-1j*np.sin(w),np.cos(w)]])
def U(p):
    q=p@C.T; o=np.empty_like(q); o[:,0]=np.roll(q[:,0],1); o[:,1]=np.roll(q[:,1],-1); return o
def eps(p): return -np.imag(np.sum(np.conj(p)*U(p),axis=1))
def pi(p): return np.imag(np.sum(np.conj(p)*np.roll(p,1,axis=0),axis=1))
def current(p,dens):
    d=dens(U(p))-dens(p); return d,-np.cumsum(d)
p=rng.normal(size=(N,2))+1j*rng.normal(size=(N,2))
for name,dens in [('energy',eps),('momentum',pi)]:
    d,J=current(p,dens); p2=p.copy(); p2[30]+=0.5; d2,J2=current(p2,dens)
    print(name,'total change',abs(d.sum()),'current changed only at places',np.where(np.abs(J2-J)>1e-12)[0])
