# F2b diagnostic (after the run; verdict unchanged): lattice rays on the flow's own dispersion, H = D(x) w(k),
# single ray through the packet centre and averaged over the packet's spread of positions and momenta (as G8's g8_rayavg.py).
import numpy as np
from scipy.integrate import solve_ivp
r=0.5; A=0.6; rc=5.0; B=120; Y0=-440; K0=0.5; sig=40
w=lambda kx,ky: np.sqrt(np.sin(kx)**2+np.sin(ky)**2+(r*(2-np.cos(kx)-np.cos(ky)))**2)
def grad_k(kx,ky,h=1e-6): return ((w(kx+h,ky)-w(kx-h,ky))/(2*h),(w(kx,ky+h)-w(kx,ky-h))/(2*h))
h_=1e-6; vy=(w(0,K0+h_)-w(0,K0-h_))/(2*h_); T=2*abs(Y0)/vy
def run(x0,y0,kx0,ky0,full):
    def D(x,y):
        P=A/np.sqrt((x+B)**2+y**2+rc**2); return (1-P)/(1+P) if full else 1-P
    def f(t,s):
        x,y,kx,ky=s; d=D(x,y); e=1e-4; gx=(D(x+e,y)-D(x-e,y))/(2*e); gy=(D(x,y+e)-D(x,y-e))/(2*e); vx,vy_=grad_k(kx,ky); ww=w(kx,ky)
        return [d*vx,d*vy_,-ww*gx,-ww*gy]
    return solve_ivp(f,(0,T),[x0,y0,kx0,ky0],rtol=1e-8,atol=1e-10).y[2,-1]-kx0
rng=np.random.default_rng(1); n=300
xs=rng.normal(0,sig/np.sqrt(2),n); ys=Y0+rng.normal(0,sig/np.sqrt(2),n); kxs=rng.normal(0,1/(sig*np.sqrt(2)),n); kys=K0+rng.normal(0,1/(sig*np.sqrt(2)),n)
for full in (False,True):
    single=-run(0,Y0,0,K0,full)/K0
    avg=np.array([-run(a,b,c,d_,full)/K0 for a,b,c,d_ in zip(xs,ys,kxs,kys)])
    print(f"{'full ' if full else 'clock'}: single ray {single:.5e}; packet-averaged {avg.mean():.5e} ± {avg.std()/np.sqrt(n):.1e}")
