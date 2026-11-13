exec(open('bloch.py').read().split("# check unitarity")[0])
import numpy as np
h=1e-5
def drift(th,b,k0=0.0,band=None):
    K0=2*k0
    def e(K,ref):
        ev=bands(K,0,th,b); return ev[np.argmin(abs(ev-ref))]
    ref=bands(K0,0,th,0)
    ref0=ref[np.argmin(abs(ref-band))] if band is not None else th
    r=e(K0,ref0)
    return -(e(K0+h,r)-e(K0-h,r))/(2*h)*2
for th in [0.1,0.4,0.55,0.59,0.6,0.61,0.65,1.0]:
    print(f"th={th}: drift/(2 sin b) at b=0.05: {drift(th,0.05)/(2*np.sin(0.05)):.6f}, b=0.4: {drift(th,0.4)/(2*np.sin(0.4)):.6f}")
print("doubler (k=pi, energy 4w-th) drift / 2 sin b:")
for th in [0.0,0.4]:
    print(th, drift(th,0.05,k0=np.pi,band=abs(4*0.3-th))/(2*np.sin(0.05)), "  light group-vel tilt at k=0.05 via Bloch:")
# light tilt at k small
for k0 in [0.02,0.2]:
    vp=-drift(0,0.05,k0=k0,band=None) if False else None
