# F1e: falling through a horizon on the flow step (G16/G17 carried over): registration (15 Nov 2026, before the run)

**Reading.** In the strong-field form (shift alone, N = ψ = 1; the author's ruling) on the flow step, H = K + σ_z m + ½{b, sin k}, a pattern at rest in the falling frame (k = 0) is carried by the shift: dx/dt = b(x), dk/dt = −b′ sin k = 0. With Painlevé–Gullstrand's b = −√(r_s/ρ) that is the radial path of a body falling from rest at infinity, ρ^(3/2) = ρ₀^(3/2) − (3/2)√r_s·t, crossing the horizon (|b| = 1 at ρ = r_s) with nothing special happening.

**Setup.** 1D radial line, 6000 places, hole centre at place 100 (b capped at |b| = 4 inside 6 places of it; the tick condition τ(3.0 + m + |b|) < π holds for |b| < 4.35). r_s = 400 places, packet at ρ₀ = 1200 (3 r_s), k = 0, m = 0.5, width 60. τ = 0.4, r = 0.5. Run until the predicted ρ = 0.5 r_s.

**Fail condition.** At ρ_predicted = 2r_s, r_s and 0.5r_s, the packet's mean differs from the prediction by more than 2% of the distance fallen.
