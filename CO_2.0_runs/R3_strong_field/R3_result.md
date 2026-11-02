# R3: the exponential metric in the strong field

Script: [`r3_strong_field.py`](r3_strong_field.py); numbers in `r3_result.json`. A short calculation, not a lattice run.

**Registered before running.** With ratio hopping the exterior is ds² = −e^{−2U}dt² + e^{2U}(dρ² + ρ²dΩ²), U = M/ρ. It agrees with GR through the classical tests and departs in the strong field. The shadow radius and ISCO are computed and set against Schwarzschild and the Event Horizon Telescope bounds. Outcome unknown; exclusion would rule out ratio hopping's exterior as written.

**Result** (G = c = 1, spin not modelled on either side).

| quantity | exponential metric | Schwarzschild | ratio |
|---|---|---|---|
| photon sphere (isotropic ρ) | 2M (exact) | — | — |
| shadow radius b | 2e M = 5.437 M | 3√3 M = 5.196 M | **1.046** |
| photon sphere, areal R | 3.30 M | 3 M | 1.10 |
| ISCO, areal R | 6.34 M | 6 M | 1.06 |
| ISCO orbital frequency Ω | 0.0633 /M | 0.0680 /M | **0.931** |

- The shadow is **4.6% larger** than Schwarzschild's: δ = +0.046 in the EHT deviation parameter. M87*: δ = −0.01 ± 0.17 (Psaltis et al. 2020). Sgr A*: about −0.08 ± 0.09 to −0.04 ± 0.09 depending on the mass prior (EHT 2022). **Not excluded**; at roughly 1σ for Sgr A*, well inside for M87*. Kerr's own shadow varies by a few percent with spin and inclination, which is of the same size as the departure, so present data cannot separate them. Next-generation EHT targets a few percent: a live kill test.
- The ISCO frequency is **7% lower**. This enters X-ray iron-line profiles, quasi-periodic oscillations, and the inspiral-to-merger transition in gravitational-wave signals. Not compared here.
- No horizon: e^{−2U} → 0 only as ρ → 0. The hole is a ceiling approached. The infall and ringdown of such an object are not Kerr's; ringdown spectra are not computed here and are the sharper test.

**Reading.** 2.0's first disagreement with GR survives current data by a margin of about one sigma on the best target and will be tested at the few-percent level. It is a prediction with a sign: shadows slightly larger than Kerr's, ISCO frequencies slightly lower.

**Owed, surfaced by this run.** Gravitational radiation. The binary-pulsar decay matches GR to 0.1%, and 2.0 has no wave equation: the quadrupole formula is derived from GR's field equations, not from the metric alone. A radiation rule in 2.0's words is needed before the inspiral can be compared.

**Post-run check.** The photon sphere at ρ = 2M and b = 2eM follow analytically from d/dρ(ρ²e^{4M/ρ}) = 0; the numerics reproduce them. ISCO found as the minimum of L²(ρ); the Schwarzschild check value Ω_ISCO = 6^{−3/2} is reproduced by the same formula on the Schwarzschild metric (not shown in the script; verified separately).
