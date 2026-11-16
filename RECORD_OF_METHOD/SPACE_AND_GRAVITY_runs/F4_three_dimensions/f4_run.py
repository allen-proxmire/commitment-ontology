import numpy as np,sys; sys.path.insert(0,'.')
from flow3d import *
from scipy.sparse.linalg import expm_multiply
tau=0.4; r=0.5; L=64; ok=True
c=(np.arange(L)-L//2); X,Y,Z=np.meshgrid(c,c,c,indexing='ij')
def accel(m,k0,nh,g,stretch):
    s=nh[0]*X+nh[1]*Y+nh[2]*Z; N=1-g*s; D=N/(1+g*s) if stretch else N
    H=build(L,m,r,N,D); p=packet(L,m,r,k0,6); xs=[]; T=40; n=8
    for i in range(n+1):
        q=dens(p,L); xs.append(np.sum(q*s) if not stretch or nh is None else np.sum(q*s))
        if i<n: p=expm_multiply(-1j*tau*T/n*H,p)
    t=np.arange(n+1)*tau*T/n; return np.polyfit(t,xs,2)[0]*2
g=2e-4
res={}
for m in (0.25,0.5):
    for name,nh in (("axis",(1,0,0)),("body diagonal",tuple(np.ones(3)/np.sqrt(3)))):
        a=(accel(m,(0,0,0),nh,g,True)-accel(m,(0,0,0),nh,-g,True))/2   # odd part in g
        pred=-g*(1+r*m); res[(m,name)]=a; d=a/pred-1; ok&=abs(d)<=0.01
        print(f"F4a: m={m}, fall along {name}: a = {a:.5e} vs -g(1+rm) = {pred:.5e} ({d:+.4f})",flush=True)
    dd=res[(m,'axis')]/res[(m,'body diagonal')]-1; ok&=abs(dd)<=0.01; print(f"F4a: m={m}: axis / body diagonal = {1+dd:.5f}",flush=True)
k0=(0,0.3,0); hh=1e-5
w=lambda k: np.sqrt(sum(np.sin(k[a])**2 for a in range(3))+(r*sum(1-np.cos(k[a]) for a in range(3)))**2)
w0=w(k0); wxx=(w((hh,0.3,0))-2*w0+w((-hh,0.3,0)))/hh**2; fac=w0*wxx
full=(accel(0.0,k0,(1,0,0),g,True)-accel(0.0,k0,(1,0,0),-g,True))/2
clock=(accel(0.0,k0,(1,0,0),g,False)-accel(0.0,k0,(1,0,0),-g,False))/2
ratio=full/clock; size=full/(-2*g*fac); ok&=abs(ratio/2-1)<=0.02 and abs(size-1)<=0.02
print(f"F4b: light k_y=0.3: full a_x = {full:.5e}, clock only {clock:.5e}, ratio {ratio:.4f}; full / (2 g w w_xx) = {size:.4f}")
print("F4",'PASS' if ok else 'FAIL')
