"""Staggered one-component walk on the 2x2x2 cell in CO's palindromic form.
Checks: Dirac continuum (alpha_j), doublers, chiral remnant beta U beta = U^dag,
taste degeneracy, massive limiting speed, per-cell SU(2) vs cross-cell swaps.
See OPEN_DIRECTIONS_notes/how_patterns_combine.md (discrete-time check)."""
import numpy as np, itertools
from scipy.linalg import expm
X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1.,-1]).astype(complex); I=np.eye(2)
k3=lambda a,b,c: np.kron(np.kron(a,b),c)
ax,ay,az,be=k3(X,I,I),k3(Z,X,I),k3(Z,Z,X),k3(Z,Z,Z); alph=[ax,ay,az]
tau=[k3(I,X,Y),k3(X,Y,I),k3(X,Z,Y)]
B=list(itertools.product([0,1],repeat=3)); idx={b:i for i,b in enumerate(B)}
def Pin(j):
    M=np.zeros((8,8),complex)
    for b in B:
        if b[j]==0:
            c=list(b);c[j]=1;c=tuple(c);e=(-1)**sum(b[:j])
            M[idx[c],idx[b]]+=1j*e; M[idx[b],idx[c]]+=-1j*e
    return M
def Pout(j,q):
    M=np.zeros((8,8),complex)
    for b in B:
        if b[j]==1:
            c=list(b);c[j]=0;c=tuple(c);e=(-1)**sum(b[:j])
            a=1j*e*np.exp(1j*q[j]); M[idx[c],idx[b]]+=a; M[idx[b],idx[c]]+=np.conj(a)
    return M
def U(q,th,thm):
    A=[expm(-0.5j*th*Pin(j))@expm(-1j*th*Pout(j,q))@expm(-0.5j*th*Pin(j)) for j in range(3)]
    F=expm(-1j*thm*be)
    return A[0]@A[1]@A[2]@F@A[2]@A[1]@A[0]
D=lambda q: np.diag([np.exp(1j*np.dot(q,b)/2) for b in B])   # site-phase relabel (site momentum q/2)
def comm(Uq,ops): return max(np.linalg.norm(o@Uq-Uq@o) for o in ops)

# --- section 1: continuum, doublers, degeneracy
for th in [np.pi/4, 0.5, 0.3]:
    print("theta",round(th,3))
    rng=np.random.default_rng(0)
    q=rng.normal(size=3)*0.7
    Uq=U(q,th,0.2)
    print("  unitary:",np.allclose(Uq.conj().T@Uq,np.eye(8)))
    print("  [tau,U] cell-phase:",round(comm(Uq,tau),4)," site-phase:",round(comm(Uq,[D(q).conj().T@t@D(q) for t in tau]),4), " other order:",round(comm(Uq,[D(q)@t@D(q).conj().T for t in tau]),4))
    # continuum: effective H slope at q->0, massless
    d=1e-4; 
    for j in range(3):
        qq=np.zeros(3);qq[j]=d
        Heff=1j*(U(qq,th,0)-U(-qq,th,0))/(2*d)
        # compare to alpha_j up to scale
        c=np.trace(Heff@alph[j]).real/8
        print("  axis",j,"slope ∝ alpha_j:",np.allclose(Heff,c*alph[j],atol=1e-6),"speed",round(c,4))
    # doublers: massless quasi-energy zeros across zone
    g=np.linspace(-np.pi,np.pi,25,endpoint=False); zeros=[]
    for q in itertools.product(g,repeat=3):
        ev=np.angle(np.linalg.eigvals(U(np.array(q),th,0)))
        if np.min(np.minimum(abs(ev),abs(abs(ev)-np.pi)))<1e-6: zeros.append((np.round(q,3),int(sum(abs(ev)<1e-6)),int(sum(abs(abs(ev)-np.pi)<1e-6))))
    print("  gapless points (q, #E=0, #E=pi):",zeros)
    # degeneracy at random q, massive
    print("  spectrum (massive):",np.round(np.sort(np.angle(np.linalg.eigvals(U(rng.normal(size=3),th,0.2)))),4))

# --- section: dt3.py
rng=np.random.default_rng(3)
for th in [0.3,0.5]:
    q=rng.normal(size=3); U0=U(q,th,0)
    print("theta",th," chiral remnant beta U beta = U^dag (m=0):",np.allclose(be@U0@be,U0.conj().T), " with mass:",np.allclose(be@U(q,th,0.2)@be,U(q,th,0.2).conj().T))
    # fine scan of gap away from q=0, massless
    g=np.linspace(-np.pi,np.pi,41); best=[]
    for qq in itertools.product(g,repeat=3):
        qq=np.array(qq); 
        if np.linalg.norm(qq)<0.6: continue
        ev=np.angle(np.linalg.eigvals(U(qq,th,0)))
        best.append((min(np.min(abs(ev)),np.min(np.pi-abs(ev))),tuple(np.round(qq,2))))
    best.sort(); print("  smallest quasi-energy distance to 0 or pi away from q=0:",best[:3])
    # taste operators (site-phase) commutator scaling in q
    u=np.array([0.3,0.5,0.8])
    for s in [0.2,0.1,0.05]:
        qq=u*s; Uq=U(qq,th,0.2)
        print("  |q|",s," [tau_site,U]:",round(comm(Uq,[D(qq).conj().T@t@D(qq) for t in tau]),6))

# --- section: dt4.py
def vmax(th,thm,u):
    u=np.array(u,float);u/=np.linalg.norm(u)
    ks=np.linspace(1e-3,np.pi,1500)
    E=[np.sort(np.abs(np.angle(np.linalg.eigvals(U(k*u,th,thm)))))[0] for k in ks]
    v=np.gradient(E,ks); return v.max(), np.abs(v[:5]).mean()
for th in [0.3,0.5]:
    v0,c0=vmax(th,0,[1,0,0]); print("theta",th,"massless slope c0",round(c0,5),"massless max v",round(v0,5))
    for thm in [0.02,0.01,0.005]:
        for u in ([1,0,0],[1,1,1]):
            vm,_=vmax(th,thm,u); print("  thm",thm,"dir",u," (vmax_m - c0)/c0 =",f"{(vm-c0)/c0:.2e}", " /thm",f"{(vm-c0)/c0/thm:.3f}")

# --- section: q2.py
T=[k3(I,Y,X),k3(Y,X,I),k3(Y,Z,X)]
print("Pauli algebra:",np.allclose(T[0]@T[1],1j*T[2]) or np.allclose(T[0]@T[1],-1j*T[2]))
rng=np.random.default_rng(5)
for n,t in zip(["IYX","YXI","YZX"],T):
    q=rng.normal(size=3); Uq=U(q,0.4,0.2)
    print(n,"[t,Pin]:",[np.allclose(t@Pin(j),Pin(j)@t) for j in range(3)],"[t,beta]",np.allclose(t@be,be@t),"[t,Pout(q)]",[np.allclose(t@Pout(j,q),Pout(j,q)@t) for j in range(3)],"[t,U]:",np.allclose(t@Uq,Uq@t))
print("relation to tau:",[np.allclose(T[i],tau[i]) for i in range(3)])
