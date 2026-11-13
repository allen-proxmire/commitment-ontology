# Does extra-species (zone-corner) energy slide down the bands as the lattice grows by births, or stay stranded?
# 1D palindromic walk (w=0.3). Births: each step, new places are inserted at random positions, born empty
# (or, second rule, carrying the mean of their neighbours' amplitudes, renormalised). Track the packet's mean |k|
# and its weight in the light region (|k| < pi/2) against the stretch factor a = L/L0.
import numpy as np
w=0.3; sx=np.array([[0,1],[1,0]],complex); F=lambda a: np.cos(a)*np.eye(2)-1j*np.sin(a)*sx
def Uk(k,th):
    A=np.diag([np.exp(-1j*k),1])@F(w)@np.diag([1,np.exp(1j*k)])@F(-w); return A@F(th)@A
def Fop(p,a): c=np.cos(a); s=np.sin(a); u,d=p; return np.array([c*u-1j*s*d, c*d-1j*s*u])
def A(p): p=Fop(p,-w); p=np.array([p[0],np.roll(p[1],-1)]); p=Fop(p,w); return np.array([np.roll(p[0],1),p[1]])
def step(p,th): return A(Fop(A(p),th))
print("1D band: E(k) at k/pi = 0, .25, .5, .75, 1:",[round(min(abs(np.angle(np.linalg.eigvals(Uk(k,0))))),3) for k in np.pi*np.array([0,.25,.5,.75,1])])
def packet(L,k0,sig,th):
    ks=2*np.pi*np.fft.fftfreq(L); amp=np.exp(-(((ks-k0+np.pi)%(2*np.pi)-np.pi)*sig)**2/2)
    phi=np.zeros((L,2),complex)
    for i,k in enumerate(ks):
        if amp[i]<1e-12: continue
        ev,v=np.linalg.eig(Uk(k,th)); phi[i]=amp[i]*v[:,np.argmin(np.angle(ev))]
    p=np.array([np.fft.ifft(phi[:,0]),np.fft.ifft(phi[:,1])]); p=np.roll(p,L//2,axis=1); return p/np.sqrt(np.sum(abs(p)**2))
def stats(p):
    L=p.shape[1]; ks=2*np.pi*np.fft.fftfreq(L); pk=np.sum(abs(np.fft.fft(p,axis=1))**2,0); pk/=pk.sum()
    return np.sum(pk*abs(ks)), pk[abs(ks)<np.pi/2].sum()
def grow(rule,th=0.0,L0=1000,a_end=4.0,T=3000,seed=1):
    rng=np.random.default_rng(seed); p=packet(L0,np.pi-0.2,80,th); L=L0; out=[]
    births_total=int(L0*(a_end-1)); per=births_total/T; acc=0.0
    for t in range(T+1):
        if t%500==0: k,f=stats(p); out.append((round(L/L0,2),round(k/np.pi,3),round(f,3)))
        p=step(p,th); acc+=per; nb=int(acc); acc-=nb
        for _ in range(nb):
            j=rng.integers(0,L)
            new=np.zeros((2,1),complex) if rule=="empty" else (p[:,j:j+1]+p[:,(j-1)%L:(j-1)%L+1])/2
            p=np.concatenate([p[:,:j],new,p[:,j:]],axis=1); L+=1
        if rule=="mean": p/=np.sqrt(np.sum(abs(p)**2))
    return out
for rule in ["empty","mean"]:
    print(rule,"births: (a, mean|k|/pi, weight in |k|<pi/2):",grow(rule))
