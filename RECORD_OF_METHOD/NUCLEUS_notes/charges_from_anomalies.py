# One generation of left-handed Weyl fields, colour count Nc; solve gauge + gravitational anomaly conditions
# for hypercharges with y_L = -1/2 (electron charge -1). Fields: Q(Nc,2,yQ), u^c(Nc*,1,yu), d^c(Nc*,1,yd), L(1,2,yL), e^c(1,1,ye)
import numpy as np
from scipy.optimize import fsolve
def conds(v,Nc):
    yQ,yu,yd,ye=v; yL=-0.5
    return [2*yQ+yu+yd,                                  # SU(Nc)^2 U(1)
            Nc*yQ+yL,                                    # SU(2)^2 U(1)
            2*Nc*yQ+Nc*yu+Nc*yd+2*yL+ye,                 # gravity^2 U(1)
            2*Nc*yQ**3+Nc*(yu**3+yd**3)+2*yL**3+ye**3]   # U(1)^3
for Nc in [1,3,5]:
    sols=set()
    for g in np.random.default_rng(0).normal(size=(40,4)):
        s,info,ier,_=fsolve(conds,g,args=(Nc,),full_output=True)
        if ier==1 and max(abs(np.array(conds(s,Nc))))<1e-10: sols.add(tuple(np.round(s,6)))
    for yQ,yu,yd,ye in sols:
        Qu,Qd=0.5+yQ,-0.5+yQ
        print(f"Nc={Nc}: yQ={yQ}, u^c={yu}, d^c={yd}, e^c={ye} -> Q_u={Qu:.4f}, Q_d={Qd:.4f}, Q_u-Q_d={Qu-Qd}, nucleon(uud for Nc=3)-type charges: proton={(Nc+1)/2*Qu+(Nc-1)/2*Qd:.4f}")
