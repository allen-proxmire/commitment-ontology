import numpy as np,sys; sys.path.insert(0,'../I1_induced_light')
from i2 import Ak,Fb,bd,od,mul,const,shells
from i4 import coeff
from scipy.linalg import schur
def shift_dir(k,q,th,w,n):
    k=np.array(k,float); k2=k+q*np.array(n)
    def Uf(kk): return Ak(0,kk[0],w)@Ak(1,kk[1],w)@Ak(2,kk[2],w)@Fb(th)@Ak(2,kk[2],w)@Ak(1,kk[1],w)@Ak(0,kk[0],w)
    U=const(bd(Uf(k),Uf(k2))); D=(np.eye(8,dtype=complex), od(-1j/4,np.eye(4)), -np.eye(8)/32)
    U0,U1,U2=mul(mul(D,U),D); T,V=schur(U0,output='complex'); lam=np.diag(T); A1=V.conj().T@U1@V; A2=V.conj().T@U2@V
    F=np.angle(lam)<0; tot=0.
    for i in np.where(F)[0]:
        d=lam[i]-lam; m=(np.abs(d)>1e-12)&~F; tot+=np.imag((A2[i,i]+np.sum(A1[i,m]*A1[m,i]/d[m]))/lam[i])
    return tot
def coeff_dir(th,w,n,p,wt):
    qs=np.array([th/20,th/10,th/5]); qh=(2*np.sin(qs/2))**2
    Cs=np.array([sum(t*shift_dir(kk,q,th,w,n) for kk,t in zip(p,wt))/(2*np.pi)**3 for q in qs])
    return np.linalg.solve(np.vstack([np.ones(3),qh,qh**2]).T,Cs)[1]
th=0.01; p,wt=shells(th,9)
print("(1) off-diagonal permittivity, w=5pi/16",flush=True)
w=5*np.pi/16; ea=[-4*coeff(th,w,j,j,'E',p,wt) for j in range(3)]; print("  axes",np.round(ea,6),flush=True)
for (i,j) in [(0,1),(0,2),(1,2)]:
    n=np.zeros(3); n[i]=n[j]=1/np.sqrt(2); en=-4*coeff_dir(th,w,n,p,wt)
    print(f"  eps_{'xyz'[i]}{'xyz'[j]} = {en-0.5*(ea[i]+ea[j]):+.2e}  (eps along diagonal {en:.6f})",flush=True)
print("(2) other w",flush=True)
for w in (0.95,1.10):
    e=[-4*coeff(th,w,j,j,'E',p,wt) for j in range(3)]; By=4*coeff(th,w,0,2,'B',p,wt); Bz=4*coeff(th,w,0,1,'B',p,wt)
    print(f"  w={w}: eps=({e[0]:+.5f},{e[1]:+.5f},{e[2]:+.5f}) eps_z-eps_x={e[2]-e[0]:+.4f} eps_y-eps_x={e[1]-e[0]:+.4f}  Z_B(B_y)={By:+.5f} Z_B(B_z)={Bz:+.5f} B offset={By-Bz:+.4f}",flush=True)
