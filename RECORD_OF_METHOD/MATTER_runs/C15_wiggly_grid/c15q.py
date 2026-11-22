# Webs flat in a less simple way: the lines' lengths depend on each other's position. 2D, massless, r = 1/2, the step H = sum_i {1/a_i, h_i}/2,
# h_i = sigma_i sin k_i + r (1 - cos k_i) sigma_z. A packet is launched; its centre is followed in the web's own labels (x, y) and in the true flat
# positions (X, Y) that the lengths describe.
#  fan:  a_x = 1, a_y = 1 + eps x/L   -> X + iY = (R + x) exp(i y / R), R = L/eps          (lengths vary by 25% either side across the web)
#  map:  a_x = a_y = |1 + eps z/L|    -> X + iY = z + eps z^2/(2L), z = x + iy
#  bowl: a_x = a_y = 1 + eps (x^2 + y^2)/L^2, curved (no flat positions exist); followed in its own labels only.
# Stated before running: on the two flat webs the true path is straight to 0.3 hop over the run and its speed within 0.5% of the even grid's,
# while in the web's labels the heading turns by more than 3 degrees.
import numpy as np
L=256; r=0.5; sig=12.0; dt=0.5; order=10; T=100; eps=0.5; kmag=0.5
g=np.arange(L)-L/2; x,y=np.meshgrid(g,g,indexing='ij'); z=x+1j*y
kk=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(kk,kk,indexing='ij')
def part(p,i):
    f=np.fft.fft2(p); K=(KX,KY)[i]; s=np.sin(K); m=r*(1-np.cos(K)); o=np.empty_like(f)
    if i==0: o[0]=m*f[0]+s*f[1]; o[1]=s*f[0]-m*f[1]
    else:    o[0]=m*f[0]-1j*s*f[1]; o[1]=1j*s*f[0]-m*f[1]
    return np.fft.ifft2(o)
def run(ax,ay,W,x0,y0,kx,ky):
    wx,wy=1/ax,1/ay; H=lambda q:0.5*(wx*part(q,0)+part(wx*q,0)+wy*part(q,1)+part(wy*q,1))
    ix,iy=int(x0+L/2),int(y0+L/2); qx,qy=kx*ax[ix,iy],ky*ay[ix,iy]          # label wavenumbers for true wavenumbers (kx, ky) along the local lines
    h=np.array([[r*(2-np.cos(qx)-np.cos(qy))*0+0, 0],[0,0]],complex)
    sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1.0,-1.0]).astype(complex)
    h=(np.sin(qx)*sx+r*(1-np.cos(qx))*sz)/ax[ix,iy]+(np.sin(qy)*sy+r*(1-np.cos(qy))*sz)/ay[ix,iy]; u=np.linalg.eigh(h)[1][:,1]
    env=np.exp(-(((x-x0)*ax[ix,iy])**2+((y-y0)*ay[ix,iy])**2)/(4*sig**2)+1j*(qx*x+qy*y)); p=np.array([u[0]*env,u[1]*env]); p/=np.sqrt((abs(p)**2).sum())
    path=[]
    for n in range(int(T/dt)+1):
        if n%20==0:
            d=(abs(p)**2).sum(0); d/=d.sum(); path.append((n*dt,(d*x).sum(),(d*y).sum(),(d*W).sum() if W is not None else 0j))
        term=p.copy(); acc=p.copy()
        for j in range(1,order+1): term=(-1j*dt/j)*H(term); acc=acc+term
        p=acc
    return np.array(path)
def report(nm,path,flat=True):
    t=path[:,0].real; gx,gy=path[:,1].real,path[:,2].real
    hd=np.degrees(np.arctan2(np.gradient(gy,t),np.gradient(gx,t))); turn=hd[-2]-hd[1]
    s=f"{nm}: heading in the web's labels turns by {turn:+.1f} degrees"
    if flat:
        Wc=path[:,3]; Xc,Yc=Wc.real,Wc.imag; cx=np.polyfit(t,Xc,1); cy=np.polyfit(t,Yc,1); v=np.hypot(cx[0],cy[0])
        n=np.array([-cy[0],cx[0]])/v; dev=(Xc-np.polyval(cx,t))*n[0]+(Yc-np.polyval(cy,t))*n[1]; along=((Xc-np.polyval(cx,t))*cx[0]+(Yc-np.polyval(cy,t))*cy[0])/v
        s+=f"; true path: speed {v:.5f}, sideways departure from a straight line at most {abs(dev).max():.3f} hop, along it {abs(along).max():.3f} hop, over {v*t[-1]:.0f} hops"
    print(s,flush=True); return s
one=np.ones((L,L)); th=np.radians(40)
p0=run(one,one,z,-60.0,-40.0,kmag*np.cos(th),kmag*np.sin(th)); report("even grid",p0)
R=L/eps; fan=(R+x)*np.exp(1j*y/R); p1=run(one,1+eps*x/L,fan,-60.0,-40.0,kmag*np.cos(th),kmag*np.sin(th)); report("fan",p1)
a=abs(1+eps*z/L); Wm=z+eps*z**2/(2*L)
# on the map the lines are turned by arg(1 + eps z/L) at the start: launch along the same true direction as the others
ang=th-np.angle(1+eps*(-60-40j)/L); p2=run(a,a,Wm,-60.0,-40.0,kmag*np.cos(ang),kmag*np.sin(ang)); report("smooth map",p2)
b=1+eps*(x**2+y**2)/L**2; p3=run(b,b,None,-60.0,-40.0,kmag*np.cos(th),kmag*np.sin(th)); report("bowl (curved)",p3,False)
