import numpy as np
# G7: the one-way part enters CO's 2D walk as a spin-blind directed hop on each y-relation (the author's ruling, candidate).
# Conveyor C(b): brickwork on y-links (even then odd), each link (x,y)->(x,y+1) rotated by b(x)/2, generator i|y+1><y| - i|y><y+1|,
# the same for both spinor parts. Step: U = C A_x A_y F(theta) A_y A_x C (palindrome).
exec(open('../G6_light_bending/g6.py').read().replace("Lx,Ly=400,256","Lx,Ly=LX,LY"))
def conveyor(p,b):          # b: array over x (shape Lx,1) or scalar
    B=np.broadcast_to(np.asarray(b,float),(Lx,Ly))
    for par in (0,1):
        cb=np.cos(B[:,par::2]/2); sb=np.sin(B[:,par::2]/2)
        q=p.copy()
        a=p[:,:,par::2]; c=np.roll(p,-1,axis=2)[:,:,par::2]   # site y (par parity) and y+1
        na=cb*a-sb*c; nc=sb*a+cb*c
        q[:,:,par::2]=na
        tmp=np.roll(q,-1,axis=2); tmp[:,:,par::2]=nc; q=np.roll(tmp,1,axis=2)
        p=q
    return p
def stepC(p,w,ang,b): return conveyor(Ax(Ay(Fop(Ay(Ax(conveyor(p,b),w),w),ang),w),w),b)
def traj(th,k0,b,sig,T,w=w0):
    p=packet(th,k0,sig); xs=[];ys=[]; ph=np.exp(2j*np.pi*np.arange(Ly)/Ly)[None,:]
    nrm=[]
    for t in range(T+1):
        q=np.sum(abs(p)**2,0); nrm.append(q.sum()); xs.append(np.sum(q*x)); ys.append(np.angle(np.sum(q*ph)))
        p=stepC(p,w,th*np.ones_like(x),b)
    return np.array(xs),np.unwrap(ys)*Ly/(2*np.pi),np.array(nrm)
