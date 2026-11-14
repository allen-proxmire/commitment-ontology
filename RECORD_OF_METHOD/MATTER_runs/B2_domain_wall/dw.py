import numpy as np
# CO's 2D palindromic walk on a strip: x periodic (momentum k), inner direction s a ring of 2L places.
# U = Ax As F(theta(s)) As Ax, As hops along s in the sigma_y basis (as Ay in g6.py).
# Domain wall: theta(s)=th_in for s<L, th_out for s>=L.
sx=np.array([[0,1],[1,0]],complex); I2=np.eye(2)
R=np.cos(np.pi/4)*I2-1j*np.sin(np.pi/4)*sx; Rd=R.conj().T
def F(a): return np.cos(a)*I2-1j*np.sin(a)*sx
def kron_s(M,n): return np.kron(np.eye(n),M)          # same 2x2 on every s
def shift_up(n):   # component 0 moves s -> s+1 (ring)
    S=np.zeros((2*n,2*n),complex)
    for s in range(n):
        S[2*((s+1)%n),2*s]=1; S[2*s+1,2*s+1]=1
    return S
def shift_dn(n):   # component 1 moves s -> s-1
    S=np.zeros((2*n,2*n),complex)
    for s in range(n):
        S[2*s,2*s]=1; S[2*((s-1)%n)+1,2*s+1]=1
    return S
def Ustrip(k,ths,w,ws=None):
    n=len(ths); ws=w if ws is None else ws
    Ax=np.diag([np.exp(-1j*k),1])@F(w)@np.diag([1,np.exp(1j*k)])@F(-w)
    AX=kron_s(Ax,n)
    Wp=np.zeros((2*n,2*n),complex); Wm=np.zeros((2*n,2*n),complex)
    for s in range(n):
        wsv=ws[s] if np.ndim(ws) else ws
        Wp[2*s:2*s+2,2*s:2*s+2]=F(wsv); Wm[2*s:2*s+2,2*s:2*s+2]=F(-wsv)
    AS=kron_s(R,n)@shift_up(n)@Wp@shift_dn(n)@Wm@kron_s(Rd,n)
    FT=np.zeros((2*n,2*n),complex)
    for s,t in enumerate(ths): FT[2*s:2*s+2,2*s:2*s+2]=F(t)
    return AX@AS@FT@AS@AX
def bulkE(kx,ky,th,w):
    Ax=np.diag([np.exp(-1j*kx),1])@F(w)@np.diag([1,np.exp(1j*kx)])@F(-w)
    Ay=R@np.diag([np.exp(-1j*ky),1])@F(w)@np.diag([1,np.exp(1j*ky)])@F(-w)@Rd
    return np.angle(np.linalg.eigvals(Ax@Ay@F(th)@Ay@Ax))
