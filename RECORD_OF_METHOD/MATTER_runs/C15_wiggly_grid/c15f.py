# Can a hand-drawn grid be made invisible to long-wavelength patterns by its hop weights alone?
# Places x_i = grid + random displacement. Seek link vectors A_ij = -A_ji and cell sizes V_i with
#   (1) sum_j A_ij = 0                       (a constant pattern has no gradient)
#   (2) sum_j A_ij (x_j - x_i)/2 = V_i * 1   (a pattern linear in the true positions has its true gradient)
# Then H = -i sigma . A_ij /(2 sqrt(V_i V_j)) is Hermitian and exact to first order. Count per place in 2D: 6 conditions;
# unknowns 2 per link + 1: 5 with the grid's four neighbours, 9 with the diagonals added.
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl
def solve(L,delta,offs,seed=5,near_even=False):
    rng=np.random.default_rng(seed); d=delta*rng.standard_normal((L,L,2))
    site=lambda x,y:(x%L)*L+(y%L)
    links=[]; 
    for x in range(L):
        for y in range(L):
            for o in offs: links.append((site(x,y),site(x+o[0],y+o[1]),np.array(o,float)+d[(x+o[0])%L,(y+o[1])%L]-d[x,y]))
    nl=len(links); nu=2*nl+L*L; rows=[];cols=[];vals=[];b=[]; r=0
    eq=lambda i,c: 6*i+c
    for l,(i,j,dx) in enumerate(links):
        for a in range(2):
            rows+= [eq(i,a),eq(j,a)]; cols+=[2*l+a]*2; vals+=[1.0,-1.0]                    # closure at i (+A) and j (-A)
            for bb in range(2):
                rows+=[eq(i,2+2*a+bb),eq(j,2+2*a+bb)]; cols+=[2*l+a]*2; vals+=[dx[bb]/2, dx[bb]/2]   # A_ij dx/2 at i ; (-A)(-dx)/2 at j
    for i in range(L*L):
        for a in range(2): rows.append(eq(i,2+3*a)); cols.append(2*nl+i); vals.append(-1.0)
    M=sp.csr_matrix((vals,(rows,cols)),shape=(6*L*L,nu))
    # particular: V = 1 everywhere fixed by moving V to the right side is not general; instead add the normalisation mean V = 1
    N=sp.csr_matrix((np.ones(L*L)/L,(np.zeros(L*L,int),2*nl+np.arange(L*L))),shape=(1,nu))
    Mx=sp.vstack([M,N]).tocsr(); rhs=np.zeros(6*L*L+1); rhs[-1]=L
    x0=np.zeros(nu)
    if near_even:    # among the exact weights, take those nearest the even grid's own (axis links 1, diagonals 0, cells 1)
        for l,(i,j,dx) in enumerate(links):
            o=offs[l%len(offs)]
            if o in ((1,0),(0,1)): x0[2*l:2*l+2]=o
        x0[2*nl:]=1.0
    sol=x0+spl.lsqr(Mx,rhs-Mx@x0,atol=1e-13,btol=1e-13,iter_lim=200000)[0]
    res=np.linalg.norm(M@sol)/np.sqrt(L*L); return res,sol,links,nl
if __name__=="__main__":
    four=[(1,0),(0,1)]; eight=four+[(1,1),(1,-1)]
    for delta in (0.05,0.15):
        for nm,offs in (("four neighbours",four),("eight neighbours",eight)):
            res,sol,links,nl=solve(24,delta,offs); V=sol[2*nl:]
            print(f"displacement {delta}: {nm}: leftover per place {res:.2e}; cell sizes {V.min():.3f} to {V.max():.3f}")
