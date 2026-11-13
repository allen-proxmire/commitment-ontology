# Curl-free nudge: b on y-relations varying along y, b(y) = asin(g y / 2)  ->  drift v_s(y) = g y.
# GR at unit lapse and flat slices (Painleve-Gullstrand form): H = E(k) + v_s(y) k_y. A pattern with zero momentum is
# carried at y' = v_s(y) (the free-faller of the PG form), so y(t) = y0 e^{g t}, momentum staying zero, every mass alike.
# Light moving along +y: speed c(k) + v_s(y) with dk/dt = -g sin k. Fail: momentum-zero packets not following y0 e^{gt},
# or different masses following different curves.
LX,LY=8,1600
exec(open('g12.py').read())
import sys
g=2e-4; T=300; t=np.arange(T+1)
By=np.arcsin(g*(yv+0.5)/2); Bx=np.zeros_like(x)        # link from y to y+1, drift taken at its midpoint
def track(th,ky0,y0,sig,Bys):
    p=packet_k(th,0,ky0,sig); p=np.roll(p,y0,axis=2); M=[]
    for s in range(T+1):
        M.append(moments(p)); p=stepD(p,th*np.ones_like(x),Bx,Bys)
    return np.array(M)
for name,th in [("matter 0.4",0.4),("matter 0.2",0.2),("matter 0.1",0.1)]:
    y0=200; M=track(th,0,y0,40,By)
    pred=M[0,1]*np.exp(g*t)
    print(f"{name}, zero momentum at y0={M[0,1]:.1f}: y(T)={M[-1,1]:.3f} predicted {pred[-1]:.3f} (moved {M[-1,1]-M[0,1]:.3f} vs {pred[-1]-M[0,1]:.3f}, ratio {(M[-1,1]-M[0,1])/(pred[-1]-M[0,1]):.4f}); k_y drift {M[-1,3]-M[0,3]:+.1e}"); sys.stdout.flush()
# light along +y from y0=-300: compare with ray integration of H = E(k)+v_s k
def ray(th,ky0,y0):
    y=float(y0); k=ky0; h=1e-5; ys=[y]
    for s in range(T):
        vy=(E(0,k+h,th,w0)-E(0,k-h,th,w0))/(2*h)+2*np.sin(np.arcsin(g*y/2))*np.cos(k)
        dk=-g*np.sin(k)*(1)   # -(d v_s/dy) sin k, v_s = 2 sin b = g y
        y+=vy; k+=dk; ys.append(y)
    return np.array(ys)
for name,th,ky0 in [("light +y",0,0.3),("light -y",0,-0.3)]:
    y0=-300 if ky0>0 else 300
    M=track(th,ky0,y0,40,By); M0=track(th,ky0,y0,40,np.zeros_like(By))
    d=M[:,1]-M0[:,1]; r=ray(th,ky0,y0)-ray(th,ky0,y0)*0; r0=y0+np.arange(T+1)*((E(0,ky0+1e-5,th,w0)-E(0,ky0-1e-5,th,w0))/2e-5)
    print(f"{name}: shift from the nudge at T: measured {d[-1]:+.3f}, ray {r[-1]-r0[-1]:+.3f}, ratio {d[-1]/(r[-1]-r0[-1]):.4f}; k_y change {M[-1,3]-M[0,3]:+.3e} vs ray {-g*np.sin(ky0)*T:+.3e}"); sys.stdout.flush()
