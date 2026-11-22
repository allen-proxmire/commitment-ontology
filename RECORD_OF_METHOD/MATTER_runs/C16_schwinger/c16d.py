# String breaking on the step. Two held charges, +1 and -1, are set d links apart in the middle of a chain of 10 places (c16's model, g = 1):
# with nothing else there, the which-way field between them is a string of energy (g^2/2) d. The step's own charges are free to answer.
# Two cases: charges with no bare mass (m = 0), and heavy ones (m = 0.8), for which making a pair costs about 2m and the string should hold
# until (g^2/2) d passes that, near d = 4m/g^2 = 3, then break.
# Not registered. Expected: m = 0.8: energy near the bare string's for d <= 2, levelling off beyond about 4, the field in the middle dropping from near 1 toward 0.
# m = 0: levelling off within a link or two.
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from c16 import Chain
N=10; g=1.0; ch=Chain(N); q=None
occ=np.array([(ch.b>>i)&1 for i in range(2*N)]).T.astype(float); q=occ[:,0::2]+occ[:,1::2]-1          # charge at each place
def ground(m,l0vec):
    dg=(m+0.5)*ch.sz+0.5*g*g*((ch.Lcum+l0vec[None,:])**2).sum(1); H=ch.Hhop+sp.diags(dg)
    w,v=spl.eigsh(H,k=1,which='SA',tol=1e-8); p=abs(v[:,0])**2
    return w[0],(p[:,None]*(ch.Lcum+l0vec[None,:])).sum(0),(p[:,None]*q).sum(0)
for m in (0.0,0.8):
    E0,_,_=ground(m,np.zeros(N-1)); print(f"bare mass m = {m}:")
    for d in range(1,8):
        a=(N-1-d)//2; l0=np.zeros(N-1); l0[a:a+d]=1.0            # string on links a..a+d-1: held +1 just left of link a (after place a), held -1 after place a+d
        E,F,Q=ground(m,l0); mid=F[a+d//2] if d%2 else 0.5*(F[a+d//2-1]+F[a+d//2])
        cloudL=Q[max(a-1,0):a+2].sum(); cloudR=Q[a+d-1:a+d+2].sum() if d>2 else float('nan')
        print(f"   d = {d}: energy {E-E0:.3f} (bare string {0.5*g*g*d:.2f}); field at the string's middle {mid:+.2f}; step's charge gathered at the + end {cloudL:+.2f}"+(f", at the - end {cloudR:+.2f}" if d>2 else ""),flush=True)
