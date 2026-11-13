# Under P7f (mass flip theta N, Wilson flip 2 cos w = c0 N/psi^2), does every band's rest energy scale with the clock (x N) and ignore the stretch?
# 3D walk of L1b; a 1% clock slowing and a 1% stretch; lowest |quasi-energy| at the zone centre and at the doublers' corners.
import numpy as np
exec(open('../../MATTER_runs/L1b_local_wilson/l1b_local_wilson.py').read().split("dirs={")[0])
c0=2*np.cos(0.3); th=0.05
for lab,N,ps2 in [("clock -1%",0.99,1.0),("stretch +1%",1.0,1.01)]:
    w=np.arccos(c0*N/ps2/2)
    for k in [(0,0,0),(np.pi,0,0),(np.pi,np.pi,0),(np.pi,np.pi,np.pi)]:
        e0=qe(U(np.array(k),th,0.3))[0]; e1=qe(U(np.array(k),th*N,w))[0]
        print(f"{lab}: k/pi={np.round(np.array(k)/np.pi,0)}  rest energy {e0:.4f} -> ratio {e1/e0:.4f}  (equivalence needs {N})")
