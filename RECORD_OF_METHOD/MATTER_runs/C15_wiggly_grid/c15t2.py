# c15t's "angle ignored" case, its path measured in that web's own flat positions (lines at right angles: X' = x, Y' = sum of a_y along y),
# not in the leaning web's. Question: is it straight there?
import numpy as np, os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"c15t.py")).read().split("K=gauss(")[0]+"def dsin"+open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"c15t.py")).read().split("def dsin",1)[1].split("for nm,ua in")[0])
Yp=np.cumsum(ay,axis=1); Yp=Yp-Yp[:,L//2][:,None]; W=x+1j*Yp
v,dev,turn,head=run(False,-40.0,-60.0,np.radians(60))
print(f"angle ignored, in its own web's positions: speed {v:.4f}, turning by {turn:+.2f} degrees, sideways departure from a straight line at most {dev:.3f} hop over {v*T:.0f} hops")
