"""R10b: Strang-symmetrised walk + unitary Wilson mass (R9-A). Count gapless points."""
import numpy as np, itertools, json
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
P=lambda j,k: Pp[j]*np.exp(1j*k)+Pm[j]*np.exp(-1j*k)
Ph=lambda j,k: np.cos(k/2)*np.eye(4)+1j*np.sin(k/2)*alpha[j]
W=lambda k: sum(1-np.cos(kj) for kj in k)
def U(k,th,r):
    ang=th+r*W(k); M=np.cos(ang)*np.eye(4)-1j*np.sin(ang)*beta
    return M@Ph(0,k[0])@Ph(1,k[1])@P(2,k[2])@Ph(1,k[1])@Ph(0,k[0])
def gapless(Uf,n=40,tol=0.08):
    ks=np.linspace(-np.pi,np.pi,n,endpoint=False); hits=[]
    for k in itertools.product(ks,repeat=3):
        if (np.abs(np.angle(np.linalg.eigvals(Uf(k))))<tol).any(): hits.append(k)
    if not hits: return 0,[]
    from scipy.cluster.hierarchy import fcluster, linkage
    H=np.array(hits); lab=fcluster(linkage(H,'single'),0.5,'distance') if len(H)>1 else np.array([1])
    return len(np.unique(lab)),[np.round(H[lab==i].mean(0)/np.pi,2).tolist() for i in np.unique(lab)]
out={}
for th,r in [(0.0,0.5),(0.3,0.5),(0.0,0.2)]:
    n,p=gapless(lambda k:U(k,th,r)); out[f'theta{th}_r{r}']={'n':n,'points_over_pi':p}; print(th,r,n,p)
# low-k check: dispersion near origin unchanged (E ~ sqrt(theta^2 + k^2) with tiny r k^2 shift)
for kk in (0.05,0.1,0.2):
    e=np.min(np.abs(np.angle(np.linalg.eigvals(U((kk,0,0),0.3,0.5))))); print("k=%.2f E=%.4f  sqrt(th^2+k^2)=%.4f"%(kk,e,np.hypot(0.3,kk)))
json.dump(out,open('r10b_result.json','w'),indent=1)
