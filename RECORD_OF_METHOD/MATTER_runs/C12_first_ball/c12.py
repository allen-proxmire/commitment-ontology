# Numbers for the beginning's ball, for the part of the universe visible today, and the dark pattern's mass under counting rules.
import numpy as np
Rvis=4.40e26; V=4/3*np.pi*Rvis**3            # comoving radius of the visible universe today (m)
ngam=410.7e6; eta=6.1e-10; Ngam=ngam*V; Nb=eta*Ngam
Ob,Oc=0.0224,0.120; mp=0.93827
print(f"visible universe: {Ngam:.2e} photons, {Nb:.2e} baryons ({3*Nb:.2e} quarks)")
print("dark pattern's mass if the beginning made as many dark patterns as ...")
for lab,per in (("baryons",1.0),("quarks (the patterns, by C9)",3.0),("quarks and electrons",3.0+0.875)):
    print(f"   {lab}: {Oc/Ob*mp/per:.2f} GeV")
rad=lambda N,l: (3*N/(4*np.pi))**(1/3)*l
for l,lab in ((1.0e-32,"largest hop allowed (neutrino bound)"),(5.73e-35,"smallest hop allowed (delta = 1)")):
    El=1.97327e-7/l
    for N0lab,N0 in (("first places = quarks + electrons + as many dark",2*(3+0.875)*Nb),):
        r0=rad(N0,l)
    for ppp in (1.0,10.0):
        Nex=Ngam/ppp; rex=rad(Nex,l)
        print(f"{lab}, l = {l:.2e} m: first ball ({N0:.1e} places) radius {r0:.2e} m; at the end of the beginning ({Nex:.1e} places, {ppp:g} photon(s) per place) radius {rex:.2e} m; growth in length {rex/r0:.0f}; places multiplied {Nex/N0:.1e}")
    Tg=2.7255*8.617e-5; stretch=El/Tg*(106.75/3.91)**(1/3)/2.7     # light at mean photon energy ~ hop energy then
    print(f"   standard history run back to light at the hop's energy ({El:.1e} eV): visible universe's radius then {Rvis/stretch:.2e} m")
    print(f"   mass-energy in the ball then: {Ngam*El*1.602e-19/9e16:.2e} kg; today's matter in the visible universe {Nb*1.673e-27*(Oc+Ob)/Ob:.2e} kg")
