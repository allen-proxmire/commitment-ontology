exec(open('dt.py').read().split("for th in")[0])
P=[I,X,Y,Z]; nm="IXYZ"
def pauli(o):
    t=[]
    for a,b,c in itertools.product(range(4),repeat=3):
        co=np.trace(k3(P[a],P[b],P[c]).conj().T@o)/8
        if abs(co)>1e-6: t.append(f"{co.real:+.3f}{co.imag:+.3f}j {nm[a]}{nm[b]}{nm[c]}")
    return t
rng=np.random.default_rng(7); qs=[rng.normal(size=3) for _ in range(6)]
def nullsp(M):
    u,s,vh=np.linalg.svd(M); return vh[np.r_[s,np.zeros(vh.shape[0]-len(s))]<1e-8*s[0]].conj()
for thm in [0.0,0.2]:
    Us={tuple(q):U(q,0.4,thm) for q in qs}; Um={tuple(q):U(-q,0.4,thm) for q in qs}
    L=nullsp(np.vstack([np.kron(Us[tuple(q)].T,np.eye(8))-np.kron(np.eye(8),Us[tuple(q)]) for q in qs]))
    A=nullsp(np.vstack([np.kron(Us[tuple(q)].conj().T,np.eye(8))-np.kron(np.eye(8),Um[tuple(q)]) for q in qs]))
    print(f"mass {thm}: linear dim {len(L)}, antilinear dim {len(A)}")
    for n in L:
        o=n.reshape(8,8,order='F'); o=o-np.trace(o)/8*np.eye(8)
        if np.linalg.norm(o)>1e-6: o/=np.abs(o).max(); print("  linear:",pauli(o)); print("   eig:",np.round(np.linalg.eigvals(o),3))
    for n in A:
        o=n.reshape(8,8,order='F'); o/=np.abs(o).max(); print("  antilinear B:",pauli(o))
# --- chirality and one-handed kind flips
G=1j*ax@ay@az
print("G anticommutes beta, commutes alphas:",np.allclose(G@be,-be@G),all(np.allclose(G@a,a@G) for a in alph), "commutes taus:",all(np.allclose(G@t,t@G) for t in tau))
u=np.array([0.3,0.5,0.8]);u/=np.linalg.norm(u)
for s in [0.2,0.1,0.05]:
    q=u*s;Uq=U(q,0.4,0.0);Dq=D(q)
    Gs=Dq.conj().T@G@Dq; PL=[(np.eye(8)-Gs)/2@(Dq.conj().T@t@Dq) for t in tau]
    print(f"|q|={s}: [G,U]={np.linalg.norm(Gs@Uq-Uq@Gs):.2e}  [P_L tau,U]={max(np.linalg.norm(o@Uq-Uq@o) for o in PL):.2e}")
# exact projected chirality: does the massless walk keep an exact chiral label in each matched set?
def proj(op,Uq):
    w,V=np.linalg.eig(Uq); Q=np.zeros((8,8),complex); used=np.zeros(8,bool)
    for i in range(8):
        if used[i]: continue
        blk=np.where(np.abs(np.angle(w*np.conj(w[i])))<1e-8)[0]; used[blk]=True
        Vb,_=np.linalg.qr(V[:,blk]); Pb=Vb@Vb.conj().T; Q+=Pb@op@Pb
    return Q
q=u*0.3;Uq=U(q,0.4,0);Dq=D(q);Gs=Dq.conj().T@G@Dq
Ge=proj(Gs,Uq); print("projected G eig:",np.round(np.linalg.eigvalsh((Ge+Ge.conj().T)/2),4))
T=[proj(Dq.conj().T@t@Dq,Uq) for t in tau]
print("projected taus commute with projected G:",[round(np.linalg.norm(Ge@t-t@Ge),4) for t in T])
