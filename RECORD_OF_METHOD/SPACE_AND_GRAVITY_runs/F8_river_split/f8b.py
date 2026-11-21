# Lambda's births and a body at rest: does it matter whether places are born inside it? Desk arithmetic.
import numpy as np
G=6.674e-11; c=2.998e8; yr=3.156e7; HL=2.2e-18*np.sqrt(0.69)
for nm,M,R in (("the Earth",5.972e24,6.371e6),("a cluster at rest, 1e15 Suns, 1 Mpc",1.989e45,3.0857e22)):
    w=HL*R; riv=np.sqrt(2*G*M/R)
    print(f"{nm}: drift of places born inside at Lambda's chance, at the edge, H_L R = {w:.2e} m/s ({w*yr*1e3:.2g} mm a year), w/c = {w/c:.1e}; the body's own river there {riv:.2e} m/s, to which Lambda adds (H_L R)^2/(2b) = {w*w/2/riv:.1e} m/s; Lambda's outward pull H_L^2 R = {HL**2*R:.1e} m/s^2 against GM/R^2 = {G*M/R**2:.1e}")
print("reading a (no births inside; rule 3 as stated): the body's river flows through its fixed places; Lambda adds to it in squares only.")
print("reading b (births inside at Lambda's chance, 3 H_L per place per time): the places drift out at H_L r and the body's patterns hop back to stay put.")
print("the two differ only in the hop-scale shift c2 -> c2 - w/2, with w/c as above.")
