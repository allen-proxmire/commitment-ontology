import numpy as np,sys; sys.path.insert(0,'.')
exec(open('b2_run.py').read().split('print("F1: eps=0")')[0])
def speeds(L,P):
    k0=mass(L,P)[1]; n=2*L; half2=np.zeros(n,bool); half2[[s%n for s in range(-L//2,L//2)]]=True; ths=[th]*L+[-th]*L
    out={}
    for k in (k0+0.04,k0+0.12):
        ev,V=np.linalg.eig(P@Ustrip(k,ths,w)); e=np.angle(ev); idx=np.where(np.abs(e)<0.3)[0]
        for j in idx:
            f=np.sum(np.abs(V[:,j].reshape(n,2)[half2])**2); out.setdefault((k, 2 if f>0.5 else 1),e[j])
    ks=sorted({k for k,_ in out}); return [abs(out[(ks[1],i)]-out[(ks[0],i)])/0.08 for i in (1,2)]
L_list=[8,16,24]
print("coherent (uniform in s):")
for n0 in [(1,1,1),(1,0,0),(0,1,0),(0,0,1)]:
    worst=0
    for eps in [0.05,0.1,0.2]:
        for L in L_list:
            v=speeds(L,Pblock([np.array(n0,float)]*(2*L),eps)); worst=max(worst,abs(v[0]-v[1]))
            if eps==0.2 and L==16: vv=v
    print(f"  n0={n0}: max|v1-v2|={worst:.2e}   (eps=0.2,L=16: v1={vv[0]:.5f} v2={vv[1]:.5f})")
print("random:")
rng=np.random.default_rng(21); draws=[[np.ones(3)+rng.normal(size=3) for _ in range(48)] for _ in range(5)]
med={}
for eps in [0.05,0.1,0.2]:
    for L in L_list:
        d=[abs(np.subtract(*speeds(L,Pblock(dr[:2*L],eps)))) for dr in draws]; med[(eps,L)]=np.median(d)
        print(f"  eps={eps} L={L:2d} |v1-v2| median={np.median(d):.2e} max={max(d):.2e}",flush=True)
r=med[(0.2,24)]/med[(0.2,8)]
print(f"ratio L24/L8 at eps=0.2: {r:.3f} ->", 'NOT PROTECTED' if r>=0.5 else ('PROTECTED' if r<=0.1 else 'INCONCLUSIVE'))
