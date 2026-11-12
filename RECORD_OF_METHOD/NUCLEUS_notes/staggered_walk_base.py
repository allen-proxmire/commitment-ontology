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
