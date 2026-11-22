# The web form in three dimensions: a flat web whose three lines' lengths all vary (a ball's own lines, far from its centre):
# a = (1, rr/R, rr sin(th)/R), rr = R + x, th = pi/2 + y/R, ph = z/R; true positions (rr sin th cos ph, rr sin th sin ph, rr cos th).
# Step: H = sum_i {1/a_i, alpha_i sin k_i + r beta (1 - cos k_i)}/2, massless, four components, r = 1/2. A packet's centre is followed in the true positions.
# Stated before running: true path straight to 0.3 hop; speed within 1% of the even grid's for the same launch; heading in the web's labels turning by more than 3 degrees.
import numpy as np, sys
L=64; R=96.0; r=0.5; sig=6.0; dt=0.5; order=10; T=40; kmag=0.6
g=np.arange(L)-L/2; x,y,z=np.meshgrid(g,g,g,indexing='ij'); kk=2*np.pi*np.fft.fftfreq(L); KS=np.meshgrid(kk,kk,kk,indexing='ij')
S=[np.sin(K) for K in KS]; C=[r*(1-np.cos(K)) for K in KS]
sg=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
def alpha(i,p):
    u,d=p[:2],p[2:]; s=sg[i]; su=np.array([s[0,0]*u[0]+s[0,1]*u[1],s[1,0]*u[0]+s[1,1]*u[1]]); sd=np.array([s[0,0]*d[0]+s[0,1]*d[1],s[1,0]*d[0]+s[1,1]*d[1]])
    return np.concatenate([sd,su])
beta=lambda p: np.concatenate([p[:2],-p[2:]])
def h0(i,p):
    f=np.fft.fftn(p,axes=(1,2,3)); return alpha(i,np.fft.ifftn(S[i]*f,axes=(1,2,3)))+beta(np.fft.ifftn(C[i]*f,axes=(1,2,3)))
def run(a,pos,x0,dirn):
    w=[1/ai for ai in a]; H=lambda q: sum(0.5*(w[i]*h0(i,q)+h0(i,w[i]*q)) for i in range(3))
    idx=tuple(int(c+L/2) for c in x0); a0=[ai[idx] for ai in a]; q=[kmag*dirn[i]*a0[i] for i in range(3)]
    A=[np.kron(np.array([[0,1],[1,0]]),s) for s in sg]; B=np.diag([1,1,-1,-1]).astype(complex)
    hm=sum((np.sin(q[i])*A[i]+r*(1-np.cos(q[i]))*B)/a0[i] for i in range(3)); u=np.linalg.eigh(hm)[1][:,3]
    env=np.exp(-sum(((c-x0[i])*a0[i])**2 for i,c in enumerate((x,y,z)))/(4*sig**2)+1j*(q[0]*x+q[1]*y+q[2]*z))
    p=np.array([u[j]*env for j in range(4)]); p/=np.sqrt((abs(p)**2).sum()); tr=[]
    for n in range(int(T/dt)+1):
        if n%8==0:
            d=(abs(p)**2).sum(0); d/=d.sum(); tr.append([n*dt]+[(d*c).sum() for c in (x,y,z)]+[(d*c).sum() for c in pos])
        term=p.copy(); acc=p.copy()
        for j in range(1,order+1): term=(-1j*dt/j)*H(term); acc=acc+term
        p=acc
    tr=np.array(tr); t=tr[:,0]; lab=tr[:,1:4]; tru=tr[:,4:7]
    fit=np.array([np.polyfit(t,tru[:,i],1) for i in range(3)]); v=fit[:,0]; sp=np.linalg.norm(v); resid=tru-(np.outer(t,v)+fit[:,1]); along=resid@v/sp
    side=np.linalg.norm(resid-np.outer(along,v/sp),axis=1).max()
    vl=np.gradient(lab,t,axis=0); c=(vl[1]@vl[-2])/np.linalg.norm(vl[1])/np.linalg.norm(vl[-2]); turn=np.degrees(np.arccos(min(c,1)))
    return sp,side,abs(along).max(),turn
one=np.ones((L,L,L)); rr=R+x; th=np.pi/2+y/R; ph=z/R
x0=(-10.0,-8.0,-8.0); dirn=np.array([0.7,0.55,0.45]); dirn/=np.linalg.norm(dirn)
for nm,a,pos in (("even grid",[one,one,one],(x,y,z)),("a ball's own lines",[one,rr/R,rr*np.sin(th)/R],(rr*np.sin(th)*np.cos(ph),rr*np.sin(th)*np.sin(ph),rr*np.cos(th)))):
    sp,side,along,turn=run(a,pos,x0,dirn)
    print(f"{nm}: true path speed {sp:.4f}; sideways departure from a straight line at most {side:.3f} hop, along it {along:.3f}, over {sp*T:.0f} hops; heading in the web's labels turns by {turn:.2f} degrees",flush=True)
