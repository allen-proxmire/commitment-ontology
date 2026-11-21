# Can growth make the ripples? Four growth rules, one measure: how uneven is the count of places in a region, against the region's size.
# Stated before running (fail if outside):
#  A  independent families (every first place grows its own family, sizes random): unevenness falls as size^-1/2 (slope -0.50 +/- 0.05).
#  B  random births (any place may bear the next, the child beside it): unevenness of one ancestor's descendants is 1.0 +/- 0.3 at every depth.
#  C  a conserved amount split in two again and again, each split uneven by a fixed fraction s: the variance added per halving is s^2 +/- 10% at every level.
#  D  a conserved amount in whole units, each unit sent left or right at random: slope -0.50 +/- 0.05.
import numpy as np
rng=np.random.default_rng(14)
def slope(x,y): return np.polyfit(np.log(x),np.log(y),1)[0]
# A
M=2**22; n=1e8*(1+0.3*rng.standard_normal(M))
xs=[];ys=[]
for j in range(0,20,2):
    b=n.reshape(-1,2**j).sum(1); xs.append(2**j); ys.append(b.std()/b.mean())
sA=slope(xs,ys); print(f"A independent families (spread 30%): unevenness {ys[0]:.2e} at 1 family, {ys[-1]:.2e} at {xs[-1]} families; slope {sA:.3f}  [{'pass' if abs(sA+0.5)<0.05 else 'FAIL'}]")
# B  (birth order kept as a tree: descendants of the places present when the count was 2^k)
G=18; ks=list(range(3,13)); lab=np.zeros((len(ks),2**G),dtype=np.int32); N=1; res=[]
nxt={2**k:i for i,k in enumerate(ks)}
for trial in range(1):
    while N<2**G:
        if N in nxt: lab[nxt[N],:N]=np.arange(N)
        p=rng.integers(N); lab[:,N]=lab[:,p]; N+=1
okB=True
for i,k in enumerate(ks):
    c=np.bincount(lab[i,:N],minlength=2**k).astype(float); u=c.std()/c.mean(); res.append(u); okB&=abs(u-1)<0.3
print("B random births: unevenness of one ancestor's descendants, ancestors numbering 2^3..2^12: "+" ".join(f"{u:.2f}" for u in res)+f"  [{'pass' if okB else 'FAIL'}]")
# C
s=0.01; G=22; P=np.ones(1)
for g in range(G):
    x=s*rng.standard_normal(P.size); P=np.column_stack((P*(1+x)/2,P*(1-x)/2)).ravel()
var=[]
for j in range(G+1):
    b=P.reshape(2**(G-j),-1).sum(1) if j>0 else P; b=P.reshape(-1,2**j).sum(1); var.append(np.var(b/b.mean()))
var=np.array(var)   # var[j]: blocks of 2^j leaves; level depth G-j
added=(var[:-1]-var[1:])/s**2   # variance added by the split at each level, in units of s^2
use=added[:G-6]   # levels with at least 64 blocks to measure with
okC=np.all(abs(use-1)<0.10)
print(f"C uneven splits (s = {s}): variance added per halving, in units of s^2, from the smallest regions up: "+" ".join(f"{a:.2f}" for a in use[::2])+f"  [{'pass' if okC else 'FAIL'}]")
print(f"   unevenness of the count: {np.sqrt(var[0]):.4f} at 1 place, {np.sqrt(var[10]):.4f} at 2^10, {np.sqrt(var[16]):.4f} at 2^16 (no fall-off with size; it shrinks only as the levels above run out)")
# D
G=20; U=2**34; P=np.array([U],dtype=np.int64)
for g in range(G):
    l=rng.binomial(P,0.5); P=np.column_stack((l,P-l)).ravel()
xs=[];ys=[]
for j in range(0,16,2):
    b=P.reshape(-1,2**j).sum(1); xs.append(2**j); ys.append(b.std()/b.mean())
sD=slope(xs,ys); print(f"D whole units sent at random: unevenness {ys[0]:.2e} at 1 place, {ys[-1]:.2e} at {xs[-1]} places; slope {sD:.3f}  [{'pass' if abs(sD+0.5)<0.05 else 'FAIL'}]")
# What rule C must be to meet the sky (C13): count uneven by 3*sqrt(A_s) per e-fold of length; a halving of the count is ln2/3 e-folds of length.
As=2.1e-9; ns=0.965
s_need=3*np.sqrt(As)*np.sqrt(np.log(2)/3)
print(f"needed split unevenness: s = 3 sqrt(A_s) sqrt(ln2/3) = {s_need:.2e} (one part in {1/s_need:,.0f})")
print(f"needed drift: s larger by {(2**((1-ns)/6)-1)*100:.2f}% per halving toward the larger sizes ({(10**((1-ns)/2)-1)*100:.1f}% per tenfold in length)")
for Np in (1e88,1e89):
    h=np.log2(Np); print(f"halvings from one place to {Np:.0e} places: {h:.0f} ({np.log(Np)/3:.0f} e-folds in length); s at the first split {s_need*2**((1-ns)/6*(h-np.log2(1e83))):.1e} if the drift holds throughout")
print(f"random births (B) against the need, per halving: a random share has rms 2*sqrt(1/12) = {2/np.sqrt(12):.2f} against s: {2/np.sqrt(12)/s_need:.0f} times too uneven")
print(f"levels of the tree at the sizes seen (1e77 places up to the whole ball, 1e88-4e89): {np.log2(1e88/1e77):.0f} to {np.log2(4e89/1e77):.0f}")
print(f"with 7e80 first places at once, a tree lives only inside one family (2e7-2e8 places, under {(2e8)**(1/3):.0f} hops); the smallest size seen is 1e77 places")
