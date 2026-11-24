# The first ball's count with the lepton number in it. C7: the first commitments set the net count of every kind of pattern, and it is kept (afterwards only pairs).
# If kinds change in pairs (n <-> p e nubar; C10's shape), what is kept is the baryon number B and the lepton number L, so first places >= |B| + |L|
# (a floor: equality if the first commitments start no antipatterns of a kind whose patterns they also start). Today L = net electrons (= protons) + net neutrinos.
# Net neutrinos are not measured. Bound (BBN and the CMB, arXiv:2510.02438): -0.12 < L < 0.13 with L = sum (n - nbar)/T_cm^3;
# per photon that is L x (4/11)/(2 zeta(3)/pi^2) = 1.49 L, so up to about 0.19 per photon.
import numpy as np
Rvis=4.40e26; V=4/3*np.pi*Rvis**3; Ngam=410.7e6*V; eta=6.1e-10; Nb=eta*Ngam; e_per_b=0.875; conv=(4/11)/(2*1.2020569/np.pi**2)
rad=lambda N,l: (3*N/(4*np.pi))**(1/3)*l
print(f"visible universe: {Ngam:.2e} photons, {Nb:.2e} baryons; L per T_cm^3 -> per photon: x {conv:.3f}; bound 0.13 -> {0.13*conv:.2f} per photon, {0.13*conv/eta:.1e} per baryon")
for lab,L,dark in (("L = 0 (net antineutrinos equal to the electrons)",0.0,2),("no net neutrinos, L = 0.875 B (the count so far)",e_per_b*Nb,2),("L = B",Nb,2),("|L| at the bound, no dark doubling",0.13*conv*Ngam,1)):
    N0=dark*(Nb+abs(L)); lo,hi=Ngam/10/N0,Ngam/N0
    print(f"{lab}: first places {N0:.2e}; radius {rad(N0,1.0e-32)*1e6:.3g} um at l = 1.0e-32 m, {rad(N0,5.73e-35)*1e9:.3g} nm at l = 5.7e-35 m; places multiplied by the epoch's end {lo:.2g} to {hi:.2g}; growth in length {lo**(1/3):.3g} to {hi**(1/3):.3g}"+("  (below 1: this L needs fewer than {:.1f} photons per place at the end)".format(Ngam/N0) if lo<1 else ""))
