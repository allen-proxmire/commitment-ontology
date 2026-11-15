import numpy as np, sys
from scipy.linalg import schur
sys.path.insert(0,'.')
from i2 import pair_ops, shells
# Dynamic transverse response: A_y = a cos(qx - omega t). Rotating frame: the k+q block's row of each step picks up e^{i omega}.
def pair_shift_dyn(k,q,om,th,w):
    U0,U1,U2=pair_ops(k,q,th,w,'B')
    R=np.diag(np.r_[np.ones(4),np.exp(1j*om)*np.ones(4)])
    filled0=np.r_[np.angle(np.linalg.eigvals(U0[:4,:4]))<0, np.angle(np.linalg.eigvals(U0[4:,4:]))<0]
    W0,W1,W2=R@U0,R@U1,R@U2
    T,V=schur(W0,output='complex'); lam=np.diag(T)
    # identify block membership and filled status of each Schur vector
    blk=(np.sum(np.abs(V[4:,:])**2,axis=0)>0.5).astype(int)
    ang=np.angle(lam*np.where(blk==1,np.exp(-1j*om),1))
    A1=V.conj().T@W1@V; A2=V.conj().T@W2@V; tot=0.
    FILLED=ang<0
    for n in range(8):
        if ang[n]>=0: continue
        d=lam[n]-lam; mask=(np.abs(d)>1e-12)&~FILLED  # filled-filled pairs cancel exactly by unitarity; dropped to avoid round-off
        tot+=np.imag((A2[n,n]+np.sum(A1[n,mask]*A1[mask,n]/d[mask]))/lam[n])
    return tot
def Cdyn(q,om,th,w,pts,wts):
    return sum(wt*pair_shift_dyn(p,q,om,th,w) for p,wt in zip(pts,wts))/(2*np.pi)**3
