# "Set more evenly where things commit": two desk checks.
# 1. Can a local rule set a wiggly web even? Each place nudges the weights of its own relations to lessen its own leftover (steepest descent on the
#    conditions of c15f; every update uses a place and its neighbours only). Eight neighbours, places displaced by 0.15 hops.
# 2. Are there enough commitments to do it? Renewals per place, in matter and in the voids.
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl
from c15w import make_d, EIGHT, FOUR
def system(L,d,offs):
    site=lambda x,y:(x%L)*L+(y%L); links=[]
    for x in range(L):
        for y in range(L):
            for o in offs: links.append((site(x,y),site(x+o[0],y+o[1]),np.array(o,float)+d[(x+o[0])%L,(y+o[1])%L]-d[x,y],o))
    nl=len(links); I=np.array([l[0] for l in links]); J=np.array([l[1] for l in links]); DX=np.array([l[2] for l in links]); ar=np.arange(nl)
    rows=[];cols=[];vals=[]
    for a in range(2):
        rows+=[6*I+a,6*J+a]; cols+=[2*ar+a]*2; vals+=[np.ones(nl),-np.ones(nl)]
        for b in range(2): rows+=[6*I+2+2*a+b,6*J+2+2*a+b]; cols+=[2*ar+a]*2; vals+=[DX[:,b]/2,DX[:,b]/2]
    M=sp.csr_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(6*L*L,2*nl))
    b=np.zeros(6*L*L); b[2::6]=1; b[5::6]=1          # cell sizes held at 1: the weights alone are adjusted
    x0=np.zeros(2*nl)
    for l,(i,j,dx,o) in enumerate(links):
        if o in ((1,0),(0,1)): x0[2*l:2*l+2]=o
    return M,b,x0
L=32; d=make_d(L,0.15,0)
for nm,offs in (("eight neighbours",EIGHT),("four neighbours",FOUR)):
    M,b,x=system(L,d,offs); eta=1.0/spl.svds(M,k=1,return_singular_vectors=False)[0]**2; line=[]
    for n in range(0,3001):
        if n in (0,10,100,1000,3000): line.append(f"{n}: {np.linalg.norm(M@x-b)/L:.1e}")
        x=x-eta*(M.T@(M@x-b))
    print(f"1. {nm}, cell sizes held at 1: leftover per place after n local rounds: "+", ".join(line))
print("   count of weights against conditions per place, cells held: d z/2 against d + d^2: needs z >= 2(1 + d) neighbours: 6 in two dimensions, 8 in three (a cubic grid has 6).")
hbar=1.0546e-34; c=2.998e8; mp=1.6726e-27; age=4.35e17
for l in (1.0e-32,5.73e-35):
    places=1/l**3; ext=(0.84e-15/l)**3
    for nm,n in (("the Earth (mean)",5513/mp),("a void (0.02 nucleons per m^3)",0.02)):
        ren=n*mp*c**2/hbar
        print(f"2. l = {l:.2g} m, {nm}: renewals per place per second {ren/places:.1e}; over the universe's age {ren/places*age:.1e}; if each renewal reaches every place its pattern spans (about {ext:.0e}): {ren*ext/places*age:.1e}")
