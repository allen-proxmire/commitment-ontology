"""R8: species count of a massless nearest-neighbour Dirac operator on
(a) the periodic cubic lattice and (b) a periodic random Delaunay lattice.
See REGISTRATION.md. Output: r8_result.json, r8_dos.png."""
import numpy as np, json, itertools, sys
from scipy.spatial import Delaunay

sx=np.array([[0,1],[1,0]]); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]])
Z=np.zeros((2,2)); alpha=[np.block([[Z,s],[s,Z]]) for s in (sx,sy,sz)]

def build_H(pos, edges, L):
    """pos: (N,3) in periodic box of side L; edges: list of (i,j, dvec) with minimum-image dvec."""
    N=len(pos); H=np.zeros((4*N,4*N),complex)
    # per-site coefficient tensor with unit weights, then normalise so trace T_i = 3
    T=np.zeros((N,3,3)); w={}
    for i,j,d in edges:
        l=np.linalg.norm(d); e=d/l
        T[i]+=l*np.outer(e,e); T[j]+=l*np.outer(e,e)
    s=np.array([3.0/np.trace(T[i]) for i in range(N)])   # site scale
    for i,j,d in edges:
        l=np.linalg.norm(d); e=d/l
        wij=np.sqrt(s[i]*s[j])            # symmetric normalisation
        A=-1j*wij*sum(e[a]*alpha[a] for a in range(3))
        H[4*i:4*i+4,4*j:4*j+4]+=A; H[4*j:4*j+4,4*i:4*i+4]+=A.conj().T
    # check: mean trace of normalised T
    Tn=np.zeros((N,3,3))
    for i,j,d in edges:
        l=np.linalg.norm(d); e=d/l; wij=np.sqrt(s[i]*s[j]); Tn[i]+=wij*l*np.outer(e,e); Tn[j]+=wij*l*np.outer(e,e)
    return H, float(np.mean([np.trace(t) for t in Tn])/3)

def cubic(n):
    L=float(n); pos=np.array(list(itertools.product(range(n),repeat=3)),float)
    idx={tuple(p):k for k,p in enumerate(pos.astype(int))}; edges=[]
    for p in pos.astype(int):
        for a in range(3):
            q=p.copy(); q[a]=(q[a]+1)%n; edges.append((idx[tuple(p)],idx[tuple(q)],np.eye(3)[a]))
    return pos,edges,L

def random_lattice(N,L,seed=0):
    rng=np.random.default_rng(seed); pos=rng.uniform(0,L,(N,3))
    # 27 periodic images for Delaunay
    shifts=np.array(list(itertools.product([-1,0,1],repeat=3)))*L
    allp=np.concatenate([pos+sh for sh in shifts]); owner=np.tile(np.arange(N),27)
    tri=Delaunay(allp); E=set()
    for simp in tri.simplices:
        for a,b in itertools.combinations(simp,2):
            ia,ib=owner[a],owner[b]
            if a//N==13 or b//N==13:           # at least one endpoint in the central copy
                key=(min(ia,ib),max(ia,ib))
                if ia!=ib: E.add(key)
    edges=[]
    for i,j in E:
        d=pos[j]-pos[i]; d-=L*np.round(d/L); edges.append((i,j,d))
    return pos,edges,L

def dos_fit(ev,V,Ec):
    e=ev[np.abs(ev)<Ec]; n=len(e)
    # count N(E)=#{|ev|<E} = (2/3) A E^3 for rho=A E^2 (both signs)
    Es=np.sort(np.abs(e)); Ns=np.arange(1,n+1)
    A=np.polyfit(Es**3,Ns,1)[0]*1.5
    A_single=V/np.pi**2        # c=1
    return A/A_single, n

out={}
n=11; pos,edges,L=cubic(n); H,tr=build_H(pos,edges,L); ev=np.linalg.eigvalsh(H)
nc,cnt=dos_fit(ev,L**3,0.5); out['cubic']={'sites':n**3,'edges':len(edges),'meanTrace3':tr,'species':nc,'modes_used':cnt}
print("cubic:",out['cubic'],flush=True)
N=n**3; pos,edges,L=random_lattice(N,float(n),seed=1); H,tr=build_H(pos,edges,L); evr=np.linalg.eigvalsh(H)
nr,cnt=dos_fit(evr,L**3,0.5); out['random']={'sites':N,'edges':len(edges),'meanTrace3':tr,'species':nr,'modes_used':cnt,
    'species_Ec0.3':dos_fit(evr,L**3,0.3)[0],'species_Ec0.8':dos_fit(evr,L**3,0.8)[0]}
out['cubic']['species_Ec0.3']=dos_fit(ev,L**3,0.3)[0]; out['cubic']['species_Ec0.8']=dos_fit(ev,L**3,0.8)[0]
print("random:",out['random'],flush=True)
json.dump(out,open('r8_result.json','w'),indent=1)
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.figure(figsize=(7,4)); bins=np.linspace(-3,3,121)
plt.hist(ev,bins,histtype='step',label='cubic (naive, 8 species)'); plt.hist(evr,bins,histtype='step',label='random Delaunay')
E=np.linspace(-1,1,200); plt.plot(E,(L**3/np.pi**2)*E**2*(bins[1]-bins[0]),'k--',label='1 species, c=1')
plt.legend(); plt.xlabel('E'); plt.ylabel('modes per bin'); plt.title('R8: Dirac density of states'); plt.tight_layout(); plt.savefig('r8_dos.png',dpi=120)
