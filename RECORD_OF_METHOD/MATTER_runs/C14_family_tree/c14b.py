# Rule C again, averaged over 24 seeds. In c14.py one coarse level (0.87) fell outside the 10% band set beforehand: the band was tighter than
# one seed's scatter there (the variance added is a difference of two measured variances, each over a few hundred regions). The fail stands in c14_out.txt.
import numpy as np
s=0.01; G=20; S=24; acc=[]
for seed in range(S):
    rng=np.random.default_rng(100+seed); P=np.ones(1)
    for g in range(G):
        x=s*rng.standard_normal(P.size); P=np.column_stack((P*(1+x)/2,P*(1-x)/2)).ravel()
    var=np.array([np.var(P.reshape(-1,2**j).sum(1)*2**(G-j)) for j in range(G+1)])
    acc.append((var[:-1]-var[1:])/s**2)
acc=np.array(acc)[:,:G-6]; m=acc.mean(0); e=acc.std(0)/np.sqrt(S)
print("variance added per halving, in units of s^2 (mean of 24 seeds, +/- standard error), from the smallest regions up:")
print(" ".join(f"{a:.3f}+/-{b:.3f}" for a,b in zip(m,e)))
print(f"all levels together: {m.mean():.3f}; largest departure from 1: {np.max(abs(m-1))*100:.1f}% (the 0.2% excess at the smallest regions is the second-order term, about 20 s^2)")
