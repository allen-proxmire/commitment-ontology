# F1c: the closed loop on the flow step: registration (15 Nov 2026, before the run)

**Reading.** G13 carried to the flow: two patterns on the 1D flow step (τ = 0.4, r = 0.5), each sourcing its own lapse by a wave equation at light's speed, each feeling only the other's field through P7f restated (here the lapse alone, as in G13: H = ½{N, K} + σ_z mN, N = 1 − h). Nothing moves until the field front arrives; then each falls toward the other at a_b = −(κm_a/2)(1 + rm_b), a_a = +(κm_b/2)(1 + rm_a) (flow units; the 1D static slope behind the front times F1a's lattice factor).

**Setup.** 6000 places, periodic. m_a = 0.25, m_b = 0.125 (θ = 0.1, 0.05 per tick), at rest, separation 1200, packet width 250. h_tt = h_xx + κ(ρ − ⟨ρ⟩), ρ = m|ψ|², κ = 10⁻⁵, four field sub-steps per tick, fields start at zero. 6000 ticks. Front reaches the other pattern at tick 3000; "before" fit over ticks 0–2700, "after" fit over ticks 3700–6000 (the front has crossed the packet; the field returns round the ring only after tick 12000).

**Fail conditions.**
- F1: before the front, either |a| exceeds 5% of its predicted after-front value.
- F2: after the front, either a differs from its prediction by more than 3%.
- F3: the balance (m_a a_a + m_b a_b)/(m_a|a_a|) differs from its predicted r(m_a − m_b)/(1 + rm_a) = +0.056 by more than 0.02.
