# G16: a black hole in Painleve-Gullstrand form on CO's 2D walk (w = 5pi/16): the drift v = sqrt(2GM/r) inward,
# lapse and stretch 1, carried by directed hops on both axes (drift 2 sin b per axis). Horizon r_s = 2GM/c0^2 = 40 hops.
# Fail conditions (stated first): zero-momentum packets not following dr/dt = -v(r) (the PG free-faller, through the horizon);
# light emitted outward not escaping outside r_s and not swept in inside it.
import numpy as np, sys
LX,LY=420,420
exec(open('../G12_rotation_and_gradient/g12.py').read().replace("open('../G6_light_bending/g6.py').read()","open('../G6_light_bending/g6.py').read().replace('w0=0.3','w0=5*np.pi/16')"))
rs=40.0; GM2=c0**2*rs; rc=4.0; vcap=1.9
def vdrift(X,Y):
    r=np.sqrt(X**2+Y**2+rc**2); v=np.minimum(np.sqrt(GM2/r),vcap); return -v*X/r, -v*Y/r, v
# link from place (x,y) to its + neighbour along an axis: drift component at the link's midpoint
vx,_,_=vdrift(x+0.5,yv); _,vy,_=vdrift(x,yv+0.5)
Bx=np.arcsin(vx/2); By=np.arcsin(vy/2)
phx=np.exp(2j*np.pi*x/Lx); phy=np.exp(2j*np.pi*yv/Ly)
def cen(q): return np.angle(np.sum(q*phx))*Lx/(2*np.pi), np.angle(np.sum(q*phy))*Ly/(2*np.pi)
def run(th,kx0,x0,sig,T):
    p=packet_k(th,kx0,0,sig); p=np.roll(p,x0,axis=1); xs=[]
    for t in range(T+1):
        q=np.sum(abs(p)**2,0); xs.append(cen(q)[0]); p=stepD(p,th*np.ones_like(x),Bx,By)
    return np.array(xs)
def ray_r(r0,T,sign=-1,c=0.0):   # dr/dt = -v(r) + c (c = light's outward speed)
    r=float(r0); out=[r]
    for t in range(T):
        rr=np.sqrt(r*r+rc*rc); v=min(np.sqrt(GM2/rr),vcap); r+=(-v*r/rr+c); out.append(r)
    return np.array(out)
print(f"c0={c0:.4f}, horizon r_s={rs}")
T=150
for x0 in [150,110]:
    xs=run(0.5,0.0,x0,12,T); pr=ray_r(x0,T)
    print(f"zero-momentum matter from r={x0}: r(t) at t=0,50,100,150: {np.round(xs[[0,50,100,150]],1)}  PG free-faller: {np.round(pr[[0,50,100,150]],1)}"); sys.stdout.flush()
for x0 in [70,50,32]:
    T2=100; xs=run(0.0,0.4,x0,10,T2); 
    vg=(E(0.4+1e-5,0,0,w0)-E(0.4-1e-5,0,0,w0))/2e-5
    pr=ray_r(x0,T2,c=vg)
    print(f"light outward from r={x0} (group speed {vg:.3f}): r at t=0,25,50,100: {np.round(xs[[0,25,50,100]],1)}  ray: {np.round(pr[[0,25,50,100]],1)}"); sys.stdout.flush()
