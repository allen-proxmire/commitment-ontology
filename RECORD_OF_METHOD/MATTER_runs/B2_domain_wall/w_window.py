import numpy as np,sys; sys.path.insert(0,'.')
exec(open('scout.py').read().split('for th in')[0])
# across the Wilson window: C_upper at theta=+-0.5, and the smallest 0-gap and pi-gap along the path theta in [-0.5,0.5] excluding the closing at theta=0
for w in np.linspace(np.pi/4+0.01,3*np.pi/8-0.01,12):
    Cp=chern(0.5,w,40); Cm=chern(-0.5,w,40)
    path=np.linspace(-0.5,0.5,11); gp=min(gaps(t,w,40)[1] for t in path); g0=min(min(gaps(0.5,w,40)[0],gaps(-0.5,w,40)[0]),9)
    print(f"w={w:.3f} ({w/np.pi*16:.2f} pi/16)  C(+0.5)={Cp:+.0f} C(-0.5)={Cm:+.0f}  0-gap at walls={g0:.3f}  min pi-gap on path={gp:.3f}")
