import numpy as np,sys; sys.path.insert(0,'../F2_flow_reruns')
from flow2ds import *
from scipy.sparse.linalg import expm_multiply
tau=0.4; r=0.5; L=300; m=0.5; R0=60; w=6; n=12; kb=4*2e-2*40   # kappa_b = 4 kappa, scaled up for a visible push
X=(np.arange(L)-L//2)[:,None]*np.ones((1,L)); Y=X.T.copy(); RR=np.hypot(X,Y); PHI=np.arctan2(Y,X)
f=np.exp(-(RR-R0)**2/(2*w**2))*np.exp(1j*n*PHI)
F=np.fft.fft2(f); kx=2*np.pi*np.fft.fftfreq(L); ps=np.zeros((L,L,2),complex)
for i,a in enumerate(kx):
    for j,b in enumerate(kx):
        if abs(F[i,j])<1e-12*np.abs(F).max(): continue
        ps[i,j]=F[i,j]*eig_u(a,b,m,r)
psi=np.fft.ifft2(ps,axes=(0,1)); psi/=np.linalg.norm(psi)
def sinop(p,ax): return (np.roll(p,-1,ax)-np.roll(p,1,ax))/(2j)     # (S - S^T)/(2i), S psi(x)=psi(x+1)
P=[np.real(np.sum(np.conj(psi)*sinop(psi,ax),2)) for ax in (0,1)]
Llat=np.sum(X*P[1]-Y*P[0])
# continuum orbital angular momentum, spectrally: -i(x d_y - y d_x)
def dspec(p,ax):
    k=2*np.pi*np.fft.fftfreq(L); sh=[1,1,1]; sh[ax]=L; return np.fft.ifft(1j*k.reshape(sh)*np.fft.fft(p,axis=ax),axis=ax)
Lcont=np.real(np.sum(np.conj(psi)*(-1j)*(X[...,None]*dspec(psi,1)-Y[...,None]*dspec(psi,0))))
ok=True; d=Llat/Lcont-1; ok&=abs(d)<=0.02
print(f"F3a: source L = {Llat:.4f}; <-i d_phi> = {Lcont:.4f} ({d:+.4f}); winding n = {n}; <sigma_z>/2 = {np.sum(np.abs(psi[...,0])**2-np.abs(psi[...,1])**2)/2:+.4f}")
# shift from the linear cost: lattice Laplacian, periodic, zero mean
kk=2*np.pi*np.fft.fftfreq(L); lam=(2*np.cos(kk)[:,None]-2)+(2*np.cos(kk)[None,:]-2); lam[0,0]=1
b=[np.real(np.fft.ifft2(-np.fft.fft2(kb*Pi)/lam)) for Pi in P]   # lap b = -kb P (first pass had the sign reversed)
for bi in b: bi-=bi.mean()
Pphi=(-np.sin(PHI)*P[0]+np.cos(PHI)*P[1]); Om_free=kb/(4*np.pi)*np.sum(np.where(RR>0,Pphi/np.maximum(RR,1e-9),0))
# periodic box: curl b has zero mean, so the free value inside drops by the ring's enclosed area over the box (first pass omitted this)
R2=np.sum(Pphi*RR)/np.sum(np.where(RR>0,Pphi/np.maximum(RR,1e-9),0)); Om_pred=Om_free*(1-np.pi*R2/L**2)
c=L//2; curl=((b[1][c+1,c]-b[1][c-1,c])-(b[0][c,c+1]-b[0][c,c-1]))/4   # (d_x b_y - d_y b_x)/2 = Omega
d=curl/Om_pred-1; ok&=abs(d)<=0.03 and np.sign(curl)==np.sign(Llat)
print(f"F3b: Omega at centre (curl/2) = {curl:.5e}; thin-shell prediction {Om_free:.5e}, in the periodic box {Om_pred:.5e} ({d:+.4f}); sense {'with' if np.sign(curl)==np.sign(Llat) else 'against'} the ring")
one=np.ones((L,L)); t=tau*150
for mm in (0.0,0.5):
    for ky in (0.3,-0.3):
        p=packet(L,L,mm,r,(0.,ky),8); H=build(L,L,mm,r,one,one,bx=b[0],by=b[1]); k0=mean_k(p,L,L,(0.,ky))
        q=expm_multiply(-1j*t*H,p); dk=mean_k(q,L,L,(0.,ky))[0]-k0[0]; pred=-curl*np.sin(ky)*t; dd=dk/pred-1; ok&=abs(dd)<=0.03
        print(f"F3c: m={mm}, ky={ky:+}: dk_x = {dk:+.5e} vs -Omega sin(ky) t = {pred:+.5e} ({dd:+.4f})",flush=True)
print("F3",'PASS' if ok else 'FAIL')
