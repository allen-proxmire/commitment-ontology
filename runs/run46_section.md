## Run 46: the full pattern rule for massive patterns

*19 October 2026. Registered and hashed with all its scripts, including the analysis, before the run (`fullrule/PREREG_46.md`, 17:29 UTC). Trials of the strengths in the third medium, of the body at triple resolution, and a code check on uniform fields are disclosed there. Run on two cores as two fixed case lists. The post hoc fits (`posthoc46.py`) were written after all results. An independent agent checked the run, found the source of the draw-based scatter, and its corrections are included.*

**Question.** Run 45's K45c failed. The engine's massive patterns, coded as flat-space waves with a redshifted mass, let bound energy fall with the wrong weight, Δ = −2K/ω². Does the pattern rule adopted on 17 October fix that, when read for massive patterns as the wave equation in the metric it gives light?

**The rule, as registered.**

The equation, exactly:
$$
(-\nabla^2+m^2N^{-2})\,\psi=\omega^2N^{-4}\psi\quad\Longleftrightarrow\quad-N^4\nabla^2\psi+m^2N^2\psi=\omega^2\psi,
$$
with one quantum normalized by $2\omega\sum N^{-4}\psi^2=1$.

The draw is the covariant (Tolman/Komar) form of "every part of a source draws by α(T⁰⁰ + ΣTⁱⁱ)", namely $N(\rho+\sum p)\sqrt\gamma$:
- for a matter count at rest it is count × N, the engine's existing rule;
- for the pattern it is
$$
d_x=\kappa\,(4\omega^2N^{-4}-2m^2N^{-2})\,\psi_x^2,\qquad\sum_x d_x=\kappa\Big(\omega+2\sum|\nabla\psi|^2\Big),
$$
  which is exact on the lattice: an algebraic identity, checked to 10⁻¹⁵ in every case. That verifies the eigen-solve and the summation, not the Komar physics itself.

The weak-field expansion was stated before running: at first order the total draw is R-b's, so binding should count once.

**Setup.** Run 45's body, stress rule and uniform outside potential, with these differences:
- three media, P₀/p_s = 64, 256 and 1024;
- strengths U_self ≈ 0.056, 0.11 and 0.22;
- base and double resolution in every medium, plus triple (h = ⅓) at U ≈ 0.22;
- Run 40c's outside (xy) case added;
- Run 45's coded equation kept as a control.

**Verdicts, as registered.**
- **K46a passes. Weak-field pull, binding counted once.** The misses, against ±0.25 b, are:
  - Run 40c's analogue (xy, base): +0.010 b (Run 40c: −0.05 b);
  - Run 42's (ground state, base): −0.015 b (Run 42: −0.086 b);
  - Run 44's (ground state, double): −0.038 b (Run 44: −0.073 b without stress for the body's own binding; −0.065 b with it under the coded equation, Run 45).

  All are closer to zero than under the coded equation.
- **K46b is undecided: a bound pattern's fall, by draw, at U ≈ 0.22.** The registered fit Δ = Δ_∞ + A·(p_s/P₀) + C·h^q gives Δ_∞ = +3.7×10⁻⁴ (q = 1) and +3.7×10⁻³ (q = 2). Its scatter is rms 4.4×10⁻³, as large as the numbers themselves, so the registered form does not describe the draw-based defect. It reaches +0.080 b (P₀/p_s = 256, base) at this strength and +0.13 b at U ≈ 0.056, against about −1 b in Run 45. It is neither passed nor falsified. The scatter is noise from the code's lookup table (below).
- **K46c is undecided: the body's own fall.** The fit gives Δ_∞ = −1.5×10⁻³ (q = 1) and −0.6×10⁻³ (q = 2).
- **K46d passes. The control.** The coded equation's ω-defect lands at 0.96–0.99 of the predicted −2K/ω² in every double-resolution case. That confirms Run 45's diagnosis.

**Results at U ≈ 0.22.**

| P₀/p_s | grid | pattern's fall by draw | pattern's fall by ω | body's own fall | pull miss |
|---|---|---|---|---|---|
| 64 | base / double / triple | +13.2 / +5.1 / −3.2 ×10⁻³ | +15.3 / +7.2 / +5.9 ×10⁻³ | +3.9 / +1.9 / +1.9 ×10⁻³ | −0.177 / −0.195 / −0.199 b |
| 256 | base / double / triple | +16.3 / +9.6 / +7.3 ×10⁻³ | +11.5 / +3.4 / +2.2 ×10⁻³ | +2.4 / +0.32 / +0.36 ×10⁻³ | −0.178 / −0.196 / −0.200 b |
| 1024 | base / double / triple | +2.9 / +6.0 / +3.1 ×10⁻³ | +10.4 / +2.4 / +1.1 ×10⁻³ | +1.9 / −0.13 / −0.09 ×10⁻³ | −0.178 / −0.196 / −0.201 b |
| Run 45, coded equation, 64 double | | −0.170 | −0.160 | +1.9×10⁻³ | −0.285 b |

![Run 46](figures/46_fullrule.png)

**Post hoc (not registered; `posthoc46.py`).**
- **The pattern's fall by ω converges cleanly, though its limit depends on the fit's exponent.** With q = 2 the same fit describes all nine points to rms 9×10⁻⁵ and gives Δ_∞ = −4.4×10⁻⁴. With q = 1 it is five times worse (rms 4.8×10⁻⁴) and gives −4.5×10⁻³. The successive differences fall by 6.3 in every medium (h²: 5.4; h: 3.0). With q free the best fit is q = 2.25:

| q | 1.5 | 2 | 2.25 (best) | 2.5 | 3 |
|---|---|---|---|---|---|
| Δ_∞ | −1.7×10⁻³ | −4.4×10⁻⁴ | −0.4×10⁻⁴ | +2.7×10⁻⁴ | +6.8×10⁻⁴ |

  **So |Δ_∞| ≲ 7×10⁻⁴ for q between 2 and 3, with q = 1 disfavoured by its fit. Read by its frequency, a bound pattern's binding falls like its energy under the full rule, to the engine's resolution.** Applied to these numbers, the registered both-fits rule would still say undecided.
- **The body's own fall has converged in the grid.** Double and triple agree in every medium. A fit in the medium alone over those six points (rms 3×10⁻⁵) gives Δ_∞ = −2.2×10⁻⁴.
- **The draw-based fall's scatter is noise from the medium's lookup table (found by the check).**
  - The medium's response R(z) is a piecewise-linear table of 4096 nodes, about 7×10⁻⁴ apart in ln P.
  - The pattern's part of the energy, E_composite − E_body, is only about 5×10⁻⁵ of the total. Its response to the outside potential therefore picks up the jumps in the table's slope as the shift moves z across nodes.
  - The check reran P₀/p_s = 256, double, U ≈ 0.22 at four ε:

| ε | 0.0025 | 0.005 | 0.0075 | 0.01 |
|---|---|---|---|---|
| R_pat − 1, the engine's table | 1.77×10⁻² | 5.38×10⁻³ | 2.06×10⁻³ | 1.19×10⁻³ |
| R_pat − 1, a table 16× finer | 1.06×10⁻³ | 1.12×10⁻³ | 0.95×10⁻³ | 0.88×10⁻³ |

  - With the engine's table the extrapolated defect depends on which ε are used: +9.6×10⁻³ from (0.005, 0.01), +3.0×10⁻² from (0.0025, 0.005). With the finer table it is +1.0 to +1.4×10⁻³, near the ω-based value for that grid (+3.4×10⁻³).
  - The pull hardly moves (E_pat changes by 2×10⁻⁵, relatively), and the body's fall jitters by only about 1.5×10⁻⁵. Pull levels in Runs 40c–46 are safe; responses taken as finite differences of small parts may not be.
- **The pull at neutron-star strength has converged at −0.20 b, the same in every medium** (coded equation: −0.29 b). A second-order miss remains under the full rule.
  - In units of U_self, miss/U = −0.67, −0.79 and −0.90 at U = 0.056, 0.11 and 0.22, roughly −0.62 − 1.3U.
  - Run 44's read-across (−1.25 U_self·b) predicted −0.14 b and −0.27 b; the full rule gives −0.087 b and −0.20 b.
  - **Here b = 1 − ω/m ≈ U_self**, the pattern's redshift-like binding in the body's well, not a binding fraction. At U_self ≈ 0.22 the body's own binding is 10.8% (self-pull 0.892), close to a neutron star's 12%. At that compactness the pattern pulls 0.20 × 0.20 = **4.0% less than its energy** (pull ratio 0.960).
  - In GR the Komar mass equals the total (ADM) mass, so any nonzero miss is a split between active mass (how a body pulls) and passive mass (how it falls, which this run's fall measures).
  - Whether a 4% active/passive split for bound patterns conflicts with binary-pulsar tests is not computed.

**Reading.**
1. **The full pattern rule removes Run 45's first-order failure.** The control reproduces the coded equation's −2K/ω² defect. The full rule's ω-based defect extrapolates to −4×10⁻⁴ (post hoc). The weak-field pull still counts binding once (K46a). **The written form, the wave equation in −N²dt² + N⁻²dx² with the Tolman/Komar draw, is recommended as the engine's rule for massive patterns. It needs a ruling, since the form is a reading of the 17 October rule.**
2. **The registered fall test is undecided, not passed.** The draw-based measure's scatter is lookup-table noise. A finer table gives about +1×10⁻³ in the one case rerun, and the ω-based measure gives |Δ_∞| ≲ 7×10⁻⁴ (post hoc). The engine's verdict at neutron-star strength is "no first-order failure; second-order fall consistent with zero at about 10⁻³, pending a registered rerun with a finer table". The pulsar triple's 2×10⁻⁶ remains far beyond it.
3. **The strong-field pull miss remains:** −0.20 b at U ≈ 0.22 (4% of the pattern's energy), converged in grid and medium. It is the same kind of second-order bookkeeping departure as Runs 40b and 44. Under option A it matters only inside compact objects and in neutron stars, where its consequence (active against passive mass) is not yet worked out.
4. **Runs 36–44's first-order pull results are consistent under the full rule for the three analogues tested** (K46a, at U ≈ 0.056 inside a ±0.25 b band), as the weak-field expansion predicted. Their second-order numbers change: like for like, the Run 44 analogue moves from −0.065 b (coded equation, with stress for the body's own binding) to −0.038 b.
5. **Next, Run 46b:** K46b's nine points rerun with a medium table of at least 65,536 nodes (or a smooth R(z)), four ε values and a linear fit, plus one case at 262,144 nodes to confirm the table has converged. Also audit the earlier finite-difference responses taken through the same table (Runs 40c, 45).
