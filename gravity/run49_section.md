## Run 49: is the 4% pull miss CO's, or the engine's body model?

*20 October 2026. Registered and hashed with every imported module before the run (`dilation/PREREG_49.md`; same hash file and restart note as Run 48). One code check (base grid, weak field, not a registered case) ran before registering. The post hoc runs were made after the results and after the independent check: the checker's `check4849/` and `posthoc49.py`. An independent agent checked the run; its corrections are included and change the reading.*

**Question.** At neutron-star strength a bound pattern's pull falls 4% short of κω: the miss is −0.20 b (Runs 46–46c). In GR, adding a quantum of Killing energy ħω to a static star raises its mass by ħω to first order. That holds for any equation of state, because an equilibrium star is a stationary point of its mass at fixed baryon number and entropy (Hartle–Sharp).

The engine's body is different in two ways:
- its stress has no energy of its own;
- its size is fixed by a rule.

Is the 4% the body model?

**The three bodies (registered).** All use the scale-free medium of Run 48, the full pattern rule and the Tolman/Komar draw.
- **A, the control** (Run 46c's body):
  - stress that holds it, with no energy of its own, set by the virial with weight sb (the rest draw);
  - proper size.
- **H, matter held at proper size:**
  - internal energy and pressure from ε = K n^{Γ−1} (n = νN³), p = (Γ−1)nε;
  - stress = what holds it, with weight sb(1 + Γε);
  - proper size.
- **E, the same matter re-settling** at fixed count and entropy:
  - stress = its own pressure, σ = 3(Γ−1) sb ε (Tolman's 3pN√γ);
  - radius from the balance Σσ = S_need(R), for a self-similar (homologous) ball.
- The isolated H and E bodies coincide at R₀ by calibration, with U_self matched to A's.

**Results** (miss in units of b).

| body | U ≈ 0.22, double | U ≈ 0.22, triple | U ≈ 0.066, double | radius change from the pattern (double) |
|---|---|---|---|---|
| A | −0.196 | −0.201 | −0.047 | — |
| H (Γ = 2) | −0.183 | −0.188 | −0.037 | −1.4×10⁻⁵ |
| E (Γ = 2) | **−0.343** | **−0.349** | −0.054 | −1.2×10⁻⁴ |
| E (Γ = 3) | −0.218 | −0.224 | — | −5.6×10⁻⁵ |

**Verdicts, as registered.**
- **K49a passes:** −0.1964 and −0.2008, against −0.1962 and −0.2007.
  - It is not an independent control: it runs the same code as Run 48's h = ½ point (−0.19638).
- **K49b: neither registered outcome.**
  - The analysis script prints "PARTLY", the otherwise branch, but the miss *grew*: re-settling took it from −0.196 to −0.343 b (double) and from −0.201 to −0.349 b (triple).
  - The "share removed" is −75%.

**What the check found: the equilibrium rule sets the answer.**
- A static fluid obeys ∂ᵢp = −(ρ + p) ∂ᵢ ln N. Take its moment with the Tolman measure N√γ = N⁻², the same measure the stress draw uses:
$$
3\sum p\,N\sqrt{\gamma}=-\sum(\rho+3p)\,N\sqrt{\gamma}\;\mathbf x\cdot\nabla U .
$$
- **So the weight in the virial should be the matter's whole draw, (ρ + 3p)N√γ.** For E and H matter that is w = sb[1 + (3Γ − 2)ε]. For body A it is sb + st, the rest draw plus the stress draw.
- Run 49 used sb(1 + Γε). Runs 42–46c used sb for body A.
- The difference is a post-Newtonian term, the same order as the 4%. It shrinks with the field, so the first-order results (the intercepts of Runs 42–46) stand. Run 44's second-order slope, ≈ −1.25 U·b, came from the same weight.
- The re-settling term equals the slope of the engine's energy at the virial point times the radius change. At h = ½ that is dẼ/d ln R = 0.178 times −1.09×10⁻⁴, which gives −0.160 b, against −0.160 b measured.
- At Newtonian order the engine *is* stationary: E − H is then second order in the pattern's amplitude, for any weight.
- So these numbers do not show that the engine lacks GR's stationarity. They show that its stress and equilibrium rules were fixed, at post-Newtonian order, in a way that matters here.

**Post hoc, with the stress weight of exact hydrostatics** (miss in units of b).

| body | U ≈ 0.22, double | U ≈ 0.22, triple | U ≈ 0.066, double | source |
|---|---|---|---|---|
| A (weight sb + st) | **+0.038** | **+0.031** | +0.012 | `posthoc49.py` |
| E (Γ = 2, weight 1 + 4ε) | **+0.029** | — | +0.017 | the check |
| H (Γ = 2, weight 1 + 4ε) | −0.116 | — | −0.017 | the check |

- With the hydrostatic weight, both self-consistent bodies show a small *excess*, not a deficit, of about +0.03 b (about 0.6% of κω):
  - A, stress-supported and held;
  - E, matter that re-settles.
- The 4% deficit is gone.
- H mixes an EOS internal energy with a stress that is not its pressure, and it lands at −0.12 b.
- These remain homologous balls, not hydrostatic profiles. Different exact moments disagree at O(U) for a non-hydrostatic profile, so about ±0.1 b is a systematic error of the body model.

**Reading.**
1. **The 4% deficit is not CO's; it came mostly from the stress rule.**
   - Runs 42–46c sized the stress by the virial with the rest draw as weight. Exact hydrostatics weights by the whole draw, stress included.
   - With that weight the held body's miss goes from −0.20 b to +0.03 b, and re-settling matter gives about the same.
   - This is post hoc. It needs a registered run before the record treats it as settled.
2. **The registered question gets no clean answer.** The re-settling body's number is set by the equilibrium rule's post-Newtonian weight:
   - with Run 49's weight, −0.34 b;
   - with the hydrostatic weight, +0.03 b.
3. **At ordinary strengths the differences shrink.** All bodies and weights lie within −0.054 to +0.017 b at U ≈ 0.066, and the first-order results stand.
4. **What would settle it: a body in local hydrostatic equilibrium on the lattice.** That means a non-homologous profile solved point by point from ∂p = (ρ + p)∂U with an equation of state. It needs no weight choice and no homologous approximation.
   - In GR the first law makes that answer zero for every Γ.
   - If the engine gives zero too (to the grid), CO's static rules have GR's mass bookkeeping at strong field. If not, the miss is a genuine CO departure.
5. **Run 47's discussion of a 4% active-mass deficit** (pulsar timing, J0737−3039B's binding energy) **is on hold until then.** The deficit may not exist.
