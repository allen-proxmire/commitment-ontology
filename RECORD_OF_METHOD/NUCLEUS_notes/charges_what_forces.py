# What forces the charges? Count the free numbers left in the charges of one generation under different sets of conditions (N_c = 3).
# Fields (left-handed): Q (colour 3, kind doublet), u^c, d^c, L (kind doublet), e^c; optionally nu^c. Electron's charge fixed as the unit (y_L = -1/2).
# The number of free charges left = unknowns - rank of the conditions' Jacobian at the known solution.
import numpy as np
Nc=3
def conds(v,gauged,nuc):
    yQ,yu,yd,ye=v[:4]; yn=v[4] if nuc else 0.0; yL=-0.5; c=[2*yQ+yu+yd, 2*Nc*yQ+Nc*(yu+yd)+2*yL+ye+yn, 2*Nc*yQ**3+Nc*(yu**3+yd**3)+2*yL**3+ye**3+yn**3]
    if gauged: c.append(Nc*yQ+yL)          # the kind label carrying a one-handed field of its own
    return np.array(c)
sol=np.array([1/6,-2/3,1/3,1.0,0.0])
for gauged in (True,):
    for nuc in (False,True):
        v=sol[:5 if nuc else 4]; f=lambda x: conds(x,gauged,nuc); J=np.array([(f(v+h)-f(v-h))/2e-6 for h in 1e-6*np.eye(len(v))]).T
        print(f"kind label {'with a one-handed field' if gauged else 'with no field of its own'}, {'with' if nuc else 'without'} a right-handed neutrino: conditions hold at the known charges to {abs(f(v)).max():.0e}; free numbers left: {len(v)-np.linalg.matrix_rank(J,tol=1e-6)}")
# With no one-handed field at all (light and colour only), left and right carry the same charge and every condition holds for any charges:
print("light and colour only (each pattern's two hands charged alike): no condition; Q_u, Q_d free (2 numbers), and the unit step between kinds is not forced")
