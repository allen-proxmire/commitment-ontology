## Reading I15a: can a covariant theory carry CO's static departures from GR? (T-I15a″, recorded as a reading)

*30 October 2026. Planned as a registered test (Reading I15 §8). Its scope and pre-registration were built (`testI15a/`) and checked before hashing (`checkPreI15a/REPORT.md`); every verdict-bearing output was already fixed by the record and the literature, so the test is recorded as a reading (option (ii)), with nothing hashed or run. The identity and constraint of §3 were then checked independently (`checkI15a_identity/REPORT.md`, 163 exact checks), whose corrections are adopted; the pre-check version is `READING_T-I15a_v1_precheck.md`.*

**In plain terms.** CO's static field outside a body is not GR's with only the clock rate changed; the spatial part changes too. At weak field, among covariant theories in which all matter feels one metric, CO's departure from GR cannot come from ordinary scalar or gauge fields, coupled to matter in any conformal way. It needs a ghost (a field of negative energy), a scalar sector of an unusual kind, or a coupling of matter to a vector field. The best-known theory of the last kind, TeVeS, gives the opposite sign of CO's departure.

### 1. The target (Run 67 §1)
$$
ds^2=-N^2dt^2+N^{-2}\big[dr^2+(r^2-2mr)\,d\Omega^2\big],\qquad N=(1+\varepsilon)\sqrt{1-2m/r}-\varepsilon,\qquad M_K=(1+\varepsilon)m .
$$
- **Exact PPN pair.** In areal radius R, with w = 1/R: −g_tt = 1 − 2M_Kw + (M_K² − 2ε(1+ε)m²)w² + …, and g^{RR} = 1 − 2M_Kw − (4ε + 3ε²)m²w² + …. So γ = 1 and
$$
\beta-1=-\frac{\varepsilon}{2(1+\varepsilon)}\quad\text{exactly}
$$
  (series, checked at four values of ε), confirming Run 66's formula beyond its numerical check (K66e).
- **Not lapse-only.** The spatial metric carries N⁻²; against Schwarzschild at the same r, g_CO = −Ω²n²dt² + Ω⁻²h_S with Ω = N/n, and g^{RR}[w²] ≠ 0. "Lapse-only" holds in the medium's variables, not in the metric matter feels (Run 69 says so).
- **A structural fact.** CO's metric is exactly an aligned TeVeS-type image of Schwarzschild, g_CO = e^{−2ψ}g_S − 2 sinh(2ψ) U U with U = n dt and ψ = ln Ω. That ψ is not harmonic on Schwarzschild; with harmonic ψ the same map gives β = 1.

### 2. What is known
- **Conformally coupled scalars, charge set by the source** (Damour–Esposito-Farèse, Eqs. 1.4a,b):
$$
\gamma-1=-\frac{2\alpha_0^2}{1+\alpha_0^2},\qquad \beta-1=\frac{\beta_0\alpha_0^2}{2(1+\alpha_0^2)^2},
$$
  so γ = 1 forces α₀ = 0 and β = 1. A star whose charge is not set by weak-field matter (spontaneous scalarisation, β₀ ≲ −4.34) can still give γ = 1 with β − 1 = ½β₀α_A².
- **Perturbative Horndeski** (Hohmann 2015, a restricted class on a constant background, with sourced charge): γ = (ω+1)/(ω+2) and β = 1 + (ω + τ − 4ωσ)/[4(ω+2)²(2ω+3)]; γ = 1 is the limit ω → ∞, in which β → 1 (inferred from the formula).
- **Einstein–aether and khronometric gravity:** β = γ = 1 for every coupling (Jacobson 2008; Blas and Lim 2014, Eq. 26).
- **TeVeS:** the aligned branch gives GR's β and γ; the non-aligned branch gives γ = 1 with β − 1 ≥ κ/(8π) + K/4 > 0 (Giannios 2005, Eqs. 56–57), the opposite sign to CO's.
- **Run 71 (K71a):** CO's exterior breaks the null energy condition everywhere outside, ρ + p_r = −(3ε/4π)(1 + 2ε/3) m²/r⁴ at leading order.

### 3. An identity and a constraint (derived; checked independently)
**The identity.** Take a static, spherical metric, ds² = −A dt² + dR²/h + R²dΩ², with two-term expansions A = 1 − 2Mw + K₂w² + …, h = 1 + h₁w + h₂w² + … that can be differentiated term by term. Then
$$
G^t{}_t=-h_2w^4,\qquad G^r{}_r=(h_1+2M)w^3+\big(h_2+2Mh_1-2K_2+4M^2\big)w^4,\qquad G^\theta{}_\theta=-\tfrac12(h_1+2M)w^3+\big(2K_2-3M^2-\tfrac32Mh_1-h_2\big)w^4 .
$$
With γ = 1 (h₁ = −2M; essential), and K₂ = 2(β − 1)M²,
$$
E_A[w^4]\equiv\big(G^t{}_t-G^\theta{}_\theta\big)[w^4]=-4(\beta-1)M^2,\qquad \mathrm{NEC}_r[w^4]\equiv\big(G^r{}_r-G^t{}_t\big)[w^4]=2h_2-2K_2 .
$$
No field equations are used. The w⁴ coefficients are unchanged under R → R + c + O(1/R).

**The constraint.** Take a ghost-free minimally coupled scalar (any P(X, φ), P_X > 0) and gauge fields (any L(F), Maxwell's sign), with matter coupled to g̃ = A²(φ)g, or with a disformal term B(φ, X)∂φ∂φ smooth at X = 0. In the Einstein frame, a static P(X, φ) scalar has T^t_t = T^θ_θ and NEC_r ≥ 0, and a radial electric field gives NEC_r = 0 and E_A ≤ 0. A conformal factor σ = s₂w² + … shifts them at w⁴ by δNEC_r = −12s₂ and δE_A = −4s₂ (δNEC_r = 3δE_A, at w⁴ only). So in the matter frame
$$
\mathrm{NEC}_r-3E_A\ \ge\ 0\quad\text{at }w^4,\qquad\text{equivalently}\qquad \mathrm{NEC}_r[w^4]\ge-12(\beta-1)M^2,\qquad g^{RR}[w^2]+4(\beta-1)M^2\ge0 .
$$
The bound is sharp: the reachable set is exactly that half-plane. With γ = 1 a free scalar charge is allowed only when α₀ = 0. By power counting the bound very probably extends to perturbative, ghost-free Horndeski with free charge (not computed).

**CO.** Exactly,
$$
E_A[w^4]=2\varepsilon(1+\varepsilon)m^2,\qquad \mathrm{NEC}_r[w^4]=-2\varepsilon(3+2\varepsilon)m^2,\qquad \mathrm{NEC}_r-3E_A=-2\varepsilon(6+5\varepsilon)m^2<0 .
$$
CO falls short of the bound by about 12εM² at every ε > 0.

**Escapes found.**
- **A ghost:** a phantom scalar or a phantom gauge field makes the whole (E_A, NEC_r) plane reachable at leading order.
- **A vector–disformal coupling (TeVeS-type):** NEC_r − 3E_A < 0 is reachable kinematically.
- **A disformal coupling to the unit gradient,** g̃ = A²g + λ(φ)n n with n = ∂φ/|∂φ|, singular at X = 0: it shifts NEC_r − 3E_A by −2λ₂Q² with no ghost and no vector. It is undefined wherever ∇φ = 0, including a regular stellar centre.

### 4. What this means for Reading I15
**At leading order in 1/R, among covariant theories with one universally coupled matter metric and a static exterior analytic in 1/R,** ε ≠ 0 (γ = 1, β < 1, with Run 71's null-energy failure) requires one of:
1. **a ghost;**
2. **a scalar sector whose leading static stress is not of the P(X, φ)-plus-conformal form:** couplings non-analytic at X = 0 (including a disformal coupling to the unit gradient), or screened or non-perturbative Horndeski, beyond-Horndeski and DHOST (untested);
3. **a vector–disformal coupling of field-dependent strength (TeVeS-type).** TeVeS itself gives β > 1, the wrong sign. Whether any consistent theory of this type gives CO's sign is not shown, although CO's exterior is kinematically such an image of Schwarzschild.

Outside the scope: matter species seeing different metrics, massive or bimetric fields (Yukawa tails), and screened regimes.

- **Under PI-strong** (no dynamical unit timelike vector), option 3 is excluded, leaving a ghost or an unusual scalar sector. A unit-gradient coupling is spacelike and would not obviously fall under PI-strong.
- **Giving up PI-strong does not by itself rescue ε:** aether and khronon gravity with minimal coupling give β = 1.
- **Reading I15 §6.1's inference is withdrawn,** not only misdirected. CO's exterior is not lapse-only. Aether and khronon theories give β = 1, so "probably aether- or khronon-type" is wrong. And "a lapse-only change needs a timelike vector" is itself false at leading order for β > 1 (a ghost-free conformal scalar with free charge reaches it); for β < 1, CO's sign, it holds within the constraint's class.

### 5. Grade
| claim | grade |
|---|---|
| CO's exterior is not lapse-only; β − 1 = −ε/[2(1+ε)] exactly | reading (Runs 66, 67, 69), now exact |
| CO's metric is an aligned TeVeS-type image of Schwarzschild with non-harmonic ψ | reading (checked) |
| the identity of §3 | derived; checked independently |
| the constraint of §3 | derived within its class; checked independently; no literature source located |
| ε ≠ 0 needs a ghost, an unusual scalar sector, or a TeVeS-type coupling (at leading order, within the scope) | follows |

### Sources
- T. Damour and G. Esposito-Farèse, [arXiv:gr-qc/9602056](https://arxiv.org/pdf/gr-qc/9602056).
- M. Hohmann, [arXiv:1506.04253](https://arxiv.org/pdf/1506.04253).
- T. Jacobson, [arXiv:0801.1547](https://arxiv.org/pdf/0801.1547); D. Blas and E. Lim, [arXiv:1412.4828](https://arxiv.org/pdf/1412.4828).
- D. Giannios, [arXiv:gr-qc/0502122](https://ar5iv.arxiv.org/html/gr-qc/0502122); J. D. Bekenstein, [arXiv:astro-ph/0403694](https://arxiv.org/abs/astro-ph/0403694) (not fetched).
- The record: `gravity/run66_section.md`, `run67_section.md` §1, `run69_section.md`, `run71_section.md` (K71a); Reading I15 §6.1 and §8.

*Ruled 30 October (Allen: "do as recommended"): recorded as a reading; ε kept provisionally pending T-I15c (Reading I15, rulings).*
