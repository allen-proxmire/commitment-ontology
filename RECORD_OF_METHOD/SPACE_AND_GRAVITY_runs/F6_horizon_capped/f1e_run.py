import numpy as np,sys,scipy.sparse as sp; sys.path.insert(0,'.')
from flow1d import *
L=6000; tau=0.4; r=0.5; m=0.5; rs=400.; c0=100; x0=1200.; sig=60
X=np.arange(L)-c0; rho=np.maximum(X,6.0); b=-np.minimum(np.sqrt(rs/rho),4.0)   # drift capped at 4 (1D tick limit at m = 0.5: 6.43); F1 let it reach 8.16
S=sp.diags([np.ones(L-1)],[1],shape=(L,L),format='lil'); S[L-1,0]=1; S=S.tocsr(); sin_=(S-S.T)/(2j)
H=build(L,m,r,np.ones(L),np.ones(L))+sp.kron(0.5*(sp.diags(b)@sin_+sin_@sp.diags(b)),np.eye(2))
p=np.roll(packet(L,m,r,sig).reshape(L,2),int(c0+x0)-L//2,axis=0).reshape(-1)
pred=lambda t: (x0**1.5-1.5*np.sqrt(rs)*t)**(2/3)
targets={2*rs:None,rs:None,0.5*rs:None}; t=0; ok=True
while True:
    q=(np.abs(p.reshape(L,2))**2).sum(1); xm=np.sum(q*X); tf=t*tau; pr=pred(tf)
    for T_ in list(targets):
        if targets[T_] is None and pr<=T_:
            dev=(xm-pr)/(x0-pr); targets[T_]=dev; ok&=abs(dev)<=0.02
            print(f"rho_pred={pr:7.1f} (target {T_:.0f}): mean={xm:7.1f}, deviation {dev:+.4f} of distance fallen; |b| at mean {np.sqrt(rs/max(xm,6)):.2f}",flush=True)
    if pr<=0.5*rs: break
    p=expm_multiply(-1j*tau*H,p); t+=1
print("F1",'PASS' if ok else 'FAIL')
