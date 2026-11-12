import sys,os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'staggered_walk_base.py')).read().split("for th in")[0])
th=0.4
def label(q,thm,seed):
    Uq=U(q,th,thm); w,V=np.linalg.eig(Uq); Q=np.zeros((8,8),complex); used=np.zeros(8,bool)
    for i in range(8):
        if used[i]: continue
        blk=np.where(np.abs(np.angle(w*np.conj(w[i])))<1e-7)[0]; used[blk]=True
        Vb,_=np.linalg.qr(V[:,blk]); P=Vb@Vb.conj().T; Q+=P@seed(q)@P
    Q=(Q+Q.conj().T)/2; e,W=np.linalg.eigh(Q)
    return W@np.diag(np.sign(e))@W.conj().T, np.min(np.abs(e)), np.linalg.norm(Q@Uq-Uq@Q)
cellseed=lambda q: tau[2]
siteseed=lambda q: D(q).conj().T@tau[2]@D(q)
def reach(thm,seed,N):
    g=2*np.pi*np.arange(N)/N; Qs=np.zeros((N,N,N,8,8),complex); mn=9
    for a,b,c in itertools.product(range(N),repeat=3):
        Qq,m,_=label(np.array([g[a],g[b],g[c]]),thm,seed); Qs[a,b,c]=Qq; mn=min(mn,m)
    F=np.fft.ifftn(Qs,axes=(0,1,2)); mx={}
    for a,b,c in itertools.product(range(N),repeat=3):
        d=max(min(a,N-a),min(b,N-b),min(c,N-c)); mx[d]=max(mx.get(d,0),np.abs(F[a,b,c]).max())
    return mn,[f"{mx[d]:.1e}" for d in sorted(mx)]
for name,seed in [("cell seed",cellseed),("site seed",siteseed)]:
    for thm in [0.2,0.05]:
        for N in [12,20]:
            mn,r=reach(thm,seed,N); print(f"{name} thm={thm} N={N} min|eig PτP|={mn:.3f}: {r}")
# --- the twist: going once around the zone along axis j conjugates the site-phase label by Z on bit j
for a,t in enumerate(tau):
    print('tau',a+1,['flips' if np.allclose(Zj@t@Zj,-t) else 'kept' for Zj in [k3(Z,I,I),k3(I,Z,I),k3(I,I,Z)]])
best=[]
for q in itertools.product(np.linspace(-np.pi,np.pi,17),repeat=3):
    q=np.array(q); w,V=np.linalg.eig(U(q,0.4,0.2)); Vb,_=np.linalg.qr(V[:,np.angle(w)>0]); Pp=Vb@Vb.conj().T
    best.append((np.sort(np.abs(np.linalg.eigvalsh(Pp@tau[2]@Pp)))[-4:].min(),tuple(np.round(q,2))))
best.sort(); print('strictly local label weakest at:',best[:2])
