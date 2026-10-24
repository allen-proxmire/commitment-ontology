# Commitment Ontology — lattice simulation record

Allen Proxmire.

Tests of the Commitment Ontology against measured physics, on a lattice engine built from its rules: 84 runs (with follow-ups 72b and 81b), 15–24 October 2026.

The project was formerly titled Event Density (ED). "The earlier papers" and the earlier event-layer engine refer to that work. Three documents from it are kept in `runs/`, unchanged except that their paths to the earlier project's files were removed: `P08_substrate_scale.md`, `Paper_BlindnessInvariant_KnotsNotCrystals.md` and `Particles_As_Knots.md`.

**Start here: [`AT_A_GLANCE.md`](AT_A_GLANCE.md)** — what goes in, what comes out, where the ontology parts from GR and how each part could fail, on one page.

## What is being tested
**[`ONTOLOGY.md`](ONTOLOGY.md)** states the ontology as it stands, on one page:
- its primitives (commitment, places, possibility, matter, clocks);
- its rules, each with its formula, the date it was ruled and the runs behind it;
- which results are derived from the rules, which needed a ruling, and which borrow standard physics;
- what it predicts that GR does not;
- what is still open.

Every run in the record tests a consequence of those rules against a measurement.

## How the work is done
- **Each run is pre-registered.** The question, kill rules and analysis are written first, then hashed (SHA-256) with the code before anything is run.
- **Verdicts are reported as registered:** PASS / FAIL / UNDECIDED. Post hoc work is labelled as such.
- **An independent agent re-checks every run,** often with its own code. Its corrections go in the record, even when they overturn a result.
- **Inputs borrowed from standard physics are tracked,** not hidden.
- **Rulings are recorded where they are made,** with what they buy, what they cost, and what would send them back.

## Where things are
- **`writeups/commitment_ontology_simulations.md`** is the full record, and the authoritative version of everything here. It holds:
  - the scorecard;
  - a section per run;
  - §3, what the record says about the ontology, with the rulings;
  - §4, the open questions.
- **`writeups/consilience_summary.md`** is the short version: what is reproduced, how, and what is open.
- **`Where CO's Gravity Stands.md`** is a plain-language summary: passed, failed, open.
- **`Gravity from Counting Commitment.md`** is the explainer.
- **`runs/`** holds each run's write-up section. These are snapshots taken when each run was written; later notes live in the full record.
- **`figures/`** holds one figure per run or group of runs.
- **The latest release** has two zips:
  - every run's code, pre-registration (`PREREG_NN.md`), hash file (`PREREG_NN.sha256`), logs and JSON results;
  - the independent checks.

## Where it stands
- **Reproduced from the rules:**
  - Newtonian gravity;
  - gravitational redshift;
  - universal free fall;
  - rest mass pulling by its local clock rate;
  - no preferred-frame effect from the medium's flow.
- **Reproduced with tracked inputs:**
  - light bending (γ = 1) and Mercury (β = 1);
  - composite-body free fall;
  - binary-pulsar energy loss;
  - clocks of different design agreeing;
  - frame dragging;
  - GR's field outside black holes.
- **CO's static field equation is GR's equation for the clock rate.** CO differed only in how space curves (Run 65).
  - Under the provisional "option 3", space curves as in GR, and CO's stars and static black holes become GR's.
  - Written on the space the medium lives on, this keeps CO's field equation, its clock and its "vacuum draws nothing" rule; stress curves that space (Run 66).
- **Black holes under option 3:**
  - A static hole's clock stops just outside where GR's horizon would be, at a cold surface with no event horizon (Run 67).
  - A collapse emits Hawking's flux only briefly, about 8M ln(P∞/p_s), then nothing (Runs 68, 71).
  - **Rulings (21 October):**
    - CO's holes are stable.
    - Infalling matter commits where the medium's possibility per place falls to about 2p_s. This comes before any matter can turn back: without it, matter with pressure turns back and comes out again (Run 71).
      - Every causal kind of matter reaches 2p_s first: the stiffest turns back at most at 1.27p_s (Run 73).
      - The core then sits at areal radius 3m. By then the Hawking-like burst is over; a cold core gives one flash of about ħ/δu, then silence (Run 74).
    - Around a spinning hole, frame dragging is possibility's own flow, so spinning holes are Kerr outside the horizon (Run 69).
- **Predictions:**
  - **Compact stars slightly break the strong equivalence principle,** Δ = εC/(1 + ε) > 0 with ε = p_s/P∞. GR gives zero. The pulsar triple bounds it, P∞/p_s ≳ 1.6–1.9×10⁵ (Run 66); CO does not yet fix its size.
  - **Under CO's original rule for space only** (withdrawn under option 3): heavy neutron stars need very stiff nuclear matter, near the causal limit above about twice nuclear density. Heavy-ion collisions allow this only at the edge of their bounds (Runs 57–62).
- **Clocks on a curved medium space:** on equal-volume places at both signs of curvature, clocks follow the zero-range theory to about 1–2% (Runs 70, 72).
  - The gap between two clock designs shifts with the sign of the curvature as predicted: detected at 5.1σ, matching the theory to 0.5σ (Run 72b).
  - The theory's apparent underestimate of these clocks' own dips (0.25–0.6%) is mostly its ambient normalisation (Run 78's check; confirmed with registered predictions on the flat lattice, Run 80). An odd cell at negative curvature was not explained by the clocks' outer links (Run 75), its replication was undecided (Run 76), and it stays about 2σ off after the normalisation.
  - The local rule fixed by option 3's planar solution doubles light bending and is excluded (Run 79).
  - A lattice curved by the medium's own stress is buildable in planar symmetry (design note in the record, Note F). On it the engine's medium carries the flux the lattice was built with, to about 0.2% (Run 77).
  - With one global hop rate, such a lattice exists only while the source's draw times the distance to the reservoir stays small. It comes from the lattice representation; CO's rules are not shown to impose it (Run 77).
- **Time's direction:** the engine's bottom is one-way, and averaging over time removes the order at a steady state (Run 29).
  - With a medium that conserves a current, averaging a one-way bottom also gives waves whose one-way share falls as 1/wavelength: two-way at large scales while things change. CO's medium as first built has no current and stays one-way (Run 81).
  - An exactly reversible bottom gives the same large-scale waves, and a wave's damping follows the local collision response whatever the bottom; so the averaged wave hides the arrow, which shows only in the local response (Run 81b). GR's waves are shear, which also needs a restoring force; that is open.
- **Open:**
  - what fixes P∞/p_s;
  - the strong-field binding miss;
  - the medium's own dynamics on a stress-curved space;
  - how long commitment takes, and the core's quantum state (Run 74);
  - the size of CO's hop (the engine suggests about 10^2.5–10^3 Planck lengths);
  - a carrier for gravitational waves built from the relations themselves. Note H, a design note in the record, sets out what it needs and the tests that would kill it. Its speed test (Run 82): the waves need a second factor of N beyond the place ticks, as light has, or they arrive with half light's Shapiro delay, which GW170817 excludes. Its mode count (Run 83): on a triangulated lattice the relations carry exactly GR's two polarisations at light's speed, but the kinetic form tried leaves a short-wavelength instability for λ > 1. Its kinetic form (Run 84): with the DeWitt form of the metric read from the relations arriving at a place, GR's route carries exactly the two polarisations, with ω² = Σ4sin²(k_a/2) at every wavelength, and the khronometric route is healthy exactly when the continuum's is (α < 2ξ). That is linear, around flat space; whether it survives at second order is the next question.

## Running it
- **Requirements:** Python 3 with numpy, scipy and matplotlib.
- **Running a run:** in its folder, `python3 runNN.py`, then `python3 analyseNN.py`. Some runs use an `engineNN.py` with a job list.
- **Absolute paths.** The scripts use the absolute paths they ran with (`/home/claude/...`). Either unzip the code so the run folders sit side by side and point `/home/claude` at that folder, or edit the paths.
- **The event-layer engines** import the earlier project's event-layer models. A copy is included in the code zip under `external/`.
- **Checking a registration.** Each `PREREG_NN.sha256` lists the files' hashes with the paths they had when hashed, and the time of hashing. Compare the hashes with `sha256sum` on the files; `sha256sum -c` will not find the old paths.

## Status
Not peer reviewed. The engine is a model built from the ontology's rules, not CO's full theory.
