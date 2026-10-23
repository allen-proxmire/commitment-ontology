## Run 69: which clock does CO's medium follow around a spinning hole? Two readings compared

*21 October 2026. Registered and hashed before the run, and before any literature for its criteria was searched (`spin69/PREREG_69.md`, 07:14 UTC). The literature was compiled afterwards by the registered criteria (`lit69.json`). An independent agent checked the run.*
- *Disclosed: some of the spin measurements were known when the criteria were set.*
- *The first compile missed an event that meets K69c's criterion, and the check found it. The verdict flips from "not challenged" to "challenged". The first compile is kept (`lit69_first_compile.json`).*
- *The exclusion of the ringdown-model (pSEOBNR) spins was decided after the numbers had been seen.*
- *The check also found that the first argument from CO's rules was wrong. Its corrections are included.*

**Question.** In a static field the medium's clock is unambiguous: N = P/P∞. Around a spinning hole two clocks are natural. The check on Runs 66–67 found that the near zone of a spinning hole, and with it GW250114, depends on which one the medium follows.

**The two readings** (Kerr, M = 1, Boyer–Lindquist; Σ = r² + a²cos²θ, Δ = r² − 2r + a², A = (r² + a²)² − a²Δ sin²θ).
- **K (Killing norm): the clock of a place held fixed.**
$$
N_K=\sqrt{F},\qquad F=-g_{tt}=1-\frac{2r}{\Sigma},
$$
  zero at the ergosurface r_E(θ) = 1 + √(1 − a²cos²θ).
- **Z (ZAMO lapse): the clock of observers who move with the frame dragging (zero angular momentum).**
$$
N_Z=\alpha=\sqrt{\frac{\Delta\,\Sigma}{A}},
$$
  zero at the horizon r₊ = 1 + √(1 − a²). A clock held fixed moves relative to these observers and ticks slower by the Lorentz factor, α√(1 − v²) = √F, as in GR.
- Both readings agree with GR on every clock. They differ on where the medium itself runs out.
- **Model, for both:** Run 67's mean field. The clock stops where the reading's GR clock equals ε/(1 + ε) (ε = 5×10⁻⁶). Outside that surface the field is Kerr to O(ε/clock); inside it there is no medium.
  - The check: this is bookkeeping for where the medium ends. Neither reading solves option 3's stationary equations with the medium; the twist coupling and the shell's shape are assumed Kerr's.

**Results.**

| spin a | horizon r₊ | K: clock stops (equator) | Z: clock stops (equator) | prograde light ring | prograde ISCO | K's clock at the light ring | Z's clock at the light ring |
|---|---|---|---|---|---|---|---|
| 0 | 2.000 | 2.000 | 2.000 | 3.000 | 6.000 | 0.577 | 0.577 |
| 0.5 | 1.866 | 2.000 | 1.866 | 2.347 | 4.233 | 0.385 | 0.422 |
| 0.68 (GW250114) | 1.733 | 2.000 | 1.733 | 2.050 | 3.484 | 0.156 | 0.332 |
| 0.75 | 1.661 | 2.000 | 1.661 | 1.917 (inside K's surface) | 3.158 | — | 0.289 |
| 0.9 | 1.436 | 2.000 | 1.436 | 1.558 (inside) | 2.321 | — | 0.168 |
| 0.95 | 1.312 | 2.000 | 1.312 | 1.386 (inside) | 1.937 (inside) | — | 0.112 |
| 0.998 | 1.063 | 2.000 | 1.063 | 1.074 (inside) | 1.237 (inside) | — | 0.019 |

- **Under K the medium ends just outside the ergosurface**, at r = 2M on the equator, so the ergoregion is gone.
  - The prograde equatorial light ring falls inside it for a > 1/√2 (computed 0.70710678).
  - The prograde ISCO falls inside it for a > 2√2/3 (computed 0.94280904).
  - **Shadow edge.** The arc-length fraction of the shadow's edge made by photon orbits that dip inside is 12% at a = 0.75 seen edge-on, 22–24% at a = 0.9 (50°, 90°), and 14–28% at a = 0.99 (17° to 90°). It is zero for a ≤ 0.68, and zero at M87*'s 17° until a > 0.970 (the check).
  - **K's boundary need not absorb** (the check). Replacing √F by N_K in g_tt leaves the t–φ block Lorentzian, so waves do not see an infinite tortoise distance there. Whether K's boundary absorbs or reflects is undetermined. At a = 0.68 it sits only 0.45M of tortoise distance inside GW250114's prograde light ring.
- **Under Z the medium ends just outside the horizon at every spin.**
  - Light rings, ISCOs and the ergoregion are Kerr's to O(ε/α): at most 4×10⁻⁴ at the light ring and ISCO for a ≤ 0.999 (the check).
  - The shell where α is a few ε is not computed. Changing only the lapse does not reproduce Run 67's throat and horn, which came from the spatial metric.

**Verdicts, as registered.**
- **K69a PASSES:** the critical spins match 1/√2 and 2√2/3 to 3×10⁻¹¹ (the check, solving the orbit conditions directly: 3×10⁻¹¹ and 6×10⁻¹²).
- **K69b: K is disfavoured, formally**, by three objects; the criterion needs two. Each one is now contested, so the verdict rests on the X-ray methods as a whole, not on any single robust object.
  - **Cyg X-1:** continuum fitting gives a > 0.9985 at 3σ (Miller-Jones et al. 2021; Zhao et al. 2021). Contested: fits with a warm Comptonizing layer give a* ≈ 0 (Zdziarski et al. 2024), and IXPE's soft-state polarization favours low spin (Niedźwiecki et al. 2026).
  - **MCG–6-30-15:** reflection gives a > 0.987 at 90% (Brenneman & Reynolds 2006). A finite-thickness disc gives 0.87–0.99 (Jiang et al. 2022).
  - **GRS 1915+105:** continuum fitting gives a > 0.98 (McClintock et al. 2006), contested by Mills et al. 2021 (0.86). Its NuSTAR reflection spin is 0.98 ± 0.01 (Miller et al. 2013).
  - Across 36 NuSTAR reflection spins, 86% are consistent with a ≥ 0.95 at 1σ (Draghis et al. 2024).
- **K69c: K is challenged by GW231028_153006** (corrected by the check; first recorded as "not challenged").
  - Its GR-based remnant spin is 0.84 (+0.05/−0.10), a 90% lower bound of 0.74 > 0.707, and its Kerr ringdown fits are consistent with GR (GWTC-4.0 tests of the remnants, arXiv:2603.19021).
  - pSEOBNR puts GR at the edge of its 90% region for this event, which the paper partly attributes to waveform systematics. A ringdown prediction specific to K would test it directly.
  - The other remnants are below the threshold: GW250114 at 0.68 ± 0.01; GW231123 at 0.84 (+0.07/−0.19); GW190828 at 0.76 ± 0.07.

![Runs 68–69](figures/68_69.png)

**What the check added.**
1. **The geometry is confirmed with independent code.** Light-ring and ISCO conditions were solved directly; every tabulated radius and clock agrees to 10⁻¹⁰; the shadow fractions agree to 0.003.
2. **The first argument from rule C1 was wrong.** It held that C1 (patterns ride possibility's flow, g₀ᵢ = −uᵢ) makes possibility flow with frame dragging, so the medium's own frame is the ZAMO frame. But on the record's own Run 34 analysis, possibility's flow is always a gradient, and "a stationary rotating body makes no flow at all". Kerr's g_tφ comes from the input current field (the Lorentz input's momentum channel), not from that flow. Reading Z therefore needs a ruling that the input current field is itself a flow of possibility.
3. **CO's rules do not decide between the readings.**
   - For K: Run 34 writes g₀₀ = −N², which in stationary lattice coordinates is the Killing norm. Run 66's variables generalise to the stationary (Ernst) reduction, U = −½ ln F. And occupancy is defined per fixed place.
   - For Z: Run 65 identified CO's field equation with GR's lapse equation, and the lapse of Kerr's natural (maximal) time slices is α. The Lorentz-input picture, in which moving clocks run slow relative to the medium, also works only if the medium's frame is orthogonal to the tick's slices.
4. **Jets are the strongest observational argument against K.**
   - Blandford–Znajek jet power needs the ergoregion, not the horizon (Komissarov 2008), and K removes the ergoregion at every spin.
   - The EHT's M87* models without spin fail on jet power (Paper V). Under K the hole's spin energy is not available to the jet, so K would sit with those failing models whatever the spin.
   - This is model-dependent: the jet simulations are GR's, K's near zone is undefined, and disc-powered jets are not excluded.
   - K would also remove superradiance.
5. **"The vacuum draws nothing" is a claim about statics only.** With rotation, the clock equation gains a vacuum source in either reading: the twist term for K, the extrinsic-curvature term αK_ijK^ij for Z.
6. **Under Z, near-extremal spins are not a worry for observables.** ε/α at the light ring is 2.6×10⁻⁴ at a = 0.998 and 3.0×10⁻⁴ at Cyg X-1's bound. O(1) effects need α ≈ ε, i.e. 1 − a ≈ 10⁻⁸.
7. **Other readings exist.** Rigid co-rotation with the horizon would end the medium at a light cylinder (3.96M at a = 0.68), which is excluded at once.

**Reading.**
1. **CO's rules do not decide which clock the medium follows in rotation.** Run 34's g₀₀ and Run 66's variables suggest K; Run 65's lapse identification suggests Z. C1's flow vanishes for stationary rotation, so it decides nothing.
2. **The data favour Z.**
   - K is disfavoured by X-ray spins, formally; each object is contested.
   - K is challenged by GW231028_153006.
   - K removes the ergoregion, and with it the Blandford–Znajek jet power that the EHT's M87* models need.
3. **Adopted provisionally (§3): reading Z.** It comes with a stated premise: the input current field (the Lorentz input's g₀ᵢ) is read as a flow of possibility, so the medium's frame is the zero-angular-momentum frame. This premise is flagged. Under Z:
   - rotating holes are Kerr outside the horizon to O(ε/α), at most about 4×10⁻⁴ at the light ring and ISCO;
   - GW250114's ringdown is Kerr's to that order;
   - the medium ends just outside the horizon.
4. **Not computed:**
   - option 3's stationary equations with the medium (the near zone, the twist term, and whether the shell absorbs);
   - superradiance and jets, which should be Kerr's under Z because the ergoregion is intact;
   - the Hawking transient of a spinning hole (Run 68's analogue).
