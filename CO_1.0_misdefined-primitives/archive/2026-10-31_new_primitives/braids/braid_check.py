import itertools, sys
sys.path.insert(0,'/tmp')
from braidcount import act, perm, one_cycle
def comps(n,L):
    words=list(itertools.product(range(1,n),repeat=L)); idx={w:i for i,w in enumerate(words)}
    par=list(range(len(words)))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    def u(a,b):
        a,b=f(a),f(b)
        if a!=b: par[max(a,b)]=min(a,b)
    byimg={}
    for w in words:
        byimg.setdefault(act(w,n),[]).append(idx[w]); u(idx[w], idx[w[1:]+w[:1]])
    for g in byimg.values():
        for x in g[1:]: u(g[0],x)
    roots={}
    for w in words:
        r=f(idx[w]); info=roots.setdefault(r,[set(w)==set(range(1,n)), one_cycle(perm(w,n)), True])
        for d in range(1,L):
            if L%d==0 and w==w[:d]*(L//d): info[2]=False
    t=len(roots); s=sum(all(v) for v in roots.values()); return t,s
for B,n in [(9,3),(9,4),(9,5),(11,3),(11,4),(13,3)]:
    t,s=comps(n,B-n); print(f"B={B} n={n}: classes {t}, sustaining {s}, share {s/t:.4f}")
