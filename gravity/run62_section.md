## Run 62: the dense matter CO needs, against heavy-ion collisions

*20 October 2026. (step 1: set route (b)'s pressure at 2–4 n_s against the heavy-ion collision bounds, which come from collision experiments, not gravity). Registered and hashed before the run (`hic62/PREREG_62.md`, 19:09 UTC). An independent agent checked it; its corrections are included.*

**Question.** Runs 60–61 leave CO one kind of neutron-star matter: like chiral EFT up to about 2 n_s, then a sharp stiffening (c_s² ≳ 0.7–0.9) up to the centres of the heaviest stars. Gold-nucleus collisions compress nuclear matter to 2–4.5 n_s in the laboratory, and the flow of the debris measures its pressure, with no theory of gravity involved. Do they allow the matter CO needs?

**The laboratory data.**
- **Symmetric nuclear matter (equal neutrons and protons) at 2 n₀:** P = 10.1 ± 3.0 MeV/fm³. This is the flow band of Danielewicz, Lacey & Lynch (2002) at 2 n₀, as tabulated by Tsang et al. (2024); FOPI's flow gives 10.3 ± 2.8.
- **Above 2 n₀:** the sound speed of symmetric matter from STAR's flow (Oliinychenko, Sorensen, Koch & McLerran 2023, Bayesian best fit):
  - c² = 0.47 ± 0.12 on 2–3 n₀;
  - c² = −0.08 ± 0.14 on 3–4 n₀, a softening the authors read as a possible phase transition.
  - The authors caution that the model's systematic errors are not yet assessed, and that the older E895 data prefer a moderately soft equation of state on both intervals.
- **From symmetric to neutron-rich matter: the symmetry energy.** Above 2 n₀ it is poorly known. DLL bracketed it with two forms (u = n/n₀):
$$
S_{\rm F1}=12.7\,u^{2/3}+38\,\frac{u^2}{1+u}\ \text{(stiff)},\qquad S_{\rm F3}=12.7\,u^{2/3}+19\,u^{1/2}\ \text{(soft)}\quad[\text{MeV}],\qquad P_{\rm sym}=n^2\frac{dS}{dn}.
$$
  F1 is generous: its slope at n₀ is L ≈ 111 MeV, above most current estimates (about 40–80 MeV).

**The bound on neutron-star matter.** The symmetric-matter pressure is integrated from its anchor with the measured sound speeds,
$$
\frac{de}{dn}=\frac{e+p}{n},\qquad dp=c^2\,de ,
$$
and the symmetry pressure is added:
$$
B(n)=P_{\rm SNM}(n)+P_{\rm sym}(n)\ \ge\ P_\beta(n)=P_{\rm SNM}+\delta^2P_{\rm sym}+P_{\rm lep}.
$$
Neutron-star matter (β-equilibrium, neutron excess δ < 1) sits below pure neutron matter, so B caps it.

| bound | P(2n₀) | c² on 2–3 / 3–4 n₀ | symmetry energy | B at 2, 2.5, 3, 3.5, 4 n₀ (MeV/fm³) |
|---|---|---|---|---|
| **B2** (K62a) | 16.1 (+2σ) | 0.71 / 0.20 (+2σ) | stiff (F1) | 42, 118, 207, 251, 298 |
| **B1** (K62b) | 13.1 (+1σ) | 0.59 / 0.06 (+1σ) | stiff (F1) | 39, 104, 178, 206, 238 |
| B2, soft symmetry (reported) | 16.1 | 0.71 / 0.20 | soft (F3) | 25, 89, 164, 190, 217 |
| B1, no softening (reported) | 13.1 | 0.59 / 0.59 | stiff (F1) | 39, 104, 178, 262, 354 |

The bound acts on 2–4 n₀, where the sound-speed intervals are; above 4 n₀ only causality applies.

**Method.** The stiffest matter each bound allows: a base equation of state to 2 n_s, then c_s² = s, following the bound wherever the s-path would cross it (never stiffer than s), and c_s² = s again above 4 n₀. s = 1 is the stiffest. Bases: SLy or APR4 to 2 n_s, or SLy to 1.1 n_s then c_s² = 0.03, 0.10 or 0.17 to 2 n_s (Run 61). CO's stars come from Run 57's solver and Run 61's tidal code.

**Verdicts, as registered.**
- **K62c PASSES (code check).** With no bound, the tabulated equation of state reproduces Run 61's family (SLy to 2 n_s, s = 0.8 and 1.0) to 10⁻⁹ in M_max and Λ(1.362).
- **K62a PASSES (B2: 2σ, stiff symmetry energy).** 15 families hold a QCD-allowed 2.08 M☉ CO star with Λ(1.362) ≤ 720. CO's largest maximum mass is 2.19 M☉.
- **K62b PASSES (B1: 1σ, stiff symmetry energy), with little room.** 13 families pass; CO's largest maximum mass is 2.13 M☉. Several pass by a few hundredths: SLy at s = 0.8 gives 2.084, and the c₁ = 0.10 base at s = 0.8 gives 2.080.

| base to 2 n_s | B2 (K62a): smallest s for 2.08 / M_max at s = 1 | B1 (K62b): smallest s / M_max at s = 1 | B2, soft symmetry energy: M_max at s = 1 | B1, no softening: M_max at s = 1 |
|---|---|---|---|---|
| SLy | 0.8 / 2.17 | 0.8 / 2.11 | 2.05 | 2.13 |
| APR4 | 0.8 / 2.16 | 0.9 / 2.11 | 2.05 | 2.13 |
| SLy, then c_s² = 0.03 from 1.1 n_s | 0.9 / 2.14 | 1.0 / 2.10 | 2.05 | 2.12 |
| SLy, then c_s² = 0.10 from 1.1 n_s | 0.8 / 2.17 | 0.8 / 2.11 | 2.05 | 2.12 |
| SLy, then c_s² = 0.17 from 1.1 n_s | 0.7 / 2.19 | 0.7 / 2.13 | excluded at 2 n_s | 2.14 |
| MPA1 (reported) | 0.8 / 2.19 | 0.8 / 2.12 | — | — |

Every 2.08 M☉ star in the table passes the QCD test; their centres are at 2.6–3.6 n_s. The bound binds in every family that reaches 2.08 M☉, from about 2.2–3.3 n_s up to 4 n₀.

**Reported.**
1. **With the soft symmetry energy (F3), CO cannot reach 2.08 M☉.** Its largest maximum mass is 2.055 M☉ (APR4 base, s = 1). That is short of J0740's central mass but within its 1σ (2.08 ± 0.07). The c₁ = 0.17 base is excluded outright: its pressure at 2 n_s (28.5 MeV/fm³) is above the bound there (24.7).
2. **Without the softening above 3 n₀ (B1, no softening)** CO passes, with the largest maximum mass 2.14 M☉. So K62b's narrow pass is set mostly by the bound on 2–3 n₀ and the symmetry energy, not by the softening.
3. **Run 61's route-(b) families against the bounds** (largest p/B between 2 n_s and the 2.08 M☉ star's centre): 0.85–1.08 under B2, 0.99–1.23 under B1, 1.15–1.42 with the soft symmetry energy. Those with s = 1 overshoot B2 slightly (by up to 8%), which the capped families avoid at little cost in mass.
4. **GR with the same capped matter** reaches 2.55–2.72 M☉ (s = 1), so the heavy-ion bound leaves GR ample room. CO's maxima are 0.80–0.83 of GR's.

![Run 62](../figures/62_hic.png)

**How stiff must the symmetry energy be? (post hoc, reported).** A one-parameter family between DLL's two forms,
$$
S_w=12.7\,u^{2/3}+19\Big[w\,\frac{2u^2}{1+u}+(1-w)\,u^{1/2}\Big],\qquad L=53.9+57\,w\ \text{MeV},\qquad S_w(2n_0)=47.0+23.8\,w\ \text{MeV},
$$
with the stiffest matter (s = 1) on the SLy, APR4 and c₁ = 0.17 bases:

| w (L, S(2n₀)) | 0 (54, 47) | 0.25 (68, 53) | 0.5 (82, 59) | 0.75 (97, 65) | 1 (111, 71) |
|---|---|---|---|---|---|
| CO's largest M_max, 2σ SNM | 2.055 | 2.100 | 2.136 | 2.165 | 2.189 |
| CO's largest M_max, 1σ SNM | — | 1.978 | 2.043 | 2.089 | 2.127 |

- So CO reaches 2.08 M☉ within the 2σ bound if L ≳ 63 MeV (S(2n₀) ≳ 51 MeV), and within the 1σ bound only if L ≳ 94 MeV (S(2n₀) ≳ 64 MeV).
- In this family that is a statement about P_sym at 2–3 n₀; L and S(2n₀) only label it.

**What the check added.**
1. **The data readings and the bound values are confirmed:** the DLL anchor (Tsang et al. 2024, Table I, 1σ error bars), Oliinychenko et al.'s best-fit values, DLL's two symmetry energies (S(2n₀) = 70.8 and 47.0 MeV, L = 110.9 and 53.9 MeV), and the tabulated B1 and B2.
   - Reading Oliinychenko et al.'s ± as 1σ is reasonable but not stated in the paper.
   - B2's +2σ anchor (16.1) already lies beyond DLL's published band, and taking the same edge on all three inputs at once is more generous than a joint 1σ or 2σ.
2. **The reproduction matches**, with the agent's own code: B1, SLy, s = 0.8 gives 2.0841 M☉ (centre of the 2.08 M☉ star at 3.333 n_s); the soft-symmetry APR4 and SLy cases give 2.0547 and 2.0536.
3. **The cap is sound but loose, and that decides the reading.**
   - The inequality P_β ≤ P_SNM + P_sym holds throughout (the agent solved β-equilibrium with electrons and muons).
   - But with the stiff symmetry energy the proton fraction is large (0.16–0.27), so pure neutron matter overstates neutron-star pressure by 12–74 MeV/fm³.
   - The cap the same inputs actually imply is
$$
B_\beta(n)=P_{\rm SNM}(n)+\delta^2(n)\,P_{\rm sym}(n)+P_{\rm lep}(n),
$$
     with δ and the lepton pressure from β-equilibrium. Under it, the agent found CO's best maximum mass to be 2.09 M☉ at 2σ (K62a would pass by about 0.01) and 1.96 M☉ at 1σ (K62b would be UNDECIDED).
   - The registered verdicts stand as registered; the reading below uses B_β.
4. **Is s = 1 under the cap the best path?** Supported, not proven. It maximises the pressure at each density, not at each energy density. Paths that stay soft and then go causal, which the agent tried, all gave lower CO maxima.
5. **Not purely gravity-independent.** The PASS criterion includes GW170817's Λ ≤ 720, which carries the GR-waveform caveat (Runs 61, 63).
6. **The crash was benign.** The table was built before the exclusion check; it hit only a reported family, and the post hoc record matches the registered intent. Fix the order before any reuse.
7. **Symmetry-energy constraints from the laboratory**, for comparison:
   - ASY-EOS: L = 72 ± 13 MeV (S(2n₀) ≈ 56 ± 5 MeV, the agent's estimate);
   - SπRIT: 42 < L < 117 MeV;
   - PREX-II: L = 106 ± 37 MeV;
   - CREX favours lower L.
   - Constraints on S(2n₀) derived from neutron stars assume GR and are not used.

**The same scan with the β-equilibrium cap (post hoc, after the check).** B_β is computed for each symmetry energy S_w (β-equilibrium with electrons and muons, parabolic in δ):

| w (L, S(2n₀)) | 0 (54, 47) | 0.25 (68, 53) | 0.5 (82, 59) | 0.75 (97, 65) | 1 (111, 71) |
|---|---|---|---|---|---|
| proton fraction at 2 / 3 / 4 n₀ | 0.08 / 0.10 / 0.12 | 0.10 / 0.14 / 0.17 | 0.12 / 0.17 / 0.21 | 0.14 / 0.20 / 0.24 | 0.16 / 0.23 / 0.27 |
| B_β at 3 n₀, 2σ / 1σ (MeV/fm³) | 160 / 131 | 165 / 136 | 168 / 139 | 170 / 141 | 171 / 142 |
| CO's largest M_max, 2σ SNM | 2.04 | 2.06 | 2.07 | 2.086 | 2.09 |
| CO's largest M_max, 1σ SNM | 1.88 | 1.92 | 1.94 | 1.95 | 1.96 |

- At 2σ, the c₁ = 0.17 base is excluded at 2 n_s for w ≤ 0.5 (its pressure there, 28.5 MeV/fm³, is above B_β).
- **So with the cap the inputs actually imply, CO reaches 2.08 M☉ only at the +2σ edge of all three heavy-ion inputs together and with L ≳ 95 MeV (S(2n₀) ≳ 64 MeV).** At the 1σ edge no symmetry energy up to DLL's stiff one gets it past 1.96 M☉.
- These maxima are within J0740's 2σ (2.08 ± 0.07, so ≥ 1.94) except at 1σ with the softest symmetry energies (1.88–1.92).

**Reading.**
1. **The registered verdicts pass, but the corrected reading is a squeeze, not a pass.** With the bound the same laboratory inputs imply for neutron-star matter (B_β), CO holds PSR J0740+6620 at its central mass only if three things hold at once:
   - symmetric matter's pressure at 2–4 n₀ sits at the +2σ edge of every heavy-ion input at once;
   - the symmetry energy is stiff (L ≳ 95 MeV, S(2n₀) ≳ 64 MeV), against ASY-EOS's 72 ± 13 MeV and PREX-II's 106 ± 37;
   - c_s² ≈ 1 from about 2 n_s up to the centre.
   Otherwise CO's heaviest stars are 1.88–2.07 M☉: below J0740's central mass, mostly within its 2σ.
2. **This is the sharpest constraint on CO's interior equations so far, and it is gravity-independent** (apart from Λ ≤ 720, which only selects among already-stiff families). It is not a falsification: the heavy-ion inputs are model-dependent transport analyses, the 2σ edges are where CO still fits, and J0740's mass is uncertain by 0.07 M☉.
3. **GR is comfortable on the same inputs:** 2.55–2.72 M☉ with the neutron-matter cap, so well above 2.08 with any cap.
4. **What would decide it:**
   - the symmetry energy at 2–3 n₀ (FRIB, FAIR, more neutron-skin data): L well below about 90 MeV would leave CO short of J0740's central mass;
   - heavy-ion flow at 2–4 n₀ with assessed model systematics (Oliinychenko et al.'s own caveat);
   - a heavier pulsar: anything above about 2.1 M☉, measured precisely, would exceed every CO maximum under B_β.
