# Lattice ray trace for G8: omega(k; x,y) = E_walk(k; w(x,y)), Hamilton's equations, one tick per step.
import numpy as np
exec(open('../G6_light_bending/g6.py').read().split("def packet")[0].replace("Lx,Ly=400,256","Lx,Ly=8,8"))
B=120; RC=5.0; K0=0.5; Y0=-440
def wat(X,Y,A,st):
    Phi=A/np.sqrt(X*X+Y*Y+RC*RC); return np.arccos(c0*(1-Phi)/(1+st*Phi)/2)
def om(kx,ky,X,Y,A,st): return E(kx,ky,0,wat(X,Y,A,st))
def trace(A,st,T):
    X,Y,kx,ky=float(B),float(Y0),0.0,K0; h=1e-4; d=0.5
    for t in range(T):
        def f(X,Y,kx,ky):
            vx=(om(kx+h,ky,X,Y,A,st)-om(kx-h,ky,X,Y,A,st))/(2*h); vy=(om(kx,ky+h,X,Y,A,st)-om(kx,ky-h,X,Y,A,st))/(2*h)
            fx=-(om(kx,ky,X+d,Y,A,st)-om(kx,ky,X-d,Y,A,st))/(2*d); fy=-(om(kx,ky,X,Y+d,A,st)-om(kx,ky,X,Y-d,A,st))/(2*d)
            return vx,vy,fx,fy
        a=f(X,Y,kx,ky); b=f(X+a[0]/2,Y+a[1]/2,kx+a[2]/2,ky+a[3]/2)
        X+=b[0];Y+=b[1];kx+=b[2];ky+=b[3]
    return kx,X,Y
T=int(2*abs(Y0)/1.85); A=0.6
for label,st in [("clock only",0),("clock+stretch",1)]:
    p=trace(A,st,T); m=trace(-A,st,T)
    print(f"ray {label}: delta kx (odd) = {(p[0]-m[0])/2:+.5e}  angle {(p[0]-m[0])/2/K0:+.5e}  x shift {(p[1]-m[1])/2:+.3f}")
