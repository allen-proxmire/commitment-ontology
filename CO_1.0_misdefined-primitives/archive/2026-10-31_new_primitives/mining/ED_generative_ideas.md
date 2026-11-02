# ED Generative: ideas that could give CO a genuine output

Scope: PAPERS_INDEX.md, REVIEW_2026-09-12.md, physics-papers/, primitives/, Attempt_C/, Derivation Attempts/, Public_repo_archive/. Ten papers or notes read in full or in their load-bearing sections. One check was computed (p-rule signalling and norm conservation, below).

## Top 5, ranked by (genuine output potential) × (survives scrutiny)

### 1. Born rule: conserved hops plus no-signalling on records, which replaces Q6
**Source:** `Derivation Attempts/ED_Attempt_02/Gleason_For_ED.md` (checks G1–G4). ED's published route is weaker and should not be used (see the rejected list).
**Assumed:** complex amplitudes; a linear transport that mixes places nontrivially and conserves an additive amount; outcomes are records; no signalling between separated records.
**Out:** two steps.
- (i) The conserved amount must be Σ|a|². By Aaronson (quant-ph/0401062; Banach–Lamperti), the only linear isometries of ℓ_p for p ≠ 2 are generalized permutations. Mixing hops can therefore conserve only the 2-norm.
- (ii) For a shared pattern Σ c_ij |i⟩|j⟩, a p-rule P ∝ |amplitude|^p lets A's coarse-graining move B's marginal unless p = 2. More generally, once P depends only on the projection (non-contextual), additivity gives g(x+y) = g(x) + g(y) with g ≥ 0, so g is linear and P = ‖Πψ‖².
**Check (computed):** on a random 3×2 state, B's marginal under fine versus grouped A-records is unchanged only at p = 2. At p = 3 it moves 0.230 → 0.201; at p = 4, 0.168 → 0.120. A random 4×4 unitary changes the ℓ1 and ℓ3 norms (2.78 → 2.56; 1.23 → 1.30) and leaves ℓ2 fixed. The derivation goes through. The physics is known (Gleason, Zurek envariance, Masanes–Galley–Müller).
**Gap:** non-contextuality for an isolated pattern.
**Transplant:** CO already has conserved possibility hopping linearly, and the two-place rule keeps S = 2√2 with no signal (Run 95). In CO a pattern commits only when something records it, so every measurement is of a shared system-plus-record pattern. If CO's records are redundant and spatially separated (any copy can be refined independently), no-signalling forces non-contextuality, and Q6 drops out as an added principle. The output is a principle removed, not a number. The statement that must be checked: every CO commitment of a pattern involves a record with a separately refinable part.

### 2. Microcanonical conservation fixes CDT's couplings (a definite, falsifiable point)
**Sources:** `Public_repo_archive/2026-09-27_before_tidy/CDT_Constraint.md`; `Attempt_C/cdt/CDT_Run_Spec.md`.
**Assumed:** spacetime is a foliated CDT triangulation. In 3+1 with χ = 0 the Dehn–Sommerville and foliation identities leave N0, N41, N32 free, for example N1T = 2N0 + N32/2. ED fixes them with a conserved event budget per slice, a conserved spatial-link budget (N41 = 2N3S), and conserved forward links, with N32 = N41 taken from the flat staircase product.
**Out:** a point with nothing tuned: N32/N41 = 1, N0/N4 = 0.044 in 3+1, and τ = N22/N3 = 1/3 in 2+1.
**Status:** genuinely tested, and it fails in 3+1. With a corrected Metropolis–Hastings sampler that reproduces both published calibrations (N0/N4 = 0.158 against 0.152–0.164; N32/N41 = 1.24–1.265 against 1.2625), CDT's N0/N4 is never below 0.073 over the region scanned, against the 0.044 needed. The 2+1 point lies inside the extended phase, which only shows it is "not pathological". N32 = N41 is a modelling choice, not a conservation law.
**Transplant:** this mechanism type is the most direct answer to CO's Dilworth width bound. Geometry comes from the ensemble of foliated triangulations, where phase C is extended and four-dimensional, not from unit growth. CO's foliation (a count of commitments per place) and its conserved possibility would fix N0 and N1T. The output would be a CO-specific N0/N4 or N32/N41, checkable with the sampler that already exists. Costs: CDT's ensemble is borrowed, and fixing the counts is microcanonical, not a choice of couplings.

### 3. Phase deposited at commitment gives a finite coherence reach with no ordering transition
**Sources:** `physics-papers/substrate-evaluation/Paper_PhaseCoherence_P12Coh.md` (read its 2026-09-06 correction: the measured term is Grad, not Coh); `Attempt_C/Polarity_Phase_Consequence.md` (Allen's provisional "the polarity phase is attached to the commitment").
**Assumed:** an alignment reward Coh = |Σ_a P_a|² − Σ_a|P_a|² = 2Σ_{a<b} √(b_a b_b) cos Δπ_ab with P = √b e^{iπ}; quenched disorder in the connection; irreversible one-shot deposition.
**Out (measured, 2D and 3D, ten seeds):** a trivial connection crystallizes. A disordered connection gives finite-reach order, because the holonomy along growth paths is a random walk, roughly independent of dimension. ξ is value-inherited, set by the disorder variance. Canonical Coh does not reproduce the finite reach.
**Transplant:** CO currently borrows "amplitudes with phases". A U(1) phase set at each commitment, carried along possibility hops, makes the phase CO-native. The coherence length ξ would then be a function of commitment statistics, a possible route to r_C or p_c, if the disorder can be tied to CO's own count fluctuations and not inserted. Moderate potential; it is unshown that the variance is CO-internal.

### 4. Three dimensions from held linking
**Sources:** `physics-papers/qft/Paper_MS-II_MatterSectorFromTheArrow.md` §7; `essays/ED_Essay_5_ThreeForcesThreeDimensions.md`.
**Topology:** correct but standard. S^p and S^q link in R^n only when p + q = n − 1, so two closed curves link only in n = 3.
**Weakness:** the premise does the selecting. In 4D a curve links a 2-surface, so "records are held by linking of 1-curves" picks the answer. The "measured" probe illustrates a known fact.
**Transplant:** CO's matter is commitment that keeps remaking itself. If persistent matter is a closed 1-cycle of commitments in space and persistence requires topological protection against the hops, d = 3 follows. This is testable on the CO engine (loop lifetimes on d = 3 versus d = 4 lattices), but the premise has to be argued from CO, not chosen.

### 5. a₀ ~ cH from matching horizon temperatures
**Sources:** `physics-papers/gravity/Note_a0_TwoPi_FormQuestion_2026-09-09.md`; review.
**Out:** Unruh T = a/2πc set equal to the de Sitter temperature H/2π gives a = cH. The 2π survives only by mixing per-radian and per-turn (T = κ/2π on one side only). This yields a dimensionless ratio, not a scale, and H₀ goes in. a₀/cH₀ observed is about 0.18. 1/2π gives 0.87–0.94 of the fitted value, and k = 1 is off by about ×6. This is Milgrom's known coincidence.
**Transplant:** low. A ratio tying a CO crossover to H is possible but would restate the same coincidence.

## Rejected (the answer is inserted, restated, or fails)

- **Paper_003 Born** (`qm-kinematics/Paper_003_BornRule.md`): inserts the answer twice, through P = √b e^{iπ} and through P-LinRate (Pr ∝ b), which the paper concedes.
- **Quantum-Logic Keystone** (`substrate-evaluation/Paper_QuantumLogicKeystone_GleasonReconstruction.md`): "one substrate context" makes non-contextuality vacuous. Gleason needs a frame function over all bases, so it constrains nothing. ℂ is selected, not derived.
- **MS-II §6, "no SU(N ≥ 4)"**: N ≤ d mutually orthogonal vectors in ℂ^d is a tautology, and d = 3 is read from the data. U(N) from norm-preserving transport is textbook. {1,2,3} gives three abelian factors, and the Standard Model has one. "No chiral abelian force" is already contradicted by hypercharge.
- **CleanSubstrateVector**: correct but trivial. With B = SAS⁻¹, det(H(k) − E) is even in k, so the winding vanishes. Useful as a negative for CO: symmetric hops cannot give chirality without breaking parity.
- **Metric-from-graph, "forced to 3D"** (`gravity/Paper_MetricFromTheGraph_ForcedTo3D.md`): the lattice and its dimension are input. "3D reproduces g ~ 1/b" matches a target built in 3D, and GR-I's metric gives PPN β = 0 (review).
- **P12 Σ and the V5 kernel**: labels for a functional and a kernel. No form is forced.
- **Λ** (`gravity/Paper_038_5`): value inherited; the naive estimate is off by about 10⁶⁰.
- **Paper_075** (D = 3+1 from chosen PDE axioms) and **T3 anyons**: textbook.
- **Attempt_B B-16/B-17**: space supplied; no geometry produced.

## Meta-finding
`Derivation Attempts/ED_Attempt_02/Shape_Of_The_Hole.md` states the useful lesson. Universality makes almost any substrate roll into known physics, so agreement there is cheap. Genuine outputs can only be counts, numbers, or no-go points. That is why candidate 2, which produced a definite and failable number, is worth more than most of the corpus, even though it failed.

## Recommended next steps
1. Write the Born replacement for Q6 in CO terms. Prove or refute that every CO pattern commitment involves a record with a separately refinable part. If it holds, Q6 moves from "added" to "derived from no-signalling".
2. Specify CO's conserved counts as CDT constraints (N0 from commitments per slice, N1T from possibility hops) and compute the implied N0/N4 and N32/N41. Pre-register against the corrected sampler's 3+1 values (N0/N4 ≥ 0.073 over the scanned region).
3. Test whether a commitment-borne U(1) phase gives a coherence length set by CO's own count fluctuations. If ξ needs an outside variance, close the route.
4. Leave linking-to-3D and a₀ ~ cH unpursued unless a CO-internal premise appears.
