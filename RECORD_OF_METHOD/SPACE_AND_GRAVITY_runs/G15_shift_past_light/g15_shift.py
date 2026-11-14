# Strong-field route through the shift alone (Painleve-Gullstrand form: N = 1, flat slices, gravity in the drift).
# At w = 5pi/16 light runs at c0 = 1.111 hops/step, while the directed hop's drift reaches 2 sin b <= 2: can the shift reach and pass c,
# with light's cone tilted by the drift and matter carried at it? 1D walk + conveyor brickwork; packets; uniform b.
import numpy as np
L=4096; w=5*np.pi/16; c0=2*np.cos(w)
sx=np.array([[0,1],[1,0]],complex); F=lambda a: np.cos(a)*np.eye(2)-1j*np.sin(a)*sx
def Uk(k,th):
    A=np.diag([np.exp(-1j*k),1])@F(w)@np.diag([1,np.exp(1j*k)])@F(-w); return A@F(th)@A
def Fop(p,a): c=np.cos(a); s=np.sin(a); u,d=p; return np.array([c*u-1j*s*d, c*d-1j*s*u])
def A(p): p=Fop(p,-w); p=np.array([p[0],np.roll(p[1],-1)]); p=Fop(p,w); return np.array([np.roll(p[0],1),p[1]])
def conv(p,b):
    cb,sb=np.cos(b/2),np.sin(b/2)
    for par in (0,1):
        a=p[:,par::2].copy(); c=np.roll(p,-1,axis=1)[:,par::2].copy()
        q=p.copy(); q[:,par::2]=cb*a-sb*c; t=np.roll(q,-1,axis=1); t[:,par::2]=sb*a+cb*c; p=np.roll(t,1,axis=1)
    return p
def step(p,th,b): return conv(A(Fop(A(conv(p,b)),th)),b)
def packet(th,k0,sig):
    ks=2*np.pi*np.fft.fftfreq(L); phi=np.zeros((L,2),complex)
    for i,k in enumerate(ks):
        kk=(k-k0+np.pi)%(2*np.pi)-np.pi; a=np.exp(-(kk*sig)**2/2)
        if a<1e-12: continue
        ev,v=np.linalg.eig(Uk(k,th)); phi[i]=a*v[:,np.argmin(np.angle(ev))]
    p=np.array([np.fft.ifft(phi[:,0]),np.fft.ifft(phi[:,1])]); return np.roll(p,L//2,axis=1)/np.sqrt(np.sum(abs(phi)**2)/L)
ph=np.exp(2j*np.pi*np.arange(L)/L)
def vel(th,k0,b,T=300):
    p=packet(th,k0,40); p/=np.sqrt(np.sum(abs(p)**2)); ys=[]
    for t in range(T+1):
        q=np.sum(abs(p)**2,0); ys.append(np.angle(np.sum(q*ph))); p=step(p,th,b)
    ys=np.unwrap(ys)*L/(2*np.pi); return np.polyfit(np.arange(T+1),ys,1)[0]
print("c0 =",c0)
for b in [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.5]:
    vp=vel(0,0.1,b); vm=vel(0,-0.1,b); vm0=vel(0.3,0.0,b)
    print(f"b={b}: drift 2 sin b = {2*np.sin(b):.3f} ({2*np.sin(b)/c0:.2f} c0); light +: {vp:+.3f}, light -: {vm:+.3f} (tilt {(vp+vm)/2:+.3f}, half-width {(vp-vm)/2:.3f}); matter drift {vm0:+.3f}")
