import numpy as np,sys; sys.path.insert(0,'.')
from c3i import *
tau=0.4; rows=[]
for th in [1e-3,3e-3,1e-2,3e-2]:
    p,wt=shells(th,9)
    ZE=-4*coeff(th,tau,0,0,'E',p,wt)[1]; ZB=4*coeff(th,tau,0,1,'B',p,wt)[1]
    ci=np.sqrt(ZB/ZE) if ZB*ZE>0 else np.nan; rows.append((th,ZE,ZB))
    print(f"th={th:.0e} Z_E={ZE:+.6f} Z_B={ZB:+.6f} c_ind/tau-1={ci/tau-1:+.5f}",flush=True)
    if th==1e-2:
        ez=-4*coeff(th,tau,2,2,'E',p,wt)[1]; Bzx=4*coeff(th,tau,2,0,'B',p,wt)[1]
        print(f"  cube check: eps_z-eps_x={ez-ZE:+.2e}  Z_B(z,x)-Z_B(x,y)={Bzx-ZB:+.2e}",flush=True)
R=np.array(rows); L=np.log(1/R[:,0]); sE=np.polyfit(L,R[:,1],1)[0]; sB=np.polyfit(L,R[:,2],1)[0]
tE,tB=1/(6*np.pi**2*tau),tau/(6*np.pi**2)
print(f"slopes: Z_E {sE:.5f} (LL {tE:.5f}, {sE/tE-1:+.3f}); Z_B {sB:.6f} (LL {tB:.6f}, {sB/tB-1:+.3f})")
print("F1",'PASS' if R[0,1]>0 and R[0,2]>0 else 'FAIL',"F2",'PASS' if abs(sE/tE-1)<=0.1 and abs(sB/tB-1)<=0.1 else 'FAIL')
