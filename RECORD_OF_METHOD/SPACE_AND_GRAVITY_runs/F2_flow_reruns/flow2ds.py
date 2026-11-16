import numpy as np, scipy.sparse as sp
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]).astype(complex); I2=np.eye(2)
def ring(L):
    S=sp.diags([np.ones(L-1)],[1],shape=(L,L),format='lil'); S[L-1,0]=1; return S.tocsr()
def build(Lx,Ly,m,r,N,D,bx=None,by=None):
    """H = 1/2{D,K} + sz m N + 1/2{bx, sin kx} + 1/2{by, sin ky}; site index i*Ly+j, x=i, y=j."""
    Sx=sp.kron(ring(Lx),sp.identity(Ly)); Sy=sp.kron(sp.identity(Lx),ring(Ly)); I=sp.identity(Lx*Ly)
    snx=(Sx-Sx.T)/(2j); sny=(Sy-Sy.T)/(2j)
    K=sp.kron(snx,sx)+sp.kron(sny,sy)+r*sp.kron(2*I-(Sx+Sx.T)/2-(Sy+Sy.T)/2,sz)
    Dm=sp.kron(sp.diags(np.ravel(D)),I2); H=0.5*(Dm@K+K@Dm)+sp.kron(sp.diags(np.ravel(m*N)),sz)
    for b,s in ((bx,snx),(by,sny)):
        if b is None: continue
        B=sp.diags(np.ravel(b)); H=H+sp.kron(0.5*(B@s+s@B),I2)
    return H.tocsr()
def eig_u(a,b,m,r):
    h=np.sin(a)*sx+np.sin(b)*sy+(m+r*(2-np.cos(a)-np.cos(b)))*sz; e,v=np.linalg.eigh(h); u=v[:,1]; return u*np.exp(-1j*np.angle(u[0]))
def packet(Lx,Ly,m,r,k0,sig,c0=None):
    """positive-energy Gaussian packet, momentum k0=(kx,ky), width sig, centred at c0 (offset from lattice centre)."""
    kx=2*np.pi*np.fft.fftfreq(Lx); ky=2*np.pi*np.fft.fftfreq(Ly); ph=np.zeros((Lx,Ly,2),complex)
    for i,a in enumerate(kx):
        aa=(a-k0[0]+np.pi)%(2*np.pi)-np.pi
        if abs(aa*sig)>6: continue
        for j,b in enumerate(ky):
            bb=(b-k0[1]+np.pi)%(2*np.pi)-np.pi
            amp=np.exp(-((aa*sig)**2+(bb*sig)**2)/2)
            if amp<1e-10: continue
            ph[i,j]=amp*eig_u(a,b,m,r)
    p=np.fft.ifft2(ph,axes=(0,1)); sh=(Lx//2,Ly//2) if c0 is None else (Lx//2+int(c0[0]),Ly//2+int(c0[1]))
    p=np.roll(p,sh,axis=(0,1)); return (p/np.linalg.norm(p)).reshape(-1)
def dens(p,Lx,Ly): return (np.abs(p.reshape(Lx,Ly,2))**2).sum(2)
def mean_k(p,Lx,Ly,k0=(0.,0.)):
    """mean momentum, each component wrapped around the reference k0"""
    f=np.fft.fft2(p.reshape(Lx,Ly,2),axes=(0,1)); w=(np.abs(f)**2).sum(2); w/=w.sum()
    kx=2*np.pi*np.fft.fftfreq(Lx)[:,None]; ky=2*np.pi*np.fft.fftfreq(Ly)[None,:]
    wx=(kx-k0[0]+np.pi)%(2*np.pi)-np.pi+k0[0]; wy=(ky-k0[1]+np.pi)%(2*np.pi)-np.pi+k0[1]
    return np.sum(w*wx), np.sum(w*wy)
def centre(q,L,axis):
    """circular mean position along an axis, offset from lattice centre"""
    s=q.sum(1-axis) if q.ndim==2 else q; th=2*np.pi*np.arange(L)/L; z=np.sum(s*np.exp(1j*th))
    return (np.angle(z)%(2*np.pi))*L/(2*np.pi)-L//2
