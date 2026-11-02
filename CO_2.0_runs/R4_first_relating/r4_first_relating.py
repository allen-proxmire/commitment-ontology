"""R4: the beginning's sentence, as a network.

Start: n0 places, all related to all (no distance yet). A conserved stock of S quanta
(hbar = 1). Each step:
  transport  - each place sends its quanta one at a time to a uniformly random
               neighbour (ratio hopping with no gradient reduces to this);
  occupancy  - a relation's occupancy is the number of quanta that crossed it this step;
  thinning   - a relation that carried nothing for W consecutive steps is not a relation;
  births     - with probability b per crossing quantum, the quantum commits mid-transit:
               a new place is inserted, splitting the relation (subdivision);
  stop       - when the mean free possibility per place drops under P_max, births stop
               (the first epoch ends); thinning continues until the graph is stable.
Variant L adds a locality proxy for the mismatch cost: a crossing quantum that would
re-relate two places does so only if they are within 2 hops (no run here; see note).

Measured on the final graph: mean degree, spectral dimension d_s from the random-walk
return probability p(t) ~ t^{-d_s/2}, and the neighbourhood-growth exponent from
N(r) ~ r^d over small r.
Registered expectation (before running): with no cost term the thinning leaves a random
sparse graph whose degree is set by the free possibility per place, and random sparse
graphs are expander-like: d_s and the growth exponent come out large, not 3. If so, the
sentence needs the mismatch cost to do real work, and the cost is what the next run
must carry.
"""
import numpy as np, json, sys
rng = np.random.default_rng(1)

def run(n0=12, S=600, P_max=8.0, b=0.02, W=5, T=400):
    N = n0
    adj = {i: set(j for j in range(n0) if j != i) for i in range(n0)}
    idle = {}          # (i,j) sorted -> idle steps
    P = np.zeros(n0) + S / n0
    quanta = [int(round(p)) for p in P]
    births_on = True
    for t in range(T):
        crossed = {}
        new_q = {i: 0 for i in adj}
        for i in list(adj):
            if not adj[i]: new_q[i] += quanta[i]; continue
            nb = list(adj[i])
            for _ in range(quanta[i]):
                j = nb[rng.integers(len(nb))]
                key = (min(i, j), max(i, j))
                crossed[key] = crossed.get(key, 0) + 1
                if births_on and rng.random() < b:
                    # subdivision: new place k between i and j, quantum stays at k
                    k = N; N += 1
                    adj[k] = {i, j}; adj[i].discard(j); adj[j].discard(i)
                    adj[i].add(k); adj[j].add(k)
                    new_q[k] = new_q.get(k, 0) + 1
                    idle.pop(key, None)
                    nb = list(adj[i]) if adj[i] else nb
                else:
                    new_q[j] = new_q.get(j, 0) + 1
        quanta = [new_q.get(i, 0) for i in range(N)]
        # thinning
        for i in list(adj):
            for j in list(adj[i]):
                if j < i: continue
                key = (i, j)
                if crossed.get(key, 0) == 0:
                    idle[key] = idle.get(key, 0) + 1
                    if idle[key] >= W:
                        adj[i].discard(j); adj[j].discard(i); idle.pop(key, None)
                else:
                    idle[key] = 0
        if births_on and S / N < P_max: births_on = False
    return adj, N

def largest_component(adj):
    seen=set(); best=set()
    for s in adj:
        if s in seen: continue
        comp=set([s]); stack=[s]
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v not in comp: comp.add(v); stack.append(v)
        seen|=comp
        if len(comp)>len(best): best=comp
    return best

def spectral_dimension(adj, nodes, steps=60, walkers=4000):
    nodes=list(nodes); idx={v:i for i,v in enumerate(nodes)}
    A=np.zeros((len(nodes),len(nodes)))
    for u in nodes:
        for v in adj[u]:
            if v in idx: A[idx[u],idx[v]]=1
    deg=A.sum(1); deg[deg==0]=1
    Pm=A/deg[:,None]
    # return probability averaged over start nodes
    pt=[]; M=np.eye(len(nodes))
    for t in range(1,steps+1):
        M=M@Pm; pt.append(np.trace(M)/len(nodes))
    pt=np.array(pt); ts=np.arange(1,steps+1)
    lo,hi=10,40
    slope=np.polyfit(np.log(ts[lo:hi]),np.log(pt[lo:hi]+1e-300),1)[0]
    return -2*slope, pt

def growth_exponent(adj, nodes, rmax=6):
    nodes=list(nodes); counts=np.zeros(rmax+1)
    for s in nodes[:200]:
        dist={s:0}; frontier=[s]
        for r in range(1,rmax+1):
            nxt=[]
            for u in frontier:
                for v in adj[u]:
                    if v not in dist: dist[v]=r; nxt.append(v)
            frontier=nxt
        for r in range(rmax+1): counts[r]+=sum(1 for d in dist.values() if d<=r)
    counts/=min(200,len(nodes))
    rs=np.arange(1,rmax+1)
    return np.polyfit(np.log(rs[1:4]),np.log(counts[2:5]),1)[0], counts

adj,N=run()
comp=largest_component(adj)
degs=[len(adj[v]) for v in comp]
ds,pt=spectral_dimension(adj,comp)
ge,counts=growth_exponent(adj,comp)
out={"places_final":N,"largest_component":len(comp),"mean_degree":float(np.mean(degs)),
     "free_per_place_final":600/N,"spectral_dimension":float(ds),"growth_exponent":float(ge),
     "N_within_r":counts.tolist()}
json.dump(out,open("r4_result.json","w"),indent=1)
for k,v in out.items(): print(f"{k:22s} {v}")
