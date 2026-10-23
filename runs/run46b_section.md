## 9zq. Run 46b: the fall test with a finer medium table

*20 October 2026. Registered and hashed with its scripts and dependencies before the run (`fullrule/PREREG_46b.md`, 21:09 UTC on 19 October). Code checks (building the finer tables) are disclosed there. The registration said no case had been computed before. In fact the checker's pre-registration test had computed one of the nine cases, P₀/p_s = 256 double at 65,536 nodes, and its numbers match the registered case to 10⁻⁹. The post hoc fits (`posthoc46b.py`) were written after all results. An independent agent checked the run; its corrections are included.*

**Question.** Run 46's registered fall test was undecided because the draw-based measure scattered. The check traced the scatter to the medium's piecewise-linear table R(z) (4096 nodes). With a finer table, does the full pattern rule make a bound pattern's binding fall like its energy at neutron-star strength?

**What changed.**
- The medium's table has 65,536 nodes (16× finer), and one case uses 262,144 nodes as a convergence check.
- There are four outside-potential steps, U_ext = 0.0025 to 0.01, fitted linearly in ε. That replaces Run 46's two steps and Richardson extrapolation.
- Everything else is Run 46's.

**Results at U ≈ 0.22** (fall defects).

- **The ω-based and body responses** are linear in ε to 10⁻⁷–10⁻⁸.
- **The draw-based responses** still carry table noise of 0.5–2.6×10⁻⁴ per ε. The four-step linear fit amplifies that noise: its intercept has about 2.4 times the spread of a mean with a known slope.

| P₀/p_s | grid | pattern's fall by draw | by ω | body's own fall | pull miss |
|---|---|---|---|---|---|
| 64 | base / double / triple | +15.1 / +5.5 / +5.8 ×10⁻³ | +15.3 / +7.2 / +5.9 ×10⁻³ | +3.9 / +1.9 / +1.9 ×10⁻³ | −0.177 / −0.195 / −0.199 b |
| 256 | base / double / triple | +9.8 / +1.19 / +0.79 ×10⁻³ | +11.5 / +3.4 / +2.1 ×10⁻³ | +2.4 / +0.32 / +0.36 ×10⁻³ | −0.178 / −0.196 / −0.200 b |
| 1024 | base / double / triple | +8.5 / −0.79 / −0.47 ×10⁻³ | +10.5 / +2.4 / +1.2 ×10⁻³ | +1.9 / −0.10 / −0.06 ×10⁻³ | −0.178 / −0.196 / −0.201 b |
| 256, 262,144-node table | double | +0.90×10⁻³ | +3.4×10⁻³ | +0.32×10⁻³ | −0.196 b |

**Verdicts, as registered.**
- **Table convergence fails.** The 262,144-node case's draw-based fall is +0.90×10⁻³, against +1.19×10⁻³ at 65,536 nodes. The difference, 2.9×10⁻⁴, is over the registered 2×10⁻⁴.
- **K46b′: undecided (table not converged).**
  - The fits would have said undecided anyway, but only just. They gave Δ_∞ = −6.9×10⁻³ (q = 1, past the 3×10⁻³ falsification line, rms 1.1×10⁻³) and −2.85×10⁻³ (q = 2, rms 7×10⁻⁴). **The q = 2 fit came within 0.15×10⁻³ of the falsification line, with the same sign.**
  - The registered form does not describe the draw-based numbers well.
  - The convergence failure itself comes mostly from the linear fit's amplified noise. The ε-averages of the two tables differ by only 0.9×10⁻⁴. The checker's pre-registration test had already shown 2.4×10⁻⁴ of scatter across ε at 65,536 nodes, so the 2×10⁻⁴ criterion was nearly certain to fail. The verdict stands as registered.
- **K46c′: undecided,** as in Run 46: −1.5×10⁻³ (q = 1) and −0.6×10⁻³ (q = 2).
- **The ω-based fall** gives Δ_∞ = −4.3×10⁻⁴ (q = 2, rms 8×10⁻⁵) and −4.5×10⁻³ (q = 1), both reported, as in Run 46.

**The audits.**
- **Run 45's K45c stands.** Through the 65,536-node table the coded equation's fall defect is −0.1698 (Run 45: −0.170), and the body's +1.90×10⁻³ (Run 45: +1.90×10⁻³).
- **Run 40c's response stands.** It is 1.0012390 through the 4096-node table and 1.0012388 through the 65,536-node one.
- The table noise mattered only for small-part responses such as the draw-based pattern fall. Pull levels and body responses are unaffected.

**Post hoc (not registered).**
- **By ω, the fall converges cleanly in the grid.** Its three grids follow one power law in every medium. The ratio of successive steps is 6.25, which means an error falling as h^2.24.
  - Removing that grid error medium by medium, then fitting the medium, gives about −0.2×10⁻⁴.
  - The registered nine-point form with q = 2.2 gives −1.0×10⁻⁴ (rms 3.7×10⁻⁵).
  - **By ω, a bound pattern's binding falls like its energy to about 0 ± a few ×10⁻⁴.**
  - On the finest grid alone, the medium-extrapolated value is +0.9×10⁻³. About that much is grid error still left at h = ⅓.
- **By draw, on the finest grid,** the medium-only extrapolation gives −0.9×10⁻³ (P₀/p_s = 64, 256, 1024: +5.8, +0.79, −0.47 ×10⁻³). Its error is wider:
  - each intercept carries ±2–4×10⁻⁴ of table noise;
  - averaging R over ε instead of fitting gives −0.7×10⁻³;
  - its double→triple steps are noise, so its grid convergence is unknown;
  - at triple it differs from the ω-based value by 1.3–1.6×10⁻³, the present systematic error.
  - **Draw-based: −0.9 ± 0.4×10⁻³; |Δ| ≲ 1.5×10⁻³.**
- **The body's own fall,** extrapolated the same way, is −0.2×10⁻³.

**Reading.**
1. **Not falsified as registered, but not comfortably.** The registered q = 2 fit came within 0.15×10⁻³ of the falsification line. Post hoc, the ω-based fall goes to about zero once its grid error is removed, and the draw-based fall is −0.9 ± 0.4×10⁻³. The two estimators still differ by about 10⁻³.
2. **A cleaner registered decision is within reach, so this line should not close yet.** With the 262,144-node table the per-ε noise falls about 50-fold for about 10% more run time.
   - **Run 46c:** the nine points at 262,144 nodes (about 70 minutes on two cores), a fit fixed in advance (double and triple only, or q fixed at ω's observed 2.24), a pooled ε slope, and a convergence check at two points. This run motivated it, which would be disclosed.
   - Close the line on that result, whatever it is.
   - The pulsar triple's bound (2×10⁻⁶) stays about 500 times beyond the engine either way.
3. **The audits leave Runs 40c and 45 as they were.**
4. **The pull miss at neutron-star strength is firm in sign and size: −0.20 to −0.21 b, about 4% of a bound pattern's energy at that compactness.** It is −0.195 at double and −0.200 at triple, and extrapolates to about −0.205. It is the clearest remaining departure from GR at strong field, and **the more dangerous line.**
   - If a 4% active-mass deficit for gravitationally bound matter meant a neutron star and a white dwarf pulled differently from how they fall, binary-pulsar limits on that difference (self-acceleration) would test it hard.
   - That should be registered next, ahead of or alongside Run 46c.
