# Which combinations of coloured patterns leave no string? In one dimension Gauss's law makes each link's field energy (g^2/2) C2(R),
# with R the colour state of everything to one side of it and C2 the quadratic Casimir. Here C2 is computed directly from the eight colour
# generators acting on one, two and three quarks (and a quark with an antiquark): no group tables assumed.
# Also: how large an exact run of the three-colour model on the step would be, by chain length.
import numpy as np, itertools, math
l=np.zeros((8,3,3),complex)
l[0][0,1]=l[0][1,0]=1; l[1][0,1]=-1j; l[1][1,0]=1j; l[2][0,0]=1; l[2][1,1]=-1; l[3][0,2]=l[3][2,0]=1; l[4][0,2]=-1j; l[4][2,0]=1j
l[5][1,2]=l[5][2,1]=1; l[6][1,2]=-1j; l[6][2,1]=1j; l[7]=np.diag([1,1,-2])/np.sqrt(3)
T=l/2; Tb=-T.conj()                                    # quark and antiquark generators
def casimir(gens):
    n=len(gens); d=3**n; C=np.zeros((d,d),complex)
    for a in range(8):
        Q=np.zeros((d,d),complex)
        for i in range(n):
            ops=[np.eye(3)]*n; ops[i]=gens[i][a]; M=ops[0]
            for o in ops[1:]: M=np.kron(M,o)
            Q+=M
        C+=Q@Q
    w=np.linalg.eigvalsh(C); vals=sorted(set(np.round(w,6))); return [(v,int(np.sum(np.isclose(w,v)))) for v in vals]
for nm,gens in (("one quark",[T]),("two quarks",[T,T]),("a quark and an antiquark",[T,Tb]),("three quarks",[T,T,T]),("two quarks and an antiquark",[T,T,Tb])):
    print(f"{nm}: string energy per link, in units of g^2/2 (number of states): "+", ".join(f"{v:.4g} ({k})" for v,k in casimir(gens)))
print("exact run of the three-colour model on the step (two modes per colour per place, each colour's count kept): states in the vacuum sector")
for N in range(2,8): print(f"   {N} places: {math.comb(2*N,N)**3:.3g} (two colours: {math.comb(2*N,N)**2:.3g}; one, as in C16: {math.comb(2*N,N)})")
