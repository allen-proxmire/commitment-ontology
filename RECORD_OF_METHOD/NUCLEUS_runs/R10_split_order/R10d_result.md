# R10d — the adopted walk's doublers are at the hop scale, not absent; r has a window; the π-sector counts

Script `r10d_window.py`, output `r10d_result.json`. The adopted walk is the palindrome x y z | flip | z y x with alternation angle θ(k) = θ + r Σ_j(1 − cos k_j). For each r the lightest mode anywhere in the zone away from the origin was found (48³ scan, Nelder–Mead refinement), in both the quasi-energy-0 sector and the quasi-energy-π sector.

| r | lightest 0-sector doubler (θ = 0.3) | lightest π-sector mode (θ = 0.3) | lightest extra mode, θ → 0 |
|---|---|---|---|
| 0.0 | 0.300 (degenerate with the physical mode) | 0.300 | 0 (32 points) |
| 0.1 | 0.499 at (½π, 0, −½π) | 0.399 at (½π, 0, 0) | 0.100 |
| 0.2 | 0.692 | 0.497 | 0.199 |
| 0.3 | 0.874 | 0.593 | 0.297 |
| 0.4 | 0.821 | 0.442 at (π,π,π) | 0.392 |
| 0.5 | 0.331 at (½π, π, π) | 0.158 at (π,π,π) | 0.142 |

**Corrections to R10.** (1) "Exactly one gapless point" at r = 0.5 was a threshold artefact: six extra 0-sector species sit at 0.331 beside the physical 0.300, and a π-sector mode at 0.158 is lighter than the physical one. (2) The unitary Wilson angle is periodic; past r ≈ 0.4 the angle θ + rW wraps and the heaviest points come back down. The window is roughly r ≲ 0.35. (3) The π-sector was never counted in R10; its lightest mode at (±½π, 0, 0) has mass ≈ θ + r, which sets the floor. (4) "The mass term gaps everything" in R10 was wrong: at r = 0 every doubler has mass θ, equal to the physical mode. (5) The massless palindrome has 32 zero points, not four.

**The correct statement.** With both rulings and r in the window, the walk has one light species and extra species at masses of order r to 0.9 in hop units, in both sectors. That is the standard Wilson-fermion statement (Wilson 1974; Karsten and Smit 1981), not a removal.

**What it means with a physical hop.** In lattice QCD the spacing is taken to zero and the Wilson doublers leave. Here the hop ℓ is physical, so the extra species are physical particles with the electron's quantum numbers and mass m_d ≈ r ħ/(ℓc) (the lightest, π-sector, θ → 0). With ℓ at the top-quark bound (1.1 × 10⁻¹⁸ m) and r = 0.3 that is ≈ 50 GeV, which is excluded (no charged lepton below ≈ 100 GeV from LEP). Read the other way: the absence of such particles bounds the hop from above, ℓ ≲ r ħ/(M_excl c) ≈ 6 × 10⁻¹⁹ m × (r/0.3)(100 GeV/M_excl), a factor 2–20 below the top-quark bound depending on r and the exclusion mass used. The doubler item therefore does not close; it converts to a bound on ℓ and a standing prediction of heavy copies at the hop scale.

**Rulings, regraded.** Hops in no preferred order: candidate (a cyclic order is not a ranking; the palindrome is itself an ordering; alternatives exist, Gupta and Short 2026). Alternation flip rate: candidate, with r ≲ 0.35. Doublers: open, as a bound on ℓ. R10's grading of both rulings as "needed" and of the item as "closed" is withdrawn.
