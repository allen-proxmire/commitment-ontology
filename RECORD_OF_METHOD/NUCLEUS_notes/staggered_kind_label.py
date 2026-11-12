exec(open('dt.py').read().split("for th in")[0])
th,thm=0.4,0.2
t3=tau[2]
def Qexact(q):
    Uq=U(q,th,thm); w,V=np.linalg.eig(Uq)
    # group eigenvalues into degenerate blocks
    ang=np.angle(w); Q=np.zeros((8,8),complex); used=np.zeros(8,bool)
    T=D(q).conj().T@t3@D(q)   # site-phase local label
    for i in range(8):
        if used[i]: continue
        blk=np.where(np.abs(np.angle(w*np.conj(w[i])))<1e-8)[0]; used[blk]=True
        Vb,_=np.linalg.qr(V[:,blk]); P=Vb@Vb.conj().T
        Q+=P@T@P
    return Q,T,Uq
# 1) Q commutes, eigenvalues, distance from local label
for s in [0.4,0.2,0.1,0.05]:
    q=np.array([0.3,0.5,0.8])*s/np.linalg.norm([0.3,0.5,0.8])
    Q,T,Uq=Qexact(q)
    print(f"|q|={s}: [Q,U]={np.linalg.norm(Q@Uq-Uq@Q):.1e}  eig(Q)={np.round(np.linalg.eigvalsh((Q+Q.conj().T)/2),5)[[0,-1]]}  ||Q-T||={np.linalg.norm(Q-T):.2e}")
# 2) real-space range of exact label (cell-phase form, which is what's periodic in q)
import sys; N=int(sys.argv[1]); g=2*np.pi*np.arange(N)/N
C={}
Qs=np.zeros((N,N,N,8,8),complex)
for a,b,c in itertools.product(range(N),repeat=3):
    q=np.array([g[a],g[b],g[c]]); Q,_,_=Qexact(q)
    Qs[a,b,c]=D(q)@Q@D(q).conj().T   # back to cell-phase convention
F=np.fft.ifftn(Qs,axes=(0,1,2))
mx={}
for a,b,c in itertools.product(range(N),repeat=3):
    d=max(min(a,N-a),min(b,N-b),min(c,N-c)); mx[d]=max(mx.get(d,0),np.abs(F[a,b,c]).max())
print("exact-label coupling vs cell distance:",{k:f"{v:.1e}" for k,v in sorted(mx.items())})
