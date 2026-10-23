## 9zza. Run 55: ED's medium and the pulsar triple, under the variational draw

*20 October 2026. (steps 2–3). Registered and hashed before the run (`medium55/PREREG_55.md`, 12:40 UTC). An independent agent checked the run. Its corrections change the reported pulsar numbers but no registered verdict. Disclosed:*
- *The registered star at U_self = 0.30 failed (its calibration hit an invalid value). The star table was extended post hoc by continuation (`posthoc55b.py`, `posthoc55c.py`). A first retry (`posthoc55_failed.py`) started from a count 16% too large, a scaling slip, and was stopped.*
- *The registered mapping of the pulsar's radius to its surface potential was wrong, and the registered analysis clamped C at the table's end instead of extrapolating. Both were corrected post hoc (`posthoc55_pulsar.py`).*
- *During the run it was ruled that inertia = total energy (§10).*

**Question.** Under the adopted variational draw, a body's equivalence-principle violation is (Runs 52, 54)
$$
\Delta=\frac{M_{\rm far}}{E_H}-1\;\approx\;\bar g-g_{\rm bg},\qquad g=c\,\frac{d\ln R}{dz}-1 ,
$$
given inertia = E_H. What does that predict for ED's own medium, the A″ mean field, and how does it compare with the pulsar triple PSR J0337+1715?

**1. ED's medium is not scale-free (K55a: PASS).** Computed from the medium's exact mean occupancy (f(n) = c ln(1 + n/p_s), π(n) ∝ zⁿ/∏f(k); §9zb):

| p_s | P/p_s = 16 | 64 | 256 | 1024 |
|---|---|---|---|---|
| 64: g·P/p_s, s | 0.9857, 1.0075 | 0.9752, 1.0079 | 0.9645, 1.0081 | 0.9537, 1.0082 |
| 256 | 0.9964, 1.0018 | 0.9938, 1.0019 | 0.9911, 1.0020 | 0.9884, 1.0021 |
| 1024 | 0.9991, 1.0005 | 0.9985, 1.0005 | 0.9978, 1.0005 | 0.9971, 1.0005 |

- Registered: PASS if |g·P/p_s − 1| ≤ 4/p_s and |s − 1| ≤ 0.02 at every point with p_s ≥ 64. All 12 points pass.
- *Correction (check):* the run's p_s = P/p_s = 1024 entry (0.997079, s = 0.9978) was a float64 rounding artifact. The table gives the exact values from the check's cumulant computation.
- **The exact form** (the check, from the identities ⟨f(n)⟩ = z and Cov(n, f(n)) = z; it matches the exact values to 10⁻⁵ for p_s and P/p_s from 16 to 16384):
$$
g=\frac{p_s-b}{P},\qquad b=\tfrac12\ln\!\Big(1+\frac{P}{p_s}\Big)-\tfrac12,\qquad s\equiv-\frac{d\ln g}{d\ln P}\approx1+\frac{1}{2p_s}.
$$
- At ED's physical scales (p_s ≳ 4×10⁵, P₀/p_s ≳ 10⁵), g·P/p_s = 1 − b/p_s ≈ 1 − 1.4×10⁻⁵ and s − 1 ≈ 1.3×10⁻⁶. *Correction:* the registration's "to better than 10⁻⁵" is slightly too strong. The medium is Run 51's controlled medium with α = 1, to about 10⁻⁵.
- With s = 1 the violation becomes one number per star:
$$
\bar g-g_{\rm bg}=g_{\rm bg}\,C,\qquad C=\Big\langle\frac{P_0}{P}\Big\rangle_T-1,\qquad \Delta\simeq C\,\frac{p_s}{P_0}.
$$
  The average is weighted by the Tolman draw T. The check confirms ḡ − g_bg = g_bg·C to 4×10⁻⁵ relative, including the star's own restructuring.

**2. The formula at another compactness (K55b: PASS).** At U_self = 0.12 (h = ⅓, g = αp_s/P at 4×10⁻³, variational draw), the energy-based fall shifts by 5.1295×10⁻⁴, against ḡ − g_bg = 5.1484×10⁻⁴: a ratio of 0.9963, inside the registered 3%.
- The lattice form (1 + ḡ)(ΣT/E_H)/(1 + g_bg) − (ΣT/E_H)₀ predicts 5.1293×10⁻⁴. The −0.4% is the 1/(1 + g_bg) factor.
- First law (trapezoid): 2.5×10⁻⁹ in both media.
- Given the Hellmann–Feynman relation and the virial identity this is close to algebraic: a consistency check at a second compactness.

**3. C against compactness.** Γ = 2 and Γ = 3 stars in exact hydrostatic balance, h = ⅓, scale-free medium. U_s = −ln μ̃ is the surface potential.

| | (U_s, C) |
|---|---|
| Γ = 2, registered (radius 12.3 cells) | (0.033, 0.051), (0.065, 0.106), (0.096, 0.164), (0.125, 0.225), (0.154, 0.291) |
| Γ = 2, post hoc (count × 1.00 … 1.25 at fixed K) | (0.134, 0.246), (0.152, 0.288), (0.174, 0.345), (0.189, 0.385), (0.209, 0.451), (0.218, 0.481) |
| Γ = 3, post hoc (count × 1.00 … 1.80 at fixed K) | (0.156, 0.246), (0.176, 0.283), (0.196, 0.325), (0.211, 0.355), (0.218, 0.371), (0.234, 0.406), (0.251, 0.448), (0.279, 0.522), (0.335, 0.695) |

- **Weak-field check.** C/U_s → 1.515 for Γ = 2, against the Newtonian n = 1 polytrope's 6/(5 − n) = 1.5. For Γ = 3 the check's two weak-field stars extrapolate to 1.336, against 4/3 for n = ½.
- **Grid dependence is small.** C at fixed U_s moves by +0.3% at h = ½ and −0.2% at h = ¼ (the check). The branch stars shrink to about 9 cells in radius, which changes C by ≤ 0.3%.
- **The end of the Γ = 2 branch.** Count continuation at fixed K converges up to × 1.25 (U_s = 0.218) and fails at × 1.26 and × 1.28. The failed solves stall at residuals that grow with distance (1.1×10⁻³, 5.9×10⁻³), and the step in U_s grows as a fold's would (dU_s/df: 0.21, 0.23, 0.26, 0.29, 0.36, 0.52, 0.88). A fold fit, U_s = U* − a√(f* − f), gives f* ≈ 1.258 and **U* ≈ 0.235** (the check).
  - Claimed: no Γ = 2 equilibrium past count × 1.26 at this K; the data fit a maximum-count fold at U_s ≈ 0.235; so no Γ = 2 star reaches 11 km (U_s ≥ 0.244).
  - Not claimed: that the fold is proven (that needs continuation through the turn), or anything about equilibria beyond it, whose stability a static engine cannot judge.
  - The check's earlier "turns over near 0.20" at h = ½ came from a coarse step and is withdrawn.
- **Γ = 3 converges past U_s = 0.33** (stopped by hand there; its end was not sought).

**4. The pulsar, corrected.** PSR J0337+1715's pulsar has M = 1.438 M☉ (GM/c² = 2.123 km); its radius is unmeasured, taken as 11–13 km. *Correction (check):* the registration set U_s = GM/(Rc²), treating the areal radius as the engine's coordinate radius. The engine's exterior is U = GM/r exactly in isotropic coordinates, so:

| R (km) | GM/(Rc²) | U_s, engine's areal radius (U e^{−U} = GM/Rc²) | U_s, surface redshift (−½ ln(1 − 2GM/Rc²)) |
|---|---|---|---|
| 13 | 0.163 | 0.199 | 0.198 |
| 12 | 0.177 | 0.221 | 0.218 |
| 11 | 0.193 | 0.247 | 0.244 |

The registered 0.164–0.193 understated U_s by 20–26%.

**5. The bound.** C is interpolated (monotone cubic through the origin) inside each equation of state's converged range. The registered analysis instead held C at the table's last value (0.291) beyond U_s = 0.154 and reported P₀/p_s ≥ 1.27×10⁵; that number is superseded. The bound is Voisin et al. 2025 (A&A 693, A143), 95%: |Δ| < 2.3×10⁻⁶ with red timing noise, < 1.5×10⁻⁶ with a circum-ternary planet.

| R | C, Γ = 3 | C, Γ = 2 | P₀/p_s ≥ (2.3×10⁻⁶) | P₀/p_s ≥ (1.5×10⁻⁶) |
|---|---|---|---|---|
| 13 km | 0.33 | 0.41–0.42 | 1.4–1.8×10⁵ | 2.2–2.8×10⁵ |
| 12 km | 0.37–0.38 | 0.48–0.49 (just past the last converged star, inside the fitted fold) | 1.6×10⁵ (Γ = 3); 2.1×10⁵ (Γ = 2) | 2.5×10⁵; 3.2×10⁵ |
| 11 km | 0.43–0.44 | no star (beyond the fold) | 1.9×10⁵ | 2.9×10⁵ |

The ranges within a cell are the two radius mappings, which differ by about 1%. So, from converged stars:
$$
\frac{P_0}{p_s}\gtrsim1.4\text{–}1.9\times10^5\ \ (2.2\text{–}2.9\times10^5\ \text{with the planet model}),\qquad \frac{p_s}{P_0}\lesssim3.4\text{–}7\times10^{-6},
$$
rising to about 2.1×10⁵ (3.2×10⁵) if the Γ = 2 star at 12 km is included.
- The spread comes from the radius (about 30%), the equation of state (Γ = 3 is 20% below Γ = 2 at 13 km: 0.330 against 0.415) and the noise model. A realistic equation of state is neither polytrope.
- The white dwarfs' C ≈ 1.7U ≈ 3×10⁻⁵ is negligible.

**6. Inertia.** The registration's von Laue note was checked:
- **Right:** for a static closed system with a conserved total energy–momentum tensor, the total stress integrates to zero and (E, P) is a four-vector. The virial identity under V, W_f = 3∫pN√γ + 2κ∫|∇ψ|², is the trace of that condition and holds in any medium.
- **Overstated:**
  - only the trace is shown (a full proof needs ∫T^{xx} = 0 along the boost; the trace gives it for spherical or cubic bodies);
  - any equilibrium of a covariant theory satisfies the identity, so it adds no evidence;
  - the adopted Lorentz input covered first post-Newtonian order only.
- **So inertia = E_H needed an input,** and a ruling supplied it: the Lorentz input extended to the complete dynamics (§10). The boosted far field carries the active momentum M_far·v, and the difference from E_H·v is the Nordtvedt effect, as in Brans–Dicke-type theories.

![Runs 55–56](figures/55_56.png)

**Reading.**
1. **ED's medium, as specified, is not scale-free.** The scale p_s, brought in after Run 22 so that clocks of different design agree, makes the medium depart from scale-free as g = (p_s − b)/P ≈ p_s/P.
2. **With inertia = total energy, ED predicts a strong-equivalence-principle violation for compact bodies:**
$$
\Delta=\frac{m_{\rm grav}}{m_{\rm inertial}}-1\;\simeq\;C\,\frac{p_s}{P_0}>0 .
$$
   - It is negligible for light bodies, grows with compactness (C ≈ 0.33–0.49 for the pulsar, Γ = 3 to Γ = 2), and is not additive.
   - GR predicts exactly zero.
3. **Its size is not predicted.** ED does not yet fix P₀/p_s. The pulsar triple requires P₀/p_s ≳ 1.4–2.9×10⁵, tighter than, and consistent with, the first-order bound of Run 45 (10⁵). If ED fixed P₀/p_s, this would become a definite number for pulsar timing, with a definite sign.
