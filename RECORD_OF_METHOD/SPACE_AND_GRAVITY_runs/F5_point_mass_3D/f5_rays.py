import numpy as np,sys; sys.path.insert(0,'.')
from common import *
from scipy.integrate import solve_ivp
def E(x,k,full):
    P=Phi(*x); N=1-P; D=N/(1+P) if full else N; return np.sqrt(D**2*np.sum(np.sin(k)**2)+(D*r*np.sum(1-np.cos(k)))**2)
def rhs(t,y,full):
    x,k=y[:3],y[3:]; e=np.eye(3); h=1e-5
    return [ (E(x,k+h*e[i],full)-E(x,k-h*e[i],full))/(2*h) for i in range(3)]+[-(E(x+h*e[i],k,full)-E(x-h*e[i],k,full))/(2*h) for i in range(3)]
# Gauss-Hermite quadrature (5 points each) over the packet's x, z, k_x, k_y spread (y and k_z spread enter at higher order);
# a 400-ray Monte Carlo first gave +/-13% sampling error, too coarse for the 5% window (f5_rays_montecarlo_out.txt)
gx,gw=np.polynomial.hermite_e.hermegauss(5); gw=gw/gw.sum(); sx=sig/np.sqrt(2); sk=1/(sig*np.sqrt(2))
xs=[];ks=[];W=[]
for a,wa in zip(gx,gw):
  for b,wb in zip(gx,gw):
    for c,wc in zip(gx,gw):
      for d_,wd in zip(gx,gw):
        xs.append([a*sx,Y0,b*sx]); ks.append([c*sk,K0+d_*sk,0.]); W.append(wa*wb*wc*wd)
xs=np.array(xs); ks=np.array(ks); W=np.array(W); n=len(W)
for full in (False,True):
    d=[solve_ivp(rhs,(0,T_FLOW),list(x)+list(k),args=(full,),rtol=1e-8,atol=1e-10).y[3,-1]-k[0] for x,k in zip(xs,ks)]
    d=np.array(d)/K0
    print(f"{'full ' if full else 'clock'}: packet-averaged deflection (dk_x/k_y) = {np.sum(W*d):+.5e} (Gauss-Hermite, {n} rays); centre ray {d[n//2]:+.5e}",flush=True)
