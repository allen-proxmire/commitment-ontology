import numpy as np
src=open('g13_loop.py').read().split('if __name__')[0].replace("L=3000;","L=LL;")
for (LL,tha,thb,D,sig,T) in [(3000,0.4,0.2,300,100,1500),(6000,0.4,0.2,600,250,2400),(6000,0.8,0.4,600,250,2400)]:
    exec(src)
    kappa=1.4e-5
    xa,xb=run(tha,thb,D,kappa,T,sig=sig)
    t=np.arange(T+1); onset=2*D/c0
    pre=slice(0,int(0.6*onset)); post=slice(int(1.5*onset),T)
    aa0=2*np.polyfit(t[pre],xa[pre],2)[0]; ab0=2*np.polyfit(t[pre],xb[pre],2)[0]
    aa=2*np.polyfit(t[post],xa[post],2)[0]; ab=2*np.polyfit(t[post],xb[post],2)[0]
    pa=c0**2*kappa*thb/2; pb=-c0**2*kappa*tha/2
    print(f"theta {tha}/{thb}, separation {2*D}, width {sig}: before the front a_a/pred={aa0/pa:+.4f}, a_b/pred={ab0/pb:+.4f}; after: a_a/pred={aa/pa:.4f}, a_b/pred={ab/pb:.4f}; (theta_a a_a + theta_b a_b)/(theta_a |a_a|) = {(tha*aa+thb*ab)/abs(tha*aa):+.4f}")
