# c15s's answer to check against, done properly: a packet 12 hops wide at k = 0.3 spreads in angle by 1/(2 sig k) = 0.14 rad, so it does not
# follow one ray. Here a bundle of rays with the packet's own spread of positions and directions is traced in the same index n = 1/w,
# and the bundle's centre is measured exactly as the pattern's was (heading fitted over the first and last 40 time units).
import numpy as np
T=240.0; kap=1.5; s=5.0; b=40.0; x0=-120.0; k0=0.3; sig=12.0; n_rays=40000; h=0.25
def nfun(case,X,Y):
    rh=np.sqrt(X**2+Y**2+s**2); a=1+kap/rh; N=1-kap/rh; return {"lengths only":a,"clock only":1/N,"both":a/N}[case]
def bundle(case,seed=0):
    rng=np.random.default_rng(seed); P=np.stack([x0+sig*rng.standard_normal(n_rays),b+sig*rng.standard_normal(n_rays)],1)
    th=rng.standard_normal(n_rays)/(2*sig*k0); V=np.stack([np.cos(th),np.sin(th)],1); tr=[]; e=1e-3
    for i in range(int(T/h)+1):
        if i%20==0: tr.append((i*h,P[:,0].mean(),P[:,1].mean()))
        n=nfun(case,P[:,0],P[:,1]); gn=np.stack([(nfun(case,P[:,0]+e,P[:,1])-nfun(case,P[:,0]-e,P[:,1]))/(2*e),(nfun(case,P[:,0],P[:,1]+e)-nfun(case,P[:,0],P[:,1]-e))/(2*e)],1)
        gp=gn-V*(V*gn).sum(1)[:,None]; V=V+h*gp/n[:,None]**2; V/=np.linalg.norm(V,axis=1)[:,None]; P=P+h*V/n[:,None]
    tr=np.array(tr)
    def head(ta,tb):
        m=(tr[:,0]>=ta)&(tr[:,0]<=tb); return np.degrees(np.arctan2(np.polyfit(tr[m,0],tr[m,2],1)[0],np.polyfit(tr[m,0],tr[m,1],1)[0]))
    return head(T-40,T)-head(0,40)
pat={"lengths only":-4.903,"clock only":-5.517,"both":-10.867}; even=-0.186
for case in pat:
    t=np.mean([bundle(case,sd) for sd in range(3)]); print(f"{case}: bundle of rays turns {t:+.3f} degrees; pattern {pat[case]:+.3f} ({pat[case]-even:+.3f} with the even grid's own {even:+.3f} taken off); pattern over bundle {pat[case]/t:.3f} ({(pat[case]-even)/t:.3f})",flush=True)
print("the step's own share: a pattern of wavenumber k bends more than light by the ratio of its phase to its group speed, about 1 + 0.27 k^2 = 1.024 at k = 0.3")
