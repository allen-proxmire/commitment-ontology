import numpy as np
# CO's 1D strictly local palindromic Wilson walk: A = S+ F(w) S- F(-w); step U = A F(theta*N(z)) A
# Lapse enters through the clock rule: the mass flip at each place is scaled by N(z) = 1 - g z.
L=6000; w=0.3
z=np.arange(L)-L//2
def Fop(psi,a):  # local flip cos a - i sin a sigma_x, a array or scalar
    c=np.cos(a); s=np.sin(a); u,d=psi
    return np.array([c*u-1j*s*d, c*d-1j*s*u])
def Sp(psi): u,d=psi; return np.array([np.roll(u,1),d])     # component 1 one place up
def Sm(psi): u,d=psi; return np.array([u,np.roll(d,-1)])    # component 2 one place down
def A(psi): return Fop(Sm(Fop(Sp(Fop(Sm(Fop(psi,-w)),w)),0)),0) if False else Sp(Fop(Sm(Fop(psi,-w)),w))
def step(psi,ang): return A(Fop(A(psi),ang))
# massless speed c0 from uniform dispersion
def Uk(k,th):
    sx=np.array([[0,1],[1,0]]); F=lambda a: np.cos(a)*np.eye(2)-1j*np.sin(a)*sx
    Spk=np.diag([np.exp(-1j*k),1]); Smk=np.diag([1,np.exp(1j*k)])
    Ak=Spk@F(w)@Smk@F(-w); return Ak@F(th)@Ak
def E(k,th): return np.sort(np.abs(np.angle(np.linalg.eigvals(Uk(k,th)))))[0]
h=1e-4; c0=(E(h,0)-E(0,0))/h if False else (E(2*h,0)-E(h,0))/h
print("c0 (hops/step) =",round(c0,5))
def packet(th,width=60):
    # positive-energy eigenvector at each k of the uniform walk, Gaussian in k around 0
    ks=2*np.pi*np.fft.fftfreq(L); amp=np.exp(-(ks*width)**2/2)
    phi=np.zeros((2,L),complex)
    for i,k in enumerate(ks):
        if amp[i]<1e-12: continue
        ev,V=np.linalg.eig(Uk(k,th)); j=np.argmin(np.angle(ev)) if False else np.argmax(np.angle(ev))
        # choose the branch with quasi-energy -E (e^{-iE}) i.e. positive energy: angle<0
        j=np.argmin(np.angle(ev)); phi[:,i]=amp[i]*V[:,j]
    psi=np.array([np.fft.ifft(phi[0]),np.fft.ifft(phi[1])])
    # momentum convention: Sp multiplies by e^{ik} when shifting up means psi(z) ~ e^{-ikz}; check by drift test below
    psi=np.roll(psi,L//2,axis=1)
    return psi/np.sqrt(np.sum(np.abs(psi)**2))
def run(th,g,T=1500):
    N=1-g*z; ang=th*N
    psi=packet(th); xs=[]
    for t in range(T+1):
        p=np.sum(np.abs(psi)**2,0); xs.append(np.sum(p*z))
        psi=step(psi,ang)
    t=np.arange(T+1); a,b,c=np.polyfit(t,xs,2)
    return 2*a, b, xs[-1]-xs[0]
print("drift check (g=0):",[round(v,6) for v in run(0.2,0.0,T=300)])
for th in [0.1,0.2,0.4]:
    for g in [2e-6,4e-6]:
        acc,v0,dx=run(th,g)
        print(f"theta={th} g={g}: measured a={acc:.4e}  predicted g*c0^2={g*c0**2:.4e}  ratio={acc/(g*c0**2):.4f}  (start velocity {v0:.2e}, total move {dx:.1f})")
