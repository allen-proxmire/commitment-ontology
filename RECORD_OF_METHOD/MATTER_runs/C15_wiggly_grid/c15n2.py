# c15n's comparators with the draws matched (raised by the cold read). Same web, measure and wavelengths as c15n.
#  PV  the place form {w, sigma sin k}/2 with w = 1/V, V = (a_left + a_right)/2 from the SAME link lengths as c15n's link case.
#  LI  the link form 1/sqrt(V V') with V drawn independently per place (not taken from link lengths).
# Both packets dressed as in c15n's link case (PV with c15n's own V and positions; LI with its V and positions from cumulated V).
import numpy as np
src=open(__file__.replace("c15n2","c15n")).read().split("tab={}")[0]; exec(src)
wxV=(1/Vx)[:,None]*np.ones((1,L)); wyV=np.ones((L,1))*(1/Vy)[None,:]
def H_PV(p): return 0.5*(wxV*sgx(dsin(p,0))+sgx(dsin(wxV*p,0))+wyV*sgy(dsin(p,1))+sgy(dsin(wyV*p,1)))
tabn={}
for k in (0.15,0.3,0.6):
    k0,rate,out=run(H_PV,k,True); tabn[('PV',k)]=rate; print(f"k = {k0:.3f}, place form with sizes from the links: loss rate {rate:.3e}",flush=True)
Vx=1+eps*rng.standard_normal(L); Vx*=L/Vx.sum(); Vy=1+eps*rng.standard_normal(L); Vy*=L/Vy.sum()
tx=(1/np.sqrt(Vx*np.roll(Vx,-1)))[:,None]; ty=(1/np.sqrt(Vy*np.roll(Vy,-1)))[None,:]; X=np.concatenate(([0],np.cumsum(Vx)[:-1]))
for k in (0.15,0.3,0.6):
    k0,rate,out=run(H_L,k,True); print(f"k = {k0:.3f}, link form with sizes drawn independently per place: loss rate {rate:.3e}",flush=True)
