## Reading I13: a bounded ledger written out

*29 October 2026.*
- *The task ruled in Reading I12 §5, ruling 2: state which bound a pattern carries, what it does to spectra, and how it compares with the β₀ bounds, including whether a minimal length applies to a composite body's centre of mass or only to its constituents.*
- *Revised after an independent check, whose corrections are adopted. Ruled in §9.*
- *Nothing here is registered. Graded under Reading I7's grades (derived, lead, fitted), plus "restatement", "excluded" and "inert" as in Reading I12.*
- *Scripts and logs: `i13_lattice_spectra.py`, `i13_composite_bounds.py` (run with PYTHONDONTWRITEBYTECODE=1). Some numbers below come from the check's script.*

**In plain terms.**
- CO says any finite region holds only finitely many places. If a pattern's position takes values only at places, the textbook rule [x, p] = iħ fails, and position and momentum share a capped information ledger.
- But the bound is a crystal's, not a minimal length: a pattern can still sit sharply on one place, and what is capped is momentum.
- What this does to spectra depends entirely on how a pattern hops between places, which is Reading I11's question and Run 101's.
  - **On the plain hop,** the shift has the minimal-length form with the opposite sign. It is far too small for atoms, and the Crab excludes it across Run 100's ladder.
  - **If the borrowed relativity carries to the lattice,** as Run 101 finds when gravity is left free, the effect vanishes at the order the bounds test.
- A body's centre of mass does not sit on a place.
  - **If the hop belongs to the electrons and nucleons,** the body inherits a deformation suppressed by the square of their number, and no resonator bound reaches CO.
  - **If it belongs to the body as well,** the resonator bounds apply in full, though none is established for CO's sign.
  - The record does not yet say which.
- The possibility stock fails as a cap on where a pattern can be, since that rule breaks superposition. As a cap on information it allows about 150 nats, far more than any one-particle experiment resolves.

### 1. What the record says

| statement | source | status |
|---|---|---|
| "Every physical quantity is finite: counts, densities, energies, and the number of places in any finite region. Continuum mathematics is an approximation to finite counts." Whether the universe has finitely many places is open | ONTOLOGY_full §1 | principle, adopted 24 October |
| possibility is "held at places … hopping between related places"; a pattern is "possibility in transit"; space is who relates to whom; places can be relabelled freely. "In the engine, places form a 3D lattice" | ONTOLOGY_full §2 | primitives; the lattice is the engine's |
| "A scaleless substrate has no direct model, so the engine uses an averaged medium as its stand-in" | ONTOLOGY_full §5 | stated 23 October |
| a pattern hops on its place's ticks (R6); massive patterns obey −N⁴∇²ψ + m²N²ψ = ω²ψ (the continuum statement only) | R6; Reading I11 §2 | added, provisional |
| M1: a scalar pattern field sits on the same places as gravity. With Run 90's gravity free it closes and stays relativistic, ω²₂ = 1 and ω²₄ = 0 (K101j). With Run 91's gravity held fixed it is NOT FOUND (K101y), and the joint closure is open (Run 102). The a⁴ residual, −s⁶/90 along the axes for the minimal-range ultralocal stencil, is "the order at which closure fails, not a prediction" | Run 101 | M1 is a lead; the relativity is inherited from the borrowed boost relation |
| a plain lattice term for patterns is excluded on Run 100's ladder by the Crab (ℓ ≲ 5.9×10⁻³² m at S = ⅓); "only 4×10⁵ ≲ p_s ≲ 1.3×10⁷ survives" | Reading I11 ruling 1; §4.3 | ruled |
| the units of ordinary matter are electrons and nucleons, each committing on its own | Q4 | ruled, for route (b) |
| a free body between records is a pattern | Reading I6 ruling 1 | ruled |
| bodies move as point particles, action −m∫dτ (added); inertia = total energy, the Lorentz input (borrowed); composite bodies fall alike (R7, borrowed) | R7, R8 | added / borrowed |
| a pattern carries a stock q = 2E/E_pair, with E_pair = aħ/T_hold = aħc/(ħ_tℓ) | Reading I4 S-i | ruled 27 October |
| C1a: (2π)^{3/2}r_C³ = 2ħ_tℓ³, so ħ_t ≈ 10⁸⁴–10⁹² (P08's hop) or 10⁷⁴–10⁸⁵ (the engine's); a renaming | Run 97 | no test |
| a capacity per place, K, as a threshold (route (c)), not a cap; C4-β′ as a per-unit threshold | Reading I8 ruling 2; C4-β, C4-β′ | a lead; Runs 98–99 |

**What the record does not say:**
- **Whether a pattern's position takes values only at places.** The primitives hold possibility at places, which suggests it. R6 and Q4 are written in the continuum. Places are relational, so the suggestion implies discreteness, not a lattice.
- **How "finitely many places in any finite region" fits "a scaleless substrate".** The first implies a density of places, and so a scale. The two statements need reconciling (§8, choice 3).
- **How amplitude relates to the units a pattern carries.**
- **Which "massive pattern" R6's hop acts on in a bound body:** the units, or the body's centre of mass.

### 2. Candidates for the bound

**(a) Finitely many places in a region, with position defined to a place.**
- **The commutator cannot be canonical.**
  - If x has eigenvectors |n⟩ (position at places), then for every p,
$$
\langle n|[x,p]|n\rangle=(x_n-x_n)\langle n|p|n\rangle=0\neq i\hbar ,
$$
    so any discrete position spectrum excludes [x, p] = iħ, finite or not.
  - On a region's n places (with p projected onto the region) the trace form also holds: Tr[x, p] = 0 ≠ iħnd. Checked numerically (`i13_lattice_spectra.py` A; check A).
  - **Grade:** derived from position at places, given locally finite places. "No infinities" enters only by making places locally finite. So the argument holds off the engine whenever places are discrete, lattice or not.
- **What survives is the Weyl form.** Places related by a hop give a translation T with T x T† = x − ℓ. On n places in a ring, T and the phase operator form the finite Heisenberg group, UV = e^{2πi/n}VU (Weyl; Schwinger). The momentum spectrum is discrete, spaced by 2πħ/(nℓ), the box's Heisenberg floor (standard). It is bounded by |p| ≤ πħ/ℓ.
- **The bound is a crystal's, with the opposite sign to a minimal length.** With x = iħ∂_p on the Brillouin zone and P = (ħ/ℓ) sin(pℓ/ħ),
$$
[x,P]=i\hbar\cos\!\Big(\frac{p\ell}{\hbar}\Big)=i\hbar\sqrt{1-\Big(\frac{\ell P}{\hbar}\Big)^2}=i\hbar\Big(1-\tfrac12\frac{\ell^2P^2}{\hbar^2}+\dots\Big)
$$
  (the square-root form holds for |pℓ/ħ| < π/2).
  - This is the world-crystal commutator, Eq. (22) of Jizba, Kleinert and Scardigli (2010). Their Eq. (29) is ΔXΔP ≳ (ħ/2)(1 − ε²Δp²/2ħ²).
  - **The plain stencil's own pair** is the half-angle momentum P₂ = (2ħ/ℓ) sin(pℓ/2ħ), with P₂²/2m equal to the NN kinetic term and
$$
[x,P_2]=i\hbar\sqrt{1-\frac{\ell^2P_2^2}{4\hbar^2}}\ \ (\text{whole zone})\approx i\hbar\Big(1-\frac{\ell^2P_2^2}{8\hbar^2}\Big),
$$
    which gives β_comm = −ℓ²/(8ħ²), the same as the spectral β in §3 (check B).
  - **Compared with KMM's [x, p] = iħ(1 + βp²), β is negative.** A state on one place has Δx = 0, so there is no position floor. Momentum is bounded. In JKS's words, the relation "does not pose any lower bound on involved uncertainties".
- **So "Δx ≳ ℓ" (Reading I12 (C)) was a misreading.** Position-to-a-place resolves the position *spectrum* (eigenvalues ℓ apart). It is not a floor on Δx. It is an information bound: on n places,
$$
\ln n\ \le\ H(x)+H(p)\ \le\ 2\ln n
$$
  (Maassen and Uffink 1988; check K finds a minimum of ln 64 over 2,000 states on 64 places). This is the finite-region form of Reading I12's entropic ledger (B), and like it a restatement. Each entropy is capped and their sum has a floor: **this is the bounded ledger in its exact form.** It carries no new spectral effect.
- **What else it changes:** a momentum cap |p| ≤ πħ/ℓ in the foliation's frame. That is not boost-invariant, so it meets the objection of Reading I12 (C) unless the cap is invisible below the band edge. The stencil decides that (§3).

**(b) The possibility stock, q = 2E/E_pair.** It is finite and conserved, so it is the most direct "budget". Two readings:
- **(b1) Support: each place the pattern occupies holds at least one of its units.** Amplitudes √P would imply this; in Reading I4, A5 is a route to S-ii, so pairing it with S-i is a new statement. A pattern then occupies at most q places, which is a *maximal* extent, not a minimal one:
$$
V_{\max}=q\,\ell^3=\frac{2E\,\hbar_t\,\ell^4}{a\hbar c}\ \overset{\text{C1a}}{=}\ (2\pi)^{3/2}r_C^3\,\frac{\ell}{a\,\bar\lambda_C},\qquad \bar\lambda_C=\frac{\hbar c}{E}.
$$
  It would give Kempf's α-type floor, Δp ≳ ħ/V_max^{1/3}.
  - **It breaks superposition.** "At most q places" is not a linear constraint: two allowed states on disjoint supports superpose to a state on 2q places. As a rule on states it fails linearity, whatever ħ_t is. This agrees with Reading I8's warning that "the places its pattern spans" depends on the state and signals.
  - **Under C1a it is also excluded by data, over most of the range.** For an Rb-87 atom at r_C = 51 μm, a = 1, on the engine's hop at p_s's lower bound (10^{3.21} ℓ_P), V_max = 2.2×10⁻²⁶ m³. That is about 13 decades below a single atom's coherence volume, about 10⁻¹³ m³: two packets of coherence length ħ/σ_p ≈ 35 μm at 50 pK (Kovachy et al. 2015). V_max ∝ ℓ, so it reaches 9.4×10⁻²⁰ m³ at Run 100's top hop and 1.9×10⁻¹⁴ m³ at I11's ceiling, where the exclusion becomes marginal.
  - **Under C1b,** with N_V = q/P∞, V_max = P∞(2π)^{3/2}r_C³ ≳ 10¹⁰ m³, which is never reached.
  - **Grade:** excluded as a rule on states (it fails linearity); under C1a also by data across most of the hop's range.
- **(b2) A cap on distinguishable states.**
$$
\frac{q}{I_B}=\frac{R_{\rm hold}}{\pi a\,R},\qquad I_B=\frac{2\pi ER}{\hbar c},\qquad R_{\rm hold}=\hbar_t\,\ell\ \gtrsim10^{43}\ \text{m (C1a)} .
$$
  - If each unit is a bit, q exceeds Bekenstein's count by more than 40 decades.
  - If q caps distinguishable states, the information is ln q ≈ 130–160 nats. That is far below Bekenstein's (about 10¹³ nats for an electron in 1 m), but above anything a single-particle experiment resolves.
  - **Either way it is inert.** Its time form, E/(aħ) renewals, is already the Margolus–Levitin count (Reading I12).
  - **Grade:** inert.

**(c) Others the record offers.**

| candidate | what it bounds | what else it changes | status |
|---|---|---|---|
| capacity per place K (C4-β) | a threshold density for route (c), not a cap | collapse-type noise at threshold surfaces; no commutator change | a lead with its own runs (98–99); not a ledger bound |
| C4-β′ | a per-unit threshold, q ≥ 2ħ_tP∞ ⟺ E ≳ aP∞ħc/ℓ (Reading I8) | inert per unit, signalling per body (Run 95) | a factor aP∞ (≳ 10²⁶) above (a)'s momentum cap; not a ledger bound |
| the vacuum's hold under C1a | r_C | as a floor on states, excluded by atomic sizes; as noise on route-(b) records, Reading I12 §2 | settled in I12 |
| the renewals, E/(aħ) per unit time | aħ/(mc) | none beyond relativistic quantum theory | a restatement unless a ≫ 1 (I12) |
| finitely many places in the universe (open) | Δp ≳ πħ/L_universe (α-type) | a closed space; the CMB bounds its size | unmeasurable as a floor (I12: ħH₀/c ≈ 8×10⁻⁶¹ kg m s⁻¹) |

**The leading candidate is (a)**, read correctly: position with a discrete spectrum, the Weyl form in place of the canonical commutator, and the Maassen–Uffink ledger on any finite region.

### 3. What (a) does to spectra

**The commutator does not fix the spectrum; the hop does.** The same Weyl pair carries any kinetic stencil K(p). Three cases, for a harmonic oscillator (ħ = m = ω = 1, spacing h = ℓ/√(ħ/mω)). Computed with FFT operators (`i13_lattice_spectra.py` C–D) and independently with finite-difference matrices (check C):

| stencil | K(p) | level shift δE_n/ħω | KMM-equivalent β |
|---|---|---|---|
| plain nearest neighbour | (1 − cos ph)/h² = p²/2 − h²p⁴/24 + … | −(h²/16)(n² + n + ½), to 0.06% at h = 0.1 | **β_eff = −Sℓ²/(8ħ²)** (S = 1 along an axis) |
| improved through h² | (15 − 16cos ph + cos 2ph)/(12h²) = p²/2 − h⁴p⁶/180 + … | δE₀ = −h⁴/96 (−0.0104 h⁴ numerically) | 0 at order ℓ² |
| exact p²/2 on the zone (nonlocal) | p²/2, \|p\| < π/h | exponentially small | 0 to all orders |

So the discreteness of position by itself has no power-law effect on a bound state's levels. Every power-law effect comes from the stencil's dispersion.

**KMM, for comparison.** The exact one-dimensional spectrum (Kempf, Mangano and Mann 1995) is E_n = ħω[(n + ½)√(1 + γ²/4) + (n² + n + ½)γ/2]. To first order,
$$
\delta E_n^{\rm KMM}=\hbar\omega\,\frac{\gamma}{2}\Big(n^2+n+\tfrac12\Big),\qquad \gamma=\beta m\hbar\omega .
$$
The plain stencil matches this with β → −Sℓ²/(8ħ²). The exact KMM spectrum at γ = −h²/8 differs at O(h⁴) (check C). In β₀ units:
$$
\beta_0^{\rm eff}=-\frac{S}{8}\Big(\frac{\ell}{\ell_P}\Big)^2 .
$$

**Hydrogen-like levels** (Coulomb; the unit is the electron).
- **Plain stencil.** δH = −α₂p⁴/(2m), with α₂ = Sℓ²/12 (ħ = c = 1) and ⟨p⁴⟩₁ₛ = 5(ħ/a₀)⁴ (checked numerically). The 1s state is isotropic, so S = ⟨Σn_i⁴⟩ = 3/5:
$$
\frac{\delta E_{1s}}{E_R}=-\frac{5S}{12}\Big(\frac{\ell}{a_0}\Big)^2=-\frac14\Big(\frac{\ell}{a_0}\Big)^2 .
$$
  - On the engine's hop at p_s's lower bound it is −9.7×10⁻⁴⁶ to −6.1×10⁻⁴⁴; on P08's, −2.3×10⁻⁵⁰.
  - At the Crab ceiling, which bounds Sℓ², it is at most −1.7×10⁻⁴³.
  - The 1S–2S interval is known to about 4×10⁻¹⁵.
- **Run 101's residual** (E² = m² + p² − α₄p⁶, α₄ = S₆ℓ⁴/90, with S₆ = 3/7 for 1s). Without the zone edge ⟨p⁶⟩₁ₛ diverges (the Coulomb cusp), so
$$
\frac{\delta E_{1s}}{E_R}\approx-\frac{32S_6}{90\pi}\Big(\frac{\ell}{a_0}\Big)^3\frac{\ell}{\bar\lambda_e}\ln\frac{\pi\bar\lambda_e}{\ell},
$$
  about −4×10⁻⁸³ on the engine's hop and −7×10⁻⁹⁶ on P08's (at S₆ = 1). 98% of it comes from p > m_ec, beyond the Schrödinger tail's validity, so this is an order of magnitude only, illustrative.
- **"No infinities" at r = 0.** The Coulomb potential sampled at places acts like a nuclear size ℓ. It is masked by the proton's 0.84 fm, by (ℓ/r_p)² ≈ 10⁻³⁴.

**Oscillators with the residual** (improved stencil):
$$
\delta E_0=-\frac{S_6}{96}\Big(\frac{\ell^2m\omega}{\hbar}\Big)^2\hbar\omega ,
$$
second order in what KMM's β is first order in.

**What this means for the ledger.**
- **On the plain stencil,** CO's places give a negative β₀ of size (S/8)(ℓ/ℓ_P)².
  - **Where it survives:** on the engine's hop at p_s's lower bound (10^{2.31}–10^{3.21} ℓ_P, conditional since Reading I6) this is 1.7×10³–3.3×10⁵. That survives the Crab (3.3×10⁵ < 5.55×10⁵, the Crab's bound in β₀ terms for S = ⅓).
  - **Where it is excluded:** on Run 100's ladder it is 10⁷–6×10¹⁸, which the Crab excludes (Reading I11). On P08's hop it is 0.04–0.13.
- **On Run 101's closure,** the borrowed boost relation, carried to the lattice by M1 (K101j, with Run 90's gravity free), gives β₀ = 0 at the order the bounds test. The first effect is the ℓ⁴ term, whose coefficient depends on the stencil. With Run 91's full gravity this is open (Run 102).
- **Grade:**
  - **Derived:** the commutator argument, the Weyl form, the sign, and the map from stencil to β₀ (checked numerically twice).
  - **Conditional:** which stencil applies, on Run 101's M1, a lead.
  - **Not what CO's places give:** the minimal-length (KMM, β > 0) form. No statement in the record gives a positive β. Reading I6 ruling 2 places *commitments* as sharply as interactions resolve, and route (b)'s r_C is a noise on records, not a floor on states (Reading I12 §2).

### 4. The composite body ("soccer-ball") question

**A body's centre of mass is not at a place.** For units at places x_i ∈ ℓℤ³, X = Σm_ix_i/M moves in steps of m_iℓ/M. For N identical units the steps are ℓ/N, and with electrons and nucleons of incommensurate masses the set of values is dense. So candidate (a)'s place resolution does not apply to X directly. The body inherits whatever its units carry.

**What it inherits.** Each unit carries the quartic term H_i = p_i²/(2m_i) + (β_i/3)p_i⁴/m_i: KMM to first order in canonical variables, or the plain stencil with β_i = −Sℓ²/(8ħ²). Write p_i = μ_iP + π_i, with μ_i = m_i/M and Σπ_i = 0:
$$
\sum_i\frac{\beta_i}{3m_i}\big\langle(\mu_iP+\pi_i)^4\big\rangle=\frac{P^4}{3M}\sum_i\mu_i^3\beta_i\;+\;2P^2\sum_i\frac{\beta_i\mu_i^2\langle\pi_i^2\rangle}{m_i}\;+\;\big(\text{terms independent of }P\big)
$$
Odd terms vanish for internal states with ⟨π_i⟩ = ⟨π_i³⟩ = 0.
- **The P⁴ term** gives
$$
\beta_{\rm com}=\sum_i\mu_i^3\beta_i\ \xrightarrow{\ N\ \text{identical}\ }\ \frac{\beta}{N^2}.
$$
  This is the result of Quesne and Tkachuk (2010), checked numerically with two and three unequal units (`i13_composite_bounds.py` §1; check G).
- **The P² term** shifts the body's inertia by a relative amount 4Σβ_iμ_i⟨π_i²⟩. That is of order β⟨π²⟩, set by the body's internal motion: an internal-state dependence of inertia. For nucleons in nuclei (⟨π⟩ ~ 200 MeV/c) on the engine's hop it is (ℓ⟨π⟩/ħ)² ~ 10⁻³⁴, against MICROSCOPE's 10⁻¹⁵. Under Run 101 (K101j) it is zero at this order.
- **A normal mode,** as the resonator bounds use: take u_i = φ_iq with max|φ| = 1, M_eff = Σm_iφ_i² and P = M_eff q̇. Then
$$
\beta_{\rm mode}=\beta\,\frac{\sum_im_i^3\phi_i^4}{M_{\rm eff}^3}=c_\phi\,\beta\Big(\frac{m}{M_{\rm eff}}\Big)^2,\qquad c_\phi=\frac{\sum\phi^4}{\sum\phi^2}\le1,
$$
  with c_φ = ¾ for a bar's first longitudinal mode and ⅜ for a BAW trapped overtone (Gaussian sideways, sinusoidal through the thickness). Nucleons dominate Σm³; electrons contribute (m_e/m_N)³ per unit.
- **The equivalence principle.** Tkachuk (2013) shows that KMM keeps the weak equivalence principle only if √β m is the same for every body. Per-unit β with one ℓ gives β_com M² = βΣm_i³/M ≈ βm_N², so √β M is the same for every body to about 10⁻³ (its electron and binding fractions). The resulting difference in free fall carries a further factor of about β₀(m_Nv/M_Pc)², which is negligible. A body-level β with no mass dependence breaks the principle; that is the form Ghosh (2014) bounds at 10²¹.

**What the record decides, and what needs a ruling.**
- **Q4** names the units (for route (b)).
- **R7** excludes a body-level β that does not depend on mass. It allows a per-unit β, or a body-level β ∝ 1/M², so it constrains the form of β, not which pattern carries it.
- **R8** (−m∫dτ; inertia = total energy) is exactly relativistic for a body. It excludes any body-level p⁴ term: fully under reading (ii) below, and at β/N² under (i) unless M1 holds. So R8 points to "no deformation of the body", which is M1's outcome, rather than to (i) over (ii).
- **Read literally,** R6 ("massive patterns obey …") together with Reading I6 ruling 1 ("a free body … is a pattern") points to (ii).
- **So the record does not decide** whether the hop belongs to the units only (i), or also to a body's centre of mass (ii). A ruling is needed (§8, choice 2).
- **Open below the units:** if the hop acts on quarks, Σμ³ for a nucleon is ill-defined, since most of its mass is field energy. Q4 settles the unit only for route (b).

### 5. The β₀ bounds, verified, with the right scaling

Convention: β = β₀/(M_Pc)², Δx_min = √β₀ ℓ_P. "Per unit" means the published bound × (M_eff/m_N)², with c_φ = 1. That is the tightest choice; c_φ < 1 loosens it.

| source | system, mass | as published | composites; sign | per unit (§4) |
|---|---|---|---|---|
| Das and Vagenas, PRL 101, 221301 (2008) | Lamb shift; Landau levels; STM current (electrons) | β₀ < 10³⁶; 10⁵⁰; 10²¹ (STM at an assumed precision) | single particles | as published |
| Ali, Das and Vagenas, PRD 84, 044013 (2011) | Landau levels; J/ψ as an oscillator; Lamb shift | α₀ < 10²³; 10¹⁷; 10¹⁰ on the **linear** GUP; no β₀ bound | single particles; charmonium as a whole | β₀ ≈ 4α₀² < 4×10³⁴ from J/ψ is a translation, not their bound; J/ψ is not a Q4 unit |
| Marin et al., Nat. Phys. 9, 71 (2013) | AURIGA bar, 2300 kg Al, first longitudinal mode ~900 Hz | β₀ < 3×10³³ (as quoted) | the mode as one oscillator; **one-sided by construction**: an upper limit on E_min, which β < 0 lowers (an inference from the method, as Bawaj et al. describe it; the original not fetched) | < 1.4×10⁹³ (M_eff = M/2, an assumption) |
| Bawaj et al., Nat. Commun. 6, 7503 (2015) | DPO 0.033 g, 5636 Hz; Si wheel 20 μg, 141.8 kHz, 4.3 K; SiN membrane 20 ng, 747 kHz (also a 77 μg wheel at 5×10¹³) | β₀ < 3×10⁷; 6×10¹²; 2×10¹⁹ (Δω, 95% CL) | centre-of-mass or reduced coordinates; the N⁻² argument discussed, not adopted; upper limits on a fitted coefficient, negative β₀ not addressed | < 1.2×10⁵²; 8.7×10⁵⁰; 2.9×10⁵¹ |
| Bushev et al., PRD 100, 066020 (2019) | sapphire split bar, 0.3 kg; quartz BAW 10 mg (total masses, not M_eff) | β₀ < 5×10⁶; quartz about 4×10⁴, an estimate; pendulum data (Atkinson 1936) "β₀ ≪ 1", not reliably established | the mode as one oscillator; no sign stated | < 1.6×10⁵⁹ at 0.3 kg (an upper estimate); quartz estimate < 1.5×10⁴⁸ |
| Campbell, Tobar, Goryachev and Galliou, arXiv:2304.00688 (preprint, dated 17 January 2024) | quartz BAW plate, B₃,₀,₀ at 5.505 MHz, M_eff 8.5 mg, 4 K | β₀ < 62.4 (3σ; one table caption says 5σ) | the centre-of-mass application is "still unclear"; possible suppression by constituent number; a mass-dependent β₀ raised. The GUP shift "cannot be decoupled from … the crystal's inherent non-linearity" | < 1.6×10⁴⁵ |
| Kumar and Plenio, Nat. Commun. 11 (2020), doi:10.1038/s41467-020-17518-5; arXiv:1908.11164 | pendulum (Smith 1964), Bawaj, Bushev | for β₀ = 1 with suppression N^{−α}: α > 0.07 (pendulum); the oscillator data give α > −0.33 and −0.25 | α treated as free | N² is α = 2, far inside every bound they quote |

**CO's numbers on the same scale (plain stencil, negative sign):**

| CO case | \|β₀\| |
|---|---|
| engine hop at p_s's lower bound, 10^{2.31}–10^{3.21} ℓ_P | 1.7×10³–3.3×10⁵ |
| Run 100's ladder (p_s from 2.2×10⁸ to 4.3×10¹⁹, a = 1) | 9.5×10⁶ up to 5.6×10¹⁸ |
| P08's hop | 0.04–0.13 |
| the Crab's bound (I11's ceiling, S = ⅓) | 5.55×10⁵ |
| Run 101's closure (M1, K101j) | 0 at order ℓ²; the first effect at order ℓ⁴ |

**Comparison.**
- **At p_s's lower bound,** the plain stencil (|β₀| ≤ 3.3×10⁵) sits below every per-unit bound, the Crab's (5.55×10⁵) included.
- **On Run 100's ladder** (10⁷–6×10¹⁸), the Crab excludes it (Reading I11).
- **Under choice 2(i) (per unit),** every resonator bound, rescaled, lies above 10⁴⁵, so Reading I12's conditional tension with Campbell et al. is removed.
- **Under choice 2(ii) (the body carries the hop too),** the tension stands: |β₀| up to 3.3×10⁵ at p_s's lower bound, against 62.4.
  - It is **not established for CO's sign.** No oscillator paper states a limit on negative β₀. AURIGA's method cannot constrain it. Campbell et al. note that the GUP shift is degenerate with the crystal's own nonlinearity.
  - P08's plain stencil (0.04–0.13) sits near the pendulum's "β₀ ≪ 1" and near Kumar and Plenio's pendulum edge.
  - Reading (ii) also sits uneasily with R8, which makes a body's motion exactly relativistic.
- **Under Run 101's closure,** neither reading bites: β₀ = 0 at the tested order.

### 6. Grades

| item | grade | conditional on |
|---|---|---|
| (A) no canonical commutator once position is discrete; the Weyl form survives | **derived** | position at places, given locally finite places (lattice or not) |
| (A′) the Maassen–Uffink ledger, ln n ≤ H(x) + H(p) ≤ 2 ln n, on n places | **a restatement**: the finite-region form of I12's (B) | (A) |
| (B) the bound is a crystal's: β < 0, no Δx floor, momentum capped at πħ/ℓ | **derived; a restatement** of lattice quantum mechanics (Jizba, Kleinert and Scardigli 2010) | (A) |
| (C) the spectral effect lies wholly in the stencil: β₀^eff = −(S/8)(ℓ/ℓ_P)² on the plain stencil, 0 on Run 101's closure | **derived** (checked twice numerically); which stencil applies is **conditional on Run 101's M1, a lead** | (A); M1 |
| (D) the plain stencil for matter | **excluded on Run 100's ladder** (Reading I11); **survives the Crab at p_s's lower bound** | the hop's scale |
| (E) β_com = Σμ_i³β_i; β_mode = c_φβ(m/M_eff)²; √β M the same for every body to about 10⁻³ | **derived**; a restatement of Quesne and Tkachuk (2010) and Tkachuk (2013), in CO's units | a per-unit hop (choice 2) |
| (F) the resonator bounds, rescaled per unit, do not reach CO | **arithmetic on published bounds** | choice 2(i) |
| (G) the stock as support, q places at most | **excluded**: it fails linearity; under C1a also by data across most of the hop's range (about 13 decades at p_s's lower bound) | a new statement (amplitude carried by units) |
| (H) the stock as an information cap | **inert** (as bits, far above Bekenstein; as states, ln q ≈ 130–160 nats, beyond any single-particle test) | — |
| a KMM minimal length (β > 0) from CO | **not in the record**; it would need a new statement | — |

**What is new, honestly.**
- **New to the record:**
  - CO's discrete places force a deformed commutator, of the crystal kind, not the minimal-length kind. So "Δx ≳ ℓ" in Reading I12 (C) was a misreading.
  - The exact bounded ledger is Maassen–Uffink's, a restatement.
  - The ledger's spectral content reduces to Reading I11's and Run 101's dispersion question.
  - Under a per-unit hop, Reading I12's tension with the oscillator bounds disappears.
  - The stock's support reading fails linearity.
- **Not new to physics:** each step is known (finite Weyl pairs; the world crystal; Maassen–Uffink; the N⁻² composite scaling; the equivalence-principle condition).
- **The bounded ledger yields no new test.** Its only live consequence is Run 101 Part F's ℓ⁴ residual, which Run 102 and the stencil question already carry.

### 7. What this means
- **A bounded ledger exists in CO.** Once position is discrete the canonical commutator fails, and on any finite region the position and momentum entropies obey ln n ≤ H(x) + H(p) ≤ 2 ln n. That bound is a lattice's: it caps momentum, not position.
- **Its effect on spectra is the hop's dispersion, and nothing else.** That is Reading I11's question (the plain stencil is excluded on Run 100's ladder but survives at p_s's lower bound) and Run 101's (relativistic through a² under M1, K101j).
- **At the order the β₀ bounds test,** the borrowed boost relation carried to the lattice by M1 gives β₀ = 0. A plain stencil gives β₀ < 0.
- **A body's centre of mass inherits its units' deformation, suppressed as Σμ³ ≈ 1/N²,** if the hop belongs to the units. Q4 points that way. R7 constrains only the form, R8 asks that the body not be deformed at all, and R6 read literally points the other way. The record does not decide.
- **The possibility stock does not supply the floor.** As support it fails linearity; as information it is inert.

### 8. Choices for a ruling
1. **Record the finding (§7).**
   - The bound from places is a crystal's. Its exact form is the Maassen–Uffink ledger on a region's places.
   - Its spectral content is the stencil's dispersion, β₀^eff = −(S/8)(ℓ/ℓ_P)² on the plain stencil and 0 under M1 (K101j).
   - The stock readings are set aside: (b1) excluded, (b2) inert.
   - Reading I12's ruling 2 closes with grade derived / restatement, not lead.
   - **A dated note on Reading I12** (not an overwrite), *29 October, after Reading I13*:
     - "Δx ≳ ℓ" in (C) and its table is superseded: places give a discrete position spectrum, β < 0 and no Δx floor.
     - The map "β₀ ≈ (ℓ/ℓ_P)² ≈ 4×10⁴–3×10⁶" is corrected to the plain stencil's β₀ = −(S/8)(ℓ/ℓ_P)², 1.7×10³–3.3×10⁵ at p_s's lower bound, and 0 under M1.
     - The row "J/ψ levels (Ali, Das and Vagenas 2011), β₀ < 10³⁴" is corrected: that paper bounds α₀ < 10¹⁷ on the linear GUP, and 4α₀² is a translation.
     - The "conditional tension" with Campbell et al. is removed under choice 2(i). Under 2(ii) it stands, and is not established for β₀ < 0.
2. **Which pattern R6's hop acts on in a bound body:**
   - **(i) the units** (electrons and nucleons, as in Q4): the centre of mass inherits β_com = Σμ³β, and the resonator bounds do not reach CO;
   - **(ii) any pattern, including a body's centre of mass** (R6 with Reading I6 ruling 1, read literally): the resonator bounds apply in full, though none is established for CO's negative sign. This sits uneasily with R8.
   - **Before ruling, decide whether R8's exact relativity for bodies is meant to force an M1-type closure** for every pattern. If it is, a body carries no deformation under either reading, and choice 2 matters only if Run 102 fails to close matter with Run 91's full gravity.
3. **Whether position takes values only at places,** outside the engine as well, or the record stays agnostic.
   - The trace argument needs only discrete places, so (A), (A′) and (B) hold off the engine whenever places are discrete. Only (C)'s stencil is specific to the engine.
   - Ruling for discreteness means reconciling "finitely many places in any finite region", which implies a density of places and so a scale, with the 23 October "scaleless substrate". For example:
     - the substrate is scaleless only in the sense of having no preferred length *above* the place density; or
     - "finitely many places per region" is read as a statement about records, not about the substrate.
   - Ruling for agnosticism leaves (A)–(B) conditional.

### 9. Rulings (29 October; Allen: "do as you recommend")
1. **§7's finding is recorded,** with the dated note on Reading I12 listed in choice 1. Reading I12's ruling 2 closes with grade derived / restatement, not lead.
2. **Which pattern R6's hop acts on in a bound body is left open until Run 102.** If matter closes with Run 91's full gravity, bodies carry no deformation under either reading.
3. **Whether position takes values only at places is left open,** pending Allen's account of how "finitely many places in any finite region" and the "scaleless substrate" fit together.

### Sources
- S. Das and E. C. Vagenas, *Phys. Rev. Lett.* 101, 221301 (2008); [arXiv:0810.5333](https://arxiv.org/abs/0810.5333). GUP with [x_i, p_j] = iħ(δ_ij + βδ_ijp² + 2βp_ip_j); β₀ < 10³⁶ (Lamb), 10⁵⁰ (Landau), 10²¹ (STM).
- A. F. Ali, S. Das and E. C. Vagenas, *Phys. Rev. D* 84, 044013 (2011); [arXiv:1107.3164](https://arxiv.org/abs/1107.3164). Linear GUP; α₀ bounds only.
- F. Marin et al., *Nat. Phys.* 9, 71 (2013). β₀ < 3×10³³ as quoted in [arXiv:2202.02044](https://arxiv.org/pdf/2202.02044); the method as described by Bawaj et al.; the original not fetched. AURIGA's parameters (2300 kg, ~900 Hz) from [arXiv:1606.04581](https://arxiv.org/pdf/1606.04581).
- M. Bawaj et al., *Nat. Commun.* 6, 7503 (2015); [arXiv:1411.6410](https://arxiv.org/abs/1411.6410). Table I. A later review attributes the strongest bound to "the lighter oscillator"; the paper assigns it to the heaviest, the DPO.
- P. A. Bushev et al., *Phys. Rev. D* 100, 066020 (2019); [arXiv:1903.03346](https://arxiv.org/abs/1903.03346).
- W. M. Campbell, M. E. Tobar, M. Goryachev and S. Galliou, [arXiv:2304.00688](https://arxiv.org/abs/2304.00688) (preprint).
- S. P. Kumar and M. B. Plenio, *Nat. Commun.* 11 (2020), doi:10.1038/s41467-020-17518-5; [arXiv:1908.11164](https://ar5iv.labs.arxiv.org/html/1908.11164).
- C. Quesne and V. M. Tkachuk, *Phys. Rev. A* 81, 012106 (2010); [arXiv:0906.0050](https://ar5iv.arxiv.org/html/0906.0050).
- V. M. Tkachuk, [arXiv:1301.1891](https://ar5iv.arxiv.org/html/1301.1891) (√β_im_i = γ, Eqs. 17–20; journal not confirmed).
- P. Jizba, H. Kleinert and F. Scardigli, *Phys. Rev. D* 81, 084030 (2010); [arXiv:0912.2253](https://arxiv.org/abs/0912.2253), Eqs. (22), (29).
- H. Maassen and J. B. M. Uffink, *Phys. Rev. Lett.* 60, 1103 (1988). From standard listings; checked numerically, not fetched.
- G. Amelino-Camelia, "Planck-scale soccer-ball problem: a case of mistaken identity", [arXiv:1407.7891](https://ar5iv.arxiv.org/html/1407.7891). Consulted for the framing.
- [The deformation parameter of the GUP (review), arXiv:1905.00287](https://arxiv.org/html/1905.00287).
- From standard listings, not re-fetched:
  - A. Kempf, G. Mangano and R. B. Mann, *Phys. Rev. D* 52, 1108 (1995);
  - L. N. Chang et al., *Phys. Rev. D* 65, 125027 (2002);
  - C. G. Parthey et al., *Phys. Rev. Lett.* 107, 203001 (2011);
  - S. Ghosh, *Class. Quantum Grav.* 31, 025025 (2014);
  - T. Kovachy et al., *Nature* 528, 530 (2015) (in the record).
