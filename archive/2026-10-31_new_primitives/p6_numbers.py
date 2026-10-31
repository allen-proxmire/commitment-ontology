# P6: primitive B (count/possibility is volume) against the engine-hop relation and route (b)'s window.
k = 0.99 * 3.141592653589793 / 3
for a in (1.0, 2 * 3.141592653589793):
    for lab, aPinf in [("B16-NR top at the cap (a*Pinf >= 5.05e27)", 5.05e27), ("registered top (a*Pinf >= 5.25e26)", 5.25e26), ("floor (a*Pinf <= 1.78e35)", 1.78e35)]:
        Pinf = aPinf / a; pc = Pinf ** (2 / 3) / (k * a); ell = (k * a * pc) ** 0.5
        print(f"a={a:.3f} {lab}: Pinf={Pinf:.2e}, p_c={pc:.2e}, hop={ell:.2e} l_P, wall 5.6e27*a={5.6e27*a:.1e}, clock floor 8e4")
# commitment 4-volume form: matter committing once per hold T = a hbar/E at Planck 4-volume per commitment -> density
hbar, c, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
lP = (hbar * G / c**3) ** 0.5; rhoP = c**5 / (hbar * G**2)
for a in (1.0, 6.283):
    rho_star = a * hbar / (c * lP**4)            # rho c^2/(a hbar) = c/lP^4  ->  rho* = a hbar/(c lP^4) = a x Planck density
    print(f"a={a}: 4-volume form needs mass density {rho_star:.2e} kg/m^3 = {rho_star/rhoP:.2f} x Planck density")
