## 9zzj. Run 63 (a derivation): ED's inspiral beyond first order, in the test-mass limit

*20 October 2026. Allen: "do as you recommend" (step 2: derive ED's two-body motion beyond first order, the condition for GW170817's tidal bound to apply to ED). This is a derivation, not a registered test: the numbers below are exact and were derived before any comparison was set up, so nothing here is scored. An independent agent checked it; its corrections are included.*

**Question.** GW170817's tidal bound (Run 61) and the gravitational-wave tests of GR assume the inspiral's phase follows GR's to 3.5 post-Newtonian orders. ED matches GR at first order (Run 34). Where does it first differ, and by how much?

**What can be derived now: the test-mass limit.** A small body orbiting a much heavier one follows a geodesic of ED's exact exterior (the pattern rule, Runs 16, 46):
$$
ds^2=-A\,dt^2+B\,(dr^2+r^2d\Omega^2),\qquad A=e^{-2M/r},\quad B=e^{2M/r}.
$$
- **Circular orbits.** For a static metric, Ω² = A′/(Br²)′ and the energy per unit rest mass is E = A/√(A − Br²Ω²). With y = M/r:
$$
(M\Omega)^2=\frac{y^3e^{-4y}}{1-y},\qquad E=e^{-y}\sqrt{\frac{1-y}{1-2y}} .
$$
- **As a series in x = (MΩ)^{2/3}** (exact rational arithmetic, `inspiral63/derive63.py`):
$$
E_{\rm ED}-1=-\frac x2\Big[1-\tfrac34x-\tfrac{89}{24}x^2-\tfrac{7195}{576}x^3-\dots\Big],
$$
$$
E_{\rm GR}-1=-\frac x2\Big[1-\tfrac34x-\tfrac{27}{8}x^2-\tfrac{675}{64}x^3-\dots\Big].
$$
- **So ED and GR agree at first order and differ at second:** ED's 2PN binding coefficient differs by −1/3 (8/81, about 10%, larger in magnitude). The 3PN coefficients differ too (−7195/576 against −6075/576). The cause is the spatial metric at O(U²): e^{2U} = 1 + 2U + 2U², against Schwarzschild's 1 + 2U + 1.5U²; g_tt also differs at O(U³).
- **The innermost stable orbit** (as in Run 28, §9u): r = (3 + √5)M in isotropic coordinates (areal radius 6.34M, GR 6M), at MΩ = 0.0633 (GR 0.0680, 7% lower), with E = 0.9452 (GR 0.9428). It lies outside ED's neutron stars (19.5 km at 2.08 M☉), so it matters for them.
- **The light ring** (Run 28): areal radius 3.30M (GR 3M); critical impact parameter 2eM = 5.44M (GR 3√3M = 5.20M). It lies inside ED's neutron stars (areal radius about 3.8–4.1M at 2 M☉), and under option A black holes have Kerr exteriors, so it applies to neither.

**What it would do to the waveform (conditional).** The gravitational-wave phase (TaylorF2) at 2PN carries φ₄ = 10 r₄, where r₄ is the v⁴ coefficient of E′(v)/F(v).
- With E′/F ∝ v⁻⁹(1 + Σ r_k v^k), the stationary-phase integral gives
$$
\varphi_k=\frac{40\,r_k}{(8-k)(5-k)},\qquad \varphi_4=10\,r_4 ,
$$
  which reproduces GR's test-mass φ₂ = 3715/756, φ₃ = −16π and φ₄ = 15293365/508032.
- If ED's flux F were GR's (not derived: ED's radiation is known only at leading quadrupole order, Run 11b), ED's binding energy alone shifts φ₄ by exactly −10.
- **An illustration, not a prediction:** that is δφ̂₄ = −0.33 in the test-mass limit, or −0.22 for equal masses if the shift did not depend on the mass ratio (an unfounded assumption). ED also changes φ₆, while the published bounds vary one coefficient at a time.
- **No current gravitational-wave bound tests it** (the check, below). GWTC-4.0's combined tests are mostly binary black holes (δφ̂₄ = −0.03 (+0.16/−0.15) and 0.11 ± 0.23 with one common value; about ±0.45 when each event may differ, 90%). Under option A a black hole's exterior is GR's, so this shift does not apply to them.

**What the check added.**
1. **The algebra is confirmed by hand:** the orbit formulas, the series (ln x = ln y − y + y²/6 + y³/9; ln E = −x/2 + x²/4 + 2x³ + (517/72)x⁴), the ISCO (4y² − 6y + 1 = 0) and the light ring. The TaylorF2 map and Δφ₄ = −10 are confirmed.
2. **Test bodies do move on geodesics here.** The adopted pattern rule (Run 46) is exactly the Klein–Gordon equation in −N²dt² + N⁻²dx², whose wave packets follow its geodesics. For bodies at relativistic speed this rests on Allen's ruling that inertia = total energy, up to the strong-equivalence-principle term (≲ 10⁻⁵, Run 55). The exterior applies when the central body is an ED star.
3. **What ED's rules fix and do not fix.** Fixed: the test-mass dynamics in this exterior; the 1PN two-body dynamics for any mass ratio (γ = β = 1, no preferred-frame terms); the leading quadrupole flux. Not fixed, so each needs a ruling:
   - **(i) option A for binaries:** does "GR's exterior" cover the near zone of a binary black hole, or the black hole of a neutron-star–black-hole binary, or only isolated holes?
   - **(ii) the two-body field beyond first order:** does the boosted-rest-field input hold at O(v⁴) and O(v²U); how do two bodies' fields combine (each draw is redshifted by the other's field, and the metric is exponential in the total U); what is the current field at O(v³)?
   - **(iii) motion in that field at 2PN.**
   - **(iv) radiation beyond the quadrupole:** the 1PN source multipoles, propagation on the curved background (GR's 4πv³ tail), any scalar or dipole channel, and which energy balances the flux.
   - **(v) a conserved binary energy including radiation** (Run 52's E_H is defined for static configurations).
   Even the test-mass flux is GR's here only by assumption: in GR the 2PN test-mass flux depends on the background metric at 2PN, which ED changes.

**Reading.**
1. **ED's inspiral is not GR's beyond first order.** Its exterior differs at O(U²), so the binding energy differs at 2PN already in the test-mass limit. GW170817's tidal bound (Run 61) assumed the two agree to 3.5PN, so K61b's PASS rests on an assumption ED's own exterior does not satisfy. How much this biases Λ̃ needs the full two-body phase.
2. **The size is not small:** a 10% change in the 2PN binding coefficient is about −0.2 to −0.3 in δφ̂₄, comparable to what binary-black-hole tests now resolve. Those tests may not apply to ED (option A), and the number itself assumes GR's flux.
3. **What is missing before this is a test** (rulings (i)–(v) above):
   - **Which binaries ED's exterior applies to.** Under option A black-hole binaries may be GR's, so their bounds would test nothing in ED. Neutron-star binaries do test it; GW170817's coefficient bounds exist (Abbott et al. 2019) but are given only in a figure and have not been read here, and the checker knows of no such test with GW190425.
   - **ED's flux beyond leading order.** Run 11b gives the leading quadrupole (0.98 of GR on the lattice). The 1PN flux coefficient alone would be tested at the ±0.07 level (δφ̂₂).
   - **The equal-mass terms at 2PN.** They need ED's field for moving sources beyond first order, where the adopted rules do not yet say what happens.
