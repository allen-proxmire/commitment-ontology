# A seam between two differently turned grids (2D, massless, r = 1/2). Left of the seam: the square grid, spacing 1.
# Right: a grid turned by 45 degrees, spacing sqrt(2), on every other place. Across the seam every other row links on; the links there have strength g.
# No rule fixes g. Question: is there a g at which a long-wavelength packet crosses cleanly, and how does the loss grow as the wavelength shortens?
# Not registered. Expected: yes, for some g of order one, with the loss falling as the wavelength grows.
import numpy as np, scipy.sparse as sp
NX,NY=400,128; r=0.5; sig=18.0
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex); I2=np.eye(2)
idx=lambda x,y: ((x+NX//2)%NX)*NY+(y%NY)
def build(g):
    rows=[];cols=[];vals=[]
    def add(i,j,m):
        for a in range(2):
            for b in range(2):
                if m[a,b]!=0: rows.append(2*i+a);cols.append(2*j+b);vals.append(m[a,b])
    def bond(i,j,d,s=1.0):
        a=np.hypot(*d); n=np.array(d)/a; sn=n[0]*sx+n[1]*sy
        add(i,j,s/a*(-0.5j*sn-0.5*r*sz)); add(j,i,s/a*(0.5j*sn-0.5*r*sz)); add(i,i,s/a*0.5*r*sz); add(j,j,s/a*0.5*r*sz)
    for x in range(-NX//2,NX//2):
        for y in range(NY):
            if x<0:
                bond(idx(x,y),idx(x,y+1),(0,1))
                if x<-1: bond(idx(x,y),idx(x+1,y),(1,0))
                elif y%2==0: bond(idx(x,y),idx(0,y),(1,0),g)       # seam link
            elif (x+y)%2==0 and x<NX//2-1:
                bond(idx(x,y),idx(x+1,y+1),(1,1)); bond(idx(x,y),idx(x+1,y-1),(1,-1))
    return sp.csr_matrix((vals,(rows,cols)),shape=(2*NX*NY,2*NX*NY))
def run(g,k0,ang=0.0,H=None):
    H=build(g) if H is None else H
    kx,ky=k0*np.cos(ang),k0*np.sin(ang); ky=2*np.pi*round(ky*NY/(2*np.pi))/NY
    X,Y=np.meshgrid(np.arange(-NX//2,NX//2),np.arange(NY),indexing='ij'); x0=-90
    dy=(Y-NY/2+NY/2)%NY-NY/2
    env=np.exp(-((X-x0)**2)/(4*sig**2)+1j*(kx*X+ky*Y))*(X<0)       # plane wave across y (periodic), packet along x
    h=np.sin(kx)*sx+np.sin(ky)*sy+r*(2-np.cos(kx)-np.cos(ky))*sz; w,v=np.linalg.eigh(h); u=v[:,1]
    p=np.zeros((NX,NY,2),complex); p[...,0]=u[0]*env; p[...,1]=u[1]*env; p=p.reshape(-1); p/=np.linalg.norm(p)
    T=180/np.cos(ang); dt=0.4
    for n in range(int(T/dt)):
        term=p.copy(); out=p.copy()
        for j in range(1,11): term=(-1j*dt/j)*(H@term); out=out+term
        p=out
    d=(abs(p.reshape(NX,NY,2))**2).sum((1,2)); xs=np.arange(-NX//2,NX//2)
    return d[xs>=4].sum(), d[xs<-4].sum(), d[(xs>=-4)&(xs<4)].sum()
print("share crossing / turned back / left at the seam, head-on, by link strength g and wavenumber k:")
best={}
for g in (0.7,1.0,1.2,1.41,1.7,2.0):
    H=build(g); line=[]
    for k in (0.2,0.4,0.8):
        t,rf,s=run(g,k,0.0,H); line.append(f"k={k}: {t:.4f}/{rf:.4f}/{s:.4f}"); best[(g,k)]=t
    print(f"  g = {g}: "+"   ".join(line))
gb=max((0.7,1.0,1.2,1.41,1.7,2.0),key=lambda g: best[(g,0.2)])
print(f"best g at the longest wavelength: {gb}")
H=build(gb)
for k in (0.1,0.2,0.4,0.8):
    for ang in (0.0,np.pi/6):
        t,rf,s=run(gb,k,ang,H); print(f"  g = {gb}, k = {k}, angle {np.degrees(ang):.0f} deg: crossing {t:.4f}, turned back {rf:.4f}, at the seam {s:.4f}")
