# Does a zone-edge (doubler) packet convert into the light species when it meets a hop-scale event?
# 1D palindromic walk (w=0.3), packet in the doubler band near k = pi, a single place with an extra flip alpha (a local event).
import numpy as np
L=4000; w=0.3; z=np.arange(L)
sx=np.array([[0,1],[1,0]],complex); F=lambda a: np.cos(a)*np.eye(2)-1j*np.sin(a)*sx
def Uk(k,th):
    A=np.diag([np.exp(-1j*k),1])@F(w)@np.diag([1,np.exp(1j*k)])@F(-w); return A@F(th)@A
def Fop(p,a): c=np.cos(a); s=np.sin(a); u,d=p; return np.array([c*u-1j*s*d, c*d-1j*s*u])
def A(p): p=Fop(p,-w); p=np.array([p[0],np.roll(p[1],-1)]); p=Fop(p,w); return np.array([np.roll(p[0],1),p[1]])
def step(p,ang): return A(Fop(A(p),ang))
ks=2*np.pi*np.fft.fftfreq(L)
def band_vectors(th):
    V=np.zeros((L,2,2),complex); E=np.zeros((L,2))
    for i,k in enumerate(ks):
        ev,v=np.linalg.eig(Uk(k,th)); o=np.argsort(-np.angle(ev)); V[i]=v[:,o]; E[i]=-np.angle(ev)[o]
    return V,E
def run(th,alpha,k0,sig=60,T=1500,x0=1000,xd=2000):
    V,E=band_vectors(th)
    amp=np.exp(-(((ks-k0+np.pi)%(2*np.pi)-np.pi)*sig)**2/2)*np.exp(-1j*ks*x0)
    phi=V[:,:,0]*amp[:,None]                      # one band
    p=np.array([np.fft.ifft(phi[:,0]),np.fft.ifft(phi[:,1])]); p/=np.sqrt(np.sum(abs(p)**2))
    vg=np.gradient(np.unwrap(E[np.argsort(ks),0]),np.sort(ks))[np.argmin(abs(np.sort(ks)-k0))]
    ang=th*np.ones(L); ang[xd]+=alpha
    for t in range(T): p=step(p,ang)
    pk=np.array([np.fft.fft(p[0]),np.fft.fft(p[1])]).T          # (L,2)
    proj=np.abs(np.einsum('kab,ka->kb',V.conj(),pk))**2; proj/=proj.sum()
    near0=np.abs(ks)<np.pi/2
    return vg, proj[near0].sum(), proj[~near0].sum()
for th in [0.0,0.05]:
    for alpha in [0.0,0.3,1.0]:
        vg,f0,fpi=run(th,alpha,np.pi-0.4)
        print(f"theta={th} event alpha={alpha}: doubler group speed {vg:+.3f}; after: weight near k=0 (light species) {f0:.4f}, near k=pi {fpi:.4f}")
