import numpy as np,sys; sys.path.insert(0,'.')
from i1 import *
w=5*np.pi/16; c0=2*np.cos(w); Nx=64; Nyz=int(sys.argv[2]) if len(sys.argv)>2 else 24
th=float(sys.argv[1]); x=np.arange(Nx)
e0=vac(Nx,th,w,Nyz); out={'B':[],'E':[]}
for n in range(1,6):
    q=2*np.pi*n/Nx; prof=np.cos(q*x)
    for f in 'BE':
        d=[]
        for a in (0.05,0.1):
            e=vac(Nx,th,w,Nyz,Ay=a*prof) if f=='B' else vac(Nx,th,w,Nyz,V=a*prof); d.append((e-e0)/a**2)
        out[f].append((4*d[0]-d[1])/3)
    print(f"th={th} n={n} q={q:.4f} C_B={out['B'][-1]:+.6e} C_E={out['E'][-1]:+.6e}",flush=True)
qh=2*np.sin(np.pi*np.arange(1,6)/Nx); X=np.vstack([qh**2,qh**4,qh**6]).T; res={}
for f in 'BE':
    y=np.array(out[f]); c=np.linalg.lstsq(X,y,rcond=None)[0]; r=np.max(np.abs(X@c-y))/np.max(np.abs(y)); res[f]=(c,r)
    print(f"{f}: c2={c[0]:+.6e} c4/c2={c[1]/c[0]:+.4f} c6/c2={c[2]/c[0]:+.4f} fit resid={r:.1e}")
cB,cE=res['B'][0][0],res['E'][0][0]
if cB*cE<0: ci=np.sqrt(-cB/cE); print(f"th={th}: c_ind={ci:.5f} c0={c0:.5f} ratio-1={ci/c0-1:+.4f}  Z_E={-4*cE:.4e} Z_B={4*cB:.4e}")
else: print("same sign: INVALID")
