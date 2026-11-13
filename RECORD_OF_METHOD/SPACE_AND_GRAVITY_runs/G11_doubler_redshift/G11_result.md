# G11 — does zone-corner energy slide down the bands as places are born? (13 Nov 2026)

**Question.** As the lattice grows by births, does energy at the zone corner (the extra species) stay stranded there, or move to longer wavelengths with everything else?

**Set-up.** CO's 1D palindromic walk (w = 0.3, θ = 0). A packet at k = π − 0.2 (width 80) on 1000 places. Over 3000 steps, 3000 places are born at random positions (stretch a = 4). Two rules for what a newborn place carries of a passing pattern, since CO does not yet say: *empty* (zero amplitude), and *mean* (the mean of its two neighbours', with the total renormalised).

**The band.** On this walk the light band runs E = 0, 1.50, 2.97, 1.96, 1.20 at k/π = 0, ¼, ½, ¾, 1: the extra species at k = π are the far side of the same band as the light species, over a top near k = π/2.

**Result** (g11_redshift.out; mean |k|/π, and weight at |k| < π/2):

| a | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| empty births | 0.94, 0.00 | 0.70, 0.19 | 0.63, 0.30 | 0.60, 0.36 |
| mean births | 0.94, 0.00 | 0.59, 0.37 | 0.42, 0.64 | 0.33, 0.77 |

A pure stretch would take mean |k| from 0.94π to 0.23π at a = 4. Mean births come close; empty births move the packet more slowly, since random empty places scatter it.

**Control: ordinary light** (g11_light.py, a packet at k = 0.2; g11_light.out). Mean births redshift it as a pure stretch does: mean |k|/π from 0.064 to 0.018 at a = 4, against 0.016 for k/a, all of it staying at |k| < π/2. Empty births scramble it: mean |k|/π rises from 0.064 to 0.377 and 37% is thrown above π/2. Light from distant sources arrives redshifted and coherent, so births that leave newborn places empty are excluded; births must carry a passing pattern smoothly, as the mean rule does (needed, given births act on passing patterns at all).

**Reading.** With smooth births, the rule ordinary light needs, zone-corner energy is not stranded: births carry it to longer wavelengths, across the band top into the light species' range (77% by a = 4, mean |k| falling toward k/a). After the epoch the lattice stretches by about 10²⁸, so none would stay at the corner. The extra species then do not freeze in as a population; their energy redshifts with the rest of the radiation. This fits the account (hop-scale energy, not matter) and makes the freeze-in bound on p unnecessary. Open: the smooth-birth rule written as a rule of CO (what a newborn place carries of a passing pattern); 3D. Grade: reading.

Scripts: g11_redshift.py (g11_redshift.out), g11_light.py (g11_light.out).
