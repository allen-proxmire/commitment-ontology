# The hand-drawn grid: same neighbours, every place moved by a random displacement (rms delta hops per component). 2D, massless.
# Four ways to set the hops' strengths on it (naive hops, r = 0, except D):
#  F  felt wiggle for reference: even grid, strengths uneven by eps per place (c15a's case at r = 0).
#  A  each hop follows its own line's length and direction: H = {t_i/|t_i|^2 . sigma, sin k_i}/2, t_i the line's tangent.
#  B  each hop follows the cell: H = sqrt(V) [ E^i . sigma sin k_i ] / sqrt(V), E^i dual to the tangents (E^i . t_j = delta_ij), V the cell's area.
#     This is exact for patterns linear in the true positions and Hermitian (central differences commute).
#  D  B with the even grid's lifting term r(2 - cos k_x - cos k_y) sigma_z, r = 1/2, added unchanged.
# Loss rate = slope of the forward share against time, the even grid's own slope taken off.
# Stated before running: A goes as k^3 (power 3.0 +/- 0.6), like a felt wiggle; B goes as k^5 (5 +/- 1) and at k = 0.3 loses at least 5 times more slowly than A.
import numpy as np, sys
L=256; sig=24.0; dt=0.5; order=10; times=(50,100,150); delta=0.15; eps=0.15
kk=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(kk,kk,indexing='ij'); SK=(np.sin(KX),np.sin(KY)); W=2-np.cos(KX)-np.cos(KY)
sg=(np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]))
def dsin(p,i): return np.fft.ifft2(SK[i]*np.fft.fft2(p))
def sig_a(a,p): return np.array([sg[a][0,0]*p[0]+sg[a][0,1]*p[1], sg[a][1,0]*p[0]+sg[a][1,1]*p[1]])
def setup(var,seed=3):
    rng=np.random.default_rng(seed)
    if var=='0': return dict(var=var)
    if var=='F': return dict(var=var,w=1+eps*rng.standard_normal((L,L)))
    d=delta*rng.standard_normal((2,L,L))
    t=[np.array([ (np.roll(d[a],-1,i)-np.roll(d[a],1,i))/2 + (1.0 if a==i else 0.0) for a in range(2)]) for i in range(2)]   # t[i][a]
    V=t[0][0]*t[1][1]-t[0][1]*t[1][0]
    E=[np.array([t[1][1],-t[1][0]])/V, np.array([-t[0][1],t[0][0]])/V]      # E[i][a]
    C=[t[i]/(t[i]**2).sum(0) for i in range(2)]
    return dict(var=var,d=d,V=V,E=E,C=C,sV=np.sqrt(V))
def H(s,p):
    v=s['var']
    if v=='0': return sum(sig_a(i,dsin(p,i)) for i in range(2))
    if v=='F':
        h0=lambda q: sum(sig_a(i,dsin(q,i)) for i in range(2)); return 0.5*(s['w']*h0(p)+h0(s['w']*p))
    if v=='A':
        out=0
        for i in range(2):
            for a in range(2):
                c=s['C'][i][a]; out=out+0.5*(c*sig_a(a,dsin(p,i))+sig_a(a,dsin(c*p,i)))
        return out
    q=p/s['sV']; out=0
    for i in range(2):
        dq=dsin(q,i)
        for a in range(2): out=out+s['E'][i][a]*sig_a(a,dq)
    out=s['sV']*out
    if v=='D':
        wp=np.fft.ifft2(0.5*W*np.fft.fft2(p)); out=out+np.array([wp[0],-wp[1]])
    return out
def run(var,k0):
    s=setup(var); k0=2*np.pi*round(k0*L/(2*np.pi))/L
    xi=np.arange(L)-L/4; X,Y=np.meshgrid(xi,np.arange(L)-L/2,indexing='ij')
    if var in 'BD': Xp,Yp=X+s['d'][0],Y+s['d'][1]
    else: Xp,Yp=X,Y
    env=np.exp(-(X**2+Y**2)/(4*sig**2)+1j*k0*Xp)
    if var in 'BD': env=env*s['sV']
    p=np.array([env,env])/np.sqrt(2); p/=np.sqrt((abs(p)**2).sum())
    win=(np.hypot(KX-k0,KY)<0.12)
    def fwd(p):
        q=p
        if var in 'BD': q=p/s['sV']*np.exp(-1j*k0*s['d'][0])      # undress: back to the true positions' phase
        f=np.fft.fft2(q); P=(abs(f)**2).sum(0); return P[win].sum()/P.sum()
    out=[fwd(p)]; n=0
    for T in times:
        while n<int(T/dt):
            term=p.copy(); acc=p.copy()
            for j in range(1,order+1): term=(-1j*dt/j)*H(s,term); acc=acc+term
            p=acc; n+=1
        out.append(fwd(p))
    return k0,np.polyfit((0,)+times,out,1)[0],out
if __name__=="__main__":
    for var in sys.argv[1]:
        for k in (0.3,0.45,0.6,0.8):
            k0,sl,out=run(var,k); print(var,f"k={k0:.3f} slope={sl:.4e} forward="+" ".join(f"{o:.5f}" for o in out),flush=True)
