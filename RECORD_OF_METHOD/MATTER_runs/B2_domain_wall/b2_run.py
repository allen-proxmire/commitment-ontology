import numpy as np,sys; sys.path.insert(0,'.')
from dw import *
from scipy.optimize import minimize_scalar
sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]).astype(complex)
w=5*np.pi/16; th=0.5; c0=2*np.cos(w)
def Pblock(ns,eps):
    n=len(ns); P=np.zeros((2*n,2*n),complex)
    for s,v in enumerate(ns):
        u=v/np.linalg.norm(v); G=u[0]*sx+u[1]*sy+u[2]*sz
        P[2*s:2*s+2,2*s:2*s+2]=np.cos(eps)*I2-1j*np.sin(eps)*G
    return P
def mass(L,P=None):
    ths=[th]*L+[-th]*L
    def g(k):
        U=Ustrip(k,ths,w); U=U if P is None else P@U
        e=np.angle(np.linalg.eigvals(U)); e=e[np.abs(e)<0.25]   # bulk gap ~0.5 (minus eps)
        e=np.sort(e); return np.min(np.diff(e)) if len(e)>1 else 9.
    ks=np.linspace(-0.4,0.4,81); i=int(np.argmin([g(k) for k in ks]))
    r=minimize_scalar(g,bounds=(ks[i]-0.01,ks[i]+0.01),method='bounded',options={'xatol':1e-9})
    return r.fun/2, r.x
print("F1: eps=0")
Ls=[8,12,16,20]; ms=[mass(L)[0] for L in Ls]
for L,m in zip(Ls,ms): print(f"  L={L:2d} m={m:.3e}")
p=np.polyfit(Ls,np.log(ms),1); fit=np.polyval(p,Ls); R2=1-np.sum((np.log(ms)-fit)**2)/np.sum((np.log(ms)-np.mean(np.log(ms)))**2)
print(f"  slope={p[0]:.4f}/place R2={R2:.5f}  F1 {'PASS' if p[0]<-0.1 and R2>0.99 else 'FAIL'}")
print("F2: L=16"); rng=np.random.default_rng(2026); worst=0; L=16; m0=ms[2]
for eps in [0.05,0.1,0.2]:
    mc,kc=mass(L,Pblock([np.ones(3)]*(2*L),eps))
    mr=[mass(L,Pblock([np.ones(3)+rng.normal(size=3) for _ in range(2*L)],eps))[0] for _ in range(20)]
    lk=max(mc,max(mr))/eps; worst=max(worst,lk)
    print(f"  eps={eps}: coherent m={mc:.3e} (crossing k={kc:+.4f}); random max m={max(mr):.3e} median {np.median(mr):.3e}; leak={lk:.2e}")
print(f"  worst leak={worst:.2e}  F2 {'PASS' if worst<0.01 else 'FAIL'}")
print("Control: plain 1D walk, theta=0")
def U1(k,eps):
    Ax=np.diag([np.exp(-1j*k),1])@F(w)@np.diag([1,np.exp(1j*k)])@F(-w)
    u=np.ones(3)/np.sqrt(3); P=np.cos(eps)*I2-1j*np.sin(eps)*(u[0]*sx+u[1]*sy+u[2]*sz)
    return P@Ax@F(0)@Ax
for eps in [0.05,0.1,0.2]:
    r=minimize_scalar(lambda k: abs(np.diff(np.angle(np.linalg.eigvals(U1(k,eps))))[0]),bounds=(-0.5,0.5),method='bounded',options={'xatol':1e-10})
    print(f"  eps={eps}: m={r.fun/2:.4e} leak={r.fun/2/eps:.3f}  {'informative' if r.fun/2>=0.3*eps else 'UNINFORMATIVE'}")
