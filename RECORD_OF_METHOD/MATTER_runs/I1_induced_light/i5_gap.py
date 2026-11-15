import numpy as np,sys,itertools; sys.path.insert(0,'.')
from i2 import Ak,Fb
from scipy.optimize import minimize
w=5*np.pi/16; th=0.03
def Us(k,o): a,b,c=o; return Ak(a,k[a],w)@Ak(b,k[b],w)@Ak(c,k[c],w)@Fb(th)@Ak(c,k[c],w)@Ak(b,k[b],w)@Ak(a,k[a],w)
for name,orders in [('six orders',list(itertools.permutations(range(3)))),('three cyclic',[(0,1,2),(1,2,0),(2,0,1)]),('single xyz',[(0,1,2)])]:
    def g(k,target):
        U=np.eye(4)
        for o in orders: U=Us(k,o)@U
        e=np.abs(np.angle(np.linalg.eigvals(U))); return np.min(e) if target==0 else np.min(np.pi-e)
    rng=np.random.default_rng(1); best={}
    for t in (0,1):
        s=min((g(k,t),tuple(k)) for k in rng.uniform(-np.pi,np.pi,(3000,3)))
        r=min((minimize(g,np.array(s[1])+rng.normal(0,0.05,3),args=(t,),method='Nelder-Mead',options={'xatol':1e-9,'fatol':1e-12}) for _ in range(4)),key=lambda r:r.fun)
        best[t]=r.fun
    print(f"{name:13s} smallest |phase| found: {best[0]:.2e}   smallest distance from pi: {best[1]:.2e}  (light-species gap at k=0: {len(orders)*th:.3f})")
