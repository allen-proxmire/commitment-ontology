"""R12: R5-B formation with parallel channels per pair. See REGISTRATION.md."""
import numpy as np, json
from collections import defaultdict
def run(n0=300,q=6,m0=4,W=4,T=120,seed=3):
    rng=np.random.default_rng(seed)
    # channels: id -> (i,j); per-place adjacency: place -> set of channel ids
    ch=[]; adj=defaultdict(set)
    for i in range(n0):
        for j in range(i+1,n0):
            for c in range(m0):
                cid=len(ch); ch.append((i,j)); adj[i].add(cid); adj[j].add(cid)
    alive=np.ones(len(ch),bool); idle=np.zeros(len(ch),int)
    other=lambda cid,i: ch[cid][1] if ch[cid][0]==i else ch[cid][0]
    quanta=[(i,-1) for i in range(n0) for _ in range(q)]
    partner={}; paired_at=defaultdict(set)
    for t in range(T):
        crossed=np.zeros(len(ch),bool); nq=[]
        for (i,frm) in quanta:
            nb=[c for c in adj[i] if alive[c]]
            if not nb: nq.append((i,-1)); continue
            c=None
            if frm>=0 and alive[frm]:
                key=(i,frm)
                if key in partner and alive[partner[key]]: c=partner[key]
                else:
                    cands=[x for x in nb if x!=frm and x not in paired_at[i]]
                    if not cands: cands=[x for x in nb if x!=frm] or nb
                    c=cands[rng.integers(len(cands))]
                    partner[(i,frm)]=c; partner[(i,c)]=frm; paired_at[i].update((frm,c))
            if c is None: c=nb[rng.integers(len(nb))]
            crossed[c]=True; nq.append((other(c,i),c))
        quanta=nq
        idle[~crossed&alive]+=1; idle[crossed]=0
        alive[alive&(idle>=W)]=False
    # multiplicity per surviving pair
    mult=defaultdict(int)
    for cid in np.flatnonzero(alive): mult[ch[cid]]+=1
    ks=np.array(list(mult.values()))
    deg=defaultdict(int)
    for (i,j) in mult: deg[i]+=1; deg[j]+=1   # distinct neighbours
    return ks, np.array(list(deg.values()))
out={}
for q in (6,8,12):
    for m0 in (1,4):
        ks,deg=run(q=q,m0=m0)
        hist={int(k):int((ks==k).sum()) for k in np.unique(ks)}
        r={'pairs':int(len(ks)),'mean_k':float(ks.mean()),'frac_k_ge2':float((ks>=2).mean()),'frac_k_ge3':float((ks>=3).mean()),'k_hist':hist,'mean_distinct_neighbours':float(deg.mean())}
        out[f'q{q}_m0{m0}']=r; print(f"q={q} m0={m0}:",r,flush=True)
json.dump(out,open('r12_result.json','w'),indent=1)
