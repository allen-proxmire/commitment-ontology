# Exact fade rate of the wall-bound mass. Inner direction at k=0: H = a4 sin p + beta (m + r(1-cos p)), m = +M | -M.
# Zero modes: z = e^{ip} solves (1-r) z^2 + 2(m+r) z - (1+r) = 0 (one chirality), (1+r) z^2 - 2(m+r) z - (1-r) = 0 (the other).
import numpy as np
def rates(M,r):
    out=[]
    for m in (M,-M):
        zs=list(np.roots([1-r,2*(m+r),-(1+r)]))+list(np.roots([1+r,-2*(m+r),-(1-r)]))
        out.append(min(abs(np.log(abs(z))) for z in zs))
    return out   # slowest decay in the +M half, in the -M half
s0=np.eye(2); sx=np.array([[0,1],[1,0]],complex); sz=np.diag([1.,-1]).astype(complex)
A4=np.kron(np.array([[0,-1j],[1j,0]]),s0); B=np.kron(sz,s0)
def gap(L,M,r):
    n=2*L; ms=np.where(np.arange(n)<L,M,-M); H=np.zeros((4*n,4*n),complex)
    for s in range(n):
        H[4*s:4*s+4,4*s:4*s+4]=(ms[s]+r)*B; t=(s+1)%n; hop=A4/(2j)-(r/2)*B
        H[4*t:4*t+4,4*s:4*s+4]+=hop; H[4*s:4*s+4,4*t:4*t+4]+=hop.conj().T
    return np.sort(np.abs(np.linalg.eigvalsh(H)))[0]
for M,r in ((0.5,0.5),(0.3,0.5),(0.8,0.5),(0.5,0.3)):
    kp,km=rates(M,r); Ls=np.arange(24,41,2); g=[gap(L,M,r) for L in Ls]
    fit=-np.polyfit(Ls,np.log(g),1)[0]
    print(f"M={M}, r={r}: exact rates +M half {kp:.5f}, -M half {km:.5f}; slower {min(kp,km):.5f}; measured (even L=24..40) {fit:.5f}")
print("closed form at r=1/2: +M half kappa = -ln(sqrt((2M+1)^2+3) - (2M+1)); at M=1/2: -ln(sqrt7 - 2) =",-np.log(np.sqrt(7)-2),"; -M half at M=1/2: ln(sqrt3) =",np.log(3)/2)
