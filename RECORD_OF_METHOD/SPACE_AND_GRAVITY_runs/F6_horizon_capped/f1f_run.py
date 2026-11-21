import numpy as np,sys; sys.path.insert(0,'.')
exec(open('f1e_run.py').read().split('targets=')[0])
damp=np.ones(L); z=X<30; damp[z]=np.exp(-0.05*(1-np.maximum(X[z],0)/30)**2); damp[X<0]=np.exp(-0.05); D2=np.repeat(damp,2)
t=0; ok=True
for T_ in (2*rs,rs,0.5*rs,0.3*rs):
    while pred(t*tau)>T_: p=D2*expm_multiply(-1j*tau*H,p); t+=1
    q=(np.abs(p.reshape(L,2))**2).sum(1); q[X<30]=0; c=np.cumsum(q)/q.sum(); med=X[np.searchsorted(c,0.5)]; pr=pred(t*tau)
    dev=(med-pr)/(x0-pr); ok&=abs(dev)<=0.02
    print(f"rho_pred={pr:6.1f}: median={med}, deviation {dev:+.4f} of distance fallen; weight remaining {np.sum(np.abs(p)**2):.3f}; |b| at prediction {np.sqrt(rs/pr):.2f}",flush=True)
print("F1",'PASS' if ok else 'FAIL')
