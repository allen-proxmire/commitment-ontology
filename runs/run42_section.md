## 9zj. Run 42: a pattern inside a body, at weak field

*19 October 2026. Pre-registered and hashed with its code before the run (`inside/PREREG_42.md`, 13:51 UTC). The registration discloses a trial of the unperturbed ground states, used to choose m. An independent agent checked the run; its corrections are included.*

**Question.** Run 40c showed that at weak field a pattern bound **outside** a body pulls by ħω, binding counted once. Atoms and nuclei are bound **inside**: they are patterns within the matter that binds them. That is what the Moon's aluminium and iron test (Bartlett & van Buren). Does the far field count ħω once when the pattern sits inside the body?

**Why it might not.**
- A pattern outside a ball pulls on the ball's matter evenly (the shell theorem), so the ball needs no extra internal support.
- A pattern inside pulls the ball's matter inward, and the ball must hold itself up with internal stress. In GR that stress pulls too, with weight 1 per direction (Tolman's ρ + 3p; PPN ζ₄).

With $\partial_jT^{ij}=f^i$ and a free surface, the virial theorem gives the stress's total:
$$
S=\int\sum_iT^{ii}\,dV=-\int\mathbf x\cdot\mathbf f\,dV=-\sum_x s_b(x)\,(\mathbf x-\mathbf c)\cdot\nabla U_p(x)\;>0 .
$$
Here $s_b$ is the ball's draw density and $U_p$ is the pattern's potential. S is positive because the pull is inward, so the stress is compressive, as in Tolman's ρ + 3p.

The engine's bodies have no stresses, so two arms were registered:
- **(a)** the adopted rules as they stand;
- **(b)** the ball's stress draws: S is added, spread like the ball's draw, and recomputed self-consistently.

**Setup.** Run 40c's unbounded, weak-field medium (p_s = 64, P₀ = 4096).
- **The ball:** self-similar and keeping its proper size; 54 pairs, radius 3, potential 0.072 at its centre, draw-weighted self-potential U_self = 0.055.
- **The pattern:** its ground state under the adopted rule (energy + flux), at test strength.

**Results** (ΔD_total/(κω), with the miss in units of the pattern's binding b).

| pattern | binding b | inside r < 3 | **(b) stress draws** | (a) no stress | stress term S/(κω) |
|---|---|---|---|---|---|
| **ground, m = 5 (registered)** | 4.9% | 84% | **0.99576 (−0.086 b): K42 passes** | 0.95901 (−0.83 b) | +0.0388 (0.79 b) |
| ground, m = 3 | 3.7% | 54% | 0.99685 (−0.084 b) | 0.97481 (−0.67 b) | +0.0233 |
| ground, m = 8 | 5.7% | 97% | 0.99516 (−0.085 b) | 0.94783 (−0.92 b) | +0.0499 |
| xy, m = 2 (outside: check) | 0.52% | 0% | 0.99977 (−0.043 b) | 0.99975 (−0.048 b, as Run 40c) | +0.00003 |

At m = 5, both with the stress drawing:
- **Held ball:** 0.99906 (−0.019 b).
- **Energy-only:** 0.97642 (−0.48 b).

![Run 42](figures/42_inside.png)

**Checks** (independent agent).
- **Resolution.** The ball is only 3 cells in radius, so S depends on how it is computed.
  - A 4th-order gradient gives S = 0.0413 κω (+0.05 b on arm b).
  - A rough spherical hydrostatic 3∫p gives 0.047 (+0.17 b).
  - K42 passes either way.
- **Spreading.** Spreading S as 3p(r) instead of like the draw gives −0.090 b (adjusting) and −0.023 b (held).
- **Balance.** The net force on the ball is about 10⁻¹⁶ against Σ|f| = 1.6×10⁻⁵, and S is unchanged when the origin moves by half a cell.
- **What arm (a) is missing.** Arm (a) misses by 0.833 b. The stress term alone is 0.788 b; the rest is the stress draw's feedback on the ball.

**The remaining −0.085 b shrinks with the body's own field (post hoc, independent agent; not registered).** The ball was rerun at ½ and ¼ strength, with U_self = 0.055, 0.028 and 0.014:

| ball strength | 1 | ½ | ¼ |
|---|---|---|---|
| adjusting, stress drawing | −0.086 b | −0.047 b | −0.019 b |
| held, stress drawing | −0.019 b | −0.010 b | +0.002 b |

So the miss is about −1.5 U_self·b: a term of order b·U_self, second order, not a first-order failure. That is why it is the same at m = 3, 5 and 8, whose bindings differ but whose ball does not.

The gap between held and adjusting also scales as U_self. The ball's draw changes with its size (dD₀/d ln R = 1.10 ≈ D₀U_self), which gives δD ≈ −0.067 b. Making the ball also draw stress for its own binding does not remove the gap (−0.093 b adjusting, −0.053 b held).

Likely sources are:
- cross terms of order U_self·U_p in the engine's nonlinear clock map;
- the uniform $e^{-\bar U_p}$ rescale applied to a U_p that varies 1.7× across the ball.

**In GR terms.**
- Nothing is counted twice. The adjusting ball carries its own binding's response (Run 40c), and S carries the stress from the mutual pull. Both appear in the Komar mass $\int\alpha(\rho+\sum T^{ii})\sqrt\gamma$.
- GR's first law makes the change in total mass the pattern's Killing energy, with the star's rearrangement entering only at second order. So in GR the held and adjusting balls agree, and the residual vanishes.
- The engine's ball is not an extremum (dD/d ln R ≠ 0), so neither arm is "the GR one". To first order they coincide, and both pass.

**Reading.**
1. **Internal binding counts once at weak field, but only if the body's internal stress pulls.**
   - With the stress drawing, all three masses land within 0.09 of a binding, with 54–97% of the pattern inside the ball. What remains is second order in the body's field.
   - Without it, they miss by 0.67–0.92 bindings, almost all of it the stress term.
   - The check case behaves as it should. With the pattern outside, the stress term is about zero, and both arms match Run 40c.
2. **"Stress pulls" (PPN ζ₄) is therefore needed, not optional.** Measured physics requires internal binding to pull like rest mass (aluminium against iron, to 4×10⁻¹²).
   - Under the adopted rules that happens only if a body's internal stresses draw, with weight 1 per direction, just as a pattern's momentum flux does.
   - **It is the same input in a fuller form:** the Lorentz input extended from moving matter's kinetic pressure to all of a body's stresses (the whole source transforms together).
   - **Adopted (19 October): "Yes — stress pulls, as part of the Lorentz input"** (§9zl).
3. **Energy-only misses by about half a binding** even with the stress drawing. So the patterns' momentum flux is still needed, as in Run 40c.
4. **Not settled here:** S at higher resolution, and the U_self scaling as a registered test.
