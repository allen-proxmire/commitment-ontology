"""R10: are the eight gamma5 modes an artefact of the split-step ordering?
Orderings tested (massless and theta=0.3): sequential Pz Py Px (baseline); Strang-symmetrised
Px^1/2 Py^1/2 Pz Py^1/2 Px^1/2 (half-steps via sqrt of each unitary factor); palindrome Px Py Pz Pz Py Px;
and the 'simultaneous' walk U = exp(-i sum_j alpha_j sin k_j)-like coin (Hamiltonian-type reference)."""
import numpy as np, itertools, json
from scipy.linalg import sqrtm, expm
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
P=lambda j,k: Pp[j]*np.exp(1j*k)+Pm[j]*np.exp(-1j*k)            # = cos k + i alpha_j sin k
Ph=lambda j,k: np.cos(k/2)*np.eye(4)+1j*np.sin(k/2)*alpha[j]     # half step (exact sqrt)
M=lambda th: np.cos(th)*np.eye(4)-1j*np.sin(th)*beta
def seq(k,th):  u=np.eye(4); [u:=P(j,k[j])@u for j in range(3)]; return M(th)@u
def strang(k,th): return M(th)@Ph(0,k[0])@Ph(1,k[1])@P(2,k[2])@Ph(1,k[1])@Ph(0,k[0])
def palin(k,th): return M(th)@P(0,k[0])@P(1,k[1])@P(2,k[2])@P(2,k[2])@P(1,k[1])@P(0,k[0])
def simul(k,th): return M(th)@expm(1j*sum(alpha[j]*np.sin(k[j]) for j in range(3)))
def gapless(Uf,n=40,tol=0.08):
    ks=np.linspace(-np.pi,np.pi,n,endpoint=False); hits=[]
    for k in itertools.product(ks,repeat=3):
        lam=np.linalg.eigvals(Uf(k))
        if (np.abs(np.angle(lam))<tol).any(): hits.append(k)
    if not hits: return 0,[]
    from scipy.cluster.hierarchy import fcluster, linkage
    H=np.array(hits); lab=fcluster(linkage(H,'single'),0.5,'distance') if len(H)>1 else np.array([1])
    return len(np.unique(lab)),[np.round(H[lab==i].mean(0)/np.pi,2).tolist() for i in np.unique(lab)]
out={}
for name,f in [('sequential',seq),('strang',strang),('palindrome',palin),('simultaneous',simul)]:
    for th in (0.0,0.3):
        n,pts=gapless(lambda k:f(k,th)); out[f'{name}_theta{th}']={'n':n,'points_over_pi':pts}; print(name,th,n,pts,flush=True)
json.dump(out,open('r10_result.json','w'),indent=1)
