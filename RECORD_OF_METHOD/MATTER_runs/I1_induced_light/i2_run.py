import numpy as np,sys; sys.path.insert(0,'.')
from i2 import *
w=5*np.pi/16; c0=2*np.cos(w); rows=[]
for th in [1e-3,3e-3,1e-2,3e-2,0.1,0.3]:
    p,wt=shells(th,12); r={}
    for f in 'BE':
        qs=[th/20,th/10]; cs=[C(q,th,w,f,p,wt)/(2*np.sin(q/2))**2 for q in qs]; qh=[(2*np.sin(q/2))**2 for q in qs]
        r[f]=cs[0]+(cs[0]-cs[1])*qh[0]/(qh[1]-qh[0])
    ZE=-4*r['E']; ZB=4*r['B']; ci=np.sqrt(ZB/ZE) if ZB*ZE>0 else float('nan')
    rows.append((th,ZE,ZB)); print(f"th={th:.0e} Z_E={ZE:+.5e} Z_B={ZB:+.5e} c_ind={ci:.5f} c_ind/c0-1={ci/c0-1:+.4f}",flush=True)
R=np.array(rows); sel=R[:,0]<=3e-2; L=np.log(1/R[sel,0])
sE,iE=np.polyfit(L,R[sel,1],1); sB,iB=np.polyfit(L,R[sel,2],1)
tE,tB=1/(6*np.pi**2*c0),c0/(6*np.pi**2)
print(f"slope Z_E={sE:.5f} (leading log {tE:.5f}, {sE/tE-1:+.3f}); slope Z_B={sB:.5f} (leading log {tB:.5f}, {sB/tB-1:+.3f}); intercepts Z_E {iE:+.4f} Z_B {iB:+.4f}")
f1=R[0,1]>0 and R[0,2]>0; f2=abs(sE/tE-1)<=0.1 and abs(sB/tB-1)<=0.1
print("F1",'PASS' if f1 else 'FAIL',"F2",'PASS' if f2 else 'FAIL')
