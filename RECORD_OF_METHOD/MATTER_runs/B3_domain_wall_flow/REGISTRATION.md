# B3: the domain-wall construction on the flow step: registration (15 Nov 2026, before the run)

**Reading.** Tuning 2's candidate removal (B2/B2b, shown on the palindrome) carries to the flow step: on the 2D Wilson–Dirac flow (U = exp(−iτH), τ = 0.4, r = 0.5) with x physical (momentum k) and an inner ring s of 2L places carrying a mass wall (m = +0.5 on one half, −0.5 on the other; −2r < −0.5 < 0 is the topological side), each wall binds one one-way mode, and a generic local disturbance cannot give the pair a mass beyond an overlap that falls exponentially with L.

**Measure.** H(k) = σ_x sin k + σ_y sin_s + σ_z(m(s) + r(1 − cos k) + r(1 − cos_s)), inner hops on the ring; m_leftover = ½ min over k of the splitting of the two sub-gap levels. Disturbance after each tick: P_s = exp(−iε n̂_s·σ), n_s = (1,1,1) + unit Gaussian (as B2), uniform in x.

**Control.** The plain 1D flow (no inner direction) at m = 0 with the coherent disturbance (n̂ = (1,1,1)/√3): its mass is the leak a counter-term would cancel.

**Fail conditions.**
- F1: at ε = 0, log m_leftover against L (L = 8, 12, 16, 20, 24) is not a falling line (slope > −0.1 per place, or R² < 0.98).
- F2: at ε = 0.2, for the coherent disturbance or any of 5 random draws (seed 77), the same fails, or m_leftover(24) exceeds 1% of the control's mass at ε = 0.2.
- Uninformative: the control's mass is below 0.3ε·τ (per tick).
