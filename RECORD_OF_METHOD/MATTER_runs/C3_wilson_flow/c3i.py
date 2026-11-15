import numpy as np,sys
from scipy.linalg import expm, schur
sys.path.insert(0,'../I1_induced_light'); from i2 import shells
I2=np.eye(2); Z2=np.zeros((2,2)); s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z2,si],[si,Z2]]) for si in s]; beta=np.block([[I2,Z2],[Z2,-I2]]); Z4=np.zeros((4,4)); I4=np.eye(4)
r=1.0
def H(k,m): return sum(alpha[j]*np.sin(k[j]) for j in range(3))+beta*(m+r*sum(1-np.cos(k[j]) for j in range(3)))
def dH(k,j): return alpha[j]*np.cos(k[j])+beta*r*np.sin(k[j])
def d2H(k,j): return -alpha[j]*np.sin(k[j])+beta*r*np.cos(k[j])
def bd(A,B): return np.block([[A,Z4],[Z4,B]])
def od(M): return np.block([[Z4,M],[M,Z4]])
def ops(k,q,m,tau,prop,link,field):
    k=np.array(k,float); k2=k.copy(); k2[prop]+=q
    H0=bd(H(k,m),H(k2,m))
    if field=='B':   # A_link = a cos(q x_prop): H(k_link + A) to second order; diagonal a^2/4 H'' halved per pair
        H1=od(0.5*dH(k,link)); H2=bd(d2H(k,link)/8,d2H(k2,link)/8)
    else:            # scalar potential a cos(q x_prop)
        H1=od(0.5*I4); H2=np.zeros((8,8))
    X,Y,Zm=-1j*tau*H0,-1j*tau*H1,-1j*tau*H2; O=np.zeros((8,8))
    E=expm(np.block([[X,Y,Zm],[O,X,Y],[O,O,X]]))   # Taylor blocks of exp(X + aY + a^2 Z)
    return E[:8,:8],E[:8,8:16],E[:8,16:]
def shift(k,q,m,tau,prop,link,field):
    U0,U1,U2=ops(k,q,m,tau,prop,link,field); T,V=schur(U0,output='complex'); lam=np.diag(T)
    A1=V.conj().T@U1@V; A2=V.conj().T@U2@V; F=np.angle(lam)<0; tot=0.
    for i in np.where(F)[0]:
        d=lam[i]-lam; msk=(np.abs(d)>1e-12)&~F; tot+=np.imag((A2[i,i]+np.sum(A1[i,msk]*A1[msk,i]/d[msk]))/lam[i])
    return tot
def coeff(th,tau,prop,link,field,p,wt):
    m=th/tau; qs=np.array([th/20,th/10,th/5]); qh=(2*np.sin(qs/2))**2
    Cs=np.array([sum(t*shift(kk,q,m,tau,prop,link,field) for kk,t in zip(p,wt))/(2*np.pi)**3 for q in qs])
    return np.linalg.solve(np.vstack([np.ones(3),qh,qh**2]).T,Cs)
