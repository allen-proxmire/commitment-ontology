## 9zf. Run 39: the ringdown with the remnant's spin (a calculation)

*19 October 2026. (step 2). The rule, method, comparisons and reading rules were fixed and hashed before the code was written (`strong/PREREG_39.md`, 11:20 UTC). Disclosed there: the first-order frame-dragging rates at the two light rings had been estimated by hand during scoping. An independent agent checked the code, numbers and bounds; its corrections are included.*

**Question.** Run 28 found that a static body under the adopted metric rings 4.4% below Schwarzschild (eikonal). GW250114 allows $\delta\hat f_{220}=+0.02^{+0.02}_{-0.02}$ and $\delta\hat\tau_{220}=-0.01^{+0.10}_{-0.09}$ at 90% (pSEOBNR, arXiv:2509.08099). Its remnant spins: χ_f = 0.68 ± 0.01, M_f = 62.7 (+1.0/−1.1) M☉ in the source frame (arXiv:2509.08054). The adopted rules now give a current field. What does ED's rotating exterior, at the order the rules define it, do to the ringdown?

**ED's rotating exterior.** In lattice (isotropic) coordinates, outside a body of angular momentum J:
$$
ds^2=-e^{-2M/r}dt^2-\frac{4J\sin^2\theta}{r}\,dt\,d\phi+e^{2M/r}\left(dr^2+r^2d\Omega^2\right).
$$
- The $g_{t\phi}$ term is the adopted current field (C2 with the Lorentz input's strength 4). It is linear in lattice coordinates, as the engine sets it.
- There are no $J^2$ terms. The rules give none until the rotation's effect on the clock field is worked out.

**Method.**
- **Eikonal (2,2) mode:** $\omega_R=2\Omega_{\rm LR}$ and $\tau=2/\lambda$, from the prograde equatorial circular null orbit and its Lyapunov exponent.
- **Three metrics at the same asymptotic M and J = aM²:**
  - **ED₁:** above.
  - **Kerr₁:** Schwarzschild plus the same first-order $g_{t\phi}$.
  - **Kerr:** exact Kerr.
- **Code checks:**
  - Kerr's light ring matches $\Omega=1/(r_{\rm ph}^{3/2}+a)$ exactly at a = 0, 0.3, 0.68 and 0.9.
  - At a = 0, ED reproduces Run 28 (Ω = 0.18394/M; 1/λ = 5.437 M).
  - Schwarzschild's λ equals Ω.

**Results** (ED / GR − 1 in the eikonal (2,2) mode).

| spin a | ED's light ring (isotropic r; throat at 1) | frequency: ED₁/Kerr₁ | ED₁/Kerr | damping time: ED₁/Kerr₁ | Kerr₁'s own error (frequency) |
|---|---|---|---|---|---|
| 0 | 2.00 | −4.4% | −4.4% | +4.6% | 0 |
| 0.05 | 1.89 | −3.8% | −3.8% | +6.3% | 0.02% |
| 0.10 | 1.78 | −3.0% | −2.9% | +8.8% | 0.1% |
| 0.15 | 1.64 | −1.8% | −1.6% | +13% | 0.3% |
| 0.20 | 1.46 | −0.2% | +0.3% | +21% | 0.5% |
| 0.25 | 1.23 | +2.6% | +3.5% | +38% | 0.9% |
| 0.30 | 0.95 (inside the throat, reached at a ≈ 0.29) | +7.7% | +9.2% | +27% | 1.4% |
| 0.68 | 0.69 (inside the throat) | — (Kerr₁ has no prograde light ring above a ≈ 0.58) | +70% | — | — |

The frequency offset's slope at a = 0 is d(δf)/da = +0.110: ED's frequency rises 0.184 per unit spin against Kerr's 0.148.

![Run 39](figures/39_spin.png)

**Verdict (as registered): undecided.** The registered comparison is undefined at a = 0.68. Both first-order exteriors fail well before the remnant's spin:
- Kerr's truncation loses its prograde light ring above a ≈ 0.58.
- ED's first-order light ring falls through ED's throat at a ≈ 0.29, beyond which the first-order metric means nothing.

**Reading.**
- **Run 28's "4% low" does not carry over to a spinning remnant.**
  - ED's ringdown is more sensitive to spin than Kerr's: its relative frequency slope is 0.50 per unit a, against Kerr's 0.385 (about 1.3 times). Frame dragging at ED's light ring (isotropic r = 2M, close to its throat) is stronger than at Kerr's.
  - The comparison can be taken to a ≤ 0.15, where Kerr's first-order truncation errs by 0.3% in frequency and 0.5% in damping time. ED's own spin-squared error is unknown.
  - Over that range spin moves ED's frequency offset from −4.4% to −1.8%: by a = 0.15, ED's frequency has risen 9.4% against Kerr₁'s 6.5%.
  - It moves the damping-time offset the other way, from +4.6% to +13%. At first order it passes +9% near a = 0.10. GW250114's 90% bound of +9% (pSEOBNR) applies at a = 0.68, not there.
  - **Linear extrapolation to a = 0.68** (not registered, and beyond where first order holds): frequency −4.4% + 0.110 × 0.68 = **+3.1%**, inside GW250114's [0, +4%]; damping time +4.6% + 0.262 × 0.68 = **+22%**, outside +9%.
- **So at first order, spin trades the frequency tension for a damping tension.** Neither number at a = 0.68 can be computed from the rules as they stand.
- **What would decide it.** ED's rotating solution beyond first order: how rotation changes the clock field, and how the current field behaves at strong field (the engine's linear rule, or the boosted-field completion). Then the gravitational (not scalar) modes, and the mass-absorption question from Run 28.
- **The adopted rules do not yet define these.** The next input, or derivation, the strong field needs is the $J^2$ structure of a rotating ED body.
