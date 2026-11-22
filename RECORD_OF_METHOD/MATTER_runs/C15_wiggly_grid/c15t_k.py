# c15t's curvature check with a comparison that is in fact curved (c15t's own, a_y = 1 + xy/(2 Lw^2), is flat: its a_y is linear in x).
import numpy as np, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"c15t.py")).read().split("K=gauss(")[0])
for nm,(E,F,G) in (("the leaning web, lengths and diagonal",(ax**2,ax*ay*cth,ay**2)),
                   ("the same lengths with the angle ignored",(ax**2,0*ax,ay**2)),
                   ("curved, right angles: a_y = 1 + 0.1 sin(2 pi x/64)",(ax**2,0*ax,(1+0.1*np.sin(2*np.pi*x/64))**2)),
                   ("curved by its angle alone: unit lengths, cos(theta) = 0.2 sin(2 pi x/64) sin(2 pi y/64)",(ax**2,0.2*np.sin(2*np.pi*x/64)*np.sin(2*np.pi*y/64),ax**2))):
    K=gauss(E,F,G); print(f"{nm}: curvature rms {np.sqrt((K**2).mean()):.1e} per hop^2")
