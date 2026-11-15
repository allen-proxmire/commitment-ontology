import numpy as np,sys; sys.path.insert(0,'.')
from dw import Ustrip,F,sx,I2
sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]).astype(complex)
w=5*np.pi/16; c0=2*np.cos(w); th=0.5; L=16; ths=[th]*L+[-th]*L; n=2*L
M=(sx+sy+sz)/np.sqrt(3)
def Ucoup(k,mu):
    U=Ustrip(k,ths,w); C=np.eye(2*n,dtype=complex)
    a,b=2*L,0
    C[a:a+2,a:a+2]=np.cos(mu)*I2; C[b:b+2,b:b+2]=np.cos(mu)*I2; C[a:a+2,b:b+2]=-1j*np.sin(mu)*M; C[b:b+2,a:a+2]=-1j*np.sin(mu)*M
    return C@U
def Eup(k,mu):   # upper sub-gap level (smallest positive quasienergy among sub-gap)
    e=np.angle(np.linalg.eigvals(Ucoup(k,mu))); e=e[(e>0)&(e<0.45)]; return e.min()
def Eup1(k,t):
    Ax=np.diag([np.exp(-1j*k),1])@F(w)@np.diag([1,np.exp(1j*k)])@F(-w); e=np.angle(np.linalg.eigvals(Ax@F(t)@Ax)); return e[e>0].min()
def kappa(Efun,par,m,k0,massless):
    ks=np.linspace(5*m,20*m,30)+k0; h=1e-4
    dv=[( (Efun(k+h,par)-Efun(k-h,par)) - (Efun(k+h,massless)-Efun(k-h,massless)) )/(2*h) for k in ks]
    X=np.vstack([np.ones_like(ks),-1/(ks-k0)**2]).T; s,A=np.linalg.lstsq(X,np.array(dv),rcond=None)[0]; return s
# calibration
ms=[0.005,0.01,0.02,0.04]; s1=[kappa(Eup1,m,m,0.0,0.0) for m in ms]
k1=np.sum(np.array(s1)*ms)/np.sum(np.array(ms)**2); R2=1-np.sum((np.array(s1)-k1*np.array(ms))**2)/np.sum((np.array(s1)-np.mean(s1))**2)
print("calibration 1D Wilson: s(m)=",[f"{x:.3e}" for x in s1],f" ds/dm={k1:.4f}  ds/dm/c0={k1/c0:.4f}  R2={R2:.4f}")
# analytic for the 1D walk: small-k expansion of E(k) numerically gives the analytic reference
def Ehigh(k,t):  # exact dispersion E(k) from eigenvalues, use symbolic-free check: excess at k>>m for the exact walk
    return Eup1(k,t)
# domain wall: find mu giving target m, crossing k*
def mass_cross(mu):
    from scipy.optimize import minimize_scalar
    g=lambda k: 2*Eup(k,mu)
    r=minimize_scalar(g,bounds=(-0.05,0.05),method='bounded',options={'xatol':1e-10}); return r.fun/2, r.x
v0=(Eup(0.05+1e-4,0)-Eup(0.05-1e-4,0))/2e-4
print(f"massless wall mode speed at k=0.05: {v0:.6f}  c0={c0:.6f}  offset={(v0-c0)/c0:+.2e}")
out=[]
for mu in [0.015,0.02,0.03,0.04]:
    m,k0=mass_cross(mu); s=kappa(Eup,mu,m,k0,0.0); out.append((m,s)); print(f"mu={mu}: m={m:.4e} k*={k0:+.2e} s={s:.4e}",flush=True)
m=np.array([o[0] for o in out]); s=np.array([o[1] for o in out]); kd=np.sum(s*m)/np.sum(m**2); R2=1-np.sum((s-kd*m)**2)/np.sum((s-np.mean(s))**2)
print(f"domain wall: ds/dm={kd:.4f}  ds/dm/c0={kd/c0:.4f}  R2={R2:.4f}   ratio to 1D calibration={kd/k1:.3f}")
