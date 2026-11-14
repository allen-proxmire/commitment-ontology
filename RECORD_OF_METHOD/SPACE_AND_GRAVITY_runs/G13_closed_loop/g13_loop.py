# Closed loop, first toy: two patterns on CO's 1D walk, each sourcing a lapse field that evolves on the lattice
# (wave equation at the walk's light speed, CO's linear cost in 1D), each feeling the other's field through P7f
# (mass flip theta N, Wilson flip 2 cos w = c0 N). No self-pull (each pattern's field acts on the other only).
# Source: rest-energy density theta |psi|^2. Field: h_tt = c0^2 (h_xx + kappa (rho - mean rho)), N = 1 - h.
# Predictions: after the field front arrives (delay = separation / c0), each falls toward the other with
# a_b = c0^2 kappa theta_a / 2 (1D, slow), so theta_a a_a = -theta_b a_b (action = reaction).
import numpy as np, sys
L=3000; w0=0.3; c0=2*np.cos(w0); z=np.arange(L)-L//2
sx=np.array([[0,1],[1,0]],complex); F=lambda a: np.cos(a)*np.eye(2)-1j*np.sin(a)*sx
def Uk(k,th):
    A=np.diag([np.exp(-1j*k),1])@F(w0)@np.diag([1,np.exp(1j*k)])@F(-w0); return A@F(th)@A
def Fop(p,a): c=np.cos(a); s=np.sin(a); u,d=p; return np.array([c*u-1j*s*d, c*d-1j*s*u])
def A(p,w): p=Fop(p,-w); p=np.array([p[0],np.roll(p[1],-1)]); p=Fop(p,w); return np.array([np.roll(p[0],1),p[1]])
def step(p,w,ang): return A(Fop(A(p,w),ang),w)
def packet(th,sig,x0):
    ks=2*np.pi*np.fft.fftfreq(L); phi=np.zeros((L,2),complex)
    for i,k in enumerate(ks):
        a=np.exp(-(k*sig)**2/2)
        if a<1e-12: continue
        ev,v=np.linalg.eig(Uk(k,th)); phi[i]=a*v[:,np.argmin(np.angle(ev))]
    p=np.array([np.fft.ifft(phi[:,0]),np.fft.ifft(phi[:,1])]); p=np.roll(p,L//2+x0,axis=1); return p/np.sqrt(np.sum(abs(p)**2))
def run(tha,thb,D,kappa,T,sig=100,sub=4):
    pa=packet(tha,sig,-D); pb=packet(thb,sig,+D)
    ha=np.zeros(L); hav=np.zeros(L); hb=np.zeros(L); hbv=np.zeros(L); dt=1.0/sub
    xa=[];xb=[]
    for t in range(T+1):
        ra=tha*np.sum(abs(pa)**2,0); rb=thb*np.sum(abs(pb)**2,0)
        xa.append(np.sum(np.sum(abs(pa)**2,0)*z)); xb.append(np.sum(np.sum(abs(pb)**2,0)*z))
        for s in range(sub):   # field a from pattern a, field b from pattern b
            for h,hv,r in ((ha,hav,ra),(hb,hbv,rb)):
                lap=np.roll(h,1)+np.roll(h,-1)-2*h
                hv+=dt*c0**2*(lap+kappa*(r-r.mean())); h+=dt*hv
        Na=1-hb; Nb=1-ha          # each feels the other's field
        pa=step(pa,np.arccos(c0*Na/2),tha*Na); pb=step(pb,np.arccos(c0*Nb/2),thb*Nb)
    return np.array(xa),np.array(xb)
if __name__=="__main__":
    tha,thb,D,kappa,T=0.4,0.2,300,1.4e-5,1500
    xa,xb=run(tha,thb,D,kappa,T)
    t=np.arange(T+1); onset=2*D/c0
    print(f"separation {2*D}, field front arrives after {onset:.0f} ticks")
    for lo,hi in [(0,int(0.8*onset)),(int(1.3*onset),T)]:
        aa=2*np.polyfit(t[lo:hi],xa[lo:hi],2)[0]; ab=2*np.polyfit(t[lo:hi],xb[lo:hi],2)[0]
        print(f"window {lo}-{hi}: a_a={aa:+.3e} (pred {+c0**2*kappa*thb/2:.3e})  a_b={ab:+.3e} (pred {-c0**2*kappa*tha/2:.3e})  theta_a a_a + theta_b a_b = {tha*aa+thb*ab:+.2e} (vs |theta a| {abs(tha*aa):.2e})")
    print("x_a(t) at 0,200,400,800,1500:",np.round(xa[[0,200,400,800,1500]]+D,3)," x_b:",np.round(xb[[0,200,400,800,1500]]-D,3))
