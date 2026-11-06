"""R11: three Dirac walks sharing one flip cycle. See REGISTRATION.md."""
import numpy as np, json
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
P=lambda j,k: Pp[j]*np.exp(1j*k)+Pm[j]*np.exp(-1j*k)
S=np.roll(np.eye(3),1,axis=0); T=(S+S.T)/2
I3=np.eye(3); w=np.exp(2j*np.pi/3)
def U(k,theta):
    hop=np.kron(P(0,k[0])@P(1,k[1])@P(2,k[2]),I3)
    from scipy.linalg import expm
    M=expm(-1j*theta*np.kron(beta,T))
    return hop@M@np.kron(P(2,k[2])@P(1,k[1])@P(0,k[0]),I3)
theta=0.3; out={}
# (1) symmetry: [U, 1⊗S] = 0
rng=np.random.default_rng(0); ks=[tuple(rng.uniform(-np.pi,np.pi,3)) for _ in range(50)]
Sk=np.kron(np.eye(4),S)
out['commutator_max']=float(max(np.abs(U(k,theta)@Sk-Sk@U(k,theta)).max() for k in ks))
# (2) sector dispersions: project on eigenvectors of S (charge k: eigenvalue w^k)
vals,vecs=np.linalg.eig(S); sect={}
for kk in range(3):
    idx=int(np.argmin(np.abs(vals-w**kk))); v=vecs[:,idx]; Pk=np.kron(np.eye(4),np.outer(v,v.conj()))
    # effective 4x4 step in this sector
    def Uk(kv):
        Uf=U(kv,theta); V=np.kron(np.eye(4),v.reshape(3,1)); return V.conj().T@Uf@V
    E0=np.sort(np.angle(np.linalg.eigvals(Uk((0,0,0)))))
    Es=[np.min(np.abs(np.angle(np.linalg.eigvals(Uk((q,0,0)))))) for q in (0,0.05,0.1,0.2)]
    sect[kk]={'quasienergies_at_k0':np.round(E0,4).tolist(),'lowest_E_vs_q':np.round(Es,4).tolist(),'eff_mass_angle':float(theta*np.cos(2*np.pi*kk/3))}
    print(f"sector k={kk} (triality {kk}): E(k=0)={np.round(E0,3)}  lowest E at q=0,0.05,0.1,0.2 -> {np.round(Es,3)}  (theta*cos(2pi k/3)={theta*np.cos(2*np.pi*kk/3):.3f})")
out['sectors']={str(k):v for k,v in sect.items()}
print("commutator max:",out['commutator_max'])
json.dump(out,open('r11_result.json','w'),indent=1)
