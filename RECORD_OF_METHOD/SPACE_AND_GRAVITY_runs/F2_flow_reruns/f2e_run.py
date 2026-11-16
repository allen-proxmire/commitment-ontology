# F2e (G16 on the flow step): a non-rotating hole in Painleve-Gullstrand form on the 2D flow, shift alone (N = psi = 1).
import numpy as np,sys; sys.path.insert(0,'.')
from flow2ds import *
from scipy.sparse.linalg import expm_multiply
from scipy.integrate import solve_ivp
tau=0.4; r=0.5; L=420; rs=40.0; one=np.ones((L,L))
X=(np.arange(L)-L//2)[:,None]*one; Y=(np.arange(L)-L//2)[None,:]*one
R=np.sqrt(X**2+Y**2+16.0); v=np.minimum(np.sqrt(rs/R),3.0); bx=-v*X/R; by=-v*Y/R     # softened at 4, capped at 3 (tick condition |b| < 4.35 - m)
ok=True
def om(k,m): return np.sqrt(np.sin(k)**2+(m+r*(1-np.cos(k)))**2)   # 1D section of the dispersion (ky = 0)
def ray(r0,k0,m,ts):
    vv=lambda x: min(np.sqrt(rs/np.sqrt(x*x+16)),3.0)
    def f(t,s):
        x,k=s; h=1e-6; vg=(om(k+h,m)-om(k-h,m))/(2*h); dv=(vv(x+1e-4)-vv(x-1e-4))/2e-4
        return [vg-vv(x)*np.cos(k), dv*np.sin(k)]                     # b = -v(x) along +x; dk/dt = -b' sin k
    return solve_ivp(f,(0,ts[-1]),[r0,k0],t_eval=ts,rtol=1e-9,atol=1e-9).y[0]
cases=[("matter",0.5,0.0,150,12,[120,85,42]),("matter",0.5,0.0,110,12,[73,40,25]),
       ("light out",0.0,0.4,70,10,None),("light out",0.0,0.4,50,10,None),("light out",0.0,0.4,32,10,None)]
for name,m,k0,r0,sig,targets in cases:
    H=build(L,L,m,r,one,one,bx=bx,by=by); p=packet(L,L,m,r,(k0,0.),sig,c0=(r0,0))
    xc=lambda q: np.sum(dens(q,L,L)*X)
    if targets:   # free-faller: r^1.5 = r0^1.5 - 1.5 sqrt(rs) t
        ts=[(r0**1.5-T**1.5)/(1.5*np.sqrt(rs)) for T in targets]
    else: ts=[25,50,100]
    t_prev=0; out=[]; q=p
    for tt,T in zip(ts,targets or [None]*3):
        q=expm_multiply(-1j*(tt-t_prev)*H,q); t_prev=tt; meas=xc(q)
        pred=T if T is not None else ray(r0,k0,m,[tt])[0]
        out.append((tt,meas,pred))
        if targets:
            dev=(meas-pred)/(r0-pred); ok&=abs(dev)<=0.02 if T>=rs else True
            print(f"{name} from {r0}: t={tt:.1f}: r={meas:.2f} vs free-faller {pred:.1f} ({dev:+.4f} of distance fallen){'' if T>=rs else ' [inside r_s, reported]'}",flush=True)
        else:
            print(f"{name} from {r0}: t={tt}: r={meas:.2f} vs ray {pred:.2f}",flush=True)
    if not targets:
        moving_out=out[-1][1]>r0+1
        if r0>rs: ok&=moving_out
        else: ok&=out[-1][1]<r0-1
        print(f"  -> {'escapes' if moving_out else 'swept in' if out[-1][1]<r0-1 else 'held'} (r_s = {rs:.0f})",flush=True)
print("F2e",'PASS' if ok else 'FAIL')
