# R12 — do parallel relations (channels) survive formation, and how many per link?

**Question.** The formation model (R5-B: all-to-all start, thinning of relations that carry nothing, pairing by first passage) was run on a simple graph, one relation per pair, so channels were excluded by construction. Allow m₀ parallel relations per pair at the start, thin and pair *per channel*, and read off the surviving multiplicity k per connected pair.

**Model.** R5-B with each pair starting with m₀ channels (m₀ = 4). A quantum arriving at a place by channel r leaves by the channel paired with r at that place; unpaired arrivals pick a random unpaired channel and the pair is kept. A channel idle for W steps dies. Quanta per place q ∈ {6, 8, 12}; n₀ = 300; T = 120; W = 4.

**Measured.** Distribution of k (channels per surviving pair) at the end; mean k; fraction of pairs with k ≥ 2 and k ≥ 3; and how these depend on q.

**Outcome unknown.** If k → 1 for all q: channels do not survive formation; the channel shape closes. If k has weight at 2–3 that tracks q: the count the nucleus needs lives in the formation model's parameters (capacity, δ), and the channel shape stands as candidate.

**Post-run check.** With m₀ = 1 the run must reproduce R5-B's degree ≈ 3–4 at q = 6–8.
