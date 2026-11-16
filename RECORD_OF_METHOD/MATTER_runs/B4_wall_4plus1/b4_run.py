import numpy as np
s0=np.eye(2); sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.,-1]).astype(complex)
A=[np.kron(sx,s) for s in (sx,sy,sz)]; B=np.kron(sz,s0)
G5=1j*A[0]@A[1]@A[2]; A4=1j*G5@B
for X in A+[B,A4]:
    for Y in A+[B,A4]:
        if X is not Y: assert np.allclose(X@Y+Y@X,0)
assert np.allclose(G5@G5,np.eye(4)) and all(np.allclose(G5@a,a@G5) for a in A) and np.allclose(G5@B,-B@G5)
r=0.5; M=0.5
def H(k,L):
    n=2*L; ms=np.where(np.arange(n)<L,M,-M); Hm=np.zeros((4*n,4*n),complex)
    kin=sum(np.sin(k[j])*A[j] for j in range(3)); wil=r*sum(1-np.cos(k[j]) for j in range(3))
    for s in range(n):
        Hm[4*s:4*s+4,4*s:4*s+4]=kin+(ms[s]+wil+r)*B          # on-site: mass wall + Wilson (3 space dirs + inner diagonal part r)
        t=(s+1)%n                                              # inner hop: alpha4 sin k_s - (r/2) beta (S + S^dag)
        hop=A4/(2j)-(r/2)*B
        Hm[4*t:4*t+4,4*s:4*s+4]+=hop; Hm[4*s:4*s+4,4*t:4*t+4]+=hop.conj().T
    return Hm
def light(k,L):
    e,v=np.linalg.eigh(H(k,L)); idx=np.argsort(np.abs(e))[:4]; out=[]
    for i in idx:
        u=v[:,i].reshape(2*L,4); w=(np.abs(u)**2).sum(1); g=np.real(np.sum(np.conj(u)*(u@G5.T)))
        wallA=np.sum(w[:L]); out.append((e[i],g,wallA))   # weight in the +M half (its edges are the two walls... see below)
    return e,out
ok=True; L=16
for name,nh in (("axis",np.array([1.,0,0])),("body diagonal",np.ones(3)/np.sqrt(3))):
    k=0.05*nh; e,out=light(k,L); ae=np.sort(np.abs(e))
    four=ae[3]<0.2 and ae[4]>0.2; ok&=four
    print(f"B4a {name}: lowest |E| = {np.round(ae[:6],5)} -> {'four light states' if four else 'NOT four'}")
    for E_,g,wa in out:
        # which wall: the walls sit at inner places L-1/L and 2L-1/0; locate by the state's mean inner position on the ring
        print(f"   E = {E_:+.5f}  <g5> = {g:+.5f}  speed |E|/|k| = {abs(E_)/0.05:.5f}")
    gs=[g for _,g,_ in out]; ok&=all(abs(g)>=0.99 for g in gs) and sum(1 for g in gs if g>0)==2
    ok&=all(abs(abs(E_)/0.05-1)<=0.01 for E_,_,_ in out)
# which wall carries which handedness
e,v=np.linalg.eigh(H(0.05*np.array([1.,0,0]),L)); idx=np.argsort(np.abs(e))[:4]
for i in idx:
    u=v[:,i].reshape(2*L,4); w=(np.abs(u)**2).sum(1); g=np.real(np.sum(np.conj(u)*(u@G5.T)))
    near_mid=np.sum(w[L-4:L+4]); near_edge=np.sum(w[:4])+np.sum(w[-4:])
    print(f"B4b: E = {e[i]:+.5f}, <g5> = {g:+.4f}: weight near the wall between places L-1|L {near_mid:.3f}, near the wall at 2L-1|0 {near_edge:.3f}")
# leftover mass at k = 0
Ls=np.arange(4,15); m=[]
for LL in Ls:
    e,_=light(np.zeros(3),LL); m.append(np.sort(np.abs(e))[0])
kap=-np.polyfit(Ls[3:],np.log(m[3:]),1)[0]; ok&=abs(kap/0.41-1)<=0.05
print("B4d: leftover |E| at k=0:",", ".join(f"L={a}: {b:.2e}" for a,b in zip(Ls,m)),f"; kappa = {kap:.4f} per place")
print("B4",'PASS' if ok else 'FAIL')
