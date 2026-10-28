## Run 74: what commitment at P = k·p_s does to the radiation

*21 October 2026. The aim was to model what commitment at 2p_s does to the geometry and to the radiation afterwards. Registered and hashed before the run (`commit74/PREREG_74.md`, 16:10 UTC).*
- *The registration used the same wrong conversion between the clock and the occupancy that the check on Run 73 found. So its "k = 2" and "k = 2.3" cases committed at a true P of about p_s and 1.3p_s, not at the ruled 2p_s.*
- *The results for the ruled threshold (N_c = 2ε) and for k = 1.34 were computed afterwards with the corrected conversion (`commit74c.py`, post hoc). Both sets are recorded below.*
- *The registration's header says 18:25 local; it was hashed at 18:10 (16:10 UTC).*
- *An independent agent checked the run. It reproduced the corrected numbers to every digit printed, and corrected four readings; they are included.*

**Question.** Under the rulings, infalling matter commits where the medium holds 2p_s per place, and the core is a total absorber. When a collapsing shell commits:
- Where is it?
- What has been radiated by then?
- What does the outside see afterwards?

**The model.** Run 71/71b's shell, in Run 67's exterior held fixed, with a flat interior.
- **The shell commits** when its clock reaches N_c = kε, i.e. P = k·p_s, since N = P/P∞.
- **After commitment** the region it bounded is the core. Outgoing modes then leave the core boundary, and CO's rules do not fix their state. Two models bound it:
  - **(A) A cold, static core (the cold-absorber extreme):** the modes are in the static (Killing) vacuum, so the flux at infinity is zero afterwards. Joining the two maps takes a transition of duration δu (in retarded time at infinity), and that transition carries a flash:
$$
E_{\rm flash}=\frac{1}{24\pi}\int\Big[\tfrac12\big((\ln p')'\big)^2-(\ln p')''\Big]du\;\simeq\;\frac{\Delta^2}{144\pi\,\delta u},\qquad \Delta=-\ln p'(u_c).
$$
  - **(B) Continuation (the other extreme):** the outgoing state continues the shell's map, giving Run 71's dust tail and no flash.
  - These are two extremes, not bounds: model A's flash grows without limit as δu shrinks (the check).
  - The true outgoing state is mixed, because the burst's partner modes are absorbed. One smooth map is a model for the energy at the junction, not the exact state (the check).
- **Cases:** dust from rest (R₀ = 10, 4); w = ⅓ thrown at γ₀ = 10; w = 1 thrown at γ₀ = 100. Each at ε = 10⁻⁴ and 5×10⁻⁶.

**Results at the ruled threshold** (k = 2, N_c = 2ε; corrected, post hoc).
1. **Where.** The core's areal radius is
$$
R_c=\frac{r\,n}{N}\Big|_{N_c}=2m\,\frac{k+1}{k}\Big(1+O(\varepsilon)\Big)=3.000m,
$$
   measured to 10⁻⁵ (3.49m at k = 1.34). The core has 2.25 times the area of GR's horizon.
2. **Every case commits,** including the w = 1 shell (Run 73: causal matter turns back at most at 1.27p_s).
3. **When.** Commitment comes almost as soon as the shell passes the throat. Seen from far away it is at u_c ≈ 110–170M.
   - There the outgoing rays are stretched by du/dτ ≈ 1.3–2.1×10⁵ at ε = 5×10⁻⁶, about 1/ε.
   - The map's redshift is Δ = 22.3 (dust), 22.0 (w = ⅓) and 20.7 (w = 1) at ε = 5×10⁻⁶; and 16.3 for dust at 10⁻⁴. That is about 2ln(1/ε) − 2.
4. **The Hawking-like burst's energy is out before commitment; its flux is not quite over.**
   - By energy it is at least 99.8% complete: what would still have come is 0.12 F_H·M of a roughly 77M burst (the check).
   - At commitment the flux is still 0.046 F_H, so commitment cuts off the last 5% of the switch-off. Model A's flash is what handles that cut.
   - The ratio before/total, 1.010 (ε = 5×10⁻⁶) and 1.015 (10⁻⁴), exceeds 1 because the rest of Run 71's map is net negative.
5. **Afterwards, model A: one flash, then silence.**
   - **Its energy** is Δ²/(144π)·ħ/δu ≈ ħ/δu for a tanh transition. The coefficient depends on the profile: a linear ramp gives three times as much, an error-function step 0.85 times (the check).
   - **It is not one quantum** (the check, from the Bogoliubov count for a kink in the map). The number of quanta per e-fold of frequency is
$$
\frac{dN}{d\ln\omega}\approx\frac{\Delta-2}{4\pi^2}\approx0.5,
$$
     from ω ≈ 0.1/M up to about 2/δu. So the energy is carried by about half a quantum near 2/δu, on top of a soft logarithmic tail.
   - **Its size depends on δu, which CO's rules do not fix.**
     - At δu = 1M it carries about 34 times the Hawking-like transient's energy.
     - If commitment takes at least one hop in the shell's own frame, δu ≳ τ_h/ε. For a 10 M☉ hole and a hop of about 10³ Planck lengths (the record's estimate of CO's hop, 300–1,000 Planck lengths; an assumption here), the flash is about one quantum of order 10¹¹ GeV: E/M ~ 10⁻⁴⁸.
6. **Afterwards, model B:** the dust tail continues, carrying −1.1% (ε = 5×10⁻⁶) to −1.7% (10⁻⁴) of the total. There is no flash.

![Run 74](../figures/74_commit.png)

**Verdicts, as registered** (for the surfaces actually modelled, at a true P of about p_s and 1.3p_s).
- **K74a PASSES:** R_c/m matches 2k/(k − 1) to 2×10⁻⁴. That formula holds only under the wrong conversion. With the correct one, R_c = 2m(k + 1)/k is matched to 10⁻⁵.
- **K74b PASSES:** the burst's energy is complete before commitment (1.01–1.02). It also holds at the ruled 2p_s (1.010–1.015).
- **K74c PASSES:** the flash follows Δ²/(144πδu) to 1.2% for δu ≤ 1M. This is a check of the code.
- **K74d PASSES as registered,** but its premise is superseded. The w = 1 shell turned first at the registered "k = 2" (true P ≈ p_s) and committed at "k = 2.3" (true P ≈ 1.3p_s). At the true ruled 2p_s it commits.
- K74a, as registered, only checks that R = rn/N reproduces the formula its own conversion implies. It is not a test of physics (the check).

**What the check added.**
1. **Independent reproduction** of the corrected numbers to every digit printed: τ_c, u_c, du/dτ, U′, dv/dV and Δ.
   - It confirmed the normalisation p′ = 1 for the static vacuum. For a static shell, dv/dV·dU/du = 1.
   - It found Δ = 2ln(1/ε) − 2.2.
2. **The flash is spread over frequencies,** and model A is an extreme, not a bound (above).
3. **The burst is complete by energy, not by flux** (above).
4. **"No echoes" now rests on the total-absorber ruling.** Run 67's surface absorbed because it sat at infinite tortoise distance; the core at N_c = 2ε does not.
   - The tortoise distance from the light ring to the core is 47.7M (ε = 5×10⁻⁶).
   - A reflecting core would echo after about 2Δr* ≈ 95M: 29 ms for GW250114's remnant, which matches Run 43's echo bound.
5. **Thrown shells.** For the w = 1 shell thrown in, the matching ingoing ray entered during the artificial static hold before release, so the flash from the release kick itself is not modelled.
6. **The geometry statement is geometry only.**
   - The hole has κ = 0, so it has no temperature and there is no first-law basis for S = A/4.
   - The core boundary is not a horizon, and its area depends on the ruling's k.
   - R_c = 3m equals the light ring's areal radius, but the two surfaces are on opposite sides of the throat.

**Reading.**
1. **A forming CO hole radiates about one Hawking-like quantum, then its matter commits at 2p_s.**
   - With a cold core it then gives one flash, about ħ/δu of energy spread over frequencies, and is silent for ever.
   - With the other extreme, it carries on with Run 71's faint negative tail.
   - Either way, this agrees with Run 68 and with the stable-holes ruling.
2. **The core is a sphere of areal radius 2m(k + 1)/k:** 3m at the ruled 2p_s, with 2.25 times the area of GR's horizon. That is a statement about geometry only: the hole has no temperature, and the core boundary is not a horizon.
3. **What the rules leave open:**
   - how long commitment takes, which sets the flash's energy and frequency (a hop in the shell's frame is a natural floor);
   - whether the core absorbs, which is now set by the ruling: a reflecting core would echo after about 95M;
   - the core's quantum state, which decides between a flash (A) and none (B);
   - what the record's own field does to the geometry, which here is held fixed.
4. **Limits:**
   - the exterior is held fixed;
   - a thin shell;
   - the 1+1 radial sector;
   - two bounding models for the core's state.
