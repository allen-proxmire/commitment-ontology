# R4: the beginning's sentence, as a network

Script: [`r4_first_relating.py`](r4_first_relating.py); numbers in `r4_result.json` (small) and `r4_result_large.json` (large).

**Registered before running.** Start all-to-all with a conserved stock; quanta hop to random neighbours; a relation that carries nothing for W steps is not a relation; a crossing quantum commits mid-transit with probability b, inserting a place (subdivision); births stop when free possibility per place falls under P_max. Expectation: with no cost term the result is a random sparse graph, expander-like, with a dimension that is large rather than three; the sentence would then need the mismatch cost to do real work.

**Result** (n₀ = 24, S = 20 000 quanta, P_max = 8, b = 0.02, W = 5, 300 steps).

| quantity | value |
|---|---|
| places at the end | 2 846 |
| free possibility per place | 7.0 (births stopped at P_max = 8) |
| degree histogram | 2 822 places of degree 2; 24 places of degree 23 |
| neighbourhood growth exponent (r = 2–6) | 2.1 |
| spectral dimension | not measurable (hub-and-chain structure) |

The final graph is the original complete graph on 24 places with every relation replaced by a chain of about 10 subdivided places. Thinning removed nothing among the original relations (the hubs carry most of the stock); births only subdivided. The structure is **K₂₄ with chains**: topologically the start, one-dimensional in between. The growth exponent near 2 is the hubs' signature, not a dimension.

**Reading.** The expectation was wrong in detail and right in substance. The sentence as written does not produce a dimension, and the reason is sharper than "needs the cost": subdivision preserves the topology of the start, and the mismatch cost prices relations that exist, it does not create any. So no cost term can rescue a start whose only relation-making is subdivision. **Excluded as written.** What the beginning needs and the sentence lacks is a rule by which *new relations form between places that were not related*: for example, two patterns committing at the same newborn place from different chains relating those chains. Without it, the first relating is the last.

**Second finding.** The free possibility per place settles just under P_max, as the threshold says, and the thinning leaves each original place with as many relations as its stock can feed: degree ≈ P∞/ħ in quanta. If this survives a corrected sentence, the degree of the adjacency, and so its dimension, is tied to the number of quanta a place holds: three dimensions on a lattice-like adjacency would mean P∞ of order a few quanta, not 10²¹. Noted, not relied on.

**Post-run check.** The degree histogram was inspected directly; the 24 hubs are the original places and the 23-degree is K₂₄ intact. The small run (n₀ = 12, S = 600) shows the same structure at degree 3.3 with chains of about 7.
