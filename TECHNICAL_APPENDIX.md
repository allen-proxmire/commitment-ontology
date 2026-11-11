# Technical appendix: the rules as equations, and one derivation

Every statement carries its grade (ruled, candidate, needed, excluded, shape, silence) or says where it is imported or identified. Notation: places i on a network of finite degree d; neighbouring places joined by relations ⟨ij⟩; hop length ℓ, tick τ = ℓ/c; amounts of possibility in units of ħ.

## 1. The rules

**Possibility.**

| rule | statement |
|---|---|
| conservation | Σ_i P_i is unchanged by every passing and every commitment (ruled); births add P_b each, a new place born with its share P_b ≈ (d − 1)ħ (candidate) |
| P1 | a hop moves one quantum, q = ħ (candidate), and compares neighbours by ratio: the flow on ⟨ij⟩ is J_ij = κ ln(P_free,i / P_free,j), κ the hop's conductance (ruled) |
| P2 | P_free,i ≤ P_max; above it the place commits (ruled) |
| P3 | P_free,i = P_i(1 − h_i), h_i the engaged fraction; what a commitment engaged is released on completion, less C3's record (ruled) |
| P4 | net flow on ⟨ij⟩ runs toward the end with larger h (ruled; with P1 and P3, at equal P, J_ij = κ ln[(1 − h_i)/(1 − h_j)], a consequence there, not a restatement) |
| P5 | possibility in transit keeps its mean direction until its own commitment redirects it: the whole step U commutes with translations, so momentum is conserved (ruled) |
| P6 | a closed whole draws δ × (turning + 2 × travel), light draws δ × 2E, and every draw becomes record (candidate); the draw per volume is δ(ρ + S), and with travel at the local clock rate the source is (ρ + S)N (candidate reading) |
| P7 | a relation carries an occupancy o_ij, its excess over the vacuum's (each relation is fed by at least a quantum of free possibility in motion, candidate), and a which-way phase φ_ij ∈ U(1) (candidate); a route's length is Π(1 + o) along it, which at rest is P∞/P_free (ruled, given the occupancy, candidate) |
| P8 | two routes meeting at a place combine as p = \|√p₁ e^{iθ₁} + √p₂ e^{iθ₂}\|² (forced by conservation in passing, scalelessness and associativity; Goyal–Knuth–Skilling, an imported theorem) |

**Commitment.**

| rule | statement |
|---|---|
| C1 | a commitment, on completing, engages ħ of adjacent free possibility (or, through a channel, a quantum in transit, C8), releases what it held, and adds one to its count n; it halts when none is adjacent (ruled). Each beat engages the free share 1 − h of what it meets, carrying the remainder, and a tick completes when a whole ħ is engaged (the free-share rule, candidate, end of §1) |
| C2 | a commitment repeats at ω = (mc²/ħ)(1 − h) (ruled; its derivation from C1 and C4 under the free-share rule is candidate, end of §1) |
| C3 | each repeat keeps δħ as record (candidate); dR/dt ≥ 0 |
| C4 | every commitment engages ħ; mass is the repeat rate, ω₀ = mc²/ħ (ruled) |
| C5 | a pattern in transit carries a phase θ advancing by one cycle per repeat (ruled; the matter sector's one addition) |
| C6 | the walk's step is U = A_x A_y A_z F(θ_m) A_z A_y A_x, with A_j = S_j⁺ F(w) S_j⁻ F(−w): S_j⁺ moves the α_j = +1 part one place forward, S_j⁻ the α_j = −1 part one place back, F(a) = exp(−iβa) a turn of the internal state, θ_m = c₀mcℓ/ħ per step, c₀ = 2cos w the massless speed in hops per step (2 at w = 0: mcℓ/ħ per hop) (flip ruled; half-shift Wilson form candidate, w ≳ 0.3, run L1b; palindromic order needed, sequential excluded, run L1) |
| C7 | the first possibility, all free in few places, puts every place over capacity; the first commitments are unordered (ruled) |
| C8 | a commitment may engage a quantum in transit through a channel; which engager takes it is drawn from \|a\|² at the engagers' places (candidate; the \|a\|² draw identified, Born; the coupling and pointer basis imported) |

**Constants of the theory's own:** δ, P_max, Λ (Λ from data); P_b fixed by the degree if the candidate reading holds. **Measured:** G, c, ħ, 1/137, the masses. **Bound:** ℓ ≲ 1.3 × 10⁻³¹ m (needed, Crab PeV electrons), so δ ≳ 2 × 10⁻⁷.

**Where each quality comes from, and what it carries.** The rules are the qualities the two primitives need to act at all, plus those that data or a known result demands. Each is tagged by where it came from (*nature*: from what the primitive is; *data*: forced by an exclusion; *match*: chosen so that a known result comes out; *theorem*: follows from others) and by what it supports, since a quality that carries several independent results earns more than one that carries only the result it was chosen for.

| quality | origin | what it carries |
|---|---|---|
| conservation in passing; birth share | nature; birth share needed (a conserved stock starves under expansion), ruled candidate; size ≈ (d − 1)ħ candidate | P8, the Born identification, the sink, the floor, the inflation-like exit |
| P1 ratio hopping, one quantum per hop | nature (scalelessness favours ratio) and data (Mercury selects the pairing); q = ħ for consistency with the degree (R5) | Newton's 1/r, β = 1, the form of G, the lapse-weighted flux |
| P2 capacity | nature (no infinities) | the beginning, the inflation-like exit, births |
| P3 hold-and-release | nature (conservation) | the clock's free share, the record |
| P4 toward engagement | theorem at equal P (P1, P3); ruled otherwise | the clock slaved to the occupancies |
| P5 inertia | nature | free motion, the walk's momentum |
| P6 transit draws (turning once, travel twice; light 2E) | match (GR's source ρ + S) | ρ + S in the radiation era, gas stars and moving closed wholes; light's factor two (its one G ruled separately) |
| P7 occupancy | data (a scalar wave is excluded) | γ = 1, tensor waves, the route factor |
| P7 which-way phase | match (minimal coupling) | charge, g = 2, Aharonov–Bohm, two-body binding |
| P8 meeting | theorem (conservation, scalelessness, associativity) | interference, the amplitude rule |
| C1 renewal | nature (an act that repeats while fed) | matter's persistence, the sink |
| C2 clock | theorem from C1 and C4 under the free-share rule (candidate); the rule is data (redshift; clock coherence against chance ticks, if h counts every mass), its power one is data (Cassini) | redshift, the lapse, free fall |
| C3 retention; fixed share δħ | retention nature (the record only grows); fixed form data (lunar ranging excludes a drifting G) | the arrow of time, the sink; fixed form: G constant |
| C4 one quantum | nature and data (ħ) | mass as frequency |
| C5 phase | posit (the matter sector's one addition; interference needs it) | the walk's waves |
| C6 the flip | identification (Feynman's checkerboard); palindrome needed by data; Wilson form candidate | mass in the walk, Dirac's equation |
| C7 the beginning | initial condition | the first epoch |
| C8 measurement | match, narrowed by data (vacuum Rabi oscillation excludes the literal form) | outcomes, Born's chance |

Of eighteen entries, two are tagged *match* alone: the travel rule, which supplies ρ + S in several settings, and the which-way phase, which carries charge, g = 2, Aharonov–Bohm and two-body binding. C8 is matched and narrowed by data.

**Can the set be smaller?** Several qualities are versions of one thing (shape; a merge changes no content; it shows which rules state one assumption more than once):
- *One commitment cycle:* C1, C2, C3, C4 and P3 describe one act: engage ħ of adjacent free possibility, hold it, release it less δħ kept as record, repeat while fed, at ω = (mc²/ħ)(1 − h). The clock, C2, follows from the rest under the free-share rule (below).
- *One draw:* P6 and the draw half of C3 say the same thing: every draw (turning once, travel twice, light 2E) is δ of its energy and becomes record.
- *One walk:* P5, C5 and C6 together define transit: hops that keep direction, a phase, and the flip (P5 also acts in formation, lining up relations, R5).
- *Not qualities:* P4 at equal P and P8 follow from others; C7 is an initial condition.

**The clock from the cycle (candidate).** By C4 a commitment beats at ω₀ = mc²/ħ; by C1 each beat must engage ħ of free possibility. Possibility at a place carries no mark but free or engaged, and the free share 1 − h is set by the place's relations: what hopping brings in against what the sink draws (step 1). Each beat advances the commitment by that share, carrying the remainder, and a tick completes when a whole ħ has been engaged (the *free-share rule*, the author's ruling, candidate). The ticks come regularly, not by chance, at

$$\omega=\omega_0(1-h)=\frac{mc^{2}}{\hbar}(1-h),$$

which is C2. Two other readings are excluded, and a third is excluded if h counts every mass:
- *It takes free possibility wherever it lies.* While at least ħ is free nearby, nothing waits, ω = ω₀ for every h, and there is no gravitational redshift: excluded by Pound–Rebka and Gravity Probe A.
- *An engagement is n quanta, each needing the free share.* Then ω = ω₀(1 − h)ⁿ and N = e^{−nU}. The route factor (step 4) does not change, so g_ij = e^{2U}δ_ij against g₀₀ = −e^{−2nU} gives γ = 1/n. Cassini's γ − 1 = (2.1 ± 2.3)×10⁻⁵ forces n = 1. If each part is one hop quantum (n = ħ/q), this is q = ħ from a second direction (candidate).
- *Each beat completes by chance, with probability 1 − h.* The mean rate is again C2, but a clock's own time then wanders by σ_τ = √(h t/ω₀), and two atoms with clock transition ω_tr lose step after

$$T_c=\frac{\omega_0}{\omega_{\text{tr}}^{2}\,h}.$$

For the bound, an atom's count is its whole, ω₀ = Mc²/ħ; independent counts of its parts give the same σ_τ, since their rates add. For strontium (ω₀ = Mc²/ħ = 1.2×10²⁶ s⁻¹, ω_tr = 2.7×10¹⁵ s⁻¹), atoms in one lattice stay in step for 26 s (Zheng et al., Nature 602, 425, 2022), so h ≲ 7×10⁻⁷. The galaxy's potential at the Sun, |Φ|/c² ≈ 1–2×10⁻⁶, already exceeds this, and the bound is 10⁵ times tighter if a transition follows the electron's own beat. Excluded if h counts every mass.

So C2 is C1 and C4 under the free-share rule (candidate: the list of readings is not exhaustive). Under it the leftover share carries to the next beat, so tick times stray from uniform by less than one beat (1/ω₀ ≈ 10⁻²⁶ s for Sr) and never build up; only differences in h are seen, as in GR.

On that count the qualities fall into about eight groups: conservation with the birth share, ratio hopping in quanta, capacity, relations with occupancy and phase, the draw, the commitment cycle, the walk, and measurement. Separate choices remain inside them: q = ħ, the birth share, the palindromic order and Wilson form, light's one G, field energy as an amount, amounts classical.

## 2. One derivation: the weak-field metric

**Step 1: the static field equation.** At rest, every place's flows balance its sink. By P1 the net inflow to place i is κ Σ_j ln(P_free,j / P_free,i); by C3 and C2 the sink of a pattern of mass M is δħ per repeat at ω₀ = Mc²/ħ (to leading order in U), δħ·ω₀ = δMc², i.e. δMc²/ħ quanta per unit time. With the conductance of a hop moving one quantum per tick, κ = ħ/τ per relation, and the lattice Laplacian Σ_j(f_j − f_i) → ℓ²∇²f (cubic lattice, d = 6; other networks change this by a factor of order one),

$$\ell^{2}\nabla^{2}\ln P_{\text{free}}\cdot\frac{\hbar}{\tau}=\delta\,M c^{2}\,\ell^{3}\,\delta^{3}(\mathbf r)\quad\Rightarrow\quad\nabla^{2}\ln P_{\text{free}}=\sigma\,\delta^{3}(\mathbf r),\qquad \sigma=\frac{\delta M c\,\ell^{2}}{\hbar}.$$

Inputs: P1 (ratio, ruled; q = ħ, candidate), C2–C4, C3's fixed share (candidate).

**Step 2: its solution, and G.** With P_free → P∞ far away,

$$\ln\frac{P_{\text{free}}}{P_\infty}=-\frac{\sigma}{4\pi r}\equiv -U,\qquad U=\frac{GM}{c^{2}r}\quad\text{with}\quad G=\frac{\sigma c^{2}}{4\pi M}=\frac{\delta c^{3}\ell^{2}}{4\pi\hbar}.$$

So ℓ = ℓ_P√(4π/δ). Nothing is fitted here: G is measured, and the relation fixes ℓ given δ.

**Step 3: the clock.** By C2 with P = P∞ at the place (an identification; it holds inside matter to about 10⁻¹⁴, the record per place at nuclear density in ħ), a clock's rate is 1 − h = P_free/P∞ = e^{−U}. A clock is a commitment, so this is the lapse:

$$N=e^{-U}=1-U+\tfrac{U^{2}}{2}-\dots,\qquad g_{00}=-N^{2}=-\left(1-2U+2U^{2}-\dots\right).$$

**Step 4: routes.** By P7, a route's length is Π(1 + o) along it, and at rest the occupancies give the route factor P∞/P_free = e^{U} (ruled, given the occupancy, candidate):

$$g_{ij}=e^{2U}\delta_{ij}=(1+2U+\dots)\,\delta_{ij}.$$

Only the U term enters here (γ); at U² it differs from Schwarzschild's isotropic form, which the cost's spatial equation supplies.

**Step 5: read off the PPN parameters.** Against the isotropic expansion g₀₀ = −(1 − 2U + 2βU²), g_ij = (1 + 2γU)δ_ij:

$$\gamma=1,\qquad \beta=1.$$

β = 1 is where the ratio rule matters: a difference rule (P_free = P∞ − k/r) gives N² = 1 − 2U + U², β = ½, and Mercury's precession at 7/6 of GR's, excluded. So β = 1 is a fit in this sense: the hop's pairing is the one Mercury selects among the local power laws, and scalelessness favours it.

**Step 6: the tests.** With γ = β = 1, the standard formulas give light bending 4GM/(c²b), the Shapiro delay (1 + γ)(GM/c³) ln(4r₁r₂/b²), and perihelion advance 6πGM/[c²a(1 − e²)] per orbit (a fit: Mercury selected the pairing), GR's to this order.

**Free fall,** from the same field: a matter wave of frequency ω = (mc²/ħ)(1 − h) refracts toward higher h, and its group moves as g = c²∇h = c²e^{−U}∇U = c²∇U·(1 + O(U)), toward the mass: Newton's acceleration, independent of m.

**What the derivation uses, in one line.** Ratio hopping (ruled), one quantum per hop (candidate), the fixed share δħ (candidate), C2's clock (ruled; via the free-share rule, candidate), the route factor (ruled, given the occupancy, candidate), and P = P∞ at a place (identification). Beyond the weak field, Lovelock's theorem (given its hypotheses) supplies the exterior; that step uses an imported theorem.

**What kind of derivation this is.** It is derived from CO's rules, step by step, with nothing fitted to the gravitational field except one choice: the hop's pairing, which scalelessness favours and Mercury selects among local power laws. Newton's 1/r, the form of G, universal redshift, free fall and γ = 1 follow without it. Three inputs are candidate (one quantum per hop; the fixed share; the occupancy behind the route factor), one is an identification (P = P∞), and κ = ħ/τ is a choice. It is not a derivation from the two primitives alone.

## 3. A second derivation: Dirac's equation from the walk

**Step 1: the shifts in momentum space.** With P_j^± = (1 ± α_j)/2 and k the momentum in lattice units, a forward shift of the α_j = +1 part and a backward shift of the α_j = −1 part are

$$S_j^{+}=P_j^{+}e^{-ik_j\ell}+P_j^{-},\qquad S_j^{-}=P_j^{+}+P_j^{-}e^{+ik_j\ell}$$

(the run code uses k → −k; same physics).

**Step 2: one conditional shift.** Without the Wilson turn (w = 0), A_j = S_j⁺S_j⁻ = P_j⁺e^{−ik_jℓ} + P_j⁻e^{+ik_jℓ}. Since α_j² = 1, this is

$$A_j=\cos(k_j\ell)-i\alpha_j\sin(k_j\ell)=e^{-ik_j\ell\,\alpha_j}.$$

**Step 3: the palindromic step.** With F(θ) = e^{−iβθ},

$$U=e^{-ik_x\ell\alpha_x}e^{-ik_y\ell\alpha_y}e^{-ik_z\ell\alpha_z}\,e^{-i\beta\theta}\,e^{-ik_z\ell\alpha_z}e^{-ik_y\ell\alpha_y}e^{-ik_x\ell\alpha_x}=\exp\!\Big(-i\big[2\ell\,\boldsymbol\alpha\cdot\mathbf k+\beta\theta\big]+O(\varepsilon^{3})\Big),$$

ε the larger of kℓ and θ. A symmetric product has no second-order commutator term (Strang 1968); a sequential product would leave one, the handedness-dependent term that run L1 excludes, which is why the palindrome is needed.

**Step 4: identify the Hamiltonian.** A step is two hops, of duration τ_s = 2ℓ/c. Writing U = exp(−iτ_sH/ħ) with p = ħk and θ = mc²τ_s/ħ = 2mcℓ/ħ (C6: mcℓ/ħ per hop),

$$H=c\,\boldsymbol\alpha\cdot\mathbf p+\beta\,mc^{2}+\frac{\hbar c}{\ell}\,O(\varepsilon^{3}).$$

With α_j and β the Dirac matrices (four components, the least the Clifford algebra allows in three dimensions; Meyer's no-go rules out a scalar walk), this is Dirac's Hamiltonian, and spin ½ is its rotation generator's internal part. Identification: Bialynicki-Birula (1994); the algebra above is standard symmetric splitting.

**Step 5: what the lattice adds.** At k_jℓ = π, A_j = −1 and U reduces to F(θ); at k_jℓ = π/2, A_j = −iα_j: further species at quasi-energy 0 or π (fermion doubling). The Wilson half-shifts, A_j = S_j⁺F(w)S_j⁻F(−w), cancel at k = 0 and add at the zone edge, giving those species a mass of order wħ/(ℓc); with w ≳ 0.3 one light species remains (candidate; checked numerically, run L1b, not derived here). The cost is a speed excess of a massive pattern over a massless one, s ≈ 0.14·mcℓ/ħ at w = 0.3, which the Crab's PeV electrons bound to ℓ ≲ 1.3 × 10⁻³¹ m (needed). The Wilson turn also changes the k-linear coefficient near k = 0, by cos w: A_j ≈ 1 − ik_jℓ cos w·α_j e^{iβw}, a massless speed of 2cos w hops per step (1.911 at w = 0.3), so τ_s = c₀ℓ/c with c₀ = 2cos w; the speed called c is this renormalised one, at which light is ruled to move (candidate).

**What kind of derivation this is.** The continuum limit is a theorem about the step; that the step is CO's (four components, palindromic order, Wilson half-shifts) rests on C5, C6, two exclusions by data and one candidate. The identification of the result with the electron is by its equation, not derived from the primitives.
