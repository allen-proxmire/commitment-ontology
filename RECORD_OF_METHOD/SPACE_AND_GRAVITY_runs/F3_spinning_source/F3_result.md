# F3: a spinning source on the 2D flow step (16 Nov 2026)

Fail conditions in FAIL_CONDITIONS.md, written before the run. A ring of matter (m = 0.5, radius 60, width 6, winding n = 12), held steady, sources the shift through the linear cost, ∇²b = −κ_b P, with P_i = Re ψ†(sin k_i ψ), the variation of H with b.

| check | result | outcome |
|---|---|---|
| F3a | the source's angular momentum Σ(xP_y − yP_x) = 11.962 against ⟨−i∂_φ⟩ = 12.043 (−0.7%) | PASS |
| F3b | inside the ring the shift turns rigidly in the ring's sense, Ω = 7.394 × 10⁻⁴ against the thin-shell value in the periodic box 7.394 × 10⁻⁴ (Thirring's dragging inside a rotating shell, 2D) | PASS (first pass solved the shift equation with its sign reversed, and compared with the free-space value, 13% above the box's: the box forces curl b to average zero; both corrected, f3_out_firstpass.txt) |
| F3c | light and a massive packet crossing the centre are pushed as in a rotating frame, dk_x/dt = −Ω sin k_y, to 0.7% and 0.3%, reversing with travel | PASS |

**Reading.** A spinning source on the step drags the frames inside it in its own sense, at the rate the linear cost gives, and light and matter there feel it as a rotating frame. Orbital motion only: see below. 2D, steady source, weak field.

**Desk: intrinsic spin and the shift.** P7f restated enters the shift as ½{b_j, sin k_j}⊗1, which commutes with spin. In the continuum, the Dirac Hamiltonian for a general metric (Obukhov, Silenko and Teryaev, Phys. Rev. D 80, 064044 (2009)) carries the same orbital term plus

$$\tfrac{\hbar}{4}\,\boldsymbol\Sigma\cdot(\nabla\times\mathbf b),$$

which makes a spin follow a dragged frame (for a frame turning at Ω, b = −Ω × r, it is −Ω·S, completing H − Ω·(L + S); in 2D, Σ·(∇×b) = σ_z(∇×b)_z with σ_z = β). Its lapse-and-stretch part, ½{N/ψ², α·p} + βmN, is already that Hamiltonian's form. So on the step, as entered, intrinsic spin neither feels frame dragging nor sources it (by variation, the source misses half the spin density's curl, the Belinfante term; in F3 the ring's spin, ⟨σ_z⟩/2 = 0.46, is about 4% of its angular momentum). Two consequences:
- *No backdrop for spinors.* P7e frees relabelling places, and a rotating relabelling turns each place's frame; the spinor turns with it (the exchange sign rests on that turn). Without the term, a rotating shift is not a pure relabelling for spin.
- *Observation.* Intrinsic-spin precession in Earth's gravitomagnetic field (about 10⁻¹⁴ rad/s) is not measured; no present bound separates the two.

The repair is the term itself, ¼(∇×b)·σ on each place (local, spin-only; F2 and F3's orbital results unchanged to leading order, corrections of order ħ∇Ω/p; the curl-free runs F1e, F2e, F2f exactly), and with it the source gains half the spin density's curl, as in GR. F3 ran with the spin-blind entry: with the term its source would carry L + S (12.0 + 0.46), not rerun.
