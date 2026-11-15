# F1b: light bending on the flow step: registration (15 Nov 2026, before the run)

**Reading.** On the 2D flow step (τ = 0.4, r = 0.5, massless) with P7f restated (H = ½{N/ψ², K}), a light packet moving across a weak field N = 1 − gx, ψ² = 1 + gx bends toward lower N at the ray rate a_x = 2g·ω·∂²ω/∂k_x² (flow units), which is 2g (twice the Newtonian pull: lapse and stretch together) up to the lattice factor ω ω_xx at the packet's momentum. This is the palindrome's G6 result carried to the flow.

**Derivation.** Local energy E = D(x)ω(k), D = N/ψ² ≈ 1 − 2gx: dk_x/dt = 2gω, dx/dt = D ∂ω/∂k_x, so ẍ = 2g ω ω_xx at k_x = 0.

**Setup.** 400 × 256 places, periodic; packet at k = (0, 0.3), width 30; 150 ticks; g = ±10⁻⁴, the odd part (a(g) − a(−g))/2 taken to remove second-order terms; x(t) fitted to a parabola.

**Fail conditions.**
- F1: |a_x / (2g ω ω_xx) − 1| > 2%.
- Reported: the lattice factor ω ω_xx at k = (0, 0.3) against 1 (the continuum's 2g).
