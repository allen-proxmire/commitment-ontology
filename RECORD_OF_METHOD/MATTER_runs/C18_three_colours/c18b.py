# Whose share is the pool's? c18's chain (three colours, bare mass 0, no tail). Two neutral wholes: a quark and an antiquark (first excitation of the
# filled lower states) and three quarks. Each one's energy above the vacuum, less what its quarks cost with the colour field off (g = 0), is the part
# the field adds: P_M and P_B.
# Stated before running: if the field's part goes by the count of quarks (a half each in the pair, a third each in the three), P_B/P_M = 1.5;
# if it goes by the string (in one dimension the same string lies under both), P_B/P_M is about 1.
#   By the count: P_B/P_M > 1.3 at N = 4, every g.  By the string: < 1.2.  Between, or changing side with g: unclear.  Outcome not known beforehand.
import numpy as np, time
from c18 import low, Colour, r
for N in (3,4):
    c=Colour(N,1); h=(c.hop+0j).toarray()+np.diag((0.0+r)*c.sz); e=np.sort(np.linalg.eigvalsh(h)); ep=e[N]; eh=-e[N-1]
    print(f"N = {N}, field off: a quark costs {ep:.4f}, an antiquark {eh:.4f}; pair {ep+eh:.4f}, three quarks {3*ep:.4f}",flush=True)
    for g in ((0.5,1.0,1.5,2.0) if N==3 else (1.0,1.5,2.0)):
        t0=time.time(); v=low(N,(N,N,N),0.0,g,0,k=2); b=low(N,(N+1,N+1,N+1),0.0,g,0,k=1)
        M=v[1]-v[0]; B=b[0]-v[0]; PM=M-(ep+eh); PB=B-3*ep
        print(f"   g = {g}: pair {M:.4f}, three {B:.4f} (ratio {B/M:.3f}); field's part: pair {PM:+.4f}, three {PB:+.4f}; P_B/P_M = {PB/PM:.3f}   ({time.time()-t0:.0f} s)",flush=True)
# Weak-field check, added after the run: the ratio as g falls (3 places).
N=3; c=Colour(N,1); h=(c.hop+0j).toarray()+np.diag(r*c.sz); e=np.sort(np.linalg.eigvalsh(h)); ep=e[N]; eh=-e[N-1]
for g in (0.1,0.25):
    v=low(N,(N,N,N),0.0,g,0,k=2); b=low(N,(N+1,N+1,N+1),0.0,g,0,k=1); PM=v[1]-v[0]-(ep+eh); PB=b[0]-v[0]-3*ep
    print(f"N = 3, g = {g}: field part pair {PM:+.5f}, three {PB:+.5f}; P_B/P_M = {PB/PM:.3f}   (weak-field check, added after the run)")
