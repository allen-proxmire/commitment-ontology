## Reading I17a: where commitment falls in a collapse (T-I17a, recorded as a reading)

*30 October 2026. Recorded as a reading, not hashed (decision D0, 30 October). It encodes no new rule. Revised after an independent check (`checkT-I17a/REPORT.md`, with `check_t_i17a.py` and its log), whose corrections are adopted; the pre-check version is `READING_T-I17a_v1_precheck.md`. The draft registration (`SCOPE.md`, `PREREG.md`), its code and its validation (`val/validate.log`: 32 PASS, 0 FAIL, on controls and planted cases only) stay in this folder as the record of how the open remainder would be tested. No Oppenheimer–Snyder slice later than the time-symmetric one was computed.*

**In plain terms.** Reading I17 asked where infalling matter commits, that is where a slicing's lapse falls to 2ε_med, in a standard collapse, relative to the horizon. For the slicing the I15 ruling names (maximal slicing), the numerical-relativity literature already answers this. The lapse on the collapsing ball collapses exponentially, the matter freezes, and the surface settles at an areal radius near 3m/2, inside the horizon. So for any ε_med small enough that 2ε_med lies below the surface's lapse at R = 2m, commitment on the surface falls inside the horizon, near 3m/2 + 3ε_med/√2. The rule does not single out maximal slicing, though. Polar slicing is fixed on each tick just as R4 requires and has the same static content, and under it commitment on the surface falls just outside the horizon (interior shells not computed). Reading I17 §2 already says that the collapse result depends on the slicing. What the literature does not give (the surface's lapse at R = 2m, which sets the threshold, and the interior shells) is parked. Under the 30 October ruling commitment relabels matter and does not hold it, so where it falls has no gravitational consequence.

---

### 1. The setting

- **The spacetime.** An Oppenheimer–Snyder dust ball of mass m, released from rest at areal radius R₀.
  - The interior is closed dust FRW, a = (a_m/2)(1 + cos η), with sin²χ_s = 2m/R₀.
  - The exterior is Schwarzschild.
- **The slicing.** Maximal slicing, K = 0, with:
  - regularity at the centre (slices orthogonal to it, N_l = 0 there);
  - N → 1 at spatial infinity;
  - the time-symmetric slice at t = 0.

  These are the conditions of Petrich, Shapiro & Teukolsky (PST85) and later work (`SCOPE.md` §5). The lapse obeys
$$
D^2N=N\big[K_{ij}K^{ij}+4\pi(\rho+S)\big].
$$
- **The reading of P.** P = P∞N (R2 through the slicing's lapse; I17 §2). Commitment falls where P = 2p_s, that is where N = 2ε_med (ε_med = p_s/P∞).
- **Horizons.**
  - Shell χ crosses the event horizon at η_EH = η_H − (χ_s − χ), with cos η_H = 4m/R₀ − 1.
  - Shell χ becomes trapped (R < 2m(χ)) at η_trap = π − 2χ.
  - At the surface both happen when R = 2m. For interior shells η_EH < η_trap.
- **The surface criterion.** With N_H the surface's lapse when R_s = 2m, and assuming that N decreases monotonically along the surface's worldline:
$$
\text{OUTSIDE if }2\varepsilon_{\rm med}>N_H,\qquad \text{INSIDE if }2\varepsilon_{\rm med}<N_H,\qquad \varepsilon_{\rm crit}=\frac{N_H}{2}.
$$
  N_H > 0, since the lapse is positive at the finite time the surface crosses R = 2m.

### 2. What the literature gives

- **Lapse collapse.**
  - PST85 give the central lapse as N(t, 0) ~ A exp(−κt), with
$$
\kappa=\frac{4}{3\sqrt6\,m}=\frac{(2/3)^{3/2}}{m}=\frac{2\sqrt6}{9m}\approx\frac{0.5443311}{m},
$$
    t being proper time at infinity. This is reported by Brewin & Kajtar, who fit 0.54424 at the origin over 25 ≤ t ≤ 35, R₀ = 5m.
  - Beig & Ó Murchadha give the same exponent at the Kruskal throat.
  - The rate agreement is already I17 §2's.
  - The draft's vacuum control reproduces it: 0.5443311 (`val/validate.log`, V1c).
  - That the lapse at the dust *surface* also decays at κ is an **inference** from the single late-time rate, supported by SST95 ("inside r_s = 1.5M, the lapse function decreases exponentially"). The stationary trumpet's own approach rate at 3m/2 is (2√2/3)(1/√3) = κ (the check, log §B).
- **R₀ = 10m** (Scheel, Shapiro & Teukolsky 1995, SST95):
  - the apparent horizon forms at t ≈ 44m, at areal radius 2m outside the matter, and "already coincides with the event horizon";
  - the lapse decreases exponentially inside r_s = 1.5m;
  - "the matter particles sit at a constant areal radius after t = 50M" (rechecked against the PDF);
  - the surface is at about 1.5m at t = 87m.
- **R₀ = 4m** (Baumgarte, Hughes & Shapiro 1999, BHS99): "all of the matter has passed inside the event horizon by t=12.31M".
- **Late-time position.** The surface's areal radius tends to about 3m/2, the stationary trumpet's limit surface. Asymptotically, for 2ε_med ≪ N_H, the surface commits at
$$
t_c\approx t_H+\frac{1}{\kappa}\ln\frac{N_H}{2\varepsilon_{\rm med}}+O(1/\kappa),\qquad R_c\approx R_\infty+b_R\cdot2\varepsilon_{\rm med},\qquad R_\infty\approx\tfrac32m .
$$
  The O(1/κ) offset arises because the exponential law holds only after freezing (t ≈ 50m in SST95), not from t_H ≈ 44m.
- **The coefficient** (an **inference**, from the check). On a comoving shell dt/dτ = W/N exactly, with W the dust's Lorentz factor relative to the slice normal. At R = 3m/2 the late normal has zero Killing energy (α(3m/2; C_crit) = 0) and radial velocity C/R² = 1/√3, with f = −1/3. So
$$
W_\infty=\sqrt3\,|dR/d\tau|_\infty,\qquad \frac{dR}{dt}=-\frac{N}{\sqrt3},\qquad b_R=\frac{|dR/d\tau|_\infty}{W_\infty\kappa}=\frac{1}{\sqrt3\,\kappa}=\frac{3}{2\sqrt2},
$$
  independent of R₀. The R₀ dependence of |dR/dτ| (1.065 at R₀ = 10m, 0.913 at 4m) cancels against W. So I17 §2's coefficient, taken from the stationary trumpet, carries over to the collapsing surface exactly. This holds provided the surface lapse decays at κ and the surface freezes at 3m/2. The check confirms it numerically (W/(√3|dR/dτ|) = 1 at R₀ = 10, 5, 4, 2.5m; a toy integration gives 1.06070 and 1.06059 against 1.060660).
- **N_H** (an **inference** by analogy). No source read gives it. The stationary trumpet's α(2m) = 3√3/16 ≈ 0.325 suggests N_H ~ 0.1–0.3, which would put ε_crit ~ 0.05–0.15. The threshold lies above 10⁻³ unless the lapse had already fallen by a factor of about 500 when the surface reached 2m. SST95's account (exponential decay inside 1.5m, freezing after t ≈ 50m against crossing at 44m) argues against that.

### 3. Does R4 fix maximal slicing?

No. It is a choice.
- **R4** ("the clock field is fixed afresh each tick") is read as requiring an instantaneous slicing condition: the lapse is solved on each slice, with no evolution equation of its own. On that **reading** it excludes hyperbolic slicings such as 1+log. It does not select one instantaneous condition.
- **Run 65** fixes the static content, D²N = 4πN(e + 3p) (K65a–c). Any slicing whose slices are the static ones in a static field satisfies it.
- **Note H §8** reads the static medium energy, (∇ ln N)²/(8πG_N), as "the counterpart of GR's lapse equation in maximal slicing". That is a reading of the static energy. The non-static term N K_ijK^ij is not in R4 or R5. At ε = 0 it is GR's, so it is borrowed.
- **The I15 ruling** chose "maximal-type slicing, physical only in stationary fields".
- **The counterexample: polar slicing** (K^θ_θ = 0; Bardeen & Piran 1983). OS in polar slicing is solved analytically by Petrich, Shapiro & Teukolsky, *Phys. Rev. D* 33, 2100 (1986) (PST86).
  - Its lapse is fixed on each slice by a radial ODE.
  - It reduces to the static slicing in static fields.
  - In spherical vacuum its slices are Schwarzschild's t = const slices, so on the surface N = √(1 − 2m/R) exactly. Commitment then falls outside the horizon:
$$
\sqrt{1-2m/R}=2\varepsilon_{\rm med}\ \Rightarrow\ R=\frac{2m}{1-4\varepsilon_{\rm med}^2}>2m .
$$
  - It does not penetrate horizons (Choptuik et al., gr-qc/0403035 §IV: "the radial-polar slicing gauge does not penetrate BH horizons"). K^θ_θ = 0 needs dR = 0 along a timelike normal, which no trapped sphere admits.
  - Its exterior lapse is the Killing norm, which is R2's stationary reading (I17 choice 2). Late maximal slices instead approach the trumpet's lapse outside, α(2m) = 0.325 against n = 0 (I17 check).
  - The "outside" verdict is shown for the surface only. Interior shells cross the event horizon before they are trapped, and polar slices avoid only the trapped region, so interior shells were not computed.
  - **Symmetry caveat.** Polar slicing is defined only with symmetry (spherical; Bardeen & Piran extend it to axisymmetry with the radial gauge), whereas maximal slicing is defined in any geometry. A requirement that the slicing condition apply in every field would exclude polar slicing, but neither R4 nor Run 65 states one. Within spherical symmetry, R4 and Run 65 do not select maximal slicing.
- **Other standard slicings**, on the surface:
  - ingoing Kerr–Schild time: N = (1 + 2m/R)^{−1/2}, so commitment falls inside, at R = 8mε²/(1 − 4ε²);
  - Painlevé–Gullstrand time and geodesic slicing: N = 1 on the dust, so commitment never falls.
- **Consequence.** Collapse verdicts hold only in the chosen slicing. This restates I17 §2 ("In a collapse, the surface depends on the slicing … Different maximal slicings of the same hole even disagree on which side of r = 2m it lies") and Reading I15 §5's R11 row ("in collapse it needs a slicing-free definition").
- **A conflict with I17 §2's bullet "One case stays invariant during collapse".** That bullet says that, by Birkhoff, a thin shell's outer face reaches n = 2ε_med at r_c, before the horizon forms there. It reads N as the Killing norm on the outer face, the polar/static value. Under the maximal slicing the ruling names, the lapse on a collapsing dust surface is not the Killing norm (on the trumpet it is 0.325 at R = 2m, against n = 0), and commitment falls inside the horizon for small ε_med. The bullet holds only under the Killing-norm reading of N (I17 choice 2), and Reading I17 needs a dated note there.

### 4. Grades

| statement | grade |
|---|---|
| Maximal-slicing lapse on OS dust decays as exp(−4t/(3√6 m)); dust freezes; surface → about 3m/2; t_H ≈ 44m (R₀ = 10m), ≤ 12.31m (R₀ = 4m) | **restatement** (PST85; SST95; BHS99; Beig & Ó Murchadha; rate and trumpet value as in I17 §2) |
| Surface commitment INSIDE the horizon, near 3m/2, for sufficiently small ε_med (2ε_med < N_H), under maximal slicing | **restatement** |
| The threshold ε_crit = N_H/2 lies above 10⁻³ | **inference** (SST95's account; no N_H quoted) |
| N_H ~ 0.1–0.3 | **inference** (by analogy with the trumpet); **open** |
| The surface lapse decays at κ; b_R = 1/(√3κ) = 3/(2√2), independent of R₀ | **inference** (supported by SST95 and the check's numerics) |
| Maximal slicing as the medium's slicing | **reading** (chosen by the I15 ruling; not **derived** from R4 or Note H §8) |
| R4 excludes 1+log | **reading** of "fixed afresh each tick" |
| Polar slicing: OS solved analytically (PST86); surface commitment outside, at R = 2m/(1 − 4ε²); no horizon penetration | **restatement** (PST86, Choptuik et al., plus R2's reading) |
| Polar slicing meets R4 and Run 65 within spherical symmetry | **reading** (with the symmetry caveat) |
| Collapse verdicts hold only in the chosen slicing | **restatement** (I17 §2; I15 §5's R11 row) |
| Every interior shell crosses the event horizon within the maximal family; the centre is never trapped | follows from the geometry (a spacelike slice through a surface point with η > η_H stays above η_EH(χ)); not computed |
| Bearing on R11 | **inert** under choice 1(i) (commitment relabels matter; I15 ruling: "physical only in stationary fields") |

### 5. What is parked

The test to run **if R11's choice 1 is ever revisited** (for example, a rule that holds matter where it commits). It is drafted in `SCOPE.md` and `PREREG.md`, with validated code; it is not hashed and not run.
1. **N_H(R₀) and ε_crit = N_H/2,** at R₀ = 10m and 4m.
2. **The interior shells** (mass fractions 0, 0.1, 0.5, 0.9). For each: lapse at event-horizon crossing and at trapping, category, and frozen R∞ against 2m(χ).
3. **b_R** as a numerical confirmation only, since §2 gives 3/(2√2) under the stated conditions.
4. **The polar interior shells.** PST86 may already settle them analytically, so it should be read before any computation.

Before it is run, it would need:
- an independent check of the code against Reading I17 §2, Reading I15 §5, Run 65 and Note H §8;
- PST85 and PST86, fetched;
- a re-run of `validate.py`, then `hash.sh`.

1+log slicing is not part of it (excluded by R4, on the reading above).

### Sources

- **Fetched (by this reading or by its check):**
  - S. A. Scheel, S. L. Shapiro and S. A. Teukolsky, "Collapse to black holes in Brans–Dicke theory I", [arXiv:gr-qc/9411025](https://arxiv.org/pdf/gr-qc/9411025): OS at R₀ = 10m in maximal slicing. Quotes rechecked against the PDF.
  - T. W. Baumgarte, S. A. Hughes and S. L. Shapiro, "Evolving Einstein's field equations with matter: the 'hydro without hydro' test", [arXiv:gr-qc/9902024](https://arxiv.org/pdf/gr-qc/9902024): OS at R₀ = 4m; gives PST85's reference.
  - L. Brewin and J. Kajtar, [arXiv:0903.5367](https://arxiv.org/pdf/0903.5367): the rate −(2/3)^{3/2}, attributed to "Petrich et al." (no year); the maximal-slicing lapse conditions.
  - R. Beig and N. Ó Murchadha, "Late time behaviour of the maximal slicing of the Schwarzschild black hole", *Phys. Rev. D* 57, 4728 (1998), [arXiv:gr-qc/9706046](https://ar5iv.labs.arxiv.org/html/gr-qc/9706046). The journal reference is confirmed by the DOI on the arXiv page.
  - M. W. Choptuik et al., [arXiv:gr-qc/0403035](https://arxiv.org/pdf/gr-qc/0403035), §IV: polar slicing does not penetrate horizons (via the check).
  - Staley et al., [arXiv:1109.0546](https://ar5iv.arxiv.org/html/1109.0546), refs. [23]–[24], and Scilit: confirmation of the PST85 and PST86 references (via the check).
- **Reference confirmed, content second-hand:**
  - L. I. Petrich, S. L. Shapiro and S. A. Teukolsky, "Oppenheimer–Snyder collapse with maximal time slicing and isotropic coordinates", *Phys. Rev. D* 31, 2459 (1985). Paywalled, not read; the rate is via Brewin & Kajtar.
  - L. I. Petrich, S. L. Shapiro and S. A. Teukolsky, "Oppenheimer–Snyder collapse in polar time slicing", *Phys. Rev. D* 33, 2100 (1986). Not read; title and reference via Staley et al. and Scilit.
  - J. M. Bardeen and T. Piran, *Phys. Rep.* 96, 205 (1983). Confirmed in the Hebrew University repository (via the check); its abstract names the polar condition only.
- **Second-hand, not fetched:** F. Estabrook, H. Wahlquist, S. Christensen, B. DeWitt, L. Smarr and E. Tsiang, "Maximally slicing a black hole", *Phys. Rev. D* 7, 2814 (1973), from standard accounts.
- **The record:**
  - `gravity/reading_I17_black_holes.md` (§2, including "One case stays invariant during collapse"; §6 step 3; the Ruling) and `checkI17/REPORT.md`;
  - `gravity/reading_I15_borrowed_inputs.md` (§5, the R11 row; Rulings);
  - `ONTOLOGY.md` (R2, R4, R11);
  - Runs 65, 71, 73 and 74;
  - Note H §8 (`gravity/design_shear_waves.md`).

*Files in this folder:*
- *`READING_T-I17a.md`: this reading.*
- *`READING_T-I17a_v1_precheck.md`: the version before the check.*
- *`SCOPE.md` and `PREREG.md`: the parked registration (not hashed).*
- *Code: `geom.py`, `maxslice.py`, `polar.py`, `family.py`, `validate.py`, `run.py` (guarded; not run), `hash.sh` (not run).*
- *`val/validate.log` and `val/validate.json`: the validation output.*

*Ruled 30 October (Allen: "go ahead"): recorded as a reading; the registered remainder (N_H, ε_crit, interior shells) is parked, and would be run if R11's choice is revisited.*
