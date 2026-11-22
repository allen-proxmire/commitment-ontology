# The lifting term on an uneven web. Same web as c15n (flat, lines relabelled alone, link lengths uneven by 0.1; a place's size V = mean of its two links;
# hops 1/sqrt(V V')). Massless, 2D, r = 1/2, packets dressed as in c15n.
#  G  lifting term built from the lengths: -(r/2) sigma_z times the lines' own second difference,
#     [ (psi(x+1) - psi(x))/a_right + (psi(x-1) - psi(x))/a_left ] / V, written for chi = sqrt(V) psi (Hermitian; zero on patterns linear in true position).
#  U  the even grid's lifting term r(2 - cos k_x - cos k_y) sigma_z added unchanged.
# Stated before running: G loses no faster than the plain hops of c15n (1.0e-5, 7.2e-5, 7.7e-4 at k = 0.15, 0.3, 0.6) at the two longer wavelengths;
# U loses at least 10 times faster than G.
import numpy as np
src=open(__file__.replace("c15p","c15n")).read().split("tab={}")[0]; exec(src)
r=0.5
gx=(1/(ax*np.sqrt(Vx*np.roll(Vx,-1))))[:,None]; gy=(1/(ay*np.sqrt(Vy*np.roll(Vy,-1))))[None,:]      # link i joins places i and i+1
dgx=((1/ax+1/np.roll(ax,1))/Vx)[:,None]; dgy=((1/ay+1/np.roll(ay,1))/Vy)[None,:]
def lift_G(p):
    lap=gx*np.roll(p,-1,1)+np.roll(gx,1,0)*np.roll(p,1,1)-dgx*p + gy*np.roll(p,-1,2)+np.roll(gy,1,1)*np.roll(p,1,2)-dgy*p
    return -(r/2)*np.array([lap[0],-lap[1]])
Wk=r*(2-np.cos(KX)-np.cos(KY))
def lift_U(p):
    w=np.fft.ifft2(Wk*np.fft.fft2(p)); return np.array([w[0],-w[1]])
H_G=lambda p: H_L(p)+lift_G(p); H_U=lambda p: H_L(p)+lift_U(p)
def run2(H,k0):       # as run(), with the positive-energy spinor of the lifted step
    k0=2*np.pi*round(k0*L/(2*np.pi))/L; xi=np.arange(L)-L/4; XI,Y=np.meshgrid(xi,np.arange(L)-L/2,indexing='ij')
    ph=np.exp(1j*k0*(X-np.arange(L)))[:,None]; sv=np.sqrt(Vx[:,None]*Vy[None,:])
    m=r*(1-np.cos(k0)); s=np.sin(k0); E=np.hypot(s,m); u=np.array([s,E-m]); u=u/np.linalg.norm(u)
    env=sv*ph*np.exp(-(XI**2+Y**2)/(4*sig**2)+1j*k0*np.arange(L)[:,None]); p=np.array([u[0]*env,u[1]*env]); p/=np.sqrt((abs(p)**2).sum())
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
    for nm,H in (("lifting term from the lengths",H_G),("lifting term unchanged",H_U)):
        k0,rate,out=run2(H,k); tab[(nm,k)]=rate; print(f"k = {k0:.3f}, {nm}: loss rate {rate:.3e}; forward share "+" ".join(f"{o:.5f}" for o in out),flush=True)
for k in (0.15,0.3,0.6): print(f"k = {k}: unchanged over from-the-lengths {tab[('lifting term unchanged',k)]/max(tab[('lifting term from the lengths',k)],1e-15):.1f}")
