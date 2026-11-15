import numpy as np,sys; sys.path.insert(0,'.')
from dw import Ustrip,F
w=5*np.pi/16; L=16; ths=[0.5]*L+[-0.5]*L
ks=np.array([0.02,0.04,0.06,0.08,0.1,0.12])
def wallE(k):
    e=np.angle(np.linalg.eigvals(Ustrip(k,ths,w))); e=np.sort(np.abs(e)); return e[:2]
def walk1(k):
    Ax=np.diag([np.exp(-1j*k),1])@F(w)@np.diag([1,np.exp(1j*k)])@F(-w); return np.abs(np.angle(np.linalg.eigvals(Ax@F(0)@Ax))).min()
m0=wallE(0.0)[0]
Ew=np.array([np.sqrt(max(wallE(k)[0]**2-m0**2,0)) for k in ks]); E1=np.array([walk1(k) for k in ks])
for name,E in (("1D Wilson walk",E1),("1+1D domain-wall mode",Ew)):
    p=np.polyfit(ks**2,E/ks,2); print(f"{name}: speed {p[2]:.6f}, c2 (E = v k (1 + c2 k^2)) = {p[1]/p[2]:+.4f}")
c2a=np.polyfit(ks**2,E1/ks,2); c2b=np.polyfit(ks**2,Ew/ks,2)
r=(c2b[1]/c2b[2])/(c2a[1]/c2a[2]); print(f"ratio of quadratic terms (wall/walk) = {r:.3f}; threshold coefficient C scales as ratio^(-1/4) = {r**-0.25:.3f}")
print("3D walk axis value for reference: -sin^2 w/8 =",-np.sin(w)**2/8)
