## Run 68: do CO's holes evaporate under option 3?

*21 October 2026. Registered and hashed before the run (`evap68/PREREG_68.md`, 07:11 UTC). The claims were derived before registration; the run checks them numerically. A smoke test at an unregistered ε is disclosed in the registration. An independent agent checked the run; its corrections are included, among them two words ("burst", "thermal") that overstated what is emitted.*

**Question.** Run 67's static hole, under option 3 with CO's medium, has a cold zero-clock surface (κ = 0) and no event horizon. It was ruled on 19 October, under option A with Kerr's surface gravity borrowed, that black holes evaporate. Does a hole formed by collapse in this geometry radiate as Hawking's does, and for how long?

**Method.** The exterior is Run 67's (m = 1):
$$
ds^2=-N^2dt^2+N^{-2}\big(dr^2+(r^2-2mr)\,d\Omega^2\big),\qquad N=(1+\varepsilon)\,n-\varepsilon,\quad n=\sqrt{1-2m/r},\quad M_K=(1+\varepsilon)m .
$$
- **Outgoing rays.** Radial null rays have r* = ∫dr/N², u = t − r*, v = t + r*. Because g_tt g_rr = −1, the affine parameter along an ingoing radial null ray is linear in r. So the outgoing ray u crosses a reference ingoing ray at r(u), with dr/du = −N²/2.
- **The peeling function** (Barceló, Liberati, Sonego & Visser 2011, arXiv:1011.5911): κ(u) = −r″(u)/r′(u) = N N_r, the local surface gravity where the outgoing ray left.
- **The flux.** In the radial (1+1, s-wave) sector, the outgoing flux of a massless field is set by the Schwarzian derivative S of r(u):
$$
F(u)=-\frac{1}{24\pi}S[r](u)=\frac{1}{48\pi}\big(\kappa^2+2\dot\kappa\big)=-\frac{N^3N_{rr}}{48\pi}.
$$
  For Schwarzschild κ → 1/4M and F → F_H = 1/(768πM²), Hawking's flux at T = κ/2π.
- **Why this is the collapse's late-time flux.** For a collapse, the coordinate U at past infinity is a smooth function of the affine parameter λ along the collapsing matter's last ingoing ray. Since S(U∘λ) = S(U)λ′² + S(λ) and λ′(u) → 0, the late-time flux is the one above.
- **The duration.** Δu_eff = E/F_H(M_K), with E = ∫F du = −(1/24π)∫N N_rr dr counted from when F first reaches F_H/2. It is the time Hawking's flux would take to carry the same energy.

**Results.**

| ε = p_s/P∞ | peak F/F_H | Δu_eff (M_K) | late time: d ln F/d ln u | late time: κ(u)·u |
|---|---|---|---|---|
| 10⁻² | 0.9216 | 28.5 | −3.000 | 2.000 |
| 10⁻³ | 0.9836 | 45.8 | −3.000 | 2.000 |
| 10⁻⁴ | 0.9970 | 64.1 | −3.000 | 2.000 |
| 10⁻⁵ | 0.9995 | 82.5 | −3.000 | 2.000 |
| 5×10⁻⁶ | 0.9997 | 88.0 | −3.000 | 2.000 |
| 3.4×10⁻⁶ | 0.9998 | 91.1 | −3.000 | 2.000 |
| 10⁻⁶ | 0.99992 | 100.9 | −3.000 | 2.000 |
| 0 (GR) | 1 for ever | unbounded: 72, 109, 146, 183 M to N = 10⁻⁴, 10⁻⁶, 10⁻⁸, 10⁻¹⁰ | — | — |

![Runs 68–69](figures/68_69.png)

**Verdicts, as registered.**
- **K68a PASSES (the transient reaches Hawking's flux):** the peak flux reaches 0.997–0.9999 of Hawking's for ε ≤ 10⁻⁴.
- **K68b PASSES (then zero temperature):** at late times F ∝ u⁻³ and κu → 2, both to 10⁻⁶, at every ε. Near the zero-clock surface r(u) − r₀ ≈ 2L²/(u − v₀), a Möbius map, whose Schwarzian vanishes.
- **K68c PASSES (the duration):** Δu_eff grows as 7.88 M_K per unit of ln(1/ε) over five decades (registered 8 ± 2%; 8.0 between 10⁻⁵ and 10⁻⁶), with intercept −8.2 M_K. The independent check's earlier rough estimate, (4/3)M per unit, is ruled out.
- **K68d PASSES (GR control):** at ε = 0 the flux stays at Hawking's (to 10⁻¹⁵), and the emitted energy grows by 8.000 M per unit of ln(1/N), without limit.

**Reported, with the check's closed forms.**
- **The flux, exactly** (the check):
$$
\frac{F}{F_H(M_K)}=\big[(1+\varepsilon)\big((1+\varepsilon)-\varepsilon/n\big)\big]^3(1-n^2)^3(1+3n^2)\;\approx\;\Big(1-\frac{\varepsilon}{n}\Big)^3\big(1-6n^4\big).
$$
  Its peak is at n ≈ (ε/8)^{1/5}, with 1 − F_max/F_H ≈ 5.68 ε^{4/5}. That is not the throat, which sits at (ε/2)^{1/3}.
- **The duration, exactly:**
$$
\Delta u_{\rm eff}=8M_K\big[\ln(1/\varepsilon)-1\big]-1.617\,M_K .
$$
  This is GR's thermal flux cut off when the clock falls to N = eε, where the local possibility is P ≈ 2.7 p_s. It is the same law Harada, Cardoso & Miyata (2019) found for a surface at 1 − 2M/R = ε², which is where CO's zero-clock surface sits.
- **At the pulsar-triple bound** (ε ≤ 3.4–6×10⁻⁶) the transient lasts Δu_eff ≥ 86–91 M:
  - ≥ 4.3 ms for a 10 M☉ hole;
  - ≥ 27 ms for a GW250114-mass remnant (that remnant spins, so it is only a scale);
  - ≥ 31 minutes for Sgr A* (4.3×10⁶ M☉).

  These are lower limits, since ε is only bounded from above. ε = 10⁻¹² would still give only about 211 M.
- **How much comes out.**
  - In the 1+1 sector E/T_H = Δu_eff/96M ≈ 0.9: about one thermal quantum per field.
  - In 4D, greybody factors cut the power (photons and gravitons: L ≈ 3.76×10⁻⁵/M² against 4.1×10⁻⁴/M² per 1+1 field), so it is about 10⁻² quanta. Most likely nothing at all is emitted.
  - The mass lost is about 0.04(m_P/M)², about 5×10⁻⁷⁸ of a solar-mass hole.
  - Then it is silent.

**What the check added.**
1. **Everything reproduces with its own code**, which integrates the ray map as an ODE and uses its closed form: peak 0.99970386 at ε = 5×10⁻⁶; κu = 2.0000006; Δu_eff = 88.03303935; GR slope 8.000000005. K68c's fitted 7.88 is pulled down by the ε = 10⁻² point; the local slopes are 7.53, 7.92, 7.990 and 7.999. Its own earlier estimate of (4/3)M was wrong: it had used n ∝ e^{−u/4M} instead of e^{−u/8M}.
2. **The closed forms above**, and the match to Harada, Cardoso & Miyata (2019). The result is standard: horizonless objects radiate transiently (Barceló et al. 2011), and incipient extremal holes give a non-thermal flux that decays as a power law (Liberati, Rothman & Sonego 2000).
3. **The reference-ray argument is sound, but conditional.** The chain rule also needs the map from the collapse's past infinity to the endpoint to be smooth there, with p′ ≠ 0.
   - In GR that is guaranteed, because the star crosses a regular horizon. Here it is assumed.
   - A power-law map, p ∝ (λ₀ − λ)^α, would add a late flux −(1 − α²)/(48πu²). That dominates the u⁻³ tail, though the energy stays finite, and it scales the transient by α².
   - Only a second exponential peeling, meaning trapping inside the matter, would bring back a sustained flux.
4. **The collapse has to cross the throat, and nothing models that.** The radial null rays never see the areal radius, so the throat does not affect the flux, and being static it does not radiate. But infalling matter must pass through it.
   - A GR dust interior conserves Γ = ∂R/∂ℓ > 0, and Γ changes sign at the throat, so dust cannot follow. The crossing relies on the medium's stress inside the matter.
   - About 55 of the 88 M of Δu_eff is carried by rays that leave the matter inside the throat, where the 4D curvature radius is about Mε.
5. **What follows the transient depends on the endpoint.** Run 68 assumes the zero-clock surface absorbs. If the discrete regime (N < 1/P∞) reflected instead, echoes would return about 8M·p_s later (the agent's estimate, not computed).
6. **"Burst" and "thermal" were loose words.** The transient is an expectation value worth about one quantum (1+1), or 10⁻² in 4D. Its plateau lasts about 3.5 thermal times (1/T_H = 8πM), and during the switch-off |κ̇|/κ² → ½, so κ/2π is not a temperature there.
7. **Consequences to record.**
   - Primordial black holes never evaporate.
   - With T = 0 and an infinite-area zero-clock surface (only the throat, about 16πM², is finite), black-hole thermodynamics (S = A/4) does not carry over without a new argument.
   - The hole absorbs and never emits, so it grows slowly in the cosmic microwave background.

**Reading.**
1. **On Run 67's static exterior, the collapse's in-state emits GR's Hawking flux until the clock falls to N ≈ eε, then nothing. CO's holes do not evaporate.**
   - The thermal-equivalent duration is 8M_K[ln(1/ε) − 1] − 1.6 M_K, at least about 86 M at the pulsar bound.
   - After that the flux falls as u⁻³: zero temperature.
   - The transient carries about one quantum per field in the radial sector, about 10⁻² in 4D.
   - In CO's terms: possibility runs out (P ≈ 2.7 p_s) before the redshift can keep growing exponentially, and Hawking's flux needs that growth.
   - **Assumed:** a smooth collapse ray map at the endpoint; an absorbing zero-clock surface; p_s ≫ 1; a non-rotating hole; test fields. The collapse, including its passage through the throat, is not modelled.
2. **This conflicts with the ruling of 19 October that black holes evaporate.** That ruling was made under option A, with Kerr's surface gravity borrowed. The choices:
   - **(i) Revise it:** CO's holes are stable. What falls in stays as record, so "no information loss" holds trivially. This follows from the adopted rules with no new input.
   - **(ii) Keep evaporation as a tracked input**, by a mechanism outside the static mean-field medium: the core's own radiation in the earlier papers 039–052, or the discrete regime below one unit per place.
3. **What would tell.** For astrophysical holes the difference from GR is unobservable either way. For primordial black holes it is not:
   - in GR, primordial holes below about 5×10¹⁴ g have evaporated by now, and evaporation bounds limit them up to about 10¹⁷ g;
   - under (i) none of them evaporate, so those bounds lapse, and a detected evaporating primordial hole would count against option 3 with CO's medium;
   - black-hole thermodynamics (S = A/4) would need a new argument in CO.
4. **Limits.**
   - The 1+1 radial sector only; greybody factors change the flux, not when it switches off.
   - The collapse itself is not modelled in this modified theory; the static exterior stands in for its late stages.
   - Mean-field medium.
   - No back-reaction (negligible at this energy).
