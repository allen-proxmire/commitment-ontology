# Targets from Run 99: what sets the near zone and the edge, and what would test them

*29 October 2026 (v2: exponent sign corrected; Run 100 split added). Post hoc and descriptive: read from the registered `quantum99/run99.json` (SHA-256 `e1688f09…`, asserted) by `targets99.py`; numbers in `targets99.log` and `targets99.json`. Not part of any registration.*

## Conversions
Every cost is linear in Γ_K, so each bound's Γ_max is linear in its measured limit. A point with q = Γ_max/Γ_K is tested once the binding measurement improves by q, expressed in that measurement's own quantity:

| bound | measured quantity X | Γ_max ∝ | improvement in X to test ratio q |
|---|---|---|---|
| LISA Pathfinder, MICROSCOPE (CM acceleration noise) | ASD | ASD² | √q |
| F, Vinante 2017 (force noise) | S_F | S_F | q |
| Earth's heat (47 TW), D1, Sun, WD | heat budget, luminosity | L | q |
| E, atmosphere | heating criterion (W m⁻²) | Q | q |
| G, G′ (in-band CSL) | λ/r_C² bound | λ/r_C² | q |

**Scaling in r_C at fixed ρ_K** (exponents measured from the stored grid, exact to 10⁻⁴):
$$
\frac{\Gamma_{\max}}{c/r_C}\propto r_C^{\,n+1},\qquad n=4\ \text{(LISA, A, F)},\qquad n=8\ \text{(Earth's bulk, E, G, G′; Earth's jumps } n=7).
$$
- **LISA:** the ratio goes as r_C⁵ and Γ_max as ASD², so r* ∝ ASD^{−2/5}. One fine step (×1.1412 in r_C) costs 1.141⁵ = 1.94 in Γ, which is ASD ×1.39.
- **Ge windows:** the ratio goes as r_C⁹, so r* ∝ (λ/r_C²)^{−1/9}. One step costs ×3.28 in λ/r_C². A bound 10× tighter moves r* by ×1.29, and 100× by ×1.67.
- **Earth's heat:** the ratio goes as r_C⁸ to r_C⁹. One step costs a heat budget ×2.9–3.3 tighter.

## Near zone (survivors with q ≤ 10)
**Fine grid: 378 points.**

| ρ_K (kg m⁻³) | binding bound | n (q ≤ 2) | r_C (μm) | q: min–median–max | improvement to test: first / half / all |
|---|---|---|---|---|---|
| 10²–10³ | LISA | 158 (54) | 0.385–0.573 | 1.005–3.2–7.8 | ASD ×1.003 / ×1.80 / ×2.78 |
| 10³–1.98×10⁴ | LISA | 194 (51) | 0.227–0.573 | 1.003–3.6–10.0 | ASD ×1.001 / ×1.88 / ×3.16 |
| 3.3–12×10³ | Earth's heat | 17 (6) | 0.338–0.502 | 1.04–2.3–5.1 | heat ×1.04 / ×2.3 / ×5.1 |
| 5248 | G′ (natural Ge) | 2 (1) | 0.851–0.971 | 1.99, 6.54 | λ/r_C² ×1.99 / – / ×6.54 |
| 5495–5754 | G (enriched Ge) | 4 (1) | 1.265–1.647 | 1.62–3.8–7.2 | λ/r_C² ×1.62 / ×3.8 / ×7.2 |
| 2.0–2.19×10⁴ | D1 (LHS 6343 C) | 3 (0) | 0.090 | 4.70–4.96 | luminosity ×4.7–5.0 (×12 against the 2024 log L = −4.77) |

**Coarse grid: 140 points.**
- **E, 44 points:** ρ_K 2×10⁻⁶–0.63, 0.44–2.15 μm, q 1.01–9.4. Testing them needs a heating criterion up to ×9.4 tighter. Only the ρ_K = 0.631 point lies in the troposphere.
- **LISA, 88 points:** 31 at ρ_K ≤ 10, 38 at 10–10³, 19 at 10³–1.98×10⁴. All lie at 0.338–0.573 μm and need ASD ×1.01–3.13.
- **Earth's heat, 2 points; D1, 6 points.**

## Edge r_C*(ρ_K), fine grid, 10² ≤ ρ_K < 1.98×10⁴
- **To move one step:** improve the bound binding at the edge grid point by that point's q. This excludes the point, and the edge rises by ×1.141.
- **To clear 1 μm:** improve the bound binding at #18 = 0.971 μm by its q there. Every r_C ≤ 0.97 μm is then excluded, and the edge rises to ≥ 1.11 μm.

| ρ_K (kg m⁻³) | rows | edge (μm) | set by | one step | clear 1 μm (binding at #18) |
|---|---|---|---|---|---|
| 100–661 | 42 | 0.440 | LISA | ASD ×1.22–1.39 | ASD ×8.9–10.1 |
| 692–3162 | 34 | 0.385 | LISA | ASD ×1.003–1.21 | ASD ×10.1–12.2 |
| 3311–5012 | 9 | 0.385–0.440 | Earth (8), LISA (1) | heat ×1.04–2.37, or ASD ×1.24–1.84 | ASD ×12.3–13.4 (LISA) |
| 5248 | 1 | 0.851 | G′ | λ/r_C² ×1.99 | λ/r_C² ×6.5 |
| 5495, 5754 | 2 | 1.444, 1.265 | G | λ/r_C² ×1.62, ×2.19 | already excluded |
| 6026–9550 | 11 | 0.338–0.385 | LISA | ASD ×1.01–1.39 | ASD ×14–16.5 |
| 1.00–1.20×10⁴ | 5 | 0.338–0.385 | Earth (4), LISA (1) | heat ×1.75–3.1, or ASD ×1.35–1.81 | ASD ×17–19 (LISA) |
| 1.26–1.58×10⁴ | 6 | 0.296 | LISA | ASD ×1.001–1.30 | ASD ×20–25 |
| 1.66–1.82×10⁴ | 3 | 0.259 | LISA | ASD ×1.02–1.37 | ASD ×28–37 |
| 1.905×10⁴ | 1 | 0.227 | LISA | ASD ×1.36 | ASD ×52 |

- **LISA sets 98 of the 115 rows, Earth's heat 14, and the Ge windows 3.**
- Under Run 100's prediction (H added), LISA sets 96 rows, H the two Xe rows (2754.2, 2884.0), Earth's heat 14 and the Ge windows 3.
- **In the Earth-set rows LISA's q at the edge point is at most 3× Earth's (and lower in two rows).** So a tighter heat budget alone moves those edges by at most a step or two before LISA takes over.
- **The Ge edges move slowly.** A Ge bound ×10 tighter gives 1.02 μm at 5248, 1.77 μm at 5495 and 1.50 μm at 5754.

## Reading
- The cheapest test of the near zone is a lower centre-of-mass noise per test-mass face area. ASD ×1.39 moves 100 of the 112 non-Ge rows by one step: the 98 LISA rows and 2 of the Earth rows. ASD ×3.2 covers every LISA-bound near-zone point.
- Moving the solid-density edge to 1 μm outside Ge needs ASD ×9–52, rising with ρ_K.
- In-band X-ray windows act only in rows within ±5% of a detector material's density, and they move as the ninth root of the bound. Their value lies in opening new rows, not in moving existing ones.
