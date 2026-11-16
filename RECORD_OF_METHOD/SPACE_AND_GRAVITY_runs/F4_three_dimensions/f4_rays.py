# F4 diagnostic (after the run): the packet-averaged ray prediction, same fit protocol as f4_run.py.
# Semiclassical energy on the step with the field: E(x,k) = sqrt(D^2 sum sin^2 k + (D w(k) + m N)^2), w = r sum(1-cos k),
# D = N/psi^2, N = 1 - g s, psi^2 = 1 + g s (or 1, clock only); s = n.x. Rays sampled from the packet's momentum density |amp|^2.
import numpy as np
from scipy.integrate import solve_ivp
r=0.5; tau=0.4; T=40; n=8; ts=np.arange(n+1)*tau*T/n; sig=6
def E(x,k,m,g,nh,stretch):
    s=np.dot(nh,x); N=1-g*s; D=N/(1+g*s) if stretch else N; w=r*np.sum(1-np.cos(k))
    return np.sqrt(D**2*np.sum(np.sin(k)**2)+(D*w+m*N)**2)
def rhs(t,y,m,g,nh,st):
    x,k=y[:3],y[3:]; h=1e-6; e=np.eye(3)
    dx=[(E(x,k+h*e[i],m,g,nh,st)-E(x,k-h*e[i],m,g,nh,st))/(2*h) for i in range(3)]
    dk=[-(E(x+h*e[i],k,m,g,nh,st)-E(x-h*e[i],k,m,g,nh,st))/(2*h) for i in range(3)]
    return dx+dk
def accel(m,k0,nh,g,st,nr=400,seed=0):
    rng=np.random.default_rng(seed); ks=np.array(k0)+rng.normal(0,1/(sig*np.sqrt(2)),(nr,3)); xs=np.zeros(n+1)
    for k in ks:
        sol=solve_ivp(rhs,(0,ts[-1]),list(np.zeros(3))+list(k),t_eval=ts,args=(m,g,nh,st),rtol=1e-9,atol=1e-12)
        xs+=np.dot(nh,sol.y[:3])
    xs/=nr; return np.polyfit(ts,xs,2)[0]*2
g=2e-4
for m in (0.25,0.5):
    for name,nh in (("axis",np.array([1.,0,0])),("body diagonal",np.ones(3)/np.sqrt(3))):
        a=(accel(m,(0,0,0),nh,g,True)-accel(m,(0,0,0),nh,-g,True))/2
        print(f"rays: m={m}, along {name}: a = {a:.5e}  (point packet g(1+rm) = {g*(1+r*m):.5e})",flush=True)
nh=np.array([1.,0,0]); full=(accel(0.0,(0,0.3,0),nh,g,True)-accel(0.0,(0,0.3,0),nh,-g,True))/2
clock=(accel(0.0,(0,0.3,0),nh,g,False)-accel(0.0,(0,0.3,0),nh,-g,False))/2
print(f"rays: light k_y=0.3: full a_x = {full:.5e}, clock {clock:.5e}, ratio {full/clock:.4f}")
