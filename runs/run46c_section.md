## 9zs. Run 46c: the fall test, settled at the engine's resolution

*20 October 2026. Registered and hashed before the run, with its scripts and main dependencies (`fullrule/PREREG_46c.md`, 23:22 UTC on 19 October; the run started seconds later). Two imported helper modules, `pattern36.py` and `free40c.py`, were not hashed; both predate the registration. Run 46b and its check motivated the choices, as disclosed in the registration: the 262,144-node table, the pooled ε slope, both fit forms, and q = 2.24, which came from Run 46b's ω-based fall. One of the nine cases (P₀/p_s = 256 double) had already been run with this table in Run 46b. The post hoc analysis (`posthoc46c.py`) was written after all results. An independent agent checked the run; its corrections are included, and the dilation argument below is its.*

**Question.** Does a bound pattern's binding fall like its energy at neutron-star strength (U ≈ 0.22) under the full pattern rule? This time the medium's table has converged, and the fit is fixed in advance. The registration also fixed a **closing rule**: whatever the verdict, the fall line closes at the engine's resolution.

**Setup.** Run 46b's nine points (P₀/p_s = 64, 256, 1024; base, double, triple), with these changes:
- a 262,144-node medium table;
- R(ε) = −ln(E(ε)/E(0))/ε at ε = 0.0025–0.01;
- one ε slope k for all cases (the median of the nine per-case slopes), and each case's defect Δ = mean_ε(R − kε) − 1.

Fits, both of the form Δ = Δ_∞ + A·(p_s/P₀) + C·h^q:
- **primary:** all nine points, q = 2.24;
- **secondary:** double and triple only, q = 2.

**Results** (fall defects ×10⁻³ at U ≈ 0.22).

| P₀/p_s | grid | pattern's fall by draw | by ω | body's own fall | pull miss |
|---|---|---|---|---|---|
| 64 | base / double / triple | +14.69 / +5.77 / +5.97 | +15.41 / +7.18 / +5.87 | +4.02 / +1.90 / +1.94 | −0.177 / −0.195 / −0.199 b |
| 256 | base / double / triple | +9.76 / +0.90 / +1.11 | +11.55 / +3.43 / +2.13 | +2.42 / +0.32 / +0.36 | −0.178 / −0.196 / −0.200 b |
| 1024 | base / double / triple | +8.40 / −0.38 / −0.18 | +10.52 / +2.43 / +1.14 | +1.99 / −0.10 / −0.06 | −0.178 / −0.196 / −0.201 b |

**The table has converged.** At the two check points, the 1,048,576-node table moves the draw-based fall by 0.4×10⁻⁵ and 1.2×10⁻⁵, well inside the registered 10⁻⁴. With the converged table, the per-ε scatter is below 10⁻⁵. Run 46b's was 0.5–2.6×10⁻⁴.
- The registration gave K46c″ "the same rules", but the code applies the convergence condition only to K46b″.
- For the body the two tables differ by 10⁻⁹, so this changes nothing.

**Verdicts, as registered.**

| test | primary (9 points, q = 2.24) | secondary (double + triple, q = 2) | verdict |
|---|---|---|---|
| **K46b″** a bound pattern's fall, by draw | Δ_∞ = −2.12×10⁻³ (rms 6.1×10⁻⁴) | −0.40×10⁻³ (rms 2.3×10⁻⁵) | **UNDECIDED** |
| **K46c″** the body's own fall | −0.56×10⁻³ (rms 1.4×10⁻⁴) | −0.15×10⁻³ (rms 8×10⁻⁶) | **PASS** |
| the pattern's fall by ω (reported) | −0.06×10⁻³ (rms 3.5×10⁻⁵) | −0.20×10⁻³ (rms 2.0×10⁻⁵) | within the pass band |

- **K46b″** is undecided because the primary fit lands at −2.1×10⁻³. That is past the 10⁻³ pass line and short of the 3×10⁻³ falsification line.
- **Under the registered closing rule, the fall line is now closed at the engine's resolution.** It has had three registered tests (K46b, K46b′, K46b″). None was falsified, and the last two fits were on the near side of the line.

**Why the primary fit misses (post hoc).** The two measures change with the grid in different ways.

- **By ω**, every refinement lowers the defect: base→double by −8.1 to −8.2×10⁻³, then double→triple by −1.3×10⁻³, in all three media. That is the single power law, h^2.24, that the primary form assumes, and it fits with rms 3.5×10⁻⁵.
- **By draw**, base→double drops by −8.8 to −8.9×10⁻³. But double→triple *rises* by +0.20×10⁻³, the same in all three media within ±4×10⁻⁶. The body's own fall does the same, more weakly (+0.04×10⁻³).
- So the draw-based grid error is not one power law. Its last step is small and of the opposite sign. With converged tables this rise is a real feature of the grid, not noise. The primary form, borrowed from ω, cannot follow it. Its rms (6.1×10⁻⁴) is about 27 times the secondary's.

**Post hoc numbers** (medium-only extrapolation to p_s/P₀ → 0 at each grid).

| grid | by draw | by ω | body's own |
|---|---|---|---|
| base | +8.0×10⁻³ | +10.2×10⁻³ | +1.9×10⁻³ |
| double | −0.76×10⁻³ | +2.1×10⁻³ | −0.23×10⁻³ |
| triple | **−0.56×10⁻³** | +0.85×10⁻³ | −0.19×10⁻³ |

- **On the finest grid, the draw-based fall is −0.56×10⁻³.** The ω-based fall is +0.85×10⁻³ there and still falling with the grid.
- The two estimators differ by 1.4×10⁻³ at triple. The difference is not monotone in the grid (−2.2, −2.9, −1.4 ×10⁻³ at base, double, triple), so it has not converged.
- **Three grids cannot pin down a two-term grid error, so the draw-based limit as h → 0 is not determined, nor is its sign.**
  - The registered fits are only two choices of form.
  - Other two-term forms fit the three values above exactly (×10⁻³):

| grid form | by draw | by ω | body's own |
|---|---|---|---|
| h² + h⁴ | +0.01 | −0.14 | −0.06 |
| h^2.24 + h⁴ | −0.08 | −0.02 | −0.08 |
| h² + h³ | +0.42 | −0.09 | +0.04 |
| h^1.5 + h² | +2.4 | +0.14 | +0.51 |
| h + h² | +4.5 | +0.38 | +1.0 |

  - With a leading h² error, as the engine's second-order stencils suggest, the draw-based limit lies between −2.1 and +0.4×10⁻³, and h² + h⁴ gives zero.
  - **By ω the limit is robust:** −0.14 to +0.38×10⁻³ in every form.
- **The engine's statement at its resolution:**
  - a bound pattern falls like its energy at neutron-star strength to a few ×10⁻⁴ by its frequency;
  - by its far field, to within about 2×10⁻³, if the leading grid error is h²;
  - the body's own binding passes as registered, to within about 6×10⁻⁴.

![Run 46c](figures/46c_fall.png)

**The pull.**
- The pull miss is −0.199 to −0.201 b on the finest grid in every medium. That is −0.204 b extrapolated in the grid (q = 2), about 4% of a bound pattern's energy at this compactness.
- Run 47 shows that Newtonian-order timing cannot see this, if passive and inertial mass are equal. That is an assumption: the engine has no inertia (§9zr).

**The dilation argument (from the independent check; not registered).** Take λ = e^{−U_ext}, a scale-free medium (P ≫ p_s) and the continuum. Then the outside potential changes nothing but scale.

- **The medium.** Where P ≫ p_s, the table gives P ≈ p_s e^{z/c}. So the potential is linear in the sources:
$$
\ln P=\ln P_{\rm bg}-\tfrac{6}{c}\,(G*s).
$$
- **The body.** P(x) = λP₀(x/λ) solves the case with the outside potential.
  - The proper-size rule gives R = λR₀.
  - The occupant count is fixed, so the draw density becomes λ⁻²·s₀(x/λ). With a 1/r kernel, the convolution is unchanged.
  - The stress scales as S → λS.
- **The full pattern rule.** N → λN and ∇² → λ⁻²∇² multiply the operator by λ²:
$$
-N^4\nabla^2\psi+m^2N^2\psi=\omega^2\psi\;\Rightarrow\;\omega=\lambda\,\omega_0\ \text{exactly}.
$$
  - ψ = φ(x/λ) keeps the normalisation 2ωΣN⁻⁴ψ² = 1.
  - The draw's total scales as λ.
- **So E_body, E_pat and κω all scale as λ at every ε.**
  - Δ_draw = Δ_ω = Δ_body = 0, and the ε slope is zero.
  - E_pat/κω, the 4% pull, does not depend on U_ext.
- **What breaks the scaling in the engine:**
  - the medium's scale p_s, which gives the A·p_s/P₀ term;
  - the lattice, which gives the C·h^q term;
  - table interpolation, about 10⁻⁵.
- **The coded equation breaks it at first order.** Its operator −∇² + m²N² does not scale, which is Run 45's −2K/ω².
- **The data agree.** The h² + h⁴ form gives zero for all three measures, and the medium term A barely depends on the grid.
- **Caveats:**
  - whether the self-consistent solution is unique;
  - the uniform shift stands in for an outside body, so tides are left out;
  - the body model itself.

**Reading.**
1. **The fall line is closed at the engine's resolution, as registered. It is not falsified.**
   - At neutron-star strength, the full pattern rule makes a bound pattern fall like its energy to a few ×10⁻⁴ by frequency. By far field it is within about 2×10⁻³, with a leading h² grid error.
   - The coded equation it replaced missed by 0.16 (K45c).
2. **The pulsar triple (2×10⁻⁶) is far beyond this engine's grid. But the grid may not be the real obstacle.**
   - If the dilation argument holds, the full rule's fall is exact in the continuum with a scale-free medium. The triple then bounds only the medium's scale:
$$
|A|\,\frac{p_s}{P_0}\lesssim4\times10^{-6},\qquad A\approx0.42\ (\text{draw}),\ 0.33\ (\omega),\ 0.14\ (\text{body}).
$$
   - That needs P₀/p_s ≳ 10⁵, times the share of the star's energy in such patterns. It is the same scale the first-order Nordtvedt bound already requires (Run 45).
   - Writing the argument up as a registered analytic claim, checked independently, is the way to reach the pulsar level.
3. **The remaining spread in the draw-based limit is a property of the grid, not of the medium.** The medium term A is the same in both fits (0.421, 0.418), the grid steps match across media, and the table has converged.
4. **The body's own binding passes as registered (K46c″).** This is the first PASS under a registered pass/falsify rule for a strong-field fall.
   - K45b met the same 10⁻³ threshold but had only a falsification branch.
   - K46c and K46c′ were undecided.
   - A pass here means |Δ| ≲ 10⁻³, about 500 times above the triple's bound.
