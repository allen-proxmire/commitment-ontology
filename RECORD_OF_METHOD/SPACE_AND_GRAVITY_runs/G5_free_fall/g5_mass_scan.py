# Does every mass fall alike? Slow fall on the lattice: a = -(dE0/dz) * E''(0),
# E0(theta N) the rest energy, E''(0) = (dE^2/dk^2 at 0)/(2 E0), the inverse inertia. Compared with g c0^2.
# E^2 is smooth in k^2, so its slope is taken by Richardson extrapolation (no mpmath here).
exec(open('g5_free_fall.py').read().split('print("drift check')[0])
def slope2(th,h):   # (E(h)^2 - E(0)^2)/h^2, Richardson in h^2
    f=lambda h:(E(h,th)**2-E(0,th)**2)/h**2
    return (4*f(h/2)-f(h))/3
def dE0(th):
    d=1e-3; f=lambda d:(E(0,th*(1+d))-E(0,th*(1-d)))/(2*d)
    return (4*f(d/2)-f(d))/3
print("massless c0^2 from E^2 slope:",slope2(0,1e-3),"vs c0^2",c0**2)
for th in [0.001,0.003,0.01,0.03,0.1,0.2,0.4]:
    Epp=slope2(th,0.05*th)/E(0,th)            # d2E/dk2 = (dE^2/d(k^2))/E0 ... = 2*slope/(2E0)
    r=dE0(th)*Epp/c0**2
    print(f"theta={th}: E0={E(0,th):.6f}  a/(g c0^2)={r:.7f}  (r-1)/theta^2={(r-1)/th**2:.4f}")
