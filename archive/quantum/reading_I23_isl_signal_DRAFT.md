## Reading I23: what a short-range gravity test would see of route (b) (draft)

*31 October 2026. Allen: "do #2" (the inverse-square test as the sharpest lever on route (b)'s window). A reading, plus arithmetic with Run 96's registered geometry functions (`i23_isl.py`, importing `quantum96/model96.py` unchanged; numbers in `i23_isl.log`). Not a registered test; it encodes no new rule. DRAFT v2, revised after an independent check (`/home/claude/checkI23/REPORT.md`), whose corrections are adopted; the pre-check version is `reading_I23_v1_precheck.md`.*

**In plain terms.** Under route (b) a solid's gravity is its mass smeared over a Gaussian of width σ = √1.5 r_C. A smeared source's field differs from Newton's only where the smearing reaches the test mass, or where it washes out the source's pattern. So the signal turns on steeply once σ approaches the gap and the plates' scale; it is not a Yukawa tail. At Lee's pattern, narrowing the gap helps only about twofold. With a finer patterned source, gap and pattern together are the levers, and precision sets how far they reach. A Lee-type torsion test at 10⁻³ precision would cut the cap from 51 μm to about 30 μm. With a pattern wavelength near 40 μm at a 10 μm gap, it would reach about 3.5 μm. Below a few μm, the window is out of reach of any foreseeable inverse-square test.

### 1. The signal (Run 96's construction)
- Lee et al.'s geometry: a detector slab of thickness 54 μm and an attractor of 99 μm, gap s, and a pattern wavenumber k = 120/22 mm.
- The quantity is the fractional change of the k-mode signal when the source's mass is smeared at σ = √1.5 r_C (Run 96's `_phiS`, `_slab`).
- Run 96's cap is reproduced: 5.11×10⁻⁵ m.
- As in Run 96, only the attractor is smeared. Smearing the detector as well would lower every r_C below by about 1/√2.

**Fractional change (negative: smearing lowers the signal):**

| r_C (μm) | 3 | 10 | 20 | 30 | 40 | 51 |
|---|---|---|---|---|---|---|
| s = 52 μm | 0 | −7×10⁻¹⁰ | −3.6×10⁻⁵ | −1.0×10⁻³ | −5.8×10⁻³ | −1.9×10⁻² |
| s = 10 μm | −1×10⁻⁸ | −1.4×10⁻⁴ | −2.8×10⁻³ | −1.2×10⁻² | −3.0×10⁻² | −6.2×10⁻² |

**Why it is steep** (a reading). The potential outside a source is harmonic, and Gaussian smoothing leaves a harmonic function unchanged. For the k-mode, the in-plane factor e^{−k²σ²/2} cancels exactly against the e^{+k²σ²/2} of the normal convolution. So the deviation comes only from smeared mass reaching the gap and the detector. When s > σ it is suppressed roughly as exp(−s²/2σ²): the gap sets the onset. That factor is an indicator, not the deviation: at r_C = 10 μm and s = 52 μm it is 1.2×10⁻⁴, while the deviation is 7×10⁻¹⁰.

### 2. What precision reaches which r_C

| set-up | 10⁻² | 10⁻³ |
|---|---|---|
| Lee geometry, s = 52 μm | 44 μm | 30 μm |
| Lee geometry, s = 10 μm | 28 μm | 16 μm |
| pattern ×10 finer (wavelength 115 μm), s = 10 μm | 8.5 μm | 5.8 μm |
| pattern ×30 finer (wavelength 38 μm), s = 10 μm | 4.6 μm | 3.5 μm |

The plate thicknesses are kept at Lee's throughout.

**The levers** (from the table and the check's sweeps):
- **At Lee's pattern,** going from a 52 to a 10 μm gap improves the reach about twofold.
- **With a finer pattern the gap dominates.** At k×30 and r_C = 5 μm the deviation is about 10⁻¹⁶ at s = 52 μm, 1.9×10⁻² at 10 μm and 0.17 at 1 μm.
- **The two levers are not separable.**
- **Plate thickness is a third lever.** At s = 1 μm and r_C = 10 μm: 6.4×10⁻⁴ at Lee's thicknesses, 2.1×10⁻³ at half, 7.2×10⁻⁵ at ten times.

**Signal size.** The Newtonian k-mode signal relative to Lee's set-up is 1.26 at s = 10 μm, 6.8×10⁻³ at k×10 and 9.0×10⁻⁵ at k×30. So the k×30 row asks for a 10⁻³ fractional measurement of a signal about 10⁴ smaller, against Casimir and patch forces. Whether that is feasible is an experimental question.

### 3. What it means
- **The window's top is testable** by an improved torsion-balance test: a 10⁻³-level test with a finer pattern would move the cap by an order of magnitude.
- **The interior below a few μm is, at best, marginal.** Under the set-ups computed (s ≥ 10 μm, Lee's thicknesses, 10⁻³), the reach stops near 3.5 μm (inference). At s = 1 μm and k×30 the deviation is still 4.4×10⁻⁴ at r_C = 1 μm, but the gravitational signal there is tiny and Casimir-dominated. Down to 0.09 μm the window rests on the floor (LISA Pathfinder) and on SNO.
- **The signature is distinctive.** It is a steep onset in r_C, set jointly by the gap, the pattern's wavenumber and the plate thickness, not a Yukawa tail. A null result at a given precision bounds r_C directly, through the table above. Mapping it onto the published (α, λ) exclusion plots needs the geometry, as Run 96 did; it cannot be read off them.

### 4. Choices for a ruling
1. Record the table as route (b)'s candidate prediction for inverse-square tests (a reading, using Run 96's registered functions).
2. Add to the README's "What would break it": "Lee-type tests reach about 30 μm at 10⁻³; with a ~40 μm pattern at a 10 μm gap, about 3.5 μm (inference, Reading I23)". Keep 0.09 μm as the closure condition. Also say plainly that route (b) is Tilloy-type gravity sourced by collapse events (Run 92 cites Tilloy 2018).

### Sources
- J. G. Lee et al., [arXiv:2002.11761](https://arxiv.org/abs/2002.11761).
- The record: `quantum/run96_section.md` (the cap); `quantum96/model96.py` (`lee_cap`, `_phiS`, `_slab`); Reading I21.
