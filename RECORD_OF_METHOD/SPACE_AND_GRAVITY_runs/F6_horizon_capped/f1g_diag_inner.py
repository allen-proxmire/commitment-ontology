import numpy as np,sys; sys.path.insert(0,'.')
exec(open('f1f_run.py').read().split('t=0; ok=True')[0])
q0=(np.abs(p.reshape(L,2))**2).sum(1); c0_=np.cumsum(q0); fr=(0.25,0.5,0.75); r0=[X[np.searchsorted(c0_,f)] for f in fr]
carry=lambda ri,tf: max(ri**1.5-1.5*np.sqrt(rs)*tf,0)**(2/3)
t=0; ok=True; absorbed=0.0
for T_ in (0.5*rs,0.3*rs):
    while carry(r0[1],t*tau)>T_:
        pn=expm_multiply(-1j*tau*H,p); p=D2*pn; t+=1
    q=(np.abs(p.reshape(L,2))**2).sum(1); inner=q[X<30].sum(); q[X<30]=0; lost=1-np.sum(np.abs(p)**2)+inner
    c=lost+np.cumsum(q)     # absorbed weight counted at the centre
    out=[]
    for f,ri in zip(fr,r0):
        meas=X[np.searchsorted(c,f)] if f>lost else 0; pr=carry(ri,t*tau); dev=(meas-pr)/(ri-pr); ok&=abs(dev)<=0.02; out.append(f"q{int(f*100)}: {meas} vs {pr:.1f} ({dev:+.4f})")
    print(f"median predicted {carry(r0[1],t*tau):.1f}, absorbed {lost:.3f}: "+"; ".join(out),flush=True)
print("F1",'PASS' if ok else 'FAIL')
