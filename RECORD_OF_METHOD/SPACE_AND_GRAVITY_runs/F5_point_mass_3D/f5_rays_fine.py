# F5 diagnostic (after the run): the packet average with the impact-parameter spread integrated finely.
# The deflection depends on the start offset (x, z) mainly through the impact parameter; tabulate the ray deflection on a grid
# of offsets along x (z = 0) and in z, using rho = |(B + x, z)|, then integrate over the packet's Gaussian; momentum spread
# folded in as a factor from Gauss-Hermite over (k_x, k_y) at zero offset.
import numpy as np,sys; sys.path.insert(0,'.')
exec(open('f5_rays.py').read().split('# Gauss-Hermite')[0])
def defl(x0,z0,kx,ky,full):
    return (solve_ivp(rhs,(0,T_FLOW),[x0,Y0,z0,kx,ky,0.],args=(full,),rtol=1e-8,atol=1e-10).y[3,-1]-kx)/K0
sx=sig/np.sqrt(2); sk=1/(sig*np.sqrt(2))
rhos=np.linspace(Bimp-4.5*sx,Bimp+4.5*sx,31); rhos=rhos[rhos>0.5]
gx,gw=np.polynomial.hermite_e.hermegauss(7); gw/=gw.sum()
for full in (False,True):
    F=np.array([defl(rh-Bimp,0.,0.,K0,full) for rh in rhos])
    xs=np.linspace(-5*sx,5*sx,201); X,Z=np.meshgrid(xs,xs); RHO=np.hypot(Bimp+X,Z); Wt=np.exp(-(X**2+Z**2)/(2*sx**2)); Wt/=Wt.sum()
    # deflection points toward the mass: its x-component is F(rho) times (B+x)/rho
    pos=np.sum(Wt*np.interp(RHO,rhos,F,left=F[0],right=F[-1])*(Bimp+X)/RHO)
    kf=sum(wa*wb*defl(0.,0.,a*sk,K0+b*sk,full) for a,wa in zip(gx,gw) for b,wb in zip(gx,gw))/defl(0.,0.,0.,K0,full)
    print(f"{'full ' if full else 'clock'}: centre ray {defl(0.,0.,0.,K0,full):+.5e}; position-averaged {pos:+.5e}; momentum factor {kf:.4f}; packet average {pos*kf:+.5e}",flush=True)
