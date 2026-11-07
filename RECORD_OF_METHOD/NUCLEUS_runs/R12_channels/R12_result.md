# R12 result — channels do not survive formation: k → 1

Script `r12_channels.py`, output `r12_result.json`. n₀ = 300, m₀ = 4 channels per pair at the start, thinning (W = 4) and pairing per channel, T = 120.

| q | m₀ | surviving pairs | mean k | pairs with k ≥ 2 | k ≥ 3 | distinct neighbours |
|---|---|---|---|---|---|---|
| 6 | 1 | 326 | 1.000 | 0 | 0 | 3.1 |
| 6 | 4 | 176 | 1.006 | 1 of 176 | 0 | 2.4 |
| 8 | 1 | 359 | 1.000 | 0 | 0 | 3.3 |
| 8 | 4 | 359 | 1.006 | 2 of 359 | 0 | 3.4 |
| 12 | 1 | 343 | 1.000 | 0 | 0 | 3.3 |
| 12 | 4 | 472 | 1.004 | 2 of 472 | 0 | 3.9 |

**Post-run check (passed).** m₀ = 1 reproduces R5-B: degree ≈ 3.1–3.3 at q = 6–12.

**Reading.** Starting with four channels per pair, the formation model ends with one: fewer than 1% of surviving pairs keep two, none keep three, at every q. The mechanism is the pairing rule itself: a quantum locks to one channel at each place and keeps to it, so a second channel on the same pair is used only if a second quantum happens to route through the same pair, and the thinning kills it first. Multiplicity does not track q. The count the nucleus needs does not come out of CO's formation model as it stands.

**Ruling.** Channels as the origin of the link matching: **excluded** in this formation model. The shape's three met clauses stand (sliding, pairing as matching, non-commutation for k ≥ 2); the fourth, k, is not supplied by the rules, and the model actively removes it. A different formation rule could change this, but that would be a new ruling, and the pairing rule is the one that gave lines (R5) and locality (R7), so it is not freely changed.
