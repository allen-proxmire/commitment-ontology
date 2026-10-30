## Reading I15: what the borrowed inputs have in common

*29 October 2026. Revised after an independent check (`checkI15/REPORT.md`), whose corrections are adopted; the pre-check version is `reading_I15_v1_precheck.md`. Written in answer to Allen's question: "maybe we should analyze what we had to borrow, like maybe it all points to a missing primitive. one or so new assumptions that fill in the gaps across the board." A reading of the record and of the canonical-gravity literature, plus one small exact enumeration (not registered; §4.3). It encodes no new rule. Statements marked **new statement** would need a ruling. Statements marked **inference** go one step past what the record or a source says and should be checked independently before anything is built on them.*

**In plain terms.** Most of what CO borrows from established physics is one thing in different places: the symmetry of special relativity, and GR's way of curving space. A known result from 1976 derives both from one requirement plus a few technical conditions: evolving the world from one moment to a later one must give the same result however "moment" is sliced through space, which is CO's "no global now", so one added principle could replace about seven borrowed entries. The principle does not follow from CO's definition of time as a local count; it is a new statement that the definition makes natural, and the gravity calculations of Runs 85–91 and 101 already impose it. Several standing rules use a preferred slicing that it would forbid or restrict, and adopting it, together with the requirement that all matter couple only to the metric and that the medium have no dynamics of its own, would most likely remove CO's own departures from GR, which all come from the medium's scale p_s. It leaves the Born rule, the particle masses, three dimensions, the value of Λ and route (b)'s scales outside, and no single further principle is found that covers them. A cheap check is proposed that could show the principle and CO's present static rules to be incompatible: whether any generally covariant theory reproduces CO's static exterior, which changes only the clock rate. A worry raised in the draft, that CO's ζ₂ already breaks the principle, turned out to rest on an out-of-date entry: under the ruled R5, ζ₂ = 0 (now corrected in the record).

**Earlier statements of the hypothesis.** Run 34's 19 October ruling already asks for "one CO rule that makes physics independent of the lattice's rest frame. It would replace this input and Run 18's together", and Note H §4 proposes "one input" for the Lorentz cluster. This reading tests that hypothesis against the literature; it does not originate it.

### 1. Why

- **Allen's request:** find what the borrowed inputs have in common, and whether "one or so new assumptions" fill the gaps.
- **The hypothesis tested here** (as posed): one principle, **path independence**, or no global "now":

  > *the commitment history is the same however it is sliced; only local counts exist,*

  would give the hypersurface-deformation algebra through Hojman, Kuchař and Teitelboim (1976). From the algebra would come the boost relation (Run 101), Lorentz invariance of local physics (parts of R7 and R8) and, given HKT's extra conditions, GR's dynamics (R9, option 3).
- **Tasks:** (1) list every input, grouped; (2) state the theorem's hypotheses and check which ones CO meets; (3) ask whether the principle follows from CO's definition of time; (4) find every preferred slicing in CO; (5) say what stays outside; (6) grade the result and propose a next step that could fail.

### 2. Every input marked added or borrowed

Sources: `ONTOLOGY.md` (rules and the Inputs table); `record/ONTOLOGY_full.md` ("Inputs, in one list"); `record/RULINGS.md`; `RESULTS.md`. The last column is this reading's assessment (§3–§6) of what path independence (PI), with HKT's conditions, would do to each input:
- **covers:** the input would follow from PI plus HKT's conditions;
- **constrains:** PI restricts the input's form or reading;
- **conflicts:** PI forbids the input as stated;
- **outside:** PI says nothing about it.

**A. Principles added to the primitives**

| input | source | kind | what it buys | under PI |
|---|---|---|---|---|
| the vacuum never commits | 15 Oct, Run 14 | added | unscreened field; the arrow lives in matter | outside |
| clocks are matter | 15 Oct | added | redshift, with R2 | outside |
| no infinities | 24 Oct | added | finite counts; no infinite density | outside (compatible) |
| three dimensions of space | primitives | assumed | the lattice | outside (§7) |
| position only at places; places finite per region, no fixed spacing | Reading I13 ruling 3 | added | the scaleless substrate; the lattice a stand-in | compatible; needed for the discrete form of PI (§4) |
| a commitment is stamped with the local count | 26 Oct (Note I) | added | position-like channels | supports PI (§4) |

**B. Gravity rules added**

| input | source | kind | what it buys | under PI |
|---|---|---|---|---|
| R1 outflow f(P) = c ln(1 + P/p_s) | 18 Oct | added, provisional | β = 1 (designed), wells multiply | constrains: p_s's departures from GR (§6) |
| R2 presence clock N = P/P∞, hold summed "over ticks" | 18 Oct | added, provisional | redshift | constrains: valid as the Killing lapse in stationary fields; a preferred time otherwise (§5) |
| R4 the clock field fixed afresh each tick; patterns ride the flow; the tick is not physical time | 19 Oct | added | a moving body keeps its well; no flow-frame effect at 1PN | constrains: allowed as a slicing condition with no slicing-dependent observables (§5) |
| R5 variational draw d = T(1 + g); a pattern's energy draws; hydrostatic balance N h = μ̃ | 19–20 Oct | added | first law; passive = active mass | constrains: PI with an action requires ζ₂ = 0 (§6) |
| R5 the undisturbed vacuum draws nothing; Λ from data | 24 Oct | added | no vacuum-energy problem | compatible; HKT leaves Λ free (§3.3) |
| R6 pattern rule (c = N², γ = 1); massive form −N⁴∇²ψ + m²N²ψ = ω²ψ | 17, 20 Oct | added, provisional | γ = 1; quantum matter falls as in GR | covers in the static limit (universal cone, §3.4) |
| R8 point particles, action −m∫dτ | 20 Oct | added | orbits | covers (geodesic motion of a covariant theory) |
| R8 relations shear, only the shear radiates | Run 11b | added (reading fixed in advance) | binary-pulsar loss | covers, if the gravitational variables are the metric only (two modes) |
| R9 φ's stress, not U's, curves γ̃ | Run 66 | added | β − 1 = −ε/[2(1 + ε)] | conflicts under HKT's conditions: GR exactly means U's stress, β = 1 (§6) |
| R10 reading Z: the medium's clock is the zero-angular-momentum frame's lapse | 21 Oct | added, provisional | Kerr outside spinning holes | constrains: harmless as a statement about stationary solutions (§5) |
| R11 commit where P = 2p_s; core at 3m; holes stable | 19, 21 Oct | added | no singularity, echoes or evaporation | constrains: the commitment surface needs an invariant definition in collapse (§5) |

**C. Borrowed: spacetime symmetry and GR's form (the cluster PI targets)**

| input | source | what it buys | under PI |
|---|---|---|---|
| R7 twist on every closed loop, ticks and relations priced alike ("Lorentz invariance put in by hand") | 17 Oct | composite free fall (MICROSCOPE); knot inertia = energy | covers the Lorentz part. Universal coupling to one metric is a separate condition (Teitelboim's, §3.4) |
| R8 the Lorentz input: a moving body's field is its boosted rest field | 19 Oct | α₁ = α₃ = 0; frame dragging (Run 34) | covers |
| R5 stress pulls with weight 1 per direction (the Lorentz input, full form) | 19 Oct | binding pulls like rest mass (Runs 42, 44); ζ₃, ζ₄ open (Run 34) | covers |
| R8 inertia = total energy | 20 Oct | a compact body's inertia (Runs 52, 55) | covers (von Laue: in a covariant theory (E, P) of a closed static system is a four-vector; Run 55 §6) |
| R9 option 3, binding tension curves space in GR's form | 21 Oct | static stars and holes as GR's | covers, with HKT's conditions |
| R11 option A, GR's exterior for mergers | 19–20 Oct | inspirals and mergers | covers, with HKT's conditions |
| GR's constraint algebra and the boost relation {H[1], H[xᵃ]} = D[e_a], imposed on the carrier | Runs 85–91, 101 ("imposed, not derived": `RESULTS.md`, `ONTOLOGY_full.md`); borrowed per Run 101, and missing from the inputs tables of `ONTOLOGY.md` and `ONTOLOGY_full.md`, so added here | relativistic gravitational waves (Run 90); relativistic matter (Run 101) | covers: this is the algebra PI yields |

**D. Borrowed: matter and quantum content**

| input | source | what it buys | under PI |
|---|---|---|---|
| particle masses, charges, nuclear equations of state | borrowed | stars, neutron stars | outside |
| the Born rule (A5: amplitudes √P with phases, Born weights) | Q5; Reading I3 A5 | outcome weights | outside (§7) |
| the singlet (two-part patterns from ordinary entangling evolution) | Q5; Reading I3 ruling 8 | entangled pairs | outside (an interaction input, not a gap in principle) |
| route (a)'s standard coherence kernel | Reading I1 | which-path records | outside |

**E. Quantum rules added**

| input | source | what it buys | under PI |
|---|---|---|---|
| Q1 draw only through records; renewal carries no stamp; medium holds no branches; phase turned by the time-averaged count | 26–27 Oct | gravity from records; no gravitational entanglement | compatible (the averaging window is read in local proper time) |
| Q2 matter and pattern are states; deposits at the Born outcome, as an impulse with no reaction partner | Reading I6 | interior gravity via route (b) | outside; an impulse with no reaction partner breaks momentum conservation, which PI with an action does not allow (an **inference**, §6) |
| Q3 route (a); interstellar gas is committed matter | Readings I1, Run 93 | records by interaction | compatible |
| Q4 route (b): rate κ_b mc²/(γħ) along the worldline (an operator); GRW-type symmetrisation; units electrons and nucleons; deposits smeared at √1.5 r_C; κ_b = 1/(aP∞) by definition; r_C primitive | Readings I4–I6 | the window (Run 96) | constrains: the rate is invariant; the localisation is defined on a slice (§5) |
| Q5 (T1): one part's commitment updates the whole pattern "at once" in the engine's foliation; the distant part gets no record | Reading I3 | Bell's correlations, no signal | constrains: allowed only while no observable depends on the foliation (§5) |
| route (c), saturation (a capacity per place; a primitive to be written out and tested, RULINGS 28 Oct) | Readings I8–I10 | a size onset | outside; its density ρ̂ is "a density in the foliation" (Reading I8), §5 |

**F. Scales and constants**

| input | kind | under PI |
|---|---|---|
| p_s ≳ 4×10⁵ (conditional); P∞/p_s ≳ 1.6–1.9×10⁵; P∞ ≳ 6.4×10¹⁰ | from data | under HKT's conditions ε = p_s/P∞ must vanish in gravity (§6) |
| the hop, 10^2.5–10³ ℓ_P | engine | outside |
| r_C (0.09–51 μm), κ_b | bounded by data | outside (form constrained, §5) |
| ρ_K, Γ_K | free / registered | outside |
| G, c, ħ, Λ | measured | G and Λ are exactly HKT's two free constants (§3.3) |

The primitives themselves, R6's massive-pattern draw d = κ(4ω²N⁻⁴ − 2m²N⁻²)ψ², and the inputs not yet used by any run (the One Being, the ripples' size) are also listed in `ONTOLOGY_full.md`; this reading starts from the added principles and does not re-grade them.

**G. Engine choices** (not claims about nature): the cubic lattice and one global hop rate; Note H's carrier (Kuhn lattice, Regge's energy, the dressings and lapse couplings of Runs 84–91). Under PI the global hop rate is a stand-in by declaration (R4: "the engine's tick is not physical time").

**What the grouping shows.** Group C is one cluster: every entry is either Lorentz invariance (R7, R8, R5's stress weight, inertia = energy, the boost relation) or GR's dynamics (option 3, option A). Groups D and F are matter content and scales, and they have nothing in common with group C.

### 3. The principle and the theorem

#### 3.1 Path independence, stated

Kuchař's and Teitelboim's requirement, in Ipek and Caticha's statement of it:

> "if the evolution from an initial instant into a final instant can occur along different paths, then all these paths must lead to the same final values for all dynamical quantities."

The intermediate "instants" are spacelike hypersurfaces, and the condition is that "the deformed surfaces remain embedded in space-time" (Ipek & Caticha, arXiv:2006.05036, fetched). Anderson calls it HKT's first principle: "embeddability into spacetime" (Anderson, gr-qc/0511070, fetched).

#### 3.2 What it gives: the hypersurface-deformation algebra

The generators of normal deformations (H, smeared with a lapse N) and of tangential deformations (D, smeared with a shift u) must close as the deformations of a hypersurface in spacetime do (Teitelboim 1973). In the record's notation (Runs 85–86):
$$
\{D[u],D[v]\}=D\big[[u,v]\big],\qquad
\{H[N],D[u]\}=-H\big[u\cdot\nabla N\big],\qquad
\{H[N],H[M]\}=s\,D\big[g^{ij}(N\partial_jM-M\partial_jN)\big].
$$
- The structure function g^{ij} in the last bracket is the inverse of the canonical metric, so the algebra is not a Lie algebra. The constraints H ≈ 0, D ≈ 0 must also hold on the initial data (Ipek & Caticha).
- **The signature enters as s.** In the record's sign convention, s = +1 for Lorentzian signature, s = −1 for Euclidean and s = 0 for the degenerate (Carroll-type) case. Only the sign of s survives redefinitions: Bojowald, Brahma, Büyükçam and D'Ambrosio (arXiv:1610.08355, abstract and summary fetched) show that a bracket multiplied by a function β gives back a classical spacetime of signature set by sgn β. **PI alone does not choose s.** The signature is an input: a causal order, or waves at a finite speed, picks s = +1.
- **The boost relation is the case N = 1, M = xᵃ on flat space** (Run 101):
$$
\{H[1],H[x^a]\}=D[e_a]\quad\Longleftrightarrow\quad [K_a,H]=P_a ,
$$
  the Poincaré relation between a boost, the energy and the momentum.

#### 3.3 The HKT theorem: hypotheses

The original paper (S. A. Hojman, K. Kuchař and C. Teitelboim, *Ann. Phys.* 96, 88 (1976)) was not fetched. Its hypotheses are taken from two secondary sources that were fetched, and those sources differ on which hypotheses are assumed and which are derived:

| | hypothesis | Farkas & Martinec (arXiv:1002.4449) | Anderson (gr-qc/0511070) | Gomes & Butterfield (arXiv:2010.16199) |
|---|---|---|---|---|
| H0 | the generators represent the hypersurface-deformation algebra (embeddability, PI) | assumed | "first principle" | assumed ("meshing") |
| H1 | the only canonical variables are the 3-metric g_ij and its momentum π^{ij} (two degrees of freedom per point) | assumed | assumed; called "questionable"; "precludes Brans–Dicke" (the Jordan-frame form) | assumed |
| H2 | D generates spatial diffeomorphisms, D_i = −2g_ij∇_kπ^{jk} | follows if D generates Lie transport | as stated | assumed (eq. 2.7) |
| H3 | locality: "the metric is to be only locally affected by a pure deformation" (ultralocal in the lapse) | assumed (kinematical) | "the remaining assumption is locality" | — |
| H4 | H at most quadratic in π, with no spatial derivatives of π | assumed (relaxable in 3D) | derived from the algebra | polynomial and ultralocal in π assumed; quadratic derived |
| H5 | time reversal (no term odd in π) | "turns out to be redundant" | subsidiary; removed by Kuchař (1974) | — |
| H6 | second-order potential (Lovelock) | — | not required by HKT; Lovelock fixes the potential; uniqueness dimension-dependent | — |
| H7 | the kinetic term is ultralocal in the metric | (iv), assumed: "we do not have any physical motivation" | — | — |

**Conclusion** (both sources): the representation is unique and is GR's,
$$
H=\frac{16\pi G}{\sqrt g}\Big(\pi^{ij}\pi_{ij}-\tfrac12\pi^2\Big)-\frac{\sqrt g}{16\pi G}\,(R-2\Lambda),\qquad D_i=-2\,g_{ij}\nabla_k\pi^{jk},
$$
with two free constants, G and Λ. Euclidean GR is the case s = −1. Farkas and Martinec add that time irreversibility is "the most interesting generalization" and is open. **This matters for CO:** under H0 and H1 the algebra excludes any term linear in π, so PI-strong forbids time-odd averaged gravitational dynamics, consistent with §5 item 1 of `ONTOLOGY_full.md` ("averaged laws cannot tell forward from backward").

#### 3.4 Matter: the universal cone

- **Teitelboim's extra condition.** The matter part of H does not depend on π^{ij}, and the metric enters it undifferentiated (non-derivative coupling; Ipek & Caticha, fetched; Anderson: "the extra postulate that H_gΨ is ultralocal in h_ab").
- **What it gives.** For a scalar pattern,
$$
H_\psi=\tfrac12\Big(\frac{\Pi^2}{\sqrt g}+\sqrt g\,g^{ij}\partial_i\psi\,\partial_j\psi+\sqrt g\,m^2\psi^2\Big),
$$
  and the closure forces matter's cone to be gravity's: ω² = s² + m² on flat space.
- **Run 101 shows the algebra decides this in advance on the lattice** (a restatement). With shared structure functions (its M1), the boost relation gives ω² = ℓu s², "gravity's own speed", and the mass term carries no momentum dependence. A joint closure exists with Run 90's gravity free (K101j); with Run 91's gravity held fixed none was found (K101y).
- **The same result from a different start.** Barbour, Foster and Ó Murchadha, "Relativity without relativity" (*Class. Quantum Grav.* 19, 3217 (2002); gr-qc/0012089, abstract fetched), start from 3-space with 3-coordinate invariance, a local square root and constraint propagation. They get GR and "Einstein causality": a scalar field must have gravity's characteristic speed.
  - Anderson and Barbour (gr-qc/0201092, fetched) restrict this. It covers the bosonic sector only. Fermions are open ("whether this light-cone is indeed universal"), fundamental vectors must be massless, and Brans–Dicke couplings are allowed.

#### 3.5 Which hypotheses CO meets

| | CO's status | meets? |
|---|---|---|
| H0, PI | Not a rule. Imposed on the carrier in Runs 85–91 and 101 ("the algebra is imposed, not derived"). Not satisfied by R2 and R4 as written, or by T1's foliation read as physical (§5) | **lacks** as a principle; imposed in the carrier |
| signature s = +1 | the carrier's waves move at c (Run 84); light's cone from R6; commitments give a one-way order | meets, in the carrier |
| H1, only the 3-metric | the relations' stretch is option 3's γ̃ (Note H), with exactly two TT modes (Run 84). But CO also has the medium P (φ). If P is fixed by the sources each tick (R4), it is not an independent degree of freedom; if it propagates, it is a third | **undecided**: this is the crux (§6) |
| H2, spatial diffeomorphisms | the primitive "sliding places costs nothing" is the content of D ≈ 0; Run 86: {D, D} closes onto the Lie bracket, "forced, not chosen" | meets: the primitive gives invariance under sliding; D ≈ 0 as a constraint also needs it to hold on the initial data (Note H §8) |
| H3, locality | continuum: yes. The lattice needs a non-ultralocal dressing at order a² (Runs 88–89) | meets in the continuum |
| H4, quadratic | Run 87: the kinetic metric's continuum dependence "is forced to be DeWitt's" | meets in the continuum |
| H5, time reversal | not needed (Kuchař 1974) | not required |
| H6, second order, n = 3 | three dimensions assumed | assumed |
| matter coupling | R6 couples patterns to N⁴, N² undifferentiated; M1 (Run 101) is graded a candidate | meets as a candidate |

**So:** CO meets H2 natively, through a primitive. It meets H3, H4 and the signature in the carrier's continuum limit. It lacks H0 as a principle, and H1 is undecided because of the medium. Everything that would turn the borrowed cluster C into an output rests on H0 and H1.

### 4. Does path independence follow from "time at a place is the count of commitments there"?

#### 4.1 The argument for

- The definition makes proper time local and intrinsic: the length of a chain of commitments, as in causal sets (Brightwell–Gregory). It names no global time.
- The record repeatedly denies that a global time is physical:
  - R4: "the engine's tick is not physical time";
  - the 26 October stamp ruling: a commitment's record "is the count at the place where it happens, not a global tick";
  - Reading I3: "Counts at two places run at different rates and carry no global order, so the update's ordering is used but recorded nowhere".
- If only local counts exist, a slicing has no physical status. Then any prediction that depended on the slicing would make the slicing physical, against the premise. So, **if "only local counts exist" is read as exclusive**, every prediction must be independent of the slicing.

#### 4.2 The argument against: three gaps

1. **Kinematics is not dynamics.** The definition says what time *is* at a place. It does not say that the rule generating new commitments ignores the order in which spacelike-separated commitments are taken. In causal set theory exactly this is a separate axiom: Rideout and Sorkin's *discrete general covariance* (DGC) is imposed alongside internal temporality and Bell causality, and does not follow from sequential growth (Rideout & Sorkin, gr-qc/9904062, listing). The engine itself is a counterexample to "follows": it defines time as local counts and still runs on one global hop rate.
2. **The exclusive reading is not in the primitives.** `ONTOLOGY.md` says "Time at a place is the count of commitments there". It does not say "and there is no other time". The record also uses a global ordering in rules that are ruled, not only in the engine: T1's "at once" and R2's "summed over ticks" (§5).
3. **The discrete statement does not give HKT's statement without a continuum.** HKT's H0 is about evolution between spacelike hypersurfaces of a Lorentzian manifold. The discrete form (DGC) reaches it only if the order of commitments approximates a Lorentzian manifold. That is the manifoldlikeness problem that Reading I14 found open in the literature since 1987.

#### 4.3 An exploratory check: does I14's grid-free stand-in satisfy the discrete form?

The discrete form can be tested exactly on the one grid-free rule written down so far: Reading I14's unruled stand-in C7, the hold-rule growth. C7 is not a Rideout–Sorkin sequential growth model (it also tracks units), so DGC is tested on the order marginal of the chain.
- **The rule.** An initial antichain of M elements holds H units each. Each new commitment takes H units uniformly at random from all units. Its parents are the units' holders, the units move to it, and the order is the transitive closure.
- **DGC requires**
$$
\Pr(\text{labelled history }C)=\Pr(\sigma C)\quad\text{for every relabelling }\sigma\text{ that keeps the labelling natural.}
$$
- **The method.** `explore_i15_dgc.py` enumerates every unit choice with rational arithmetic, for up to four births, and compares the probability of every natural relabelling. Log: `explore_i15_dgc.log`.

| rule | cases (M, H, births) | relabellings checked | DGC violations |
|---|---|---|---|
| transitive percolation (control; known to satisfy DGC) | (2, –, 3) at p = ⅓; (1, –, 4) at p = ½ | 1648; 2681 | 0; 0 |
| **hold-rule growth (C7)** | (2,1,4), (2,2,3), (2,2,4), (3,1,4), (3,2,3), (3,2,4), (2,3,3) | 92 to 45,018 per case | **0 in every case** |
| negative control: parent = the most recently born element with probability ½ | (2, –, 3); (2, –, 4) | 148; 1460 | 16; 352 (relative gap 1.0) |

- **Why C7 passes** (an **inference**, a proof sketch, not checked independently):
  - every unit-level history has the same probability, C(MH, H)^(−n);
  - two unrelated births that happen one after the other take disjoint sets of units, since the later cannot take a unit the earlier holds without becoming its child;
  - so swapping them maps a valid unit history to a valid unit history with the same parent sets;
  - so every natural relabelling is a bijection on unit histories, and DGC holds exactly at every size, not only up to four births.
- **What it shows.** The discrete form of PI is satisfied by the simplest grid-free stand-in. The check reproduced every count with an independent code, added the case (2,1,5) (504 relabellings, 0 violations), and tested the swap step directly on every unit history.
- **What it does not show.**
  - It holds because the sampling ignores the state. Reading I14 §8 named that same mean-field property as the likely reason C7 would fail to produce manifold-like orders.
  - A hold weighted by the local possibility present (R2's actual content) makes the transition weights depend on the state. The check's exploratory preview: with each unit drawn with weight equal to its holder's holdings, DGC **fails** at (M, H, n) = (2, 2, 3), 8 of 92 relabellings, worst relative gap 0.5. This is a pilot, to be disclosed if T-I15b is registered.
  - Reading I14's finite-valency result rules out a Lorentz-invariant sprinkling, so C7 passing DGC does not carry over to HKT's continuum H0 (§4.2, gap 3).

#### 4.4 Grade

**New statement, motivated.** PI is not derived from the definition of time. It is the natural strengthening of four standing statements (the definition, R4's disclaimer, the local stamp, and Reading I3's "recorded nowhere"). At the discrete level it is consistent with CO's only grid-free rule (§4.3), and CO's primitive "sliding places costs nothing" already supplies its spatial half (H2). Getting from the discrete form to HKT's continuum form needs manifoldlikeness, which is open.

Two forms are worth separating for a ruling:
- **PI-weak:** no observable depends on a slicing; records carry only local counts. This is close to what the record already says.
- **PI-strong:** the dynamics, and not only its observables, is slicing-free; in the continuum, H0. HKT needs PI-strong.

### 5. Every preferred slicing in CO, and whether PI forbids it

| item | where | what it slices by | verdict under PI |
|---|---|---|---|
| **R2**, the hold summed "over ticks"; N = P/P∞ as a rate per tick | ONTOLOGY R2; ONTOLOGY_full R2, ∑_ticks(P_a + P_b) ≥ 2ħ_tP∞ | the engine's ticks: dτ = N dt with t global | **Harmless in stationary fields, conflicting otherwise.** In GR the lapse is not a scalar: it depends on the slicing. In a static spacetime the static lapse is the norm of the timelike Killing field, N = √(−ξ·ξ), which is invariant. That is where Runs 22, 65 and 67 use N. Without a Killing field, "the clock rate relative to infinity" has no invariant meaning. Identifying N with a function of a local count P then picks a time function. That is khronometric structure, which PI-strong forbids. Under PI, R2 must be read as the stationary statement, with dynamics open |
| **R4**, the field fixed afresh each tick | ONTOLOGY R4; Run 34 | elliptic equation on engine slices; the lattice frame "taken as the PPN preferred frame" | **Harmless as a slicing condition, open beyond 1PN.** GR's potentials obey Poisson-type equations in its constraint structure (ONTOLOGY_full §5, item 1; Flanagan & Hughes). Note H §8 reads CO's medium energy as "the counterpart of GR's lapse equation in maximal slicing". A slicing condition is allowed under PI only if no observable depends on it. Run 34 shows α₂ = ζ₁ = ξ = 0 given R8's borrowed boost, and "signalling through the constraint" is untested beyond 1PN (Run 34; Open) |
| **R4 / R8**, patterns ride the flow, g₀ᵢ = −uᵢ | Run 34 | the medium's flow as a frame | **Harmless if the flow is a field's state** (like a fluid's rest frame), not a structure of the laws. In GR the shift is gauge. CO makes it physical, and Run 34 derives k₂ = ½ from conservation "in the slicing where part 1 holds" |
| **R10**, reading Z: the medium's clock is the ZAMO lapse | ONTOLOGY_full R10 | zero-angular-momentum observers, the normals to the t = const slices of a stationary axisymmetric spacetime | **Harmless as a statement about stationary solutions**; conflicting if read as a fundamental medium frame |
| **R11**, commit where P = 2p_s | R11; Runs 71, 73–74 | "where the clock has fallen to 2ε" | **Constrains.** In a static field this is a level set of the Killing norm and is invariant. In collapse it needs a slicing-free definition, for example a local count, if P per place is a scalar density of places |
| **R6**, hops on the place's ticks; coordinate speed N² | R6 | the static frame | harmless (static) |
| **T1** (Q5), the update "at once" in the engine's foliation | Reading I3 rulings 1, 4 | a global simultaneity, "recorded nowhere" | **Compatible with PI-weak, conflicting with PI-strong.** The Bell statistics do not depend on the foliation (Reading I3 §4). Its status is that of the preferred foliation in a pilot-wave theory: it is used and not observable |
| **Q4**, route (b)'s rate | Reading I6 ruling 11 (28 Oct) | along the worldline: κ_b mc²/ħ per unit proper time | **harmless (invariant).** The task's "route (b)'s rate in the cosmic frame" was M2, replaced on 28 October by the worldline reading |
| **Q4**, route (b)'s localisation L(x) and deposit smearing at √1.5 r_C; GRW-type symmetrisation | ONTOLOGY Q4 | a Gaussian on a slice (nonrelativistic GRW) | **Conflicts under PI-strong** unless rewritten in a relativistic collapse form. Reading I3 notes that Tumulka's relativistic GRW (2006) "covers only non-interacting distinguishable particles" |
| **Run 96**, relic-neutrino kicks "applied in the cosmic frame" | Run 96, B16-NR | the CMB frame | a modelling choice for a state of matter. Harmless as a frame of the matter. Under PI-strong the heating would need recomputing in a covariant form |
| **route (c)**, ρ̂ "a density in the foliation, the same preferred frame as M2's rate" | Reading I8 C4-β | the foliation | conflicts under PI-strong (a candidate only) |
| **Reading I13**, a momentum cap \|p\| ≤ πħ/ℓ "in the foliation's frame" | Reading I13 §2 | the foliation | conflicts (noted there as not boost-invariant; not ruled as CO's) |
| **The One Being**, first commitments "at virtually the same moment at every place" | stated 23 Oct | a global moment | **Harmless if read as an initial antichain** (Reading I14 C6): a set of mutually unrelated commitments, which needs no slicing |
| **The khronometric route** | Note H §8 (after the earlier papers' GR-II) | a preferred foliation, made dynamical | **Excluded by PI.** It was never adopted; Runs 85–91 found GR's route surviving, so the fallback was not triggered |
| **The engine's global hop rate** | engine table | a global tick | harmless by declaration ("not claims about nature") |

**Is the principle already effectively adopted? In the carrier, yes; in the rules, no; and N has two roles.**
- **Runs 85–91 and 101 impose the hypersurface-deformation algebra itself.** They close {H[N], H[M]}, {H[N], D[u]} and {D[u], D[v]} with N and M *arbitrary smearing functions*. The lapse is a Lagrange multiplier there: any slicing is allowed. Run 101 states that relativity for matter "follows from the borrowed boost relation", which is PI's algebra.
- **R2 makes N a physical field,** N = P/P∞, read by clocks.
- **This is not a contradiction.** Closure for arbitrary smearing functions includes any particular slicing condition, such as R4's elliptic one, and Note H §8 already reads the medium's energy as maximal slicing's lapse equation; Note H's GR route is gauge-fixed GR (Bonazzola et al. 2004). **The open tension is ontological:** P is a primitive count per place, while a lapse depends on the slicing. If N = P/P∞ held in every slicing, P could not be a slicing-independent count.

Adopting PI would therefore add little to the carrier calculations, beyond making obligatory the closures not yet shown: field order 3, and the joint closure with Run 91's gravity (Run 102). A failure there would kill the principle. Its content, and its cost, lie in extending it to R2, R4, R10, R11, Q4 and T1. That means reading N as the lapse of a slicing condition, physical only through its slicing-invariant content (redshift between stationary clocks).

### 6. The cost: the medium's scale

**6.1 HKT's H1 decides ε.** CO's departures from GR all come from the medium's scale p_s, through ε = p_s/P∞ (R9: "ε sets every static departure from GR"):
$$
\beta-1=-\frac{\varepsilon}{2(1+\varepsilon)},\qquad \Delta=\frac{\varepsilon C}{1+\varepsilon},\qquad N=(1+\varepsilon)e^{-\varphi}-\varepsilon .
$$
- **If H1 holds, all matter (clocks included) couples only to the metric, and the medium has no dynamics of its own** (N is the lapse of a slicing), HKT gives GR exactly:
  - ε drops out of the metric: β = 1, Δ = 0;
  - R9's choice becomes empty (φ = U at ε = 0);
  - p_s survives only in the clock-agreement and quantum sectors.
  - H1 alone is not enough: a minimally coupled scalar in the Einstein frame that other matter also couples to meets H1 and still departs from GR. CO's clocks read N = P/P∞, so universal coupling is exactly what is in question.
- **If the medium is an independent scalar,** H1 fails and HKT's uniqueness is lost. The theory is then a scalar–tensor theory, which also represents the algebra (Anderson: H1 "precludes Brans–Dicke"). That scalar sector would have to be written covariantly, and R4's instantaneous form would have to become a constraint or a propagating field.
  - The covariant theory with an infinitely fast scalar is the cuscuton, or minimal Hořava gravity. Note H §8 already records it as strongly coupled and probably not viable (Franchini et al. 2021; Jacobson & Pulakkat 2025, as cited there).
  - An **inference**, unchecked: in the common conformally coupled scalar–tensor class (Damour–Esposito-Farèse), γ − 1 = −2α₀²/(1 + α₀²), so γ = 1 forces α₀ = 0 and then β = 1 at 1PN. CO's pair (γ = 1, β ≠ 1) would need a less common covariant scalar sector.
  - *Withdrawn 30 October (T-I15a″ reading, `testI15a/READING_T-I15a.md` §4).* The inference that CO's exterior changes only the lapse, and so needs an aether- or khronon-type completion, was wrong on three counts: the exterior is not lapse-only (Run 67 §1); aether and khronon theories give β = 1; and a lapse-only change does not in general need a timelike vector. **The replacement:** at leading order, among covariant theories with one universally coupled matter metric, ε ≠ 0 needs a ghost, an unusual scalar sector (couplings non-analytic at X = 0, or screened or non-perturbative Horndeski and beyond), or a TeVeS-type vector–disformal coupling; TeVeS itself has the wrong sign of β − 1.

**6.2 ζ₂ under the ruled R5 is zero** (a record correction; reading).
- Run 30's ζ₂ = 2(β − 1) is the value under the draw used before R5 (rule E, d = ρ*N). With R5's d = T(1+g) = −ρ* dN/dφ the static sector is Lagrangian, the Φ₂ coefficient of g₀₀ is 2(4 − 2β), and ζ₂ = 0 for every ε:
$$
g_{00}=-1+2U-\frac{2+\varepsilon}{1+\varepsilon}U^2+\Big(6+\frac{2a}{1+\varepsilon}\Big)\Phi_2,\qquad a=-1\ (\text{R5}),\ \ a=-(1+\varepsilon)\ (\text{rule E}),
$$
  matched to Will's 2(3γ − 2β + 1 + ζ₂ + ξ) with γ = 1, ξ = 0 (checked exactly, `checkI15/check_zeta2.py`, and by hand).
- Run 66's Δ = εC/(1+ε), the current scale input, already corresponds to η_N = 4(β − 1), the fully conservative form. The ζ₂ entries of Runs 30, 34, 45 and 47, `RESULTS.md`, the consilience summary and `ONTOLOGY_full.md`'s R5 line were out of date; dated notes now correct them (29 October).
- An invariant action requires ζ₂ = 0 with or without PI (Will 2014, §3.2), and preferred-frame theories with an action (Einstein–aether, khronometric) also have ζ₂ = 0. So ζ₂ does not distinguish PI from a preferred foliation.
- R5 does not make CO semi-conservative: α₃ and ζ₁ rest on borrowed inputs, and ζ₃ and ζ₄ are still open (Run 34).

**6.3 Q2's impulse "with no reaction partner"** (an **inference**). A deposit that changes a body's momentum with no partner breaks the conservation of total momentum, which an invariant action guarantees. Under PI-strong it would have to be shown to average to zero, or to belong to the quantum sector's stochastic part, which lies outside the classical theorem.

### 7. What stays outside, and whether another single principle covers it

| input | does PI reach it? | candidate principle | grade |
|---|---|---|---|
| **Born rule** | No. No-signalling across T1's foliation constrains probability rules, but only partially (Han & Choi, arXiv:1208.2814, fetched: their own §3.4 admits non-Born power laws for Bell states) | **Unit counting:** each unit of possibility is equally likely to be the one that commits. With P_i ∝ \|ψ_i\|², this gives p_i = P_i/ΣP = \|ψ_i\|². The identification has an argument: under unitary evolution the only conserved positive quadratic form invariant under all unitaries is a multiple of the norm (Schur), and possibility is CO's conserved quantity. It is related to Zurek's envariance argument (Zurek, quant-ph/0405161, listing), though the Schur step is a uniqueness argument for an invariant form, not envariance. (A claimed quantisation of probabilities is dropped: the relevant count is the pattern's total units, which Reading I4 counts in proportion to its energy, and continuous unitary evolution does not keep branch counts whole.) | **restatement**: it moves Born to A5's √P amplitudes plus an indifference assumption  *Superseded 30 October by Reading I16 (noncontextuality, a candidate).* |
| **the singlet** | no | none needed: two-part patterns come from entangling interactions, which are part of matter's content | not a gap in principle |
| **three dimensions** | No. HKT works for any spatial dimension under H4–H6 (Farkas & Martinec); Lovelock's uniqueness is dimension-dependent (Anderson) | grid-free growth (Reading I14, T-I14a), expected to fail | open; no principle |
| **masses, charges, equations of state** | no | none in the record | borrowed |
| **Λ** | Partly. HKT leaves Λ as a free constant beside G, matching R5's "Λ from data" and unimodular gravity | none fixes its value | restatement (why it is free, not what it is) |
| **p_s, P∞, ε** | Yes, negatively. Under H1, ε → 0 in gravity (§6) | — | a cost, not an output |
| **r_C, κ_b** | Form only: route (b) must be relativistic under PI-strong | none fixes the values | outside |

**No single further principle covers this group.** The Born rule's best candidate (unit counting) is a different kind of statement from PI: a symmetry among units, not a statement about slicing. A slogan joins them ("time is a count; probability is a count"), but no derivation does.

### 8. Grade, what would be new, and a next step that could fail

**Grade of the hypothesis.** **Partly right.**
- **Right:** one principle, PI (general covariance in its canonical form), with HKT's technical conditions, covers the whole borrowed cluster C:
  - R7's Lorentz part;
  - R8's Lorentz input and inertia = total energy;
  - R5's stress weight;
  - R9's option 3 and R11's option A;
  - the boost relation of Runs 90 and 101.

  That replaces seven borrowed entries with one added principle and at least five conditions: H1 (no extra gravitational variable), universal non-derivative matter coupling, locality, the signature, and Farkas–Martinec's (iv), with three dimensions also assumed. Composite free fall (R7's MICROSCOPE job) needs the coupling condition as well as PI.
- **Not as hoped:**
  1. PI does not follow from CO's definition of time (§4: a new statement, motivated);
  2. in the carrier it is already imposed, so it gives no new consequences there (§5);
  3. it restricts or forbids several standing rules and readings: R2 outside stationarity, R4 beyond 1PN, R10 as a fundamental frame, R11 in collapse, route (b)'s localisation, T1 under the strong form, route (c), and I13's cap;
  4. under H1 with universal coupling it removes CO's own departures from GR (β − 1, Δ);
  5. it leaves the quantum and matter inputs outside.
- **The "missing primitive" exists for the spacetime cluster, and it is a known one.** CO's specific question is whether commitment can be shown to imply it.

**What would be new versus restatement.**

| claim | grade |
|---|---|
| PI ⇒ the deformation algebra ⇒ GR (HKT 1976; Teitelboim 1973; Kuchař 1974) | restatement |
| PI ⇒ matter shares gravity's cone (Teitelboim; Barbour–Foster–Ó Murchadha); Run 101's lattice result | restatement |
| CO's primitive "sliding places costs nothing" is HKT's H2 | reading |
| CO's grid-free hold rule (I14's C7) satisfies discrete general covariance exactly (§4.3) | new to the record; exploratory, with a proof sketch; small |
| Under PI-strong with universal coupling, CO's ε-departures survive at weak field only with a ghost or an unusual scalar sector (§6.1; T-I15a″ reading) | follows from a derived constraint, checked independently |
| ζ₂ = 0 under R5 (§6.2) | record correction (reading) |
| PI derived from commitment | **not achieved**; the open problem |

**T-I15a″, recorded as a reading (30 October).** Its pre-registration was built and checked; every verdict-bearing output was already fixed by the record and the literature, so it was recorded as a reading instead (`testI15a/READING_T-I15a.md`). Its result replaces §6.1's withdrawn inference. The kill wording "khronometric by construction" is withdrawn: aether and khronon theories give β = 1.

**A cheaper companion: T-I15b, DGC with a state-dependent hold.** Rerun §4.3's exact enumeration with R2's content put back in: a new commitment's units drawn with weight proportional to the possibility its candidate parents hold, or a hold that depends on the local count. Registered prediction: the two-step weight of two unrelated consecutive births does not depend on their order. Kill: any DGC violation means the presence clock, written without a grid, picks a slicing. **Disclosure:** the check's pilot already found a violation for one state-dependent weighting (§4.3), so the registered weighting must be fixed before running and the pilot disclosed.

### 9. Choices for a ruling

1. **The principle.**
   - (i) Adopt PI-strong as an added principle: no global now, for the dynamics as well as the records.
   - (ii) Adopt PI-weak: no observable depends on a slicing; records carry only local counts.
   - (iii) Do not adopt; keep the cluster C borrowed.

   Grade under (i) or (ii): new statement, motivated by the definition of time, the local stamp and R4's disclaimer, not derived from them.
2. **The medium under PI (only if 1(i)).**
   - (i) The medium is a slicing condition: N is the lapse of a maximal-type slicing, physical only in stationary fields. Then HKT gives GR, ε → 0 in gravity, R9's choice goes to U's stress, and Δ and β − 1 leave "where CO differs".
   - (ii) The medium is an independent covariant scalar: a scalar–tensor completion to be written, with HKT's uniqueness lost.
   - (iii) Keep a preferred slicing for the medium (the khronometric class) and decline PI-strong.
3. **R2's wording.** Restrict N = P/P∞ to stationary fields (the Killing norm) and list its non-stationary reading as open, or leave it as is.
4. **T1's foliation.** Record that it is unobservable and so compatible with PI-weak, or require a foliation-free form (relativistic-collapse type), which would also reopen route (b)'s localisation and Run 96's cosmic-frame kicks.
5. **Next test:** T-I15a″ (a covariant completion of the lapse-only exterior, with the kill rule of §8) or T-I15b (state-dependent DGC, pilot disclosed), or park.
6. **§4.3's DGC result.** Record it as exploratory, with its proof sketch sent for an independent check, or leave it in this draft.
7. **The Born rule.** Write out unit counting as a candidate (graded restatement: it moves Born to A5's √P amplitudes), or leave Born borrowed without a candidate.
8. **Bookkeeping.** Done 29 October: ζ₂ = 0 under R5 written back to Runs 30, 34, 45 and 47 and the summaries. Still to do: add the boost relation and GR's constraint algebra to both inputs tables as borrowed, and mark the M2 references in Readings I3 and I8 as superseded by I6 ruling 11.

### Sources

- S. A. Hojman, K. Kuchař and C. Teitelboim, "Geometrodynamics regained", *Ann. Phys. (N.Y.)* 96, 88 (1976). From standard listings, not fetched; hypotheses taken from the two secondary sources below.
- C. Teitelboim, "How commutators of constraints reflect the spacetime structure", *Ann. Phys. (N.Y.)* 79, 542 (1973). From standard listings, not fetched.
- K. Kuchař, "Geometrodynamics regained: a Lagrangian approach", *J. Math. Phys.* 15, 708 (1974): removal of time reversal. Via Anderson; not fetched.
- S. Farkas and E. J. Martinec, "Gravity from the extension of spatial diffeomorphisms", [arXiv:1002.4449](https://arxiv.org/pdf/1002.4449). Fetched; HKT conditions (i)–(iv), time irreversibility, Hořava.
- E. Anderson, "On the recovery of geometrodynamics from two different sets of first principles", [arXiv:gr-qc/0511070](https://arxiv.org/pdf/gr-qc/0511070). Fetched (first 100,000 characters); HKT's and BFO's principles, the two-degree-of-freedom assumption, Lovelock, Teitelboim's matter postulate.
- S. Ipek and A. Caticha, "The entropic dynamics of quantum scalar fields coupled to gravity", [arXiv:2006.05036](https://arxiv.org/pdf/2006.05036). Fetched; the statement of path independence; non-derivative coupling.
- M. Bojowald, S. Brahma, U. Büyükçam and F. D'Ambrosio, "Hypersurface-deformation algebroids and effective space-time models", [arXiv:1610.08355](https://arxiv.org/pdf/1610.08355). Abstract and summary fetched; only sgn β survives.
- J. Barbour, B. Z. Foster and N. Ó Murchadha, "Relativity without relativity", *Class. Quantum Grav.* 19, 3217 (2002); [arXiv:gr-qc/0012089](https://arxiv.org/abs/gr-qc/0012089). Abstract fetched.
- E. Anderson and J. Barbour, "Interacting vector fields in Relativity without Relativity", [arXiv:gr-qc/0201092](https://arxiv.org/abs/gr-qc/0201092). Fetched.
- H. Gomes and J. Butterfield, [arXiv:2010.16199](https://arxiv.org/pdf/2010.16199), §2 on HKT. Fetched by the check.
- C. M. Will, "The confrontation between General Relativity and experiment", *Living Rev. Relativ.* 17, 4 (2014); [arXiv:1403.7377](https://arxiv.org/pdf/1403.7377). Fetched; §3.2, semi-conservative theories.
- D. P. Rideout and R. D. Sorkin, "A classical sequential growth dynamics for causal sets", [arXiv:gr-qc/9904062](https://arxiv.org/abs/gr-qc/9904062). Listing only (DGC as a separate condition, from standard accounts and Reading I14).
- Y. D. Han and T. Choi, "Limits on quantum probability rule by no-signaling principle", [arXiv:1208.2814](https://arxiv.org/abs/1208.2814). Abstract and summary fetched.
- W. H. Zurek, "Probabilities from entanglement, Born's rule from envariance", [arXiv:quant-ph/0405161](https://arxiv.org/pdf/quant-ph/0405161v1). Listing only.
- R. Tumulka, relativistic GRW (2006). Via Reading I3; not fetched.
- The record: `ONTOLOGY.md`; `record/ONTOLOGY_full.md` (R1–R11, §5 item 1, §7, Note H §8 via `gravity/design_shear_waves.md`); `record/RULINGS.md`; `RESULTS.md`; `gravity/run30_section.md`, `run34_section.md`, `run45_section.md`, `run47_section.md`, `run52_section.md`, `run55_section.md`, `run84_section.md`–`run91_section.md`, `run101_section.md`; `quantum/reading_I3_two_place_commitment.md`, `reading_I6_matter_and_pattern.md`, `reading_I8_C4b_statement.md`, `reading_I11_ps_upper_bound.md`, `reading_I13_bounded_ledger.md`; Reading I14 draft (unchecked).

*Files in this folder: `reading_I15_DRAFT.md` (this reading); `explore_i15_dgc.py` and `explore_i15_dgc.log` (§4.3, exploratory, not registered).*

### Rulings (30 October 2026)

Allen: "do as recommended."
1. **Choice 2, the medium under PI: ε is kept provisionally,** pending T-I15c, which asks whether a cuscuton-type theory (an infinitely fast scalar with no waves of its own, P = μ²√(2X) − V(φ)), the natural covariant form of a medium fixed afresh each tick, can carry CO's exterior. If it cannot, the reading recommends ε = 0 in gravity.
2. **Choice 5: T-I15a″ is recorded as a reading** (`reading_I15a_covariant_completion.md`): its verdict-bearing outputs were already fixed by the record and the literature.
3. **§6.2 recorded:** ζ₂ = 0 under R5 (written back to Runs 30, 34, 45 and 47 and the summaries, 29 October).
4. **§7's unit-counting candidate is superseded** by Reading I16 (Q6).

Choices 1, 3, 4 and 6 are left open.

*Note (30 October, Readings I15a and I15b):* the cuscuton route is closed as scoped (I15b). CO's static sector is exactly N√h[R + α(N)aᵢaⁱ] with α(N) = 2[1 − N²/(N+ε)²], which a lapse-dependent field redefinition turns into GR: CO's exterior is GR with matter on a metric depending on the foliation's lapse. A khronometric completion with gravity waves at light speed gives α₁ = −4α∞ ≈ −16ε, so ε ≲ 2.5×10⁻⁶ (P∞/p_s ≳ 4×10⁵) from the pulsar bound Run 34 uses, and it conflicts with R8's borrowed α₁ = α₂ = 0 whenever ε ≠ 0; α₂ vanishes only on a tuned strip. ε stays provisional pending a ruling on that price.

**Ruling (30 October; Allen: "do as you recommend").** CO keeps ε, with a preferred time: choice 1 is (ii), "no global now" for observables (PI-weak), and choice 2 is (iii), the medium keeps a preferred slicing. PI-strong is declined. R8's borrowed boost holds at zeroth order in ε; at first order a khronometric completion predicts α₁ = −4α∞ ≈ −16ε, so ε ≲ 2.5×10⁻⁶ (Run 34's pulsar bound). α₂ vanishes only on a tuned strip, λ ≈ 4ε. The lapse-coupled completion's α₁ and α₂ are to be computed in a registered test.

*Note (30 October, T-I15d):* the price of keeping ε is now computed for the lapse-coupled completion: α₂ ≈ −2ε gives ε ≲ 8×10⁻¹⁰ under the pulsar bound (registered reading EXCLUDED, below the 10⁻⁸ floor), and the two-cone bound gives 1.3×10⁻⁷. At such ε CO's gravity is observationally GR; only interior structure inside holes depends on ε. The ε ruling is open for review.

**Ruling (30 October, after T-I15d; Allen: "do as you recommend").** ε = 0 in gravity, replacing the earlier ruling to keep it. Choice 2 becomes (i): the medium is a slicing condition, and HKT with universal coupling gives GR; R8's borrowed boost is exact. Choice 1 (PI-strong or PI-weak) is reopened, since ε no longer blocks PI-strong. R11's black-hole statements are to be re-read under ε = 0.

*Note (30 October): P∞ ≳ 6.4×10¹⁰ was p_s's bound times the pulsar triple's ratio bound; with ε = 0 in gravity the ratio bound and this figure lapse (Reading I17). What remains is p_s ≳ 4×10⁵ (conditional) and route (b)'s a·P∞ ≳ 2.5–5×10²⁷ (Run 96 with its relic-neutrino addendum). The upper bound p_s ≲ 1.1×10³⁰/a (Reading I11) rested on the same pulsar-triple ratio and lapses too (corrected 30 October after Reading I18's check).*
