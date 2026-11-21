# What the sky's ripples ask of the first event, in the ball's units (end of the beginning; standard history back to the hop's energy).
import numpy as np
As=2.1e-9; ns=0.965; k0=0.05          # per Mpc
Mpc=3.0857e22; Rvis=4.40e26
Rball_hops=4.70e29                    # ball radius in hops at the epoch's end (C12b), the same for both l
hop_per_m_today=Rball_hops/Rvis       # hops (then) per comoving metre (today)
zeta=lambda k: np.sqrt(As*(k/k0)**(ns-1))
print(f"rms unevenness of the stretch per e-fold of size: sqrt(A_s) = {np.sqrt(As):.2e} at k = 0.05/Mpc")
for lab,k in (("largest seen (k = 2e-4/Mpc, the whole sky)",2e-4),("CMB pivot (0.05/Mpc)",0.05),("smallest seen (k = 3/Mpc, Lyman-alpha forest)",3.0)):
    lam=2*np.pi/k*Mpc; hops=lam*hop_per_m_today; N=hops**3
    print(f"  {lab}: size today {lam/Mpc:.0f} Mpc = {hops:.1e} hops then, {N:.1e} places; stretch uneven by {zeta(k):.2e}; count of places uneven by 3*zeta = {3*zeta(k):.2e}; independent noise would give {1/np.sqrt(N):.1e}")
print(f"change of the unevenness per factor 10 in size: {(10**((1-ns)/2)-1)*100:.1f}% larger on the larger size")
print(f"shear (gravitational-wave) part: below sqrt(0.036 A_s) = {np.sqrt(0.036*As):.1e}")
print(f"bell-curve shape: skewness below about f_NL*zeta = {10*np.sqrt(As):.0e} of the unevenness itself (|f_NL| < 10)")
print(f"matter-to-light ratio the same everywhere: uneven by less than about {np.sqrt(0.04)*np.sqrt(As):.0e} beyond the ripple itself (isocurvature share < 4%)")
print(f"size at which independent noise equals the need: N = 1/(3 zeta)^2 = {1/(9*As):.1e} places, {(1/(9*As))**(1/3):.0f} hops across, {(1/(9*As))**(1/3)/hop_per_m_today:.2f} m today")
