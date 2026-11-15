import numpy as np,sys; sys.path.insert(0,'.')
from flow1d import *
L=6000; tau=0.4; r=0.5; T=6000; kap=1e-5; ma,mb=0.25,0.125; sep=1200; sig=250
x=np.arange(L)-L//2; xa,xb=-sep//2,sep//2
pa=np.roll(packet(L,ma,r,sig).reshape(L,2),xa,axis=0).reshape(-1); pb=np.roll(packet(L,mb,r,sig).reshape(L,2),xb,axis=0).reshape(-1)
ha=np.zeros(L); hb=np.zeros(L); va=np.zeros(L); vb=np.zeros(L)   # h and dh/dt (flow time)
lap=lambda h: np.roll(h,1)+np.roll(h,-1)-2*h
XA=[];XB=[]
for t in range(T+1):
    qa=(np.abs(pa.reshape(L,2))**2).sum(1); qb=(np.abs(pb.reshape(L,2))**2).sum(1)
    XA.append(np.sum(qa*x)); XB.append(np.sum(qb*x))
    if t==T: break
    # field sub-steps (leapfrog), dt = tau/4
    for _ in range(4):
        dt=tau/4
        va+=dt*(lap(ha)+kap*(ma*qa-ma*qa.mean())); vb+=dt*(lap(hb)+kap*(mb*qb-mb*qb.mean()))
        ha+=dt*va; hb+=dt*vb
    Na=1-hb; Nb=1-ha   # each feels the other's field
    pa=expm_multiply(-1j*tau*build(L,ma,r,Na,Na),pa); pb=expm_multiply(-1j*tau*build(L,mb,r,Nb,Nb),pb)
    if t%1000==0: print("tick",t,flush=True)
XA=np.array(XA); XB=np.array(XB); tt=np.arange(T+1)
def acc(X,a,b): s=slice(a,b); return np.polyfit(tt[s],X[s],2)[0]*2/tau**2
pa_=+(kap*mb/2)*(1+r*ma); pb_=-(kap*ma/2)*(1+r*mb)
ba,bb=acc(XA,0,2701),acc(XB,0,2701); aa,ab=acc(XA,3700,6001),acc(XB,3700,6001)
bal=(ma*aa+mb*ab)/(ma*abs(aa)); balp=r*(ma-mb)/(1+r*ma)
print(f"before: a_a/pred={ba/pa_:+.4f} a_b/pred={bb/pb_:+.4f}")
print(f"after:  a_a/pred={aa/pa_:.4f} a_b/pred={ab/pb_:.4f}")
print(f"balance {bal:+.4f} (predicted {balp:+.4f})")
print("F1",'PASS' if abs(ba/pa_)<=0.05 and abs(bb/pb_)<=0.05 else 'FAIL',"F2",'PASS' if abs(aa/pa_-1)<=0.03 and abs(ab/pb_-1)<=0.03 else 'FAIL',"F3",'PASS' if abs(bal-balp)<=0.02 else 'FAIL')
