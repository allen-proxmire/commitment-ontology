## Working note: the line between matter and pattern, and what it does to route (b) (status, 27 October 2026)

*A dated status note, not a ruled reading. It records rulings made on 27 October during Reading I6, and the consequences found by independent checks. The numbers in §3 are unreviewed as a whole: a final independent review and Reading I6's final ruling are pending. The working draft of Reading I6 is in `reading_I6_matter_and_pattern_DRAFT.md`.*

### 1. Rulings made (27 October)

1. **The conditional picture** (Allen: "close to how I imagine CO's quantum to be"). A free body between records is a pattern, its phase turned by the committed world's count (A4). Matter keeps its rhythm, and a record strikes the beat.
2. **A renewal records nothing** (the restated A3′). It keeps no place, no count and no deposit beyond the body's records.
   - Records are placed by their interaction kernel.
   - Route (b) is exempt and localises at r_C.
   - Alternatives fail: a renewal that localised at any scale would heat matter (about 7×10⁴ W per nucleon at 10⁻¹¹ m); one that kept a count would carry which-path information in time; one that deposited gravity would remove the lunar and gas bounds.
3. **The clock chain, option (a).** Run 24's numbers stand as engine results. Their premise for physical clocks, a clock's self-dip, lapses, because renewals carry no deposit. That reopens:
   - p_s ≳ 4×10⁵;
   - gravity's P∞ ≳ 6.4×10¹⁰;
   - Note I's lower bound on ε;
   - the hop of about 10^2.5–10³ ℓ_P, and with it P-G-Closure (ℓ_ED = ℓ_P).

   The pulsar triple's P∞/p_s ≳ 1.6×10⁵ stays.
4. **Deposits, option (iii).** A gravity deposit lands only where a record fixes position, at that record's own Born outcome, over its kernel width.
   - Records that fix only internal states, such as how a solid's vibrations are shared, make no deposit.
   - The alternatives fail: drawing the place with an update heats matter; drawing it without one is nonlinear in the state, the (S)/Gisin signalling Reading I0 excluded.
5. **Reading (b) excluded.** A record that fixes a body's position lays down only the struck part's gravity, as T1 implies.
   - A whole-body deposit would put deposits at the far end of a rod at a time the near-end party chooses: (T2)-type timing.
   - It also has no linear placement. A fixed shape template is excluded by the measured gravity of a vibrating beam (Brack et al. 2022).
6. **A body's own route-(b) deposits act on it,** as M3 implies.

### 2. What follows

**Solids gravitate through route (b).** A solid's interior atoms are recorded only internally, so their gravity is laid down by route (b) alone, smeared at r_C:
$$
g(d)=\frac{GM}{d^2}\Big[(1-f)+f\,w(d/r_C)\Big],\qquad f=\frac{\lambda_b}{\Gamma_{\rm ext}+\lambda_b}\to1 ,
$$
with w the fraction of a Gaussian of standard deviation √1.5 r_C enclosed. Newton holds only at d ≫ r_C. This is the structure of GRW flash gravity (Tilloy 2018).

Three consequences:

- **Run 93's B13 loses its premise.** It assumed a solid's internal records deposit at fine resolution.
- **Run 94's B15 stands,** since gas collisions fix position.
- **The short-range cap.** The 52 μm inverse-square test (Lee et al. 2020) requires r_C ≲ 5×10⁻⁵ m, uncertain by about ±20% (`checkGamma2/`).

**A lower edge from gravity's graininess** (`checkGamma2/`; being re-derived in `checkFloor/`). A solid's gravity arrives in deposits of μ = ħ/(κ_b c²). LISA Pathfinder's test masses, including the pull of each mass's own deposits, then require
$$
\kappa_b\ \ge\ \frac{4\hbar J}{c^2M_{\rm TM}^2\,{\rm ASD}^2}\approx3.6\text{–}5.6\times10^{-36},\qquad J=\int\rho_{\rm src}\langle\tilde g_x^2\rangle\,dV .
$$

**Symmetrisation.** Under the ruled GRW-type symmetrisation (`checkSym/`), identical units within r_C share a localisation. Heating, emission and break-up fall by
$$
R=\frac{1}{2n(2\pi r_C^2)^{3/2}}\approx\frac{1}{31.5\,n\,r_C^3},
$$
which is 10¹²–10¹⁸ at r_C = 1–100 μm. So SNO, XENONnT and Earth's heat no longer bind there, and 'indep' (nucleons and electrons) and 'com' (atoms) have the same window. Run 92's note that the labelled bounds overstate "by up to the number of like units within r_C" understates the factor, which is about 7.5 times that number.

**Photon bounds** (`checkXray/`). A hit deflects a photon by σ_α = 1/(√2 r_C k) per axis, and the hits along a path number N = κ_b k_obs χ(z_S), with χ the comoving distance and the rate counted in the cosmic frame (M2).
- With χ in place of cT, HST's B5 becomes κ_b < 5.2×10⁻³⁴.
- X-ray imaging of distant quasars, from halo limits and spectral slopes, closes the window for r_C ≲ 2×10⁻⁵ m by 10–100×.

### 3. The current window (unreviewed as a whole)

*Update, 27 October (`checkXray2/`): fitting Chandra's point-spread function to published high-redshift quasar profiles narrows the strip further. See the end of this section.*


$$
3.6\text{–}5.6\times10^{-36}\ <\ \kappa_b\ <\ 2.8\times10^{-35}\ (\text{at }r_C=5\times10^{-5}\ \text{m}),\qquad 2\times10^{-5}\ \lesssim\ r_C\ \lesssim\ 5\times10^{-5}\ \text{m},
$$
so a·P∞ ≳ 3.5×10³⁴ under κ_b = 1/(aP∞).

- **What could close it.** A Chandra criterion that photons stay within a 1″–2″ core would close the strip by a factor of 1–1.6. That criterion is being pinned to published data (`checkXray2/`).
- **What it assumes.** Every photon bound assumes route (b)'s rate counts phase in the cosmic frame. If it counts along the worldline, photons never commit, and none of the photon bounds exist.

**The Chandra core criterion, pinned to published data** (`checkXray2/`).
- **The model.** Chandra's point-spread function is modelled as three Gaussians matching its encircled energy (0.733, 0.916, 0.954 and 0.967 at 0.5″, 1″, 2″ and 5″). Hits are counts-weighted over 0.5–2 keV.
- **The data.** Clean z = 3.5–4.6 quasars (Lopez et al. 2006; Bassett et al. 2004) allow an excess of about 0.1 of the soft counts beyond 1″ from statistics alone, and 0.2–0.3 once the model's systematics are included.
- **Below about 4×10⁻⁵ m the strip is closed** under every one of those criteria (by 2–7× at 2×10⁻⁵ m).
- **Near the cap, 4–5×10⁻⁵ m, it is undecided.**
  - An excess of 0.1 closes it, by 1.6–2.8×.
  - An excess of 0.2 leaves a sliver of 1.1–1.3×.
  - An excess of 0.3 leaves it open from about 3.5×10⁻⁵ m. Even then κ_b is capped at 6.2×10⁻³⁶ at the cap, so a·P∞ ≳ 1.6×10³⁵.
- **What would decide it.** At the floor, route (b) would at least double the soft-band core of every z ≈ 4 quasar, adding a symmetric blur of 0.4–0.7″ at the cap. That resembles Chandra's own aspect-blur correction. The test that would decide it compares high-redshift quasars with nearby stars on the same detector, epoch and band, and it has not been published.
- **CMB up-conversion does not bite in the strip.** It reaches only about 10⁻³ of the far-infrared background there, and stays below the FIRAS spectral-distortion limits. The earlier estimate of it was about 60–100× too high.
- **The LISA floor's dependence** (`checkFloor/`). The floor, 3.6–5.6×10⁻³⁶, is confirmed under the impulse model that Run 92 uses. If a deposit's field persisted instead, there would be no floor at all. Without the self term (that is, with action–reaction per deposit), it would be about 1–2×10⁻³⁶. Both are to be ruled.

### 4. Open

- A comparison of high-redshift quasars with nearby stars in archival Chandra data, which decides the cap region.
- Two rulings: whether a deposit acts as an impulse or a persisting field, and whether a single deposit conserves momentum.
- A final independent review of the whole chain.
- Reading I6's final ruling. Until then, ONTOLOGY's statements that rest on B13 (a·P∞ ≳ 3.7×10²⁴) and on Run 24's self-dip (p_s, P∞ ≳ 6.4×10¹⁰, the hop) are to be read as conditional.
- How a solid's draw is laid down at fine resolution, if at all: only route (b) and external position records do so under the rulings.
- If the strip survives, a registered run: r_C of 20–50 μm, testable by short-range gravity and X-ray imaging.
- If it closes, the chain (iii), T1 and route (b) cannot all stand, and one gives way.

### Checks
`checkI6/`–`checkI6f/` (Reading I6's drafts), `checkGamma/`, `checkGamma2/`, `checkRod/`, `checkSym/`, `checkXray/`, `checkXray2/`, `checkFloor/`, all REPORT.md; the working draft's earlier versions are in `readingI6/superseded/`.
