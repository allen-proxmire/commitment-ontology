# Rigid-rotation shift: drift v_s = omega (-y, x)  ->  nudges b_x = asin(-omega y/2), b_y = asin(omega x/2).
# GR (and H = E(k) + v_s.k): a packet moving along x with velocity v feels a_y = 2 omega v (Coriolis), k_y grows at omega k_x;
# light and matter alike. Fail: a_y / (2 omega v) off by more than the packet's spread, or different for light and matter.
LX,LY=400,400
exec(open('g12.py').read())
import sys
T=60; t=np.arange(T+1)
def run(th,kx0,sig,om):
    Bx=np.arcsin(-om*yv/2); By=np.arcsin(om*x/2)   # link from place (x,y) to its + neighbour; drift at the link's start
    p=packet_k(th,kx0,0,sig); M=[]
    for s in range(T+1):
        M.append(moments(p)); p=stepD(p,th*np.ones_like(x),Bx,By)
    M=np.array(M); return M
om=4e-4
for name,th,kx0,sig in [("light",0,0.3,25),("matter 0.4",0.4,0.15,25),("matter 0.2",0.2,0.08,30)]:
    Mp=run(th,kx0,sig,om); Mm=run(th,kx0,sig,-om)
    vx=np.polyfit(t,(Mp[:,0]+Mm[:,0])/2,1)[0]
    ay=2*np.polyfit(t,(Mp[:,1]-Mm[:,1])/2,2)[0]
    dky=np.polyfit(t,(Mp[:,3]-Mm[:,3])/2,1)[0]; kx=np.mean(Mp[:,2])
    hh=1e-4; Exx=(E(kx0,hh,th,w0)-2*E(kx0,0,th,w0)+E(kx0,-hh,th,w0))/hh**2; ray=om*(Exx*np.sin(kx0)+vx)
    print(f"{name}: lattice ray a_y={ray:+.4e}, measured/ray={ay/ray:.4f};  v_x={vx:.4f}  a_y={ay:+.4e}  2*omega*v={2*om*vx:.4e}  ratio={ay/(2*om*vx):.4f} | dk_y/dt={dky:+.4e} vs omega*sin(k_x)={om*np.sin(kx):.4e} ratio {dky/(om*np.sin(kx)):.4f}"); sys.stdout.flush()
