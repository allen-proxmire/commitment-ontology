# Event Density corpus mined for Commitment Ontology: candidate ideas

Scope: `/home/claude/allen-proxmire/event-density` (foundations/, theory/, theorems/, arcs/, docs/). Each ED claim below was treated as overclaimed until checked.

## What did not survive (so CO can skip it)

- **Curvature-emergence chain** (`foundations/CurvatureEmergence_MetricFromBandwidth_Foothold.md`, `..._ReachLaw_Derived_Holographic.md`, `..._LengthScale_IsThePlanckGrain.md`). The emergent metric is **true by definition**: with reach r(x) = R0·b(x)^p, the hop count across a span is ≈ ∫dx/(R0·b^p), so the measured exponent q = p by construction. That is why its table shows q tracking p. The "derived" reach law p = 1/(d−1) has three problems:
  - It reads d−1 off the boundary cut of a nearest-neighbour lattice whose dimension d was chosen in advance.
  - It sets b = surface cut, but in the probe's own graph a locus linking everything within R has degree ~R^d (a volume). That gives p = 1/d, which in 3D is p = 1/3 and g ~ b^(−2/3), not 1/b.
  - "Only 3D gives g ~ 1/b" is uniqueness relative to GR-I's assigned metric, which the outside review found gives PPN β = 0.
  
  No dimension or metric comes out that was not put in.
- **3D from linking.** ED's own failed closure (`foundations/ThreeD_ExactlyThree_ClosureAttempt_Failed_2026-07-26.md`) found two problems: the linking number is symmetric and so cannot carry an order, and in 4D a chain can link a membrane. `Gauge_08` gets internal d = 3 by putting in the Standard Model's {1,2,3}.
- **Theorems claimed as forced** (checked one by one):
  - T19, G = c³ℓ_P²/ℏ, is the definition of ℓ_P (ℓ_P² ≡ ℏG/c³); G goes in.
  - T20, a₀ = cH₀/2π = 1.08×10⁻¹⁰ m/s², is Milgrom's 1983 coincidence. ED's own target #18 says the 2π is not forced. With H₀ = 67.4 it gives 1.04×10⁻¹⁰, against 1.2×10⁻¹⁰ observed.
  - T21: v⁴ = GMa₀ is one line of algebra from MOND's deep-limit rule a = √(a_N·a₀).
  - T13 and T16 are Stone's theorem. T15 is the textbook Galilean-algebra result (Lévy-Leblond).
  - T1, T2 and T3 are textbook once D = 3+1 (P06) is assumed.
  - T7 follows trivially from discreteness. T18 builds the arrow in ("no backward chains exist").
  - T10, T11 and T14 are already downgraded in their own files.
  
  **None gives a genuine output.**
- **Round 8 lapse** (`foundations/Phase3_GR_Round8_SignatureAndFactor.md`): a null front with Γ ~ b^α and g ~ 1/b gives g₀₀·g_rr ~ −b^(2(α−1)), so γ = 1 if and only if α = 1. **CO already has this as R6** (hops on the place's own ticks, coordinate speed N²). Nothing new.
- **Black-hole 1/4** (`foundations/BH_EntropyCoefficient_FromEventCounting.md`): Route A borrows b = 1 − r_s/r (Schwarzschild) and T = κ/2π.
- **Commitment as phase annihilation**: retracted by ED itself (`Commitment_As_PhaseAnnihilation_BornResidue_DRAFT_2026-07-27.md`).

## Top 5 for CO, ranked by (output potential) × (survives scrutiny)

### 1. Spectral dimension as a length-free output, tested on a two-kernel arena
Source: `theory/Note_SpectralDimension_ArenaScoping.md`; `docs/ED_Research_Targets.md` #17.

- **Assumptions:** only a bare graph. d_s = −2·dlog P_return(t)/dlog t for a lazy random walk.
- **Claimed output:** none. ED filed it as a negative.
- **Does it go through?** The method checks out: 3.10 on a cubic lattice where 3 is required. The question itself was never answered, because no ED arena had both short within-chain (V1) links and longer cross-chain (V5) links.
- **Why it ranks first:** it is the one statistic in the corpus that is defined with no lengths and no lattice, so it cannot be inserted by hand.
- **Transplant:** CO's "unit growth laws give no manifold" result needs a pass/fail statistic, and this is it. Run d_s (plus a causal-set Myrheim–Meyer estimate on the commitment order) on graphs grown by candidate rules: commitment chains (1D) knit together by relations.
  - Required output: d_s → 3 at large t, ideally running lower at small t.
  - Risk ED recorded: a purpose-built arena tests your model, not the theory. Fix the grading rule before running.
  - Trap to avoid: ED's integer-rounded reach made b completely inert at R0 = 1.

### 2. Hilbert-space form from the record lattice (Piron–Solèr)
Source: `foundations/Gleason_CircularityAudit_2026-07-10.md`, `Gleason_Soler_LatticeVerification.md`, `Soler_ArcExhaustion_*`.

- **Assumptions:**
  - Commitment exclusivity gives a metric-free orthocomplement.
  - Irreversible, repeatable (first-kind) commitment gives the covering law.
  - Homogeneity gives an infinite family of atoms with equal weight.
  - Solèr's theorem then gives a Hilbert space over ℝ, ℂ or ℍ.
- **Claimed output:** the inner-product form plus orthogonality (`⟨K|L⟩ = 0` from perfect distinguishability, with the best confusion-free detection 1 − c²).
- **Does it go through?** Non-circular as a structure, because lattice-⟂ is the input and metric-⟂ the output. But the full orthomodular identity is assumed, not shown metric-free (ED's own "tightest screw"). ℂ was taken from the U(1) of P09, and T14 says that step fails.
- **Transplant:** CO's Q6 assumes the √P-amplitude Hilbert space, then gets Born from noncontextuality; Q6 itself records "a restatement; it predicts nothing new". CO's records are kept, irreversible and repeatable, which is exactly ED's input list. Showing that CO's record propositions are orthomodular with the covering law would move "amplitudes" from borrowed to derived (a structure, not a number). Getting ℂ needs an extra composition axiom, e.g. local tomography (Masanes–Müller; this is outside the ED corpus).

### 3. The shape of MOND's interpolating function from a monopole plus dipole norm
Source: `docs/ED_Research_Targets.md` #19 (and #18).

- **Assumptions:** the cosmic-horizon response is coupled by its norm, not by a cosθ projection. Parseval then gives ‖Σ‖² = |a₀₀|² + |a₁₀|².
- **Claimed output:** a_eff = √(a² + a₀²) − a₀, i.e. μ(x) = [√(1+x²) − 1]/x.
- **Does it go through?** The algebra is right, but it restates Milgrom's 1999 de Sitter/Unruh construction (Deser–Levin), as ED concedes. The value fails: three ED routes give a₀ ~ O(1)·cH₀, and nature wants about cH₀/5.7. In CO, with Λ as an input, a₀ = c√(Λ/3) = cH₀√Ω_Λ ≈ 0.83 × 6.8×10⁻¹⁰ ≈ 5.6×10⁻¹⁰ m/s², about 4.7 times too large.
- **Transplant:** if CO's presence clock picks up a de Sitter floor that adds in quadrature with the local acceleration, CO outputs a definite μ-shape, testable on SPARC. Treat it as a falsifiable structure whose coefficient is already in tension.

### 4. Graph-intrinsic linking as a dimension selector
Source: `foundations/ChainsAsLinks_MultichainV5_Reachable.md`, `ThreeDimensions_ConsolidatedReview.md`.

- **Assumptions:** the record graph contains a Petersen-family (K6-type) minor, which is constructive and was measured in ED. Record integrity then needs links that cannot be undone.
- **Claimed output:** d = 3. Such a graph does not embed in 2D (it is non-planar), and in 4D every graph has a linkless embedding.
- **Does it go through?** Only as a necessary-dimension argument. It assumes the graph must sit in a manifold (the thing CO lacks), and ED's own closure attempt failed: linking guards "non-separability", not order, and the 4D membrane loophole remains.
- **Transplant:** a cheap check on any CO growth rule: does it generate intrinsically linked minors at every scale? That is necessary, not sufficient.

### 5. Capacity–reach scaling as a consistency relation
Source: the CurvatureEmergence reach-law note, salvaged.

- **Assumptions:** a place's capacity counts its boundary (holographic, `AreaLaw_FromStraddlingEdges.md`).
- **Claimed output:** reach ~ P^(1/(d−1)), metric g ~ P^(−2/(d−1)).
- **Does it go through?** Not as a derivation (see above).
- **Transplant, inverted:** CO already has g_ij ∝ N^(−2) with N = P/P∞ (R2 and R9 at ε = 0). If CO can independently fix whether hop capacity scales with surface or volume, then matching exponents gives d: surface counting gives −2/(d−1) = −2, so d = 2, which is wrong. Unlikely to survive, but it is a quick test.

## Honest limits (ED's walls that point at a missing primitive)

- **Scale.** `docs/ED_Research_Targets.md` #10 and #9 (arc FSC): "every successful ED derivation of a number is an O(1) coefficient riding on an already-inherited scale". There is no mechanism for 10¹²². P09's U(1) is not compact under the dynamics, and the marginal RG flow has no fixed point. The Perron–Frobenius "universal" ratios depend on transition rates that are themselves inputs. This independently backs CO's finding that no record-internal primitive fixes p_c or the hop size (10^2.5–10³ ℓ_P).
  - Lesson: a large pure number needs a global count, e.g. N_H = (R_H/ℓ_P)² ~ 10¹²² (the only large number ED handles, in T19's holographic count), or an exponential. Local rules will not give one. Do not fit p_c ≈ 10⁶ as a power of N_H without a mechanism: that is numerology.
- **Continuum.** ED's committal substrate coarse-grains to ballistic transport, not diffusion, and never reaches Gaussianity (#3, #3c). CO's R3 is a discrete Laplacian (an average over 6 neighbours) on an assumed cubic lattice. Check whether CO's hop rule actually mixes enough to give that Laplacian.
- **#16.** There is no map from physical structure to channel capacities. In CO terms: what sets a body's draw from its make-up.

## Recommended next steps
1. Fix a dimension criterion in advance (d_s plateau within ±0.2 of 3 over a decade of t, plus a Myrheim–Meyer estimate), then grow CO graphs with chains-plus-relations rules and grade them.
2. Write out CO's record propositions as a lattice and test orthomodularity and the covering law directly. This is the step that would lift Q6 above a restatement.
3. Before adopting the μ-shape, compute CO's a₀ from its Λ input and record the factor-of-4.7 tension as a falsifier.
