## Note H (design note): can the relations carry a two-way shear wave? (calculation)

*23 October 2026.*
- *This note follows Runs 81 and 81b. It sets out what a gravitational wave needs, tests CO's possible carriers against those needs, and names the test that would kill each.*
- *It is a calculation, and no engine run was made. The numbers come from `shearH/designH.py` (output `designH.json`); the outside results are cited.*
- *An independent agent checked it with its own code (`shearH/checkH/`). Its corrections are included and listed at the end.*

**1. Why.**
- **The waves are the one place CO still adopts GR's equations outright.**
  - Run 11b gave the relations a six-component strain s_ij obeying linearised GR's wave equation, s̈_ij = ∇²s_ij + 16πG T_ij.
  - It then ruled which parts are real: "relations are all there is", so sliding places is free and isotropic stretch is set by matter. That leaves the two transverse-traceless (TT) polarisations, which give 0.98 of GR's binary-pulsar loss.
  - The wave equation for patterns (R6) is also adopted.
- **Runs 81 and 81b fixed two facts, shown there for longitudinal sound:**
  - a wave averaged from one-way updates is two-way at large scales only if it carries a conserved current;
  - once it does, averaging hides the arrow.

  Here both are assumed to carry over to shear.
- **In linearised GR only h^TT_ij obeys a wave equation** (Flanagan & Hughes 2005, §2.2). The rest is fixed by matter each moment, as CO's R4 fixes the clock field.

**2. What a carrier must deliver.**

| | requirement | measured bound, or reason |
|---|---|---|
| (a) | **two-way while travelling:** a current conserved *exactly* through its updates (Run 81) | with lattice-scale viscosity the attenuation over the path is Q⁻¹kD ≈ 10⁻¹⁹–10⁻¹⁷ for LIGO waves from 40 Mpc to 3 Gpc (ℓ_hop = 10³ ℓ_P), so the viscosity is harmless. A leak at rate r damps every scale alike, so GW170817 needs r ≲ 10⁻¹⁷ s⁻¹, about 10⁻⁵⁷ per tick |
| (b) | **a restoring force for shear** | without one, shear only diffuses: ω = −iνk², one-way at every scale |
| (c) | **exactly the two TT polarisations,** no breathing, longitudinal or vector waves | Run 11b: extra channels at most about 10⁻⁴ of GR's radiation (double pulsar, Kramer et al. 2021) |
| (d) | **light's speed,** at infinity and in wells | −3×10⁻¹⁵ < Δc/c < 7×10⁻¹⁶ and −2.6×10⁻⁷ < γ_GW − γ_EM < 1.2×10⁻⁶ (GW170817 with GRB 170817A; Abbott et al. 2017, ApJL 848 L13, §§4.1 and 4.3) |
| (e) | **sourced by matter's total conserved stress at Newton's G** | the double pulsar tests the wave coupling against the orbit's masses to about 10⁻⁴. Sliding requires the source to be conserved (∂_jT_ij = −∂_tT_0i), so the bodies' kinetic stress and the binding tension enter together, as in Run 11b |
| (f) | **stable:** no direction in which the energy is unbounded below | a one-way update has no steady state along such a direction (§4, C2) |
| (g) | **received:** the stretch must act on light's hops (direction-dependent, ∝ 1 + ½ n̂·h·n̂), on matter's motion and on the medium | it must act in a way that ignores sliding, or pure-sliding stretch becomes observable. Radiation reaction needs one energy shared by matter and stretch |

**3. What CO's relations have now.**
- **The structure.** Places and relations: in the engine, a cubic lattice of nearest neighbours.
- **What relations can do.** Relations can dissolve back into a two-part possibility pattern and re-form (stated 22 October).
- **How space curves.** Two readings remain open:
  - **(A)** space is the pattern of relations;
  - **(B)** relations are fixed, and space is read from a state across them.
- **What is missing.** Nothing yet gives a relation a dynamical state that propagates. Run 11b's strain was a continuum field laid over the lattice.

**4. Candidate carriers.**

**C0: places that move (any displacement medium, such as an elastic solid).**
- An isotropic elastic solid carries displacement waves, with
$$
c_t^2=\mu/\rho\ \ (\mathbf u\perp\mathbf k),\qquad c_l^2=(\lambda+2\mu)/\rho\ \ (\mathbf u\parallel\mathbf k).
$$
- **Their strain is never TT.** The strain ε_ij = ½(∂_iu_j + ∂_ju_i) is pure sliding, so its TT part is exactly zero whatever the material law (`designH.json`; the check, over 10⁴ random cases):
  - transverse waves are purely "vector" in Run 11b's split;
  - longitudinal waves are purely "longitudinal".
- **So a displacement carrier radiates only in channels Run 11b bounds to about 10⁻⁴, and none in GR's.** It also contradicts "sliding places is free", since here sliding is what stores energy.
- **Excluded by (c).**

**C1: a momentum-carrying fluid of relations or possibility** (Run 81's M2).
- Its longitudinal sound is two-way at large scales.
- Its transverse momentum only diffuses, at ω = −iνk², and on the six-direction lattice not even that.
- Its sound would be a scalar channel, bounded by Run 11b.
- **Excluded by (b) and (c)** as the carrier of GR's waves.

**C2: relations that carry their own stretch.**

Each relation carries a stretch, a state of its own, independent of where its places sit, together with the current conjugate to it. A relation along unit vector n̂ reads the strain as δℓ/ℓ = ½ n̂_i n̂_j h_ij.

- **The graph must carry a full strain tensor** (`designH.json`, reproduced by the check):

  | relation graph | strain components carried | TT wave along an axis | usable as a cell complex? |
  |---|---|---|---|
  | the engine's cubic lattice (3 directions) | 3 of 6 | only "+" seen; "×" invisible | — |
  | body-centred (4 directions) | 4 of 6 | only "×" seen | — |
  | face-centred (6 directions) | **6 of 6** | both | yes: tetrahedra and octahedra; no extra modes |
  | cubic, Kuhn triangulation (3 axes, 3 face diagonals of one orientation, 1 body diagonal) | 6 of 6 | both | yes: Roček & Williams's lattice; 1 extra mode per place; breaks cubic symmetry |
  | cubic + all face diagonals (9), cubic + all body diagonals (7) | 6 of 6 | both | no: crossing relations, so the energy is undefined |

  **On the engine's cubic relations C2 fails by counting.** The relation graph must be face-centred, or a triangulated cubic lattice.
- **The energy.**
  - For a three-dimensional relation graph, the curvature energy is Regge's: the relations are the hinges, and
$$
\int\!\sqrt{\gamma}\,R\,d^3x\;=\;2\sum_{e}\ell_e\,\varepsilon_e ,
$$
    with ε_e the deficit angle around relation e.
  - **It is invariant under sliding places, but only as a sum.** That is why lattice models that keep the tensor gauge symmetry exactly, place by place, end up with curvature-squared energies and soft waves:
    - ω ∝ k², with an extra trace mode, on a face-centred lattice (Xu 2006);
    - ω ∝ k³ in the controlled case, with linear dispersion only argued (Gu & Wen 2012, arXiv:0907.1203).
  - Linearised Regge calculus on a triangulated hypercubic lattice gives the free spin-2 propagator in the continuum limit, with vertex translations as gauge modes (Roček & Williams 1981, 1984).
  - Linear dispersion is necessary, not sufficient: the wave's speed is a separate coefficient (below).
- **Sliding places must cost nothing, at every instant.**
  - Moving places shifts h_ij by ∂_iξ_j + ∂_jξ_i.
  - With a current, an energy unchanged under *fixed* sliding still leaves three modes per wavevector that drift (the stretch creeping at constant current, driven by matter's momentum).
  - To remove them, sliding must hold moment by moment. That needs a **momentum constraint**, ∂_jπ_ij equal to matter's momentum (GR's ∇²Ξ_i = −16πS_i), or equivalently a shift: K_ij = ½(ḣ_ij − ∂_iN_j − ∂_jN_i).
  - CO's candidate for the shift is the flow of R8 and R10, g_0i = −u_i, which has no curl part yet.
  - With the momentum constraint, sliding removes the vector and longitudinal parts.
- **The isotropic stretch must be fixed by matter: for stability, not only to keep a wave out.**
  - With the Regge/Einstein energy the isotropic stretch has negative gradient energy. For γ = (1 + 2ψ)δ, ∫√γR contains +2(∇ψ)², against −¼(∂h^TT)² for the TT part (the check, by finite differences).
  - Without a ruling the scalar is a ghost or an instability; at λ = 1 it freezes. It is not a scalar wave.
  - A one-way stochastic update has no steady state along such a direction.
  - So Run 11b's "isotropic stretch is bound to matter", with R4's "clock field fixed each tick", is required as a constraint enforced every tick. It is the Hamiltonian constraint of GR.
- **What the symmetry fixes, and what it does not.**
  - **With full Lorentz invariance and linearised spacetime gauge symmetry,** the two-derivative energy is unique: the linearised Einstein form, whose only waves are the two TT polarisations (van Nieuwenhuizen 1973; Fierz & Pauli 1939 for the massive theory).
  - **CO has a preferred tick.** Its general two-derivative theory is the infrared limit of Hořava gravity (Hořava 2009; Blas, Pujolàs & Sibiryakov 2010):
$$
\sqrt{\gamma}\,N\big[K_{ij}K^{ij}-\lambda K^2+\xi R+\alpha\,a_ia^i\big],\qquad a_i=\partial_i\ln N .
$$
    That is three coefficients beyond GR:
    - λ, the kinetic coefficient;
    - ξ, which sets the TT speed, c_T² = ξ, so it is requirement (d);
    - α, which shifts Newton's constant, G_N = G/(1 − α/2), so it bears on (e).
  - Its extra scalar is healthy only with the α term, λ > 1 and 0 < α < 2. Even then, radiation differs from GR's for Newtonian sources.
  - **GR's structure means λ = ξ = 1, α = 0, with both constraints enforced.** In CO these are choices, unless borrowed.
  - **A cheaper accounting.** CO already borrows Lorentz invariance at first post-Newtonian order (R7, R8). Extending that borrowing to the stretch would supply (c) and (d) as one input.
- **The wave speed.**
  - Updating a relation's stretch on its places' ticks gives one factor of N, so c_h = N. R6's light has two factors, ticks and free capacity, so c = N².
  - With ticks alone the Shapiro delay of waves is ∫U dl, against light's 2∫U dl. That gives γ_GW = 0 and γ_GW − γ_EM = −1, about 4×10⁶ times outside the GW170817 bound.
  - A second factor, analogous to R6's capacity factor, is required.
- **What C2 would take as input:**
  1. relations carry a stretch with its own exactly conserved current;
  2. the relation graph is a face-centred or triangulated complex;
  3. the energy is Regge's, first order in curvature;
  4. the momentum constraint (or a shift) and the isotropic-stretch constraint, enforced every tick;
  5. the wave speed: a second factor of N beyond the ticks, or borrowed Lorentz invariance;
  6. the reception couplings, (g).

**5. One object for two jobs: the relations' stretch as the medium's space.**

Under option 3, CO's medium lives on a space γ̃ that stress curves (Run 66), and how γ̃ arises is open:
- Run 66 read what remains as GR's whole spatial-geometry sector;
- ONTOLOGY §7 lists "the dynamical completion with ε ≠ 0";
- Run 79 excluded a rule that reads γ̃ from the local field φ alone, and left open second-derivative rules and "a state carried by the relations that builds up across space".

**Proposal for testing: the relations' stretch in C2 *is* γ̃.**
- **Static and radiating parts.** The static part of the stretch is option 3's curved space, fixed by matter and the field's tension. Its TT part is the gravitational wave.
  - Since γ̃ = N²g differs from g only by a conformal factor, γ̃'s TT part equals GR's h^TT exactly.
- **One G, if three conditions hold:**
  - one coefficient for the scalar and TT parts (the Regge/Einstein form);
  - c_h = c;
  - the total conserved stress as source.

  Then the wave equation inherits the static sector's G. That is a consequence of those choices, not automatic.
- **A home for reading (B).** It is a state across fixed relations, one of the two classes Run 79 left open. The stretch builds up across space through the field equations, not read from φ at a point.
- **Reading (A).** It would need the same stretch carried by the relations' pattern (formation and rewiring), which is harder.

If this holds, Notes F and G, Run 79 and Run 11b are one question: the relations carry γ̃, and its TT part radiates.

**6. Tests, in order** (each to be registered before it is run).

| | test | kill |
|---|---|---|
| H1 | **Calculation.** The linearised Regge energy (2Σℓ_eε_e) for per-relation stretches on the face-centred complex and on the Kuhn-triangulated cubic complex, with conjugate currents and both constraints imposed. Count the normal modes at small k: sliding modes (3 per place), constrained modes, non-metric modes (expected 0 face-centred, 1 Kuhn), propagating modes. Registered beforehand: without the constraints, the expected ghost, instability or frozen mode | with the constraints: propagating modes other than 2; any ghost or ω² < 0; a gapless non-metric branch; ω not ∝ k; c anisotropic at leading order; drifting modes |
| H2 | **Calculation.** The wave speed with stretch updates on place ticks, with and without a second factor of N. Registered beforehand: ticks alone give c_h = N, so γ_GW = 0 | c_h ≠ c at infinity, or γ_GW ≠ γ_EM, beyond the GW170817 bounds |
| H3 | **Calculation.** Matter's conserved stress as source, with Run 11b's orbiting pair (conservation checked first) | radiated power off the quadrupole formula by more than 10⁻³; any scalar, vector or longitudinal radiation |
| H4 | **Calculation.** A single static mass: the stretch's static part against option 3's γ̃, to second order. At first order γ = 1 is nearly automatic, and a spherical source has no TT part | β ≠ 1 at O(U²) (Run 79's rule gave β = 2) |
| H5 | **Engine.** A one-way stochastic update for (stretch, current) whose average is H1's dynamics, preserving both constraints exactly every tick. A TT ripple, measured as in Run 81, with the Green–Kubo prediction (Run 81b's lesson) | overdamped at large scales; damping off its k = 0 prediction; the constraints drift |

**H1 comes first.** It is cheap, and it decides whether a lattice of relations can carry GR's two polarisations, stably and with linear dispersion. H2 is cheaper still and settles the speed.

**7. What would be derived, and what chosen.** If H1–H4 pass:
- **Derived:**
  - from sliding with the momentum constraint: no vector or longitudinal waves;
  - from sliding: the source is the total conserved stress, so a single coupling covers all stress;
  - the quadrupole formula's angular pattern. Its normalisation needs G_h = G and c_h = c.
- **Chosen:**
  - relations carry a stretch with an exactly conserved current;
  - a face-centred or triangulated relation complex;
  - Regge's energy;
  - the momentum constraint (or shift) and the isotropic-stretch constraint, every tick (Run 11b's and R4's rulings, which stability requires);
  - the Hořava coefficients λ = ξ = 1 and α = 0, or borrowed Lorentz invariance;
  - the reception couplings.
- **Shared with option 3 if section 5's conditions hold:** one G.

The likeliest outcome is linearised GR on the relations, with GR's constraint structure chosen rather than derived. That would move the wave sector from "adopted equation" to "follows from a symmetry and two constraints, given these choices". It would not be a derivation from commitment alone.

**What the check added** (`shearH/checkH/checkH.py`, independent of `designH.py`):
1. **Reproduction.** The counting and the elastic-solid result reproduce. A displacement strain has no TT part for any material, not only isotropic ones.
2. **Speed (corrected).** Ticks alone give c_h = N, not N². That gives γ_GW = 0, excluded by about 4×10⁶ times the bound, so a second factor is needed.
3. **Sliding with a current.** Fixed sliding leaves three drifting modes per wavevector; a momentum constraint or shift is needed. Sliding removes the longitudinal parts as well as the vector parts.
4. **The Hořava caveat (corrected).** There are three extra coefficients (λ, ξ, α), not one. The extra scalar is healthy only with α.
5. **Stability (added).** The Einstein/Regge energy is unbounded below in the isotropic stretch, so the isotropic-stretch ruling is required for stability.
6. **Requirements added:** reception, a conserved total source, and exact current conservation (in the form of the attenuation over the path).
7. **The energy and the graphs (corrected).**
   - In three dimensions the energy is 2Σℓ_eε_e, over relations.
   - The 7- and 9-direction graphs are not cell complexes.
   - The Kuhn triangulation is Roček & Williams's lattice.
8. **Test changes.**
   - H4 (the static mass) is decisive only at second order (β).
   - The speed test moved forward.
   - Kill conditions were added for ghosts, drift and constraint violation.
9. **Wording.**
   - Fierz & Pauli 1939 is the massive theory; massless uniqueness also needs Lorentz invariance (van Nieuwenhuizen 1973).
   - ONTOLOGY §7's wording is quoted correctly, and Runs 81 and 81b are stated as shown for longitudinal sound.
