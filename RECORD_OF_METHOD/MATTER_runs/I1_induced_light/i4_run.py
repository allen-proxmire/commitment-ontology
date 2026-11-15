import numpy as np,sys; sys.path.insert(0,'.')
from i4 import *
w=5*np.pi/16; c0=2*np.cos(w); sp={}
for th in [1e-3,3e-3,1e-2,3e-2]:
    p,wt=shells(th,9); L=np.log(1/th)
    eps=[-4*coeff(th,w,j,j,'E',p,wt) for j in range(3)]
    D={}
    for i in range(3):
        for j in range(3):
            if i==j: continue
            ZB=4*coeff(th,w,i,j,'B',p,wt); c=np.sqrt(ZB/eps[j]) if ZB*eps[j]>0 else np.nan; D[(i,j)]=2*L*(c/c0-1)
            print(f"th={th:.0e} prop={'xyz'[i]} pol={'xyz'[j]} Z_B={ZB:+.5f} eps_pol={eps[j]:+.5f} c/c0-1={c/c0-1:+.5f} D={D[(i,j)]:+.4f}",flush=True)
    v=np.array(list(D.values())); sp[th]=np.nanmax(v)-np.nanmin(v)
    print(f"th={th:.0e} eps(x,y,z)=({eps[0]:+.5f},{eps[1]:+.5f},{eps[2]:+.5f})  spread of D={sp[th]:.4f}",flush=True)
s1,s3=sp[1e-3],sp[3e-2]
print("outcome:", 'ANISOTROPIC' if s1>0.01 and s1>=0.5*s3 else ('ISOTROPIC' if s1<0.01 else 'INCONCLUSIVE'))
