# G8: light passing a point mass on CO's 2D walk (a slice through the mass: the ray stays in the plane).
# Phi = A / sqrt(r^2 + rc^2); lapse N = 1 - Phi; hop stretch psi^2 = 1 + Phi (gamma = 1); clock only: psi^2 = 1.
# Field enters by P7f: Wilson flip 2 cos w = c0 N/psi^2 (light, theta = 0). +A only (second order ~ Phi(b) ~ 0.5%),
# minus the no-field run; packets pass on both sides (x = +-b) and are averaged, cancelling the 2D walk's sideways drift at first order.
LX,LY=512,1024
exec(open('../G6_light_bending/g6.py').read().replace("Lx,Ly=400,256","Lx,Ly=LX,LY"))
yv=(np.arange(Ly)-Ly//2)[None,:]*np.ones((Lx,1))
B=120; RC=5.0; K0=0.5; SIG=40; Y0=-440
r=np.sqrt(x**2+yv**2)
def wfield(A,stretch):
    Phi=A/np.sqrt(r**2+RC**2); N=1-Phi; ps2=1+stretch*Phi
    return np.arccos(c0*N/ps2/2)
kxs=2*np.pi*np.fft.fftfreq(Lx)[:,None]; kys=2*np.pi*np.fft.fftfreq(Ly)[None,:]
def run(A,stretch,T,side=1):
    p=packet(0,K0,SIG); p=np.roll(p,(side*B,Y0),axis=(1,2))   # start at x=B, y=Y0, moving +y
    w=wfield(A,stretch); ang=np.zeros_like(x)
    for t in range(T): p=step(p,w,ang)
    q=np.sum(abs(p)**2,0); pk=np.sum(abs(np.fft.fft2(p,axes=(1,2)))**2,0)
    kx=np.sum(pk*kxs)/pk.sum(); ky=np.sum(pk*((kys+np.pi)%(2*np.pi)-np.pi))/pk.sum()
    return kx,ky,np.sum(q*x),np.sum(q*yv)
