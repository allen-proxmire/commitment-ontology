# Uniform nudge b: light along +y and -y, and matter at rest (theta 0.2, 0.4). Drift and tilt against 2 sin b.
LX,LY=128,512
exec(open('g7.py').read())
T=120; t=np.arange(T+1)
for b in [0.0,0.02,0.05]:
    out=[]
    for name,th,k0 in [("light +y",0,0.2),("light -y",0,-0.2),("matter 0.2",0.2,0),("matter 0.4",0.4,0)]:
        xs,ys,n=traj(th,k0,b,25,T); v=np.polyfit(t,ys,1)[0]; out.append(v)
        print(f"b={b} {name}: v_y={v:+.5f}  x drift {xs[-1]-xs[0]:+.4f}  norm {n[-1]:.12f}")
    print(f"   light: (v+ - |v-|)/2 = {(out[0]+out[1])/2:+.5f}, mean speed {(out[0]-out[1])/2:.5f};  matter drifts {out[2]:+.5f}, {out[3]:+.5f}")
