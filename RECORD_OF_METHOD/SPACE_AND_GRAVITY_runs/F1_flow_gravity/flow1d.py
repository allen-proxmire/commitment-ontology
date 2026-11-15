import numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
# 1D flow step with P7f restated: H = 1/2{D,K} + sz m N, K = sx sin k + sz r (1 - cos k), D = N/psi^2
sx=np.array([[0,1],[1,0]],complex); sz=np.diag([1.,-1]).astype(complex); I2=np.eye(2)
def build(Lx,m,r,N,D):
    S=sp.diags([np.ones(Lx-1)],[1],shape=(Lx,Lx),format='csr').tolil(); S[Lx-1,0]=1; S=S.tocsr()   # (S psi)(x)=psi(x+1)
    sin_=(S-S.T)/(2j); omc=sp.identity(Lx)-(S+S.T)/2
    K=sp.kron(sin_,sx)+r*sp.kron(omc,sz); Dm=sp.kron(sp.diags(D),I2)
    return (0.5*(Dm@K+K@Dm)+sp.kron(sp.diags(m*N),sz)).tocsr()
def packet(Lx,m,r,sig,k0=0.0):
    ks=2*np.pi*np.fft.fftfreq(Lx); ph=np.zeros((Lx,2),complex)
    for i,k in enumerate(ks):
        kk=(k+np.pi)%(2*np.pi)-np.pi; amp=np.exp(-((kk-k0)*sig)**2/2)
        if amp<1e-12: continue
        h=np.sin(k)*sx+(r*(1-np.cos(k))+m)*sz; e,v=np.linalg.eigh(h); u=v[:,1]; u=u*np.exp(-1j*np.angle(u[0])) if abs(u[0])>1e-12 else u; ph[i]=amp*u   # smooth gauge
    p=np.fft.ifft(ph,axis=0); p=np.roll(p,Lx//2,axis=0); return (p/np.linalg.norm(p)).reshape(-1)
