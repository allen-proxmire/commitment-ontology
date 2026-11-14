# B2: domain-wall walk, registration (14 Nov 2026, before the run)

**Reading under test.** Tuning 2 (a mass counter-term per fermion) can be removed by a domain-wall walk: CO's matter is the light mode bound to a wall in a short inner direction. Local disturbances then cannot give it mass, except through the exponentially small overlap between the two walls.

**Construction (scouted, not tested).** CO's 2D palindromic walk U = A_x A_s F(θ(s)) A_s A_x at w = 5π/16. x is the physical direction (momentum k). s is the inner direction, a ring of 2L places with θ = +0.5 on one half and −0.5 on the other. Scout: the band above quasienergy 0 has Chern number −1 for 0 < θ ≲ 1.6 and 0 for −1.5 ≲ θ < 0; the gap at π stays open between ±0.5. So each wall carries one one-way mode. At ε = 0 the scout found a residual mass m(L) falling exponentially, and the bound pair moving at c₀ = 2cos w to 0.1%.

**Mass measure.** At each k there are two sub-gap levels, one per wall. m = ½ min over k of their splitting.

**Disturbance.** After each step, every inner place s applies P_s = exp(−iε n̂_s·σ), with n_s = (1,1,1) + a unit Gaussian vector (independent per s; uniform in x, so k stays exact). The (1,1,1) part is a coherent shift standing in for loop corrections; the random part makes it generic. No symmetry is assumed or kept.

**Control.** CO's plain 1D walk at θ = 0, with the coherent disturbance exp(−iε n̂₀·σ), n̂₀ = (1,1,1)/√3. Its mass is expected to be of order ε: the leak a counter-term must cancel.

**Fail conditions (stated first).**
- F1: at ε = 0, log m against L (L = 8, 12, 16, 20) is not a falling straight line (slope > −0.1 per place, or R² < 0.99).
- F2: at L = 16, for ε = 0.05, 0.1, 0.2, the coherent disturbance or any of 20 random draws gives m > 0.01 ε (more than a 1% leak).
- Uninformative: the control leaks less than 0.3 ε.

**Expected from theory.** Pass: a single one-way mode cannot be gapped by anything local, whatever the symmetry (Chern protection needs none). The run checks that CO's actual walk realises this; it is not a test of the topology.

**Not tested here.** Disturbances varying in x (they break k; they cannot couple the walls, but this run does not show it). Time-dependent disturbances. Interactions. The 3+1D version, which needs a 4+1D walk. How a deliberate physical mass enters (a direct wall-to-wall coupling: a new rule).
