# F2f horizons (G17c on the flow step): R = 2000, r_s = 600, run to 0.97 t_c, record when each shell crosses its own horizon r = r_s q.
import numpy as np,sys
src=open('f2f_run.py').read().split('ok=True; dev_by_scale')[0].replace("T=int(0.8*tc/tau)","T=int(0.97*tc/tau)")
exec(src)
hq=(0.5,0.7,0.9,0.97); tc,t,out,cross,r0=run(4,list(hq),hq); rs=600.0
for q,a in zip(hq,r0):
    tp=(a**1.5-(rs*q)**1.5)/(1.5*np.sqrt(rs*q)); tm=cross.get(q,np.nan)
    print(f"q={q}: start r={a:.0f}, crossed own horizon {rs*q:.0f} at t={tm:.0f} vs {tp:.0f} predicted ({tm/tp-1:+.4f})",flush=True)
