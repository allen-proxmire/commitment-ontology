import numpy as np, sys
from scipy.optimize import minimize_scalar, brentq
sys.path.insert(0,'../B7_wall_rate_exact')
# ---------- (a) best wall setting ----------
def rate(m,r):   # slowest zero-mode decay rate in a half of mass m
    zs=list(np.roots([1-r,2*(m+r),-(1+r)]))+list(np.roots([1+r,-2*(m+r),-(1-r)]))
    return min(abs(np.log(abs(z))) for z in zs)
r=0.5
f=lambda M: -min(rate(M,r),rate(-M,r))
o=minimize_scalar(f,bounds=(0.05,0.99),method='bounded',options={'xatol':1e-10})
print(f"(a) equal walls, r=1/2: best M = {o.x:.5f}, rate {-o.fun:.5f} per place (M=1/2 gives {-f(0.5):.5f})")
print(f"    unequal walls (+M1 | -M2), r=1/2: the -M2 half is fastest at M2 = r: {rate(-0.5,r):.5f} = ln sqrt3; the +M1 half: " + ", ".join(f"M1={M}: {rate(M,r):.4f}" for M in (0.5,0.7,1.0,2.0)))
s0=np.eye(2); A4=np.kron(np.array([[0,-1j],[1j,0]]),s0); B=np.kron(np.diag([1.,-1]),s0)
def gap(L,M1,M2,r):
    n=2*L; ms=np.where(np.arange(n)<L,M1,-M2); H=np.zeros((4*n,4*n),complex)
    for s in range(n):
        H[4*s:4*s+4,4*s:4*s+4]=(ms[s]+r)*B; t=(s+1)%n; hop=A4/(2j)-(r/2)*B
        H[4*t:4*t+4,4*s:4*s+4]+=hop; H[4*s:4*s+4,4*t:4*t+4]+=hop.conj().T
    return np.sort(np.abs(np.linalg.eigvalsh(H)))[0]
for M1,M2 in ((0.5,0.5),(o.x,o.x),(0.7,0.5),(1.0,0.5)):
    Ls=np.arange(20,33,2); g=[gap(L,M1,M2,r) for L in Ls]; print(f"    exact matrix, walls +{M1:.3f} | -{M2:.3f}: fitted rate {-np.polyfit(Ls,np.log(g),1)[0]:.4f}; predicted {min(rate(M1,r),rate(-M2,r)):.4f}; ring for leftover 1e-6: L = {np.log(1e6)/min(rate(M1,r),rate(-M2,r)):.0f}")
# ---------- (b) how much of the sky has a low ceiling ----------
xs=np.linspace(0.02,0.5,241)
def C(n):
    c2=np.abs(3*(r*r/8-np.sum(n**4,axis=-1)/6))[...,None]; g=xs**3+(1-xs)**3; a=c2/3*g; b=r/2; c=1/(2*xs*(1-xs))
    return np.sqrt(((b+np.sqrt(b*b+4*a*c))/(2*a)).min(-1))
rng=np.random.default_rng(0); n=rng.normal(size=(400000,3)); n/=np.linalg.norm(n,axis=1)[:,None]; Cs=C(n); Ca=C(np.array([[1.,0,0]]))[0]
print(f"(b) ceiling over the sky (in units of the axis value): median {np.median(Cs)/Ca:.3f}, mean {Cs.mean()/Ca:.3f}; share of sky within 10% of the lowest {np.mean(Cs<1.1*Ca)*100:.1f}%, within 25% {np.mean(Cs<1.25*Ca)*100:.1f}%; share within 10% of the highest (1.75) {np.mean(Cs>Cs.max()/1.1)*100:.1f}%")
# ---------- (c) the exact tick limit ----------
def Emax(m,r,b=0.0,bdir=(1,0,0),n=121):
    g=np.linspace(-np.pi,np.pi,n); K=np.stack(np.meshgrid(g,g,g,indexing='ij'),-1)
    E=np.sqrt(np.sum(np.sin(K)**2,-1)+(m+r*np.sum(1-np.cos(K),-1))**2)+b*np.sin(K)@(np.array(bdir)/np.linalg.norm(bdir))
    return E.max()
print(f"(c) free step, r=1/2: largest energy {Emax(0,0.5):.4f} (m=0), {Emax(0.5,0.5):.4f} (m=0.5); corner value m+6r = 3, 3.5; so tick limit tau < pi/(m+6r): {np.pi/3:.4f} at m=0")
for rr in (0.2,0.3,0.4):
    print(f"    r={rr}: largest energy {Emax(0,rr):.4f} against corner 6r = {6*rr:.2f}")
tau=0.4
for d,lab in (((1,0,0),'axis'),((1,1,1),'body diagonal')):
    bl=brentq(lambda b: Emax(0,0.5,b,d,n=81)-np.pi/tau,3,8)
    print(f"    uniform drift along the {lab} at tau=0.4: exact limit |b| < {bl:.3f} (the sufficient bound in the docs gives pi/tau - 3 = {np.pi/tau-3:.3f})")
