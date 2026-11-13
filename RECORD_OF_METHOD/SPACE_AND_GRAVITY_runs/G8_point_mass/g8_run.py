import sys
exec(open('g8.py').read())
T=int(2*abs(Y0)/1.85); A=0.6
res={}
for side in (1,-1):
    base=run(0,0,T,side); print(f"side {side}, no field: kx={base[0]:+.2e} final x={base[2]:.2f}"); sys.stdout.flush()
    for label,st in [("clock only",0),("clock+stretch",1)]:
        pp=run(A,st,T,side); dkx=(pp[0]-base[0])*side   # toward the mass counts negative
        res[(label,side)]=dkx
        print(f"  {label}: delta kx toward mass = {dkx:+.5e}  angle {dkx/K0:+.5e}  x shift {(pp[2]-base[2])*side:+.3f}"); sys.stdout.flush()
for label in ["clock only","clock+stretch"]:
    m=(res[(label,1)]+res[(label,-1)])/2; print(f"{label}: mean angle {m/K0:+.5e}")
yend=Y0+T*1.85; geo=(abs(Y0)/np.hypot(Y0,B)+yend/np.hypot(yend,B))/2
cl=(res[("clock only",1)]+res[("clock only",-1)])/2; fu=(res[("clock+stretch",1)]+res[("clock+stretch",-1)])/2
print(f"continuum full deflection 4A/b x path factor = {4*A/B*geo:.5e}; measured/continuum: full {abs(fu/K0)/(4*A/B*geo):.4f}, clock {abs(cl/K0)/(2*A/B*geo):.4f}; ratio full/clock {fu/cl:.4f}")
