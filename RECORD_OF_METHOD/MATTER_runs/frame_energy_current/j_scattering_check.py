import numpy as np
from scipy.optimize import brentq
m,r=0.3,1.0
def E(k): M=m+r*np.sum(1-np.cos(k)); return np.sqrt(np.sum(np.sin(k)**2)+M**2)
def J(k,e=1e-6): return np.array([(E(k+e*d)**2-E(k-e*d)**2)/(4*e) for d in np.eye(3)])
rng=np.random.default_rng(1); out=[]
for scale in (0.05,0.2,0.6):
  ws=[]
  for t in range(200):
    p1,p2=rng.normal(0,scale,3),rng.normal(0,scale,3); P=p1+p2; Et=E(p1)+E(p2)
    n=rng.normal(size=3); n/=np.linalg.norm(n); c=P/2
    f=lambda s: E(c+s*n)+E(P-c-s*n)-Et
    try: s=brentq(f,0,3)
    except ValueError: continue
    p3=c+s*n; p4=P-p3
    dJ=np.linalg.norm(J(p3)+J(p4)-J(p1)-J(p2)); ws.append(dJ/np.linalg.norm(J(p1)+J(p2)+1e-12))
  out.append((scale,np.median(ws),len(ws)))
for o in out: print('momentum scale %.2f (hop units): median relative change of total J in elastic 2->2: %.2e  (%d events)'%o)
