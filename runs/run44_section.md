## Run 44: Run 42 on a grid twice as fine, and whether its residual is second order

*19 October 2026. Registered and hashed with its code before the run (`fine/PREREG_44.md`, 14:31 UTC). A trial of the ball alone and the unperturbed ground state at both resolutions is disclosed there. An independent agent checked the run; its corrections and one post hoc scan are included.*

**Question.** The check of Run 42 raised two points:
- the stress term depended on the stencil (6%), because the ball is only 3 places in radius;
- post hoc, the remaining −0.086 b shrank with the ball's own field.

Does Run 42's pass survive a grid twice as fine? Is the residual second order, as a registered test?

**Setup.** As Run 42, with every length doubled in places:
- ball radius R₀ = 6 and edge width 1.4, with 216 occupants, so the potential U(r) is unchanged;
- pattern m = 2.5, so the binding is unchanged.

The trial reproduced the same body:

| | U_self | U(centre) | binding | inside r < R₀ |
|---|---|---|---|---|
| base | 0.0553 | 0.0720 | 4.92% | 84% |
| double | 0.0549 | 0.0715 | 4.85% | 86% |

The ball's strength s (occupants × s) was set to 1, ½ and ¼, at both resolutions. The stress term was taken with a 2nd-order or a 4th-order gradient.

**Results** (miss in units of the pattern's binding b; body keeping its proper size unless "held").

| | s = 1 | s = ½ | s = ¼ | linear fit in U_self: intercept, slope |
|---|---|---|---|---|
| U_self (double / base) | 0.0549 / 0.0553 | 0.0282 / 0.0284 | 0.0143 / 0.0144 | |
| **double, stress drawing** | **−0.073 (K44a passes)** | −0.042 | −0.022 | **−0.005 b, −1.25 (K44b passes)** |
| base, stress drawing (Run 42) | −0.086 | −0.047 | −0.019 | +0.002 b, −1.62 |
| double, held | −0.008 | −0.006 | −0.002 | −0.001 b, −0.14 |
| base, held | −0.019 | −0.010 | +0.002 | +0.007 b, −0.49 |
| double, no stress draw (arm a) | −0.832 | | | |
| stress drawn with the 4th-order S (double / base) | −0.060 / −0.038 | | | |

The linear fits are good to 0.002–0.004 b. With three points the intercept depends on the fit's form, though K44b passes under every form tried:

| fit | double: intercept | double: coefficient of U_self | base: intercept |
|---|---|---|---|
| linear (registered) | −0.005 b (formal 95% half-width ±0.04) | −1.25 | +0.002 b |
| through the origin | — | −1.37 | — |
| exact quadratic | +0.003 b | −1.8 (leading) | +0.017 b |

The held ball's quadratic intercepts are +0.006 b (double) and +0.020 b (base).

**A shape-preserving scan (post hoc, independent agent; not registered).** As the ball weakens, the pattern spreads out: the share inside R₀ goes 0.86 → 0.70 → 0.49. So lowering U_self also moves the pattern toward the outside case. The check reran the double-resolution, stress-drawing case with m = 2.5/√s, which keeps 86–88% inside. That scan is linear to 1×10⁻⁴: intercept −0.004 b, slope −1.26. It supports K44b and the coefficient −1.25.

**The stress term.** At s = 1 the 2nd- and 4th-order values are:
- base: S/(κω) = 0.0388 and 0.0413, a gap of 6.1%;
- double: 0.0388 and 0.0395, a gap of 1.7%.

**K44c passes.** Against the converged value, the 2nd-order gap went 6.96% → 1.74%, exactly the fourfold shrink a 2nd-order stencil's h² error predicts. The converged value comes from higher-order stencils: S/(κω) = 0.04168 at base, 0.03949 at double. The 6.1% → 1.7% quoted against S₄ looks smaller only because S₄ is itself 0.9% off at base.

The 2nd-order value staying at 0.0388 on both grids is a cancellation. The exact-gradient S fell 5.6% between grids, as the pattern's shape changed with the lattice.

![Run 44](figures/44_fine.png)

**Reading.**
1. **Run 42's pass survives the finer grid.** With the body's stress drawing, the far field counts a bound pattern's ħω once to within 0.04–0.09 of its binding on the grids and stencils run. Extrapolated to an infinitely fine grid it is about −0.07 b. At base resolution with an exact gradient it would be about −0.03 b (estimated, not run).

   Without the stress draw, the miss is the same on both grids (−0.83 b). So "stress pulls" is needed independently of resolution.
2. **What is left is second order, as registered.** On both grids and for both body models the miss goes to zero with the body's own field. The intercepts are within 0.007 b of zero for the linear fit, and within 0.006 b (double) or 0.02 b (base) for exact quadratics. Its size is
$$
\frac{\Delta D_{\rm total}}{\kappa\omega}-1\;\approx\;-1.25\,U_{\rm self}\,b\qquad(\text{body keeping its proper size, double resolution}).
$$
   - At this order it is a departure from GR, whose first law makes the residual vanish. It is of the same kind as Run 40b's strong-field miss (second order in the field), though the two configurations differ.
   - **Here b is binding in the body's own gravitational well.** Nuclear binding is not modelled.
     - Read literally, with b ~ U_self, the term is about U_self², about 10⁻²¹ for the Moon.
     - If the same form held for binding by other forces (untested), the aluminium–iron difference in binding fraction (about 5×10⁻⁴) would give about 1.25 × 4×10⁻¹¹ × 5×10⁻⁴ ≈ 2×10⁻¹⁴, below the bound of 4×10⁻¹².
     - Either way it is negligible for ordinary bodies.
3. **The held ball comes closer on the finer grid** (slope −0.14 against −0.49). The difference between the two body models is itself of order U_self·b. The check found the engine's ball is not an extremum (dD/d ln R ≠ 0), which is why the two body models differ at all.
4. **Neutron stars: a potential falsifier.** A neutron star's binding is gravitational, the kind this run models, and large: U_self ≈ 0.2, binding b ≈ 0.15.
   - Read across naively, the term is 1.25 × 0.2 × 0.15 ≈ 4×10⁻² of the star's mass.
   - Pulsar tests of the strong equivalence principle bound how a neutron star **falls** relative to white dwarfs: the triple system PSR J0337+1715 gives Δ = (+0.5 ± 1.8)×10⁻⁶ at 95% (Voisin et al. 2020).
   - This run measures how a pattern **pulls** (the far field), not how a body falls. The two agree in GR, but that is not shown for the engine.
   - The fit is extrapolated from U_self ≤ 0.055.
   - Option A's input covers black-hole exteriors, not neutron stars.
   - **If pull and fall agree in the engine and the term holds at U_self ≈ 0.2, it would exceed the bound by about 10⁴.** Not computed; the next registered test.
