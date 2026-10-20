## 9zk. Run 43: what option A implies for ED's core

*19 October 2026. Allen chose option A: "take GR's black-hole exterior as a tracked input, keep ED's no-singularity core." The calculation and its reading were registered before the code was written (`core/PREREG_43.md`, 13:58 UTC). An independent agent checked the numbers and the literature; its corrections are included.*

**What the input settles.** Outside a compact object the field is Kerr's. So GW250114's ringdown and the M87* and Sgr A* shadows match GR by construction, and are no longer tests of ED.

**What it opens.** Where GR has a horizon, ED has a core where possibility runs out. Its surface sits at a small lapse (clock rate) $\alpha_s>0$. Three kinds of observation test such a surface.

**1. Echoes.** Waves bounce between the surface and the light ring, and come back again and again, spaced by a fixed delay. For GW250114's remnant (a = 0.68; detector-frame mass 62.7 × 1.09 M☉, so GM/c³ = 0.3366 ms), the delay is
$$
\Delta t=2\int_{r_s}^{r_{\rm LR}}\frac{r^2+a^2}{\Delta}\,dr\;\approx\;\Big[\frac{2}{\kappa}\ln\frac{1}{\alpha_s}-9.7\Big]M,\qquad \kappa=\frac{r_+-r_-}{2(r_+^2+a^2)}=0.2115/M .
$$
- The integrand is Kerr's tortoise coordinate, which does not depend on latitude. Only where the wall sits is set by the equatorial lapse. A wall set by the polar lapse adds 0.23 ms.

| where the surface sits | lapse α_s | r_s − r₊ (Boyer–Lindquist radius, in M) | echo delay |
|---|---|---|---|
| where ED's medium changes regime (P ≈ p_s), at the smallest allowed P₀/p_s = 2.3×10⁴ | ≤ 4.3×10⁻⁵ | 5×10⁻⁹ | **≥ 85 M = 29 ms** |
| | 10⁻¹⁰ | 3×10⁻²⁰ | 208 M = 70 ms |
| | 10⁻²⁰ | 3×10⁻⁴⁰ | 426 M = 143 ms |
| one Planck length from the horizon | 3×10⁻⁴¹ | 3×10⁻⁸¹ | 871 M = 293 ms |

How to read the table:
- **The first row is a natural scale, not a derived surface.** The engine's lapse is P/P₀, and its medium changes regime at P ~ p_s. Whether lapse = P/P₀ still holds at P ~ p_s is untested.
- **P₀/p_s ≥ 2.3×10⁴ is a lower bound, so 29 ms is the shortest delay.** It grows by 7.3 ms for every tenfold increase in P₀/p_s, and reaches 50 ms at P₀/p_s ≈ 2×10⁷.
- **"One Planck length" is a proper distance s.** Near the horizon the lapse grows as α ≈ κs, while the coordinate gap r − r₊ grows as s². That is why the third column is so much smaller.
  - This row matches the standard formula 4M(1 + 1/√(1 − a²)) ln(M/ℓ_P) = 292 ms (Abedi et al.).
  - Using the source-frame mass for ℓ_P/M changes it by 0.3 ms.

**What the echo search says.** The GWTC-3 echo search covered O1–O3 events, not GW250114 (arXiv:2302.12158).
- It looked from 50 to 350 ms after merger (and 0.2 to 1.2 s for longer delays), and found no echoes.
- Its limits are 0.11–0.75 of the ringdown's strength (in h_rss over 15 events). That is the echo amplitude only if echo and ringdown have the same shape.
- For a remnant like GW250114's with a 29 ms delay, the first echo falls in the search's 50 ms blind time, but later ones (57, 86, … 344 ms) fall inside its window.

**So echoes at ED's natural scale are within reach of searches of this kind, unless the core absorbs enough to keep them weak.**

**2. The ergoregion instability.** Spinning objects without a horizon and with a reflecting surface amplify waves and spin down. Absorbing part of what reaches the surface quenches this (Maggio et al., arXiv:1807.08840):
- at least 0.3% for spin ≲ 0.7, which covers GW250114's remnant (0.68);
- at least 6% for spin ≲ 0.9;
- about 60% only if near-extremal objects must be stable.

**3. Surface glow.** If Sgr A*'s accreted energy hit a surface and was re-emitted as heat, the EHT would see it (Carballo-Rubio et al., arXiv:2205.13555).
- For a surface far closer to the horizon than ED's, that bound needs absorption κ ≪ 10⁻¹⁴. Absorption of 10⁻⁵ weakens it by about nine orders of magnitude, and near-total absorption (1 − κ ≈ 10⁻²) removes it.
- For a core at ED's natural scale (surface compactness μ = 1 − 2M/R ≈ α_s² ≈ 2×10⁻⁹), their eq. 18 needs only κ ≳ (27/8)μ/10⁻² ≈ 6×10⁻⁷.

![Run 43](figures/43_core.png)

**Reading** (corrected by the check: the registration said "viable only if the core is a strong absorber", which overstates it).
1. **Option A is viable if ED's core absorbs a few percent of what reaches it.**
   - That quenches the instability at the spins seen.
   - The surface-glow bound at ED's natural scale needs far less.
   - Current echo searches do not demand more.

   A perfectly reflecting core would fail the instability test.
2. **Near-total absorption is enough but not required, and it would make option A observationally silent in all three channels.** Partial absorption leaves echoes, and their spacing is set by ln(P₀/p_s): at least 29 ms for a GW250114-like remnant. That would be ED's distinctive signal under option A.
3. **So ED needs a rule for what happens at the core.** Allen ruled "it commits" (19 October; §9zl). The two options were:
   - **"A pattern or piece of matter that reaches the core commits."** It becomes record, so the core keeps it: a total absorber in ED's own terms. Infalling information goes into the record, not lost (Allen's "no information loss"). It passes every bound, and leaves no echo.
   - **A partly reflecting core.** It needs an ED rule for the reflected fraction, and would predict echoes spaced by ≥ 29 ms (for this remnant) with a strength set by that fraction.
4. **Whether the core re-emits is constrained, not ruled out.** If it radiates, as Allen's "black holes radiate" papers propose, the surface-glow bound limits how much of the infalling energy comes back out as thermal light.
