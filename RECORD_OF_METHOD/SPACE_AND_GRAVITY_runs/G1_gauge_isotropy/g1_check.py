"""G1 post-run check: the Fierz-Pauli (linearised Einstein-Hilbert) cost lies in the cubic solution space,
and every member of that space propagates tensor waves isotropically."""
import numpy as np
exec(open('g1_gauge_isotropy.py').read().split("for name,g in")[0])
eta=np.diag([-1,1,1,1.])
def QFP(H,k):
    hu=eta@H@eta; ku=eta@k; k2=k@ku; tr=np.trace(eta@H)
    v=ku@H
    return 0.5*(k2*np.sum(H*hu) - 2*(v@eta@v) + 2*tr*(ku@H@ku) - k2*tr**2)
null=solve(cubic,1500)
X=[];y=[]
for _ in range(2000):
    H=sym(rng.normal(size=(4,4))); k=rng.normal(size=4); X.append(feat(H,k)); y.append(QFP(H,k))
X=np.array(X); y=np.array(y)
B=X@null.T; coef,res,_,_=np.linalg.lstsq(B,y,rcond=None)
print('cubic space dim',len(null),' FP fit relative residual',np.linalg.norm(B@coef-y)/np.linalg.norm(y))
# gauge check of FP itself
H=sym(rng.normal(size=(4,4)));k=rng.normal(size=4);xi=rng.normal(size=4);dH=np.outer(k,xi)+np.outer(xi,k)
print('FP gauge change',QFP(H+dH,k)-QFP(H,k))
# isotropy of random members
for t in range(3):
    c=rng.normal(size=len(null))@null
    sp=[tt_speeds(c,d) for d in ([1,0,0],[1,1,0],[1,1,1],[1,2,3])]
    print('random member speeds by direction',sp)
c=coef@null
print('FP member speeds',[tt_speeds(c,d) for d in ([1,0,0],[1,1,1],[1,2,3])])
