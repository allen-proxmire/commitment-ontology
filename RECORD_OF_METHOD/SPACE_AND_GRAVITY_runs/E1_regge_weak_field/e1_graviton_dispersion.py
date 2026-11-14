# The graviton's lattice dispersion from E1's Regge set-up: a spatial plane wave (no time component), transverse-traceless.
exec(open('e1_regge.py').read().split("rng=np.random")[0])
import numpy as np
def tt(n):
    k=np.array(n,float); k/=np.linalg.norm(k)
    # two unit vectors orthogonal to k in the spatial block (axes 1..3) -> e = u u - v v
    a=np.array([0,1,0,0.]) if abs(k[1])<0.9 else np.array([0,0,1,0.])
    u=a-k*(a@k); u/=np.linalg.norm(u); v=np.cross(k[1:],u[1:]); v=np.r_[0,v]; v/=np.linalg.norm(v)
    return np.outer(u,u)-np.outer(v,v), np.outer(u,v)+np.outer(v,u)
for n in [(0,1,0,0),(0,1,1,0),(0,1,1,1)]:
    for pol in (0,1):
        rows=[]
        for L in [24,48,96]:
            e=tt(n)[pol]; k=2*np.pi*np.array(n)/L
            r=S2(L,n,e)/Q(e,k)/L/(-0.25)
            rows.append((np.sum(k**2),r))
        k2=np.array([a for a,b in rows]); rr=np.array([b for a,b in rows])
        xi=np.polyfit(k2,rr,1)[0]
        print(f"n={n} pol {pol}: S2/Q/(-1/4) at L=24,48,96: {np.round(rr,5)}  -> xi (omega^2 = k^2(1+xi k^2)) = {xi:+.4f}; group-speed c2 = 1.5 xi = {1.5*xi:+.4f}")
