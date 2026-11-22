# What "flat" means at one hop: the same unevenness, sited on places or on links. 2D, massless, plain hops (r = 0), unevenness 0.1.
# Lengths along x depend on x only, along y on y only (a relabelling of the lines: flat).
#  P  strengths on places, as the step has them: H = {w_x(x), sigma_x sin k_x}/2 + {w_y(y), sigma_y sin k_y}/2, w = 1/length drawn per place.
#  L  lengths on links: link x+1/2 has length a; a place's size along x is V(x) = (a_left + a_right)/2; the hop over a link has strength
#     1/sqrt(V V') of its two ends. This is the exact first-order form of c15f, which closes when the lines are relabelled separately.
# Loss rate = slope of the forward share against time. Not registered. Expected: L loses at least 5 times more slowly than P at k = 0.3.
import numpy as np
L=256; sig=24.0; dt=0.5; order=10; eps=0.1; times=(50,100,150)
kk=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(kk,kk,indexing='ij')
sgx=lambda p: np.array([p[1],p[0]]); sgy=lambda p: np.array([-1j*p[1],1j*p[0]])
rng=np.random.default_rng(2)
ax=1+eps*rng.standard_normal(L); ax*=L/ax.sum(); ay=1+eps*rng.standard_normal(L); ay*=L/ay.sum()     # link i sits between places i and i+1
Vx=(ax+np.roll(ax,1))/2; Vy=(ay+np.roll(ay,1))/2
tx=(1/np.sqrt(Vx*np.roll(Vx,-1)))[:,None]; ty=(1/np.sqrt(Vy*np.roll(Vy,-1)))[None,:]
X=np.concatenate(([0],np.cumsum(ax)[:-1]))            # true position along x of place i
wx=(1/(1+eps*rng.standard_normal(L)))[:,None]*np.ones((1,L)); wy=np.ones((L,1))*(1/(1+eps*rng.standard_normal(L)))[None,:]
def H_L(p):
    dxp=(tx*np.roll(p,-1,1)-np.roll(tx,1,0)*np.roll(p,1,1))/2; dyp=(ty*np.roll(p,-1,2)-np.roll(ty,1,1)*np.roll(p,1,2))/2
    return -1j*(sgx(dxp)+sgy(dyp))
def dsin(p,i): return np.fft.ifft2((np.sin(KX),np.sin(KY))[i]*np.fft.fft2(p))
def H_P(p): return 0.5*(wx*sgx(dsin(p,0))+sgx(dsin(wx*p,0))+wy*sgy(dsin(p,1))+sgy(dsin(wy*p,1)))
def H_0(p): return sgx(dsin(p,0))+sgy(dsin(p,1))
def run(H,k0,dress):
    k0=2*np.pi*round(k0*L/(2*np.pi))/L; xi=np.arange(L)-L/4; XI,Y=np.meshgrid(xi,np.arange(L)-L/2,indexing='ij')
    ph=np.exp(1j*k0*(X-np.arange(L)))[:,None] if dress else 1.0; sv=np.sqrt(Vx[:,None]*Vy[None,:]) if dress else 1.0
    env=sv*ph*np.exp(-(XI**2+Y**2)/(4*sig**2)+1j*k0*np.arange(L)[:,None]); p=np.array([env,env])/np.sqrt(2); p/=np.sqrt((abs(p)**2).sum())
    w=np.hypot(KX-k0,KY)<0.12
    def fwd(p):
        q=p/sv/ph; P=(abs(np.fft.fft2(q))**2).sum(0); return P[w].sum()/P.sum()
    out=[fwd(p)]; n=0
    for T in times:
        while n<int(T/dt):
            term=p.copy(); acc=p.copy()
            for j in range(1,order+1): term=(-1j*dt/j)*H(term); acc=acc+term
            p=acc; n+=1
        out.append(fwd(p))
    return k0,-np.polyfit((0,)+times,out,1)[0],out
tab={}
for k in (0.15,0.3,0.6):
    for nm,H,dr in (("even",H_0,False),("places",H_P,False),("links",H_L,True)):
        k0,rate,out=run(H,k,dr); tab[(nm,k)]=rate; print(f"k = {k0:.3f}, {nm}: loss rate {rate:.3e}; forward share "+" ".join(f"{o:.5f}" for o in out),flush=True)
for k in (0.15,0.3,0.6): print(f"k = {k}: places over links {tab[('places',k)]/max(tab[('links',k)],1e-15):.1f}")
