# G17 — a black hole forming from matter on CO's walk (radial reduction) (14 Nov 2026)

**Question.** Can a cloud of matter on CO's walk collapse under its own gravity, the river sourced by the cloud itself, and form a horizon on time?

**Set-up.** The strong-field entry (shift alone, lapse and stretch at 1, w = 5π/16 fixed) in Painlevé–Gullstrand form for a spherical cloud: the drift inward at radius r is v(r) = √(2GM(<r)/r), set every step by the cloud's own enclosed mass (in GR a constraint, so no propagating field is needed for a spherical cloud). The cloud is many patterns, each pulled by the others; its density is carried by one wavefunction with the self-share (1/N) neglected, consistent with no self-pull. Radial reduction: CO's 1D walk in r (s-wave, far from the centre, where the 1/r terms of the radial Dirac equation are small). Zero momentum throughout (marginally bound dust). Drift capped at 1.9 hops per step near the centre.

**Prediction.** Each shell keeps its enclosed mass Mq while shells do not cross, and falls as

r_q^{3/2}(t) = r_q0^{3/2} − (3/2)√(2GMq) t,

crossing its own horizon r = 2GMq/c₀² at a definite time.

**Fail condition, stated first.** Lagrangian radii (radii enclosing a fixed share q of the mass) off this by more than the packet's spreading, shrinking as the cloud is made larger.

**Result.**
- *A hollow shell* (g17.py, g17.out): the shells cross (the outer reach the centre first), and the formula, which assumes no crossing, does not apply: the run shows the cloud falling nearly as one block. Not a test; replaced.
- *A uniform ball* (g17b.py, g17b.out; density per dr ∝ r² inside R, which collapses with no crossing). At 0.8 of the collapse time, with the radius shrunk about 3.3 times:

| cloud size (R, r_s) | shells q = 0.1, 0.3, 0.5, 0.7, 0.9: r ÷ prediction |
|---|---|
| 500, 150 | 0.95, 0.96, 0.90, 0.90, 1.01 |
| 1000, 300 | 0.97, 0.97, 0.98, 0.95, 0.98 |
| 2000, 600 | 0.99, 0.99, 0.99, 0.98, 0.98 |

  converging to the prediction as the cloud grows (its patterns' momentum spread, focused by the converging flow, falls in proportion).
- *Horizons* (g17c.py, g17c.out; R = 2000, r_s = 600): the shells q = 0.5, 0.7, 0.9, 0.97 cross their own horizons at t = 1931, 1851, 1787, 1808 against 1934, 1863, 1798, 1798 predicted: within 0.6%. Deeper inside (r ≲ 0.3 r_s, near the capped centre) the radii stray by up to 10%.

**Reading.** On CO's walk a cloud of matter, sourcing its own river, collapses as GR's dust does and forms a horizon on time: a black hole from matter, matter and field in one run at strong field. Limits: the radial reduction (s-wave, far from the centre), a Hartree cloud (one wavefunction for many patterns), the river as GR's constraint rather than a field evolved on the lattice (exact for spherical symmetry), zero momentum (marginally bound), the drift capped near the centre, and the centre itself not modelled. Grade: reading.

Scripts: g17.py (hollow shell), g17b.py (ball, three sizes), g17c.py (horizon crossings), each with its .out.
