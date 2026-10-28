### Run 99: C4-β with Γ_K = c/r_C, saturation at a fixed rate (a calculation, quantum runs)

*28 October 2026.*
- *Registered and hashed before the run (`quantum99/PREREG_99.md`, 18 files, 20:02:56 UTC), after three independent pre-registration checks (`checkPre99/`, `checkPre99b/`, `checkPre99c/`), whose corrections were adopted, and Allen's "go".*
- *Validated beforehand (53 checks, all PASS).*
- *Not blind: the verdict, and the map outside the germanium windows, were known before hashing (below).*
- *A second independent agent checked the registered run (`check99/REPORT.md`): the hashes verify, a re-run reproduces the output byte for byte, and its own code reproduces every new bound at 17 points (E and F to 10⁻⁵, G and G′ to 10⁻¹³). Its wording points are adopted below.*

**Why.** Reading I9 (ruled) found that no CO quantity fixes ρ_K at laboratory densities, but that Γ_K can be fixed by a lead that keeps Run 98's jump: a saturated cell commits once per light-crossing,
$$
\Gamma_K=\frac{c}{r_C}.
$$
That is the hold's ceiling at the scale of a cell, a ceiling read as a rate. α = 1 in c/(αr_C) is a choice. With the rate fixed, points can be excluded, so the test has power over the map, though not over the verdict.

**The test.**
- C4-β as in Run 98, with ρ_K free and r_C in Run 96's window.
- A point survives if:
  - a cell at ρ_K holds at least 10 nucleons;
  - every bound allows c/r_C;
  - c/r_C ≥ 10λN_cell at the floor κ_b.
- The bounds:
  - Runs 98 and 98a's;
  - **E**, the atmosphere: US Standard Atmosphere 1976, P/A ≤ 1 W m⁻², fair above about 19 km on local heating rates;
  - **F**, a levitated magnetic microsphere's force noise (Vinante et al. 2017; r_C ≤ 2 μm);
  - **G**, enriched-germanium X-rays (Majorana Demonstrator 2022, λ/r_C² < 0.494 s⁻¹ m⁻²);
  - **G′**, natural-germanium X-rays (Donadi et al. 2021, its Ge term, 70.2 s⁻¹ m⁻²).
- Inside the band where ρ_K matches a material's density, the channel is exactly mass-proportional CSL, which is why the X-ray limits apply:
$$
\lambda_{\rm eq}=\frac{\Gamma_K\,(S'm_0/\delta\rho)^2}{2^{3/2}V_c^2}.
$$
- Registered in advance: the edge r_C\*(ρ_K) below which no onset survives, at 115 densities from 10² to 1.98×10⁴ kg m⁻³. It was predicted from one evaluation of every bound at the window's lower edge plus exact scaling laws (Γ_max ∝ r_C⁴ or r_C⁸), and required to agree exactly, with no holes.

**Result.**
- **K99: LEAD AT LABORATORY DENSITIES** (foregone).
- **The predicted edge agrees** at 115 of 115 densities, with no holes, including the three germanium rows. That checks the method, not the theory. Outside the germanium rows the whole survivor map equals the one computed from Run 98a's bounds before registration.

| quantity | fine grid (49 r_C × 118 ρ_K, 10²–osmium) |
|---|---|
| survivors, 10³–1.98×10⁴ kg m⁻³ (a laboratory bound applies) | 2473 of 3185 |
| edge r_C\* outside germanium | 0.23–0.44 μm (LISA Pathfinder in 98 rows, Earth's heat in 14) |
| edge in the germanium rows | 0.85 μm at 5248 (natural Ge), 1.44 μm at 5495 and 1.26 μm at 5754 kg m⁻³ (enriched Ge) |
| near zone, Γ_max/Γ_K ≤ 10 | 378 points (LISA 352); 113 within 2×; the closest 1.003 at 0.296 μm, 1.26×10⁴ kg m⁻³ (LISA) |

- **Named lines.**
  - **C1b with c/r_C** (K = P∞, one unit per cell): **EXCLUDED** at every r_C of its own window, by 14–17 decades (interference).
  - **The per-particle regime:** excluded everywhere (interference).
  - **C1a with K = 1** (a hop mass per cell): survives at laboratory densities only at large r_C, 45–51 μm (P08) or 5.4–51 μm (engine), with margins ≥ 10⁶.
- **Variants** (reported only):
  - α = √(2π): 4635 survivors; edges about 0.83× lower where LISA sets them.
  - Majorana with quasi-free electrons only: 6 more survivors.
  - Donadi's published all-component bound: no change.
- **A registered statement failed.** "E's tropospheric part classifies no point alone" fails at one coarse point: r_C = 0.44 μm, ρ_K = 0.50 kg m⁻³, at 8.4 km. There 1 W m⁻² is 0.2 K/day, which the criterion itself calls unobservable.
  - The point is excluded as registered, and is reported as "E-only, tropospheric, not observable". LISA allows it by 0.5%.
  - The registration's claim that no grid point lies in E's tropospheric interval rested on a check at ρ_K = 0.3 only. The interval spans 0.3 < ρ_K ≲ 0.65.
  - Registered coarse counts: 2022 survivors at ρ_K ≤ osmium, 140 in the near zone. With the point reclassified: 2023 and 141.

**What it would take to test it.**
- **Centre-of-mass noise.** Γ_max ∝ ASD², so a near-zone ratio q needs an acceleration noise √q better at fixed geometry:
  - 3.2× covers the whole near zone;
  - 7.8× moves the LISA-set edge from 0.44 to 1 μm.

  The LISA mission's requirement is no better than LISA Pathfinder's achieved noise. A test needs lower force noise per unit face area.
- **Germanium.** r\* ∝ (λ/r_C²)^{−1/9}, so a 10× tighter X-ray bound moves the germanium edges only 1.29×. These windows test only ρ_K within ±5% of germanium's density. Other detector materials (liquid xenon, TeO₂, CaWO₄) would open rows of their own; they are flagged, not registered.

**What it means.**
- **With the rate fixed at c/r_C, saturation leaves a definite, testable map,** not a free family over 7–33 decades.
  - If this candidate is right, route (b)'s coarseness must exceed about 0.23–0.44 μm at solid densities (up to 1.44 μm near germanium's). That is conditional on adopting C4-β with c/r_C; it is not a bound on route (b) itself.
  - Large parts of the allowed region sit within a factor of a few of present limits.
- **It remains a lead, not a result:**
  - c/r_C is a ceiling read as a rate, with α a choice;
  - ρ_K is free, so the map describes a family of candidates indexed by ρ_K;
  - the ×10 onset is a proxy;
  - "survives" means consistent with the registered bounds, not evidence for the theory.
- **The CO-native threshold (C1b, one unit per cell) is excluded** at this rate.
