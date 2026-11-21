# Whose frame do the places keep, and what does that do to the photon and neutrino tests? And the places' motion in empty space. Desk arithmetic.
import numpy as np
c=2.998e5
print("1. Frames along the tests' paths (speeds against the frame of the cosmic background light):")
for nm,v in (("the Sun",370.),("the Local Group",620.),("the Galaxy's turning at the Sun",230.),("the Earth round the Sun",30.),("the Earth's spin at the equator",0.46)):
    print(f"   {nm}: {v:g} km/s, v/c = {v/c:.1e}")
b=620./c
print(f"   whichever of these frames the places keep, an energy read in it differs by at most v/c = {b*100:.2f}%.")
print(f"   photon ceiling: bound on l goes as E^-2, so it moves by at most {2*b*100:.1f}%, against the 11% error on the photons' energies and the factor 1.75 across the sky.")
print(f"   neutrino term: grows with E, so a moving frame adds a variation with direction and time of day of 2v/c = {2*370./c*100:.2f}% of the term (Sun's speed; phase goes as E L, both shifted); the term itself is unseen, so the bound is unchanged.")
print("2. A ball moving at V through empty space, places at rest far away. Counting places fixes the flow's divergence and its part normal to the ball;")
print("   the flow with no curl is then the one with least motion (Kelvin's theorem): u = -grad[ V R^3 cos(th) / (2 r^2) ].")
rng=np.random.default_rng(9); R=1.0; V=1.0; n=4_000_000
r=R/rng.random(n)**(1/3.)            # samples with density ~ r^-4 dr outside the ball (u^2 ~ r^-6)
mu=rng.uniform(-1,1,n); ur=V*mu*(R/r)**3; ut=0.5*V*np.sqrt(1-mu**2)*(R/r)**3
u2=ur**2+ut**2; w=(4*np.pi*r**2)/(3*R**3/r**4)   # volume element over sampling density, per unit mu-range/2
I=np.mean(u2*w)
print(f"   integral of u^2 outside the ball: {I:.4f} V^2 R^3 (exact 2 pi/3 = {2*np.pi/3:.4f}); a swirl added to it, tangent at the ball, only adds (cross term zero).")
print(f"   places slide past the ball's side at 1.5 V (ball's side moves at V, places beside it at -V/2): a slip surface, where places must change neighbours.")
print(f"   the dragged flow falls as (R/r)^3: {100*(1/2)**3:.0f}% of V one radius above the surface, {100*(1/10)**3:.1f}% at ten radii.")
