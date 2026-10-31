## Reading I22: how space curves, after ε = 0 

*31 October 2026. Allen: "look at 'how space curves, from the primitives'". A reading of the record; it encodes no new rule. Revised after one independent check, whose corrections are adopted. **Inference** marks a step past what the record or the literature says; **new statement** marks a proposal that would need a ruling.*

**In plain terms.** With ε zero in gravity, R9 ("option 3") is exactly GR's static field equation, and its one added choice has gone; the record already says so. Reading I15 showed that one known principle can turn most of the borrowed spacetime cluster into an output: path independence for the dynamics as well as the records (PI-strong), through the Hojman–Kuchař–Teitelboim theorem. The cluster is R9, R8's boost, the constraint algebra of Runs 85–91 and inertia = total energy. Adopting it would replace seven borrowed entries with one added principle and at least five technical conditions. The earlier ruling to keep ε stood in the way; since 30 October it does not, and the question is reopened.

Whether commitment *implies* PI-strong comes down, at the discrete level, to whether its growth rule ignores the order of commitments that are not causally related. Three things are known:
- The simplest grid-free hold passes.
- A holdings-weighted draw of units fails.
- In the check's unregistered exploration, a natural local form also passes at small sizes: a place commits at a rate set by its own holdings.

That last result is the step worth registering.

### 1. R9 at ε = 0 (restatement)
The record defines U through dU/dφ = 1 + g, with g = ε/N (Run 66 §2). That is U ≡ −ln N, since d(−ln N)/dφ = (1 + ε)e^{−φ}/N = 1 + ε/N. At ε = 0, N = e^{−φ}, so dU/dφ = 1, and with φ = U = 0 at infinity, **φ = U exactly**:
$$
ds^2=-e^{-2\varphi}dt^2+e^{2\varphi}\tilde\gamma_{ij}dx^idx^j,\qquad \tilde R_{ij}=2\,\partial_i U\,\partial_j U-16\pi\,p\,e^{2U}\tilde\gamma_{ij}.
$$
- **This is GR's R_ij equation for the static sector.** With the field equation Δ̃U = −4π(e + 3p)e^{2U} and the balance hN = const (Run 66 §1), it gives β = γ = 1.
- **The record already says it:** ONTOLOGY's ε paragraph ("R9's choice of φ's stress becomes empty (φ = U)"), I15 §6.1 and I15 choice 2(i).
- **Bookkeeping, still undone:**
  - R9's own note ("an added choice … ε sets every static departure from GR");
  - R3's line β − 1 = −ε/[2(1 + ε)];
  - the Open list's "a cuscuton-type form is being tested, T-I15c".

### 2. What HKT needs, and where CO stands now
Reading I15 §3.5, updated for ε = 0.

| hypothesis | status |
|---|---|
| H0, path independence (PI-strong) | **the one principle missing**; imposed in the carrier (Runs 85–91, 101) |
| H1, only the 3-metric | **met by ruling** (30 October: the medium is a slicing condition, N the lapse of a maximal-type slicing). Not derived: I15 §5's tension (P a primitive count, a lapse slicing-dependent, R2 still N = P/P∞) and R2's stationary restriction (I15 choice 3) are open |
| H2, spatial diffeomorphisms | met by the primitive "sliding places costs nothing" (Run 86); D ≈ 0 must also hold on the initial data |
| H3, locality | met in the continuum; the lattice needs a non-ultralocal dressing at order a² (Runs 88–89) |
| H4, quadratic kinetic term | met in the continuum (Run 87) |
| H7, kinetic term ultralocal in the metric (Farkas–Martinec iv) | assumed |
| signature s = +1 | met (the carrier's waves; the one-way order) |
| universal, non-derivative matter coupling | candidate (M1; K101y found no joint closure with Run 91's gravity held fixed; Run 102 found one with gravity free) |
| three dimensions | assumed |

**Under H0 and these conditions** (HKT; a restatement):
$$
H=\frac{16\pi G}{\sqrt g}\Big(\pi^{ij}\pi_{ij}-\tfrac12\pi^2\Big)-\frac{\sqrt g}{16\pi G}(R-2\Lambda),\qquad D_i=-2g_{ij}\nabla_k\pi^{jk},
$$
with G and Λ free. R9 is its static part. I15 §8's count: seven borrowed entries are replaced by one added principle and at least five conditions.

### 3. Why PI-strong does not yet follow from commitment (I15 §4.2)
1. **Kinematics is not dynamics.** "Time at a place is the count of commitments there" says what time is. It does not say the rule making new commitments ignores the order of spacelike-separated ones. In causal set theory this is a separate axiom, discrete general covariance (DGC; Rideout and Sorkin 1999).
2. **The exclusive reading** ("and no other time") is not in the primitives. The record still uses a global order in T1's "at once" and R2's "summed over ticks".
3. **The continuum.** DGC reaches HKT's H0 only if the order of commitments approximates a Lorentzian manifold. Reading I14 found that open (manifoldlikeness).

### 4. The discrete test, as it stands
**DGC** (discrete general covariance, the discrete form of PI) for a growth rule says every natural relabelling of a history has the same probability, Pr(C) = Pr(σC). A **sufficient** condition at the level of unit histories, for two unrelated consecutive births a and b from state s, which take disjoint units (so s+a+b = s+b+a):
$$
\frac{w_a(s)}{Z(s)}\cdot\frac{w_b(s{+}a)}{Z(s{+}a)}\;=\;\frac{w_b(s)}{Z(s)}\cdot\frac{w_a(s{+}b)}{Z(s{+}b)} .
$$

| rule | (2,2,3) | (3,2,3) | status |
|---|---|---|---|
| C7: H units uniform from all units (I14) | 0 / 92 | 0 / 3744 | passes at every size (I15 §4.3, proof sketch checked) |
| W1: holdings-weighted draw, sequential without replacement (I15's pilot) | 8 / 92, worst gap 0.50 | 972 / 3744, worst 0.59 | fails |
| W1, subset weight ∝ sum or ∝ product | 8 / 92 (0.25; 0.46) | 972 / 3744 | fails |
| W2 (one reading): seed unit uniform; the other H − 1 drawn by holdings from units held by elements comparable to the seed's holder | 0 / 40 | 0 / 558 | passes here; unregistered |
| W3 (one reading): jump chain, holder i commits next with probability h_i/(MH), taking H units uniformly from units held by elements comparable to i | 0 / 40 | 0 / 558 | passes here; unregistered |

The W2 and W3 rows come from the check's exploration (the check's exploratory script). They are not registered. At H = 1 every form passes trivially.

**Why W1 fails** (an inference; a worked case from the check). At (2,2,3), after a first birth c = {u0, u2}, take a = {u1, u3} and b = {u0, u2}, which are unrelated. Then
$$
\Pr(a\text{ then }b)=\tfrac{1}{15}\cdot\tfrac16=\tfrac1{90},\qquad \Pr(b\text{ then }a)=\tfrac13\cdot\tfrac1{15}=\tfrac1{45}.
$$
The total weight changes, from 6 to 8, when a's units move to a holder of H units. Where the two births share a parent holder, the weights change too.

**Why W3 passes where it does** (an inference). Total holdings are conserved (Σh = MH), so the step normalisation is constant, as in C7.

**Rideout and Sorkin** (gr-qc/9904062, from standard accounts, not fetched). Order-only growth with internal temporality, DGC and Bell causality is the classical sequential growth family, with transition probability λ(ϖ, m)/λ(n, 0), where λ(ϖ, m) = Σ_k C(ϖ − m, k − m)t_k. Here ϖ is the precursor set's size and m its number of maximal elements. CO's rules also track units, so this does not apply directly. It shows that DGC lets the weights depend on the state only through coarse order invariants (inference).

### 5. The failable step: T-I15b, specified
**Question.** Does a presence-dependent rule satisfy DGC exactly? Reading R2 (a commitment holds until the summed presence reaches a fixed amount) as a choice of units, or as a timing, is itself a **reading**.

**Family, to be fixed in code and archived before hashing:**
- **C7** (control, passes).
- **W1-seq** (control, known to fail).
- **W2:** seed unit uniform over all units. The other H − 1 are drawn sequentially without replacement, weighted by holdings, from units whose holder is comparable to the seed's holder (the seed holder included). If there are fewer than H − 1 such units, the history is excluded and the exclusion counted.
- **W3:** a jump chain. Holder i commits next with probability h_i/Σh, and takes H units uniformly from units held by elements comparable to i (i included). With too few units, the same rule as W2.
- **W4** (the timing form): each holder carries an accumulated presence that grows by its holdings per stage. The holder that first reaches the fixed amount commits, with ties broken uniformly, and takes H units uniformly from its comparable set. This is the only deterministic-timing form; its random elements are the ties and the draw.

**Cases:** (2,2,3), (2,2,4), (3,2,3), (3,2,4), (2,3,3), (2,2,5), with (2,1,5) as a trivial control. Exact rational enumeration. Minutes to an hour of CPU (the largest case is (2,2,5)); (3,3,5), about 4×10⁹ histories, is excluded.

**Kill rule.**
- A rule passes only with zero violations in every case.
- **A pass** means PI-strong is compatible with that reading of R2 at these sizes. The continuum gap (I14) stays open.
- **If W2, W3 and W4 all fail,** the record reads "R2's presence-dependence picks a slicing in every tested form", and PI-strong would need R2 amended (a new statement).

**Disclosed.** W1 fails (the pilot), and one reading each of W2 and W3 passes at (2,2,3) and (3,2,3) (the check's exploration). The larger cases and W4 have not been computed.

### 6. Finding
- R9 is exactly GR's static sector at ε = 0, and its φ choice is moot (restatement; bookkeeping undone).
- Under the ε = 0 ruling, HKT's H1 is met by ruling. The borrowed spacetime cluster then rests on one missing principle, PI-strong, plus at least five technical conditions (restatement of I15, updated).
- At the discrete level, whether commitment implies PI-strong is a question about DGC for presence-dependent rules.
  - A holdings-weighted draw fails.
  - Local forms whose total weight is conserved pass at small sizes (exploration, unregistered).
- The continuum step (manifoldlikeness) stays open in the literature.

### 7. Choices for a ruling
1. **Bookkeeping:** amend R9's note, R3's β line and the Open list's T-I15c entry in ONTOLOGY.
2. **Choice 1 of I15 (reopened):**
   - (a) adopt PI-strong as an added principle now;
   - (b) run T-I15b first, since it decides whether (a) forces R2 to change;
   - (c) keep the cluster borrowed.

   I15 choices 3 (R2's wording) and 4 (T1's foliation) remain open beside it.
3. **T-I15b:** register §5 (registration, one pre-check, one post-run check, since its outcome is unknown and would change a ruling), or park it.

### Sources
- S. A. Hojman, K. Kuchař and C. Teitelboim, Ann. Phys. 96, 88 (1976), via Reading I15's secondary sources: Farkas and Martinec, [arXiv:1002.4449](https://arxiv.org/abs/1002.4449); Anderson, [gr-qc/0511070](https://arxiv.org/abs/gr-qc/0511070).
- D. P. Rideout and R. D. Sorkin, [gr-qc/9904062](https://arxiv.org/abs/gr-qc/9904062).
- The record: ONTOLOGY R2, R9 and the ε note; `gravity/reading_I15_borrowed_inputs.md` §3–§5, §8–§9 and its rulings; `gravity/run66_section.md`; Runs 85–91, 101–102; Reading I14.

### Ruling (30 October 2026)

Allen: "do as you recommend."
1. **Bookkeeping done:** R9's note, R3's β line and the Open list are amended in ONTOLOGY.
2. **Choice 1 (PI-strong):** run T-I15b first.
3. **T-I15b is to be registered** as §5 specifies, with one pre-check and one post-run check.

*Note, 31 October (T-I15b and its pre-check): §4's W2 and W3 rows, and §6's "local forms whose total weight is conserved pass", give an incomplete reason. From an initial antichain, a pool limited to elements comparable to one holder never joins two initial elements, so every draw is forced and the pass is inert. With pools that can join unrelated elements (W5, W6), DGC fails: the subset normalisation changes with the order of spacelike births. T-I15b reads ALL FAIL in the tested forms; only C7's global uniform draw passes non-inertly (`test_I15b_section.md`).*

**Ruling (31 October, after T-I15b; Allen: "do as you recommend").** PI-weak (I15 choice 1(ii)). R9 and the spacetime cluster stay borrowed. Deriving them would need PI-strong, and with it an amended R2 that passes DGC: a new statement not made.
