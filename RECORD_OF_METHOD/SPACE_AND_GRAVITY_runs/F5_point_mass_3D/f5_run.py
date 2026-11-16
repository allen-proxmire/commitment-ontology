import numpy as np,scipy.sparse as sp,sys; sys.path.insert(0,'.'); sys.path.insert(0,'../F4_three_dimensions')
from common import *
from flow3d import A as AL,B,I4,h,ring
from scipy.sparse.linalg import expm_multiply
def build(N,D):
    Ls=(Lx,Ly,Lz); I=[sp.identity(L) for L in Ls]
    def S(a):
        m=[ring(Ls[i]) if i==a else I[i] for i in range(3)]; return sp.kron(sp.kron(m[0],m[1]),m[2]).tocsr()
    Ss=[S(a) for a in range(3)]; Id=sp.identity(Lx*Ly*Lz)
    K=sum(sp.kron((Ss[a]-Ss[a].T)/(2j),AL[a]) for a in range(3))+r*sp.kron(3*Id-sum((Ss[a]+Ss[a].T)/2 for a in range(3)),B)
    Dm=sp.kron(sp.diags(np.ravel(D)),I4); return (0.5*(Dm@K+K@Dm)).tocsr()
def packet():
    kx=2*np.pi*np.fft.fftfreq(Lx); ky=2*np.pi*np.fft.fftfreq(Ly); kz=2*np.pi*np.fft.fftfreq(Lz); ph=np.zeros((Lx,Ly,Lz,4),complex)
    wr=lambda k,c:((k-c+np.pi)%(2*np.pi)-np.pi)
    for i,a in enumerate(kx):
        if abs(wr(a,0)*sig)>5: continue
        for j,b in enumerate(ky):
            if abs(wr(b,K0)*sig)>5: continue
            for l,c in enumerate(kz):
                amp=np.exp(-((wr(a,0)*sig)**2+(wr(b,K0)*sig)**2+(wr(c,0)*sig)**2)/2)
                if amp<1e-8: continue
                e,v=np.linalg.eigh(h((a,b,c),0.0,r))
                if e[3]<1e-9: continue    # k = 0: zero energy, no positive band
                P=v[:,2:]@v[:,2:].conj().T; u=P@np.array([1,0,0,0],complex)
                if np.linalg.norm(u)<0.3: u=P@np.array([0,0,1,0],complex)
                ph[i,j,l]=amp*u/np.linalg.norm(u)
    p=np.fft.ifftn(ph,axes=(0,1,2)); p=np.roll(p,(Lx//2,Ly//2+Y0,Lz//2),axis=(0,1,2)); return (p/np.linalg.norm(p)).reshape(-1)
def mean_kx(p):
    f=np.fft.fftn(p.reshape(Lx,Ly,Lz,4),axes=(0,1,2)); w=(np.abs(f)**2).sum(3); w/=w.sum()
    k=2*np.pi*np.fft.fftfreq(Lx); k=(k+np.pi)%(2*np.pi)-np.pi; return np.sum(w*k[:,None,None])
x=(np.arange(Lx)-Lx//2)[:,None,None]; y=(np.arange(Ly)-Ly//2)[None,:,None]; z=(np.arange(Lz)-Lz//2)[None,None,:]
P_=Phi(x+0*y+0*z,y+0*x+0*z,z+0*x+0*y); one=np.ones_like(P_)
p0=packet(); res={}
for label,N,D in (("none",one,one),("clock",1-P_,1-P_),("full",1-P_,(1-P_)/(1+P_))):
    q=expm_multiply(-1j*T_FLOW*build(N,D),p0); res[label]=mean_kx(q)/K0
    print(f"{label}: <k_x>/k_y = {res[label]:+.5e}",flush=True)
cl=res["clock"]-res["none"]; fu=res["full"]-res["none"]
rc_,rf_=-1.40422e-03,-2.79436e-03
print(f"deflection: clock {cl:+.5e} (rays {rc_:+.5e}, {cl/rc_-1:+.4f}); full {fu:+.5e} (rays {rf_:+.5e}, {fu/rf_-1:+.4f}); ratio {fu/cl:.4f}")
ok=abs(fu/cl-2)<=0.05 and abs(cl/rc_-1)<=0.05 and abs(fu/rf_-1)<=0.05
print("F5",'PASS' if ok else 'FAIL')
