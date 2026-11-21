# What inflation is asked to do, in the first ball's units (standard hot history run back to light at the hop's energy).
import numpy as np
MPl=1.2209e19; g=106.75; H0=67.4/3.0857e19*6.582e-25   # GeV, -, H0 in GeV (hbar H0)
Tg=2.7255*8.617e-14                                    # today's photon temperature in GeV
for l,lab in ((1.0e-32,"largest hop"),(5.73e-35,"smallest hop")):
    El=1.97327e-16/l                                   # GeV
    T=El/2.7; H=1.66*np.sqrt(g)*T**2/MPl               # mean photon energy = hop energy
    stretch=(T/Tg)*(g/3.91)**(1/3); Rball=4.40e26/stretch/l   # ball radius in hops
    hor=(El/H)                                         # Hubble length in hops (c/H divided by l)
    print(f"{lab}: T = {T:.2e} GeV; growth per tick in length H*tau = {H/El:.3f} (places: {3*H/El:.3f}); Hubble length {hor:.1f} hops; ball radius {Rball:.2e} hops; separate Hubble patches in the ball {(Rball/hor)**3:.1e}")
    aH=(H/H0)/stretch; print(f"   flatness: today |Omega_k| < 0.002 needs |Omega - 1| < {0.002/aH**2:.1e} then")
    # place-by-place noise: N places inside the region that becomes a 1-degree CMB patch (comoving ~ 1e2 Mpc ~ 3e24 m)
    Npatch=4/3*np.pi*(3.0e24/stretch/l)**3; print(f"   independent noise per place: ripple on a CMB-patch scale ~ 1/sqrt(N) = {1/np.sqrt(Npatch):.1e} (observed 1e-5)")
