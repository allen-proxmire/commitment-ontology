# Whose rate is it? c16's chain, the charges' mass taken from none to heavy. The lowest neutral pattern's mass M against the two charges' own, 2 m_eff
# (m_eff = m - m*, m* the bare mass at which the charges are massless, from c16). Share s = 2 m_eff / M: 0 where the rate is all the whole's (the proton's case),
# near 1 where the parts' rates add up (the atom's case). M from the two lowest levels at each N, as in c16: M^2 = e1^2 - (e2^2 - e1^2)/3.
# Stated before running: with x = m_eff/g, let x25 and x75 be where s crosses 0.25 and 0.75 (N = 10, g = 0.75 and 1.0).
#   A sharp switch: x75/x25 < 3.  A slow slide: x75/x25 > 10.  Between: unclear.  Expected: a slide (about 20).
#   Check of the heavy end: at the heaviest mass M - 2 m_eff within 30% of the linear string's 2.338 (g^4 / 4 m_eff)^(1/3).
import numpy as np, os, sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import c16
chains={N:c16.Chain(N) for N in (8,10)}
xs=[0.0,0.05,0.1,0.2,0.3,0.5,0.75,1.0,1.5,2.0,2.5]
for g in (0.75,1.0):
    res={}
    for N in (8,10):
        ch=chains[N]; ms,_,_=c16.mstar(ch,g); row=[]
        for x in xs:
            w,_=ch.low(ms+x*g,g,k=4); e=w-w[0]; M2=e[1]**2-(e[2]**2-e[1]**2)/3; row.append((np.sqrt(max(M2,0)),e[1],e[2],e[3]))
        res[N]=(ms,row)
    print(f"g = {g}: m* = {res[10][0]:+.4f} (N = 10), {res[8][0]:+.4f} (N = 8)")
    print("   m_eff/g   M/g (N=10)  M/g (N=8)   share s (N=10)  s (N=8)   gaps N=10")
    s10=[]
    for i,x in enumerate(xs):
        M10=res[10][1][i][0]; M8=res[8][1][i][0]; s=2*x*g/M10; s8=2*x*g/M8; s10.append(s)
        print(f"   {x:5.2f}    {M10/g:7.3f}    {M8/g:7.3f}      {s:6.3f}        {s8:6.3f}    "+" ".join(f"{v:.3f}" for v in res[10][1][i][1:]),flush=True)
    s10=np.array(s10); lx=np.array(xs)
    def cross(v):
        i=np.nonzero((s10[:-1]<v)&(s10[1:]>=v))[0]
        if len(i)==0: return None
        i=i[0]; return lx[i]+(v-s10[i])*(lx[i+1]-lx[i])/(s10[i+1]-s10[i])
    a,b=cross(0.25),cross(0.75)
    print(f"   s = 0.25 at m_eff/g = {a}, s = 0.75 at {b}; ratio {None if (a is None or b is None) else round(b/a,1)}")
    x=xs[-1]; M=res[10][1][-1][0]; bind=M-2*x*g; lin=2.338*(g**4/(4*x*g))**(1/3)
    print(f"   heavy end (m_eff/g = {x}): M - 2 m_eff = {bind:.3f}; linear string {lin:.3f}; ratio {bind/lin:.2f}")
    d=np.diff(s10)/np.diff(lx); print("   slope ds/dx between points: "+" ".join(f"{v:.2f}" for v in d))
