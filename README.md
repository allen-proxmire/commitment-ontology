# Commitment Ontology — lattice simulation record

Allen Proxmire.

Tests of the commitment ontology against measured physics, on a lattice engine built from its rules. 

60 runs, 15–20 October 2026.

## How the work is done
- Each run is **pre-registered**: question, kill rules and analysis written first, then
  hashed (SHA-256) with the code before anything is run. Verdicts are reported as
  registered: PASS / FAIL / UNDECIDED. Post hoc work is labelled as such.
- An **independent agent** re-checks every run, often with its own code; its corrections go in the record.
- Inputs borrowed from standard physics are **tracked**, not hidden.

## Where things are
- `writeups/commitment_ontology_simulations.md` — the full record: scorecard, a section per run,
  §10 (what it says about the ontology, and Allen's rulings), §11 (open questions).
- `writeups/consilience_summary.md` — the short version: what is reproduced, how, what is open.
- `figures/` — one figure per run or group of runs.
- `runs/` — one file per run (e.g. `firstlaw/`, `vardraw/`, `medium55/`, `eos57/`, `nuc60/`): `PREREG_NN.md`,
  `PREREG_NN.sha256`, `runNN.py`, `analyseNN.py`, logs and JSON results.
- `check*/` — the independent checks.

## Where it stands
- **Reproduced from the rules:** Newtonian gravity, gravitational redshift, universal free fall,
  rest mass pulling by its local clock rate, no preferred-frame effect from the medium's flow.
- **Reproduced with tracked inputs:** light bending (γ = 1), Mercury (β = 1), composite-body
  free fall, binary-pulsar energy loss, clocks of different design agreeing, frame dragging,
  and GR's field outside black holes (with ED's core inside).
- **Predictions:**
  - Compact stars slightly break the strong equivalence principle: Δ ≈ C·p_s/P₀ > 0.
    GR gives zero. The pulsar triple bounds it (P₀/p_s ≳ 2×10⁵); ED does not yet fix its size.
  - Heavy neutron stars need very stiff nuclear matter. ED holds about 75–80% of GR's
    maximum mass, so 2 M☉ pulsars need the sound speed near the causal limit above about
    2× nuclear density. That still passes nuclear theory and QCD.
- **Open:** the strong-field binding miss; what fixes P₀/p_s; the size of ED's hop
  (the engine suggests about 10³ Planck lengths).

## Running it
Python 3 with numpy, scipy and matplotlib. In a run folder: `python3 runNN.py`, then `python3 analyseNN.py`.
Check the registration first with `sha256sum -c PREREG_NN.sha256`.

## Status
Not peer reviewed. The engine is a model built from the ontology's rules, not the full theory.
