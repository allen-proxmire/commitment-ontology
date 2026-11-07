# R13 — churn: does a renewing pattern change the relation density around it, and how far does it reach?

**Question.** A pattern at rest renews by hopping across the relations at its place and returning (the zitter). Relations persist only while fed. Does a renewing pattern raise the number of surviving relations near it, and does the effect fall off with distance the way h does, or is it a contact effect?

**Model.** R5-B (n₀ = 300 places, q = 6 free quanta per place, all-to-all start, thinning W = 4, pairing by first passage, T = 120). Add at place 0 a pattern of M quanta that each step cross a random surviving relation at their current place and return the next step (at rest: no net direction). M ∈ {0, 6, 24, 96}.

**Measured.** Mean surviving degree (distinct neighbours) of places at graph distance 0, 1, 2, 3 from place 0, versus M; and the total number of surviving relations.

**Outcome unknown.** If degree rises at distance 0 and 1 only: a contact effect, and the churn shape is the pooling rule restated (or less). If the rise extends to distance 2–3 and grows with M: churn reaches, and "two halves, one count" becomes a candidate worth a geometric test.

**Post-run check.** M = 0 reproduces R5-B degree ≈ 3.
