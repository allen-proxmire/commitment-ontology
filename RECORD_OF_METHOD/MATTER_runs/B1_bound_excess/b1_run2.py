exec(open('b1_bound.py').read().split('if __name__')[0])
import sys
for th,sig,L in [(0.005,0.01,300),(0.005,0.003,500),(0.002,0.01,300),(0.0,0.01,300),(0.01,0.01,300)]:
    qs,rr,FT=setup(L); Ks=[0,0.004,0.008]
    out=[bound_E(K,th,sig,L,qs,rr,FT) for K in Ks]
    Eb=np.array([o[0] for o in out]); a=np.polyfit(np.array(Ks)**2,Eb**2,1)[0]
    M=Eb[0]; sc=np.sqrt(a)/c0-1
    print(f"theta={th} sigma={sig} L={L}: M={M:.5f} (M/theta={M/th if th else float('inf'):.1f}) rms={out[0][2]:.1f} (rms at K=.008 {out[2][2]:.1f}) ++weight={out[0][1]:.3f}  E(K)={np.round(Eb,6)}  s_comp={sc:+.6f}  s(theta)={s_single(th):+.6f}  s(M)={s_single(M):+.6f}")
    sys.stdout.flush()
