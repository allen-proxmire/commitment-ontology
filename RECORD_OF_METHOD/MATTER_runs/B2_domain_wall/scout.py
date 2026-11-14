import numpy as np, sys; sys.path.insert(0,'.')
from dw import *
w=5*np.pi/16
# bulk gaps at quasienergy 0 and pi, and Chern number of the band below 0 (Fukui-Hatsugai) for a scan of theta
def chern(th,w,N=60):
    ks=2*np.pi*np.arange(N)/N; V=np.zeros((N,N,2),complex)
    for i,a in enumerate(ks):
        for j,b in enumerate(ks):
            Ax=np.diag([np.exp(-1j*a),1])@F(w)@np.diag([1,np.exp(1j*a)])@F(-w)
            Ay=R@np.diag([np.exp(-1j*b),1])@F(w)@np.diag([1,np.exp(1j*b)])@F(-w)@Rd
            ev,vec=np.linalg.eig(Ax@Ay@F(th)@Ay@Ax); V[i,j]=vec[:,np.argmax(np.angle(ev))]  # upper band (E in (0,pi))
    C=0
    for i in range(N):
        for j in range(N):
            a=V[i,j];b=V[(i+1)%N,j];c=V[(i+1)%N,(j+1)%N];d=V[i,(j+1)%N]
            C+=np.angle(np.vdot(a,b)*np.vdot(b,c)*np.vdot(c,d)*np.vdot(d,a))
    return C/(2*np.pi)
def gaps(th,w,N=60):
    ks=2*np.pi*np.arange(N)/N; e=np.array([bulkE(a,b,th,w) for a in ks for b in ks])
    return np.min(np.abs(e)), np.min(np.pi-np.abs(e))
for th in np.linspace(-3,3,25):
    g0,gp=gaps(th,w); print(f"th={th:+.2f} gap0={g0:.3f} gapPi={gp:.3f} C_upper={chern(th,w):+.2f}")
