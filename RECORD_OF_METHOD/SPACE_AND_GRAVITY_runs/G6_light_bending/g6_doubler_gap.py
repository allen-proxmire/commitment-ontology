# How far the Wilson flip can speed light up before the 3D walk's extra species (doublers) close their gap. Grid 24^3, so a gap can close between grid points.
import sys; sys.argv=['x']
src=open('../../MATTER_runs/L1b_local_wilson/l1b_local_wilson.py').read().split('dirs={')[0]
exec(src)
import numpy as np, itertools
def mingap(w,n=24):
    ks=np.linspace(-np.pi,np.pi,n,endpoint=False); g0=9; gp=9
    for k in itertools.product(ks,repeat=3):
        if np.allclose(k,0): continue
        e=qe(U(k,0,w)); g0=min(g0,e[0]); gp=min(gp,np.pi-e[-1])
    return g0,gp
c0=2*np.cos(0.3)
for w in [0.3,0.28,0.26,0.24,0.22,0.2]:
    g0,gp=mingap(w); print(f"w={w}: light speed 2cos w = {2*np.cos(w):.4f} (+{(2*np.cos(w)/c0-1)*100:.2f}%)  min gap: 0-sector {g0:.3f}, pi-sector {gp:.3f}")
