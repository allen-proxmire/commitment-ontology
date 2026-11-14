import numpy as np,sys; sys.path.insert(0,'.')
from dw import Ustrip, F as F2
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]).astype(complex); I2=np.eye(2)
R=np.cos(np.pi/4)*I2-1j*np.sin(np.pi/4)*sx; Rd=R.conj().T
w=5*np.pi/16; th=0.5; Lx=400; T=300; eps=0.2; Om=0.05
def app(M,p): return np.einsum('ij,jxs->ixs',M,p) if M.ndim==2 else np.einsum('xsij,jxs->ixs',M,p)
def Fop(p,a): c=np.cos(a); s=np.sin(a); return np.array([c*p[0]-1j*s*p[1], c*p[1]-1j*s*p[0]])
def Ax(p): p=Fop(p,-w); p[1]=np.roll(p[1],-1,0); p=Fop(p,w); p[0]=np.roll(p[0],1,0); return p
def As(p): p=app(Rd,p); p=Fop(p,-w); p[1]=np.roll(p[1],-1,1); p=Fop(p,w); p[0]=np.roll(p[0],1,1); return app(R,p)
def step(p,ths): return Ax(As(Fop(As(Ax(p)),ths[None,:]),))
def packet(L):
    n=2*L; ths=[th]*L+[-th]*L; ks=2*np.pi*np.fft.fftfreq(Lx); ph=np.zeros((2,Lx,n),complex)
    near1=np.zeros(n,bool); near1[L-3:L+3]=True
    for i,k in enumerate(ks):
        amp=np.exp(-((((k+np.pi)%(2*np.pi)-np.pi)-0.05)*40)**2/2)
        if amp<1e-8: continue
        ev,V=np.linalg.eig(Ustrip(k,ths,w)); e=np.angle(ev); idx=np.where(np.abs(e)<0.25)[0]
        wts=[np.sum(np.abs(V[:,j].reshape(n,2)[near1])**2) for j in idx]; v=V[:,idx[int(np.argmax(wts))]].reshape(n,2).T
        ph[:,i,:]=amp*v
    p=np.fft.ifft(ph,axis=1); return p/np.linalg.norm(p)
def gens(L,rng):
    n=2*L; v=np.ones(3)+rng.normal(size=(Lx,n,3)); u=v/np.linalg.norm(v,axis=-1,keepdims=True)
    return u[...,0,None,None]*sx+u[...,1,None,None]*sy+u[...,2,None,None]*sz, rng.uniform(0,2*np.pi,(Lx,n))
def run(L,case):
    rng=np.random.default_rng(5); n=2*L; ths=np.array([th]*L+[-th]*L); G,phi=gens(L,rng)
    p=packet(L); w2=np.zeros(n,bool); w2[[s%n for s in range(-3,4)]]=True
    P=lambda q: np.sum(np.abs(q[:,:,w2])**2)
    P0=P(p); mx=P0
    for t in range(T):
        p=step(p,ths)
        if case in 'ab':
            e=eps*np.ones((Lx,n)) if case=='a' else eps*np.cos(Om*t+phi)
            M=np.cos(e)[...,None,None]*I2-1j*np.sin(e)[...,None,None]*G; p=app(M,p)
        else:
            a=p[:,:,L].copy(); b=p[:,:,0].copy(); p[:,:,L]=np.cos(eps)*a-1j*np.sin(eps)*b; p[:,:,0]=np.cos(eps)*b-1j*np.sin(eps)*a
        mx=max(mx,P(p))
    return mx-P0, P0
res={}
for case in 'abc':
    for L in [8,12,16]:
        d,P0=run(L,case); res[(case,L)]=d; print(f"case {case} L={L:2d}  dP2={d:.3e}  (P2 at t=0 {P0:.1e})",flush=True)
ok=True
for c in 'ab':
    f1=res[(c,16)]<=1e-3; f2=res[(c,16)]<=res[(c,8)]/10; ok&=f1 and f2
    print(f"case {c}: F1 {'PASS' if f1 else 'FAIL'}  F2 {'PASS' if f2 else 'FAIL'}")
print("control", "informative" if res[('c',16)]>=0.1 else "UNINFORMATIVE"); print("B2c","PASS" if ok and res[('c',16)]>=0.1 else "FAIL/UNINFORMATIVE")
