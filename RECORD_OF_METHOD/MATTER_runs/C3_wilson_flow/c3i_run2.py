import numpy as np,sys; sys.path.insert(0,'.')
from c3i import *
tau=0.4; t=tau/(6*np.pi**2); R=[]
for th in [1e-4,3e-4]:
    p,wt=shells(th,9); ZE=-4*coeff(th,tau,0,0,'E',p,wt)[1]; ZB=4*coeff(th,tau,0,1,'B',p,wt)[1]; R.append((th,ZE,ZB))
    print(f"th={th:.0e} Z_E={ZE:+.6f} Z_B={ZB:+.6f} c_ind-1={np.sqrt(ZB/ZE)-1:+.5f}",flush=True)
dL=np.log(3); sE=(R[0][1]-R[1][1])/dL; sB=(R[0][2]-R[1][2])/dL
print(f"local slopes: Z_E {sE:.6f} ({sE/t-1:+.3f}), Z_B {sB:.6f} ({sB/t-1:+.3f}) against {t:.6f}")
print("PASS" if abs(sE/t-1)<=0.05 and abs(sB/t-1)<=0.05 else "FAIL")
