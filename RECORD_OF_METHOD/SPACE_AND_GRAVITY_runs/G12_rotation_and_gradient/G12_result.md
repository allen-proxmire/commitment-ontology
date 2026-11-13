# G12 — the shift on both axes: a rotating frame and a curl-free shift (13 Nov 2026)

**Rule tested.** G7's directed hop on both axes: nudges b_x on x-relations and b_y on y-relations, drift 2 sin b along each, U = C_x C_y A_x A_y F(θ) A_y A_x C_y C_x. GR at unit lapse and flat slices: H = E(k) + v_s·k for light and matter alike.

## A. Rotating frame (local frame dragging)

**Field.** v_s = ω(−y, x), a rigid rotation, ω = 4 × 10⁻⁴ per tick; each at ±ω, odd part; lattice 400 × 400.

**Prediction.** k rotates at ω: dk_y/dt = ω sin k_x on the lattice. A pattern moving along x with speed v feels the Coriolis push a_y = 2ωv in the continuum; on the lattice the ray prediction is a_y = ω(E_yy sin k_x + v_x).

**Fail condition, stated before the run.** a_y off the ray prediction by more than the packet's spread, or light and matter differing. (The plan named the Sagnac delay of light circling a spinning body; that needs light guided round a loop, so the local equivalent, the rotating frame's Coriolis push, was run instead.)

**Result** (g12_coriolis.out).

| packet | dk_y/dt ÷ ω sin k_x | a_y ÷ lattice ray | a_y ÷ 2ωv |
|---|---|---|---|
| light, k_x = 0.3 | 0.9996 | 0.999 | 0.941 |
| matter θ = 0.4, k_x = 0.15 | 0.9996 | 0.991 | 0.986 |
| matter θ = 0.2, k_x = 0.08 | 0.9997 | 0.978 | 0.996 |

Passed: the push is exact to 4 × 10⁻⁴, and the acceleration matches the ray prediction within 2.2%, light and matter alike. Against the continuum's 2ωv, light at k = 0.3 is 6% low, which is the lattice dispersion at that wavelength.

## B. Curl-free shift

**Field.** b_y = arcsin(gy/2), so v_s = gy along y, varying along its own relation; g = 2 × 10⁻⁴; lattice 8 × 1600.

**Correction to G7.** G7 listed this case as "pure gauge in GR". That is wrong for a time-independent shift: a curl-free shift at unit lapse on flat slices is the Painlevé–Gullstrand form of a static field (Schwarzschild has v_s = √(2GM/r)). A pattern with zero momentum is the free-faller of that form and is carried at dy/dt = v_s(y); a body at zero velocity accelerates at v_s ∂v_s.

**Prediction.** Zero-momentum packets: y(t) = y₀ e^{gt}, momentum staying zero, every mass alike. Light moving along ±y: H = E(k) + v_s(y) sin k (ray integration).

**Fail condition.** Zero-momentum packets off y₀e^{gt} by more than the packet's spread, or masses differing.

**Result** (g12_gradient.out). Zero momentum at y₀ = 200, 300 steps: moved 12.365, 12.365, 12.364 hops for θ = 0.4, 0.2, 0.1, against 12.367; momentum unchanged to 10⁻⁹. Light along ±y: displacement from the nudge 0.92 hops against the ray's 0.98, momentum change −0.0172 against −0.0177 (3% low), opposite for opposite directions.

Passed for matter, to 3 × 10⁻⁴ and every mass alike. Light is 3–6% short of the ray prediction, within the packet's momentum spread (width 40 at k = 0.3, about 8%).

## Reading

On both axes the directed hop acts as GR's shift: a rotating shift gives the Coriolis push (local frame dragging) to light and matter alike, and a curl-free shift carries zero-momentum patterns as free-fallers in the Painlevé–Gullstrand form, every mass alike. Not tested: the 1/r² shift of a spinning mass and the Sagnac delay round it, 3D, strong fields. Grade: reading.

Scripts: g12.py (walk with both conveyors; uses ../G6_light_bending/g6.py), g12_coriolis.py, g12_gradient.py, each with its .out.
