"""Triangles and gears, two trial rules (desk check).
Pieces: closed rings (helium-4) and loose nucleons (kind, turning).
Rule 3: at most one loose nucleon of each (kind, turning). Four loose = a ring.
Joins: loose p and n turning alike -> full. Any other two pieces -> one weak join.
Trial rule A (two together): a body holds if no split of its pieces into two
  parts crosses only a single weak join.
Trial rule B (rolling): a loose nucleon beside a ring circles it one unit, in
  the sense of its own turning. Spin = |sum of (circling + turning)|.
"""
from itertools import combinations, product
OBS = {  # (Z,N): (name, bound?, spin)
 (1,1):("H-2",True,1),(2,0):("He-2",False,None),(0,2):("2n",False,None),
 (2,1):("He-3",True,.5),(1,2):("H-3",True,.5),(2,2):("He-4",True,0),
 (2,3):("He-5",False,1.5),(3,2):("Li-5",False,1.5),(2,4):("He-6",True,0),
 (3,3):("Li-6",True,1),(4,2):("Be-6",False,0),(3,4):("Li-7",True,1.5),
 (4,3):("Be-7",True,1.5),(4,4):("Be-8",False,0),(4,5):("Be-9",True,1.5),
 (5,4):("B-9",False,1.5),(4,6):("Be-10",True,0),(5,5):("B-10",True,3),
 (5,6):("B-11",True,1.5),(6,5):("C-11",True,1.5),(6,6):("C-12",True,0),
 (6,7):("C-13",True,.5),(7,6):("N-13",True,.5),(7,7):("N-14",True,1),
 (7,8):("N-15",True,.5),(8,7):("O-15",True,.5),(8,8):("O-16",True,0),
 # bound, but more than two alike outside the rings (rule 3 cannot build them):
 (2,6):("He-8",True,0),(3,5):("Li-8",True,2),(3,6):("Li-9",True,1.5),
 (5,3):("B-8",True,2),(4,7):("Be-11",True,.5),(5,7):("B-12",True,1)}
def holds(pieces):
    n=len(pieces)
    if n==1: return True
    def join(a,b):
        if a!='R' and b!='R' and a[0]!=b[0] and a[1]==b[1]: return 'F'
        return 'W'
    for k in range(1,n//2+1):
        for part in combinations(range(n),k):
            cross=[join(pieces[i],pieces[j]) for i in part for j in range(n) if j not in part]
            if 'F' not in cross and len(cross)<2: return False
    return True
def spin(pieces):
    rings=pieces.count('R'); loose=[p for p in pieces if p!='R']
    w=1.5 if rings else .5
    return abs(sum(w*p[1] for p in loose))
print(f"{'':6}{'holds':>6}{'obs':>6}   spins given / observed")
for (Z,N),(name,ob,os_) in OBS.items():
    res=[]
    for r in range(0,min(Z,N)//2+1):
        zp,nn=Z-2*r,N-2*r
        if zp>2 or nn>2: continue
        if zp==2 and nn==2: continue          # four loose are a ring
        for ps in ([()] if zp==0 else [(1,),(-1,)] if zp==1 else [(1,-1)]):
            for ns in ([()] if nn==0 else [(1,),(-1,)] if nn==1 else [(1,-1)]):
                pcs=['R']*r+[('p',s) for s in ps]+[('n',s) for s in ns]
                if holds(pcs): res.append(spin(pcs))
    h=bool(res); sp=sorted(set(res))
    flag='' if h==ob and (not h or os_ in sp) else '  <-- miss'
    if not h and not ob: flag=''
    if not res and ob: flag='  <-- cannot be built'
    print(f"{name:6}{str(h):>6}{str(ob):>6}   {sp} / {os_}{flag}")
