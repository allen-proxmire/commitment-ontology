# A curved web: does a pattern bend by gravity's amount when a mass's geometry is put into the hop lengths?
# Weak field of a mass (softened), in a plane through it: hop length a = 1 + kap/rho, clock rate N = 1 - kap/rho, rho = sqrt(r^2 + s^2), kap = r_s/2.
# Step (P7f's form): H = {w, H_W}/2 with w = N/a; massless, 2D, r = 1/2. Three cases: lengths only (w = 1/a), clock only (w = N), both.
# The answer to check against is the light ray's own bending in the index n = 1/w (ray equation integrated from the same start, over the same times).
# Stated before running: each case's turn within 5% of its ray's; both together twice the lengths-only turn within 5%.
import numpy as np, sys
L=320; r=0.5; sig=12.0; dt=0.5; order=10; T=240.0; kap=1.5; s=5.0; b=40.0; x0=-120.0; k0=0.3
g=np.arange(L)-L/2; x,y=np.meshgrid(g,g,indexing='ij'); rho=np.sqrt(x**2+y**2+s**2)
kk=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(kk,kk,indexing='ij'); sx,sy=np.sin(KX),np.sin(KY); M=r*(2-np.cos(KX)-np.cos(KY))
def H0(p):
    f=np.fft.fft2(p); o=np.empty_like(f); o[0]=M*f[0]+(sx-1j*sy)*f[1]; o[1]=(sx+1j*sy)*f[0]-M*f[1]; return np.fft.ifft2(o)
def wfun(case,X,Y):
    rh=np.sqrt(X**2+Y**2+s**2); a=1+kap/rh; N=1-kap/rh
    return {"lengths only":1/a,"clock only":N,"both":N/a,"even":np.ones_like(rh)}[case]
def ray(case,t1,t2):
    pos=np.array([x0,b]); v=np.array([1.0,0.0]); h=0.02; t=0.0; hd={}
    def grad_n(P):
        e=1e-4; n=lambda q:1/wfun(case,q[0],q[1]); return np.array([(n(P+[e,0])-n(P-[e,0]))/(2*e),(n(P+[0,e])-n(P-[0,e]))/(2*e)]),n(P)
    while t<t2+h:
        for tt in (t1,t2):
            if abs(t-tt)<h/2: hd[tt]=np.degrees(np.arctan2(v[1],v[0]))
        gn,n=grad_n(pos); gp=gn-v*(v@gn); v=v+h*gp/n**2; v/=np.linalg.norm(v); pos=pos+h*v/n; t+=h
    return hd[t2]-hd[t1]
def run(case):
    w=wfun(case,x,y); m=r*(1-np.cos(k0)); sn=np.sin(k0); E=np.hypot(sn,m); u=np.array([sn,E-m]); u/=np.linalg.norm(u)
    env=np.exp(-((x-x0)**2+(y-b)**2)/(4*sig**2)+1j*k0*x); p=np.array([u[0]*env,u[1]*env]); p/=np.sqrt((abs(p)**2).sum()); tr=[]
    for n in range(int(T/dt)+1):
        if n%10==0:
            d=(abs(p)**2).sum(0); d/=d.sum(); tr.append((n*dt,(d*x).sum(),(d*y).sum()))
        term=p.copy(); acc=p.copy()
        for j in range(1,order+1): term=(-1j*dt/j)*0.5*(w*H0(term)+H0(w*term)); acc=acc+term
        p=acc
    tr=np.array(tr); head=lambda ta,tb: np.degrees(np.arctan2(*np.polyfit(tr[(tr[:,0]>=ta)&(tr[:,0]<=tb),0],tr[(tr[:,0]>=ta)&(tr[:,0]<=tb),2],1)[:1],np.polyfit(tr[(tr[:,0]>=ta)&(tr[:,0]<=tb),0],tr[(tr[:,0]>=ta)&(tr[:,0]<=tb),1],1)[0]))
    turn=float(head(T-40,T)-head(0,40)); return turn,tr[-1]
res={}
for case in ("even","lengths only","clock only","both"):
    turn,end=run(case); rt=ray(case,20.0,T-20.0) if case!="even" else 0.0; res[case]=(turn,rt)
    print(f"{case}: pattern's heading turns {turn:+.3f} degrees; the ray's {rt:+.3f}"+(f"; pattern over ray {turn/rt:.3f}" if rt else "")+f"; ends at ({end[1]:.1f}, {end[2]:.1f})",flush=True)
print(f"both over lengths only: {res['both'][0]/res['lengths only'][0]:.3f}; clock only over lengths only: {res['clock only'][0]/res['lengths only'][0]:.3f}")
