import numpy as np,sys; sys.path.insert(0,'.')
from flow1d import *
Lx=6000; tau=0.4; r=0.5; T=1500; x=np.arange(Lx)-Lx//2; m=0.25
def fall(g,k0):
    N=1-g*x; D=N/(1+g*x); H=build(Lx,m,r,N,D); p=packet(Lx,m,r,300,k0); xs=[]
    for t in range(T+1):
        q=(np.abs(p.reshape(Lx,2))**2).sum(1); xs.append(np.sum(q*x))
        if t<T: p=expm_multiply(-1j*tau*H,p)
    return np.polyfit(np.arange(T+1),xs,2)[0]*2/tau**2
ad=(fall(2e-6,np.pi)-fall(-2e-6,np.pi))/2; pred=(4*r+m)*(1-r*(2*r+m))/(2*r+m)
print(f"extra species: a/g = {ad/2e-6:.5f}, prediction {pred:.5f}, ratio {ad/2e-6/pred:.5f}")
am=(fall(2e-6,0.0)-fall(-2e-6,0.0))/2; print(f"matter (reference): a/g = {am/2e-6:.5f}, prediction {1+r*m:.5f}")
print("F1",'PASS' if abs(ad/2e-6/pred-1)<=0.02 else 'FAIL')
