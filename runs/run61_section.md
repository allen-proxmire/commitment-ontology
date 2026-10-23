## Run 61: ED's neutron stars against tidal deformability (GW170817) and radii (NICER)

*20 October 2026. The steps:*
1. *derive ED's exterior beyond first order and its tidal Love numbers, then use GW170817 and the NICER radii;*
2. *tighten K60b with a softer chiral-EFT base;*
3. *track the hop as an open tension (§3, §4).*

*Registered and hashed before the run (`tidal61/PREREG_61.md`, 18:00 UTC). One amendment before any result (18:25 UTC; below). An independent agent reproduced the run with its own code; its corrections are included.*

**Question.** Run 60 left ED two routes to PSR J0740+6620 (2.08 M☉) with matter that nuclear theory and QCD allow:
- **(a)** c_s² ≥ 0.33 from 1.1 n_s;
- **(b)** chiral-EFT-like matter to 2 n_s, then c_s² ≥ 0.8.

Stiff matter makes large stars that deform easily under a companion's tide. Does either route also fit how little the stars in GW170817 deformed, and the radii NICER measures?

**ED's exterior, beyond first order.** Outside a star the engine's metric is exactly
$$
ds^2=-e^{-2M/r}dt^2+e^{2M/r}\big(dr^2+r^2d\Omega^2\big)\qquad(\text{isotropic }r).
$$
- It agrees with Schwarzschild at first post-Newtonian order.
- The spatial metric differs at O(U²): e^{2U} = 1 + 2U + 2U², against Schwarzschild's (1 + U/2)⁴ = 1 + 2U + 1.5U².
- For light the medium acts as an optical index n(r) = e^{2M/r}.

**ED's tidal Love number (derived).** A static ℓ = 2 tide perturbs U by δU = H(r)Y₂ₘ.
- The matter stays in balance, h e^{−U} = const, so δh/h = δU.
- With dp = n dh and c_s² = dp/de, this gives δ(e + 3p) = (e + p)(3 + 1/c_s²) δU.
- The source's factor e^{2U} adds 2(e + 3p) δU.
- ED's field equation ∇²U = −4π(e + 3p)e^{2U} is linear in its flat Laplacian, so
$$
H''+\frac2rH'-\frac{6}{r^2}H=-4\pi e^{2U}\Big[(e+p)\Big(3+\frac1{c_s^2}\Big)+2(e+3p)\Big]H .
$$
- Outside the star the right side vanishes, so H = a r² + b r⁻³ exactly. The ratio b/(3a) is the tidal deformability λ, the same quantity the Newtonian limit and GR's asymptotic expansion define.
- With y = rH'/H at the surface and U_s = M/R_coord:
$$
\Lambda\equiv\frac{\lambda}{M^5}=\frac{2-y_s}{3\,(3+y_s)\,U_s^5},\qquad k_2=\frac{2-y_s}{2(3+y_s)}\ \text{(weak field)}.
$$
- GR's Λ (Hinderer 2008; Postnikov et al. 2010) is computed with the same equation-of-state code, for comparison.

**Data.**
- **GW170817:**
  - Λ̃ = 300 (+420/−230), the 90% highest-density interval with a low-spin prior (Abbott et al. 2019, PRX 9, 011001), so Λ̃ ≤ 720;
  - chirp mass 1.186 M☉, so equal masses of 1.362 M☉, where Λ̃ = Λ(1.362);
  - Λ(1.4) = 190 (+390/−120), 90% (Abbott et al. 2018, PRL 121, 161101). It was registered as reported only; it rests on GR's quasi-universal relations, so it is shown but not used as a test (the check).
- **NICER (68%):**
  - PSR J0437−4715: 11.36 (+0.95/−0.63) km at 1.418 M☉ (Choudhury et al. 2024);
  - PSR J0740+6620 at 2.08 M☉: 12.39 (+1.30/−0.98) km (Riley et al. 2021), 12.92 (+2.09/−1.13) km (Dittmann et al. 2024), 13.7 (+2.6/−1.5) km (Miller et al. 2021).
- **NICER's radii assume GR's exterior.** For ED's stars the run gives two "GR-equivalent" radii: the Schwarzschild radius with the same grazing deflection of light, and the one with the same surface redshift.

**Families.**
- **The softer base (new):** SLy to 1.1 n_s; then a constant c_s² = c₁ to 2 n_s, with c₁ = 0.10 (N3LO's central value; registered), or 0.03 and 0.17 (its 1σ edges); then c_s² = s.
- **Run 60's families:** route (a), SLy to 1.1 n_s then s = 0.35–1; route (b), SLy, APR4 or MPA1 to 2 n_s then s = 0.7–1.

**The amendment (before any result).** The first launch computed c_s² as a numerical derivative. Near the surface h − 1 falls below double precision, the derivative vanished, the tidal equation went stiff and the process ran out of memory. The fix uses the analytic c_s² = KΓn^{Γ−1}/h of each polytropic piece. It was recorded in the pre-registration and re-hashed before relaunch; nothing else changed.

**Verdicts, as registered.**
- **K61c PASSES (code check).** At weak field ED's Love number is 0.25986, against the Newtonian n = 1 polytrope's (15 − π²)/(2π²) = 0.25991 (largest deviation 0.06%). GR's code gives SLy Λ(1.4) = 296 at R = 11.71 km, against the literature's roughly 300. (GR's own weak-field values, 0.2624 and 0.2546, are cancellation noise in GR's k₂ formula at tiny compactness and are not a check.)
- **K61a PASSES (the softer base).** With N3LO's central c_s² = 0.10 from 1.1 to 2 n_s, ED holds a QCD-allowed 2.08 M☉ star for s ≥ 0.8 (M_max 2.10, 2.14, 2.18 for s = 0.8, 0.9, 1.0; 2.05 for s = 0.7). At c₁ = 0.03 it needs s ≥ 0.9; at c₁ = 0.17, s ≥ 0.7.
- **K61b PASSES (GW170817), conditionally.** Every route-(b) family that holds 2.08 M☉ has Λ_ED(1.362) = 374–658 ≤ 720. The condition (the check): the bound was extracted with GR's inspiral phasing through 3.5 post-Newtonian orders, which ED has not been shown to share (below).

| family (base, then c_s²) | ED M_max | Λ(1.362), ED (GR) | Λ(1.4) | R(1.418) [GR-equivalent] | R(2.08) [GR-equiv.: deflection / redshift] |
|---|---|---|---|---|---|
| **route (a):** SLy to 1.1 n_s, s = 0.35 | 2.14 | **1230** (1401) | 1068 | 13.93 [13.46] | 13.78 [13.02 / 13.57] |
| route (a): s = 1.0 | 2.91 | **1588** (1765) | 1400 | 14.41 [13.94] | 15.31 [14.57 / 15.14] |
| **softer base** c₁ = 0.10, s = 0.8 | 2.10 | 463 (570) | 395 | 12.18 [11.70] | 11.60 [10.78 / 11.31] |
| c₁ = 0.10, s = 1.0 | 2.18 | 475 (582) | 407 | 12.22 [11.74] | 12.03 [11.23 / 11.77] |
| c₁ = 0.03, s = 0.9 / 1.0 | 2.11 / 2.15 | 374 / 382 | 321 / 329 | 11.63 / 11.67 [11.14 / 11.18] | 11.38 / 11.61 |
| c₁ = 0.17, s = 0.7–1.0 | 2.10–2.22 | 651–658 (794–799) | 549–557 | 12.81–12.83 [12.33–12.35] | 11.98–12.51 |
| **route (b):** SLy to 2 n_s, s = 0.8 / 1.0 | 2.11 / 2.19 | 449 / 461 (552 / 563) | 384 / 395 | 12.08 / 12.12 | 11.61 / 12.01 |
| APR4 to 2 n_s, s = 0.8 / 1.0 | 2.09 / 2.17 | 408 / 423 (504 / 518) | 350 / 364 | 11.82 / 11.88 | 11.33 / 11.84 |
| MPA1 to 2 n_s, s = 0.7 / 1.0 | 2.08 / 2.21 | 506 / 518 (620 / 631) | 432 / 444 | 12.29 / 12.33 | 11.48 / 12.22 |
| **bound** | ≥ 2.08 | **≤ 720** (90%) | (≤ 580, shown only) | 11.36 (+0.95/−0.63), J0437 | 12.39 (+1.30/−0.98), J0740 (Riley) |

Radii are areal, in km; the GR-equivalent radius in brackets is the one with the same grazing deflection. Every 2.08 M☉ star listed passes the QCD test (X = 1, 2, 4); their centres are at 2.5–3.4 n_s on route (b) and 1.3–2.4 n_s on route (a).

**Reported.**
1. **Route (a) is excluded by GW170817 and disfavoured by J0437, independently.**
   - Λ(1.362) = 1230–1588, 1.7–2.2 times the 90% bound. A modest systematic in the inspiral phasing would not close a factor of about 2.
   - R(1.418) = 13.9–14.4 km (GR-equivalent 13.5–13.9 km): 1.1–1.6 km above the upper end of J0437's 68% interval (12.31 km).
2. **Route (b) fits GW170817 and J0437.** Λ(1.362) = 374–658 sits inside GW170817's 90% interval, above its median of 300. R(1.418) = 11.6–12.8 km (GR-equivalent 11.1–12.35 km) lies inside J0437's 68% interval, with c₁ = 0.17 at its upper edge.
3. **Route (b) is in mild tension with J0740's radius.** At 2.08 M☉ it gives R = 11.3–12.5 km in ED's metric; a GR-based analysis would read these stars as 10.5–11.7 km (same deflection) or 11.0–12.3 km (same redshift).
   - That sits at or below the lower ends of the 68% intervals: Riley et al. 11.41 km, Dittmann et al. 11.79 km, Miller et al. 12.2 km. In σ, the GR-equivalent radii are 0.7–1.9σ below Riley and up to about 2σ below Dittmann and Miller.
   - Route (a) (13.8–15.3 km) fits Dittmann and Miller and sits at Riley's upper edge.
   - Reported, not tested: NICER's pulse-profile fits were not redone in ED's metric.
4. **How large the metric difference is.** For the same star a GR-based reading is smaller than ED's areal radius by 0.47–0.49 km at 1.418 M☉ and 0.74–0.84 km at 2.08 M☉ (same grazing deflection), or by 0.07–0.10 and 0.17–0.31 km (same redshift). A real pulse-profile fit would land between the two.
5. **ED's stars deform less than GR's for the same matter:** Λ_ED(1.362) = 0.80–0.82 Λ_GR on route (b) and 0.88–0.90 on route (a). A star of given mass is more compact in ED (Run 57): at 1.4 M☉ about 0.2–0.3 km smaller.
6. **GR does not need any of these families.** With route (b)'s matter it would give 2.6–3.0 M☉ maxima and Λ(1.362) = 462–799; the c₁ = 0.17 families would fail GW170817 in GR (794–799).

![Run 61](figures/61_tidal.png)

**What the check added.**
1. **The tidal equation and Λ are confirmed.** The agent derived the ℓ = 2 equation itself (δe = (e + p)δU/c_s², δp = (e + p)δU, plus 2(e + 3p)δU from e^{2U}) and confirmed λ = b/(3a) as the quantity the leading tidal term of a waveform measures.
   - Changing from isotropic to areal radius adds no r⁻³ term (the change is a terminating polynomial).
   - Reading the response from g_tt = −e^{−2U} instead of from U changes Λ by only −4/45.
2. **The reproduction matches.** With its own code: route (b), SLy to 2 n_s with s = 0.8, Λ(1.362) = 448.8, R(1.418) = 12.079 km, R(2.08) = 11.607 km; route (a), s = 0.35, 1230.4, 13.927 and 13.780. Its own TOV gives SLy's GR Λ(1.4) = 295.6. Its own light-bending quadrature, in u = 1/r, matches the GR-equivalent radii to better than 1 m. The integration warnings came from the bracket end next to GR's photon sphere; the roots sit at R/M ≈ 3.5–4.5.
3. **Does GW170817's bound apply to ED? Conditionally.**
   - What carries over: the leading tidal physics. ED's exterior field is linear, so superposition and Newtonian tidal coupling hold exactly at that order, and the chirp mass is a far-field mass, as in GR.
   - What does not: Λ̃ was extracted with GR waveform models (GR point-particle phasing through 3.5PN, NR-calibrated tidal terms). Λ̃ enters at 5PN, so any ED difference at 1–3.5PN would bias it. ED's two-body dynamics beyond first post-Newtonian order, and its radiation beyond the leading quadrupole, have not been derived. The registered reading ("ED reproduces both") was too strong.
4. **Provenance.** The current files match the amendment's hashes, and the registration text is unchanged apart from the added amendment section. The original `star61.py` was not kept, so that only `cs2` changed rests on this record rather than on a hash. The analytic sound speed it now uses is correct (c_s² = KΓn^{Γ−1}/h = Γp/(e + p) for a polytropic piece).

**Reading.**
1. **ED survives the tidal and radius tests on one route only.** With ED's interior equations binding (the ruling), the heaviest pulsars, nuclear theory, QCD and GW170817 together leave ED one kind of dense matter:
   - like chiral EFT up to about 2 n_s (c_s² ≈ 0.03–0.17);
   - then a sharp stiffening, to c_s² of at least 0.7–0.9 (depending on the base below), from about 2 n_s up to the centres of the heaviest stars (2.5–3.4 n_s).
   - Route (a), stiff from 1.1 n_s, is excluded by GW170817 and disfavoured by J0437.
2. **This is a definite prediction about nuclear matter between 2 and 3 n_s, independent of gravity:** the sound speed must rise from about 0.1 to at least about 0.7–0.9 there. GR needs no such rise. Laboratory constraints at 2–4 n_s (heavy-ion collision flow) and nuclear theory carried to 2–3 n_s can test it.
3. **The surviving route is not comfortable.** Its heavy stars are small: J0740's radius sits 1–2σ above what a GR-based analysis would infer for them. Redoing NICER's fit with ED's exterior would make this a test.
4. **Conditions on the tidal verdict.** ED's Λ and radii here are its own, from its exact exterior and its own Love-number equation. K61b's PASS holds if ED's inspiral matches GR's through 3.5PN, which has not been derived. Route (a)'s exclusion is less exposed to that condition: it misses by a factor of about 2, and J0437 disfavours it without any waveform.
