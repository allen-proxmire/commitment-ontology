# Closed loop in 2D with the stretch: one field Phi (the lapse N = 1 - Phi and the hop stretch psi^2 = 1 + Phi, gamma = 1)
# sourced by rest-energy density, evolving by the lattice wave equation at the walk's light speed:
#   Phi_tt = c0^2 (lap Phi + kappa (rho - <rho>)),   static: Phi = -(kappa m / 2 pi) ln r + const
# felt through P7f: mass flip theta N, Wilson flip 2 cos w = c0 N / psi^2. No self-pull.
import numpy as np, sys
exec(open('../G6_light_bending/g6.py').read().replace("Lx,Ly=400,256","Lx,Ly=LX,LY").replace("w0=0.3","w0=5*np.pi/16"))
yv=(np.arange(Ly)-Ly//2)[None,:]*np.ones((Lx,1))
def lap(h): return np.roll(h,1,0)+np.roll(h,-1,0)+np.roll(h,1,1)+np.roll(h,-1,1)-4*h
def field_step(P,V,rho,kappa,sub=3):
    dt=1.0/sub
    for s in range(sub):
        V+=dt*c0**2*(lap(P)+kappa*(rho-rho.mean())); P+=dt*V
def flips(P,stretch=1):
    P=P-P.mean()   # a uniform part only relabels every clock alike
    N=1-P; ps2=1+stretch*P; return N, np.arccos(np.clip(c0*N/ps2/2,-1,1))
def pk_at(th,k0x,k0y,sig,x0,y0):
    p=packet(th,k0y,sig) if k0x==0 else None
    return np.roll(p,(x0,y0),axis=(1,2))
