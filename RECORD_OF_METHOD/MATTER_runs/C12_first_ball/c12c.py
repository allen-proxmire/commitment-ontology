# C12's counts redone per whole: a quark has no commitment of its own, so the matter patterns that commit are the baryons and the electrons
# (and as many dark patterns). Beside them, the earlier count per quark, which stands if at the start, with no neutral wholes yet, quarks were the units (open).
import numpy as np
Rvis=4.40e26; V=4/3*np.pi*Rvis**3; ngam=410.7e6; eta=6.1e-10; Ngam=ngam*V; Nb=eta*Ngam; Ob,Oc=0.0224,0.120; mp=0.93827; e_per_b=0.875
rad=lambda N,l: (3*N/(4*np.pi))**(1/3)*l
print(f"visible universe: {Ngam:.2e} photons, {Nb:.2e} baryons, {e_per_b*Nb:.2e} electrons")
print("dark pattern's mass if the beginning made as many dark patterns as ...")
for lab,per in (("baryons",1.0),("baryons and electrons",1+e_per_b),("[per quark, earlier] quarks",3.0),("[per quark, earlier] quarks and electrons",3+e_per_b)):
    print(f"   {lab}: {Oc/Ob*mp/per:.2f} GeV")
for lab,N0 in (("per whole: baryons + electrons + as many dark",2*(1+e_per_b)*Nb),("per quark (earlier): quarks + electrons + as many dark",2*(3+e_per_b)*Nb)):
    print(f"first places, {lab}: {N0:.2e}; radius {rad(N0,1.0e-32)*1e6:.1f} um at l = 1.0e-32 m, {rad(N0,5.73e-35)*1e9:.0f} nm at l = 5.7e-35 m; places multiplied by the epoch's end (1 to 10 photons per place): {Ngam/10/N0:.1e} to {Ngam/N0:.1e}; growth in length {(Ngam/10/N0)**(1/3):.0f} to {(Ngam/N0)**(1/3):.0f} ({np.log((Ngam/10/N0)**(1/3)):.1f} to {np.log((Ngam/N0)**(1/3)):.1f} e-folds)")
