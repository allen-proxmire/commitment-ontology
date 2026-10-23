## 9zzv. Run 73: does the stiffest matter commit before it turns back?

*21 October 2026. The aim was to pin down the "about 2p_s" in the ruling of 14:00 (infalling matter commits where the medium's possibility per place falls to about 2p_s) with a shell of the stiffest matter. Registered and hashed before the scan (`stiff73/PREREG_73.md`, 16:06 UTC).*
- *Amendment 1: the analysis script had a Python syntax error, fixed without changing its logic. The scan's rows had already been printed when the fix was made.*
- *The registration's header says 18:15 local; it was hashed at 18:06 (16:06 UTC).*
- *An independent agent checked the run. It reproduced every turning point, and found that the run converted the clock to possibility per place with the wrong formula. The correction reverses the registered verdict on the ruling's number. Both are recorded below.*

**Question.** Run 71's check found that a shell with surface pressure p = wσ passes the throat and then turns back where N ≈ wε. The ruled threshold is P = 2p_s. Does every kind of causal matter (w ≤ 1) reach it before it can turn back?

**The conversion, corrected.**
- In the record (Runs 66–67) the medium's clock is its occupancy:
$$
N=\frac{P}{P_\infty}\quad\Rightarrow\quad\frac{P}{p_s}=\frac{N}{\varepsilon}.
$$
- The registration and the run instead used P/P∞ = (N + ε)/(1 + ε). That is GR's lapse n, not the occupancy, and it overstates P by about p_s.
- It had been introduced in Run 71's reading and in the note on the ruling; both are corrected (§9zzs, §10).
- So the ruled 2p_s sits at N_c = 2ε, not N ≈ ε.

**The scan.** Run 71b's model, unchanged:
- Run 67's exterior, held fixed;
- a flat interior;
- Israel's two conditions, with [K^τ_τ] = 4π(σ + 2p) = (1 + 2w)M_s/R².

The grid is w = ⅓, ½, ⅔ and 1; ε = 10⁻², 10⁻⁴ and 10⁻⁶; shells released at R₀ = 4, 10 and 50 (units of m), thrown inward with γ₀ = 1 to 1000. That is 216 shells.
- 36 do not fall from rest.
- 75 turn back before the throat: they are held up by pressure, never come near the core, and the commitment rule never applies to them.
- 105 turn in the horn.

**Results** (where shells turn back, P/p_s = N/ε).

| w | grid maximum (all ε) | grid maximum (ε = 10⁻⁶) | supremum: shells thrown just hard enough to cross (the check) |
|---|---|---|---|
| ⅓ | 0.41 | 0.39 | — |
| ½ | 0.62 | 0.57 | 0.61 |
| ⅔ | 0.87 | 0.78 | 0.83 |
| 1 | 1.65 (ε = 10⁻²) | 1.14 | **1.27** |

- **Every causal shell turns back below 1.3p_s** at physical ε. So it reaches the ruled 2p_s, and commits, before it can turn: the margin is 2/1.27 ≈ 1.6.
- Only acausal matter, w ≳ 1.6, would turn above 2p_s.
- **The largest turns come from shells thrown just hard enough to cross the throat** (the check). They linger at the throat, then fall in almost from rest.
  - Their supremum for w = 1 is 1.272p_s, converged to 0.2% between ε = 10⁻⁴ and 10⁻⁶, and the same from R₀ = 10 and 50.
  - The grid's maxima underestimate it.
- **Harder throws do not push the turn higher:** from γ₀ = 100 to 1000 it moves by at most 0.8%.

![Run 73](figures/73_stiff.png)

**Verdicts.**
- **K73a: FAIL as registered; PASS on the record's definition.**
  - As registered, with the wrong conversion, the largest turn was at "2.63p_s", and raising the threshold to about 2.3p_s had been suggested. That suggestion is withdrawn.
  - With N = P/P∞ the largest turn is 1.65p_s (at ε = 10⁻², far from the pulsar bound), and at most 1.27p_s at physical ε. Both are below 2p_s.
- **K73b: FAIL as registered.** The grid's w = 1 maximum moved by 3.5% between ε = 10⁻⁴ and 10⁻⁶. This is a sampling effect: the minimum throw needed to cross depends on ε (the check). The underlying supremum converges to 0.2%.
- **K73c: PASSES.** Harder throws saturate. Soft throws near the crossing threshold give a finite supremum too (the check).

**What the check added.**
1. **The conversion error and its correction** (above). It also corrects the core's areal radius in Run 74: R_c = 2m(k + 1)/k, which is 3m at k = 2, not 4m.
2. **Independent reproduction** of the turning points to six or seven digits.
3. **The causal limit for a surface fluid** is |p| ≤ σ, i.e. w ≤ 1. A thin layer of 3D fluid with p = w₃ρ has w = w₃, so w = 1 is 3D stiff matter and a layer of radiation gives w = ⅓.
4. **Real collapsing cores have w ≲ 0.6:** about 0.3–0.6 at the centres of maximum-mass neutron stars, and ⅓ for perturbative QCD. Their supremum turn is about 0.75p_s.
5. **Commitment at N = 2ε falls inside the region where Run 71's flux switches off** (N at the shell ≈ 1.5ε). What the committed surface does to waves therefore matters for the late flux (Run 74).

**Reading.**
1. **The ruled 2p_s catches all causal matter, with room to spare.** Every shell with w ≤ 1 that passes the throat turns back at no more than 1.27p_s, and commits first at 2p_s.
   - Matter with ordinary pressure (w ≲ 0.6) would turn back below about 0.75p_s.
   - No change to the ruling is needed.
2. **Any threshold above about 1.34p_s would work.** The ruled 2p_s is a natural choice: twice the medium's crossover.
3. **Limits:**
   - a thin shell's surface pressure is a stand-in for a star's;
   - w is held constant;
   - the exterior is held fixed.
