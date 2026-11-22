# Reading c16_out.txt: the neutral pattern's mass at bare m = 0 and at m*, from the two lowest gaps (E_n^2 = M^2 + v^2 (n pi/(N + d))^2, n = 1, 2),
# and how the mass answers to the bare mass (continuum: dM/dm = exp(gamma) = 1.781 near the massless point).
import numpy as np, re
rows=[l for l in open(__file__.replace("c16b.py","c16_out.txt")) if l.startswith("g = ")]
for l in rows:
    g=float(re.search(r"g = ([\d.]+)",l).group(1)); N=int(re.search(r"N = (\d+)",l).group(1)); ms=float(re.search(r"m\* = ([-+\d.]+)",l).group(1))
    a=[float(x) for x in l.split("gaps at m*: ")[1].split(";")[0].split()]; b=[float(x) for x in l.split("gaps at m = 0: ")[1].split()]
    M=lambda e: np.sqrt(max(e[0]**2-(e[1]**2-e[0]**2)/3,0))
    print(f"g = {g}, N = {N}: at m = 0, M/g = {M(b)/g:.3f}; at m* = {ms:+.3f}, M/g = {M(a)/g:.3f}; dM/dm between them = {(M(b)-M(a))/(0-ms):.2f}; M/g would be 0.564 at m = {-(M(b)-0.5642*g)*(0-ms)/(M(b)-M(a)):+.3f}")
