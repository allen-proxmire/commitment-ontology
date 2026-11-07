"""R13: a renewing pattern (M quanta hopping out and back at place 0) in the R5-B formation model."""
import numpy as np, json
from collections import deque
def run(n0=300,q=6,M=0,W=4,T=120,seed=3):
    rng=np.random.default_rng(seed)
    alive=np.ones((n0,n0),bool); np.fill_diagonal(alive,False); idle=np.zeros((n0,n0),int)
    quanta=[(i,-1) for i in range(n0) for _ in range(q)]
    patt=[(0,-1)]*M   # (current place, home-or-away flag: -1 at home)
    partner={}
    for t in range(T):
        crossed=np.zeros((n0,n0),bool); nq=[]
        for (i,frm) in quanta:
            nb=np.flatnonzero(alive[i])
            if len(nb)==0: nq.append((i,-1)); continue
            j=None
            if frm>=0 and alive[i,frm]:
                key=(i,frm)
                if key in partner and alive[i,partner[key]]: j=partner[key]
                else:
                    paired={partner[k] for k in partner if k[0]==i}|{k[1] for k in partner if k[0]==i}
                    cands=[x for x in nb if x!=frm and x not in paired]
                    if not cands: cands=[x for x in nb if x!=frm] or list(nb)
                    j=int(cands[rng.integers(len(cands))]); partner[(i,frm)]=j; partner[(i,j)]=frm
            if j is None: j=int(nb[rng.integers(len(nb))])
            crossed[i,j]=crossed[j,i]=True; nq.append((j,i))
        quanta=nq
        # pattern quanta: out from home along a random alive relation, then back
        npatt=[]
        for (p,flag) in patt:
            if flag==-1:
                nb=np.flatnonzero(alive[0])
                if len(nb)==0: npatt.append((0,-1)); continue
                j=int(nb[rng.integers(len(nb))]); crossed[0,j]=crossed[j,0]=True; npatt.append((j,0))
            else:
                if alive[p,0]: crossed[p,0]=crossed[0,p]=True
                npatt.append((0,-1))
        patt=npatt
        idle[~crossed&alive]+=1; idle[crossed]=0
        alive[alive&(idle>=W)]=False
    # distances from place 0
    dist=-np.ones(n0,int); dist[0]=0; dq=deque([0])
    while dq:
        u=dq.popleft()
        for v in np.flatnonzero(alive[u]):
            if dist[v]<0: dist[v]=dist[u]+1; dq.append(v)
    deg=alive.sum(1)
    out={'total_relations':int(alive.sum()//2),'deg_by_distance':{}}
    for d in range(4):
        sel=dist==d
        out['deg_by_distance'][d]={'n_places':int(sel.sum()),'mean_degree':float(deg[sel].mean()) if sel.any() else None}
    out['mean_degree_all_alive']=float(deg[deg>0].mean())
    return out
res={}
for M in (0,6,24,96):
    r=run(M=M); res[f'M{M}']=r
    print(f"M={M}: total rel={r['total_relations']}  deg d0={r['deg_by_distance'][0]['mean_degree']}  d1={r['deg_by_distance'][1]['mean_degree']} (n={r['deg_by_distance'][1]['n_places']})  d2={r['deg_by_distance'][2]['mean_degree']} (n={r['deg_by_distance'][2]['n_places']})  d3={r['deg_by_distance'][3]['mean_degree']} (n={r['deg_by_distance'][3]['n_places']})  all={r['mean_degree_all_alive']:.2f}",flush=True)
json.dump(res,open('r13_result.json','w'),indent=1)
