# The ontology

The primitives, the rules and the inputs as they stand. Each rule is marked **derived**, **added** (chosen when the primitives were silent) or **borrowed** (taken from established physics). The history of every rule is in [`archive/`](archive/INDEX.md).

## Primitives

| primitive | what it is |
|---|---|
| **Commitment** | one irreversible update at a place. Time at a place is the count of commitments there |
| **Place, relation** | space is who relates to whom; sliding places costs nothing |
| **Possibility** | a conserved quantity held at places (P units per place), hopping between related places |
| **Matter** | commitment that keeps re-making itself; mass is the upkeep |
| **Pattern** | possibility in transit between commitments: light, and quantum matter between records |
| **Record** | what has been committed. It is kept |

**Added principles:** the vacuum never commits; clocks are matter; no infinities. **Assumed:** three dimensions of space.

## Gravity

| rule | statement | kind |
|---|---|---|
| R1 medium | outflow f = 0.99P below the crossover p_c, f = A + B ln P above it (B = 0.99p_c, A = 0.99p_c(1 − ln p_c)), with p_c = (1/p_s + 1/P∞)⁻¹ | added |
| R2 presence clock | a commitment holds until the summed presence reaches a fixed amount: N = P/P∞ | added |
| R3 field | conservation makes the mean outflow a linear, unscreened field of matter's draw: ⅙Σ_{y∼x} z_y − z_x = s_x − s̄ | derived |
| R4 field dynamics | the clock field is fixed afresh each tick | added |
| R5 what draws | the redshifted Tolman weight, T = (e + 3p)N√γ; the undisturbed vacuum draws nothing, so vacuum energy never enters gravity and Λ is taken from data | added; stress weight borrowed |
| R6 pattern rule | a pattern hops on its place's ticks: light's coordinate speed is N², so γ = 1; massive patterns obey −N⁴∇²ψ + m²N²ψ = ω²ψ | added |
| R7 twist | twist is charged on every closed loop, ticks and relations priced alike (Lorentz invariance by hand) | borrowed |
| R8 motion, inertia | patterns ride the flow; a moving body's field is its boosted rest field; inertia = total energy; only the relations' shear radiates | borrowed and added |
| R9 how space curves ("option 3") | GR's static sector: ds² = −N²dt² + N⁻²γ̃ᵢⱼdxⁱdxʲ, with R̃ᵢⱼ = 2∂ᵢU∂ⱼU − 16πp e^{2U}γ̃ᵢⱼ, N = e^{−U} | borrowed |
| R10 rotation | frame dragging is possibility's circulating flow; spinning holes are Kerr outside | added |
| R11 black holes | GR's holes; infalling matter's commitment relabels it as a record | added |

**ε = 0 in gravity.** The medium's scale ε = p_s/P∞ does not enter the metric. CO's own preferred-time completions give α₂ ≈ −2ε and a two-cone delay of −2ε/(1 + ε). With the pulsar bound and GW170817, these force ε ≲ 8×10⁻¹⁰ and 1.3×10⁻⁷. So gravity outside matter is GR's, and the medium is read as a slicing condition.

## Quantum

| rule | statement | kind |
|---|---|---|
| Q1 | a pattern draws only through its records; the medium holds no branches, so gravity cannot entangle masses | added |
| Q2 | matter and pattern are states, not kinds; deposits land where a record fixes position | added |
| Q3 route (a) | a pattern is recorded when committed matter keeps which-path information | added |
| Q4 route (b) | matter commits at random at rate λ = κ_b mc²/(γħ), localising as L(x) = (πr_C²)^{−3/4} e^{−(q−x)²/2r_C²}; identical units symmetrised GRW-type | added |
| Q5 two places | a commitment of one part updates the whole pattern at once; Bell's correlations are QM's, and nothing signals | added |
| Q6 noncontextual reading | a record's chance is F(⟨ψ\|E\|ψ⟩), the same F for every record; with additivity, Pr(E) = ⟨ψ\|E\|ψ⟩ | added |
| amplitudes with phases; the singlet | the state structure | borrowed |

**Saturation (route (c))**, a capacity primitive, is a candidate, not ruled. A body commits once its density passes ρ_K at the rate c/r_C. That gives a definite onset map at laboratory densities, set by one free number, p_c.

## What CO shows

1. **Weak-field gravity from counting.** Newton's law, the redshift and universal free fall follow from R1–R3 with nothing chosen for them.
2. **Gravity outside matter is GR's,** because ε is forced to zero (see above). Black holes are GR's.
3. **The borrowed spacetime cluster rests on one principle.** R9, R8's boost, inertia and GR's constraint algebra would all follow from path independence for the dynamics (PI-strong), through the Hojman–Kuchař–Teitelboim theorem. CO's hold rule breaks its discrete form: every tested presence-dependent growth rule that can join unrelated places picks a slicing (T-I15b). Ruled: PI-weak. No observable depends on a slicing, but the dynamics uses one.
4. **CO's units cannot grow a spacetime.**
   - With U conserved units, every element lies on the chain of some unit's holders. So the order is covered by U chains, no antichain exceeds U (Dilworth), and large intervals become one-dimensional.
   - A stock that commitment creates gives a shallow bush.
   - Local or regulated draws give threads.
   
   Geometry is an input: the engine's lattice.
5. **Born and commitment.**
   - Q6 is an added principle.
   - If a commitment randomises the relative phase of what it merges, and the weights of alternatives add, then
   $$\mathbb E_\theta F\big(|a+be^{i\theta}|\big)=F(a)+F(b)\ \Rightarrow\ F(x)=kx^2 .$$
     This is elementary, and conditional on the premise of additivity, which carries noncontextuality.
   - The √P measure follows from conserved possibility under mixing hops: a restatement of Lamperti's isometry theorem, published in this form by Lesovik (2014) and Axelsson (2026).
6. **Nothing fixes CO's scales.** Inside the record and out, p_c has been tied to the quantum vacuum, species counts, count-as-volume and CDT cells. Each tie is excluded, inert, or moves the free number elsewhere.

## Inputs

| input | kind |
|---|---|
| R1, R2, R4–R6, R8 (parts), R10, R11, Q1–Q6 | added |
| R7, R8's boost and inertia, R9, GR's constraint algebra, mergers' exterior, complex amplitudes, the singlet, masses and couplings | borrowed |
| three dimensions; the engine's lattice | assumed |
| p_c ≳ 8×10⁴ per place (clocks; conditional on physical clocks not dipping themselves); the engine's own fit gives about 10⁶ | bounded by the engine |
| r_C, κ_b: 0.09 μm ≲ r_C ≲ 51 μm, 5.6×10⁻³⁶ < κ_b ≲ 2×10⁻²⁸ at the cap | bounded by data |
| G, c, ħ, Λ | measured |

## Tried and failed (each in [`archive/`](archive/INDEX.md))
- A vacuum that commits; the flow clock (β = ½); slowing hops by the local clock (the medium froze).
- A nonzero ε in gravity: excluded by α₂ and GW170817.
- CO's own black-hole interior (core at 3m, no horizon): withdrawn with ε = 0.
- Fixing p_c: the Planck-length hop (excluded by clocks), the boost cap (kept only as a candidate), the Standard Model as a species count (excluded), count-as-volume (inert or a restatement), one CDT cell as the hop (p_c ∼ 1, excluded).
- Spacetime from CO's units: a global draw, a local draw, created stocks, regulated creation. All excluded.
- Deriving Q6 from one-way commitment alone: phase-freedom does not fix the power. Phase randomisation does, conditionally.

## Open
- How space curves, from the primitives, without borrowing GR's form.
- What fixes p_c, r_C and κ_b.
- Where three dimensions come from.
- The Hilbert-space form from the logic of records. CO supplies one Boolean algebra per record type, not the lattice that Piron's theorem needs.
- What sources Λ; why the beginning starts to commit.
