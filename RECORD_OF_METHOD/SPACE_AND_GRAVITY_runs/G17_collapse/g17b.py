# Homologous collapse (Oppenheimer-Snyder ball, marginally bound): density per dr ~ r^2 inside R (uniform in 3D), zero momentum.
# Then v(r) ~ r inside, every shell reaches the centre together: r_q(t) = r_q0 (1 - t/t_c)^{2/3}, t_c = (2/3) R^{3/2}/sqrt(2GM).
# Each shell keeps its own enclosed mass (no crossing): r_q^{3/2}(t) = r_q0^{3/2} - (3/2) sqrt(2 G M q) t, the comparison used.
# No shell crossing (a hollow shell crosses, which the first pass ran into). Horizon: the surface reaches r_s = 2GM/c0^2.
exec(open('g17.py').read().split('if __name__')[0])
import sys
def ball(th,R,edge):
    prof=np.where(r<R, (r/R), 0.0)*0.5*(1-np.tanh((r-R)/edge))   # amplitude ~ r (density ~ r^2), smooth edge
    prof=prof*(r>0)
    ks=2*np.pi*np.fft.fftfreq(L); f=np.fft.fft(prof); phi=np.zeros((L,2),complex)
    for i,k in enumerate(ks):
        if abs(f[i])<1e-10*np.abs(f).max(): continue
        ev,v=np.linalg.eig(Uk(k,th)); phi[i]=f[i]*v[:,np.argmin(np.angle(ev))]
    p=np.array([np.fft.ifft(phi[:,0]),np.fft.ifft(phi[:,1])]); return p/np.sqrt(np.sum(abs(p)**2))
def runb(th,R,edge,rs,T,qs,grav=True):
    p=ball(th,R,edge); out=[]
    for t in range(T+1):
        dens=np.sum(abs(p)**2,0); dens[r>L-200]=0; M=np.cumsum(dens); M/=M[-1]
        out.append([np.interp(q,M,r) for q in qs])
        rm=np.maximum(r+0.5,1.0); v=np.minimum(np.sqrt(c0**2*rs*np.interp(r+0.5,r,M)/rm),1.9) if grav else 0*r
        p=step(p,th,-np.arcsin(v/2))
    return np.array(out)
for scale in [1,2,4]:
    exec(open('g17.py').read().split('if __name__')[0].replace("L=1400;","L=%d;"%(1400*scale)))
    th=0.5; R=500*scale; edge=20*scale; rs=150.0*scale; tc=(2/3)*R**1.5/np.sqrt(c0**2*rs); T=int(0.8*tc); qs=[0.1,0.3,0.5,0.7,0.9]
    out=runb(th,R,edge,rs,T,qs); t=np.arange(T+1)
    line=[]
    for j,q in enumerate(qs):
        pred=np.maximum(out[0,j]**1.5-1.5*np.sqrt(c0**2*rs*q)*t,0)**(2/3)
        line.append(f"q={q}: {out[0,j]:.0f}->{out[-1,j]:.0f} (shell prediction {pred[-1]:.0f}, ratio {out[-1,j]/pred[-1]:.3f})")
    print(f"scale {scale}: t_c={tc:.0f}, run to {T}: "+"; ".join(line)); sys.stdout.flush()
