# Blind referee review, 2026-11-04

A fresh session with no access to the working conversation was given the repository and a brief to review it as a hostile but fair journal referee, to recompute at least five claims itself, to classify each result, and to grade. The report is reproduced verbatim below. The corrections it forced are recorded at the top of each affected document.

---

## 1. Summary of the claims

The author proposes two primitives, a conserved "possibility" distributed over a network of places and an irreversible "commitment" that updates it, with time defined as a count of commitments. Clock rate is set to be proportional to the local free possibility, matter is a slow sink of it ("pooling", constant δ), and because the substrate is "scaleless" the sink equalises ratios, giving ∇²ln P = σδ(r) and hence the exponential (Yilmaz) metric ds² = −e^{−2U}dt² + e^{2U}dx², with γ = β = 1 and a 4.6% larger black-hole shadow than Schwarzschild. Gravitational waves are then said to require relations to carry an "occupancy" (edge length), whose mismatch cost is fixed by "sliding costs nothing" plus Lovelock's theorem to be Einstein–Hilbert, giving GR's quadrupole. Three dimensions are claimed as a consistency condition; Friedmann's equation follows from a Newtonian shell; a wave-driven birth mechanism for expansion was tested and withdrawn. In the matter sector, one addition ("commitments happen at a rate") is said to force amplitudes, the Born rule, a four-component internal state (Meyer, Clifford) and the Dirac equation (Bialynicki-Birula), with spin ½ and g = 2; charge, 1/137, the masses and colour are left open.

## 2. Checked computations

1. **Shadow and ISCO of the exponential metric (R3).** Recomputed b(ρ) = ρe^{2M/ρ}: minimum at ρ = 2M, b = 2eM = 5.4366M, ratio to 3√3M = 1.0463; areal photon-sphere radius 3.297M; ISCO at ρ = 5.236M, areal R = 6.338M, Ω = 0.06333/M, ratio to 6^{−3/2} = 0.931. **Correct.** But see item 3: the metric is not consistent with the dynamics the document also claims.

2. **Scalar quadrupole = 1/6 of GR for a circular binary.** For a scalar sourced by ρ with Newtonian normalisation, the far-field flux gives P = (G/60c⁵)[(A_ii)² + 2A_ijA_ij] (the angular integral ∮(n_in_jA_ij)²dΩ = (4π/15)[tr² + 2A:A] verified by Monte Carlo); with a constant trace the ratio to (G/5)[A:A − tr²/3] is exactly 1/6. **Correct**, and a well-known result about scalar gravity restated.

3. **Is the exponential metric a solution of the claimed Einstein–Hilbert dynamics?** The Ricci tensor computed numerically at a generic point: R_tt = 0, R_ij = −2∂_iU∂_jU ≠ 0. The exponential metric is **not Ricci-flat**; it is GR sourced by a massless scalar (the standard characterisation of the Yilmaz metric). By Birkhoff's theorem a pure EH mismatch cost makes every static spherical exterior Schwarzschild, so the "4.6% larger shadow" and "Einstein–Hilbert cost, GR's quadrupole" cannot both hold. If instead the scalar ln P carries stress-energy, it also carries radiation, and the author's own 1/6 argument then re-enters as an O(1) scalar admixture excluded by Hulse–Taylor at 0.3%. **Internally incorrect as a pair of claims.**

4. **Ġ/G.** With fixed δħ per renewal the floor P∞ falls at the expansion rate and G ∝ 1/P∞ gives Ġ/G ≈ H₀ ≈ 7×10⁻¹¹ yr⁻¹ against the lunar-laser-ranging bound ~10⁻¹³ yr⁻¹. **Correct arithmetic**, exclusion by ~10³ as stated. The rescue, "pooling as a share of what is there, δħ(P_free/P_max)", does remove the observable, but it is a factor introduced for that purpose. The document says as much; it should also say that this leaves δ with no observational handle at all.

5. **Hop-length relation ℓ = ℓ_P√(4πP_max/δ).** The diffusion bookkeeping (D = νℓ², point-sink deficit σ/(4πνr) per place, h = GM/(c²rℓ)) gives G = δc³ℓ²/(4πħP_max), dimensionally consistent, algebra **correct**. It is a definition of δ in terms of ℓ, not a prediction; "no new constant" is true only in the sense that one unknown was renamed. MATTER.md also gives two incompatible values: ℓ ≈ 10⁻¹⁶ m (used to get δ ≈ 10⁻³⁷) and ℓ ≲ 1.1×10⁻¹⁸ m from the top-quark bound two paragraphs earlier.

6. **g-factor and spin of the loops.** Square: S = mcℓ/2 = ħ/2, μ = ecℓ/4 = eħ/4m, g = 1: **correct**, the classical co-moving charge/mass result. Chair vector area (1,−1,1)ℓ², S = ħ/√3: **correct**. Honestly reported as a failure; the subsequent "g = 2 follows from Dirac" is simply the Dirac equation's property under minimal coupling, which CO has not derived (charge and Maxwell are "candidate").

7. **Q1 "geometric ratio".** The note claims the measured hexagon/square circulation ratio 0.87 "is the geometric ratio for a smooth circulating field … (√3/6)/(1/4) = 0.866" and the post-run check says this was "computed independently and matches". (√3/6)/(1/4) = 1.1547, not 0.866; the document inverted the fraction. Sampling a uniform-curl field and Gaussian vortices on the same lattice loops with the same RMS statistic: hex/sq = 1.15 (uniform) to 1.06–1.15 (vortices). The measured 0.87 therefore does **not** match a smooth field; squares carry more circulation per edge than a smooth vortex would. The qualitative conclusion (hexagons do not dominate, so the chair is not the orbit) survives; the quantitative confirmation is **incorrect and misleadingly presented**.

8. **Ollivier curvature.** κ via LP for Z², Z³ and the triangular lattice with uniform non-lazy neighbour measures: all zero. **Correct**; the "flatness does not know dimension" finding is right. It is also not new: annealing random graphs under an Ollivier-curvature action and watching lattice-like geometry emerge is Trugenberger's "combinatorial quantum gravity" programme (2017–2019), uncited.

9. **Mercury 7/6 and β.** N = 1−U gives β = ½ and (2+2γ−β)/3 = 7/6; N = e^{−U} gives β = 1. **Correct.**

10. **Radiation era.** "Newton on a shell" gives ä = −(4πG/3)ρa; integrating this with ρ ∝ a⁻⁴ gives H² = (4πG/3)ρ, half the Friedmann coefficient. The document instead asserts H² = (8πG/3)ρ and says "ρ + 3p follows by differentiating … it is bookkeeping". That is circular: the pressure term is exactly what the Newtonian shell does not supply. **Incorrect as a derivation.**

## 3. Classification

- Newton's law, redshift, universal free fall, light bending 4GM/c²b, Shapiro delay, Friedmann (matter era): **(d)** relabelling of standard weak-field physics; the metric is *assumed* to be built from one potential "counted twice".
- Ratio hopping → exponential metric, β = 1: **(c)**; the choice was selected by Mercury ("Mercury excludes difference hopping"), so Mercury is an input, not a prediction, contrary to CO_plain_language ("fixed by a statement … ruled before gravity").
- Strong-field shadow/ISCO: **(a)** given the metric, but the metric is Yilmaz's, and it contradicts the item below.
- Einstein–Hilbert cost, tensor waves, quadrupole: **(b)**; Lovelock's theorem does all the work, with an unstated hypothesis (second-order field equations) and an unestablished one (that occupancies form a metric with no other dynamical field). Regge calculus does the "network" part.
- Three dimensions: **(d)**; Ehrenfest (orbits/atoms), Huygens in even d, polarisation count, and Gauss–Bonnet in d ≥ 5 are the standard Tegmark-style arguments.
- Inflation with its own exit, "beginning", black hole as ceiling: **(c)**; no number is produced.
- R4–R7b locality results: **(a)** as modest numerical experiments; prior art exists.
- Amplitude rule and Born rule: **(b)/(c)**; the premise "the cross term has zero mean and scales as √(p₁p₂)" already encodes the structure, the relevant theorem is the Goyal–Knuth–Skilling-type derivation from associativity, and "Lamperti's isometry" (isometries of L^p) does not obviously do this job. "Born for free" is the Born postulate restated as "chance = possibility".
- Internal state, four components: **(b)**; Meyer's no-go and the Clifford representation count, with the author's own admission that "'the limit must be relativistic' is what forces β".
- Dirac equation, spin ½, g = 2: **(b)/(d)**; Bialynicki-Birula's automaton is identified with the rules, and g = 2 requires a coupling CO does not have.
- Charge as carried sign, Maxwell by uniqueness, quantisation: **(c)**, labelled candidate, correctly.
- Colour excluded via SO(3) ⊂ SU(3): **(a)**, correct group theory, negative.

## 4. Three weakest links

1. **Two incompatible gravity sectors.** The exterior is the exponential metric (Ricci ≠ 0) while the dynamics is claimed to be Einstein–Hilbert. One of the two headline results (the 4.6% shadow, or "GR's quadrupole with Einstein's coefficient") is false. Fixing it either removes the only prediction that differs from GR, or reintroduces scalar radiation already excluded by the author.
2. **"Sliding costs nothing" → Lovelock.** This needs (i) that occupancies alone define a metric and nothing else is dynamical, though the theory has a scalar ln P everywhere, and (ii) second-order field equations, never justified. Without them R², f(R) and scalar–tensor costs are allowed and nothing is forced.
3. **Ratio hopping and "route lengthens" as readings.** The clock factor e^{−U} is a definition (rate ∝ P_free) and the spatial factor e^{+U} is a reading ("the route factor is P∞/P_free"). Both are chosen so that the exponential metric results; change the second and γ and the strong-field predictions change. Mercury selected the first.

## 5. Strongest claim

The strong-field prediction: shadow radius 2eM (+4.6%), ISCO frequency −7%, no horizon. It is sharp, has a sign, and ngEHT or ringdown/iron-line data can kill it. However it is Yilmaz's metric's prediction, published decades ago, and is only CO's if the EH/exponential contradiction is resolved in favour of the exponential metric. Falsification: shadow consistent with Kerr to ≲3% for an independently measured mass; or Kerr ringdown; also the absence of a horizon implies surface emission already constrained by EHT.

## 6. Honesty assessment

The working documents are unusually candid: withdrawals are kept with reasons, R1–R2 and Q1 report negatives, the "where a fair critic pushes" lists are accurate and name the borrowed theorems. Overclaims concentrate in README.md and CO_plain_language.md: "From them: Newton's law … all four classical tests" (relabelling), "Three dimensions follow as a consistency condition" (standard argument), "Mercury's precession is fixed by a statement … ruled before gravity" (Mercury was the selector), "Friedmann's equation with the matter and radiation eras … with nothing borrowed" (radiation era circular), "forced, not assumed" for amplitudes (premises encode the structure), "g = 2 follows" (no coupling derived), "Complete as far as the two primitives force it" (the gravity sector is self-inconsistent). Q1's post-run check reports a false numerical confirmation. Underclaim: the author's own 1/6 argument is stronger than they use it; it also excludes the exponential-metric-plus-EH combination.

## 7. Grades

- Internal consistency: **D** — the exterior metric and the claimed field equations are mutually exclusive, and ℓ is given two incompatible values.
- Honesty of status labels: **B−** — exemplary in the working files, inflated in the public summaries, one false "verified" check.
- Mathematical correctness: **B−** — shadow, ISCO, 1/6, g = 1, Ollivier and Ġ/G arithmetic are right; the Q1 ratio is inverted, the radiation-era Friedmann step is circular, and Lamperti is misapplied.
- Novelty beyond standard physics: **D** — the only non-standard prediction is Yilmaz's; the lattice-emergence runs reproduce Trugenberger's programme.
- Testability: **C** — one borrowed, sharp, live number; inflation, the beginning and the ceiling carry no numbers.

## 8. Verdict to the editor

Reject in present form. This is a careful, self-critical and largely numerically competent reinterpretation of known physics in a new vocabulary, not a derivation of it: every quantitative success is standard weak-field gravity, Friedmann cosmology, or the Dirac automaton under its own name, and every genuine theorem (Lovelock, Meyer, Clifford, Bialynicki-Birula) is doing the work with its hypotheses supplied by fiat. The one distinguishing prediction, the Yilmaz exterior and its 4.6% shadow, is contradicted by the manuscript's own claim that the dynamics is Einstein–Hilbert, since that metric is not Ricci-flat. Resubmission as a short note is encouraged only if the author (i) chooses one gravity sector and shows it is consistent with both Hulse–Taylor and the classical tests, (ii) removes or re-derives the radiation-era step, (iii) corrects the Q1 ratio, (iv) cites Yilmaz and Trugenberger as prior art, and (v) rewrites the public summaries to match the honesty of the working records.
