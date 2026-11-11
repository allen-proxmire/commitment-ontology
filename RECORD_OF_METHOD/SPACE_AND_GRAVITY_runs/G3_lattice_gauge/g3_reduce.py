"""G3 step 2: remove costs that vanish identically (the monomial basis is redundant, c_j^2 + s_j^2/4 = 1),
leaving the genuinely distinct invariant costs."""
import numpy as np
exec(open('g3_lattice_gauge.py').read().split("nf=len(AB)")[0])
null=np.load('g3_null.npy'); rng=np.random.default_rng(7)
F=[]
for n in range(9000):
    kv=rng.uniform(-np.pi,np.pi,4); kv[0]=rng.normal(); h=rng.normal(size=10); F.append(feat(h,kv))
F=np.array(F)
vals=F@null.T                       # each invariant cost evaluated at samples
sv=np.linalg.svd(vals,compute_uv=False)
rank=int(np.sum(sv>1e-8*sv[0]))
print('invariant costs found',len(null),' genuinely distinct (rank on samples):',rank)
U,S,Vt=np.linalg.svd(vals,full_matrices=False)
basis=(Vt[:rank]@null)               # coefficient vectors of distinct costs
np.save('g3_basis.npy',basis)
