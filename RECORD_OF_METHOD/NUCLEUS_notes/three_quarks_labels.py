# Two desk questions on three quarks in one whole.
# 1. With colour's part fixed (antisymmetric, the neutral three) and the three sharing one orbital, the rest of the labels must be symmetric under swaps.
#    Which wholes are there with a kind label alone (up/down), and with a kind label and a spin (two two-way labels)?
# 2. Is "a dressed quark each, plus a spin-spin term" enough for the eight lightest baryon families?
#    M = sum m_i + A sum_{i<j} S_i.S_j / (m_i m_j), three numbers (m_u, m_s, A) against eight masses (isospin averages, MeV).
import numpy as np, itertools
from scipy.optimize import least_squares
def sym_space(d):
    n=d**3; P=np.zeros((n,n))
    for p in itertools.permutations(range(3)):
        for idx in itertools.product(range(d),repeat=3):
            j=[idx[p[k]] for k in range(3)]; P[np.ravel_multi_index(j,(d,)*3),np.ravel_multi_index(idx,(d,)*3)]+=1/6
    w,v=np.linalg.eigh(P); return v[:,w>0.5]
sx=np.array([[0,1],[1,0]])/2; sy=np.array([[0,-1j],[1j,0]])/2; sz=np.array([[1,0],[0,-1]])/2; I2=np.eye(2)
def total_sq(ops,d):            # (sum over the three quarks of a one-quark vector operator)^2
    T=0
    for o in ops:
        parts=[]
        for i in range(3):
            m=[np.eye(d)]*3; m[i]=o; parts.append(np.kron(np.kron(m[0],m[1]),m[2]))
        S=sum(parts); T=T+S@S
    return T
V=sym_space(2); K2=V.conj().T@total_sq([sx,sy,sz],2)@V
print("1. kind label alone: symmetric wholes:",V.shape[1],"; total kind-spin T(T+1) =",sorted(set(np.round(np.linalg.eigvalsh(K2),6))),"(3.75 = T 3/2: uuu, uud, udd, ddd, the all-alike family; no T = 1/2)")
V=sym_space(4); spin=[np.kron(o,I2) for o in (sx,sy,sz)]; kind=[np.kron(I2,o) for o in (sx,sy,sz)]
S2=V.conj().T@total_sq(spin,4)@V; T2=V.conj().T@total_sq(kind,4)@V; w=np.linalg.eigvalsh(S2+10*T2); from collections import Counter
c=Counter(np.round(w,4)); print("   kind and spin: symmetric wholes:",V.shape[1],"; (S(S+1) + 10 T(T+1)) : count =",dict(sorted(c.items())),"(8.25 = S 1/2, T 1/2: 4 states, proton and neutron; 41.25 = S 3/2, T 3/2: 16 states)")
data={"N":938.9,"Lambda":1115.7,"Sigma":1193.2,"Xi":1318.3,"Delta":1232.0,"Sigma*":1384.6,"Xi*":1533.4,"Omega":1672.5}
def model(p):
    u,s,A=p; return {"N":3*u-0.75*A/u**2,"Delta":3*u+0.75*A/u**2,"Lambda":2*u+s-0.75*A/u**2,"Sigma":2*u+s+A*(0.25/u**2-1/(u*s)),"Sigma*":2*u+s+A*(0.25/u**2+0.5/(u*s)),
                     "Xi":2*s+u+A*(0.25/s**2-1/(u*s)),"Xi*":2*s+u+A*(0.25/s**2+0.5/(u*s)),"Omega":3*s+0.75*A/s**2}
f=least_squares(lambda p:[(model(p)[k]-data[k])/data[k] for k in data],[360,540,2.6e7]); u,s,A=f.x; m=model(f.x)
print(f"2. fit: m_u = {u:.0f} MeV, m_s = {s:.0f} MeV, A/m_u^2 = {A/u**2:.0f} MeV")
for k in data: print(f"   {k:7s} measured {data[k]:7.1f}  model {m[k]:7.1f}  off by {100*(m[k]-data[k])/data[k]:+.1f}%")
print(f"   largest miss {max(abs(m[k]-data[k])/data[k] for k in data)*100:.1f}%; eight masses, three numbers; proton's share: quarks {3*u:.0f}, spin term {-0.75*A/u**2:.0f}")
