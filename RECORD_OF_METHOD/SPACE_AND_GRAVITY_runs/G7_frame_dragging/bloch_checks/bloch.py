import numpy as np
w=0.3; I2=np.eye(2); sx=np.array([[0,1],[1,0]],complex)
R=np.cos(np.pi/4)*I2-1j*np.sin(np.pi/4)*sx; Rd=R.conj().T
def F(a): return np.cos(a)*I2-1j*np.sin(a)*sx
# 2-site cell along y (sites 0,1), Bloch momentum K for the cell (cell length 2); basis (site, spin)
def Ay2(K):
    # A_y = R S+(down) F(w) S-(up)... replicate g6 Ay on real space: p=Rd p; p=F(-w)p; p[1]=roll(p[1],-1) (p1(y)<-p1(y+1)); p=F(w)p; p0(y)<-p0(y-1); p=R p
    def shift(comp,d):  # new[y]=old[y+d] on 2-site cell with Bloch K (cell length 2, momentum per site k=K/2)
        M=np.zeros((4,4),complex)
        for y in range(2):
            ys=y+d; cell=ys//2; s=ys%2
            M[2*y+comp,2*s+comp]=np.exp(1j*K*cell)
        for y in range(2):
            for c in range(2):
                if c!=comp: M[2*y+c,2*y+c]=1
        return M
    big=lambda m: np.kron(I2,m)
    return big(R)@shift(0,-1)@big(F(w))@shift(1,1)@big(F(-w))@big(Rd)
def Ax(kx):
    return np.diag([np.exp(-1j*kx),1])@F(w)@np.diag([1,np.exp(1j*kx)])@F(-w)
def layer(K,b,par):
    M=np.eye(4,dtype=complex); c=np.cos(b/2); s=np.sin(b/2)
    if par==0: # link site0-site1 within cell
        blk=np.array([[c,-s],[s,c]]); M=np.kron(blk,I2)
    else: # link site1 -> site0 of next cell
        M=np.zeros((4,4),complex)
        ph=np.exp(1j*K)
        # new a(site1)= c a1 - s a0(next); new a0(next)= s a1 + c a0(next)  => in Bloch: a0 gets ph^-1 factor
        for sp in range(2):
            M[2+sp,2+sp]=c; M[2+sp,0+sp]=-s*ph
            M[0+sp,0+sp]=c; M[0+sp,2+sp]=s/ph
    return M
def U(K,kx,th,b,pal=False):
    Axk=np.kron(I2,Ax(kx)); W=Axk@Ay2(K)@np.kron(I2,F(th))@Ay2(K)@Axk
    E=layer(K,b,0); O=layer(K,b,1)
    C=O@E
    if pal: return C@W@(E@O) if False else (E@O)@W@C
    return C@W@C
def bands(K,kx,th,b,pal=False):
    return np.sort(np.angle(np.linalg.eigvals(U(K,kx,th,b,pal))))
# check unitarity and b=0 vs folded 1-site dispersion
import sys
sys.path.insert(0,'/dev/null')
for pal in (False,True):
  print("pal",pal)
  for b in [0.02,0.4]:
    for th in [0.4]:
        h=1e-4
        # matter at rest: lowest positive band near +th; velocity dE/dk_site = 2 dE/dK
        def e(K):
            ev=bands(K,0,th,b,pal); return ev[np.argmin(abs(ev-th))]
        v=(e(h)-e(-h))/(2*h)*2
        print(f" b={b} th={th}: drift {-v:+.5f}? 2sinb={2*np.sin(b):.5f} 2b={2*b:.5f}  unitary err {np.abs(U(0.3,0.1,th,b,pal)@U(0.3,0.1,th,b,pal).conj().T-np.eye(4)).max():.1e}")
