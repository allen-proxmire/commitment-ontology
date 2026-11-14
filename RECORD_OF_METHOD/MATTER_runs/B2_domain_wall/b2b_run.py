import numpy as np,sys; sys.path.insert(0,'.')
exec(open('b2_run.py').read().split('print("F1: eps=0")')[0])
rng=np.random.default_rng(77); eps=0.2; Ls=[8,12,16,20,24]; ok=True
cases=[('coherent',None)]+[(f'draw{i}',[np.ones(3)+rng.normal(size=3) for _ in range(2*24)]) for i in range(5)]
for name,ns in cases:
    ms=[]
    for L in Ls:
        nn=[np.ones(3)]*(2*L) if ns is None else ns[:2*L]
        ms.append(mass(L,Pblock(nn,eps))[0])
    p=np.polyfit(Ls,np.log(ms),1); fit=np.polyval(p,Ls); R2=1-np.sum((np.log(ms)-fit)**2)/np.sum((np.log(ms)-np.mean(np.log(ms)))**2)
    f1=p[0]<-0.1 and R2>0.98; f2=ms[-1]<=2e-4; ok&=f1 and f2
    print(f"{name:9s} m(L)="+" ".join(f"{m:.2e}" for m in ms)+f"  slope={p[0]:.3f} R2={R2:.4f}  F1 {'PASS' if f1 else 'FAIL'} F2 {'PASS' if f2 else 'FAIL'}")
print("B2b", "PASS" if ok else "FAIL")
