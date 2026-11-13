# G6: light bending and slow fall on CO's 2D walk, field via the Wilson flip (2 cos w = c0 N/psi) and the mass flip (theta N).
# Linear response taken as the odd part in g: a_odd = (a(+g) - a(-g))/2; the even part is the field's second order.
src=open('g6.py').read().replace("Lx,Ly=400,256","Lx,Ly=640,256")
exec(src)
def traj(th,k0,g,lapse,stretch,sig,T=150):
    N=1-lapse*g*x; ps=1+stretch*g*x; w=np.arccos(c0*N/ps/2); p=packet(th,k0,sig); xs=[]
    for t in range(T+1): xs.append(np.sum(np.sum(abs(p)**2,0)*x)); p=step(p,w,th*N)
    return np.array(xs)
t=np.arange(151)
def acc(xs): return 2*np.polyfit(t,xs,2)[0]
import sys
cases=[(0,0.15,40),(0,0.3,30),(0.4,0,40)]
for th,k0,sig in cases:
    x0=traj(th,k0,0,0,0,sig)
    for g in [5e-5,2.5e-5]:
        row=[]
        for label,(la,st) in [("clock",(1,0)),("stretch",(0,1)),("clock+stretch",(1,1))]:
            ap=acc(traj(th,k0,g,la,st,sig)-x0); am=acc(traj(th,k0,-g,la,st,sig)-x0)
            row.append(f"{label}: odd {(ap-am)/2/(g*c0**2):+.4f} even {(ap+am)/2/(g*c0**2):+.4f}")
        print(f"theta={th} k0y={k0} sig={sig} g={g}:  "+" | ".join(row)); sys.stdout.flush()
