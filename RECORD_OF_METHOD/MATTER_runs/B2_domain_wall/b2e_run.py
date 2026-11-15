import numpy as np
from scipy.optimize import minimize_scalar
src=open('b2d_run.py').read().split('def analyse')[0].replace('Lc=8','Lc=32')
exec(src)
CTRL=lambda: None
def Uc(q,L,P,ctrl):
    if not ctrl: return U(q,L,P,False)
    n=2*L; D=2*Lc*n; p=np.eye(D,dtype=complex).reshape(Lc,n,2,D); phi=q*Lc
    Ft=np.array([F(t) for t in [th]*L+[-th]*L])[None]*np.ones((Lc,1,1,1))
    p=Ax(p,phi); p=As(p); p=app(Ft,p); p=As(p); p=Ax(p,phi); p=app(P,p)
    M=(sx+sy+sz)/np.sqrt(3); a=p[:,L].copy(); b=p[:,0].copy()
    p[:,L]=np.cos(eps)*a-1j*np.sin(eps)*np.einsum('ij,xjd->xid',M,b); p[:,0]=np.cos(eps)*b-1j*np.sin(eps)*np.einsum('ij,xjd->xid',M,a)
    return p.reshape(D,D)
def analyse(L,seed,ctrl=False):
    P=Pdraw(L,seed); n=2*L; half2=np.zeros(n,bool); half2[[s%n for s in range(-L//2,L//2)]]=True
    def near(q,vecs=False):   # eigenpairs of U nearest quasienergy 0 by shift-invert (same result as full eig, faster)
        from scipy.linalg import lu_factor, lu_solve
        from scipy.sparse.linalg import eigs, LinearOperator
        Um=Uc(q,L,P,ctrl); D=Um.shape[0]; lu=lu_factor(Um-np.eye(D))
        op=LinearOperator((D,D),matvec=lambda v: lu_solve(lu,v),dtype=complex)
        mu,V=eigs(op,k=24,which='LM',tol=1e-12); ev=1+1/mu; e=np.angle(ev)
        return (e,V) if vecs else e
    def lev(q):
        e=near(q); return np.sort(e[np.abs(e)<0.25])
    qs=np.linspace(-np.pi/Lc,np.pi/Lc,81); E=[lev(q) for q in qs]; gaps=[]
    for i in range(1,len(qs)-1):
        for j in range(min(len(E[i-1]),len(E[i]),len(E[i+1]))-1):
            g=[E[i+d][j+1]-E[i+d][j] for d in (-1,0,1)]
            if g[1]<g[0] and g[1]<=g[2]:
                def gq(q):
                    e=lev(q); return e[j+1]-e[j] if len(e)>j+1 else 9
                r=minimize_scalar(gq,bounds=(qs[i-1],qs[i+1]),method='bounded',options={'xatol':1e-10})
                e,V=near(r.x,True); idx=np.where(np.abs(e)<0.25)[0]; idx=idx[np.argsort(e[idx])]
                if len(idx)<=j+1: continue
                f=[np.sum(np.abs(V[:,k].reshape(Lc,n,2)[:,half2])**2) for k in idx[j:j+2]]
                if all(0.3<x<0.7 for x in f): gaps.append((r.fun/2, float(np.mean(e[idx[j:j+2]]))))
    return gaps
res={}
for L in [8,12,16]:
    g=analyse(L,11); res[L]=g; print(f"L={L:2d} crossings={len(g)}  m at (E): "+", ".join(f"{m:.2e}({E:+.3f})" for m,E in sorted(g,key=lambda t:t[1])),flush=True)
gc=analyse(16,11,True); print("control L=16:", ", ".join(f"{m:.2e}({E:+.3f})" for m,E in gc),flush=True)
mx={L:max(m for m,_ in res[L]) if res[L] else None for L in res}
f2=all(len(res[L])>=3 for L in res); f1=f2 and mx[16]<=mx[8]/10 and mx[16]<=1e-3
mc=max([m for m,_ in gc],default=0)
print("F1",'PASS' if f1 else 'FAIL',"F2",'PASS' if f2 else 'FAIL',"control",'informative' if mc>=0.03 else 'UNINFORMATIVE')
