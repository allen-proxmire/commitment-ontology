## 9zzn. Run 67: the near-horizon shell under option 3, with ED's medium

*21 October 2026. Step 4. Registered and hashed before the run (`shell67/PREREG_67.md`, 06:30 UTC). The claims were derived before registration; K67b and K67d check analytic forms numerically, while K67a and K67c are computations whose outcome was not known. Smoke tests on unregistered inputs are disclosed in the registration. An independent agent checked the run; its corrections are included.*

**Question.** Under option 3 a static hole looks like Schwarzschild's until possibility runs low. Run 65's check flagged the shell where N ≲ p_s/P₀, where the medium's g = p_s/P is no longer small. What happens there, and how does it relate to Run 43's core, which was ruled to commit?

**1. The static vacuum, exactly.** In vacuum the equations for (γ̃, φ) do not involve the medium (§9zzm), so they are Schwarzschild's, with a parameter m:
$$
\tilde\gamma=dr^2+(r^2-2mr)\,d\Omega^2,\qquad \varphi=-\ln n,\qquad n\equiv N_{\rm GR}=\sqrt{1-2m/r} .
$$
The clock is the medium's occupancy. In the mean field,
$$
N=(1+\varepsilon)\,n-\varepsilon,\qquad \varepsilon=\frac{p_s}{P_\infty},\qquad ds^2=-N^2dt^2+N^{-2}\big(dr^2+(r^2-2mr)\,d\Omega^2\big),
$$
with Kepler mass M_K = (1 + ε)m. **This is Run 32's form** (N = ((1 + Q)e^{−M/r} − 1)/Q, under option 1) with e^{−M/r} replaced by GR's lapse.

**2. The zero-clock surface.** Possibility runs out (P = 0) where GR's lapse would be
$$
n_0=\frac{\varepsilon}{1+\varepsilon},\qquad r_0-2m\approx2m\,\varepsilon^2 .
$$
At the bound (ε ≈ 3.4–6×10⁻⁶) the clock stops 2–7×10⁻¹¹ of the mass parameter m (in the coordinate r) outside where GR's horizon would be. There:
- N falls to zero linearly, N ≈ (r − r₀)/L with L = r₀²n₀/((1 + ε)m) ≈ 4mε. So κ = 0, Run 32's cold, extremal-type end.
- The static proper distance ∫dr/N grows as L ln(1/(r − r₀)), so it is infinite. The areal radius R = a/N grows as 1/(r − r₀).
- **The tortoise coordinate r* = ∫dr/N² → −∞**, as at a horizon. Waves that go in do not come back: the surface absorbs. It is not a reflecting wall at finite r*.
- **An infaller reaches it in finite proper time.** From r = 6M_K, starting from rest at infinity, it takes 5.5949 M_K (ε = 5×10⁻⁶), against Schwarzschild's 5.5949 M to its horizon.
- **Infallers meet a curvature singularity there.** In the static orthonormal frame, S_tt + S_xx = −N²R″/R (R_{tθtθ} + R_{rθrθ}), which is zero for Schwarzschild, tends to −2/L² (K67b: 0.9975 of it at N = 10⁻³ε). An infaller of energy E sees its angular tidal component shifted by (E²/N² − 1)(S_tt + S_xx), which grows as 2/(τ₀ − τ)². That is a curvature singularity along infall, of the stretching kind: separations grow as 1/(τ₀ − τ), as the sphere's area blows up.
- **There is no event horizon.** N > 0 everywhere outside the zero-clock surface, so light from anywhere outside it escapes, infinitely redshifted toward it.

**3. A throat.** Between the light ring and the surface the areal radius has a minimum:
$$
n_*\approx\Big(\frac{\varepsilon}{2}\Big)^{1/3},\qquad R_{\min}\approx2m\Big(1+3\Big(\frac{\varepsilon}{2}\Big)^{2/3}\Big).
$$
Inside it, the area grows again toward the surface.

| | ε = 10⁻³ | ε = 5×10⁻⁶ |
|---|---|---|
| throat: GR's lapse n* (asymptotic (ε/2)^{1/3}) | 0.07951 (0.07937) | 0.013573 (0.013572) |
| throat: clock N there, redshift 1/N | 0.0786, 12.7 | 0.01357, 73.7 |
| throat: R_min/2M_K (asymptotic) | 1.01713 (1.01788) | 1.000543 (1.000548) |
| tortoise distance, light ring to throat | 9.8 M | 16.8 M |
| S_tt + S_xx at the throat (Schwarzschild's horizon tide is 1/8m²) | −0.363/m² | −0.375/m² |
| an infaller's extra angular tide at the throat (E = 1), in units of 1/8m² | about 470 | about 1.6×10⁴ |

**4. Outside, GR to O(ε).**
- **Waves** (K67c). A massless scalar, ℓ = 2, from ωM_K = 0.25 to 1.00: the reflection |R| differs from Schwarzschild's by at most 1.2×10⁻⁵ at ε = 5×10⁻⁶ (1.2×10⁻³ at ε = 10⁻³). Flux is conserved to 3×10⁻¹⁰. The throat sends back nothing measurable, so there are no echoes at this level.
- **The shadow** (K67d): b_c = 3√3 M_K(1 + 0.4641ε), so +2×10⁻⁶ at the bound.
- **β − 1 = −ε/2** (Run 66).

**5. The exact medium** (K67a). In the exact zero-range process the clock also stops at z = 0. The zero-clock lapse differs from the mean field's ε/(1 + ε) by 3.5×10⁻³/p_s (P∞/p_s = 10³) and 4.6×10⁻⁴/p_s (10⁴), for p_s = 64, 256 and 1024. The clock itself departs from the mean field by at most 0.6% (p_s = 64) to 0.04% (p_s = 1024), at n = 1.5ε.

**Verdicts, as registered.**
- **K67a PASSES:** the exact zero-clock lapse is within 0.0035/p_s of the mean field's (threshold 1/p_s).
- **K67b PASSES:** the throat sits within 0.006% of (ε/2)^{1/3} at ε = 5×10⁻⁶; the boost defect is 0.9975 of −2/L² at N = 10⁻³ε (both ε); the infall time is 5.5949 M_K against 5.5949 M.
- **K67c PASSES:** max ||R_ε| − |R_GR|| = 1.2×10⁻⁵ at ε = 5×10⁻⁶ (threshold 10⁻²); flux check 3×10⁻¹⁰.
- **K67d PASSES:** the shadow shift is 0.998 of 0.4641ε at ε = 10⁻³ (0.9998 at 10⁻⁴).

![Runs 66–67](figures/66_67.png)

**What the check added.**
1. **Confirmed with its own code:** the geometry; the boost-defect formula (for g_tt g_rr = −1, R_t̂θ̂t̂θ̂ + R_r̂θ̂r̂θ̂ = −N²R″/R, zero for Schwarzschild); the tide's growth as −2/(τ₀ − τ)², independent of L; the wave potential, with V → 0 in the horn, so the horn absorbs. Its numbers: shadow within 8.5×10⁻⁷ of the first-order form at ε = 10⁻³; the throat; infall times 5.5974, 5.5951 and 5.5949 M_K at ε = 10⁻³, 10⁻⁴ and 5×10⁻⁶; L/(4mε) = 0.998; boost-defect ratios 0.9976 and 0.9953 at ε = 10⁻³ and 10⁻⁴; the exact medium's 5.39×10⁻⁵ at p_s = 64, P∞/p_s = 10³.
2. **Added: no event horizon**, and **the tide is already large at the throat** (above). There the defect is three times Schwarzschild's horizon tide, multiplied by (E/N)² ≈ 1/n*², so an infaller into a stellar-mass hole is torn apart near the throat, before it reaches P = 0.
3. **Two phrases were overstated and are reworded.**
   - "Commits as a consequence": the geometry gives a curvature singularity reached in finite proper time; "commits" is ED's reading of it. Formation is not computed, and under option 3 Buchdahl's bound (R > 9M/4) keeps static stars out of this region, so the shell describes the end state of a collapse that has not been modelled. At P → 0 matter's pairs cannot renew, so whether matter commits or dissolves is a reading, not a result.
   - "Run 43's first echo row superseded": rather, a reflecting wall does not arise in the static vacuum solution. The throat reflects weakly (|R| changes by at most 1.2×10⁻⁵ at ε = 5×10⁻⁶), with a tortoise delay of about 16.8 M from the light ring to the throat.
4. **A conflict with the ruling that black holes evaporate.** The static hole has κ = 0 and no event horizon, so its Hawking temperature is zero. The agent's rough estimate, not computed: after a collapse, thermal emission would last only about (4/3)M ln(1/ε), a few tens of M. The 19 October ruling borrowed Kerr's κ under option A. This needs its own check.

**Reading.**
1. **Under option 3, ED's hole is Schwarzschild outside, to O(ε), and ends where possibility runs out.**
   - Its clock stops not at GR's horizon but where GR's lapse would be ε/(1 + ε), about 2mε² further out.
   - That surface is at infinite tortoise distance and infinite static proper distance, absorbs everything that falls in, and tears infallers apart in finite proper time.
2. **If this geometry forms, an infaller meets a curvature singularity at the zero-clock surface in finite proper time; in ED's terms it commits there.** That is consistent with the ruling of 19 October, not derived from it. The surface absorbs waves because it is at infinite tortoise distance. So:
   - a reflecting wall does not arise in the static vacuum solution, and the throat sends back at most 1.2×10⁻⁵ of a wave: no echoes at that level;
   - for a spinning hole this is not computed (§10: which clock the medium follows in rotation is not ruled).
3. **New:** a throat, a minimum of the area, sits where GR's lapse is (ε/2)^{1/3}, at a redshift of about 74 for ε = 5×10⁻⁶. It is 0.05% larger than GR's horizon and is invisible to waves at the 10⁻⁵ level.
4. **Not settled.**
   - **Evaporation.** The static hole's surface is cold (κ = 0) and there is no event horizon, so it does not radiate at Hawking's temperature. That conflicts with the 19 October ruling that black holes evaporate, unless a collapse changes it; to be checked.
   - The mean field fails where a place holds less than one unit (N ≲ 1/P∞), so the singularity's last stretch is in ED's discrete regime.
   - Whether a collapse ends in this vacuum is not computed. A static body cannot make it: GR's Buchdahl limit applies under option 3.
   - The scalar field stands in for gravitational waves, whose equations under the medium are not derived.
