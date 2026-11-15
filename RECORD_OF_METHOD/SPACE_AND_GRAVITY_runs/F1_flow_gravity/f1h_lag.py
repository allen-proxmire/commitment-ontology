import numpy as np,sys; sys.path.insert(0,'.')
exec(open('f1f_run.py').read().split('t=0; ok=True')[0])
# Lag poke: does the median's lag behind its carried path match the integrated shortfall of the shift's carrying speed, b*(1 - <cos k>)?
q0=(np.abs(p.reshape(L,2))**2).sum(1); r0=X[np.searchsorted(np.cumsum(q0),0.5)]
carry=lambda ri,tf: max(ri**1.5-1.5*np.sqrt(rs)*tf,0)**(2/3)
ks=2*np.pi*np.fft.fftfreq(L); t=0; lagpred=0.0
for T_ in (rs,0.75*rs,0.5*rs,0.3*rs):
    while carry(r0,t*tau)>T_:
        ph=np.fft.fft(p.reshape(L,2),axis=0); pk=(np.abs(ph)**2).sum(1); cosk=np.sum(np.cos(ks)*pk)/pk.sum()
        xm=max(carry(r0,t*tau),6.0); lagpred+=tau*np.sqrt(rs/xm)*(1-cosk)    # carrying-speed shortfall integrated along the path
        p=D2*expm_multiply(-1j*tau*H,p); t+=1
    q=(np.abs(p.reshape(L,2))**2).sum(1); q[X<30]=0; lost=1-np.sum(np.abs(p)**2); c=lost+np.cumsum(q)
    med=X[np.searchsorted(c,0.5)]; pr=carry(r0,t*tau)
    print(f"median predicted {pr:6.1f}: measured lag {med-pr:+6.1f} places; integrated b(1-<cos k>) {lagpred:6.1f} places; <1-cos k> now {1-cosk:.4f}",flush=True)
