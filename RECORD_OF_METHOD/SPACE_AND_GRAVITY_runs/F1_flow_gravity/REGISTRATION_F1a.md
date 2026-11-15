# F1a: free fall on the flow step: registration (15 Nov 2026, before the run)

**Reading.** On the flow step (U = exp(−iτH), τ = 0.4, r = 0.5) with P7f restated (H = ½{N/ψ², K} + σ_z mN), a slow packet in a weak field N = 1 − gx, ψ² = 1 + gx falls at the lattice rate a = g(1 + rm) (flow units, light speed 1): Einstein's g with the speed-excess factor (1 + s)², s = ½ rm. This is the palindrome's G5 result carried to the flow.

**Derivation of the prediction.** Rest energy mN(x), slope −mg; inverse inertia E″(0) = (1 + rm)/m at x = 0; a = mg·(1 + rm)/m = g(1 + rm).

**Setup.** One dimension, 6000 places, periodic. Packet from the uniform flow's positive-energy states, Gaussian in momentum at rest, widths 150 and 300 places. θ = mτ = 0.1 and 0.2 (m = 0.25, 0.5). g = 2×10⁻⁶ and 4×10⁻⁶. 1500 ticks; mean position fitted to a parabola; a converted to flow units (÷τ²).

**Fail conditions.**
- F1: at width 300, |a/(g(1 + rm)) − 1| > 1% for either mass.
- F2: doubling g changes a/g by more than 0.5%.
- Sanity: with g = 0 the packet's fitted acceleration must be below 1% of the g = 2×10⁻⁶ value.

## First run invalid (construction bug), rerun unchanged
The first run (f1a_out_bugged.txt) failed F1 and F2 with accelerations 10–20 times the prediction, growing with width. Cause: the packet builder took each momentum's positive-energy spinor with the arbitrary phase returned by the eigensolver, so the packet was scrambled in space. Fixed by a smooth gauge (first component real and positive). Debug check after the fix (600 ticks, θ = 0.1, width 150): lapse alone gives a/g = 1.1245 against 1 + rm = 1.125; hop stretch alone −0.0009; uniform field 0 to 10⁻¹³. The registered run is repeated unchanged.
