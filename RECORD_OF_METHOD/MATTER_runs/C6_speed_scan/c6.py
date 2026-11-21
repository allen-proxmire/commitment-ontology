# Does a pattern on the flow step ever outrun straight light (speed 1)? Group speed |grad_k E| over the whole zone.
# E(k) = sqrt(sum sin^2 k_j + W^2), W = m + r sum(1 - cos k_j);  dE/dk_j = sin k_j (cos k_j + r W)/E.
import numpy as np
from scipy.optimize import minimize
def v(k,m,r):
    k=np.asarray(k,float); W=m+r*np.sum(1-np.cos(k),axis=-1); E=np.sqrt(np.sum(np.sin(k)**2,axis=-1)+W**2)
    return np.linalg.norm(np.sin(k)*(np.cos(k)+r*W[...,None]),axis=-1)/np.maximum(E,1e-300)
n=161; g=np.linspace(0,np.pi,n); K=np.stack(np.meshgrid(g,g,g,indexing='ij'),-1).reshape(-1,3)   # one octant suffices (v even in each k_j)
for r in (0.5,0.55,0.6,0.7):
    for m in (0.0,1e-6,1e-3,0.05,0.25,0.5):
        Kk=K[1:] if m==0 else K
        vv=v(Kk,m,r); i=np.argmax(vv); best=Kk[i]
        res=minimize(lambda k:-v(k,m,r),best,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-14})
        vmax=max(vv[i],-res.fun); kb=res.x if -res.fun>=vv[i] else best
        print(f"r={r}, m={m:g}: max group speed = {vmax:.9f} at k = ({kb[0]:.4f}, {kb[1]:.4f}, {kb[2]:.4f})  {'<= 1' if vmax<=1+1e-12 else 'EXCEEDS 1'}",flush=True)
