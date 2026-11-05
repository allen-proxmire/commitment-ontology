"""R10c: local symmetrised step (palindrome x y z | flip | z y x) + alternation mass. Half-steps are not
lattice-local; the palindrome is the local form of 'no preferred order'. Count gapless points."""
import numpy as np, itertools, json
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
P=lambda j,k: Pp[j]*np.exp(1j*k)+Pm[j]*np.exp(-1j*k)
W=lambda k: sum(1-np.cos(kj) for kj in k)
def U(k,th,r):
    ang=th+r*W(k); M=np.cos(ang)*np.eye(4)-1j*np.sin(ang)*beta
    return P(0,k[0])@P(1,k[1])@P(2,k[2])@M@P(2,k[2])@P(1,k[1])@P(0,k[0])
def gapless(Uf,n=40,tol=0.08):
    ks=np.linspace(-np.pi,np.pi,n,endpoint=False); hits=[]
    for k in itertools.product(ks,repeat=3):
        if (np.abs(np.angle(np.linalg.eigvals(Uf(k))))<tol).any(): hits.append(k)
    if not hits: return 0,[]
    from scipy.cluster.hierarchy import fcluster, linkage
    H=np.array(hits); lab=fcluster(linkage(H,'single'),0.5,'distance') if len(H)>1 else np.array([1])
    return len(np.unique(lab)),[np.round(H[lab==i].mean(0)/np.pi,2).tolist() for i in np.unique(lab)]
out={}
for th,r in [(0.0,0.0),(0.0,0.5),(0.3,0.0),(0.3,0.5)]:
    n,p=gapless(lambda k:U(k,th,r)); out[f'theta{th}_r{r}']={'n':n,'points_over_pi':p if n<10 else 'many'}; print(th,r,n,(p if n<10 else 'many'))
for kk in (0.05,0.1,0.2):
    e=np.min(np.abs(np.angle(np.linalg.eigvals(U((kk,0,0),0.3,0.5))))); print("k=%.2f E=%.4f  sqrt(th^2+(2k)^2)=%.4f (double step: two hops per flip)"%(kk,e,np.hypot(0.3,2*kk)))
json.dump(out,open('r10c_result.json','w'),indent=1)
