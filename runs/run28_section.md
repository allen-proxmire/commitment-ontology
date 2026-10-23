## 9u. Run 28: the strong field (ED's adopted metric against black-hole images and ringdowns)

**Question.** Under the adopted rules (Candidate A′, P₀ ≫ p_s), the clock gives $N=e^{-U}$ exactly. The pattern rule gives the spatial part. Outside a static body that is the exponential metric, which has no horizon:

$$
ds^2=-e^{-2M/r}dt^2+e^{2M/r}\left(dr^2+r^2d\Omega^2\right)
$$

What does it predict where gravity is strong, and do current observations allow it?

**Prior record (added later: "we've been here before, 4% and no horizon").** This calculation repeats ED_Attempt_03, note 5 (`Full_Locus_Strong_Field.md`, 15 September 2026, C26–C35). That note found the same metric, the same light ring at 2GM/c², the same 4.6% larger shadow, and the same 1.4σ and 1.0σ from EHT's Sgr A*. It went further on horizons:
- Sgr A*'s missing surface glow (any surface emits less than 0.4% of the accretion power) and quiet X-ray binaries put a horizonless object in strong tension.
- An escape check, under an exit rule fixed first, found at least 10% of the infalling energy escapes, 25 times the limit.
- **ED's strong-field line was closed** (C33–C34).

Attempt 1 had chosen the rate laws behind this metric (clocks $e^{-U}$, motion $e^{-2U}$; RD35–RD36) to match light bending and Mercury.

**What Runs 21–28 add.**
- Candidate A′ *derives* the $e^{-U}$ clock from counting rules on the engine, where attempts 1 and 3 had matched it. But it arrives at the same metric, so it inherits attempt 3's closure.
- The only new strong-field number here is the ringdown comparison with GW250114.
- **One difference that is unchecked:** attempt 3's capped core stopped the redshift at e. Candidate A′'s possibility instead runs out where $U\approx\ln(P_0/p_s)\approx8$, where clocks stop. Whether that deeper core escapes attempt 3's surface-glow argument has not been computed.
- **The check that should have come first:** This was run without first searching the earlier attempts.

This is a calculation, not a simulation. Pre-registered: `PREREG_28.md`, hashed after the calculation and before any bound except Sgr A*'s was looked up (disclosed); `strong_run.zip`.

**Predictions (`strong28.py`).** Static, non-rotating; G = c = 1.

| quantity | ED (exponential) | GR (Schwarzschild) | ED/GR − 1 |
|---|---|---|---|
| shadow, critical impact parameter | $2e\,M$ = 5.437 M | $3\sqrt3\,M$ = 5.196 M | **+4.6%** |
| light ring, areal radius | $2\sqrt e\,M$ = 3.30 M | 3 M | +9.9% |
| ringdown frequency, eikonal (light-ring Ω) | 0.1839/M | 0.1925/M | **−4.4%** |
| ringdown damping time, eikonal (1/Lyapunov) | 5.44 M | 5.20 M | +4.6% |
| scalar l = 2 mode, 3rd-order WKB (Mω) | 0.4650 − 0.0989i | 0.4836 − 0.0986i (exact 0.4836 − 0.0968i) | **f −3.9%** |
| scalar l = 3 mode, 3rd-order WKB | 0.6466 − 0.0923i | 0.6752 − 0.0962i (exact 0.6754 − 0.0965i) | f −4.2%, τ +4.2% |
| ISCO orbital frequency MΩ; areal radius; binding | 0.0633; 6.34 M; 5.48% | 0.0680; 6 M; 5.72% | −6.9% |
| horizon | none: a throat at r = M (areal e M ≈ 2.72 M) | at areal 2M | |
| $g_{tt}$, U³ coefficient (isotropic) | 4/3 | 3/2 | 2PN |

**The WKB rows** were added after registration as a robustness check. They show that the frequency shift is not an artefact of the eikonal limit: −3.9% at l = 2 and −4.2% at l = 3, against −4.4% in the eikonal limit. The WKB code reproduces Schwarzschild's exact real parts to 0.03%. Its l = 2 damping is 2% off, so the l = 2 damping time is not used.

**ED's own departure.** The medium is logarithmic only while P ≫ p_s. Possibility therefore runs out where $U=\ln(1+P_0/p_s)$: at isotropic r ≈ 0.13 M for P₀/p_s = 2000. That is beyond the throat, invisible from outside, and changes nothing in the table. (It would make an ED black hole's interior end in a region where clocks stop. That is untested.)

**Comparisons (as registered).**

| test | measurement | ED | verdict |
|---|---|---|---|
| C1, shadow: Sgr A* (VLTI mass prior) | δ = −0.08 ± 0.09 | +0.046 | **tension, 1.4σ** (inside 2σ) |
| C1, shadow: Sgr A* (Keck mass prior) | δ = −0.04 +0.09/−0.10 | +0.046 | pass (1.0σ) |
| C1, shadow: M87* | δ = −0.01 ± 0.17 | +0.046 | pass (0.3σ) |
| C2, ringdown frequency, GW250114 (pSEOBNR, 90%) | δf₂₂₀ = 0.02 ± 0.02 | −0.044 (eikonal), −0.039 (WKB, l = 2) | **outside the 90% interval, about 5σ: flag** |
| C2, ringdown damping time, GW250114 (90%) | δτ₂₂₀ = −0.01 +0.10/−0.09 | +0.046 | inside |

**Reading.**
- **The shadow is allowed.** ED's shadow is 4.6% larger than GR's. That sits inside every current EHT interval at 2σ, with 1.4σ tension against Sgr A* under one mass prior. The next generation of EHT measurements could decide it.
- **The ringdown is the first serious tension since the adoption.** For a static body, the exponential metric rings about 4% lower in frequency than a Kerr black hole of the same mass. GW250114, the loudest event so far, pins the dominant ringdown frequency to within ±2% of Kerr (90%). Taken at face value that is about 5σ.
- **It is a flag, not an exclusion, for three reasons, all registered beforehand:**
  1. **Rotation.** The estimate ignores the remnant's spin (a ≈ 0.7), and ED has no rotating solution yet; its frame dragging is untested.
  2. **The wrong field.** The modes are a scalar field's, not ED's gravitational perturbations; ED's wave sector (Run 11b) is not derived for strong fields.
  3. **Mass absorption.** LVK's test fits the whole signal. ED also shifts the inspiral (its ISCO frequency is 6.9% lower), so part of a common shift could be absorbed into the inferred masses.
- **What carries the strong field.** β and γ fix the metric only to first post-Newtonian order. Beyond that, the spatial part is set by the pattern rule's exact form ($c=N^2$, so $g_{ij}=N^{-2}\delta_{ij}$ at all orders), which was chosen to give γ = 1 at first order. The ringdown and the shadow test that choice. A different nonlinear form with the same β and γ would move both.

![Run 28](figures/28_strong.png)
