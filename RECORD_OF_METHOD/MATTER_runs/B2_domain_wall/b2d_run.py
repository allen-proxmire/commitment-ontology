import numpy as np,sys
from scipy.optimize import minimize_scalar
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]).astype(complex); I2=np.eye(2)
R=np.cos(np.pi/4)*I2-1j*np.sin(np.pi/4)*sx; Rd=R.conj().T
w=5*np.pi/16; th=0.5; Lc=8; eps=0.2
def F(a): return np.cos(a)*I2-1j*np.sin(a)*sx
def app(M,p): return np.einsum('ij,xsjd->xsid',M,p) if M.ndim==2 else np.einsum('xsij,xsjd->xsid',M,p)
def rx(q,d,phi):
    q=np.roll(q,d,0)
    if d==1: q[0]*=np.exp(1j*phi)
    else: q[-1]*=np.exp(-1j*phi)
    return q
def Ax(p,phi): p=app(F(-w),p); p[:,:,1]=rx(p[:,:,1],-1,phi); p=app(F(w),p); p[:,:,0]=rx(p[:,:,0],1,phi); return p
def As(p): p=app(Rd,p); p=app(F(-w),p); p[:,:,1]=np.roll(p[:,:,1],-1,1); p=app(F(w),p); p[:,:,0]=np.roll(p[:,:,0],1,1); return app(R,p)
def U(q,L,P,ctrl):
    n=2*L; D=2*Lc*n; p=np.eye(D,dtype=complex).reshape(Lc,n,2,D); phi=q*Lc
    Ft=np.array([F(t) for t in [th]*L+[-th]*L])[None]*np.ones((Lc,1,1,1))
    p=Ax(p,phi); p=As(p); p=app(Ft,p); p=As(p); p=Ax(p,phi); p=app(P,p)
    if ctrl:
        a=p[:,L].copy(); b=p[:,0].copy(); p[:,L]=np.cos(eps)*a-1j*np.sin(eps)*b; p[:,0]=np.cos(eps)*b-1j*np.sin(eps)*a
    return p.reshape(D,D)
def Pdraw(L,seed):
    rng=np.random.default_rng(seed); v=np.ones(3)+rng.normal(size=(Lc,2*L,3)); u=v/np.linalg.norm(v,axis=-1,keepdims=True)
    G=u[...,0,None,None]*sx+u[...,1,None,None]*sy+u[...,2,None,None]*sz; return np.cos(eps)*I2-1j*np.sin(eps)*G
def analyse(L,seed,ctrl=False):
    P=Pdraw(L,seed); n=2*L
    half2=np.zeros(n,bool); half2[[s%n for s in range(-L//2,L//2)]]=True
    def sub(q):
        ev,V=np.linalg.eig(U(q,L,P,ctrl)); e=np.angle(ev); i=np.where(np.abs(e)<0.25)[0]; o=np.argsort(e[i]); i=i[o]
        f=np.array([np.sum(np.abs(V[:,j].reshape(Lc,n,2)[:,half2])**2)/np.sum(np.abs(V[:,j])**2) for j in i])
        return e[i],f
    qs=np.linspace(-np.pi/Lc,np.pi/Lc,241); data=[sub(q) for q in qs]
    best=[]; 
    for idx in range(1,len(qs)-1):
        for j in range(len(data[idx][0])-1):
            g=lambda d: d[0][j+1]-d[0][j] if len(d[0])>j+1 else 9
            if g(data[idx])<g(data[idx-1]) and g(data[idx])<=g(data[idx+1]):
                def gq(q):
                    e,f=sub(q); return e[j+1]-e[j] if len(e)>j+1 else 9
                r=minimize_scalar(gq,bounds=(qs[idx-1],qs[idx+1]),method='bounded',options={'xatol':1e-10})
                e,f=sub(r.x)
                if len(e)>j+1 and 0.3<f[j]<0.7 and 0.3<f[j+1]<0.7: best.append(r.fun/2)
    return (max(best) if best else None), len(best)
res={}
for L in [8,12,16]:
    m,c=analyse(L,11); res[L]=m; print(f"(a) L={L:2d} m={m} crossings={c}",flush=True)
ms=[analyse(16,s)[0] for s in [12,13,14]]; print("(b) L=16 seeds 12-14:",ms)
mc,cc=analyse(16,11,True); print(f"control L=16 m={mc} crossings={cc}")
allm=[res[16]]+ms
f2=all(x is not None for x in [res[8],res[12],res[16]]+ms)
f1=f2 and res[16]<=res[8]/10 and max(allm)<=1e-3
print("F1",'PASS' if f1 else 'FAIL',"F2",'PASS' if f2 else 'FAIL',"control",'informative' if (mc or 0)>=0.03 else 'UNINFORMATIVE')
