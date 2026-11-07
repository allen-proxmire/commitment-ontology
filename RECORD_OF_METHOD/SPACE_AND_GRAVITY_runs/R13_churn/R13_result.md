# R13 result — churn is a contact effect: the pattern's own place becomes a hub; its neighbours are not changed

Script `r13_churn.py`; outputs `r13_result.json` (seed 3, M = 0, 6, 24, 96) and `r13_seeds.json` (seeds 5, 7, 11 averaged, M = 0 and 24).

| M (pattern quanta at place 0) | degree at distance 0 | distance 1 | distance 2 | distance 3 | background |
|---|---|---|---|---|---|
| 0 (3 seeds) | 1.3 | 2.5 | 2.8 | 3.9 | 2.8 |
| 24 (3 seeds) | 13.3 | 2.6 | 3.2 | 3.4 | 2.9 |
| 6 / 24 / 96 (seed 3) | 2 / 13 / 42 | 4.0 / 3.6 / 2.1 | 2.3 / 4.0 / 3.1 | 3.5 / 3.5 / 2.7 | 2.5 / 3.3 / 2.8 |

**Post-run check (passed).** M = 0 gives background degree ≈ 2.8, R5-B's value.

**Reading.** A renewing pattern keeps alive about M/2 relations at its own place (degree 13 for M = 24, 42 for M = 96): it is a hub. One step away the degree is at background or below (2.1 at M = 96, since the hub's many neighbours are each fed by one relation only); two and three steps away, background. The effect does not reach, does not grow with distance, and does not fall off as h does; it is confined to the relations the pattern itself crosses.

**Ruling.** The churn shape, that more relations kept per place near matter is the route half of the metric and that the two halves are one count: **excluded** in this formation model. What a renewing pattern does to the lattice is keep its own relations alive, which is the pooling rule's "possibility engaged at the place" said in relations; it does not stretch space around it. The route half of the metric stands where it was obtained, from ratio hopping.

**Scope.** One pattern model (out and back each step); 300 places; graph distance on an expander-like formation graph, not a geometric lattice. A different pattern model (transit that reaches further before returning) would feed relations further out, but that is the pattern's size, not churn.
