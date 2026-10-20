## 9zo. Run 45: a body at neutron-star strength — does its binding pull and fall like its energy?

*19 October 2026. Allen: "run 45 please". Registered and hashed with its code before the run (`nstar/PREREG_45.md`, 16:12 UTC).*

*The first launch stopped on an array-shape bug before any result. The fix (`.ravel()`, as `body42.py` does) is disclosed and re-hashed in an amendment (16:16 UTC). Removing it reproduces the original hashes exactly.*

*A trial of the body alone, used to choose the strengths, is disclosed in the registration. `analyse45.py` was written before any result but not hashed. The diagnosis script `diag45.py` was written at 16:23 UTC, about 70 s after the first registered case printed, and ran alongside the rest; it is post hoc.*

*An independent agent checked the run; its corrections are included.*

**Question.** Run 44 left a second-order term in how a bound pattern pulls, about −1.25 U_self·b. Read across naively to a neutron star (U ≈ 0.2, binding ≈ 0.12–0.15), it is a few ×10⁻². The pulsar triple PSR J0337+1715 bounds how a neutron star *falls* relative to white dwarfs: Δ = (+0.5 ± 1.8)×10⁻⁶ at 95% (Voisin et al. 2020). Does the engine make a body's binding pull and fall like its energy at that strength?

**Part 1: first order (calculation).** ED's Nordtvedt parameter is η_N = (10/3)(β − 1). The record's theory for β − 1 gives about −0.45 p_s/P₀ at large p_s, so η_N ≈ −1.5 p_s/P₀ (−6.5×10⁻⁵ at P₀/p_s = 2.3×10⁴). A 1.44 M☉ neutron star's binding fraction is about 0.12, so
$$
|\Delta|\approx|\eta_N|\times0.12\approx0.18\,\frac{p_s}{P_0}\;\lesssim\;2\times10^{-6}\quad\Longrightarrow\quad \frac{P_0}{p_s}\gtrsim9\times10^{4}.
$$
- **The sign matters.** η_N < 0 gives Δ > 0, and the 95% upper limit (+2.3×10⁻⁶) then gives 7.8×10⁴. The other sign would give 1.4×10⁵.
- **Either way, about 10⁵**, roughly four times the current lower bound (2.3×10⁴, from ζ₂). The pulsar triple tightens the scale bound; it does not falsify the rules at first order.
- **Two approximations.** The linear Nordtvedt form is not exact at neutron-star compactness. And Part 1 assumes bound matter's energy falls by GR's weights, which Part 2 shows the coded patterns do not do.

**Part 2: setup.**
- **Medium:** Run 40c's unbounded mean-field medium, P₀ = 4096, at P₀/p_s = 64 and 256.
- **The body:** double resolution (R₀ = 6), keeping its proper size, at U_self ≈ 0.056, 0.11 and 0.22.
- **Stress pulls (Allen's ruling).** The body's stress holds it against its own field and against the pattern's: $S=-\sum_x s_b(x)\,(\mathbf x-\mathbf c)\cdot\nabla U_{\rm bal}(x)$, drawn at weight 1 per direction. This is the first run with stress for the body's own binding.
- **The pattern:** Run 16's equation, as in Runs 36–44: $-\nabla^2\psi+m^2N^2\psi=\omega^2\psi$. This is a flat-space wave with its mass redshifted; the pattern keeps speed 1. The record calls it the "clock half". It is not the wave equation of a metric with only $g_{tt}$ changed, which would give half the defect found below. Its mass m = 2.5√(0.055/U) keeps its shape.
- **Fall** is the response of the body's energy at infinity (its total draw E: z is linear in the draw, so the far field sees exactly E) to a uniform outside potential, a shift of the background P → P₀e^{−U_ext}:
$$
\Delta=\frac{d\ln E}{d(-U_{\rm ext})}-1\qquad(\text{GR: }0),
$$
  at U_ext = 0.005 and 0.01, extrapolated to 0.
  - Passive mass = d(energy at infinity)/d(−U) is a stated assumption: the engine's bodies are held, not moved.
  - The uniform shift captures the redshift, and the coupling between background and self-field through the medium. It misses tidal terms and the support of a body held in a gradient.
  - Without stress, the body's fall at U = 0.056 is +1.10×10⁻³. Run 40c's distant point draw gave +1.24×10⁻³, which supports the proxy.

**Results.**

| | U_self | 0.056 | 0.110 | 0.218 |
|---|---|---|---|---|
| **body's own pull**, E/D_rest (GR, first order: 1 − U/2) | P₀/p_s = 64 | 0.97190 (0.97181) | 0.94547 (0.94526) | 0.89185 (0.89108) |
| | 256 | 0.97188 | 0.94504 | 0.89175 |
| | no stress (64) | 0.94653 | 0.90081 | 0.81832 |
| **body's own fall** Δ | 64 | +3.8×10⁻⁴ | +8.1×10⁻⁴ | +1.9×10⁻³ (base resolution: +3.9×10⁻³) |
| | 256 | +3.9×10⁻⁵ | +1.1×10⁻⁴ | +3.2×10⁻⁴ |
| | no stress (64) | +1.1×10⁻³ | +2.1×10⁻³ | +4.1×10⁻³ |
| **bound pattern's fall** Δ (clock half) | 64 | −0.040 (−0.81 b) | −0.080 (−0.86 b) | −0.170 (−1.00 b) (base: −0.166) |
| | 256 | −0.040 | −0.084 | −0.165 |
| **pattern's pull**, miss in b (stress: self + pattern) | 64 / 256 | −0.065 / −0.065 | −0.137 / −0.138 | −0.285 / −0.286 |
| pattern's pull, pattern's stress only (Runs 42–44) | 64 / 256 | −0.060 / −0.060 | −0.124 / −0.125 | −0.249 / −0.249 |

The pattern's binding b is 0.050, 0.093 and 0.171 at the three strengths. The composite's fall equals the body's to within 10⁻⁵, since the pattern is at test strength.

**Verdicts, as registered.**
- **K45a passes.** The fit of (E/D_rest − 1)/U_self against U_self has intercept −0.4991 in both media (registered: −0.5 ± 0.05; slopes +0.012 and +0.009). With its stress drawing, the body's own binding pulls once at first order.
  - This is analytic. The clock-rate draw gives −2|W|, and the virial stress gives +|W|, so E = M(1 − Ū/2).
  - So K45a checks that the stress rule is implemented as Tolman's term. It is not independent physics.
  - Without stress the body counts its binding twice (slope −0.97).
- **K45b: not falsified at about 10⁻³ resolution.**
  - Removing the medium's part as registered gives Δ_∞ = (4Δ₂₅₆ − Δ₆₄)/3 = −2.1×10⁻⁴ at U = 0.218. For any medium part ∝ (p_s/P₀)^k with k ≥ 1, Δ_∞ lies in [−2.1, +3.2]×10⁻⁴.
  - But the base-resolution case is 2.08 times the double-resolution one. That narrowly misses the registered factor-2 agreement, which matters only for the falsified branch.
  - The lattice error, about 0.7–2 ×10⁻³ by Richardson extrapolation, passes into Δ_∞ undiminished. So the honest statement is "not falsified at ~10⁻³", not "at 2×10⁻⁴".
  - The medium's part has the sign that −η_N U/2 predicts. It is 0.58–0.75 of that prediction at P₀/p_s = 64 and 0.23–0.50 at 256.
  - The 2×10⁻⁶ bound itself is beyond this engine.
- **K45c: falsified, as registered.** The bound pattern's fall defect is Δ_∞ = −0.163 at U = 0.218, and the base-resolution case agrees (−0.166). **The engine's massive patterns, as coded, fail PSR J0337+1715 by about 10⁵.**
  - Read across the same way, they would also fail lunar laser ranging by about 10⁴.
  - The registration expected the missing spatial half to matter only at second order. That expectation failed: it matters at first order.

![Run 45](figures/45_nstar.png)

**Diagnosis (post hoc, `diag45.py`; not registered).**

**The defect law.** If the body's field rescales as $N(\mathbf x)\to\lambda N(\mathbf x/\lambda)$ with λ = e^{−U} (proper size), the coded equation gives $(\omega/\lambda)^2$ = eigenvalue of $(-\lambda^{-4}\nabla^2+m^2N^2)$. So
$$
\Delta_{\rm clock}=-\,\frac{2K}{\omega^2},\qquad K=\langle-\nabla^2\rangle .
$$
The defect is first order in the pattern's internal gradient energy, which for gravitational binding is first order in the binding. The check confirmed it numerically: −0.0408 against −0.0393 measured at U = 0.056, and −0.168 against −0.157 at U = 0.22 (base resolution).

**The full rule.** The adopted rule (17 October, c = N², which light obeys) puts a pattern in the metric $-N^2dt^2+N^{-2}d\mathbf x^2$. Its wave equation is then, exactly ($\sqrt{-g}=N^{-2}$, $\sqrt{-g}\,g^{ij}=\delta_{ij}$, $\sqrt{-g}\,g^{tt}=-N^{-4}$),
$$
-N^4\nabla^2\psi+m^2N^2\psi=\omega^2\psi\quad\Longleftrightarrow\quad(-\nabla^2+m^2N^{-2})\,\psi=\omega^2N^{-4}\psi .
$$
Under the same rescaling every term scales alike, so ω → ωe^{−U} exactly. That holds only in the continuum, and only if the medium's field map is exactly exponential; it departs from that at order p_s/P₀.

**The test.** A test pattern's frequency was computed in the same body fields under both equations (ω only; no full-rule draw rule is defined yet):

| | U_self | clock half: b, fall defect | full rule: b, fall defect |
|---|---|---|---|
| P₀/p_s = 64, double | 0.056 | 0.050, −3.9×10⁻² (−0.79 b) | 0.053, +1.6×10⁻³ (+0.030 b) |
| P₀/p_s = 64, double | 0.218 | 0.171, −0.160 (−0.94 b) | 0.201, +7.2×10⁻³ (+0.036 b) |
| P₀/p_s = 64, base (the check's rerun) | 0.219 | | +1.53×10⁻² |
| P₀/p_s = 256, double | 0.218 | 0.171, −0.162 (−0.95 b) | 0.201, +3.4×10⁻³ (+0.017 b) |

**The full rule removes most of the first-order defect: 22–47 times smaller, case by case.** What remains depends on both the medium and the grid:
- It roughly halves from P₀/p_s = 64 to 256.
- It doubles from double to base resolution. Richardson extrapolation gives +4.5×10⁻³ if the lattice error goes as h², or −1×10⁻³ if it goes as h.
- So most of it is lattice error.
- Removing the medium's part at double resolution leaves +2.2×10⁻³, above the registered 10⁻³. **As measured, the full rule would itself fall in K45c's falsifying region.** Only a registered, converged test (Run 46) can say whether it passes.

The independent check reproduced the diagnosis's ω values to 10 digits and its defects exactly, with a different form of the full-rule operator and a generic start.

**Reading.**
1. **The engine's massive patterns, as coded, fail.** With a redshifted mass only, bound energy falls with the wrong weight, Δ = −2K/ω², at first order. By the same scaling argument (not run), any binding (not only gravitational) would do the same. If real matter's bound constituents obeyed this equation, laboratory tests of the equivalence principle would fail by many orders of magnitude.
2. **The adopted rule is worded for all patterns, but its form for massive patterns was never written down.**
   - §11 item 9 flagged the spatial half for light and fast motion. Item 10 still lists whether matter's own commitments obey the pattern rule.
   - The wave equation in $-N^2dt^2+N^{-2}d\mathbf x^2$ used here is a reading of the rule, adopted post hoc.
   - It removes most of the defect, but has not been tested as registered, and its draw rule is not yet written.
3. **Runs 36–44 used the coded patterns.** Their first-order pull results stand under the full rule only if its covariant draw reduces to the adopted rule R-b at first order. That is to be shown and registered in Run 46. Their second-order residuals (Run 44's −1.25 U_self·b) may change.
4. **The body's own binding passes what the engine resolves.**
   - It pulls once to first order (K45a, by construction of the stress rule).
   - Its fall defect is ≤ 2×10⁻³ at double resolution (3.9×10⁻³ at base), and shrinks toward the physical medium and with the grid.
   - With stress pulling it is 2.2–2.9 times smaller than without at P₀/p_s = 64, and 4.8–11.5 times smaller at 256.
5. **The pattern's pull at neutron-star strength.** At U = 0.218 the read-across is −0.27 b, and the two arms bracket it (−0.25 b, −0.29 b). These are clock-half patterns, to be redone under the full rule.
6. **Run 46 should register:**
   - the full rule's covariant draw, with its weak-field expansion shown before running;
   - the exact generalized eigenproblem, with the coded equation kept as a control (predicted Δ = −2K/ω²);
   - fall (by draw and by ω) and pull at U = 0.056, 0.11 and 0.22;
   - three media (P₀/p_s = 64, 256, 1024), two resolutions in each, and a third at U = 0.22;
   - a registered separation of lattice and medium parts, and in advance what counts as a pass;
   - the weak-field pull of Runs 40c, 42 and 44 rechecked;
   - every script hashed.
