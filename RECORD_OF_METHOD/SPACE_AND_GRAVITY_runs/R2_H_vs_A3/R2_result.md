# R2: H ∝ A³ against the measured expansion history

Script: [`r2_h_vs_a3.py`](r2_h_vs_a3.py); numbers in `r2_result.json`; curves in `r2_H_vs_A3.png`.

**Registered before running.** Under born-of-record, H(a) = ν·Pr(ξ > Δ/(A(a)P_max)) and with a 1/distance source population H ∝ A(a)³. The measured history (ΛCDM: radiation, matter, then Λ) fixes the A(a) the rule requires. The test is whether any real wave background has that shape. Outcome unknown; it would change the standing of the wave rule.

**Inputs.** A as dimensionless strain. Required: A_req(a) = A_today·(H(a)/H₀)^{1/3} with H from Ω_r = 9×10⁻⁵, Ω_m = 0.31, Ω_Λ = 0.69. Candidates: primordial tensors at the r = 0.03 bound, A_s = 2.1×10⁻⁹, as an rms over modes (≈ 8×10⁻⁶, constant, set by modes at horizon entry) and as a single sub-horizon mode (∝ 1/a); the astrophysical SMBHB background, A_today ≈ 2.4×10⁻¹⁵ (PTA, at 1/yr), history ∝ cumulative star formation (Madau & Dickinson 2014). Only shapes enter H/H₀.

**Result.**

| epoch | A_req / A_today | ΛCDM H/H₀ | primordial rms | primordial one mode | astrophysical |
|---|---|---|---|---|---|
| BBN (a ≈ 10⁻⁹) | 2.1×10⁵ | 9.5×10¹⁵ | 1 | 10⁹ | 10⁻¹⁰⁴ |
| recombination | 29 | 2.3×10⁴ | 1 | 10⁹ | 10⁻³¹ |
| z = 2 | 1.44 | 3.0 | 1 | 27 | 0.03 |
| z = 1 | 1.21 | 1.8 | 1 | 8 | 0.29 |
| z = 0.5 | 1.10 | 1.3 | 1 | 3.4 | 0.61 |

(Last three columns: H/H_today implied by H ∝ A³ for that candidate.)

- No real wave background has the required shape. The radiation and matter eras need A falling as a^{−2/3} then a^{−1/2}; the primordial rms is flat, a single mode falls as a^{−1} (too steep, and 10⁹ too large), and the astrophysical background rises toward today.
- **H ∝ A³ as the sole driver of expansion is excluded** by the expansion history.
- The late era is the one place it fits: a flat primordial crest gives H ≈ constant, matching ΛCDM at z < 1 to about 30%. The mechanism can play Λ. It cannot play the decelerating eras.
- The astrophysical background is ~10⁹ below the primordial rms. On the rms reading, mergers do not set the late crest, so **"acceleration begins when mergers begin" is not supported** and the why-now coincidence is withdrawn pending a per-place crest definition that weights short wavelengths (tidal, ∝ (ℓ/λ)²), which needs the hop scale ℓ. Not available.

**Reading.** Space and Gravity has no driver for the radiation and matter eras. In standard cosmology those come from energy density through Friedmann's equation; in Space and Gravity expansion is births, and births by waves give only a Λ-like term. The one door left: the free-stock births of R1 Case A, before void record accumulated, give H ∝ a^{−3α} for a crest tail index α; a matter era needs α ≈ ½ and a radiation era α ≈ ⅔, far from the 3 of a 1/distance population. A knob, not a result.

**Post-run check.** A_req is a restatement of ΛCDM through the cube root; the landmarks reproduce H/H₀ = 2.3×10⁴ at recombination and 9.5×10¹⁵ at a = 10⁻⁹. The astrophysical history's cumulative-SFR form is crude; its direction (rising toward today) is not.
