# F2f (G17 on the flow step): a uniform ball sourcing its own Painleve-Gullstrand drift, radial reduction, flow units.
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
def run(scale,qs,horizon_qs=()):
    L=1400*scale; R=500*scale; edge=20*scale; rs=150.0*scale; x=np.arange(L)
    S=sp.diags([np.ones(L-1)],[1],shape=(L,L),format='lil'); S[L-1,0]=1; S=S.tocsr(); sn=(S-S.T)/(2j)
    H0=build(L,m,r_,np.ones(L),np.ones(L)); p=ball(L,R,edge)
    tc=(2/3)*R**1.5/np.sqrt(rs); T=int(0.8*tc/tau)
    def radii(p):
        d=(np.abs(p.reshape(L,2))**2).sum(1); d[x>L-200]=0; M=np.cumsum(d); M/=M[-1]; return M,[np.interp(q,M,x) for q in qs]
    M,r0=radii(p); cross={}
    for n in range(T):
        rm=np.maximum(x+0.5,1.0); b=-np.minimum(np.sqrt(rs*np.interp(x+0.5,x,M)/rm),3.0)   # inward drift at link midpoints
        Bd=sp.diags(b); H=H0+sp.kron(0.5*(Bd@sn+sn@Bd),I2)
        p=expm_multiply(-1j*tau*H,p); M,rq=radii(p)
        for q in horizon_qs:
            if q not in cross and np.interp(q,M,x)<=rs*q: cross[q]=(n+1)*tau
    t=T*tau; out=[]
    for q,a,b_ in zip(qs,r0,rq):
        pred=max(a**1.5-1.5*np.sqrt(rs*q)*t,0)**(2/3); out.append((q,a,b_,pred,b_/pred))
    return tc,t,out,cross,r0
ok=True; dev_by_scale=[]
for scale in (1,2,4):
    qs=[0.1,0.3,0.5,0.7,0.9]; hq=(0.5,0.7,0.9,0.97) if scale==4 else ()
    tc,t,out,cross,r0=run(scale,qs+[0.97] if scale==4 else qs,hq)
    line="; ".join(f"q={q}: {a:.0f}->{b:.0f} (pred {p_:.0f}, ratio {rt:.3f})" for q,a,b,p_,rt in out)
    worst=max(abs(o[4]-1) for o in out if o[0] in qs); dev_by_scale.append(worst)
    print(f"scale {scale}: t_c={tc:.0f}, run to t={t:.0f}: {line}; worst {worst:.4f}",flush=True)
    if scale==1: ok&=worst<=0.10
    if cross:
        rs=150.0*scale
        for q in hq:
            a=dict((o[0],o[1]) for o in out)[q]; tp=(a**1.5-(rs*q)**1.5)/(1.5*np.sqrt(rs*q))
            print(f"  horizon q={q}: crossed at t={cross.get(q,float('nan')):.0f} vs {tp:.0f} predicted ({cross.get(q,np.nan)/tp-1:+.4f})",flush=True)
ok&=dev_by_scale[-1]<=dev_by_scale[0]
print("F2f",'PASS' if ok else 'FAIL')
