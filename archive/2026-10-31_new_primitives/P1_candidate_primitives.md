## P1: candidate primitives (draft)

*31 October 2026. Allen: "new primitive(s) … I want CO developed toward remarkable." This note changes the method. CO will no longer add one rule per phenomenon. It will take one law for how commitments grow, and judge it only by what that law forces. Each existing rule (R1–R11, Q1–Q7) must then follow from the law or be dropped. A candidate is worth keeping only if it outputs a number or a structure that was not put in.*

### 1. Why the method changes
- **What the runs could do.** Each run tested whether a chosen rule reproduces a known result, so a rule chosen to give a result returns that result.
- **What I15 found about the borrowed inputs.** They fall into one cluster. One known principle, path independence for the dynamics (PI-strong), would yield the whole cluster through the Hojman–Kuchař–Teitelboim theorem.
- **What T-I15b found about CO's own hold rule.** It breaks that principle's discrete form. The one rule that passed while presence still mattered draws a commitment's units uniformly from all possibility (C7):
$$
\Pr(S)=\binom{U}{H}^{-1},\qquad U=\text{total units, conserved}.
$$
- **Every local, presence-weighted draw picked a slicing.** This is the first result in the record that was not put in.

### 2. The candidates

| | primitive | what it replaces | what it must output | cheapest kill test |
|---|---|---|---|---|
| **A** | **Possibility has no place.** Possibility is one conserved stock, U units. A commitment draws H units uniformly from all of it, and its parents are the units' last holders. Places, distance and locality are not given: they are read off the order of commitments | the lattice, R1's per-place outflow, R2's local draw, the global hop rate; PI-strong becomes automatic at the discrete level (C7 satisfies DGC exactly) | a causal order that approximates a Lorentzian manifold of some dimension, without being told one; then the dimension, and how U and H set a length | **manifoldlikeness:** do C7 orders give a dimension estimate that is consistent across scales and across estimators? (P2, below) |
| **B** | **Count is volume.** Each commitment carries one fixed unit of spacetime volume (the causal-set number–volume correspondence) | the free hop ℓ and the free crossover p_c (I19, I20): the engine-hop relation ℓ² = k a ℓ_P² p_c would then fix p_c | p_c, and so saturation's onset map, as a number | whether the fixed volume is consistent with the engine-hop relation and the clock floor p_c ≳ 8×10⁴: one line of arithmetic once a volume unit is stated |
| **C** | **A record has a phase.** Each commitment carries a phase set by the units it draws, and records add as amplitudes | Q6 (Born from noncontextuality), A5's amplitudes | Born weights from counting, the "first non-restatement on Born" | whether the phase rule makes additivity F(w₁) + F(w₂) = F(w₁ + w₂) forced rather than assumed (I16's mirror question) |

**How they fit together.** A is the most basic: it says what the substrate is. B gives A a scale. C gives A a quantum phase. If A dies, B and C still stand as additions to the old CO. If A lives, B and C become statements about A's units.

### 3. Why A first
- **It is the only candidate the data pointed to** (T-I15b).
- **It is close to causal sets,** which is a sign that it is natural, and it carries their known obstacle with it. Transitive percolation, the best-studied covariant growth law, does not give manifold-like orders. Reading I14 suspected that C7, which ignores the state, would not either.
- **So A can die fast,** and that is useful.

**A is also not causal sets.**
- Its units are conserved, so the number of possible parents never grows beyond U.
- Its draw is uniform over units, not over earlier elements.
- So the shape of the growth is set by U and H. Whether that helps or hurts is what P2 measures.

### 4. Choices
1. Take A as the candidate primitive under test (P2), with B and C held.
2. P2's kill rule, written before any run (`P2_manifoldlike.md`).
