"""More joins wins? Faces: loose nucleon 2 free sides + 2 flanks; ring 4 flanks, no free side.
Joins (one per pair of pieces): stack (2 sides; p-n only; full if turning alike, weak if opposed),
notch (giver's side into receiver's flank), and, option RR, flank to flank between two rings.
Holding: no split crosses a single weak join only. List best holding arrangements by join count,
split by whether the proton and neutron are fully joined."""
import sys
from itertools import combinations, product
RR=True
def arrangements(pieces):
    n=len(pieces); pairs=list(combinations(range(n),2)); opts=[]
    for i,j in pairs:
        a,b=pieces[i],pieces[j]; o=['-']
        if a!='R' and b!='R' and a[0]!=b[0]: o+=['S']
        if a!='R': o+=['i>j']
        if b!='R': o+=['j>i']
        if a=='R' and b=='R' and RR: o+=['RR']
        opts.append(o)
    out=[]
    for ch in product(*opts):
        sides=[0]*n; fl=[0]*n; J={}
        for (i,j),c in zip(pairs,ch):
            if c=='-': continue
            if c=='S':
                sides[i]+=1; sides[j]+=1
                J[(i,j)]='F' if pieces[i][1]==pieces[j][1] else 'W'
            elif c=='RR': fl[i]+=1; fl[j]+=1; J[(i,j)]='W'
            else:
                g,r=(i,j) if c=='i>j' else (j,i); sides[g]+=1; fl[r]+=1; J[(i,j)]='W'
        if any(pieces[i]!='R' and sides[i]>2 for i in range(n)): continue
        if any(fl[i]>(4 if pieces[i]=='R' else 2) for i in range(n)): continue
        ok=True
        for k in range(1,n//2+1):
            for part in combinations(range(n),k):
                cr=[v for (i,j),v in J.items() if (i in part)!=(j in part)]
                if 'F' not in cr and len(cr)<2: ok=False;break
            if not ok: break
        if ok: out.append((list(J.values()).count('F'),list(J.values()).count('W')))
    return out
P=lambda s:('p',s); N=lambda s:('n',s)
cases={"H-2":[P(1),N(1)],"He-5":['R',N(1)],"He-6":['R',N(1),N(-1)],"Li-6 alike":['R',P(1),N(1)],"Li-6 opposed":['R',P(1),N(-1)],
"Li-7":['R',P(1),N(1),N(-1)],"Be-8":['R','R'],"Be-9":['R','R',N(1)],"B-10 alike":['R','R',P(1),N(1)],"B-10 opposed":['R','R',P(1),N(-1)],
"B-11":['R','R',P(1),N(1),N(-1)],"C-12":['R','R','R'],"C-13":['R','R','R',N(1)]}
for rr in (False,True):
    RR=rr; print("\nring-to-ring join:",rr)
    for k,v in cases.items():
        a=arrangements(v)
        if not a: print(f"  {k:13} does not hold"); continue
        withF=max((w for f,w in a if f),default=None); noF=max((w for f,w in a if not f),default=None)
        print(f"  {k:13} holds.  with the full join: {'1 full + %d weak'%withF if withF is not None else 'none'};  without: {'%d weak'%noF if noF is not None else 'none'}")
