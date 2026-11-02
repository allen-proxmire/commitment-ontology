# CO 2.0

A restart from the primitives. Nothing from [`ONTOLOGY.md`](ONTOLOGY.md) is assumed; what is kept is re-derived or re-ruled here. No runs. Conversation only, until the rulings settle.

**Method.** A rule is added only where the primitives are silent, and only if it retires at least one thing previously added by hand. A rule whose prerequisites are not yet ruled stays **candidate**.

## Primitives

| primitive | what it is |
|---|---|
| **Possibility** | the conserved stuff |
| **Commitment** | one irreversible act on it |
| **Matter** | commitment that renews |

**Matter, in one sentence.** Matter is a commitment that, on completing, engages adjacent possibility into its next commitment, releases what the last one held, and adds one to its count; it persists exactly as long as that cycle keeps closing.

## Consequences, not primitives

| term | what it is |
|---|---|
| **Time** | matter's count. Read only by ratio: N_A / N_B. Nothing says "what time it is" |
| **Record** | a commitment matter carries forward by renewing. Kept by being renewed; nothing else keeps anything |
| **Pattern** | possibility between commitments |
| **Place, relation** | the adjacency along which possibility moves. No claim that space comes from it |

**Space:** nothing said.

## Rulings

| ruling | statement |
|---|---|
| vacuum | possibility with no commitment. Timeless and scaleless by construction: zero commitments, zero count. Flow is undefined there; it becomes a fact only against matter's count |
| hold-and-release | a renewal engages possibility, completes, releases it. Nothing is consumed. P_free = P(1 − h), h the fraction engaged |
| (B) one quantum per renewal | every renewal engages the same amount, ħ. Mass is renewal frequency: ω = mc²/ħ. The first scale is an action, and it arrives with the first renewal |
| g linear | renewal rate = (m/ħ)(1 − h). h = 1 is the hole: everything local engaged, nothing free, no renewal completes. A ceiling approached, not a point reached |
| gravity | possibility moves toward where it is being engaged. Patterns ride possibility. So patterns fall toward matter, mass-independent. The slowed clock is the view from outside |

**Why (B).** The alternative, universal rate with varying engagement, cannot give universal redshift without an extra assumption, and gives E = ħω no reading. (B) gives both:

$$\frac{N_A}{N_B}=\frac{1-h_A}{1-h_B},\qquad h\propto\sum_i m_i\ \text{over adjacent matter}.$$

The quantity that slows clocks and the quantity that gravitates are the same, counted the same way.

**Clock mechanism vs clock reading.** A clock's mechanism references the possibility around it; a clock's reading references another clock. Neither needs a background tick.

## The balance

Strict local hold-and-release gives no field outside matter: a renewal engages at its adjacency and releases at the same adjacency, net zero per cycle. A clock a metre above the ground would run at full rate. So matter must be a **net sink** of free possibility. A steady point sink into a conserved, diffusing stock gives

$$\nabla^2 P_{\text{free}}=\sigma\,\delta(\mathbf r)\ \Rightarrow\ P_{\text{free}}(r)=P_\infty-\frac{k}{r},\qquad k\propto\sigma ,$$

Newton's potential, linear and unscreened, from conservation alone. The question is what makes matter a sink.

| option | statement | status |
|---|---|---|
| **pooling** | a renewal releases a fraction (1 − δ) of what it engaged; the rest stays engaged. The body's engaged stock grows, free possibility is drawn in to meet the deficit, and that draw is the field. The hole is where pooling finishes: h → 1 | **ruled** |
| circulation | engage from the near side, release to the far side, through a channel patterns do not ride | candidate |
| nothing | strict local release, no net sink | excluded: no field outside matter |

**Pooling, in one sentence.** A renewal releases a fraction (1 − δ) of what it engaged; the rest stays engaged as the body's record.

**The retained fraction is the record.** Of the three readings of "the rest," *destroyed* breaks conservation and leaves no ceiling (the engaged stock would not grow, so h could not reach 1); *leaves* is circulation under another name. *Stays engaged* keeps both, and says what a record is made of: possibility withdrawn from the free stock and held. "It is kept" means "it is still engaged." The hole is a body that is all record and no renewal. The count rising and the free stock falling are one process; the record only grows because δ > 0.

**What pooling costs.** δ is 2.0's first constant that is not ħ and not borrowed: a fraction of a quantum not returned per cycle, the same for every renewal. Sink strength is then

$$\sigma=\delta\,\hbar\,\omega=\delta\,mc^2 ,$$

so G ∝ δ/P∞.

**The vacuum far away.** Conservation gives

$$\dot P_{\text{free}}=-\dot P_{\text{engaged}}=-\delta\sum_i m_ic^2 .$$

- A uniform fall in P∞ makes no gradient: no force, and **not Λ**. Λ stays an input.
- Around a body h(r) = (k/r)/P∞, so the field strengthens as the floor falls:
 $$\frac{\dot G}{G}=-\frac{\dot P_\infty}{P_\infty}>0 .$$
 A sign: G increases. Lunar laser ranging and pulsar timing hold |Ġ/G| at or under about 10⁻¹³ per year, so the vacuum's depletion e-folding time exceeds about 10¹³ years; over the age of the universe at most a part in a thousand of the free stock has pooled. A body's own clocks slow on the same timescale, same sign.
- With no infinities the free stock is finite, so the record has a finite capacity and the process has an end: everything engaged. The Ġ/G bound is a lower bound on how far off that is.

**Second leg.** "Possibility moves toward engagement" is a flow statement and needs the sink. If the sink failed, attraction would still follow from a static gradient: patterns hop on free possibility, hop slower where it is scarce, and so linger near matter. Not needed under pooling; noted.

## The beginning

At the start everything is free: no matter, no renewal, no count. Under the rulings above that state is stable; nothing makes free possibility commit. The first commitment cannot be a renewal.

| option | statement | status |
|---|---|---|
| threshold | an adjacency holds at most P_max of free possibility; above that it commits. Retires "the vacuum never commits" (today P∞ < P_max); the start commits everywhere at once; the first epoch ends when P_free ≤ P_max everywhere, so P∞ ≲ P_max today | candidate |
| steep rate | r = r₀(P_free/P*)ⁿ with n chosen large | set aside: an exponent nothing fixes |
| boundary condition | the record has a first line; CO does not ask why | holds by default until the threshold's prerequisites are ruled |

**Prerequisites for the threshold.**
- Does a bare commitment (one with no predecessor) start a renewal cycle, or leave only a record?
- What lowers P_free to P_max: pooling (a large primordial record), or more adjacencies (space grows)?

## Open

- **The masses.** What sets each pattern's renewal frequency.
- **Space.**
- **δ.** Its value, and whether it is one number for every renewal.
- **Bare commitment.** Whether it renews.
