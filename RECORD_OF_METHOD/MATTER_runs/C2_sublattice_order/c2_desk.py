import numpy as np, itertools
# Does "nesting order chosen by sublattice" define a unitary step? Test W = sum_s U_{order_s} P_s on a 6^3 ring, s = (x+y+z) mod 3.
I2=np.eye(2); Z2=np.zeros((2,2)); s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z2,si],[si,Z2]]) for si in s]; beta=np.block([[I2,Z2],[Z2,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
def Fb(a): return np.cos(a)*np.eye(4)-1j*np.sin(a)*beta
N=6; L=N**3; w=5*np.pi/16; th=0.3
idx=lambda x,y,z: ((x%N)*N+(y%N))*N+(z%N)
def shift(j,d):
    S=np.zeros((L,L))
    for x,y,z in itertools.product(range(N),repeat=3):
        t=[x,y,z]; t[j]+=d; S[idx(*t),idx(x,y,z)]=1
    return S
I_L=np.eye(L)
def A(j):
    Sp=np.kron(shift(j,1),Pp[j])+np.kron(I_L,Pm[j]); Sm=np.kron(I_L,Pp[j])+np.kron(shift(j,-1),Pm[j])
    return Sp@np.kron(I_L,Fb(w))@Sm@np.kron(I_L,Fb(-w))
Aj=[A(j) for j in range(3)]; Ft=np.kron(I_L,Fb(th))
def U(o): a,b,c=o; return Aj[a]@Aj[b]@Aj[c]@Ft@Aj[c]@Aj[b]@Aj[a]
orders=[(0,1,2),(1,2,0),(2,0,1)]
sub=np.array([(x+y+z)%3 for x,y,z in itertools.product(range(N),repeat=3)])
P=[np.kron(np.diag((sub==k).astype(float)),np.eye(4)) for k in range(3)]
W=sum(U(orders[k])@P[k] for k in range(3))
print("U(xyz) unitary:",np.abs(U(orders[0]).conj().T@U(orders[0])-np.eye(4*L)).max())
print("W = sum_s U_s P_s unitary? max|W^dag W - I| =",np.abs(W.conj().T@W-np.eye(4*L)).max())
print("singular values of W: min",np.linalg.svd(W,compute_uv=False).min()," max",np.linalg.svd(W,compute_uv=False).max())
