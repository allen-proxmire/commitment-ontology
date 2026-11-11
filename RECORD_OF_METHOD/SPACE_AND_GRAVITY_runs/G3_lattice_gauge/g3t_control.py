"""G3: gauge-invariant quadratic costs on CO's lattice carriers (lapse and shear at places; stretch and one-way part on links)."""
import numpy as np, itertools, time
rng=np.random.default_rng(1)
# components: 0:h00 1-3:h0i(link i) 4-6:hii(link i) 7:hxy 8:hyz 9:hxz (places)
off={(0,1):7,(1,2):8,(0,2):9}
def gauge(kv,xi):
    k0,k=kv[0],kv[1:]; s=2*np.sin(k/2); c=np.ones(3); x0,xs=xi[0],xi[1:]
    d=np.zeros(10)
    d[0]=2*k0*x0
    for i in range(3):
        d[1+i]=s[i]*x0+k0*c[i]*xs[i]
        d[4+i]=2*s[i]*xs[i]
    for (i,j),a in off.items():
        d[a]=s[i]*c[i]*xs[j]+s[j]*c[j]*xs[i]
    return d
def monos(kv):
    k0,k=kv[0],kv[1:]; s=2*np.sin(k/2); c=np.cos(k/2)
    D=np.r_[k0,s]; dd=[D[a]*D[b] for a in range(4) for b in range(a,4)]
    cc=[1.0]+[c[a]*c[b] for a in range(3) for b in range(a,3)]
    return np.array([x*y for x in dd for y in cc])
AB=[(a,b) for a in range(10) for b in range(a,10)]
def feat(h,kv):
    m=monos(kv); hh=np.array([h[a]*h[b] for (a,b) in AB]); return np.outer(hh,m).ravel()
# symmetry actions on (k, h)
def perm_act(P):  # P: permutation of spatial axes, new axis a = old P[a]
    def act(kv,h):
        k=kv.copy(); k[1:]=kv[1:][P]
        g=np.zeros(10); g[0]=h[0]
        for a in range(3): g[1+a]=h[1+P[a]]; g[4+a]=h[4+P[a]]
        for (i,j),idx in off.items():
            pi,pj=sorted((P[i],P[j])); g[idx]=h[off[(pi,pj)]]
        return k,g
    return act
def refl(axis):
    def act(kv,h):
        k=kv.copy(); k[1+axis]=-k[1+axis]; g=h.copy(); g[1+axis]=-g[1+axis]
        for (i,j),idx in off.items():
            if axis in (i,j): g[idx]=-g[idx]
        return k,g
    return act
def trev(kv,h):
    k=kv.copy(); k[0]=-k[0]; g=h.copy(); g[1:4]=-g[1:4]; return k,g
gens=[perm_act(np.array([1,2,0])),perm_act(np.array([1,0,2])),refl(0),trev]
nf=len(AB)*len(monos(np.ones(4)))
G=np.zeros((nf,nf)); t=time.time()
for n in range(2500):
    kv=rng.uniform(-np.pi,np.pi,4); kv[0]=rng.normal()
    h=rng.normal(size=10); f0=feat(h,kv)
    rows=[]
    for g in gens:
        k2,h2=g(kv,h); rows.append(feat(h2,k2)-f0)
    xi=rng.normal(size=4); rows.append(feat(h+gauge(kv,xi),kv)-f0)
    R=np.array(rows); G+=R.T@R
ev,V=np.linalg.eigh(G)
null=V[:,ev<1e-9*ev.max()].T
print('features',nf,'null-space dimension (exactly invariant costs):',len(null),' time',round(time.time()-t,1),'s')
np.save('g3t_null.npy',null)
