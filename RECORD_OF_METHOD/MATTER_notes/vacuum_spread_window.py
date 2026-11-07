"""Vacuum-spread window: lower bound from the dent (heating), upper bound from clock coherence.
Inputs are the sector's own: l = l_P sqrt(4 pi P_max / delta); delta ~ 1e-32; l ~ 1e-18 m."""
import math
hbar=1.055e-34; c=3e8; lP=1.616e-35
m_n=1.67e-27; m_e=9.11e-31
delta=1e-32; l=1e-18
Pmax=delta*(l/lP)**2/(4*math.pi)              # in units of hbar
print(f"P_max = {Pmax:.1f} hbar  (from l = l_P sqrt(4 pi P_max/delta))")
# --- lower bound on sigma (in units of hbar): dent dephasing Gamma=(delta/s)^2 * omega must stay below collapse bounds
om_n=m_n*c**2/hbar; om_e=m_e*c**2/hbar
Gamma_bound=1e-17   # s^-1 per nucleon, current CSL ceiling at r_C=1e-7 m (order of magnitude)
s_low=delta*math.sqrt(om_n/Gamma_bound)
print(f"omega_n = {om_n:.1e} s^-1, omega_e = {om_e:.1e} s^-1")
print(f"dent: sigma must exceed ~{s_low:.1e} hbar to keep Gamma=(delta/sigma)^2 omega below {Gamma_bound} s^-1  (heating floor: {delta*math.sqrt(om_n/1e-8):.0e} hbar for Gamma=1e-8)")
# --- upper bound on sigma: clock couples to h = 1 - P_free/P; spread sigma_h = sigma/P_free, P_free ~ P_max today
# a pattern averages over N_places = (lambda_C/l)^3 ; independent places -> sigma_h_eff = sigma_h/sqrt(N)
for name,m,om,t in [("electron",m_e,om_e,1.0),("nucleon (atom interferometer, t=1 s)",m_n,om_n,1.0)]:
    lamC=hbar/(m*c); N=(lamC/l)**3
    # require om*sigma_h_eff*t <~ 1
    sh_eff_max=1/(om*t); sh_max=sh_eff_max*math.sqrt(N); s_up=sh_max*Pmax
    print(f"{name}: lambda_C/l = {lamC/l:.0f}, N_places = {N:.0e}; sigma_h,eff <~ {sh_eff_max:.0e}; sigma <~ {s_up:.0e} hbar")
print("window: lower ~%.0e hbar, upper ~%.0e hbar  -> empty if lower > upper" % (s_low, 1/(om_n*1.0)*math.sqrt((hbar/(m_n*c)/l)**3)*Pmax))
