"""R10d (post-review): the adopted walk (palindrome x y z | flip | z y x) with alternation angle
theta(k) = theta + r*W(k), W = sum(1-cos k_j). The unitary Wilson angle is periodic, so r must sit in a window.
For each r: lowest |quasi-energy| anywhere in the zone away from the origin (the lightest doubler), found by
a 48^3 grid scan refined by Nelder-Mead; also the lightest mode in the pi-sector (|E| near pi counted as pi-|E|)."""
import numpy as np, itertools, json
from scipy.optimize import minimize
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
P=lambda j,k: Pp[j]*np.exp(1j*k)+Pm[j]*np.exp(-1j*k)
W=lambda k: sum(1-np.cos(kj) for kj in k)
def U(k,th,r):
    ang=th+r*W(k); M=np.cos(ang)*np.eye(4)-1j*np.sin(ang)*beta
    return P(0,k[0])@P(1,k[1])@P(2,k[2])@M@P(2,k[2])@P(1,k[1])@P(0,k[0])
def E0(k,th,r): return np.min(np.abs(np.angle(np.linalg.eigvals(U(k,th,r)))))
def Epi(k,th,r): return np.min(np.pi-np.abs(np.angle(np.linalg.eigvals(U(k,th,r)))))
def lightest(f,th,r,n=48,exclude_origin=True):
    ks=np.linspace(-np.pi,np.pi,n,endpoint=False); best=[]
    for k in itertools.product(ks,repeat=3):
        if exclude_origin and np.linalg.norm(k)<0.6: continue
        best.append((f(k,th,r),k))
    best.sort(key=lambda t:t[0]); out=[]
    for e,k in best[:6]:
        res=minimize(lambda q:f(q,th,r),k,method='Nelder-Mead',options={'xatol':1e-5,'fatol':1e-7})
        out.append((float(res.fun),np.round(np.array(res.x)/np.pi,3).tolist()))
    out.sort(key=lambda t:t[0]); return out[0]
out={}
for th in (0.3,0.0):
    for r in (0.0,0.1,0.2,0.3,0.4,0.5):
        e0,k0=lightest(E0,th,r); ep,kp=lightest(Epi,th,r,exclude_origin=False)
        out[f'theta{th}_r{r}']={'origin_E':float(E0((0,0,0),th,r)),'lightest_doubler_E0':e0,'at_k_over_pi':k0,'lightest_pi_sector':ep,'pi_at_k_over_pi':kp}
        print(f"theta={th} r={r}: origin {E0((0,0,0),th,r):.3f} | lightest 0-sector doubler {e0:.3f} at {k0} | lightest pi-sector {ep:.3f} at {kp}",flush=True)
json.dump(out,open('r10d_result.json','w'),indent=1)
