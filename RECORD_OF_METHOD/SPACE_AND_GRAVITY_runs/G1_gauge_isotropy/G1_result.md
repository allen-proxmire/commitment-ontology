# G1 result — relabelling freedom forces linearised Einstein–Hilbert on the cubic graph, isotropically

Script [`g1_gauge_isotropy.py`](g1_gauge_isotropy.py); check [`g1_check.py`](g1_check.py). Registered before running ([`REGISTRATION.md`](REGISTRATION.md)).

| symmetry imposed (with linearised relabelling, δh_μν = k_μξ_ν + k_νξ_μ, and time reversal) | dimension of the space of quadratic, two-derivative costs |
|---|---|
| full rotations | 2 |
| cubic group only | 2 |

**Post-run check (passed).** The Fierz–Pauli cost (linearised Einstein–Hilbert, written independently) is gauge invariant to 3 × 10⁻¹⁴ and lies in the cubic solution space to a relative residual of 2 × 10⁻¹⁵; its tensor waves travel at speed 1 (units of the tick, ℓ/c) along an axis, a body diagonal and a generic direction.

**Further check.** Random members of the cubic space propagate tensor waves at one speed in every direction tested ((1,0,0), (1,1,0), (1,1,1), (1,2,3)); the speed differs between members, and one member had no real wave speed.

**Cold reading (re-ran the check; extra counts).** The result rests on resetting clocks as well as moving places. With moving places alone (ξ_i only) the cube allows 8 costs against 7 for rotations: one direction-dependent cost survives. With only a shift of h_0i (the one-way part's loop-only behaviour) the count is isotropic (4 = 4) but does not single out Einstein's cost. Resetting clocks (ξ_0) also shifts h_00, the lapse; that is what closes the count at 2.

**Reading.** On the cubic graph, the only quadratic two-derivative costs for the ten carriers that leave moving places and resetting clocks (including the lapse shift) free are linearised Einstein–Hilbert, up to two numbers: an overall strength and a time-rescaling (a speed, whose value and sign G1 does not fix). The cube's reduced symmetry admits nothing the full rotation group excludes, so isotropy at this order is forced, and Lorentz invariance emerges up to the speed.

**Ruling.** At linear order and long wavelength, the form of the relations' cost is **needed, given that resetting clocks (including the lapse shift) is free as well as moving places**, with two derivatives, without assuming Lorentz invariance. Moving places is P7's posit; resetting clocks is an extension of it to time, proposed for the author's ruling. With moving places alone the cube allows one direction-dependent cost. The speed and its sign come from elsewhere (the update's tick, ℓ/c, would fix it). Lovelock (general covariance) remains the route to the full nonlinear exterior.

**Scope.** Linear order, continuum (long-wavelength) limit, two derivatives; h_μν treated as a symmetric tensor with the cubic group acting on its indices; continuum gauge transformations; time reversal imposed; numerical null-space counting by random sampling (2500 samples per generator set). Not covered: the nonlinear rule; lattice-scale terms.
