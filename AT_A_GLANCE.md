# The commitment ontology at a glance

What goes in, what comes out, and where it parts from general relativity, on one page. Every line points to the runs behind it. The rules in full are in [`ONTOLOGY.md`](ONTOLOGY.md), and the evidence is in the record (`writeups/commitment_ontology_simulations.md`).

## The idea

The world is made of **commitments**: irreversible updates at places, never undone. Time at a place is the count of its commitments, so time runs one way at the bottom. Between commitments, places hold **possibility**, a conserved stuff that hops between related places. **Matter** is commitment that keeps renewing itself, drawing on the possibility around it. **Clocks are matter**, and they tick in proportion to the possibility present, so clocks near matter run slow. That clock-rate gradient is gravity. Light and quantum matter are patterns of possibility that hop on their places' ticks, so they fall and bend in the same field.

## What goes in

**The ontology's own rules,** in the forms chosen for the engine:
- commitments are never undone, and the vacuum never commits (15 October; Run 14);
- possibility's outflow is f(P) = c ln(1 + P/p_s), linear below a crossover p_s and comparing ratios above it (18 October; chosen so that β = 1; Runs 21–26);
- the presence clock: a commitment holds until a fixed amount of possibility has been present at its places (18 October; Runs 22–24);
- matter draws possibility, by the variational draw (20 October; Runs 52–55);
- the pattern rule: a pattern hops on its place's ticks and needs free capacity there (17 October; Runs 9, 17, 46);
- twist is charged on every closed loop, ticks included, and relations shear (Runs 11b, 12–13, 18).

**Taken from GR or standard physics, and tracked as such:**
- **option 3:** how the medium's space curves, which is GR's equation for space written in the ontology's terms (21 October, provisional; Runs 65–67);
- **the Lorentz input:** a moving body's field is its boosted rest field (19 October; Run 34);
- **inertia = total energy** for compact bodies (20 October; Runs 52, 55);
- **option A:** GR's exterior for merging black holes (19–20 October).

**Choices where the rules are silent:**
- infalling matter commits where possibility falls to about 2p_s per place (Runs 71, 73–74);
- frame dragging is possibility's own flow (Run 69);
- black holes are stable (Run 68).

**Scales set by data, not by the ontology:** p_s ≳ 4×10⁵ units per place, and P∞/p_s ≳ 1.6–1.9×10⁵, the second from the pulsar triple PSR J0337+1715 (Runs 24, 66).

## What comes out

**From the rules alone, in the engine:**
- Newton's law: 1/r², linear in the source, unscreened (Runs 1, 14);
- gravitational redshift (Run 22);
- universal free fall (Runs 16, 27);
- rest mass in a well pulls by its clock rate, as in Tolman (Run 30);
- no preferred-frame effect from possibility's flow: α₂ = ζ₁ = ξ = 0 (Run 34);
- one-way time, with time-averaged clock records losing most of the order (Runs 29, 35, 37).

**From rules chosen to give them:**
- light bending and Shapiro delay, γ = 1 (the pattern rule; Runs 9, 17);
- Mercury's perihelion and β = 1 (the medium and clock; Runs 22–26);
- binary-pulsar energy loss, at 0.98 of GR (relations shear; Run 11b).

**From the inputs taken from GR:** frame dragging and α₁, α₃ (Run 34); neutron stars and static and spinning black holes as GR's (Runs 65–69); merging black holes.

## Where it parts from GR, and how each could fail

1. **Black holes never evaporate** (Run 68). A detected evaporating primordial black hole would count against the ontology.
2. **A hole has no singularity and no event horizon** (Runs 67, 73–74):
   - its clock stops where GR's lapse would be about ε = p_s/P∞, just outside GR's horizon, behind a throat;
   - infalling matter commits first, at areal radius 3m.
   - This rests on option 3 and on the 2p_s choice.
3. **Compact bodies slightly break the strong equivalence principle** (Runs 55, 66): Δ = εC/(1 + ε) > 0, where GR gives zero, growing with compactness. Its size waits on ε, which pulsar timing bounds.
4. **β − 1 = −ε/[2(1 + ε)]** (Run 66), below current reach at the bound on ε.
5. **The vacuum's energy does not pull,** because the vacuum never commits. Its size has not been computed.

The sizes in items 2–4 all depend on ε, which the ontology does not yet fix.

## What was tried and failed (all kept in the record)

- a vacuum that commits (dropped after Run 14);
- the flow clock, which gave β = ½ (Runs 15–20; replaced);
- slowing possibility's own hops by the local clock, which froze the medium (Run 17);
- the ontology's original rule for space. Its strong field rang about 4% below Kerr, a 5σ tension with GW250114 (Run 28). Every rotating exterior failed GW250114 (Run 41). Heavy neutron stars needed matter at the edge of what heavy-ion collisions allow (Runs 57–62). Option 3 replaced it.
- the local rule fixed by option 3's planar solution, which doubled light bending (Run 79; excluded).

## The open problem that matters most

**Deriving option 3 from the ontology:** a rule, from its own primitives, by which the medium's space curves. With it, the strong field and the black-hole differences above would move from "taken from GR" to "derived". Two readings are being tested: (A) relations dissolve and re-form, and (B) relations stay fixed and the medium's state across them carries the curve (Note G and Run 79 in the record).

## How it is tested

- **Before each run** (most runs from Run 14 on), the question, the kill rules and the analysis are written down and hashed (SHA-256) with the code.
- **Verdicts are reported as registered:** PASS, FAIL or UNDECIDED.
- **An independent agent re-checks each run,** with its own code, and its corrections go into the record.
- **Failures and withdrawn rules stay in the record.**

Code, registrations and checks are in the latest release's two zips.
