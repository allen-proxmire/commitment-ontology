# Shear between the lines. The web's data per square: the two link lengths a_x, a_y and one diagonal d, which fixes the angle between the lines,
# d^2 = a_x^2 + a_y^2 + 2 a_x a_y cos(theta). The step: H = sum_i { E^i . sigma, sin k_i }/2 + lifting term, E^x = (1, -cot theta)/a_x, E^y = (0, 1/sin theta)/a_y
# (the hop along a line now feeds both spin matrices). 2D, massless, r = 1/2 (lifting term {1/a_i, r(1 - cos k_i)}/2 sigma_z).
# Flat test web: X = x + eps y^2/(2 Lw), Y = y  (lines along y lean more and more: a_x = 1, a_y = sqrt(1 + (eps y/Lw)^2), cos theta = (eps y/Lw)/a_y).
#  1. Gauss's curvature from (a_x, a_y, theta) alone (Brioschi's formula, by differences): zero for this web?
#  2. A packet's path in the true positions: straight with the angle used; and with the angle ignored (lines taken at right angles)?
# Stated before running: with the angle, the true path is straight to 0.3 hop over the run; with it ignored, it departs by more than 3 hops.
import numpy as np
L=256; Lw=256.0; r=0.5; sig=14.0; dt=0.5; order=10; T=100; eps=0.8; kmag=0.3
g=np.arange(L)-L/2; x,y=np.meshgrid(g,g,indexing='ij')
kk=2*np.pi*np.fft.fftfreq(L); KX,KY=np.meshgrid(kk,kk,indexing='ij')
sl=eps*y/Lw; ax=np.ones((L,L)); ay=np.sqrt(1+sl**2); d2=(1+sl)**2+1.0            # diagonal of the square from (x,y) to (x+1,y+1): (1 + slope, 1) in true positions
cth=(d2-ax**2-ay**2)/(2*ax*ay); sth=np.sqrt(1-cth**2)
def gauss(E,F,G):
    du=lambda f:(np.roll(f,-1,0)-np.roll(f,1,0))/2; dv=lambda f:(np.roll(f,-1,1)-np.roll(f,1,1))/2
    Eu,Ev,Fu,Fv,Gu,Gv=du(E),dv(E),du(F),dv(F),du(G),dv(G); Evv,Fuv,Guu=dv(Ev),dv(Fu),du(Gu)
    det3=lambda a,b,c,d,e,f,g_,h,i:a*(e*i-f*h)-b*(d*i-f*g_)+c*(d*h-e*g_)
    A=det3(-Evv/2+Fuv-Guu/2,Eu/2,Fu-Ev/2, Fv-Gu/2,E,F, Gv/2,F,G); B=det3(0*E,Ev/2,Gu/2, Ev/2,E,F, Gu/2,F,G)
    return ((A-B)/(E*G-F**2)**2)[6:-6,6:-6]
K=gauss(ax**2,ax*ay*cth,ay**2); print(f"1. curvature from lengths and diagonal: rms {np.sqrt((K**2).mean()):.1e} per hop^2 (lengths vary by {ay.max()-1:.3f}, the angle from {np.degrees(np.arccos(cth)).min():.0f} to {np.degrees(np.arccos(cth)).max():.0f} degrees)")
Kb=gauss(ax**2,0*ax,(1+0.5*x*y/Lw**2)**2); print(f"   for comparison, a curved web with right angles (a_y = 1 + xy/(2 Lw^2)): rms {np.sqrt((Kb**2).mean()):.1e}")
def dsin(p,i): return np.fft.ifft2((np.sin(KX),np.sin(KY))[i]*np.fft.fft2(p))
def dcos(p,i): return np.fft.ifft2((1-np.cos((KX,KY)[i]))*np.fft.fft2(p))
sgx=lambda p: np.array([p[1],p[0]]); sgy=lambda p: np.array([-1j*p[1],1j*p[0]]); sgz=lambda p: np.array([p[0],-p[1]])
def make_H(use_angle):
    Exx=1/ax; Exy=(-cth/sth/ax) if use_angle else 0*ax; Eyy=(1/(sth*ay)) if use_angle else 1/ay; wx,wy=1/ax,1/ay
    def H(q):
        sxq,syq=dsin(q,0),dsin(q,1)
        out=0.5*(Exx*sgx(sxq)+sgx(dsin(Exx*q,0)))+0.5*(Exy*sgy(sxq)+sgy(dsin(Exy*q,0)))+0.5*(Eyy*sgy(syq)+sgy(dsin(Eyy*q,1)))
        return out+r*0.5*(wx*sgz(dcos(q,0))+sgz(dcos(wx*q,0))+wy*sgz(dcos(q,1))+sgz(dcos(wy*q,1)))
    return H
W=(x+eps*y**2/(2*Lw))+1j*y
def run(use_angle,x0,y0,th):
    H=make_H(use_angle); ix,iy=int(x0+L/2),int(y0+L/2); s0=sl[ix,iy]
    Kt=kmag*np.array([np.cos(th),np.sin(th)]); qx,qy=Kt[0],Kt[0]*s0+Kt[1]            # label wavenumbers: q_i = K . t_i, t_x = (1,0), t_y = (slope,1)
    env=np.exp(-(((x-x0)+s0*(y-y0))**2+(y-y0)**2)/(4*sig**2)+1j*(qx*x+qy*y))
    sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); u=np.linalg.eigh(Kt[0]*sx+Kt[1]*sy)[1][:,1]
    p=np.array([u[0]*env,u[1]*env]); p/=np.sqrt((abs(p)**2).sum()); path=[]
    for n in range(int(T/dt)+1):
        if n%20==0:
            dd=(abs(p)**2).sum(0); dd/=dd.sum(); path.append((n*dt,(dd*W).sum()))
        term=p.copy(); acc=p.copy()
        for j in range(1,order+1): term=(-1j*dt/j)*H(term); acc=acc+term
        p=acc
    path=np.array(path); t=path[:,0].real; Xc,Yc=path[:,1].real,path[:,1].imag; cx=np.polyfit(t,Xc,1); cy=np.polyfit(t,Yc,1); v=np.hypot(cx[0],cy[0])
    dev=((Xc-np.polyval(cx,t))*(-cy[0])+(Yc-np.polyval(cy,t))*cx[0])/v
    hd=np.degrees(np.arctan2(np.gradient(Yc,t),np.gradient(Xc,t)))
    return v,abs(dev).max(),hd[-2]-hd[1],np.degrees(np.arctan2(cy[0],cx[0]))
for nm,ua in (("angle used",True),("angle ignored",False)):
    v,dev,turn,head=run(ua,-40.0,-60.0,np.radians(60))
    print(f"2. {nm}: true path speed {v:.4f}, heading {head:.1f} degrees (launched at 60), turning by {turn:+.2f} degrees, sideways departure from a straight line at most {dev:.3f} hop over {v*T:.0f} hops",flush=True)
