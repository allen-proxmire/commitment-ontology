# Q1: where the Dirac automaton's current flows at rest

Script: [`q1_zitter_current.py`](q1_zitter_current.py); numbers in `q1_result.json`.

**Registered before running.** The three-dimensional Dirac automaton (split-step α-shifts, then the mass step exp(−iβθ)), started from one site in the spin-up positive-energy rest spinor, θ = f/L ∈ {1, 0.5, 0.2}. The conserved bond currents of a step are accumulated substep by substep. Measured: circulation per edge around every unit cube's six square faces and four Petrie hexagons (the chairs) near the origin (RMS), the net current, and the angular momentum of the current. The chair hypothesis says hexagonal circulation dominates square circulation at θ near 1. Outcome unknown.

**Result.** (14³ lattice; net current zero in every run.)

| θ | steps | square circ./edge (RMS) | hexagon circ./edge (RMS) | hex / sq | L_z of the current |
|---|---|---|---|---|---|
| 1.0 | 4 | 0.0053 | 0.0046 | 0.87 | 0.76 |
| 1.0 | 8 | 0.0013 | 0.0011 | 0.88 | 0.31 |
| 0.5 | 4 | 0.0062 | 0.0054 | 0.87 | 0.31 |
| 0.5 | 8 | 0.0011 | 0.0009 | 0.87 | 0.22 |
| 0.2 | 4 | 0.0049 | 0.0042 | 0.87 | 0.29 |
| 0.2 | 8 | 0.0004 | 0.0003 | 0.88 | −0.05 |

- The ratio is 0.87 in every run, independent of θ and of the number of steps. That is the geometric ratio for a *smooth* circulating field sampled by the two loops: a hexagon has area √3 over six edges, a square area 1 over four, and (√3/6)/(1/4) = 0.866. The current samples the same curl either way. **No preference for chair paths.**
- The current does circulate about the spin axis (L_z ≠ 0, net current zero): the zitter is there, as a smooth vortex about the spin, not as a hexagonal orbit.
- A single-site start is not a stationary state and disperses (values fall with steps); the geometric ratio is unaffected by that.

**Reading.** **The chair is not the electron's orbit.** The Dirac walk at rest has a smooth circulating current about the spin axis with no lattice-loop structure at any mass. What the loop picture supplied, the internal state (chirality × sense) and the mass as flip density, is carried by the walk; the loop as a literal path is not. The chair's role shrinks to an illustration of the maximal flip density and the Weyl sign correlations, which it still exhibits. "One pattern" stands as "one walk with one internal state"; "one pattern" as "one chair-shaped loop" is excluded by this run.

**Post-run check.** Continuity holds exactly for the substep currents by construction (the earlier whole-step current was not conserved and was replaced). The 0.866 geometric value was computed independently and matches the measured ratio to two digits in all six runs.
