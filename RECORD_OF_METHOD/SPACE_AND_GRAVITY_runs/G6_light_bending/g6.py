import numpy as np
# 2D palindromic Wilson walk: U = Ax Ay F(theta N) Ay Ax.  Ax = Sx+ F(w) Sx- F(-w) (hops in sigma_z basis);
# Ay = R (same along y) R^dag, R = exp(-i pi/4 sigma_x): hops along y in the sigma_y basis; flips stay sigma_x.
# Field along x: lapse N = 1 - g x, hop stretch psi (= the standard conformal factor squared) = 1 + g x. Rule: 2 cos w(x) = c0 * N/psi (light's local speed); mass flip theta*N.
Lx,Ly=400,256; w0=0.3; c0=2*np.cos(w0)
x=(np.arange(Lx)-Lx//2)[:,None]*np.ones((1,Ly))
sx=np.array([[0,1],[1,0]],complex); I2=np.eye(2)
R=np.cos(np.pi/4)*I2-1j*np.sin(np.pi/4)*sx; Rd=R.conj().T
def Fop(p,a):
    c=np.cos(a); s=np.sin(a); u,d=p; return np.array([c*u-1j*s*d, c*d-1j*s*u])
def mat(M,p): return np.array([M[0,0]*p[0]+M[0,1]*p[1], M[1,0]*p[0]+M[1,1]*p[1]])
def Ax(p,w): p=Fop(p,-w); p=np.array([p[0],np.roll(p[1],-1,0)]); p=Fop(p,w); return np.array([np.roll(p[0],1,0),p[1]])
def Ay(p,w):
    p=mat(Rd,p); p=Fop(p,-w); p=np.array([p[0],np.roll(p[1],-1,1)]); p=Fop(p,w); p=np.array([np.roll(p[0],1,1),p[1]]); return mat(R,p)
def step(p,w,ang): return Ax(Ay(Fop(Ay(Ax(p,w),w),ang),w),w)
def F(a): return np.cos(a)*I2-1j*np.sin(a)*sx
def Uk(kx,ky,th,w):
    Ax_=np.diag([np.exp(-1j*kx),1])@F(w)@np.diag([1,np.exp(1j*kx)])@F(-w)
    Ay_=R@np.diag([np.exp(-1j*ky),1])@F(w)@np.diag([1,np.exp(1j*ky)])@F(-w)@Rd
    return Ax_@Ay_@F(th)@Ay_@Ax_
def E(kx,ky,th,w): return np.sort(np.abs(np.angle(np.linalg.eigvals(Uk(kx,ky,th,w)))))[0]
def packet(th,k0y,sig):
    kx=2*np.pi*np.fft.fftfreq(Lx); ky=2*np.pi*np.fft.fftfreq(Ly)
    phi=np.zeros((2,Lx,Ly),complex)
    for i,a in enumerate(kx):
        for j,b in enumerate(ky):
            bb=(b+np.pi)%(2*np.pi)-np.pi
            amp=np.exp(-((a*sig)**2+((bb-k0y)*sig)**2)/2)
            if amp<1e-10: continue
            ev,V=np.linalg.eig(Uk(a,b,th,w0)); phi[:,i,j]=amp*V[:,np.argmin(np.angle(ev))]
    p=np.array([np.fft.ifft2(phi[0]),np.fft.ifft2(phi[1])])
    p=np.roll(p,(Lx//2,Ly//2),axis=(1,2)); return p/np.sqrt(np.sum(abs(p)**2))
def run(th,k0y,g,kap,sig=30,T=150):   # early single-sign version, not used by g6_final; np.clip hides a failed arccos
    N=1-g*x; psi=1+kap*g*x
    w=np.arccos(np.clip(c0*N/psi/2,-1,1)); ang=th*N
    p=packet(th,k0y,sig); xs=[];ys=[]
    for t in range(T+1):
        q=np.sum(abs(p)**2,0); xs.append(np.sum(q*x)); ys.append(np.sum(q*np.arange(Ly)[None,:]))
        p=step(p,w,ang)
    t=np.arange(T+1); a=np.polyfit(t,xs,2)[0]*2
    return a, np.polyfit(t,np.unwrap(np.array(ys)/Ly*2*np.pi)*Ly/(2*np.pi),1)[0]
