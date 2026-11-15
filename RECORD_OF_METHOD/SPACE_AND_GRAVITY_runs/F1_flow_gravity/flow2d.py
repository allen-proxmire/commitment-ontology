import numpy as np, scipy.sparse as sp
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]).astype(complex); I2=np.eye(2)
def ring(L):
    S=sp.diags([np.ones(L-1)],[1],shape=(L,L),format='lil'); S[L-1,0]=1; return S.tocsr()
def build(Lx,Ly,m,r,N,D):
    Sx=sp.kron(ring(Lx),sp.identity(Ly)); Sy=sp.kron(sp.identity(Lx),ring(Ly)); I=sp.identity(Lx*Ly)
    K=sp.kron((Sx-Sx.T)/(2j),sx)+sp.kron((Sy-Sy.T)/(2j),sy)+r*sp.kron(2*I-(Sx+Sx.T)/2-(Sy+Sy.T)/2,sz)
    Dm=sp.kron(sp.diags(D.reshape(-1)),I2)
    return (0.5*(Dm@K+K@Dm)+sp.kron(sp.diags((m*N).reshape(-1)),sz)).tocsr()
def omega(k,r,m=0.):
    return np.sqrt(np.sin(k[0])**2+np.sin(k[1])**2+(m+r*(2-np.cos(k[0])-np.cos(k[1])))**2)
def packet(Lx,Ly,m,r,k0y,sig):
    kx=2*np.pi*np.fft.fftfreq(Lx); ky=2*np.pi*np.fft.fftfreq(Ly); ph=np.zeros((Lx,Ly,2),complex)
    for i,a in enumerate(kx):
        for j,b in enumerate(ky):
            aa=(a+np.pi)%(2*np.pi)-np.pi; bb=(b+np.pi)%(2*np.pi)-np.pi
            amp=np.exp(-((aa*sig)**2+((bb-k0y)*sig)**2)/2)
            if amp<1e-10: continue
            h=np.sin(a)*sx+np.sin(b)*sy+(m+r*(2-np.cos(a)-np.cos(b)))*sz; e,v=np.linalg.eigh(h); u=v[:,1]; u=u*np.exp(-1j*np.angle(u[0])); ph[i,j]=amp*u
    p=np.fft.ifft2(ph,axes=(0,1)); p=np.roll(p,(Lx//2,Ly//2),axis=(0,1)); return (p/np.linalg.norm(p)).reshape(-1)
