# Shear: nudge b(x) = b1 x (drift gradient 2 b1). Each at +-b1, odd part. Force d<k_x>/dt against -2 b1 sin k_y; transverse acceleration against the lattice ray prediction. Lattice 512 wide so the seam of the linear profile stays far from the packet.
LX,LY=512,256
exec(open('g7.py').read())
T=100; t=np.arange(T+1); b1=1e-4
kxs=2*np.pi*np.fft.fftfreq(Lx)[:,None]
def raypred(th,k0):
    hk=1e-3; Exx=(E(hk,k0,th,w0)-2*E(0,k0,th,w0)+E(-hk,k0,th,w0))/hk**2
    return -Exx*2*b1*np.sin(k0), -2*b1*np.sin(k0)
def run(th,k0,sig,bb):
    p=packet(th,k0,sig); xs=[]; kx=[]; B=bb*x
    for s in range(T+1):
        q=np.sum(abs(p)**2,0); xs.append(np.sum(q*x))
        pk=np.sum(abs(np.fft.fft(p,axis=1))**2,0); kx.append(np.sum(pk*kxs)/pk.sum())
        p=stepC(p,w0,th*np.ones_like(x),B)
    return 2*np.polyfit(t,xs,2)[0], np.polyfit(t,kx,1)[0]
for name,th,k0,sig in [("light +y",0,0.2,25),("light +y",0,0.2,50),("light -y",0,-0.2,50),("matter 0.4 at rest",0.4,0,50),("matter 0.4 moving +y",0.4,0.1,25),("matter 0.4 moving +y",0.4,0.1,50)]:
    ap,kp=run(th,k0,sig,b1); am,km=run(th,k0,sig,-b1); a=(ap-am)/2; kd=(kp-km)/2
    pa,pk=raypred(th,k0)
    print(f"{name} w{sig}: dk_x/dt={kd:+.4e} (pred {pk:+.4e}, ratio {kd/pk if pk else 0:.4f}) | a_x={a:+.4e} (ray {pa:+.4e}, ratio {a/pa if pa else 0:.4f})")
