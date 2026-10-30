## Reading I15b: can a cuscuton-type theory carry CO's static exterior? (T-I15c, recorded as a reading)

*30 October 2026. Planned as a registered test (T-I15a″ §4, option 2: sectors non-analytic at X = 0). A scope and pre-registration were built and validated on controls (`SCOPE.md`, `PREREG.md`; 79 checks, none on CO's exterior). The literature and each class's signature already fixed every verdict-bearing output, so by decision (D0, 30 October) the test is recorded as a reading. Nothing was hashed or run. The reading was then checked independently (`checkI15c/REPORT.md`), and its corrections are adopted here. The pre-check version is `READING_T-I15c_v1_precheck.md`.*

**In plain terms.** The cuscuton is the covariant form of a scalar with no motion of its own, which makes it the nearest covariant match to CO's medium being fixed afresh each tick.
- No cuscuton-type theory with matter feeling the ordinary metric, or a metric built from it that does not depend on X, carries CO's field outside a body.
- The extended cuscuton comes close: it reproduces CO's clock rate and CO's β exactly, but on GR's spatial geometry, so its light bending is wrong.
- ε survives only where matter couples to the lapse of the preferred foliation. That coupling fits any static field. CO's own static equations, rewritten, turn out to be exactly that same static sector.
- Such a coupling is then tested by the preferred-frame parameters α₁ and α₂. Its one computed completion, the khronometric one, needs ε ≲ 2.5×10⁻⁶, about 2.5 times tighter than the record's present bound. It also conflicts with the borrowed α₁ = α₂ = 0 whenever ε ≠ 0.

### 1. The target (Run 67 §1)
$$
ds^2=-N^2dt^2+N^{-2}\big[dr^2+(r^2-2mr)\,d\Omega^2\big],\qquad N=(1+\varepsilon)n-\varepsilon,\quad n=\sqrt{1-2m/r},\qquad M_K=(1+\varepsilon)m .
$$
In areal radius R, w = 1/R: −g_tt = 1 − 2Mw + K₂w², g^RR = 1 − 2γMw + h₂w², K₂ = 2(β−γ)M². The exact values from the record (T-I15a″ §1, §3) are
$$
\gamma=1,\quad \beta-1=-\frac{\varepsilon}{2(1+\varepsilon)},\quad K_2=-\varepsilon(1+\varepsilon)m^2,\quad h_2=-(4\varepsilon+3\varepsilon^2)m^2,\quad (\mathrm{NEC}_r-3E_A)[w^4]=-2\varepsilon(6+5\varepsilon)m^2 .
$$
"Leading order in 1/R" means (M, γ, K₂, h₂).

### 2. The cuscuton
- **Action.** Signature (−,+,+,+), X = −½(∂φ)²:
$$
S=\int\!\sqrt{-g}\,\big[\tfrac12M_{\rm Pl}^2R+s\mu^2\sqrt{2|X|}-V(\phi)\big]+S_m .
$$
- **Only X > 0 (a timelike gradient) is a cuscuton.** It has no local degree of freedom and an infinite sound speed (Afshordi, Chung & Geshnizjani 2007). With a spacelike gradient a propagating mode appears (Iyonaga, Takahashi & Kobayashi 2018, hereafter ITK, App. D).
- **A static configuration must be aligned.** T^t_r = P_X g^{tt}qψ′ = 0 forces φ = qt, and then
$$
T^t{}_t=-V,\qquad T^r{}_r=T^\theta{}_\theta=\frac{s\mu^2|q|}{\sqrt{A}}-V .
$$
  This is a pressure that does not fall off; asymptotic flatness makes it cosmologically small at local scales.
- **The spacelike branch.**
  - E_A ≡ 0 and NEC_r = −8πsμ²|∂φ|.
  - The profile δφ ≈ −2sμ²/(V″R) is self-consistent only if s·V″ > 0. The ghost-free sign s = −1 therefore needs V″ < 0.
  - Its stress, and ½V″δφ², enter at w² (∝ μ⁴/V″), not at w⁴. The non-analyticity at X = 0 moves the stress down an order; it does not open T-I15a″'s bound.

### 3. The classes and their outcomes

| class | matter metric | static exterior | signature | outcome |
|---|---|---|---|---|
| **C0** | g | Schwarzschild | γ = β = 1 | **excluded** (K₂ = h₂ = 0 ≠ CO's) |
| **C1a** | A²(φ)g + B(φ)∂φ∂φ, constant on the exterior | −(n²−b)/(1−b)dt² + h_S | γ = β = 1 − b, exactly (K₂ = 0) | **excluded** (γ = 1 ⇒ b = 0 ⇒ C0) |
| **C2** | g; extended cuscuton, B₄ = b₀ + b₁/N, v₃ = 0, no lapse mass | −[(1+e)n − e]²dt² + h_S, e = b₁/b₀ | γ = 1/(1+e), β − 1 = −e/[2(1+e)], h₂ = 0 | **excluded** (γ = 1 ⇒ e = 0 ⇒ C0) |
| **C1b** | A²(X)g + B(X)∂φ∂φ | −F(n)²dt² + 𝒜(n)²h_S(M_g) | none | **not counted** (D1) |

- **C0.** The literature says the same.
  - Franchini, Herrero-Valea & Barausse 2021: the static, asymptotically flat solutions of minimal Hořava gravity are Schwarzschild, with the khronon on K = 0 slices and first post-Newtonian order equal to GR's.
  - Bhattacharyya et al. 2018: the full cuscuton has no asymptotically flat stationary solutions in general.
- **C2.**
  - **Static sector.** In unitary gauge the two-degree-of-freedom condition forces B₄ = b₀ + b₁/N and B₅ = 0 (ITK Eq. 48), and there are no aᵢ = ∂ᵢ ln N terms. The static aligned sector is therefore √γ(b₀N + b₁)R. Its vacuum is GR's static vacuum for Ñ = b₀N + b₁.
  - **γ** agrees with Iyonaga & Kobayashi 2021 (hereafter IK), Eq. 12 (b₀ = α₂, b₁ = α₄).
  - **IK's Eq. 25** black hole, N² − B² = N₀²[1 − μ₀/r + ((1−α₂)/α₂)b₀²/r⁴], is Schwarzschild only at leading order, or exactly when α₂ = 1 or b₀ = 0. Its tilt enters the metric only at w⁴.
  - **v₃ ≠ 0** excludes *aligned* static solutions (it puts a source ∝ ∂ᵢA₃(N) into the momentum constraint). Tilted ones are not excluded; they lie outside the registered scope (D2).
  - **What C2's exterior is.** It is T-I15a″'s "lapse-only" object: CO's affine clock map and CO's β on Schwarzschild's 3-geometry, so γ ≠ 1.
- **C1b, uncounted.**
  - In the aligned exterior X/X∞ = 1/n², with n the lapse of g. So F and 𝒜 are two free functions of n, and with them every static, spherical, asymptotically flat exterior is reachable, order by order, for any M_g (validated on Reissner–Nordström and planted maps).
  - For CO, F = N and 𝒜 = n/N. This is T-I15a″ §1's image, g_CO = −Ω²n²dt² + Ω⁻²h_S, with the foliation supplied by the cuscuton.
  - A class that fits everything carries no content, so it is not counted for the verdict.
  - **Its consistency is open:**
    - **Degrees of freedom.** Matter depends on the lapse nonlinearly. IK warn that "a subtlety arises when matter is present", and in their example a field coupled outside the Einstein frame revives the scalar.
    - **Ghosts.**
    - **Preferred-frame effects in matter** (§5).
    - **Two cones.** Gravitons ride g and matter rides g̃. With M_g = m, γ_GW − γ_EM = −2ε/(1+ε), which is 26–47 times outside GW170817's −2.6×10⁻⁷. M_g = M_K removes it at first post-Newtonian order.

### 4. Reading
**KILL, as scoped.** For aligned, shift-symmetric configurations with v₃ = 0 and W ≡ 0, at leading order in 1/R, no cuscuton-type theory carries CO's exterior when matter couples to g, or to a metric built from g and φ that does not depend on X. C0, C1a and C2 are excluded.
- **Where ε survives.** Only where matter couples to the foliation's lapse: C1b, which is the same static sector as §5. That fits any static exterior, and is then tested by α₁ and α₂ (§5).
- **For the cuscuton route, the reading recommends ε = 0 in gravity.**
- **Not excluded here:** T-I15a″'s other escapes (a ghost; TeVeS-type vector couplings; a disformal coupling to the unit spacelike gradient; beyond-Horndeski or DHOST outside ITK's class), and tilted C2 solutions with v₃ ≠ 0.
- **Every cuscuton route has a preferred foliation,** which means declining PI-strong.
- **The cuscuton's own viability is doubtful** (Note H §8, confirmed on reading Franchini et al. 2021 and Jacobson & Pulakkat 2025).

### 5. CO's static sector, rewritten; preferred-frame consequences (checked independently)
**The rewrite.** The record's vacuum equations in the medium's variables, Δ̃φ = 0 and R̃ᵢⱼ = 2∂ᵢφ∂ⱼφ, are the Euler–Lagrange equations of Run 66 §3's functional. Substitute γ̃ = N²h and φ = −ln[(N+ε)/(1+ε)], and use √γ̃R̃ = N√h[R + 2aᵢaⁱ] up to a divergence:
$$
\mathcal L^{\rm CO}_{\rm static}=N\sqrt h\,\big[R+\alpha(N)\,a_ia^i\big],\qquad a_i=\partial_i\ln N,\qquad \alpha(N)=2\Big[1-\frac{N^2}{(N+\varepsilon)^2}\Big],\qquad \alpha_\infty=\frac{2\varepsilon(2+\varepsilon)}{(1+\varepsilon)^2}\approx4\varepsilon .
$$
- **What the check confirmed** (exact series through x¹⁰, at the five registered values of ε):
  - The Euler–Lagrange equations vanish identically on Run 67's exterior, and its γ and β come out exactly.
  - With matter, the map reproduces minimal coupling to g and R5's draw.
  - Constant α gives the Janis–Newman–Winicour family, with γ = β = 1 exactly. The constant-α controls (α∞ held constant, and α = 0) fail on CO's metric, as they should.
- **The sign is healthy:** 0 < α(N) < 2, with 2 − α(N) = 2N²/(N+ε)². α tends to 2, the edge, only at the zero-clock surface.
- **Concordance:** G_N = G₀/(1 − α∞/2) = (1+ε)²G₀, which is the record's G_eff ∝ (1 + g_bg)² (Runs 52, 66).
- **Class.** A coefficient that depends on N breaks the khronon's φ → f(φ) symmetry. The form is therefore **spatially covariant gravity (Gao's class)**, the same family as ITK, and not khronometric gravity in the strict sense. α(X) also needs a reference X∞, which comes from P∞.
- **It is the same static sector as C1b and T-I15a″ §1.** Statically, α(N) can be removed by an invertible lapse-dependent field redefinition (IK Eq. 5):
$$
\tilde N=\frac{N+\varepsilon}{1+\varepsilon},\qquad \hat\gamma_{ij}=\Big[\frac{(1+\varepsilon)N}{N+\varepsilon}\Big]^2h_{ij}\quad\Longrightarrow\quad N\sqrt h\,[R+\alpha(N)a^2]=\tilde N\sqrt{\hat\gamma}\,\hat R+\text{div.}
$$
  This is GR, with matter on a metric that depends on the foliation's lapse. Whether a scalar propagates is decided by the non-static completion, not by α(N).

**Preferred-frame parameters.**
- **A khronometric completion** with c_T = 1 (so β_BL ≈ 0), using Blas & Lim Eq. 27 in the khronometric limit, gives
$$
\alpha_1=-4\alpha_\infty\approx-16\varepsilon\ \ (\text{every }\lambda),\qquad \alpha_2=\frac{\alpha\,[\alpha-\lambda(1-2\alpha)]}{(2-\alpha)\lambda}.
$$
  α₂ vanishes only on the tuned strip λ ≈ α/(1−2α) ≈ 4ε. Off the strip, α₂ ≈ −α/2 ≈ −10⁻⁵, against the pulsar bound 2×10⁻⁹. α₁ cannot be tuned: α = 2β would give c_T² − 1 ≈ 2ε.
- **The ε each α₁ bound allows** (α₁ ≈ −16ε):

| α₁ bound | ε allowed | P∞/p_s |
|---|---|---|
| 10⁻⁴ (lunar laser ranging) | ε < 6.25×10⁻⁶ | ≳ 1.6×10⁵ (the record's present bound) |
| 4×10⁻⁵ (PSR J1738+0333; the bound Run 34 uses) | **ε ≲ 2.5×10⁻⁶** | **≳ 4×10⁵** |
| Shao & Wex 2012, 95% | ε ≲ 2.2×10⁻⁶ | ≳ 4.6×10⁵ |
| LAGEOS, α₁ = (1 ± 2)×10⁻⁵ | ε ≈ 2×10⁻⁶ | ≳ 5×10⁵ |

- **Caveat.** Pulsar bounds constrain strong-field α̂'s, which can differ from the weak-field values in Lorentz-violating gravity.
- **Conflict with R8.** R8's borrowed boost gives α₁ = α₂ = 0 exactly (Run 34). A khronometric completion contradicts it whenever ε ≠ 0, and observably so at the present ε bound.
- **Not computed:** the α₁ and α₂ of the other completions, the C1b / IK-transformed-GR forms and kinetic terms that break the reparametrisation symmetry. Matter that feels the foliation's lapse very probably gives nonzero values at O(ε), but this is not shown.

### 6. Grade
| claim | grade |
|---|---|
| CO's exterior values (γ = 1, β − 1 = −ε/[2(1+ε)], K₂, h₂) | reading (T-I15a″, exact) |
| a static P(X) cuscuton must be aligned; E_A ≡ 0 in the spacelike branch; its stress at w² (s·V″ > 0) | derived; checked independently |
| C0's exterior is Schwarzschild | restatement (Franchini et al.; Bhattacharyya et al.) |
| C0 | excluded |
| C1a: γ = β = 1 − b | derived; checked independently |
| C1a | excluded |
| C2: static sector √γ(b₀N + b₁)R; γ = 1/(1+e) | restatement (ITK Eq. 48; IK Eq. 12) plus a derived reduction |
| C2: β − 1 = −e/[2(1+e)], h₂ = 0 | derived; checked independently |
| C2 | excluded |
| C1b reproduces any static exterior | derived (validated); restates T-I15a″ §1's image |
| C1b for the verdict | inert (not counted, D1) |
| KILL as scoped; ε = 0 in gravity for the cuscuton route | reading |
| CO's static sector = N√h[R + α(N)aᵢaⁱ], spatially covariant, healthy sign, G_N = (1+ε)²G₀ | derived; checked independently (restates Run 66 §3 in physical variables) |
| α(N) removable statically by IK Eq. 5's map; same static sector as C1b | derived; checked independently |
| khronometric completion: α₁ = −4α∞, needs ε ≲ 2.5×10⁻⁶ | derived from Blas–Lim's formulas; checked independently |
| khronometric completion versus R8's α₁ = α₂ = 0 | excluded unless ε ≲ 2.5×10⁻⁶ (inference from the computed formulas) |
| α₁ and α₂ of the C1b / IK-transformed-GR completion | needed (not computed) |
| C1b two-cone offset −2ε/(1+ε) at M_g = m | derived; checked independently (first post-Newtonian order) |

### 7. Derived while scoping, not yet independently checked
1. The aligned branch's w⁴ stress being of order μ²|q|M⁴, negligible against εM².
2. C2 asymptotics: W(1) = W′(1) = 0, with W″(1) ≠ 0 giving a massive (Yukawa) lapse.
3. C1b universality and the order-by-order solver: validated on controls (V5–V6), not re-derived by the check.
4. The claim that matter which feels the foliation's lapse gives α₁, α₂ ≠ 0 at O(ε) in completions other than the khronometric one (inference).
5. The bounds not fetched by either session: Franchini et al.'s strip value, and Blas–Pujolàs–Sibiryakov's and Jacobson's formulas (only Blas–Lim's Eq. 27 was fetched, by the check).

### Sources
- **Fetched in full:**
  - J. Bhattacharyya et al., [arXiv:1612.01824](https://arxiv.org/pdf/1612.01824);
  - A. Iyonaga, K. Takahashi, T. Kobayashi, [arXiv:1809.10935](https://arxiv.org/pdf/1809.10935);
  - A. Iyonaga, T. Kobayashi, [arXiv:2109.10615](https://arxiv.org/pdf/2109.10615);
  - N. Franchini, M. Herrero-Valea, E. Barausse, [arXiv:2103.00929](https://arxiv.org/pdf/2103.00929);
  - T. Jacobson, A. Pulakkat, [arXiv:2508.03106](https://arxiv.org/pdf/2508.03106);
  - A. De Felice et al., [arXiv:2010.13067](https://arxiv.org/pdf/2010.13067) and [arXiv:2110.14496](https://arxiv.org/pdf/2110.14496).
- **Fetched in part:**
  - N. Afshordi, D. J. H. Chung, G. Geshnizjani, [arXiv:hep-th/0609150](https://ar5iv.labs.arxiv.org/html/hep-th/0609150), through §III;
  - A. Iyonaga, K. Takahashi, T. Kobayashi, [arXiv:2003.01934](https://ar5iv.labs.arxiv.org/html/2003.01934);
  - H. Gomes, D. C. Guariento, [arXiv:1703.08226](https://ar5iv.arxiv.org/html/1703.08226);
  - N. Afshordi et al., [arXiv:astro-ph/0702002](https://arxiv.org/abs/astro-ph/0702002), abstract only.
- **Fetched by the check:**
  - D. Blas, E. Lim, [arXiv:1412.4828](https://arxiv.org/pdf/1412.4828), Eqs. 19 and 27;
  - L. Shao, N. Wex, [arXiv:1209.4503](https://ar5iv.arxiv.org/html/1209.4503);
  - C. M. Will, Living Rev. Relativ. 17, 4 (2014), Table 4;
  - the LAGEOS α₁ result, [arXiv:2602.00867](https://arxiv.org/abs/2602.00867).
- **Not fetched:** N. Afshordi, arXiv:0907.5201 (blocked); Blas–Pujolàs–Sibiryakov; Jacobson 2008; Cassini; the GW170817 Shapiro bound (as commonly quoted).
- **The record:** Run 67 §1; Run 66 §3; Runs 34 and 52; R5 and R8; `testI15a/READING_T-I15a.md`; `checkI15a_identity/REPORT.md`; Reading I15 §6.1; Note H §8. **This folder:** `SCOPE.md`, `PREREG.md`, `val/validate.log`. **The check:** `checkI15c/REPORT.md`.

*Ruled 30 October (Allen: "do as you recommend"): recorded as a reading; the cuscuton route is closed as scoped; ε stays provisional, now with the preferred-frame price of §5.*

*Note (30 October, T-I15d):* for the lapse-coupled completion (α_E = 0 member) α₁ = −4α∞ and α₂ = 2ε[ε − λ_E(1−ε)]/[λ_E(1+ε)²] ≈ −2ε exactly; the khronometric completion here has the same off-strip α₂ ≈ −2ε. Under the pulsar α̂₂ bound both give ε ≲ 8×10⁻¹⁰ untuned; the lapse-coupled one also has γ_GW − γ_EM = −2ε/(1+ε), so ε ≲ 1.3×10⁻⁷ from GW170817 (`test_I15d_section.md`).

*Note (30 October, Reading I18c):* R1 is amended beyond first order (a pure logarithm above p_c ≡ (1/p_s + 1/P∞)⁻¹, joined smoothly to f = 0.99P below). Results here that rest on g ≈ p_s/P, or on R1's curvature above the crossover, belong to the original R1; most had already lapsed as gravity results with ε = 0 in gravity. Where p_s sets a scale, read p_c.
