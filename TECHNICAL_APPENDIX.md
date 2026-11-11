# Technical appendix: the rules as equations, and one derivation

Each rule's grade is in its own column: posited (a quality the author has decided, not derived), candidate (proposed, open to reversal), needed (forced by data or exclusion), excluded, shape (a form without a rule), silence; or imported, identified. Notation: places i on a network of finite degree d; neighbouring places joined by relations ⟨ij⟩; hop length ℓ, tick τ = ℓ/c; amounts of possibility in units of ħ.

## 1. The rules

**Possibility.**

| rule | statement | grade |
|---|---|---|
| conservation | Σ_i P_i is unchanged by every hop. Every draw (C3's δħ per repeat; P6's travel, light and field energy) turns possibility into record, so between births Σ_i (P_i + R_i) is unchanged and dR ≥ 0. Births add P_b each, a new place born with its share P_b = P∞ | per hop: posited. P + R: the author's ruling, candidate. P_b's size: shape, set by R5's count (about (d − 1)ħ without pairing; larger at the same degree with pairing, R5-B); with the held share and stretch at one place, no condition ties P∞ to the relations' feed |
| P1 | a hop moves one quantum, q = ħ, and compares neighbours by ratio: the flow on ⟨ij⟩ is J_ij = κ ln(P_free,i / P_free,j), κ the hop's conductance | q = ħ: candidate. ratio flow: posited |
| P2 | P_free,i ≤ P_max; above it the place commits | posited |
| P3 | P_free,i = P_i(1 − h_i), h_i the engaged fraction; what a commitment engaged is released on completion, less C3's record | posited |
| P4 | net flow on ⟨ij⟩ runs toward the end with larger h; with P1 and P3, at equal P, J_ij = κ ln[(1 − h_i)/(1 − h_j)] | posited; a consequence at equal P, not a restatement |
| P5 | possibility in transit keeps its mean direction until its own commitment redirects it: the whole step U commutes with translations, so momentum is conserved | posited |
| P6 | a closed whole draws δ × (turning + 2 × travel); light draws δ × 2E; every draw becomes record and sets the held share and stretch of the places around it, against a stiffness of one quantum per relation; the relations' own field energy draws as every field's does, the draw the flat ln P law's compounding stands in for (on the curved network, the relations' stretch weighting the flow), not an added source; the draw per volume is δ(ρ + S), and with travel at the local clock rate the source is (ρ + S)N | draws: candidate. setting the held share and stretch, stiffness one quantum: the author's ruling, candidate. (ρ + S)N: candidate reading. The relations' field energy: the author's ruling, candidate |
| P7a | a place carries the lapse share h and the stretch (the diagonal γ_ii): the excess a draw sets is held at the place, not free for commitments to engage, not drawing, counted in h; a route's length is the product of its hops' stretch factors, each hop taking the mean of its two ends' stretch, at rest P∞/P_free. Relations are fed by at least a quantum of free possibility in motion, the vacuum's, with a stiffness of one quantum (whether the stiffness tracks the feed, open) | placement: the author's ruling, candidate (run G3). held: the author's ruling, candidate. feed: candidate. route length: posited, given the stretch, candidate. Mean of a hop's ends: the author's ruling, candidate (a hop has no front or back for size; matches the staggered averaging to a link; error of order (ℓ/r)² rather than ℓ/r) |
| P7b | a relation carries the direction-reversing quantities: its one-way part a_ij = (o_ij − o_ji)/2, set by the direction of travelling draws, which carries the shift g_0i, and the displacement of its places, which is pure gauge; only the one-way part's sums around loops are physical, as for a U(1) link | the author's ruling, candidate |
| P7c | each square between relations carries the shear (the off-diagonal γ_ij, i ≠ j), set by the off-diagonal stress T_ij; the walk reads its local frame from its place's stretch and the surrounding squares' shear; with P7a and P7b every metric component has a carrier on the cubic graph, placed so that no backdrop holds exactly on the lattice (run G3) | the author's ruling, candidate |
| P7d | a relation carries a which-way phase φ_ij ∈ U(1) | candidate |
| P7e | no backdrop: moving places and reparametrising each place's time, including rate changes that shift its lapse, cost nothing, at every order (the freedom may itself depend on the field; at linear order, linearised diffeomorphism invariance). Given that, locality, two derivatives, time reversal and long wavelengths, the relations' cost is forced to linearised Einstein–Hilbert up to a strength and a speed (run G1); exactly on the lattice when the carriers are staggered as P7a–c place them, and not, within nearest-neighbour range, as previously placed (run G3); the carriers' behaviour as a tensor is an identification. No backdrop holds for everything on the network, the walk included: a pattern cannot tell a relabelling from no change; with locality and at most one derivative on the carriers, the walk's linear response is then −½ h_μν T^μν, T the walk's symmetric stress tensor, the coupling that sources the field (continuum, linear order; the spin's share uses P8b's frame identification) | places: posited. time: the author's ruling, candidate. the linear cost: needed, given both and the identification; cube-anisotropic terms at order (kℓ)² suppressed, not excluded. At every order: the author's ruling, candidate; with locality and two derivatives at every order and Lorentz-invariant interactions (assumptions), the cost is Einstein–Hilbert plus Λ (consistent deformation: Wald 1986; Boulanger, Damour, Gualtieri, Henneaux 2001), given the metric identification, in the continuum (the lattice's nonlinear cost open). For the walk: the author's ruling, candidate; the linear response needed, given it; exact on the lattice at linear order for a free Wilson–Dirac stand-in in continuous time (run G4; not unique), the discrete-time walk and interactions owed |
| P8 | two routes meeting at a place combine as p = \|√p₁ e^{iθ₁} + √p₂ e^{iθ₂}\|² | imported theorem (Goyal–Knuth–Skilling: forced by conservation in passing, scalelessness and associativity) |
| P8b | two patterns of one kind: the exchange factor is flat on the graph (no phase around elementary squares once the which-way phase is removed), so in three dimensions it is ±1; its value is the factor the internal states pick up as the places' frames carry them through the swap, (−1)^{2s} | the author's rulings, candidate; ±1 needed given flatness (Leinaas–Myrheim) |

**Commitment.**

| rule | statement | grade |
|---|---|---|
| C1 | a commitment of a pattern (a first commitment, C7, or one of its repeats), on completing, engages ħ of adjacent free possibility (or, through a channel, a quantum in transit, C8), releases what it held, less C3's record, and adds one to its count n; it halts when none is adjacent. Each beat engages the free share 1 − h of what it meets, carrying the remainder; a tick completes when a whole ħ is engaged (the free-share rule, end of §1). A commitment forced by over-capacity in the beginning's epoch does not renew (C7) | posited; the free-share rule: candidate; restriction to patterns' commitments: with C7's ruling, candidate |
| C2 | a commitment repeats at ω = (mc²/ħ)(1 − h) | posited; its derivation from C1 and C4 under the free-share rule: candidate |
| C3 | each repeat keeps δħ as record; dR/dt ≥ 0; record is what possibility became, not possibility, and does not count in a place's P | δħ: candidate. record not possibility: the author's ruling, candidate |
| C4 | every commitment engages ħ; mass is the repeat rate, ω₀ = mc²/ħ | posited |
| C5 | a pattern in transit carries a phase θ advancing by one cycle per repeat | posited; the matter sector's one addition |
| C6 | the walk's step is U = A_x A_y A_z F(θ_m) A_z A_y A_x, with A_j = S_j⁺ F(w) S_j⁻ F(−w): S_j⁺ moves the α_j = +1 part one place forward, S_j⁻ the α_j = −1 part one place back, F(a) = exp(−iβa) a turn of the internal state, θ_m = c₀mcℓ/ħ per step, c₀ = 2cos w the massless speed in hops per step (2 at w = 0: mcℓ/ħ per hop) | flip: posited. half-shift Wilson form: candidate, w ≳ 0.3 (run L1b). palindromic order: needed; sequential excluded (run L1) |
| C7 | the first possibility, all free in few places, puts every place over capacity; the first commitments are unordered. Only the first commitments start renewing patterns; a commitment forced later in the epoch by over-capacity is a single event: it turns possibility into record, releases the rest in transit, and does not renew | posited. First commitments alone renew: the author's ruling, candidate |
| C8 | a commitment may engage a quantum in transit through a channel, a final state with its width, at the weight of its line shape (κ = 0 only with no final state or a zero matrix element); which engager takes it is drawn from \|a\|² at the engagers' places | candidate; the \|a\|² draw identified (Born); the coupling and pointer basis imported |

**Constants of the theory's own:** δ, P_max, Λ (Λ from data); P_b fixed by the degree if the candidate reading holds. **Measured:** G, c, ħ, 1/137, the masses. **Bound:** ℓ ≲ 1.3 × 10⁻³¹ m (needed, Crab PeV electrons), so δ ≳ 2 × 10⁻⁷ (through G's formula).

**Where each quality comes from, and what it carries.** The rules are the qualities the two primitives need to act at all, plus those that data or a known result demands. Each is tagged by where it came from (*nature*: from what the primitive is; *data*: forced by an exclusion; *match*: chosen so that a known result comes out; *theorem*: follows from others) and by what it supports, since a quality that carries several independent results earns more than one that carries only the result it was chosen for.

| quality | origin | what it carries |
|---|---|---|
| conservation in passing; birth share | nature; birth share needed (a conserved stock starves under expansion), posited, candidate; size shape (R5's count) | P8, the Born identification, the sink, the floor, the inflation-like exit |
| P1 ratio hopping, one quantum per hop | nature (scalelessness favours ratio) and data (Mercury selects the pairing); q = ħ for consistency with the degree (R5) | Newton's 1/r, β = 1, the form of G, the lapse-weighted flux |
| P2 capacity | nature (no infinities) | the beginning, the inflation-like exit, births |
| P3 hold-and-release | nature (conservation) | the clock's free share, the record |
| P4 toward engagement | theorem at equal P (P1, P3); posited otherwise | the clock slaved to the held share |
| P5 inertia | nature | free motion, the walk's momentum |
| P6 transit draws (turning once, travel twice; light 2E) | match (GR's source ρ + S) | ρ + S in the radiation era, gas stars and moving closed wholes; light's factor two (its one G posited separately) |
| P7a stretch | data (a scalar wave is excluded) | γ = 1, tensor waves, the route factor |
| P7a held share and stretch at places; P7b one-way part on relations; P7c shear on squares | posits (the field must be carried by the network's parts; each part of the metric needs a carrier) | the moving body's field, frame dragging, shear |
| P7d which-way phase | match (minimal coupling) | charge, g = 2, Aharonov–Bohm, two-body binding |
| P8 meeting | theorem (conservation, scalelessness, associativity) | interference, the amplitude rule |
| C1 renewal | nature (an act that repeats while fed) | matter's persistence, the sink |
| C2 clock | theorem from C1 and C4 under the free-share rule (candidate); the rule is data (redshift; clock coherence against chance ticks, if h counts every mass), its power one is data (Cassini) | redshift, the lapse, free fall |
| C3 retention; fixed share δħ | retention nature (the record only grows); fixed form data (lunar ranging excludes a drifting G) | the arrow of time, the sink; fixed form: G constant |
| C4 one quantum | nature and data (ħ) | mass as frequency |
| C5 phase | posit (the matter sector's one addition; interference needs it) | the walk's waves |
| C6 the flip | identification (Feynman's checkerboard); palindrome needed by data; Wilson form candidate | mass in the walk, Dirac's equation |
| C7 the beginning | initial condition | the first epoch |
| C8 measurement | match, narrowed by data (vacuum Rabi oscillation excludes the literal form); its channel clause (frequency and direction) follows from the walk and the phase for a classical drive and a translation-invariant engager, within a width (candidate) | outcomes, Born's chance |

Of the entries, two are tagged *match* alone: the travel rule, which supplies ρ + S in several settings, and the which-way phase, which carries charge, g = 2, Aharonov–Bohm and two-body binding. C8 is matched and narrowed by data.

**Can the set be smaller?** Several qualities are versions of one thing (shape; a merge changes no content; it shows which rules state one assumption more than once):
- *One commitment cycle:* C1, C2, C3, C4 and P3 describe one act: engage ħ of adjacent free possibility, hold it, release it less δħ kept as record, repeat while fed, at ω = (mc²/ħ)(1 − h). The clock, C2, follows from the rest under the free-share rule (below).
- *One draw:* P6 and the draw half of C3 say the same thing: every draw (turning once, travel twice, light 2E) is δ of its energy and becomes record.
- *One walk:* P5, C5 and C6 together define transit: hops that keep direction, a phase, and the flip (P5 also acts in formation, lining up relations, R5).
- *Not qualities:* P4 at equal P and P8 follow from others; C7 is an initial condition.
- *Partly consequences:* C2 follows from C1 and C4 under the free-share rule (below); C8's channel clause (frequency and direction, with recoil, within a width) follows from the walk and the phase for a classical drive, leaving C8's core posited: that a passage can be an engagement, which passages are, single-quantum exchange (held) and the Lüders update.

On that count the qualities fall into about eight groups: conservation with the birth share, ratio hopping in quanta, capacity, the network's carriers (stretch, one-way part, shear) and phase, the draw, the commitment cycle, the walk, and measurement. Separate choices remain inside them: q = ħ, the birth share, the palindromic order and Wilson form, light's one G, field energy as an amount, amounts classical.

**The clock from the cycle (candidate).** By C4 a commitment beats at ω₀ = mc²/ħ; by C1 each beat must engage ħ of free possibility. Possibility at a place carries no mark but free or engaged, and the free share 1 − h is set by the place's relations: what hopping brings in against what the sink draws (step 1). Each beat advances the commitment by that share, carrying the remainder, and a tick completes when a whole ħ has been engaged (the *free-share rule*, posited, candidate). The ticks come regularly, not by chance, at

$$\omega=\omega_0(1-h)=\frac{mc^{2}}{\hbar}(1-h),$$

which is C2. Two other readings are excluded, and a third is excluded if h counts every mass:
- *It takes free possibility wherever it lies.* While at least ħ is free nearby, nothing waits, ω = ω₀ for every h, and there is no gravitational redshift: excluded by Pound–Rebka and Gravity Probe A.
- *An engagement is n quanta, each needing the free share.* Then ω = ω₀(1 − h)ⁿ and N = e^{−nU}. The route factor (step 4) does not change, so g_ij = e^{2U}δ_ij against g₀₀ = −e^{−2nU} gives γ = 1/n. Cassini's γ − 1 = (2.1 ± 2.3)×10⁻⁵ forces n = 1. If each part is one hop quantum (n = ħ/q), this is q = ħ from a second direction (candidate).
- *Each beat completes by chance, with probability 1 − h.* The mean rate is again C2, but a clock's own time then wanders by σ_τ = √(h t/ω₀), and two atoms with clock transition ω_tr lose step after

$$T_c=\frac{\omega_0}{\omega_{\text{tr}}^{2}\,h}.$$

For the bound, an atom's count is its whole, ω₀ = Mc²/ħ; independent counts of its parts give the same σ_τ, since their rates add. For strontium (ω₀ = Mc²/ħ = 1.2×10²⁶ s⁻¹, ω_tr = 2.7×10¹⁵ s⁻¹), atoms in one lattice stay in step for 26 s (Zheng et al., Nature 602, 425, 2022), so h ≲ 7×10⁻⁷. The galaxy's potential at the Sun, |Φ|/c² ≈ 1–2×10⁻⁶, already exceeds this, and the bound is 10⁵ times tighter if a transition follows the electron's own beat. Excluded if h counts every mass.

So C2 is C1 and C4 under the free-share rule (candidate: the list of readings is not exhaustive). Under it the leftover share carries to the next beat, so tick times stray from uniform by less than one beat (1/ω₀ ≈ 10⁻²⁶ s for Sr) and never build up; only differences in h are seen, as in GR.

## 2. One derivation: the weak-field metric

**Step 1: the static field equation.** At rest, every place's flows balance its sink. By P1 the net inflow to place i is κ Σ_j ln(P_free,j / P_free,i); by C3 and C2 the sink of a pattern of mass M is δħ per repeat at ω₀ = Mc²/ħ (to leading order in U), δħ·ω₀ = δMc², i.e. δMc²/ħ quanta per unit time. With the conductance of a hop moving one quantum per tick, κ = ħ/τ per relation, and the lattice Laplacian Σ_j(f_j − f_i) → ℓ²∇²f (cubic lattice, d = 6; other networks change this by a factor of order one),

$$\ell^{2}\nabla^{2}\ln P_{\text{free}}\cdot\frac{\hbar}{\tau}=\delta\,M c^{2}\,\ell^{3}\,\delta^{3}(\mathbf r)\quad\Rightarrow\quad\nabla^{2}\ln P_{\text{free}}=\sigma\,\delta^{3}(\mathbf r),\qquad \sigma=\frac{\delta M c\,\ell^{2}}{\hbar}.$$

Inputs: P1 (ratio, posited; q = ħ, candidate), C2–C4, C3's fixed share (candidate).

**Step 2: its solution, and G.** With P_free → P∞ far away,

$$\ln\frac{P_{\text{free}}}{P_\infty}=-\frac{\sigma}{4\pi r}\equiv -U,\qquad U=\frac{GM}{c^{2}r}\quad\text{with}\quad G=\frac{\sigma c^{2}}{4\pi M}=\frac{\delta c^{3}\ell^{2}}{4\pi\hbar}.$$

So ℓ = ℓ_P√(4π/δ). Nothing is fitted here: G is measured, and the relation fixes ℓ given δ. Since the inflow is the static form only, the formula's footing is static consistency. Under the ruling that a draw sets the held share and stretch of the places around it, against a stiffness of one quantum per relation (the author's ruling, candidate), the network imposes the profile, and ratio hopping across it must carry the body's draw, the same flux through every sphere: that is this balance, so G = δc⁴ℓ/(4πκ), which is δc³ℓ²/(4πħ) at κ = ħ/τ (a choice). Reading G as the draw against the relations' stiffness gives the same form; equating the stiffness with the conductance is a further posit (shape).

**Step 3: the clock.** By C2 with P = P∞ at the place (an identification; record is not possibility and does not count in P, so inside matter it holds to at most ~10⁻⁴⁹, the engaged share per place at nuclear density), a clock's rate is 1 − h = P_free/P∞ = e^{−U}. A clock is a commitment, so this is the lapse:

$$N=e^{-U}=1-U+\tfrac{U^{2}}{2}-\dots,\qquad g_{00}=-N^{2}=-\left(1-2U+2U^{2}-\dots\right).$$

**Step 4: routes.** By P7, a route's length is the product of its places' stretch factors, and at rest the stretch gives the route factor P∞/P_free = e^{U} (posited, given the stretch, candidate). The stretch and the held share sit at one place, so the clause ties them with no lattice factor; at linear order it agrees with the cost's static solution (γ = 1):

$$g_{ij}=e^{2U}\delta_{ij}=(1+2U+\dots)\,\delta_{ij}.$$

Only the U term enters here (γ); at U² it differs from Schwarzschild's isotropic form, which the cost's spatial equation supplies.

**Step 5: read off the PPN parameters.** Against the isotropic expansion g₀₀ = −(1 − 2U + 2βU²), g_ij = (1 + 2γU)δ_ij:

$$\gamma=1,\qquad \beta=1.$$

β = 1 is where the ratio rule matters: a difference rule (P_free = P∞ − k/r) gives N² = 1 − 2U + U², β = ½, and Mercury's precession at 7/6 of GR's, excluded. So β = 1 is a fit in this sense: the hop's pairing is the one Mercury selects among the local power laws, and scalelessness favours it.

**Step 6: the tests.** With γ = β = 1, the standard formulas give light bending 4GM/(c²b), the Shapiro delay (1 + γ)(GM/c³) ln(4r₁r₂/b²), and perihelion advance 6πGM/[c²a(1 − e²)] per orbit (a fit: Mercury selected the pairing), GR's to this order.

**Free fall,** from the same field: a matter wave of frequency ω = (mc²/ħ)(1 − h) refracts toward higher h, and its group moves as g = c²∇h = c²e^{−U}∇U = c²∇U·(1 + O(U)), toward the mass: Newton's acceleration, independent of m.

**What the derivation uses, in one line.** Ratio hopping (posited), one quantum per hop (candidate), the fixed share δħ (candidate), C2's clock (posited; via the free-share rule, candidate), the route factor (posited, given the stretch, candidate), and P = P∞ at a place (identification). Beyond the weak field, the exterior comes from the cost being Einstein–Hilbert, by consistent deformation given P7e at every order and its assumptions (P7e row); that step uses an imported theorem.

**What kind of derivation this is.** It is derived from CO's rules, step by step, with two choices made by data: the hop's pairing, which scalelessness favours and Mercury selects among local power laws (β = 1), and the route factor, whose stretch reading was chosen when a scalar wave was excluded (γ = 1, with Cassini fixing the clock's one quantum per engagement). Newton's 1/r, the form of G, universal redshift and free fall follow without either. Three inputs are candidate (one quantum per hop; the fixed share; the stretch behind the route factor), one is an identification (P = P∞), and κ = ħ/τ is a choice. It is not a derivation from the two primitives alone. It is a static derivation: read in time, step 1's inflow is diffusion, far too slow to set up or carry a field (`OPEN_DIRECTIONS.md`, "What carries the field"), so the equation stands only as a static form; the inflow cannot be the field's dynamics; G's formula rests on the draws setting the network (step 2).

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

**Step 5: what the lattice adds.** At k_jℓ = π, A_j = −1 and U reduces to F(θ); at k_jℓ = π/2, A_j = −iα_j: further species at quasi-energy 0 or π (fermion doubling). The Wilson half-shifts, A_j = S_j⁺F(w)S_j⁻F(−w), cancel at k = 0 and add at the zone edge, giving those species a mass of order wħ/(ℓc); with w ≳ 0.3 one light species remains (candidate; checked numerically, run L1b, not derived here). The cost is a speed excess of a massive pattern over a massless one, s ≈ 0.14·mcℓ/ħ at w = 0.3, which the Crab's PeV electrons bound to ℓ ≲ 1.3 × 10⁻³¹ m (needed). The Wilson turn also changes the k-linear coefficient near k = 0, by cos w: A_j ≈ 1 − ik_jℓ cos w·α_j e^{iβw}, a massless speed of 2cos w hops per step (1.911 at w = 0.3), so τ_s = c₀ℓ/c with c₀ = 2cos w; the speed called c is this renormalised one, at which light is posited to move (candidate).

**What kind of derivation this is.** The continuum limit is a theorem about the step; that the step is CO's (four components, palindromic order, Wilson half-shifts) rests on C5, C6, two exclusions by data and one candidate. The identification of the result with the electron is by its equation, not derived from the primitives.
