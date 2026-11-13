exec(open('bloch.py').read().split("# check unitarity")[0])
import numpy as np
h=1e-5
def vel(th,b,k0):
    K0=2*k0
    ref=bands(K0,0,th,0); r0=ref[np.argmin(abs(ref-abs(ref).min()))] if th==0 else th
    # follow positive light band continuously from b=0
    r=None; 
    for bb in np.linspace(0,b,60):
        ev=bands(K0,0,th,bb); r=ev[np.argmin(abs(ev-(r if r is not None else min(ref[ref>0]))))]
    def e(K):
        ev=bands(K,0,th,b); return ev[np.argmin(abs(ev-r))]
    return (e(K0+h)-e(K0-h))/(2*h)*2
for b in [0,0.1,0.4,0.8,np.pi/2,2.0]:
    vp=vel(0,b,0.1); vm=vel(0,b,-0.1)
    print(f"b={b:.3f}: light |v| at k=+-0.1: {abs(vp):.4f} {abs(vm):.4f}  tilt {(abs(vp)-abs(vm))/2:+.4f} mean {(abs(vp)+abs(vm))/2:.4f}  2sinb cos0.1={2*np.sin(b)*np.cos(0.1):.4f}")
print("signed:")
for b in [0.8,1.2,np.pi/2]:
    print(f"b={b:.3f} light v(+0.1)={vel(0,b,0.1):+.4f} v(-0.1)={vel(0,b,-0.1):+.4f}; matter th0.4 drift={vel(0.4,b,0.0) if False else 0}")
exec(open('b3.py').read().split('for th in')[0])
for b in [0.8,1.2,np.pi/2]:
    print(f" b={b:.3f} matter drift/(2 sin b): th0.2 {drift(0.2,b)/(2*np.sin(b)):.5f} th0.4 {drift(0.4,b)/(2*np.sin(b)):.5f}")
