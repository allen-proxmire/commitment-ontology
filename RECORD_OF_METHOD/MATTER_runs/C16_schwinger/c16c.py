# C16 read at bare m = 0 throughout (the cold read's points): the levels' speed and end correction from the two chains' gaps at m = 0,
# the third level predicted from the first two, and the local answer of the mass to the bare mass (N = 8, m = -0.02, 0, +0.02).
import numpy as np, re, os, sys
d0=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,d0)
rows=[l for l in open(os.path.join(d0,"c16_out.txt")) if l.startswith("g = ")]; gaps={}
for l in rows:
    g=float(re.search(r"g = ([\d.]+)",l).group(1)); N=int(re.search(r"N = (\d+)",l).group(1)); gaps[(g,N)]=[float(x) for x in l.split("gaps at m = 0: ")[1].split()]
for g in (0.5,0.75,1.0):
    S={N:(gaps[(g,N)][1]**2-gaps[(g,N)][0]**2)/3 for N in (8,10)}; a={N:np.pi/np.sqrt(S[N]) for N in S}; v=2/(a[10]-a[8]); d=v*a[8]-8
    line=f"g = {g}, m = 0: speed v = {v:.3f}, end correction d = {d:.2f}"
    for N in (8,10):
        M2=gaps[(g,N)][0]**2-S[N]; e3=np.sqrt(M2+9*S[N]); line+=f"; N = {N}: third level predicted {e3:.4f}, found {gaps[(g,N)][2]:.4f} ({(gaps[(g,N)][2]/e3-1)*100:+.1f}%)"
    print(line)
from c16 import Chain
ch=Chain(8)
def M(m,g):
    w,_=ch.low(m,g,k=4); e=w[1:]-w[0]; return np.sqrt(e[0]**2-(e[1]**2-e[0]**2)/3)
for g in (0.5,0.75,1.0): print(f"g = {g}, N = 8: dM/dm at m = 0 (from m = -0.02 and +0.02): {(M(0.02,g)-M(-0.02,g))/0.04:.2f}")
