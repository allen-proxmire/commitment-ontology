import numpy as np,sys; sys.path.insert(0,'.')
from flow1d import *
Lx=6000; tau=0.4; r=0.5; T=1500; x=np.arange(Lx)-Lx//2
def fall(m,g,sig):
    N=1-g*x; D=N/(1+g*x); H=build(Lx,m,r,N,D); p=packet(Lx,m,r,sig)
    xs=[]
    for t in range(T+1):
        q=(np.abs(p.reshape(Lx,2))**2).sum(1); xs.append(np.sum(q*x))
        if t<T: p=expm_multiply(-1j*tau*H,p)
    tt=np.arange(T+1); return np.polyfit(tt,xs,2)[0]*2/tau**2
res={}
for th in (0.1,0.2):
    m=th/tau; pred=1+r*m
    for sig in (150,300):
        a1=fall(m,2e-6,sig); res[(th,sig)]=a1/(2e-6*pred); print(f"theta={th} width={sig}: a/(g(1+rm)) = {res[(th,sig)]:.5f}   a/g = {a1/2e-6:.5f}",flush=True)
    a2=fall(m,4e-6,300); print(f"theta={th} width=300 g doubled: a/g ratio change = {(a2/4e-6)/(a1/2e-6)-1:+.2e}",flush=True); res[(th,'g2')]=(a2/4e-6)/(a1/2e-6)-1
a0=fall(0.25,0.0,300); print(f"g=0 sanity: a = {a0:.2e} (vs {2e-6*(1+r*0.25):.2e})")
f1=all(abs(res[(th,300)]-1)<=0.01 for th in (0.1,0.2)); f2=all(abs(res[(th,'g2')])<=0.005 for th in (0.1,0.2))
print("F1",'PASS' if f1 else 'FAIL',"F2",'PASS' if f2 else 'FAIL',"sanity",'PASS' if abs(a0)<0.01*2e-6 else 'FAIL')
