# G17: a cloud collapsing under its own river, radial reduction (s-wave, far from the centre: the 1D walk in r).
# Many patterns, each pulled by the others; the cloud's density is carried by one wavefunction (Hartree-like, the self-share 1/N
# neglected). Painleve-Gullstrand: lapse 1, flat slices, drift inward v(r) = sqrt(2 G M(<r) / r), set each step by the cloud's
# own enclosed mass (a constraint in GR, no propagation needed), carried by directed hops on the radial links; w = 5pi/16 fixed.
# Prediction: marginally bound dust (Oppenheimer-Snyder, zero momentum): each shell keeps its enclosed mass and falls as
#   r_q^{3/2}(t) = r_q0^{3/2} - (3/2) sqrt(2 G M q) t,
# and crosses its own horizon r = 2 G M q / c0^2. Fail: Lagrangian radii off this by more than the packet's spreading.
import numpy as np, sys
L=1400; w=5*np.pi/16; c0=2*np.cos(w); r=np.arange(L).astype(float)
sx=np.array([[0,1],[1,0]],complex); F=lambda a: np.cos(a)*np.eye(2)-1j*np.sin(a)*sx
def Uk(k,th):
    A=np.diag([np.exp(-1j*k),1])@F(w)@np.diag([1,np.exp(1j*k)])@F(-w); return A@F(th)@A
def Fop(p,a): c=np.cos(a); s=np.sin(a); u,d=p; return np.array([c*u-1j*s*d, c*d-1j*s*u])
def A(p): p=Fop(p,-w); p=np.array([p[0],np.roll(p[1],-1)]); p=Fop(p,w); return np.array([np.roll(p[0],1),p[1]])
def conv(p,B):
    for par in (0,1):
        cb=np.cos(B[par::2]/2); sb=np.sin(B[par::2]/2)
        a=p[:,par::2].copy(); c=np.roll(p,-1,axis=1)[:,par::2].copy()
        q=p.copy(); q[:,par::2]=cb*a-sb*c; t=np.roll(q,-1,axis=1); t[:,par::2]=sb*a+cb*c; p=np.roll(t,1,axis=1)
    return p
def step(p,th,B): return conv(A(Fop(A(conv(p,B)),th)),B)
def shell(th,r0,sig_r):
    ks=2*np.pi*np.fft.fftfreq(L); phi=np.zeros((L,2),complex); sig=1/(np.sqrt(2)*0+1/sig_r)
    for i,k in enumerate(ks):
        a=np.exp(-(k*sig_r)**2/2)
        if a<1e-12: continue
        ev,v=np.linalg.eig(Uk(k,th)); phi[i]=a*v[:,np.argmin(np.angle(ev))]*np.exp(-1j*k*r0)
    p=np.array([np.fft.ifft(phi[:,0]),np.fft.ifft(phi[:,1])]); return p/np.sqrt(np.sum(abs(p)**2))
def run(th,r0,sig_r,rs,T,qs):
    p=shell(th,r0,sig_r); out=[]
    for t in range(T+1):
        dens=np.sum(abs(p)**2,0); M=np.cumsum(dens); M/=M[-1]
        out.append([np.interp(q,M,r) for q in qs])
        rm=np.maximum(r+0.5,1.0); v=np.minimum(np.sqrt(c0**2*rs*np.interp(r+0.5,r,M)/rm),1.9)
        p=step(p,th,-np.arcsin(v/2))
    return np.array(out)
if __name__=="__main__":
    th=0.5; r0=500; sig_r=60; rs=150.0; T=420; qs=[0.1,0.5,0.9]
    out=run(th,r0,sig_r,rs,T,qs)
    out0=run(th,r0,sig_r,0.0,T,qs)       # no gravity: the shell's own spreading
    t=np.arange(T+1)
    print(f"c0={c0:.4f}; cloud's horizon radius 2GM/c0^2 = {rs}")
    for j,q in enumerate(qs):
        rq0=out[0,j]; pred=np.maximum(rq0**1.5-1.5*np.sqrt(c0**2*rs*q)*t,0)**(2/3)
        hz=q*rs; cross=np.argmax(out[:,j]<hz) if (out[:,j]<hz).any() else -1; pcross=np.argmax(pred<hz) if (pred<hz).any() else -1
        print(f"shell q={q}: r at t=0,100,200,300,420: {np.round(out[[0,100,200,300,420],j],1)}  predicted {np.round(pred[[0,100,200,300,420]],1)}  (no gravity {np.round(out0[[0,420],j],1)});  crosses its horizon r={hz:.0f} at t={cross} (pred {pcross})")
        sys.stdout.flush()
