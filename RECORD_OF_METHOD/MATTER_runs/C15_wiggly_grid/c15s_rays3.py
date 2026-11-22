# Is the step's expected excess over light right? Rays of the step itself: H = w(x) E_W(k), E_W^2 = sin^2 kx + sin^2 ky + r^2 (2 - cos kx - cos ky)^2,
# dx/dt = w dE_W/dk, dk/dt = -E_W grad w, a bundle with the packet's spread in position (12) and wavenumber (1/24 per component), measured as the pattern was.
# Against: light's rays (c15s_rays2 at the group speed) and the pattern at L = 640 (c15s2).
import numpy as np
T=240.0; kap=1.5; s=5.0; b=40.0; x0=-120.0; k0=0.3; sig=12.0; n_rays=40000; h=0.25; r=0.5
def wfun(case,X,Y):
    rh=np.sqrt(X**2+Y**2+s**2); a=1+kap/rh; N=1-kap/rh; return {"lengths only":1/a,"clock only":N,"both":N/a}[case]
def EW(k):
    return np.sqrt(np.sin(k[:,0])**2+np.sin(k[:,1])**2+r**2*(2-np.cos(k[:,0])-np.cos(k[:,1]))**2)
def dEW(k):
    E=EW(k); m=r**2*(2-np.cos(k[:,0])-np.cos(k[:,1])); return np.stack([(np.sin(k[:,0])*np.cos(k[:,0])+m*np.sin(k[:,0]))/E,(np.sin(k[:,1])*np.cos(k[:,1])+m*np.sin(k[:,1]))/E],1)
def bundle(case,seed,light):
    rng=np.random.default_rng(seed); P=np.stack([x0+sig*rng.standard_normal(n_rays),b+sig*rng.standard_normal(n_rays)],1)
    K=np.array([k0,0.0])+rng.standard_normal((n_rays,2))/(2*sig); tr=[]; e=1e-3
    for i in range(int(T/h)+1):
        if i%20==0: tr.append((i*h,P[:,0].mean(),P[:,1].mean()))
        w=wfun(case,P[:,0],P[:,1]); gw=np.stack([(wfun(case,P[:,0]+e,P[:,1])-wfun(case,P[:,0]-e,P[:,1]))/(2*e),(wfun(case,P[:,0],P[:,1]+e)-wfun(case,P[:,0],P[:,1]-e))/(2*e)],1)
        if light: kn=np.linalg.norm(K,axis=1)[:,None]; v=0.964*K/kn; En=0.964*kn[:,0]
        else: v=dEW(K); En=EW(K)
        K=K-h*En[:,None]*gw; P=P+h*w[:,None]*v
    tr=np.array(tr)
    def head(ta,tb):
        m=(tr[:,0]>=ta)&(tr[:,0]<=tb); return np.degrees(np.arctan2(np.polyfit(tr[m,0],tr[m,2],1)[0],np.polyfit(tr[m,0],tr[m,1],1)[0]))
    return head(T-40,T)-head(0,40)
pat={"lengths only":-4.425,"clock only":-4.996,"both":-9.962}
for case in pat:
    st=[bundle(case,sd,False) for sd in range(3)]; li=[bundle(case,sd,True) for sd in range(3)]
    print(f"{case}: the step's own rays {np.mean(st):+.3f} (+/- {np.std(st)/np.sqrt(3):.3f}); light's rays {np.mean(li):+.3f}; pattern {pat[case]:+.3f}; step's rays over light's {np.mean(st)/np.mean(li):.3f}; pattern over step's rays {pat[case]/np.mean(st):.3f}",flush=True)
