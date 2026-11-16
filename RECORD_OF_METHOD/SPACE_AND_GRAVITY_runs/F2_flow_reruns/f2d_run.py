# F2d (G14 on the flow step): two patterns, each sourcing a field by a 2D wave equation, each feeling the other's through P7f restated.
import numpy as np,scipy.sparse as sp,sys,time; sys.path.insert(0,'.')
from flow2ds import *
from scipy.sparse.linalg import expm_multiply
tau=0.4; r=0.5; Lx,Ly=600,400; d=200; sig=30; kap=2e-2; mA,mB=0.4,0.3; Tend=360.0; nT=int(Tend/tau)
Sx=sp.kron(ring(Lx),sp.identity(Ly)); Sy=sp.kron(sp.identity(Lx),ring(Ly)); I=sp.identity(Lx*Ly)
K=(sp.kron((Sx-Sx.T)/(2j),sx)+sp.kron((Sy-Sy.T)/(2j),sy)+r*sp.kron(2*I-(Sx+Sx.T)/2-(Sy+Sy.T)/2,sz)).tocsr()
Z=sp.kron(I,sz).tocsr()
def Hof(m,Phi):
    N=1-Phi.ravel(); D=np.repeat(N/(1+Phi.ravel()),2); Dm=sp.diags(D)
    return (0.5*(Dm@K+K@Dm)+sp.diags(np.repeat(m*N,2))@Z).tocsr()
lap=lambda F: np.roll(F,1,0)+np.roll(F,-1,0)+np.roll(F,1,1)+np.roll(F,-1,1)-4*F
pa=packet(Lx,Ly,mA,r,(0.,0.),sig,c0=(-d//2,0)); pb=packet(Lx,Ly,mB,r,(0.,0.),sig,c0=(d//2,0))
H0a=Hof(mA,np.zeros((Lx,Ly))); H0b=Hof(mB,np.zeros((Lx,Ly)))
qa,qb=pa.copy(),pb.copy()          # no-field references
Pa=np.zeros((Lx,Ly)); Pa_old=Pa.copy(); Pb=Pa.copy(); Pb_old=Pa.copy()   # fields sourced by A and by B
nsub=2; dt=tau/nsub; rec=[]; t0=time.time()
for n in range(1,nT+1):
    pa=expm_multiply(-1j*tau*Hof(mA,Pb-Pb.mean()),pa); pb=expm_multiply(-1j*tau*Hof(mB,Pa-Pa.mean()),pb)
    qa=expm_multiply(-1j*tau*H0a,qa); qb=expm_multiply(-1j*tau*H0b,qb)
    for F,Fo,m,p in ((Pa,Pa_old,mA,pa),(Pb,Pb_old,mB,pb)):
        rho=m*dens(p,Lx,Ly); src=kap*(rho-rho.mean())
        for s in range(nsub):
            Fn=2*F-Fo+dt**2*(lap(F)+src); Fo[:]=F; F[:]=Fn
    if n%25==0:
        xa=centre(dens(pa,Lx,Ly),Lx,0)-centre(dens(qa,Lx,Ly),Lx,0); xb=centre(dens(pb,Lx,Ly),Lx,0)-centre(dens(qb,Lx,Ly),Lx,0)
        rec.append((n*tau,xa,xb)); print(f"t={n*tau:.0f}: dx_a={xa:+.4f} dx_b={xb:+.4f}  ({time.time()-t0:.0f}s)",flush=True)
# point-pattern prediction: accel of b toward a = (1+r m_b) kap m_a /(2 pi d) / sqrt(1-(d/t)^2) for t > d (separation held fixed)
ts=np.linspace(0,Tend,200001)
def disp(msrc,mfelt):
    a=np.where(ts>d,(1+r*mfelt)*kap*msrc/(2*np.pi*d)/np.sqrt(np.maximum(1-(d/np.maximum(ts,1e-9))**2,1e-12)),0)
    v=np.cumsum(a)*(ts[1]-ts[0]); return np.cumsum(v)*(ts[1]-ts[0])
pa_=disp(mB,mA); pb_=-disp(mA,mB); ok=True; final=rec[-1]
for t,xa,xb in rec:
    i=np.searchsorted(ts,t); print(f"t={t:.0f}: dx_a {xa:+.4f} (pred {pa_[i]:+.4f})  dx_b {xb:+.4f} (pred {pb_[i]:+.4f})")
pre=[(xa,xb) for t,xa,xb in rec if t<=d]; i=np.searchsorted(ts,final[0])
fa=final[1]/pa_[i]; fb=final[2]/pb_[i]; ok&=0.8<=fa<=1.2 and 0.8<=fb<=1.2
ok&=max(max(abs(a),abs(b)) for a,b in pre)<=0.05*max(abs(final[1]),abs(final[2]))
print(f"final ratios: a {fa:.3f}, b {fb:.3f}; largest motion before the front {max(max(abs(a),abs(b)) for a,b in pre):.4f}")
print("F2d",'PASS' if ok else 'FAIL')
