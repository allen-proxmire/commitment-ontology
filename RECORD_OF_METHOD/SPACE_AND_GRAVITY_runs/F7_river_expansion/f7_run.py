# Expansion as the river: a uniform ball of matter sourcing its own outward drift b = +sqrt(2 G M(<r)/r)
# (F2f's collapse run in reverse; radial reduction, flow units). Flat slices (N = psi = 1); the drift from the constraint
# with zero energy is the k = 0 expansion: shells follow r_q^{3/2} = r_q0^{3/2} + (3/2) sqrt(r_s q) t, i.e. a ~ t^{2/3},
# and H^2 = (8 pi G/3) rho, which in these units reads H(t) = sqrt(r_s)/R(t)^{3/2}.
import numpy as np,scipy.sparse as sp,sys
from scipy.sparse.linalg import expm_multiply
sys.path.insert(0,'../F1_flow_gravity'); from flow1d import build,sx,sz,I2
tau=0.4; r_=0.5; m=0.5
def ball(L,R,edge):
    x=np.arange(L); prof=np.where(x<R,x/R,0.0)*0.5*(1-np.tanh((x-R)/edge))
    ks=2*np.pi*np.fft.fftfreq(L); f=np.fft.fft(prof); ph=np.zeros((L,2),complex)
    for i,k in enumerate(ks):
        if abs(f[i])<1e-10*np.abs(f).max(): continue
        h=np.sin(k)*sx+(r_*(1-np.cos(k))+m)*sz; e,v=np.linalg.eigh(h); u=v[:,1]; u=u*np.exp(-1j*np.angle(u[0])); ph[i]=f[i]*u
    p=np.fft.ifft(ph,axis=0); return (p/np.linalg.norm(p)).reshape(-1)
def run(scale):
    L=2400*scale; R=300*scale; edge=12*scale; rs=60.0*scale; x=np.arange(L)
    S=sp.diags([np.ones(L-1)],[1],shape=(L,L),format='lil'); S[L-1,0]=1; S=S.tocsr(); sn=(S-S.T)/(2j)
    H0=build(L,m,r_,np.ones(L),np.ones(L)); p=ball(L,R,edge); qs=[0.2,0.4,0.6,0.8]
    def radii(p):
        d=(np.abs(p.reshape(L,2))**2).sum(1); M=np.cumsum(d); M/=M[-1]; return M,np.array([np.interp(q,M,x) for q in qs])
    M,r0=radii(p); T=int(3.0*(2/3)*R**1.5/np.sqrt(rs)/tau); out=[]
    for n in range(1,T+1):
        rm=np.maximum(x+0.5,1.0); b=np.minimum(np.sqrt(rs*np.interp(x+0.5,x,M)/rm),3.0)     # outward
        Bd=sp.diags(b); p=expm_multiply(-1j*tau*(H0+sp.kron(0.5*(Bd@sn+sn@Bd),I2)),p); M,rq=radii(p)
        if n in (T//3,2*T//3,T):
            t=n*tau; pred=(r0**1.5+1.5*np.sqrt(rs*np.array(qs))*t)**(2/3); out.append((t,rq/pred,rq/r0))
    return out,qs
ok=True
for scale in (1,2):
    out,qs=run(scale)
    for t,ratio,grow in out:
        print(f"scale {scale}, t={t:.0f}: shells q={qs}: measured/predicted {np.round(ratio,4)}; growth {np.round(grow,3)} (one factor for all shells = Hubble's law: spread {grow.std()/grow.mean():.4f})",flush=True)
        ok&=np.all(np.abs(ratio-1)<0.05)
print("F7",'holds' if ok else 'does not hold',"(not registered; a reversal of F2f)")
