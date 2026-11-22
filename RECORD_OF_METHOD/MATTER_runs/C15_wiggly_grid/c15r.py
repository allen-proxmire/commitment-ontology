# Which length does the lifting term carry? r multiplies a length; with no drawing the only lengths are the relations' own.
#  G   (c15p) -(r/2) sigma_z [ (psi(x+1) - psi(x))/a_right + (psi(x-1) - psi(x))/a_left ] / V : a fixed reference length (the mean hop) times the true second difference.
#  G'  (here) -(r/2) sigma_z [ (psi(x+1) - psi(x)) + (psi(x-1) - psi(x)) ] / V : each link's difference weighted by that link's own length.
# On an even web of hop length a, G goes as r/a^2 and G' as r/a, the step's own {1/a, r(1 - cos k)}/2. Same web and measure as c15p. Not registered.
import numpy as np
import os; d=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(d,"c15n.py")).read().split("tab={}")[0])                                   # the web and the link hops
exec(open(os.path.join(d,"c15p.py")).read().split("exec(src)\n")[1].split("\ntab={}\n")[0])        # r, run2
ox=(1/np.sqrt(Vx*np.roll(Vx,-1)))[:,None]; oy=(1/np.sqrt(Vy*np.roll(Vy,-1)))[None,:]; dx_=(2/Vx)[:,None]; dy_=(2/Vy)[None,:]
def lift_Gp(p):
    lap=ox*np.roll(p,-1,1)+np.roll(ox,1,0)*np.roll(p,1,1)-dx_*p + oy*np.roll(p,-1,2)+np.roll(oy,1,1)*np.roll(p,1,2)-dy_*p
    return -(r/2)*np.array([lap[0],-lap[1]])
for k in (0.15,0.3,0.6):
    k0,rate,out=run2(lambda p: H_L(p)+lift_Gp(p),k); print(f"k = {k0:.3f}, lifting term with each link's own length: forward share "+" ".join(f"{o:.5f}" for o in out)+f"; fall over 150: {out[0]-out[-1]:.2e}",flush=True)
