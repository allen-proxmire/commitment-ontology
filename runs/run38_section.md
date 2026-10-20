## 9ze. Run 38: frame dragging on the engine (a construction check)

*19 October 2026. Allen: "do your next steps" (step 4). This is a construction check, not registered. The script's docstring set a 3% criterion, which the in-well releases miss (1.068). The no-well releases and the diagnostic were added after that in-well result was seen. The strength of frame dragging is the Lorentz input (Run 34), so nothing here can test ED. It checks that the engine carries a pattern with the current field.*

**Setup** (`drag/run38.py`).
- A ring of 32 committed pairs, radius 8, in the plane z = 20 of box 40, on Candidate A″'s relaxed medium (mean field). It draws 8.48 per tick.
- It rotates at tangential speed w = 0.2. Its field is static and axisymmetric (up to the lattice), so possibility's own flow is zero.
- The input's current field $g_{0i}=-4V_i$ solves the same Poisson law as the clock field's deficit, sourced by the draw density times velocity.
- A pattern (Run 16's, m = 1, width 3) is released at rest 4 places from the axis, inside the ring. The engine carries it by $\mathbf v=-g_{0i}=4\mathbf V$ (Run 35's convective form).

**Results.**

| release | sideways drift ÷ (the flow, density-weighted, integrated along the path) |
|---|---|
| no clock well (N = 1), w = 0.2 | **0.998** |
| no clock well, w = 0.05 | **0.998** |
| in the ring's clock well, w = 0.2 | 1.068 |
| in the ring's clock well, w = 0.05 | 1.068 |

- **The pattern is dragged with the ring's rotation, at the flow's speed to 0.2%.** At the release point $4V_y=0.072$, against the ring's w = 0.2.
- **In the clock well** the packet also falls outward toward the ring while it co-rotates.
  - The flow's shear turns its outward momentum, $\dot k_y=-k_x\,\partial_yv_x$: the frame-dragging (gravitomagnetic) force on a falling body.
  - ⟨k_y⟩ rises to 0.0066 at t = 15 and is 0.0056 at t = 20.
  - Its integral, $\int\langle k_y\rangle dt/\omega\approx0.087$ (with ω ≈ mN ≈ 0.84), accounts for the extra sideways drift, 1.335 − 1.250 = 0.085. So the extra 7% is that force at work, not an error in the coupling.
- **A uniform flow inside the same well** (post hoc) gives 0.979 of vT. The well is not carried with the flow, so the motion is not a pure boost.
- A centroid-based angular measure for a packet this wide and this near the axis is not clean. It gives 0.94–1.04, so it is not used.

**Reading.** The engine's patterns ride the current field as the adopted rules say, and they co-rotate with a rotating body. Its strength (GR's 4V, and Gravity Probe B's 37 mas/yr) is the Lorentz input, not a result.
