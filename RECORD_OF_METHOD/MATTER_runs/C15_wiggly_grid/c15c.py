# The seam of c15b with the unlinked rows linked on as well: a left place on an odd row links diagonally to the two seam places beside it, strength g2.
# Question: can the seam be made clean at long wavelength by the links' strengths alone?
import numpy as np, importlib.util, scipy.sparse as sp, sys, io, contextlib
spec=importlib.util.spec_from_file_location("c15b",__file__.replace("c15c","c15b"))
src=open(__file__.replace("c15c","c15b")).read().split('print("share crossing')[0]
exec(src)
def build2(g,g2):
    H=build(g).tolil(); rows=[];cols=[];vals=[]
    def add(i,j,m):
        for a in range(2):
            for b in range(2):
                if m[a,b]!=0: rows.append(2*i+a);cols.append(2*j+b);vals.append(m[a,b])
    for y in range(1,NY,2):
        for dy in (1,-1):
            i,j=idx(-1,y),idx(0,y+dy); d=(1,dy); a=np.sqrt(2); n=np.array(d)/a; sn=n[0]*sx+n[1]*sy; s=g2
            add(i,j,s/a*(-0.5j*sn-0.5*r*sz)); add(j,i,s/a*(0.5j*sn-0.5*r*sz)); add(i,i,s/a*0.5*r*sz); add(j,j,s/a*0.5*r*sz)
    return (build(g)+sp.csr_matrix((vals,(rows,cols)),shape=(2*NX*NY,2*NX*NY))).tocsr()
print("share turned back, head-on, k = 0.2, by straight-link strength g and diagonal-link strength g2:")
tab={}
for g in (0.7,1.0,1.41):
    for g2 in (0.5,1.0,1.41):
        t,rf,s=run(g,0.2,0.0,build2(g,g2)); tab[(g,g2)]=rf; print(f"  g = {g}, g2 = {g2}: turned back {rf:.4f}")
gb=min(tab,key=tab.get); print("best:",gb)
H=build2(*gb)
for k in (0.1,0.2,0.4,0.8):
    t,rf,s=run(gb[0],k,0.0,H); print(f"  k = {k}: crossing {t:.4f}, turned back {rf:.4f}, at the seam {s:.4f}")
