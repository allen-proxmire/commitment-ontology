import numpy as np
# 1D: pure stretch field (lapse 1), light's local speed c0/psi set via the Wilson flip: 2 cos w(z) = c0/(1+g z).
# Slow matter at rest should feel no push at first order (GR). Each field at +g and -g; linear response = odd part.
# Here psi is the hop stretch (route factor), the standard conformal factor squared.
L=8000; w0=0.3; c0=2*np.cos(w0); z=np.arange(L)-L//2
def Fop(p,a): c=np.cos(a); s=np.sin(a); u,d=p; return np.array([c*u-1j*s*d, c*d-1j*s*u])
def A(p,w): p=Fop(p,-w); p=np.array([p[0],np.roll(p[1],-1)]); p=Fop(p,w); return np.array([np.roll(p[0],1),p[1]])
def step(p,w,ang): return A(Fop(A(p,w),ang),w)
sx=np.array([[0,1],[1,0]]); F=lambda a: np.cos(a)*np.eye(2)-1j*np.sin(a)*sx
def Uk(k,th,w):
    Ak=np.diag([np.exp(-1j*k),1])@F(w)@np.diag([1,np.exp(1j*k)])@F(-w); return Ak@F(th)@Ak
def packet(th,sig):
    ks=2*np.pi*np.fft.fftfreq(L); phi=np.zeros((2,L),complex)
    for i,k in enumerate(ks):
        a=np.exp(-(k*sig)**2/2)
        if a<1e-12: continue
        ev,V=np.linalg.eig(Uk(k,th,w0)); phi[:,i]=a*V[:,np.argmin(np.angle(ev))]
    p=np.roll(np.array([np.fft.ifft(phi[0]),np.fft.ifft(phi[1])]),L//2,axis=1); return p/np.sqrt(np.sum(abs(p)**2))
def acc(th,sig,g,lapse,stretch,T=1500):
    N=1-lapse*g*z; ps=1+stretch*g*z; w=np.arccos(c0*N/ps/2); p=packet(th,sig); xs=[]
    for t in range(T+1):
        xs.append(np.sum(np.sum(abs(p)**2,0)*z)); p=step(p,w,th*N)
    return 2*np.polyfit(np.arange(T+1),xs,2)[0]
g=2e-6
def odd(th,sig,la,st): return (acc(th,sig,g,la,st)-acc(th,sig,-g,la,st))/2/(g*c0**2)
for th in [0.1,0.2,0.4]:
    for sig in [150,300,600]:
        print(f"theta={th} sig={sig}: pure stretch {odd(th,sig,0,1):+.5f}   clock {odd(th,sig,1,0):.4f}   clock+stretch {odd(th,sig,1,1):.4f}")
