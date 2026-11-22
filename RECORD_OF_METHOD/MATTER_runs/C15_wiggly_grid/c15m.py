# Uneven hop to hop, yet flat: strengths along x depending on x only, along y on y only (a relabelling of the lines; curvature zero, c15l).
# Same step, measure and size of unevenness as c15a (2D, massless, r = 1/2, eps = 0.1, T = 150), where independent unevenness lost 0.0196 (k = 0.295) and 0.1677 (k = 0.589).
# Not registered. Question: is flat hop-scale unevenness felt?
import numpy as np
L=256; r=0.5; sig=24.0; T=150.0; dt=0.5; order=10; eps=0.1
kx=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(kx,kx,indexing='ij')
def part(p,i):      # the hops along line i: sigma_i sin k_i + r (1 - cos k_i) sigma_z
    f=np.fft.fft2(p); K=(KX,KY)[i]; s=np.sin(K); m=r*(1-np.cos(K)); g=np.empty_like(f)
    if i==0: g[0]=m*f[0]+s*f[1]; g[1]=s*f[0]-m*f[1]
    else:    g[0]=m*f[0]-1j*s*f[1]; g[1]=1j*s*f[0]-m*f[1]
    return np.fft.ifft2(g)
def run(k0,wx,wy):
    k0=2*np.pi*round(k0*L/(2*np.pi))/L; x=np.arange(L)-L/4; X,Y=np.meshgrid(x,np.arange(L)-L/2,indexing='ij')
    env=np.exp(-(X**2+Y**2)/(4*sig**2)+1j*k0*X); m=r*(1-np.cos(k0)); s=np.sin(k0); E=np.hypot(s,m); u=np.array([s,E-m]); u/=np.linalg.norm(u)
    p=np.array([u[0]*env,u[1]*env]); p/=np.sqrt((abs(p)**2).sum())
    H=lambda q: 0.5*(wx*part(q,0)+part(wx*q,0)+wy*part(q,1)+part(wy*q,1))
    for n in range(int(T/dt)):
        term=p.copy(); out=p.copy()
        for j in range(1,order+1): term=(-1j*dt/j)*H(term); out=out+term
        p=out
    P=(abs(np.fft.fft2(p))**2).sum(0); P/=P.sum(); return k0,P[np.hypot(KX-k0,KY)<0.15].sum()
rng=np.random.default_rng(1); one=np.ones((L,L))
wx=np.repeat(1+eps*rng.standard_normal((L,1)),L,1); wy=np.repeat(1+eps*rng.standard_normal((1,L)),L,0)
for k in (0.3,0.6):
    k0,f0=run(k,one,one); k0,f1=run(k,wx,wy); print(f"k = {k0:.3f}: forward share kept on the even grid {f0:.4f}, on the flat uneven one {f1:.4f}; loss {f0-f1:.4f}",flush=True)
