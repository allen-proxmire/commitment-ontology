"""R3: the exponential metric against Kerr/Schwarzschild in the strong field.

Metric (isotropic, G = c = 1, U = M/rho):
    ds^2 = -e^{-2U} dt^2 + e^{2U} (d rho^2 + rho^2 dOmega^2)
Photon sphere: extremum of C/A with A = e^{-2U}, C = rho^2 e^{2U}.
Shadow radius (critical impact parameter) b = sqrt(C/A) at the photon sphere.
ISCO: innermost stable circular orbit of a massive particle, from the effective
potential of the same metric, found numerically.
Comparison values are Schwarzschild (spin is not modelled on either side).
"""
import numpy as np, json
from scipy.optimize import brentq

M = 1.0
A = lambda r: np.exp(-2*M/r)
B = lambda r: np.exp(2*M/r)
C = lambda r: r**2 * np.exp(2*M/r)

# photon sphere: d/dr (C/A) = 0
f = lambda r: (C(r+1e-7)/A(r+1e-7) - C(r-1e-7)/A(r-1e-7)) / 2e-7
r_ph = brentq(f, 1.0, 4.0)
b_exp = np.sqrt(C(r_ph)/A(r_ph))
b_sch = 3*np.sqrt(3)*M
# analytic: r_ph = 2M, b = 2 e M

# ISCO: for circular orbits E^2 and L^2 from A, C; stability from d^2 V/dr^2.
# Standard: L^2 = C^2 A' / (A C' - C A'),  E^2 = A^2 C' / (A C' - C A')
def d(fn, r, h=1e-6): return (fn(r+h) - fn(r-h)) / (2*h)
def L2(r): return C(r)**2 * d(A, r) / (A(r)*d(C, r) - C(r)*d(A, r))
# ISCO where dL2/dr = 0 (L^2 minimum)
g = lambda r: d(L2, r, 1e-4)
r_isco = brentq(g, 3.0, 12.0)
# Schwarzschild ISCO in isotropic coords: areal r = 6M -> isotropic rho = (6 - 2 + sqrt(36 - 12... )); use areal comparison instead:
# areal radius of exponential metric: R = sqrt(C) = rho e^{M/rho}
R_isco_exp = np.sqrt(C(r_isco))
R_isco_sch = 6.0 * M
R_ph_exp = np.sqrt(C(r_ph)); R_ph_sch = 3.0 * M

# orbital frequency at ISCO (areal-independent observable): Omega^2 = A'/C'
Om_isco_exp = np.sqrt(d(A, r_isco)/d(C, r_isco))
Om_isco_sch = 1/(6**1.5)   # M=1

out = {
 "photon_sphere_isotropic_rho": r_ph, "shadow_b_exp": b_exp, "shadow_b_schw": b_sch,
 "shadow_ratio_exp_over_schw": b_exp/b_sch, "shadow_deviation_delta": b_exp/b_sch - 1,
 "areal_R_photon_sphere_exp": R_ph_exp, "areal_R_photon_sphere_schw": R_ph_sch,
 "isco_isotropic_rho": r_isco, "areal_R_isco_exp": R_isco_exp, "areal_R_isco_schw": R_isco_sch,
 "Omega_isco_exp": Om_isco_exp, "Omega_isco_schw": Om_isco_sch, "Omega_isco_ratio": Om_isco_exp/Om_isco_sch,
 "EHT_delta_M87": "-0.01 +/- 0.17 (Psaltis et al. 2020)",
 "EHT_delta_SgrA": "about -0.08 +/- 0.09 to -0.04 +/- 0.09 depending on mass prior (EHT 2022)",
}
json.dump(out, open("r3_result.json", "w"), indent=1)
for k, v in out.items(): print(f"{k:34s} {v}")
