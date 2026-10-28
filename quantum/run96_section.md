### Run 96: route (b)'s window under Reading I6 (a calculation, quantum runs)

*28 October 2026.*
- *Registered and hashed before the run (`quantum96/PREREG_96.md`, 11 files, 12:15:28 UTC). This followed an independent pre-registration check (`checkPre96/REPORT.md`), whose corrections were adopted, and Allen's "go".*
- *Validated beforehand (V1–V11, all PASS).*
- *Not blind. The calculation is deterministic, and its outcome was visible before hashing in the inputs, the smoke test and two full executions of the draft code (PREREG §6).*
- *A second independent agent checked the registered run (`check96/REPORT.md`). It reproduced every number from its own code, and its corrections are adopted below as a post hoc addendum. K96 is unchanged.*

**Why.** Reading I6 (ruled 28 October) made route (b) the only way a solid's interior gravitates. It set the window that route (b)'s rate (κ_b) and coarseness (r_C) must lie in as Run 96's registration target. Run 96 freezes that window's edges, data and code, then computes it once. The window's top edge is now set by the measured thermal history of the intergalactic medium (B7′). It replaces Run 92's B7, an estimate that was compared with no measurement (`run96_inputs.md`).

**The edges** (`model96.py`).
- **Lower: LISA Pathfinder.** A test mass's own deposits must not exceed its measured acceleration noise:
$$
\kappa_b\ \ge\ \frac{4\hbar J}{c^2M_{\rm TM}^2{\rm ASD}^2}=3.634\times10^{-36}\ \text{(self term)},\quad 5.617\times10^{-36}\ \text{(with an assumed solid Mo housing; primary)}.
$$
- **Top:** the least of the registered upper bounds, under the worldline rate and GRW-type symmetrisation:
  - SNO's deuteron break-up;
  - B7′;
  - Rb-atom and 172 kDa-cluster interference;
  - LISA's centre-of-mass kicks;
  - XENONnT;
  - Earth's heat;
  - B14 and B15.

  Two bounds are set aside:
  - **B5**, the photon bounds, lapses under ruling 11.
  - **B6′**, Run 92's per-pattern *neutrino* bound, falls under Run 92's per-population ruling and Reading I6 §4. It is not a photon bound, as Reading I6 §5 lists it. If B6′ applied, it would close the window.
- **B7′.** Every free particle's centre of mass gains, whatever its mass,
$$
P=\frac{3\kappa_bc^2\hbar}{4r_C^2},\qquad \frac{dT}{dt}\Big|_b=\frac{2P}{3k_B}.
$$
  The mean-density IGM temperature is integrated from z = 200, with Hubble cooling, Compton coupling and recombination plus free-free cooling. There is no photoheating, which is conservative by about 5×. It is compared with 20 measured T₀(z):
  - Hu et al. 2026, z = 0.1–0.4;
  - Ondro & Gális 2021, z = 1.7 and 1.9;
  - Walther et al. 2019, z = 1.8 (read second-hand);
  - Gaikwad et al. 2021, z = 2.0–3.8;
  - Boera et al. 2019, z = 4.2–5.0.

  The cooling is H II recombination and free-free only. That makes the bound about 2% tighter than with full cooling, which is not conservative but is immaterial.

  The bound is a combined one-sided test at 95%, in which a point counts only when T_b exceeds T₀:
$$
\mathrm{TS}(P)=\sum_{T_b>T_0}\Big(\frac{T_b-T_0}{\sigma_{\rm up}}\Big)^2\ \ (\text{Hu et al. in }\log_{10}T),\qquad \sum_{n}\binom{N}{n}2^{-N}\chi^2_{n,\rm sf}(\mathrm{TS})=0.05 .
$$
- **Right: Lee et al. 2020.** The 52 μm inverse-square test is applied with the interior's gravity smeared at √1.5 r_C.

**The decision rule (K96).**
- **FAIL** if the window is empty.
- **PASS (FRAGILE)** if any of nine registered variants empties it. These are:
  - R1, the photoheated form;
  - R2, Leo T;
  - R3, Run 92's B7;
  - R4, one nucleon species;
  - R5, without XENONnT's excitation estimate;
  - R6 and R7, the cap at 1% and 0.3%;
  - R8, the self-term floor;
  - R9, the tightest single point.
- **PASS** otherwise.

K96 has essentially no power: emptying the window would take a factor of about 3×10⁸ (below). What is registered is the numbers.

**Result: K96 PASS.**
$$
5.62\times10^{-36}<\kappa_b<\min\!\big(0.948\,r_C^5,\ 7.29\times10^{-19}\,r_C^2,\ 2.82\times10^{-27}\big),\qquad 9.01\times10^{-8}\ \text{m}\le r_C\le5.11\times10^{-5}\ \text{m}.
$$
The three terms are SNO under GRW-type symmetrisation, B7′, and B4 (Rb interferometry, which does not depend on r_C).

| quantity | value |
|---|---|
| B7′ coefficient | 7.287×10⁻¹⁹; tightest single point 6.62×10⁻¹⁹ at z = 1.9; 10.9× looser than Run 92's B7 |
| lower edge | 9.007×10⁻⁸ m (8.256×10⁻⁸ m with the self-term floor) |
| SNO hands over to B7′ at | 9.16×10⁻⁷ m |
| κ_top at the cap | 1.904×10⁻²⁷, set by B7′; 8.5 decades above the floor |
| under κ_b = 1/(aP∞) | a·P∞ ≳ 5.25×10²⁶ at the Lee cap; ≳ 3.55×10²⁶ for any cap (B4) |
| weak-field edge ℓ_P²/r_C² | ≤ 3×10⁻⁵⁶, far below the floor |
| consistency with Reading I6 §6 and the inputs | met |

**The variants** (κ_top at the cap). None empties the window.

| variant | κ_top at the cap | edges |
|---|---|---|
| R1 photoheated | 3.4×10⁻²⁸ (C = 1.30×10⁻¹⁹, z = 1.9); a·P∞ ≳ 3×10²⁷ | |
| R2 Leo T | 4.8×10⁻²⁸ (C = 1.8×10⁻¹⁹, the lowest-density case) | |
| R3 B7 | 1.75×10⁻²⁸ | Reading I6 §6's value |
| R4 one nucleon species | | lower edge 6.9×10⁻⁸ m |
| R6 cap at 1% | 1.4×10⁻²⁷ | cap 44 μm |
| R7 cap at 0.3% | 9.2×10⁻²⁸ | cap 36 μm |
| R9 single point | 1.73×10⁻²⁷ | |

The IGM sensitivities (data subsets, confidence level, cooling ×0.5 to ×2) give 1.7–2.8×10⁻²⁷. With only Gaikwad's and Boera's z ≥ 2 data (S7), B7′ and B4 tie to 0.24%. With looser caps of 63 and 76 μm, the Rb-atom bound takes the top at 2.8×10⁻²⁷; it does so for any cap above about 6.2×10⁻⁵ m. Without symmetrisation the window is empty, as Reading I6 said.

**What would close it.** Any one of three changes would empty the primary window:
- a LISA-type acceleration noise about 3.5×10³ lower. The floor would rise by f² = 1.2×10⁷, but the same measurement's centre-of-mass bound B2 would tighten by f², and the two meet. Any other cause would need to raise the floor by 3.4×10⁸;
- an inverse-square test sensitive to smearing at 0.09 μm;
- a top edge 3.4×10⁸ lower.

**What it means.**
- **CO's falsifiable statement in the quantum sector.** Given Reading I6's rulings:
  - **r_C:** route (b)'s collapse length lies between about 0.09 and 51 μm;
  - **κ_b:** route (b)'s rate constant lies within about 8.5 decades of LISA Pathfinder's gravity-noise floor;
  - **gravity:** a solid's gravity departs from Newton's inside r_C;
  - **entanglement:** gravity cannot entangle masses.
- **The narrower photoheated window.** It is modelled on standard photoheating and Leo T: κ_top ≲ 5×10⁻²⁸ at the cap, so a·P∞ ≳ 2×10²⁷.
  - The photoheated form rests on a photoheating model that fails at z ≈ 0.1.
  - It uses an approximate excess construction, about 10–15% too tight.
  - Leo T's arithmetic was checked, but its cooling inputs were not checked first-hand.
- **What the window rests on:**
  - GRW-type symmetrisation; without it the window closes;
  - setting B6′ aside;
  - an assumed housing mass for the floor;
  - Hu et al.'s broad z ≲ 0.4 lines being read as an upper bound on the thermal temperature. That reading is CO's; the authors also offer turbulence or new heating;
  - Walther et al.'s z = 1.8 point, which is read second-hand but does not bind;
  - the lower edge, which rests on SNO under symmetrisation and scales as floor^{1/5}.
- **Untested here:** the lightest neutrino's validity condition (m₁ ≳ 10⁻¹⁴–10⁻¹⁰ eV).

**Post hoc addendum** (`check96/REPORT.md`; `quantum96/PREREG_96_errata.md`).
- **The re-run.** All hashes matched, the run postdates hashing, and a re-run reproduces the log exactly. Independent code reproduced every headline number to ≤ 0.02%, and every variant to ≤ 0.1%. A Monte Carlo confirms the one-sided test's 95% threshold, with a tail of 0.0501.
- **ERROR, in a reported closure condition:**
  - PREREG §5 gave a LISA-type noise "about 2×10⁴ lower" (1.84×10⁴ in the log). It is 3.46×10³, because B2 tightens as the floor rises.
  - Corrected above.
- **Stale PREREG sentence (B6′).** "The 0.3% cap would empty it" used the first draft's coefficient. With the adopted one, B6′ would leave 3.36–3.56×10⁻⁵ m open. This is moot: under the worldline rate, B6′ closes the window.
- **PREREG's Gaikwad count** is 10 points, not 11. The total of 20 is right.
- **Reading I6 §6's numbers are superseded:**

| | Reading I6 §6 | Run 96 |
|---|---|---|
| κ_top at the cap | 1.74×10⁻²⁸ | 1.90×10⁻²⁷ |
| a·P∞ | ≳ 5.75×10²⁷ | ≳ 5.25×10²⁶ |
| SNO handover | below 4.1×10⁻⁷ m | 9.16×10⁻⁷ m |
| Leo T | "up to about 40×" tighter | withdrawn |
