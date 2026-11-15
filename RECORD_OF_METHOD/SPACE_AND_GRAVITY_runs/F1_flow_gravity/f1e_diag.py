import numpy as np,sys; sys.path.insert(0,'.')
exec(open('f1e_run.py').read().split('targets=')[0])
t=0
for stop in (0.75*rs,0.6*rs,0.5*rs):
    while pred(t*tau)>stop: p=expm_multiply(-1j*tau*H,p); t+=1
    q=(np.abs(p.reshape(L,2))**2).sum(1); c=np.cumsum(q)
    qs=[X[np.searchsorted(c,f)] for f in (0.05,0.25,0.5,0.75,0.95)]
    # momentum content
    ph=np.fft.fft(p.reshape(L,2),axis=0); pk=(np.abs(ph)**2).sum(1); ks=2*np.pi*np.fft.fftfreq(L)
    print(f"rho_pred={pred(t*tau):.0f}: position quantiles 5/25/50/75/95% = {qs}; weight with |k|>0.5: {pk[np.abs(ks)>0.5].sum()/pk.sum():.3f}; mean |k| {np.sum(np.abs(ks)*pk)/pk.sum():.3f}",flush=True)
