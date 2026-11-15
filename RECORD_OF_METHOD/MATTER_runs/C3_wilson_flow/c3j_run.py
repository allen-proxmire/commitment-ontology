import numpy as np,sys; sys.path.insert(0,'.')
import c3i; c3i.r=0.5
from c3i import coeff, shells
tau=0.4; t=tau/(6*np.pi**2); R=[]
for th in [1e-3,3e-4,1e-4]:
    p,wt=shells(th,9); ZE=-4*coeff(th,tau,0,0,'E',p,wt)[1]; ZB=4*coeff(th,tau,0,1,'B',p,wt)[1]; R.append((th,ZE,ZB))
    print(f"th={th:.0e} Z_E={ZE:+.6f} Z_B={ZB:+.6f} c_ind-1={np.sqrt(ZB/ZE)-1 if ZB*ZE>0 else float('nan'):+.5f}",flush=True)
sE=(R[2][1]-R[1][1])/np.log(3); sB=(R[2][2]-R[1][2])/np.log(3)
f1=all(x[1]>0 and x[2]>0 for x in R); f2=abs(sE/t-1)<=0.05 and abs(sB/t-1)<=0.05
print(f"local slopes: Z_E {sE:.6f} ({sE/t-1:+.3f}), Z_B {sB:.6f} ({sB/t-1:+.3f})"); print("F1",'PASS' if f1 else 'FAIL',"F2",'PASS' if f2 else 'FAIL')
