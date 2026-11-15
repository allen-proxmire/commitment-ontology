import numpy as np,sys; sys.path.insert(0,'.')
from c3i import *
# finite-difference check of the Taylor blocks
k=(0.3,-0.7,1.1); q=0.05; m=0.1; tau=0.4
U0,U1,U2=ops(k,q,m,tau,0,1,'B')
def Ua(a):
    kk=np.array(k); k2=kk.copy(); k2[0]+=q
    H0=bd(H(kk,m),H(k2,m)); H1=od(0.5*dH(kk,1)); H2=bd(d2H(kk,1)/8,d2H(k2,1)/8)
    return expm(-1j*tau*(H0+a*H1+a*a*H2))
h=1e-3; print("U1 err",np.abs((Ua(h)-Ua(-h))/(2*h)-U1).max()," U2 err",np.abs((Ua(h)+Ua(-h)-2*Ua(0))/(2*h*h)-U2).max())
import time; p,wt=shells(0.01,9); t=time.time(); print(len(p)); shift(k,0.001,0.025,0.4,0,1,'B'); print("per point",(time.time()-t))
