## P4: what P2 and P3 show, and the next law (draft)

*31 October 2026. A reading of P2 and P3, written before any new run.*

### 1. The two failures

| law | draw | result |
|---|---|---|
| A (P2) | H units uniformly from all U | non-local random order. The dimension is ≈ 2.3–3.2 at small scales and drifts to 1 at large, like transitive percolation. Effective spatial size U/H² |
| A′ (P3) | a seed, plus H − 1 units from holders within r links | thin, chain-like orders (d ≈ 1). Where the order fills in (H = 4, r = 3), the same drift: 2.3 → 1.2 |

### 2. A common cause (inference)
Both laws keep two things fixed.
1. **The stock is conserved,** so the set of current holders, a slice of "space", never holds more than U elements. Space has a fixed size, and every interval longer than the time to cross it looks one-dimensional.
2. **Each commitment has at most H parents.** A manifold-like order in d dimensions needs an element's past links to grow without bound if it is to be Lorentz-invariant (Bombelli–Henson–Sorkin; Reading I14's finite-valency result). Under the PI-weak ruling a preferred frame is allowed, but then space must still be allowed to grow.

The second cause is softened by PI-weak. The first is not: neither law has room for space to grow.

### 3. The next law: A″, possibility is made by commitment
**New statement.** Each commitment, besides moving the H units it draws, creates c new units, held by the newborn. So
$$
U_n=U_0+c\,n .
$$
- **This replaces** "possibility is conserved", one of CO's primitives. That is a real change to CO, not a tweak.
- **What it must output:**
  1. a manifold-like order with a stable dimension (P2's kill rule, unchanged);
  2. how the slice of space grows with the number of commitments. That is an expansion law that comes from the primitive and is not put in. For a d-dimensional region growing at fixed density, the slice's size W should grow as
$$
W(n)\propto n^{(d-1)/d}.
$$
- **Draws:**
  - local, as in A′, since PI-weak allows a frame and locality is what manifold-likeness needs;
  - c ∈ {1, 2}, H ∈ {3, 4}, r ∈ {2, 3}.
- **Kill rule:** P2's, plus the slice's growth exponent. It must agree with (d − 1)/d, using the measured d, to within 0.15.

### 4. What survival would mean
- **If A″ passes,** CO would have its first output that was not put in:
  - a dimension, and an expansion, both from "commitment creates possibility";
  - with c and H setting both.
- **If it fails,** the obstruction lies in finite, unit-based commitment itself. The next step is then a reading on whether CO's units should be replaced by an order-only law, which is the causal-set route. That would be an honest convergence, not a new theory.

### 5. Addendum (31 October): A″ and a regulated variant, explored before registering
- **A″ (c new units per birth), smoke test plus an unregistered diagnosis** (`primitivesP5/`, n = 1500). The slice grows with exponent 0.87–0.98 at every setting, close to linear. A d of 10 or more would be needed for (d − 1)/d to match, while the intervals show d ≈ 1. The registered run would be foregone, so it was not run.
- **Regulated creation (capacity K), exploratory** (`primitivesP5/explore_regulated.py`, n = 3000). A unit is created only when the newborn's r-ball holds fewer than K units. Every setting gave chains (d_MM ≈ 1.0–1.16) or no large intervals.
- **The P3 check proved, by Dilworth's theorem, that** a law with U fixed units covers the order with U chains (each unit's holders). So no antichain exceeds U, and every large interval becomes a chain.

**Reading.**
- In every unit-based law tried, the causal order is the history of the units' motion: each unit's holders form a chain, and an element has at most H past links.
- A fixed stock makes the order one-dimensional at large scales. A created stock makes it a shallow bush. Regulation and locality collapse it into threads.
- A manifold-like order with finite valency and a preferred frame does exist (the lattice). But the record's engine put the lattice in by hand: CO's geometry was always an input.
- "Possibility has no place" (A) is **excluded in every tested form.** Getting geometry from an order-only growth law is the central open problem of causal-set theory, not a gap special to CO.
