# G10 — does extra-species energy pass into the light species? (13 Nov 2026)

**Question.** Is there a conserved number that keeps energy in the walk's extra species (zone corners), or does a hop-scale event pass it into the light species (zone centre)?

**Set-up.** CO's 1D palindromic walk (w = 0.3), 4000 places. A packet in one band near k = π − 0.4 (the extra species, group speed 1.08 hops per tick) starts 1000 hops from a single place where the flip is increased by α for every step (a local hop-scale event). After 1500 steps the packet's weight is projected onto the walk's bands and split into |k| < π/2 (light species) and the rest.

**Result** (g10_conversion.out).

| θ | α | weight passed to the light species |
|---|---|---|
| 0 | 0 / 0.3 / 1.0 | 0 / 0.034 / 0.208 |
| 0.05 | 0 / 0.3 / 1.0 | 0 / 0.033 / 0.211 |

About 0.4 α² per event at small α; the mass flip makes no difference.

**Reading.** No conserved number keeps energy in the extra species: a single hop-scale event passes a share of order α² into the light species. Pairs of extra species can also turn into light species through smooth interactions, since their momenta π + π sum to zero on the lattice. Later events, set by the light species' tiny mass flips, are far too weak to convert anything. Whether the conversion empties the extra species before the epoch ends is not computed. One dimension; one event type. Grade: reading.

Script: g10_conversion.py.
