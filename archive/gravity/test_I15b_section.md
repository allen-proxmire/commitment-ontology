### T-I15b: discrete general covariance for presence-dependent growth rules (a registered calculation, gravity sector)

*31 October 2026.*
- *Registered and hashed before the run (`testI15b/PREREG_I15b.md`, 02:19:53 UTC), after one independent pre-check (`checkPreI15b/`), whose corrections were adopted.*
- *The pre-check showed that the first design could not fail. W5 and W6, the rules that decide the verdict, were added on its advice and had no pre-check of their own.*
- *One post-run check (`checkI15b/`) found no errors. The hashes verify, the log postdates the stamp, all 45 completed lines reproduce exactly, and an independent reimplementation reproduces W5 and W6.*

**Why.** Reading I22: the borrowed spacetime cluster rests on one missing principle, PI-strong. Its discrete form is discrete general covariance (DGC): every natural relabelling of a growth history has the same probability. The question is whether a growth rule in which presence matters can satisfy DGC exactly.

**Rules.** An initial antichain of M elements holds H units each. A birth takes H units, its parents are their holders, and the units move to it.

| rule | role | result |
|---|---|---|
| C7: H units uniform from all units | control, must pass | passes, 7/7 cases |
| W1: units drawn sequentially, weighted by holdings | control, must fail | fails, 6/7 (trivial pass at H = 1) |
| W2, W3: draws from the units of elements comparable to one holder | controls, must pass | pass, 7/7. Inert: every component stays a chain and every draw is forced (pre-check) |
| W4: deterministic threshold timing | reported | fails by construction |
| **W5:** two seeds i, j weighted by holdings; S uniform from units of elements comparable to i or to j | **verdict** | **fails, 6/7**; at (2,2,3), 8 of 92 relabellings, worst gap 7/16 |
| **W6:** Erlang-2 clocks (R2's timing, randomised) with W5's pool | **verdict** | **fails, 3/3 computed** |

**Result: ALL FAIL in the tested forms.**

**Why W5 fails** (the post-run check's worked pair). At (2,2,3), take the same order reached in two birth orders:
$$
p(R)=\tfrac13\cdot\tfrac{3}{16}\cdot\tfrac{7}{48}=\tfrac{7}{768},\qquad p(R')=\tfrac13\cdot\tfrac{7}{48}\cdot\tfrac13=\tfrac{7}{432},
$$
against 1/54 for both under C7. The seed normalisation Σh is constant, but the subset normalisation 1/C(|pool|, H) is not. The pool's size depends on which units have already moved to elements spacelike to the seed. So a birth's factor depends on the order of spacelike births, which is a slicing (a reading, at small sizes).

**Disclosed.**
- The run was stopped by a 30-minute background cap, which is not in the registration, during W6 at (3,2,4).
- Four W6 cases and the JSON output were not produced.
- The reading was applied by hand from the log under the registered rule. A pass needs zero violations in every case, so one failing case suffices, and the stop does not change the reading.

**What it means.**
- **In the tested forms, R2's presence-dependence picks a slicing.** PI-strong would need R2 amended (a new statement).
- **C7 is the only pass that is not inert.** Its subset normalisation, set by all units, never changes.
- **A candidate condition for a rule that passes** (inference): each birth's factor must be unchanged when spacelike births are reordered. That needs a normalisation that is global or conserved, or presence entering only through quantities that spacelike births leave alone.
- **The literature's DGC class** is Rideout–Sorkin sequential growth, defined on the order alone. Whether any unit-carrying rule beyond C7 passes is open.
- **Limits:** small sizes only; equal initial holdings; k = 2 only; nothing about manifoldlikeness (Reading I14).
