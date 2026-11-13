# G12: the directed hop on both axes. Nudges b_x on x-relations and b_y on y-relations (fields over places).
# Step: U = C_x C_y A_x A_y F(theta) A_y A_x C_y C_x  (conveyors: brickwork, even then odd links, rotation by b/2,
# generator i|j+1><j| - i|j><j+1|, spin-blind). Drift per axis: 2 sin b.
import numpy as np
exec(open('../G6_light_bending/g6.py').read().replace("Lx,Ly=400,256","Lx,Ly=LX,LY"))
def conv(p,B,axis):
    # axis 1 = x (rows), 2 = y (cols); B array (Lx,Ly): nudge on the link from each place to its + neighbour
    for par in (0,1):
        if axis==2:
            a=p[:,:,par::2]; c=np.roll(p,-1,axis=2)[:,:,par::2]; cb=np.cos(B[:,par::2]/2); sb=np.sin(B[:,par::2]/2)
            q=p.copy(); q[:,:,par::2]=cb*a-sb*c; tmp=np.roll(q,-1,axis=2); tmp[:,:,par::2]=sb*a+cb*c; p=np.roll(tmp,1,axis=2)
        else:
            a=p[:,par::2,:]; c=np.roll(p,-1,axis=1)[:,par::2,:]; cb=np.cos(B[par::2,:]/2); sb=np.sin(B[par::2,:]/2)
            q=p.copy(); q[:,par::2,:]=cb*a-sb*c; tmp=np.roll(q,-1,axis=1); tmp[:,par::2,:]=sb*a+cb*c; p=np.roll(tmp,1,axis=1)
    return p
yv=(np.arange(Ly)-Ly//2)[None,:]*np.ones((Lx,1))
def stepD(p,ang,Bx,By):
    p=conv(conv(p,Bx,1),By,2)
    p=Ax(Ay(Fop(Ay(Ax(p,w0),w0),ang),w0),w0)
    return conv(conv(p,By,2),Bx,1)
kxs=2*np.pi*np.fft.fftfreq(Lx)[:,None]; kys=2*np.pi*np.fft.fftfreq(Ly)[None,:]
def moments(p):
    q=np.sum(abs(p)**2,0); pk=np.sum(abs(np.fft.fft2(p,axes=(1,2)))**2,0); pk/=pk.sum()
    wrap=lambda k:(k+np.pi)%(2*np.pi)-np.pi
    return np.sum(q*x),np.sum(q*yv),np.sum(pk*wrap(kxs)),np.sum(pk*wrap(kys))
def packet_k(th,kx0,ky0,sig):
    kx=2*np.pi*np.fft.fftfreq(Lx); ky=2*np.pi*np.fft.fftfreq(Ly); phi=np.zeros((2,Lx,Ly),complex)
    for i,a in enumerate(kx):
        aa=(a+np.pi)%(2*np.pi)-np.pi
        for j,b in enumerate(ky):
            bb=(b+np.pi)%(2*np.pi)-np.pi
            amp=np.exp(-(((aa-kx0)*sig)**2+((bb-ky0)*sig)**2)/2)
            if amp<1e-10: continue
            ev,V=np.linalg.eig(Uk(a,b,th,w0)); phi[:,i,j]=amp*V[:,np.argmin(np.angle(ev))]
    p=np.array([np.fft.ifft2(phi[0]),np.fft.ifft2(phi[1])]); p=np.roll(p,(Lx//2,Ly//2),axis=(1,2)); return p/np.sqrt(np.sum(abs(p)**2))
