# Can the mass flip carry a direction in kind space on CO's step? One pattern, two kinds: 4 (the step's four) x 2 (kind) = 8 at a place.
# G5 = -i alpha_x alpha_y alpha_z commutes with the alphas and anticommutes with beta; P_L = (1 - G5)/2, P_R = (1 + G5)/2.
# A turn of the left-handed part's kind: g_L = P_R x 1 + P_L x g, g in SU(2).
# Flip with a direction: T(A) = beta P_L x A + beta P_R x A^dagger, A a 2x2 matrix (A = m V: one mass, direction V; A = V diag(m_u, m_d): two masses).
# Step: U = exp(-i tau H), H = sum_j alpha_j sin k_j x 1 + T(A) + lifting term, w = r sum_j (1 - cos k_j), r = 1/2.
#   (a) lifting term carrying the direction too: T(A + w V).   (b) lifting term bare: w beta x 1.
# Checks: (1) g_L U(A) g_L^dagger = U(A g^dagger) in form (a), exactly; (2) the energies do not depend on the direction in (a), and do in (b);
#         (3) at r = 0 the turn is exact, and the copies at the zone's corners: of which hand, in effect, is the part P_L picks?
import numpy as np
from scipy.linalg import expm
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]; I2=np.eye(2); Z=np.zeros((2,2))
al=[np.block([[Z,si],[si,Z]]) for si in s]; be=np.block([[I2,Z],[Z,-I2]]).astype(complex); G5=-1j*al[0]@al[1]@al[2]; PL=(np.eye(4)-G5)/2; PR=(np.eye(4)+G5)/2
print("G5: squares to one",np.allclose(G5@G5,np.eye(4)),"; commutes with the alphas",all(np.allclose(G5@a,a@G5) for a in al),"; anticommutes with beta",np.allclose(G5@be,-be@G5))
rng=np.random.default_rng(1)
def su2():
    v=rng.normal(size=3); return expm(1j*sum(v[i]*s[i] for i in range(3)))
T=lambda A: np.kron(be@PL,A)+np.kron(be@PR,A.conj().T)
def H(k,A,r,form,V=None):
    w=r*sum(1-np.cos(k)); kin=sum(np.kron(al[j]*np.sin(k[j]),I2) for j in range(3))
    return kin+(T(A+w*V) if form=="a" else T(A)+w*np.kron(be,I2))
tau=0.5; k=np.array([0.3,0.5,0.8])*0.1/np.linalg.norm([0.3,0.5,0.8])*10   # |k| = 1.0, a short wavelength, to show the lifting term at full size
for m in (0.1,):
    V=su2(); g=su2(); gL=np.kron(PR,I2)+np.kron(PL,g)
    Ua=expm(-1j*tau*H(k,m*V,0.5,"a",V)); Ua2=expm(-1j*tau*H(k,m*V@g.conj().T,0.5,"a",V@g.conj().T))
    print(f"(1) lifting term carrying the direction: | g_L U(V) g_L^dagger - U(V g^dagger) | = {np.linalg.norm(gL@Ua@gL.conj().T-Ua2):.1e}")
    for kk,lab in ((k,"|k| = 1.0"),(k*0.1,"|k| = 0.1"),(k*0.01,"|k| = 0.01")):
        ea=[np.sort(np.linalg.eigvalsh(H(kk,m*W,0.5,"a",W)))[-1] for W in (su2() for _ in range(6))]
        eb=[np.sort(np.linalg.eigvalsh(H(kk,m*W,0.5,"b")))[[4,-1]] for W in [np.eye(2),-np.eye(2)]+[su2() for _ in range(4)]]
        w=0.5*sum(1-np.cos(kk)); eb=np.array(eb)
        print(f"(2) {lab}, m = {m}: lifting term w = {w:.2e}; form (a): top energy spread over directions {max(ea)-min(ea):.1e}; form (b): energies range {eb.min():.5f} to {eb.max():.5f} with the direction (masses between |m - w| = {abs(m-w):.5f} and m + w = {m+w:.5f})")
    A=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); sv=np.linalg.svd(A,compute_uv=False); e=np.sort(np.linalg.eigvalsh(H(np.zeros(3),A,0.5,"a",np.eye(2))))
    print(f"    a general A at k = 0: the two kinds' masses are A's singular values {sv[1]:.4f}, {sv[0]:.4f}; energies found {e[4]:.4f}, {e[-1]:.4f}")
# (3) r = 0, massless: the copies. Near corner K (components 0 or pi), H = sum_j c_j alpha_j q_j, c_j = cos K_j = +-1: a Dirac pattern with alphas a_j = c_j alpha_j,
#     whose own spin is S_1 = -(i/2) a_2 a_3 (and cyclic). A positive-energy massless state has helicity (its own spin along its motion) equal to its hand.
#     Measured: that helicity times G5. +1: the part P_L picks is left-handed there as at the origin; -1: it is right-handed in effect.
import itertools
out={}
for K in itertools.product((0,np.pi),repeat=3):
    q=np.array([0.3,0.5,0.8])*1e-3; kk=np.array(K)+q; c=np.cos(np.array(K)); Hk=sum(al[j]*np.sin(kk[j]) for j in range(3)); w_,v=np.linalg.eigh(Hk); pos=v[:,w_>0]
    a_=[c[j]*al[j] for j in range(3)]; S=[-1j/2*a_[x]@a_[y] for x,y in ((1,2),(2,0),(0,1))]; hel=2*sum(S[j]*q[j] for j in range(3))/np.linalg.norm(q)
    out[tuple(int(x>0) for x in K)]=np.trace(pos.conj().T@(hel@G5)@pos).real/2
print("(3) r = 0: the pattern's own helicity times G5, positive-energy states, at each corner of the zone (1 = that axis at pi):")
print("    "+"; ".join(f"{k_}: {v_:+.2f}" for k_,v_ in out.items()),"->",sum(1 for v_ in out.values() if v_>0.5),"as at the origin,",sum(1 for v_ in out.values() if v_<-0.5),"reversed")
