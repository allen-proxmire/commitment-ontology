# Shared tools for c15i, c15j: weights on a displaced grid (the conditions of c15f), the Hamiltonian, a packet run. 2D, massless, r = 0.
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl
FOUR=[(1,0),(0,1)]; EIGHT=FOUR+[(1,1),(1,-1)]
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]])
def make_d(L,delta,xi=0,seed=5):
    rng=np.random.default_rng(seed); d=rng.standard_normal((L,L,2))
    if xi>0:
        k=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(k,k,indexing='ij'); f=np.exp(-(KX**2+KY**2)*xi**2/2)
        d=np.stack([np.fft.ifft2(np.fft.fft2(d[...,a])*f).real for a in range(2)],-1)
    return d*delta/d.std()
def weights(L,d,offs,near=True):
    site=lambda x,y:(x%L)*L+(y%L); links=[]
    for x in range(L):
        for y in range(L):
            for o in offs: links.append((site(x,y),site(x+o[0],y+o[1]),np.array(o,float)+d[(x+o[0])%L,(y+o[1])%L]-d[x,y],o))
    nl=len(links); nu=2*nl+L*L; I=np.array([l[0] for l in links]); J=np.array([l[1] for l in links]); DX=np.array([l[2] for l in links]); ar=np.arange(nl)
    rows=[];cols=[];vals=[]
    for a in range(2):
        rows+=[6*I+a,6*J+a]; cols+=[2*ar+a]*2; vals+=[np.ones(nl),-np.ones(nl)]
        for b in range(2): rows+=[6*I+2+2*a+b,6*J+2+2*a+b]; cols+=[2*ar+a]*2; vals+=[DX[:,b]/2,DX[:,b]/2]
        rows.append(6*np.arange(L*L)+2+3*a); cols.append(2*nl+np.arange(L*L)); vals.append(-np.ones(L*L))
    M=sp.csr_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(6*L*L,nu))
    x0=np.zeros(nu); x0[2*nl:]=1.0
    for l,(i,j,dx,o) in enumerate(links):
        if o in ((1,0),(0,1)): x0[2*l:2*l+2]=o
    N=sp.csr_matrix((np.ones(L*L)/L,(np.zeros(L*L,int),2*nl+np.arange(L*L))),shape=(1,nu))     # mean cell size 1
    Mx=sp.vstack([M,N]).tocsr(); rhs=np.zeros(6*L*L+1); rhs[-1]=L
    if not near: x0=np.zeros(nu)
    sol=x0+spl.lsqr(Mx,rhs-Mx@x0,atol=1e-12,btol=1e-12,iter_lim=100000)[0]
    res=np.linalg.norm(M@sol)/L; A=sol[:2*nl].reshape(nl,2); V=sol[2*nl:]
    rows=[];cols=[];vals=[]; s=np.sqrt(V[I]*V[J])
    for a in range(2):
        for b in range(2):
            m=-0.5j*(A[:,0]*sx[a,b]+A[:,1]*sy[a,b])/s
            rows+=[2*I+a,2*J+a]; cols+=[2*J+b,2*I+b]; vals+=[m,-m]
    H=sp.csr_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(2*L*L,2*L*L))
    return H,V.reshape(L,L),res
def plane(L,V,d,k0):
    X,Y=np.meshgrid(np.arange(L),np.arange(L),indexing='ij'); chi=np.sqrt(V)*np.exp(1j*k0*(X+d[...,0]))
    p=np.stack([chi,chi],-1).reshape(-1)/np.sqrt(2); return p/np.linalg.norm(p)
def residual(H,L,V,d,k):
    k0=2*np.pi*round(k*L/(2*np.pi))/L; p=plane(L,V,d,k0); Hp=H@p; E=np.vdot(p,Hp).real; return k0,np.linalg.norm(Hp-E*p)
def loss_rate(H,L,V,d,k,sig,times,win=0.12,dt=0.4):
    k0=2*np.pi*round(k*L/(2*np.pi))/L; xi=np.arange(L)-L/4; X,Y=np.meshgrid(xi,np.arange(L)-L/2,indexing='ij')
    env=np.sqrt(V)*np.exp(-(X**2+Y**2)/(4*sig**2)+1j*k0*(X+d[...,0])); p=np.stack([env,env],-1).reshape(-1)/np.sqrt(2); p=p/np.linalg.norm(p)
    kk=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(kk,kk,indexing='ij'); w=np.hypot(KX-k0,KY)<win
    def fwd(p):
        q=p.reshape(L,L,2)/np.sqrt(V)[...,None]*np.exp(-1j*k0*d[...,0])[...,None]; P=(abs(np.fft.fft2(q,axes=(0,1)))**2).sum(-1); return P[w].sum()/P.sum()
    out=[fwd(p)]; n=0
    for T in times:
        while n<int(T/dt):
            term=p.copy(); acc=p.copy()
            for j in range(1,11): term=(-1j*dt/j)*(H@term); acc=acc+term
            p=acc; n+=1
        out.append(fwd(p))
    return k0,-np.polyfit((0,)+tuple(times),out,1)[0],out
