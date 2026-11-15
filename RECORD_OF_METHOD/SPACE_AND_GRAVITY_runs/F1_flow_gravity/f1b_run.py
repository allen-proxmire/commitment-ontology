import numpy as np,sys; sys.path.insert(0,'.')
from flow2d import *
from scipy.sparse.linalg import expm_multiply
Lx,Ly=400,256; tau=0.4; r=0.5; T=150; k0=0.3; sig=30
X=(np.arange(Lx)-Lx//2)[:,None]*np.ones((1,Ly))
def run(g):
    N=1-g*X; D=N/(1+g*X); H=build(Lx,Ly,0.0,r,N,D); p=packet(Lx,Ly,0.0,r,k0,sig); xs=[]
    for t in range(T+1):
        q=(np.abs(p.reshape(Lx,Ly,2))**2).sum(2); xs.append(np.sum(q*X))
        if t<T: p=expm_multiply(-1j*tau*H,p)
    return np.polyfit(np.arange(T+1),xs,2)[0]*2/tau**2
ap=run(1e-4); am=run(-1e-4); a=(ap-am)/2
h=1e-4; k=np.array([0.,k0]); w0=omega(k,r); wxx=(omega(k+[h,0],r)-2*w0+omega(k-[h,0],r))/h**2; fac=w0*wxx
print(f"a_x (odd part) / g = {a/1e-4:.5f};  lattice factor omega*omega_xx = {fac:.5f};  a_x/(2g*factor) = {a/(2e-4*fac):.5f}")
print("F1",'PASS' if abs(a/(2e-4*fac)-1)<=0.02 else 'FAIL')
