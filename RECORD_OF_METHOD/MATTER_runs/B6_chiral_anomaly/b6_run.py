import numpy as np,sys; sys.path.insert(0,'../B5_wall_charge')
src=open('../B5_wall_charge/b5_run.py').read().split('ok=True')[0]; exec(src)
def wall_of(v):
    u=np.abs(v.reshape(Lx,n,4))**2; w=u.sum((0,2)); a=w[L-4:L+4].sum(); b=w[:4].sum()+w[-4:].sum()
    return 'A' if a>0.6 else ('B' if b>0.6 else 'bulk')
kzs=-np.pi+(np.arange(64)+0.5)*2*np.pi/64; ok=True
for ky in (0.0,0.7):
    tr={'A':[], 'B':[]}; stray=[]
    for kz in kzs:
        e,v=eigsh(H(ky,kz),k=6,sigma=1e-4,which='LM')
        for i in range(len(e)):
            if abs(e[i])<0.15:
                w=wall_of(v[:,i])
                if w in tr: tr[w].append((kz,e[i]))
                else: stray.append((kz,e[i]))
    res={}
    for w in 'AB':
        pts=sorted(tr[w]); cross=[]
        for (k1,e1),(k2,e2) in zip(pts,pts[1:]):
            if abs(k2-k1)<0.11 and np.sign(e1)!=np.sign(e2): cross.append((0.5*(k1+k2),np.sign(e2-e1)))
        res[w]=cross; kr=(min(p[0] for p in pts),max(p[0] for p in pts)) if pts else None
        print(f"ky={ky}, wall {w}: {len(pts)} low points, k_z range {kr[0]:+.3f}..{kr[1]:+.3f}; zero crossings {[(round(c,3),'up' if s>0 else 'down') for c,s in cross]}",flush=True)
    print(f"ky={ky}: stray low states (bulk, |E|<0.15): {len(stray)}",flush=True)
    ok&=len(res['A'])==1 and len(res['B'])==1 and res['A'][0][1]!=res['B'][0][1] and len(stray)==0
print("B6",'PASS' if ok else 'FAIL')
