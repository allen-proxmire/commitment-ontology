# F3: a spinning source on the 2D flow step — fail conditions (16 Nov 2026, before the run)

Flow step, τ = 0.4, r = 0.5. A ring of matter (m = 0.5, radius 60, width 6) turning with winding n = 12, held steady. Its shift is sourced by the variation of H with b, P_i = Re ψ†(sin k_i ψ) (the lattice momentum density, spin-blind as P7f's shift entry is), through the linear cost's shift equation ∇²b = −κ_b P, κ_b = 4κ (linearised Einstein's factor 4 over the lapse's source).

| check | prediction | fail if |
|---|---|---|
| F3a | the source carries the ring's orbital angular momentum: Σ(xP_y − yP_x) = ⟨−i∂_φ⟩ | off by > 2% |
| F3b | inside the ring the shift is a rigid rotation, Ω = (κ_b/4π) Σ_x P_φ(x)/r(x) (a thin shell's field: Thirring's dragging inside a rotating shell), in the ring's sense | curl of b at the centre off by > 3%, or opposite sense |
| F3c | a light packet and a massive packet crossing the centre are pushed as in a rotating frame, dk_x/dt = −Ω sin k_y | off by > 3% |

The run tests the orbital part only. In the continuum GR's shift also turns a spinor's frame (the term ¼(∇×b)·σ); P7f's directed hop, ½{b, sin k}⊗1, commutes with spin, so on the step intrinsic spin neither feels nor sources frame dragging. That is a desk statement, read separately.
