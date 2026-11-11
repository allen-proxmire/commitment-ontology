"""C3 check: totals of a G4 solution against band quantities.
J_i total = E v_i (energy current); P_ij total = E v_i v_j (symmetric momentum flux)."""
import sys, itertools, numpy as np
d=int(sys.argv[1]); R=int(sys.argv[2]); m=float(sys.argv[3]); variant=sys.argv[4]
sys.argv=['x',str(d),str(R),str(m),variant]
src=open('g4_matter_coupling.py').read().split('t0 = time.time()')[0]
exec(src)
u=np.load(f'g4_sol_d{d}_R{R}_m{m}_{variant}.npy')
def kern(o,k,kp):
    P=patch(o); K=np.zeros((n,n),complex)
    for a in P:
        for b in P:
            blk=np.array([[u[var[(o,a,b,al,be)]] for be in range(n)] for al in range(n)])
            K+=np.exp(-1j*np.dot(k,a))*blk*np.exp(1j*np.dot(kp,b))
    return K
def Hk(k): return sum(hd*np.exp(1j*np.dot(k,disp)) for disp,hd in h.items())
rng=np.random.default_rng(0); worst=0; worstE=0
for t in range(20):
    k=rng.uniform(-np.pi,np.pi,d); w,U=np.linalg.eigh(Hk(k)); eps=1e-6
    for bnd in range(n):
        uu=U[:,bnd]; E=w[bnd]
        v=[]
        for i in range(d):
            dk=np.zeros(d); dk[i]=eps
            v.append((np.linalg.eigh(Hk(k+dk))[0][bnd]-np.linalg.eigh(Hk(k-dk))[0][bnd])/(2*eps))
        worstE=max(worstE,abs(uu.conj()@kern(('E',),k,k)@uu-E))
        for i in range(d):
            Ji=uu.conj()@kern(('J',i),k,k)@uu; worst=max(worst,abs(Ji-E*v[i]))
            for j in range(i,d):
                o=('P',i,j)
                if o not in objs: continue
                Pij=uu.conj()@kern(o,k,k)@uu
                worst=max(worst,abs(Pij-E*v[i]*v[j]))
print(f'd={d} R={R} m={m} {variant}: max |E-E_band| {worstE:.2e}; max |J - E v|, |P - E v v| over bands {worst:.2e}')
