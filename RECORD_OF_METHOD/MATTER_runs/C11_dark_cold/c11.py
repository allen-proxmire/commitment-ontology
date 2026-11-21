# Why would a dark pattern made at the beginning be slow today? Momentum redshifts with the light's.
# If it starts with typical momentum f times the light's at that time (f <= 1), today p ~ 3.15 f T_x,
# T_x = T_gamma (g_today/g_then)^(1/3) (it shares none of the later heating of the light).
import numpy as np
Tg=2.7255; kB=8.617e-5; Tnu=1.945; Odm=0.120; rho_c_h2=1.0537e4   # K, eV/K, K, -, eV/cm^3
ngam=410.7
def Tth(m_th_keV): return Tnu*(Odm*93.14/(m_th_keV*1e3))**(1/3)      # temperature of a thermal relic that is all the dark matter
print("thermal warm-dark-matter bounds as a speed today (v = 3.15 T/m):")
for lab,mth in (("galaxy counts at high redshift",1.8),("Lyman-alpha forest (about)",5.3)):
    T=Tth(mth); v=3.15*kB*T/(mth*1e3); print(f"  m_thermal > {mth} keV ({lab}): T_relic = {T:.3f} K, speed today < {v:.2e} c = {v*3e5:.4f} km/s")
for gthen in (106.75,1000.0):
    Tx=Tg*(3.91/gthen)**(1/3)
    print(f"dark pattern starting with the light's typical momentum (f = 1), {gthen:g} kinds of light then: T_x = {Tx:.3f} K")
    for lab,mth in (("galaxy counts",1.8),("Lyman-alpha",5.3)):
        print(f"   cold enough if m > {mth*Tx/Tth(mth):.1f} keV ({lab})")
    for m,lab in ((0.13e3,"0.13 keV (Pauli bound)"),(10e3,"10 keV"),(5e9,"5 GeV")):
        print(f"   m = {lab}: speed today {3.15*kB*Tx/m:.1e} c")
for m in (10e3,5e9): print(f"number needed, m = {m:g} eV: {Odm*rho_c_h2/m/ngam:.2e} per photon (baryons: 6.1e-10)")
# born at one place with hop-scale momentum: how much stretching since then
for El in (1.9e25,3.4e27):
    print(f"born with momentum hbar/l = {El:.1e} eV/c, m = 5 GeV: needs stretching in length by > {El/5e9/3e-9:.1e} to reach 3e-9 c; the light's own stretch from hop-scale heat to today is about {El/(kB*Tg)*(106.75/3.91)**(1/3):.1e}")
