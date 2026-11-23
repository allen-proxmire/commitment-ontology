# Where does the neutral pattern's energy sit? c16's chain (N = 10, bare mass 0): the lowest neutral level's energy above the vacuum, split into
#   the field (the which-way field's energy, (g^2/2) sum L^2), the charges' motion (the hop sigma_x sin k), and the lifting term (r(1 - cos k) sigma_z).
# Each part is the difference of its expectation between the level and the vacuum; the three add to the gap. Not registered.
import numpy as np, scipy.sparse as sp, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import c16
N=10; ch=c16.Chain(N); r0=c16.r; c16.r=0.0; Hkin=c16.Chain(N).Hhop; c16.r=r0; Hlift_hop=ch.Hhop-Hkin
for g in (0.5,0.75,1.0):
    w,v=ch.low(0.0,g,k=3); fld=0.5*g*g*(ch.Lcum**2).sum(1); site=r0*ch.sz
    def parts(x):
        p=abs(x)**2; return np.array([(p*fld).sum(), np.vdot(x,Hkin@x).real, (p*site).sum()+np.vdot(x,Hlift_hop@x).real])
    d=parts(v[:,1])-parts(v[:,0]); gap=w[1]-w[0]
    print(f"g = {g}: gap {gap:.4f} = field {d[0]:+.4f} + motion {d[1]:+.4f} + lifting term {d[2]:+.4f} (sum {d.sum():.4f});  shares: field {100*d[0]/gap:.0f}%, motion {100*d[1]/gap:.0f}%, lifting term {100*d[2]/gap:.0f}%",flush=True)
    v0=parts(v[:,0]); print(f"        in the vacuum itself: field {v0[0]:.4f}, motion {v0[1]:.4f}, lifting term {v0[2]:.4f}")
