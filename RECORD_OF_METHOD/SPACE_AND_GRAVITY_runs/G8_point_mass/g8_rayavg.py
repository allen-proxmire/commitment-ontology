# Ray prediction averaged over the packet: start x ~ N(B, SIG/sqrt2), k_x ~ N(0, 1/(SIG sqrt2)), mass on the +B side.
exec(open('g8_ray.py').read().split("T=int(")[0])
SIG=40
def trace2(A,st,T,X0,kx0):
    X,Y,kx,ky=float(X0),float(Y0),kx0,K0; h=1e-4; d=0.5
    def f(X,Y,kx,ky):
        vx=(om(kx+h,ky,X,Y,A,st)-om(kx-h,ky,X,Y,A,st))/(2*h); vy=(om(kx,ky+h,X,Y,A,st)-om(kx,ky-h,X,Y,A,st))/(2*h)
        fx=-(om(kx,ky,X+d,Y,A,st)-om(kx,ky,X-d,Y,A,st))/(2*d); fy=-(om(kx,ky,X,Y+d,A,st)-om(kx,ky,X,Y-d,A,st))/(2*d)
        return vx,vy,fx,fy
    for t in range(T):
        a=f(X,Y,kx,ky); b=f(X+a[0]/2,Y+a[1]/2,kx+a[2]/2,ky+a[3]/2)
        X+=b[0];Y+=b[1];kx+=b[2];ky+=b[3]
    return kx-kx0
T=int(2*abs(Y0)/1.85); A=0.6
rng=np.random.default_rng(1); n=150
xs=rng.normal(B,SIG/np.sqrt(2),n); ks=rng.normal(0,1/(SIG*np.sqrt(2)),n)
for label,st in [("clock only",0),("clock+stretch",1)]:
    d=[trace2(A,st,T,X0,k0)-0 for X0,k0 in zip(xs,ks)]
    d0=[trace2(0,st,T,X0,k0) for X0,k0 in zip(xs[:5],ks[:5])]
    print(f"packet-averaged ray {label}: delta kx = {np.mean(d):+.5e} (+- {np.std(d)/np.sqrt(n):.1e}), angle {np.mean(d)/K0:+.5e}; single central ray see g8_ray")
