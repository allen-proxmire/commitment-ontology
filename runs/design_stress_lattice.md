# Design note: a lattice curved by the medium's own stress

21 October 2026. This note asks whether the engine can test clock universality on the medium's space γ̃ when γ̃ is curved by the medium's own field, as option 3 requires, rather than by an imposed shape (Runs 70, 72, 72b, 75). It is a calculation; no engine run was made.

*Corrected 22 October, after Run 77 and its check. The limit in 2(b) is on the source's draw times the distance to the reservoir, not on how far the lattice stretches, and it belongs to this representation: a regular equal-place lattice with one global hop rate, whose clocks are not slowed with it. The affected statements are marked.*

## 1. What can be built on a cubic lattice

Under option 3, outside matter (ε → 0):
$$
\tilde R_{ij}=2\,\partial_i\varphi\,\partial_j\varphi,\qquad \tilde\Delta\varphi=0 .
$$

**Spherical symmetry is out.** A cubic lattice with nearest-neighbour hops can carry only a diagonal metric. Equal places need √γ̃ = 1. A spherically symmetric γ̃ with unit determinant is not diagonal in Cartesian coordinates. Run 70's conformal lattice can carry it, but that reopens the "per place or per volume" question that Run 72 closed.

**Planar symmetry works exactly.** Write the metric as
$$
\tilde\gamma = ds^2+h(s)^2(dy^2+dz^2),\qquad \tilde R_{ss}=-\frac{2h''}{h},\qquad \tilde R_{yy}=-(hh''+h'^2).
$$
Then:
- R̃_yy = 0 gives (hh′)′ = 0, so B ≡ h² is linear in s.
- R̃_ss = 2φ_s² gives φ_s = F/B, with F a constant: the flux of φ per unit area, which is fixed by the source.
- Δ̃φ = 0 then holds automatically.

In the equal-place coordinate ξ (dξ = B ds), this is exactly Run 72's lattice form, with x-link conductance B² and y/z-link conductance 1/B:
$$
\tilde\gamma=B^{-2}d\xi^2+B\,(dy^2+dz^2),\qquad B(\xi)^2=B_0^2+4F|\xi|,\qquad \frac{d\varphi}{d\xi}=\frac{F}{B^2},\qquad \tilde R=\frac{2F^2}{B^2}.
$$
The lattice's own flux conservation, B²φ_ξ = const, is the same statement as the field equation. So a slab of matter curves the lattice in a closed form.

## 2. Two obstacles in the engine as built

**(a) Where released possibility goes.** The engine returns released units uniformly over the periodic box. In the field equation that is a uniform negative source with no stress. Option 3's static equations (GR's) have no static solution with such a source, so an exactly self-consistent γ̃ does not exist in the engine as it stands.
- **The fix is a boundary condition, not a rule.** Return the units in a "reservoir" plane far from the slab, standing in for infinity. Between slab and reservoir the flux is then constant and the solution above is exact.
- **It is still a change to the engine's release step.** For that reason it is flagged here rather than assumed.

**(b) The one-hop-per-tick cap.** A hop probability per tick cannot exceed one, so the conductances are scaled by c_n = 6/max(2B² + 4/B).
- c_n is the medium's hop rate per tick, and the field's gradient scales as 1/c_n (F = 6J/(c·c_n), with J the flux per place per tick).
- So a more stretched γ̃ forces a slower medium everywhere, which deepens the well, which stretches γ̃ further.
- Estimated with the closed form above (slab draw σ per place per tick, reservoir at distance ξ_r):

| σ | ξ_r | c_n | F | B² at reservoir | R̃ at slab | design effect ≈ 0.01·R̃ | φ: flat − curved |
|---|---|---|---|---|---|---|---|
| 0.01 | 6 | 0.95 | 0.022 | 1.5 | 0.001 | 10⁻⁵ | 0.03 |
| 0.01 | 12 | 0.85 | 0.025 | 2.2 | 0.001 | 10⁻⁵ | 0.10 |
| 0.02 | 6 | 0.85 | 0.050 | 2.2 | 0.005 | 5×10⁻⁵ | 0.10 |
| 0.02 | 12 | 0.52 | 0.081 | 4.9 | 0.013 | 10⁻⁴ | 0.58 |
| 0.05 | 6 | 0.29 | 0.36 | 9.6 | 0.26 | 3×10⁻³ | 1.6 |
| 0.02 | 18 | runs away | | | | | |
| 0.05 | ≥ 12 | runs away | | | | | |

- For a fixed draw the loop runs away when σ ≳ c/(4ξ_r): the draw times the distance to the reservoir is then too large, c_n collapses and no stationary lattice exists. Below that bound a stationary lattice exists however stretched it is. *(Corrected after Run 77: the first version put the limit at B² ≈ 10. Run 77's check found self-consistent lattices with B² up to 229 at ξ_r = 18, and about 1085 at ξ_r = 108.)*
- This is a limit of a regular equal-place lattice with one global hop rate, not of option 3. It disappears if the clocks slow with the hops (a uniform change of time unit), and an irregular graph of isotropic, equal-volume cells, or a local tick, would avoid it (Run 77's check).

## 3. What this means

1. **Clock universality on a self-curved lattice can add little to what is already done.** Large stress curvature appears only next to a strong source, and falls off as 1/B² away from it. *(Corrected after Run 77: the first version said the largest curvature the engine can carry stably is R̃ ≈ 0.3 per spacing². On Run 77's box, self-consistent lattices reach R̃ = 2F² ≈ 0.8 at the sheet with the medium slowed to c_n ≈ 0.07 (k = 5), and about 20 with c_n ≈ 0.014 (k = 4), at the cost of correspondingly longer runs.)*
   - There the design-dependent clock effect is about 10⁻³, at the limit of resolution. It is about 10⁻⁵ to 10⁻⁴ elsewhere.
   - Runs 72, 72b and 75 tested the same mechanism at imposed curvature R̃ = ±1.1, where it is large, and the theory matched to about half a percent.
   - The theory scales the effect to about 10⁻³⁹ for a neutron star.
   - So the open item "clock universality on a stress-curved lattice" can reasonably be recorded as settled by those runs plus the scaling.
2. **A limit on "the engine carries option 3 as built"** (§9zzo), *corrected after Run 77*.
   - With one global hop rate on a regular equal-place lattice, a self-consistent planar lattice exists only while the source's draw times the distance to the reservoir stays small. Within that bound γ̃ can stretch far (B² up to 229 on Run 77's box). *(The first version said only mildly stretched γ̃, B² ≲ 10.)*
   - The limit comes from slowing the medium's hops while the clocks keep their rate, which changes G. It disappears if both slow together, and an isotropic-cell graph or a local tick would avoid it (Run 77's check).
   - *Withdrawn:* "the engine carries option 3 in weak and moderate fields, not near holes." Spherical symmetry, where the stretch peaks near the source rather than at the far boundary, is untested, so this note says nothing about holes.
3. **One run would still add something:** the engine's own medium on its self-curved lattice, giving option 3's planar field rather than option 1's.
   - The difference is large: 20–60% in φ at the reservoir for σ = 0.01–0.02.
   - It would show by simulation, not only by calculation, that the medium hopping on γ̃ is option 3.
   - It needs the reservoir boundary condition (2a).

## 4. Choices

| choice | what it gives | cost |
|---|---|---|
| (i) Record universality on γ̃ as settled (Runs 72, 72b, 75 plus scaling), and record the hop-cap limit | closes the item; states a real limit of the engine | none |
| (ii) As (i), plus a registered planar run with reservoir release (σ ≈ 0.02, ξ_r = 6–12) | shows the engine's medium gives option 3's planar field on its self-curved lattice | an engine change to the release step (a boundary condition); about 2 hours |
| (iii) Lift the hop cap (several hops per tick, or a local tick) so strong fields can be carried | the engine near holes | a rule-level change to the hop rule, which needs a ruling |

The recommendation is (i) now, and (ii) if a simulated demonstration of option 3 is wanted. (iii) is a question for the ontology, not a run.

*After Run 77: (ii) was run (§9zzz2). The limit may need no change to the hop rule (clocks slowed with the hops, or isotropic cells), so (iii) is first a question about how the lattice represents γ̃ (the check).*
