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
| C1 | a commitment, on completing, engages ħ of adjacent free possibility (or, through a channel, a quantum in transit, C8), releases what it held, and adds one to its count n; it halts when none is adjacent (ruled) |
| C2 | a commitment repeats at ω = (mc²/ħ)(1 − h) (ruled) |
| C3 | each repeat keeps δħ as record (candidate); dR/dt ≥ 0 |
| C4 | every commitment engages ħ; mass is the repeat rate, ω₀ = mc²/ħ (ruled) |
| C5 | a pattern in transit carries a phase θ advancing by one cycle per repeat (ruled; the matter sector's one addition) |
| C6 | the walk's step is U = A_x A_y A_z F(θ_m) A_z A_y A_x, with A_j = S_j⁺ F(w) S_j⁻ F(−w): S_j⁺ moves the α_j = +1 part one place forward, S_j⁻ the α_j = −1 part one place back, F(a) = exp(−iβa) a turn of the internal state, θ_m = mcℓ/ħ per step (flip ruled; half-shift Wilson form candidate, w ≳ 0.3, run L1b; palindromic order needed, sequential excluded, run L1) |
| C7 | the first possibility, all free in few places, puts every place over capacity; the first commitments are unordered (ruled) |
| C8 | a commitment may engage a quantum in transit through a channel; which engager takes it is drawn from \|a\|² at the engagers' places (candidate; the \|a\|² draw identified, Born; the coupling and pointer basis imported) |

**Constants of the theory's own:** δ, P_max, Λ (Λ from data); P_b fixed by the degree if the candidate reading holds. **Measured:** G, c, ħ, 1/137, the masses. **Bound:** ℓ ≲ 1.3 × 10⁻³¹ m (needed, Crab PeV electrons), so δ ≳ 2 × 10⁻⁷.

## 2. One derivation: the weak-field metric

**Step 1: the static field equation.** At rest, every place's flows balance its sink. By P1 the net inflow to place i is κ Σ_j ln(P_free,j / P_free,i); by C3 and C2 the sink of a pattern of mass M is δħ per repeat at ω₀ = Mc²/ħ, δħ·ω₀ = δMc², i.e. δMc²/ħ quanta per unit time. With the conductance of a hop moving one quantum per tick, κ = ħ/τ per relation, and the lattice Laplacian Σ_j(f_j − f_i) → ℓ²∇²f (cubic lattice, d = 6; other networks change this by a factor of order one),

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

**What the derivation uses, in one line.** Ratio hopping (ruled), one quantum per hop (candidate), the fixed share δħ (candidate), C2's clock (ruled), the route factor (ruled, given the occupancy, candidate), and P = P∞ at a place (identification). Beyond the weak field, Lovelock's theorem (given its hypotheses) supplies the exterior; that step uses an imported theorem.
