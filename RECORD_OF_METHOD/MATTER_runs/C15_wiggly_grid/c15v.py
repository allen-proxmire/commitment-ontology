# Does the pattern follow light's rays or the step's own, where rays can be trusted? A smooth field with no core:
# w = 1 + 0.036 sin(2 pi y/256) (the step {w, H_W}/2, massless, 2D, r = 1/2), packet k = 0.3, 12 hops wide, launched along x where the gradient is largest.
# The wave's turn against a bundle of light's rays (at the group speed) and a bundle of the step's own rays (H = w E_W(k)). Not registered.
import numpy as np
L=256; r=0.5; sig=12.0; dt=0.5; order=10; T=150.0; k0=0.3; amp=0.036
g=np.arange(L)-L/2; x,y=np.meshgrid(g,g,indexing='ij'); w=1+amp*np.sin(2*np.pi*y/L)
kk=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(kk,kk,indexing='ij'); sx,sy=np.sin(KX),np.sin(KY); M=r*(2-np.cos(KX)-np.cos(KY))
def H0(p):
    f=np.fft.fft2(p); o=np.empty_like(f); o[0]=M*f[0]+(sx-1j*sy)*f[1]; o[1]=(sx+1j*sy)*f[0]-M*f[1]; return np.fft.ifft2(o)
def head(tr,ta,tb):
    m=(tr[:,0]>=ta)&(tr[:,0]<=tb); return np.degrees(np.arctan2(np.polyfit(tr[m,0],tr[m,2],1)[0],np.polyfit(tr[m,0],tr[m,1],1)[0]))
x0=-70.0
m=r*(1-np.cos(k0)); sn=np.sin(k0); E=np.hypot(sn,m); u=np.array([sn,E-m]); u/=np.linalg.norm(u)
env=np.exp(-((x-x0)**2+y**2)/(4*sig**2)+1j*k0*x); p=np.array([u[0]*env,u[1]*env]); p/=np.sqrt((abs(p)**2).sum()); tr=[]
for n in range(int(T/dt)+1):
    if n%10==0:
        d=(abs(p)**2).sum(0); d/=d.sum(); xs=np.angle((d*np.exp(2j*np.pi*x/L)).sum())*L/(2*np.pi); tr.append((n*dt,xs,(d*y).sum()))
    term=p.copy(); acc=p.copy()
    for j in range(1,order+1): term=(-1j*dt/j)*0.5*(w*H0(term)+H0(w*term)); acc=acc+term
    p=acc
tr=np.array(tr); tr[:,1]=np.unwrap(tr[:,1]*2*np.pi/L)*L/(2*np.pi); wave=head(tr,T-30,T)-head(tr,0,30)
def EW(k): return np.sqrt(np.sin(k[:,0])**2+np.sin(k[:,1])**2+r**2*(2-np.cos(k[:,0])-np.cos(k[:,1]))**2)
def dEW(k):
    E=EW(k); mm=r**2*(2-np.cos(k[:,0])-np.cos(k[:,1])); return np.stack([(np.sin(k[:,0])*np.cos(k[:,0])+mm*np.sin(k[:,0]))/E,(np.sin(k[:,1])*np.cos(k[:,1])+mm*np.sin(k[:,1]))/E],1)
def bundle(light,seed,n_rays=40000,h=0.25):
    rng=np.random.default_rng(seed); P=np.stack([x0+sig*rng.standard_normal(n_rays),sig*rng.standard_normal(n_rays)],1); K=np.array([k0,0.0])+rng.standard_normal((n_rays,2))/(2*sig); t=[]
    for i in range(int(T/h)+1):
        if i%20==0: t.append((i*h,P[:,0].mean(),P[:,1].mean()))
        ww=1+amp*np.sin(2*np.pi*P[:,1]/L); gy=amp*2*np.pi/L*np.cos(2*np.pi*P[:,1]/L)
        if light: kn=np.linalg.norm(K,axis=1)[:,None]; v=0.964*K/kn; En=0.964*kn[:,0]
        else: v=dEW(K); En=EW(K)
        K[:,1]-=h*En*gy; P=P+h*ww[:,None]*v
    t=np.array(t); return head(t,T-30,T)-head(t,0,30)
li=np.mean([bundle(True,s) for s in range(3)]); st=np.mean([bundle(False,s) for s in range(3)])
print(f"wave turns {wave:+.3f} degrees; light's rays {li:+.3f}; the step's own rays {st:+.3f}; wave over light's {wave/li:.3f}; wave over the step's {wave/st:.3f}")
