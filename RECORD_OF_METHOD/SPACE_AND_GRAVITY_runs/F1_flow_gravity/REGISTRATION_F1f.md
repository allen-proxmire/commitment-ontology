# F1f: inside the horizon, with an absorbing centre: registration (15 Nov 2026, after F1e, before this run)

**Why.** F1e's mean failed inside 0.6 r_s because the packet's leading tail ran through the capped centre and wrapped round the 1D ring. This rerun removes that: probability reaching the centre is absorbed (a smooth damping region within 30 places of the centre, applied each tick), and the registered measure is the median of what remains outside the damping region.

**Setup.** As F1e (r_s = 400, ρ₀ = 1200, m = 0.5, width 60, τ = 0.4, r = 0.5, b = −√(r_s/ρ) capped at |b| = 4), with damping exp(−0.05·(1 − ρ/30)²) per tick for ρ < 30.

**Fail condition.** At ρ_predicted = 2r_s, r_s, 0.5r_s and 0.3r_s, the median differs from the predicted path by more than 2% of the distance fallen.
