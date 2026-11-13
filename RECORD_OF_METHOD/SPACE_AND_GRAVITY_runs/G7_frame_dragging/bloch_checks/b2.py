exec(open('bloch.py').read().split("# check unitarity")[0])
import numpy as np
# brickwork alone, spinless (take spin block)
for b in [0.4]:
    for K in [0,0.5,np.pi]:
        C=(layer(K,b,1)@layer(K,b,0))
        print("C alone K",K,np.round(np.sort(np.angle(np.linalg.eigvals(C))),4), "  CC:",np.round(np.sort(np.angle(np.linalg.eigvals(C@C))),4))
print("full U bands at kx=0, th=0.4 (4 bands = k and k+pi folded, each +/-):")
for b in [0,0.05,0.4]:
    for K in [0,0.2,np.pi/2,np.pi-0.2,np.pi]:
        print(f" b={b} K={K:.3f}", np.round(bands(K,0,0.4,b),4))
print("light th=0:")
for b in [0,0.4]:
    for K in [0,0.4,np.pi]:
        print(f" b={b} K={K:.3f}", np.round(bands(K,0,0.0,b),4))
