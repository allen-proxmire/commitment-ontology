# The spin term in a pair and in a three: does the colour rule's factor of two hold in the measured masses?
# M = sum m_i + A sum_{i<j} S_i.S_j / (m_i m_j). If the spin term is the colour field's (one exchange), A carries the pair's colour product:
# T_i.T_j = -4/3 for a quark with an antiquark, -2/3 for each pair in a three (sum over pairs = -(n/2) C_F), so A_pair / A_three = 2 for wholes of the same size.
# Stated before running: 2 by the colour rule; within 25% counts as holding, given that the two wholes need not be the same size. Sizes of the two fits not known beforehand
# beyond the textbook's round numbers.
import numpy as np
from scipy.optimize import least_squares
mes={"pi":138.0,"K":495.6,"rho":775.3,"K*":893.6,"omega":782.7,"phi":1019.5}
def mm(p):
    u,s,A=p; return {"pi":2*u-0.75*A/u**2,"rho":2*u+0.25*A/u**2,"omega":2*u+0.25*A/u**2,"K":u+s-0.75*A/(u*s),"K*":u+s+0.25*A/(u*s),"phi":2*s+0.25*A/s**2}
f=least_squares(lambda p:[(mm(p)[k]-mes[k])/mes[k] for k in mes],[310,480,6e7]); u,s,A=f.x; m=mm(f.x)
print(f"pairs: m_u = {u:.0f}, m_s = {s:.0f} MeV, A = {A:.3e} MeV^3 (A/m_u^2 = {A/u**2:.0f} MeV); misses: "+", ".join(f"{k} {100*(m[k]-mes[k])/mes[k]:+.0f}%" for k in mes))
bar={"N":938.9,"Lambda":1115.7,"Sigma":1193.2,"Xi":1318.3,"Delta":1232.0,"Sigma*":1384.6,"Xi*":1533.4,"Omega":1672.5}
def bm(p):
    u,s,A=p; return {"N":3*u-0.75*A/u**2,"Delta":3*u+0.75*A/u**2,"Lambda":2*u+s-0.75*A/u**2,"Sigma":2*u+s+A*(0.25/u**2-1/(u*s)),"Sigma*":2*u+s+A*(0.25/u**2+0.5/(u*s)),
                 "Xi":2*s+u+A*(0.25/s**2-1/(u*s)),"Xi*":2*s+u+A*(0.25/s**2+0.5/(u*s)),"Omega":3*s+0.75*A/s**2}
g=least_squares(lambda p:[(bm(p)[k]-bar[k])/bar[k] for k in bar],[360,540,2.6e7]); ub,sb,Ab=g.x
print(f"threes: m_u = {ub:.0f}, m_s = {sb:.0f} MeV, A = {Ab:.3e} MeV^3 (A/m_u^2 = {Ab/ub**2:.0f} MeV)")
print(f"A_pair / A_three = {A/Ab:.2f}   (colour rule: 2)")
print(f"the same from two splittings alone: (rho - pi) m_pair^2 / ((Delta - N) m_three^2) x (3/2) = {(775.3-138.0)*u**2/((1232.0-938.9)*ub**2)*1.5:.2f}")
print(f"dressed quark in a pair {u:.0f}, in a three {ub:.0f}: ratio {ub/u:.2f}")
