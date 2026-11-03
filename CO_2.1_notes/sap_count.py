"""Closed walks on the cubic lattice, up to the lattice's symmetries (48 rotations and
reflections, plus translation), by length. Self-avoiding polygons only: a loop does not
revisit a place within one repeat. A hand count done by machine; L = 4..10."""
import itertools, numpy as np
dirs=[np.array(v) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
# 48 signed permutation matrices
syms=[]
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3),int)
        for i,p in enumerate(perm): M[i,p]=signs[i]
        syms.append(M)
def canon(pts):
    best=None
    for M in syms:
        q=[tuple(M@p) for p in pts]
        # all rotations of the cycle and both directions, translated to lexicographic min
        n=len(q)
        for start in range(n):
            for d in (1,-1):
                seq=[q[(start+d*k)%n] for k in range(n)]
                base=np.array(seq[0]); seq=tuple(tuple(np.array(s)-base) for s in seq)
                if best is None or seq<best: best=seq
    return best
def polygons(L):
    found=set()
    def rec(path,visited):
        if len(path)==L:
            if np.array_equal(path[-1]+dirs[0],path[0]) or any(np.array_equal(path[-1]+d,path[0]) for d in dirs):
                if any(np.array_equal(path[-1]+d,path[0]) for d in dirs):
                    found.add(canon(path))
            return
        for d in dirs:
            nxt=path[-1]+d
            if tuple(nxt) in visited: continue
            # prune: must be able to return
            if np.abs(nxt).sum()>L-len(path): continue
            rec(path+[nxt],visited|{tuple(nxt)})
    rec([np.zeros(3,int)],{(0,0,0)})
    return found
for L in [4,6,8,10]:
    P=polygons(L)
    planar=sum(1 for p in P if any(all(pt[ax]==0 for pt in p) for ax in range(3)))
    print(f"L={L}: {len(P)} shapes ({planar} planar, {len(P)-planar} non-planar)")
