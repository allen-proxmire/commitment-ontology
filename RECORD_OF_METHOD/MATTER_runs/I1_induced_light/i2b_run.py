import numpy as np,sys; sys.path.insert(0,'.')
from i2 import *
w=5*np.pi/16; c0=2*np.cos(w)
def Uk(k,th):
    return Ak(0,k[0],w)@Ak(1,k[1],w)@Ak(2,k[2],w)@Fb(th)@Ak(2,k[2],w)@Ak(1,k[1],w)@Ak(0,k[0],w)
def filled(k,th):
    e=np.angle(np.linalg.eigvals(Uk(k,th))); return e[e<0].sum()
ZE=dict((float(l.split()[0][3:]),float(l.split()[1][4:])) for l in open('i2_out.txt') if l.startswith('th='))
rows=[]
for th in [1e-3,3e-3,1e-2,3e-2,0.1,0.3]:
    p,wt=shells(th,12)
    qs=np.array([th/20,th/10,th/5]); qh=(2*np.sin(qs/2))**2
    Cs=np.array([C(q,th,w,'B',p,wt) for q in qs])
    X=np.vstack([np.ones(3),qh,qh**2]).T; C0,c2,c4=np.linalg.solve(X,Cs)
    h=1e-3; off=sum(wt_*(filled(k+[0,h,0],th)-2*filled(k,th)+filled(k-[0,h,0],th))/h**2 for k,wt_ in zip(p,wt))/(2*np.pi)**3/4
    ZB=4*c2; ze=ZE[th]; ci=np.sqrt(ZB/ze) if ZB*ze>0 else float('nan')
    rows.append((th,ze,ZB))
    print(f"th={th:.0e} C0(fit)={C0:+.4e} C0(direct, constant A on same grid)={off:+.4e} ratio={C0/off if off else 0:.4f}  Z_B={ZB:+.5e} Z_E={ze:+.5e} c_ind={ci:.5f} c_ind/c0-1={ci/c0-1:+.4f}",flush=True)
R=np.array(rows); sel=R[:,0]<=3e-2; L=np.log(1/R[sel,0])
sE,iE=np.polyfit(L,R[sel,1],1); sB,iB=np.polyfit(L,R[sel,2],1); tE,tB=1/(6*np.pi**2*c0),c0/(6*np.pi**2)
print(f"slope Z_E={sE:.5f} (leading log {tE:.5f}, {sE/tE-1:+.3f}); slope Z_B={sB:.5f} (leading log {tB:.5f}, {sB/tB-1:+.3f}); intercepts Z_E {iE:+.4f} Z_B {iB:+.4f}")
print("F1",'PASS' if R[0,1]>0 and R[0,2]>0 else 'FAIL',"F2",'PASS' if abs(sE/tE-1)<=0.1 and abs(sB/tB-1)<=0.1 else 'FAIL')
