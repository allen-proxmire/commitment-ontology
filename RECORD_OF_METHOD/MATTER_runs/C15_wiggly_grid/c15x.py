# Hop-to-hop unevenness in three dimensions. A flat web: each line's links relabelled alone, lengths uneven by 0.1 from link to link.
#  links:        a place's size along a line V = mean of its two links; hops 1/sqrt(V V'); lifting term with each link's own length (c15r's form).
#  independent:  the same form with sizes drawn independently per place (not from links).
# Massless, four components, r = 1/2, L = 64, k = 0.6, T = 26 (before the packet nears the box edge). Measure: the share of the dressed packet still
# within 0.30 of its launch wavenumber (a first pass at 0.15 kept only 73% of the launch packet and its changes were noise: c15x_firstpass_out.txt). Stated before running: with sizes from the links the share falls at most a third as far as with independent sizes.
import numpy as np
L=64; r=0.5; sig=6.0; dt=0.5; order=10; T=26; kmag=0.6; eps=0.1
g=np.arange(L); kk=2*np.pi*np.fft.fftfreq(L); KS=np.meshgrid(kk,kk,kk,indexing='ij')
sg=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def alpha(i,p):
    u,d=p[:2],p[2:]; s=sg[i]; su=np.array([s[0,0]*u[0]+s[0,1]*u[1],s[1,0]*u[0]+s[1,1]*u[1]]); sd=np.array([s[0,0]*d[0]+s[0,1]*d[1],s[1,0]*d[0]+s[1,1]*d[1]])
    return np.concatenate([sd,su])
beta=lambda p: np.concatenate([p[:2],-p[2:]])
sh=lambda v,i: v.reshape([L if j==i else 1 for j in range(3)])
def run(V,Xpos):
    t=[1/np.sqrt(V[i]*np.roll(V[i],-1)) for i in range(3)]
    def H(q):
        out=0
        for i in range(3):
            tp=sh(t[i],i); tm=sh(np.roll(t[i],1),i); qp=np.roll(q,-1,i+1); qm=np.roll(q,1,i+1)
            out=out-0.5j*alpha(i,tp*qp-tm*qm)-(r/2)*beta(tp*qp+tm*qm-sh(2/V[i],i)*q)
        return out
    dirn=np.array([0.7,0.55,0.45]); dirn/=np.linalg.norm(dirn); k0=np.array([2*np.pi*round(kmag*d*L/(2*np.pi))/L for d in dirn])
    A=[np.kron(np.array([[0,1],[1,0]]),s) for s in sg]; B=np.diag([1,1,-1,-1]).astype(complex)
    u=np.linalg.eigh(sum(np.sin(k0[i])*A[i]+r*(1-np.cos(k0[i]))*B for i in range(3)))[1][:,3]
    x0=np.array([22.0,24.0,24.0]); sv=1.0; ph=1.0; env=1.0
    for i in range(3):
        sv=sv*sh(np.sqrt(V[i]),i); ph=ph*sh(np.exp(1j*k0[i]*(Xpos[i]-g)),i); env=env*sh(np.exp(-(g-x0[i])**2/(4*sig**2)+1j*k0[i]*g),i)
    p=np.array([u[j]*sv*ph*env for j in range(4)]); p/=np.sqrt((abs(p)**2).sum())
    win=np.sqrt(sum((KS[i]-k0[i])**2 for i in range(3)))<0.30
    def fwd(p):
        P=(abs(np.fft.fftn(p/sv/ph,axes=(1,2,3)))**2).sum(0); return P[win].sum()/P.sum()
    out=[fwd(p)]
    for n in range(int(T/dt)):
        term=p.copy(); acc=p.copy()
        for j in range(1,order+1): term=(-1j*dt/j)*H(term); acc=acc+term
        p=acc
        if (n+1)%26==0: out.append(fwd(p))
    return out
rng=np.random.default_rng(4)
def from_links():
    V=[];X=[]
    for i in range(3):
        a=1+eps*rng.standard_normal(L); a*=L/a.sum(); V.append((a+np.roll(a,1))/2); X.append(np.concatenate(([0],np.cumsum(a)[:-1])))
    return V,X
def independent():
    V=[];X=[]
    for i in range(3):
        v=1+eps*rng.standard_normal(L); v*=L/v.sum(); V.append(v); X.append(np.concatenate(([0],np.cumsum(v)[:-1])))
    return V,X
res={}
for nm,(V,X) in (("even grid",([np.ones(L)]*3,[g.astype(float)]*3)),("sizes from the links",from_links()),("sizes independent per place",independent())):
    out=run(V,X); res[nm]=out[0]-out[-1]; print(f"{nm}: share kept "+" ".join(f"{o:.5f}" for o in out)+f"; fall {out[0]-out[-1]:.2e}",flush=True)
print(f"independent over from-the-links: {res['sizes independent per place']/res['sizes from the links']:.1f}")
