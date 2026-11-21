# A wiggly grid: same neighbours everywhere, each place's hop strength uneven by a random fraction eps (H = {w, H_W}/2, w = 1 + eps*eta, eta unit normal per place).
# Massless pattern, 2D, r = 1/2. A packet of wavenumber k runs for time T; loss = share that has left the forward direction.
# Stated before running: loss goes as eps^2 (power 2.0 +/- 0.3) and as k^3 in 2D (power 3.0 +/- 0.6), the Rayleigh law; in 3D the same law is k^4.
import numpy as np
L=256; r=0.5; sig=24.0; T=150.0; dt=0.5; order=10
kx=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(kx,kx,indexing='ij')
sx,sy=np.sin(KX),np.sin(KY); M=r*(2-np.cos(KX)-np.cos(KY))
def H0(p):   # p: (2,L,L) in real space
    f=np.fft.fft2(p); g=np.empty_like(f)
    g[0]=M*f[0]+(sx-1j*sy)*f[1]; g[1]=(sx+1j*sy)*f[0]-M*f[1]
    return np.fft.ifft2(g)
def run(eps,k0,seed=1):
    rng=np.random.default_rng(seed); w=1+eps*rng.standard_normal((L,L))
    k0=2*np.pi*round(k0*L/(2*np.pi))/L
    x=np.arange(L)-L/4; X,Y=np.meshgrid(x,np.arange(L)-L/2,indexing='ij')
    env=np.exp(-(X**2+Y**2)/(4*sig**2)+1j*k0*X)
    m=r*(1-np.cos(k0)); s=np.sin(k0); E=np.hypot(s,m); u=np.array([s,E-m]); u=u/np.linalg.norm(u)   # positive-energy spinor for k along x
    p=np.array([u[0]*env,u[1]*env]); p/=np.sqrt((abs(p)**2).sum())
    for n in range(int(T/dt)):
        term=p.copy(); out=p.copy()
        for j in range(1,order+1):
            term=(-1j*dt/j)*0.5*(w*H0(term)+H0(w*term)); out=out+term
        p=out
    f=np.fft.fft2(p); P=(abs(f)**2).sum(0); P/=P.sum()
    return P[np.hypot(KX-k0,KY)<0.15].sum(), k0
base={}
print("loss of the forward packet after T = 150 hops' time (the even grid's own loss taken off):")
res=[]
for k in (0.3,0.45,0.6,0.9):
    f0,kk=run(0.0,k); base[k]=f0
    f1,_=run(0.1,k); res.append((kk,f0-f1)); print(f"  eps = 0.10, k = {kk:.3f}: loss {f0-f1:.4f}  (even grid keeps {f0:.4f}); loss/(eps^2 k^3 T) = {(f0-f1)/(0.01*kk**3*T):.2f}")
pk=np.polyfit(np.log([a for a,b in res[:3]]),np.log([b for a,b in res[:3]]),1)[0]
print(f"power of k (first three): {pk:.2f}  [{'pass' if abs(pk-3)<0.6 else 'FAIL'}]")
re=[]
for e in (0.05,0.1,0.2):
    f1,kk=run(e,0.6); re.append((e,base[0.6]-f1)); print(f"  k = {kk:.3f}, eps = {e}: loss {base[0.6]-f1:.4f}")
pe=np.polyfit(np.log([a for a,b in re]),np.log([b for a,b in re]),1)[0]
print(f"power of eps: {pe:.2f}  [{'pass' if abs(pe-2)<0.3 else 'FAIL'}]")
