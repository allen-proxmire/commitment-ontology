"""R9: two 'commitment gives transit a direction' versions of CO's automaton U = M Pz Py Px.
 (A) unitary Wilson mass: U_A(k) = exp(-i r beta W(k)) U(k),  W(k) = sum_j (1 - cos k_j)
 (B) non-unitary damping:  U_B(k) = exp(-eps W(k)) U(k)
Count gapless points (quasi-energy 0, |lambda|=1 within tol) over the zone, and the low-k lifetime for (B)."""
import numpy as np, itertools, json
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
def U0(k,theta):
    u=np.eye(4)
    for j in range(3): u=(Pp[j]*np.exp(1j*k[j])+Pm[j]*np.exp(-1j*k[j]))@u
    return (np.cos(theta)*np.eye(4)-1j*np.sin(theta)*beta)@u
W=lambda k: sum(1-np.cos(kj) for kj in k)
UA=lambda k,theta,r: (np.cos(r*W(k))*np.eye(4)-1j*np.sin(r*W(k))*beta)@U0(k,theta)
UB=lambda k,theta,eps: np.exp(-eps*W(k))*U0(k,theta)
def gapless_points(Uf, n=40, tol_E=0.08, tol_mod=0.02):
    ks=np.linspace(-np.pi,np.pi,n,endpoint=False); hits=[]
    for k in itertools.product(ks,repeat=3):
        lam=np.linalg.eigvals(Uf(k))
        ok=(np.abs(np.angle(lam))<tol_E)&(np.abs(np.abs(lam)-1)<tol_mod)
        if ok.any(): hits.append(k)
    if not hits: return 0,[]
    from scipy.cluster.hierarchy import fcluster, linkage
    H=np.array(hits); lab=fcluster(linkage(H,'single'),0.5,'distance') if len(H)>1 else np.array([1])
    return len(np.unique(lab)),[np.round(H[lab==i].mean(0)/np.pi,2).tolist() for i in np.unique(lab)]
out={}
out['baseline_massless']=gapless_points(lambda k:U0(k,0.0))
out['baseline_massive']=gapless_points(lambda k:U0(k,0.3))
out['A_wilson_mass_massless_r0.5']=gapless_points(lambda k:UA(k,0.0,0.5))
out['A_wilson_mass_massive_r0.5']=gapless_points(lambda k:UA(k,0.3,0.5))
out['B_damping_massless_eps0.5']=gapless_points(lambda k:UB(k,0.0,0.5))
# (B) low-k lifetime: |lambda| per step at small k -> decay rate eps*k^2/2 per step
rates={}
for kk in (1e-1,1e-2,1e-3):
    lam=np.linalg.eigvals(UB((kk,0,0),0.0,0.5)); rates[kk]=float(-np.log(np.abs(lam).max()))
out['B_decay_per_step']=rates
hop_per_s=3e8/1.1e-18; k_e=1.1e-18/3.86e-13   # electron reduced Compton in hop units
out['B_electron_lifetime_s']=1/(0.5*k_e**2/2*hop_per_s)
for k,v in out.items(): print(k,":",v)
json.dump(out,open('r9_result.json','w'),indent=1,default=float)
