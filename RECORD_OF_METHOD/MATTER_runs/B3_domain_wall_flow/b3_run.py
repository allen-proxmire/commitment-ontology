import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]).astype(complex); I2=np.eye(2)
tau=0.4; r=0.5; M=0.5
def Hstrip(k,L):
    n=2*L; S=np.roll(np.eye(n),1,axis=0)          # (S v)_s = v_{s-1}... ring shift
    sins=(S-S.T)/(2j); omcs=np.eye(n)-(S+S.T)/2; ms=np.diag([M]*L+[-M]*L)
    return np.kron(np.eye(n),np.sin(k)*sx)+np.kron(sins,sy)+np.kron(ms+r*(1-np.cos(k))*np.eye(n)+r*omcs,sz)
def Pblock(ns,eps):
    n=len(ns); P=np.zeros((2*n,2*n),complex)
    for s_,v in enumerate(ns):
        u=v/np.linalg.norm(v); G=u[0]*sx+u[1]*sy+u[2]*sz; P[2*s_:2*s_+2,2*s_:2*s_+2]=np.cos(eps)*I2-1j*np.sin(eps)*G
    return P
def mass(L,P=None):
    def g(k):
        U=expm(-1j*tau*Hstrip(k,L)); U=U if P is None else P@U
        e=np.sort(np.angle(np.linalg.eigvals(U))); e=e[np.abs(e)<0.1]
        return np.min(np.diff(e)) if len(e)>1 else 9.
    ks=np.linspace(-0.3,0.3,61); i=int(np.argmin([g(k) for k in ks]))
    r_=minimize_scalar(g,bounds=(ks[i]-0.01,ks[i]+0.01),method='bounded',options={'xatol':1e-10}); return r_.fun/2
def line(Ls,ms):
    p=np.polyfit(Ls,np.log(ms),1); f=np.polyval(p,Ls); R2=1-np.sum((np.log(ms)-f)**2)/np.sum((np.log(ms)-np.mean(np.log(ms)))**2); return p[0],R2
Ls=[8,12,16,20,24]
m0=[mass(L) for L in Ls]; s0,R0=line(Ls,m0); print("eps=0: m(L) =",[f"{x:.2e}" for x in m0],f"slope {s0:.3f} R2 {R0:.4f}",flush=True)
f1=s0<-0.1 and R0>0.98
# control
u=np.ones(3)/np.sqrt(3); Pc=np.cos(0.2)*I2-1j*np.sin(0.2)*(u[0]*sx+u[1]*sy+u[2]*sz)
def g1(k):
    h=np.sin(k)*sx+r*(1-np.cos(k))*sz; e=np.angle(np.linalg.eigvals(Pc@expm(-1j*tau*h))); return abs(e[0]-e[1])
mc=minimize_scalar(g1,bounds=(-0.5,0.5),method='bounded',options={'xatol':1e-12}).fun/2
print(f"control (plain flow, m=0, eps=0.2): mass per tick {mc:.4e}  ({'informative' if mc>=0.3*0.2*tau else 'UNINFORMATIVE'})",flush=True)
rng=np.random.default_rng(77); cases=[('coherent',[np.ones(3)]*48)]+[(f'draw{i}',[np.ones(3)+rng.normal(size=3) for _ in range(48)]) for i in range(5)]
f2=True
for name,ns in cases:
    ms=[mass(L,Pblock(ns[:2*L],0.2)) for L in Ls]; sl,R2=line(Ls,ms); ok=sl<-0.1 and R2>0.98 and ms[-1]<=0.01*mc; f2&=ok
    print(f"{name:9s} m(L)="+" ".join(f"{x:.2e}" for x in ms)+f" slope {sl:.3f} R2 {R2:.4f} {'ok' if ok else 'FAIL'}",flush=True)
print("F1",'PASS' if f1 else 'FAIL',"F2",'PASS' if f2 else 'FAIL')
