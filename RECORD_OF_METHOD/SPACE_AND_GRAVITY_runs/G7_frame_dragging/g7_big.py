# Large nudges: tilt past the old reach of 2 hops per tick, still the same for light and matter.
LX,LY=64,1024
exec(open('g7.py').read())
# large nudges: does the tilt go past the walk's old reach (2 hops/tick) and stay universal?
T=100; t=np.arange(T+1)
for b in [0.1,0.2,0.4]:
    v=[np.polyfit(t,traj(th,k0,b,20,T)[1],1)[0] for th,k0 in [(0,0.1),(0,-0.1),(0.4,0)]]
    print(f"b={b}: light +y {v[0]:+.4f}, light -y {v[1]:+.4f}  (tilt {(v[0]+v[1])/2:+.4f}, mean speed {(v[0]-v[1])/2:.4f});  matter drift {v[2]:+.4f};  sin(b)*2 = {2*np.sin(b):.4f}")
