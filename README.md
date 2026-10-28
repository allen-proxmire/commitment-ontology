# Commitment Ontology

The world is made of **commitments**: irreversible updates at places. Time at a place is the count of its commitments, so time runs one way at the bottom. Between commitments, places hold **possibility**, a conserved stuff that hops between related places; the vacuum never commits. **Matter** is commitment that keeps re-making itself, and on average its renewals draw on the possibility around it. **Clocks are matter**, so clocks near matter run slow, and that clock-rate gradient is gravity. Light and quantum objects are **patterns** of possibility between commitments; they commit only when something records them, or, for matter, at a slow random rate of their own. The project tests how much of known physics follows from this, on a lattice engine built from the rules and in calculations, against measurement.

## In and out

| goes in | kind |
|---|---|
| commitments, places and relations, possibility, matter, patterns, the record | the primitives |
| the vacuum never commits; clocks are matter; no infinities; three dimensions of space | added principles; dimension assumed |
| the medium's outflow, the presence clock, the clock field fixed each tick, matter's draw, the pattern rule, relations that shear, which field's stress curves space, frame dragging as possibility's flow, matter committing at the core | added rules, chosen in forms the runs required |
| how space curves (GR's form, "option 3"); a moving body's field is its boosted rest field; twist priced alike on ticks and relations (Lorentz invariance by hand); inertia = total energy; GR's exterior for merging black holes; particle masses, charges and nuclear equations of state | borrowed |
| quantum sector: patterns draw only through records; the line between matter and pattern; route (b)'s worldline rate; GRW-type symmetrisation; the two-place rule | added rules |
| quantum sector: the Born rule; the singlet state | borrowed; input |
| the engine: a cubic lattice, one global hop rate; for waves, a constructed triangulated carrier | engine choices |
| p_s, P∞ (P∞/p_s ≳ 1.6×10⁵ from the pulsar triple; p_s ≳ 4×10⁵ conditional since Reading I6), the hop, r_C and κ_b, G, c, ħ, Λ | set or bounded by data |

| comes out | how |
|---|---|
| Newton's 1/r² (beyond r_C for solids), redshift, patterns' universal free fall, the Tolman pull, no preferred frame from the flow, one-way time | from the rules alone |
| light bending and Shapiro delay (γ = 1), Mercury (β = 1), binary-pulsar energy loss (0.98 of GR) | from rules chosen to give them |
| composite bodies falling alike, frame dragging, neutron stars, static black holes as GR's; spinning holes as Kerr (with frame dragging as possibility's flow, added) | from the borrowed inputs |

The full list, with what each input buys and its history, is in [`record/ONTOLOGY_full.md`](record/ONTOLOGY_full.md); the short form is in [`ONTOLOGY.md`](ONTOLOGY.md).

## Results

- **Gravity's weak field** follows from counting commitments: Newton's law, unscreened and linear, the redshift, and patterns falling at the same rate for every mass.
- **The post-Newtonian tests pass** (γ = β = 1, binary-pulsar radiation), but by rules chosen for them, not derived.
- **Waves on the relations:** on a constructed triangulated lattice, the relations carry exactly GR's two polarisations at light's speed (with a second factor of N in their ticking). GR's constraint algebra closes through field order 2 at order a², and that closure forces the waves to stay relativistic. It is one formal closure, imposed, not derived.
- **Black holes:** no singularity, no event horizon, no evaporation. Infalling matter commits at areal radius 3m (this rests on option 3 and a chosen threshold).
- **A prediction, untested:** compact stars break the strong equivalence principle slightly, Δ = εC/(1 + ε) > 0, where GR gives zero. It rests on inertia = total energy (borrowed) and a recorded choice of which field curves space; its size waits on ε = p_s/P∞, which pulsar timing bounds.
- **The quantum vacuum's energy does not pull** (a rule: energy is measured from the undisturbed vacuum), so the old cosmological-constant problem does not arise. Λ itself is taken from data.
- **The quantum sector:** a solid's gravity is laid down only by matter's own slow commitments. That leaves a window for the collapse length, **0.09 μm ≲ r_C ≲ 51 μm**. The rate lies above LISA Pathfinder's gravity-noise floor (with an assumed housing) and below SNO's deuteron break-up (r_C < 0.92 μm) or intergalactic-gas heating (above). It rests on GRW-type symmetrisation, an added choice: without it the window closes. The window is a registration, not a test that could have failed. Gravity cannot entangle masses.

Every result, with its status and the runs behind it: [`RESULTS.md`](RESULTS.md).

![Binary radiation by counting](figures/11b_shear.png)
*Run 11b: if relations are all there is, an orbiting pair radiates 0.98 of GR's power, through the two shear polarisations only.*

## What would break it

- A short-range gravity test that sees no smearing of solids' gravity down to 0.09 μm, or a LISA-type test mass about 3.5×10³ quieter. Either closes the quantum window.
- Gravitationally mediated entanglement between masses.
- Black-hole echoes, or evaporation.
- A strong-equivalence violation in compact stars with the opposite sign (Δ < 0).

## Open targets

These would move the ontology from reproducing physics to deriving it:
- **How space curves,** from the primitives, replacing the borrowed option 3.
- **What sets r_C and the commitment rate,** ideally one scale doing both jobs.
- **Commitment set by internal complexity** rather than mass alone.
- **The Born rule** from counting commitments.
- **ε = p_s/P∞,** which sets every strong-field departure from GR.
- **The low-entropy beginning:** a fully in-step start as the only state with zero becoming.

## Map

| folder | what it holds |
|---|---|
| [`ONTOLOGY.md`](ONTOLOGY.md) | the primitives and rules, with formulas |
| [`RESULTS.md`](RESULTS.md) | every result: claim, status, runs |
| [`gravity/`](gravity/) | write-ups of Runs 11b–91 and the gravity design notes |
| [`quantum/`](quantum/) | the quantum sector: readings I0–I6, Runs 92–96, design note I |
| [`record/`](record/) | the full record, the run index, the rulings in order, and every earlier document (unchanged apart from link paths in four files) |
| [`figures/`](figures/) | one figure per run or group of runs |

## Method

Runs 1–13 were mostly exploratory. From Run 14 most runs were pre-registered with kill rules and the analysis; from about Run 22 the registrations were hashed (SHA-256) with the code before running; from about Run 29 most runs were re-checked by an independent agent with its own code. Verdicts are reported as registered, and failures stay in the record. Code, registrations and checks are in the releases. How to run the code: [`record/README_old.md`](record/README_old.md#running-it).

Not peer reviewed. The engine is a model built from the rules, not the whole ontology.
