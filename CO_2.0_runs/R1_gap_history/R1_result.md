# R1: the gap's history under the wave rule

Closed-form bookkeeping, not a lattice run. Script: [`r1_gap_history.py`](r1_gap_history.py); numbers in `r1_result.json`; curves in `r1_H_of_a.png`.

**Registered before running.** Under the wave rule as written, with the free stock conserved, dilution opens the gap as N grows (x = P∞/P_max ∝ a⁻³) while a crest's displacement per place scales with the floor (∝ s·x). The tip condition ξ > (1 − x)/(s x) then runs away, and H should fall as a steep power of a. If so, the rule as written is excluded as today's expansion.

**Setup.** Possibility in units of ħ. Crest per place c = s(a)·x·P_max·ξ, with Pr(ξ > y) = y⁻³ (uniform-in-volume sources). H = ν·Pr(ξ > (1 − x)/(s x)). Strain history s(a): primordial ∝ 1/a plus a structure-made part following the cosmic star-formation history (Madau & Dickinson form). Amplitudes are hand-chosen; only shapes are claimed.

**Result.**

| case | floor | outcome |
|---|---|---|
| A: rule as written | x = x₀ (a₀/a)³ | H falls as roughly a⁻⁹ times the strain history (late slope d ln H / d ln a ≈ −17 in the run). H today / ν ≈ 10⁻⁷². Expansion stops once the gap opens. **Excluded** as today's expansion |
| C: pinned floor | x = x₀ | H = ν·Pr(ξ > (1 − x₀)/s(a)) ∝ s(a)³. The expansion history is the cube of the wave-background amplitude history. Shape in the run is input-dominated and does not match ΛCDM's flat late H with an instantaneous merger-rate strain; a cumulative background rises toward today and would give rising H. Neither matched nor excluded here |

**Reading.** The wave rule survives only if the floor does not fall as places are born: a newborn place must be born *at the floor*, with its free content drawn from somewhere other than the free stock. The one source that is not free is the record. So the rescue is a rule change: *a place is born of record*; the crest tips it, the record fills it. That is the earlier "record becomes relation" idea with the right sign (places, not shortcuts).

Under the rescue, 2.0 makes a sharp claim: H(a) ∝ A(a)³, with A the characteristic wave amplitude per place at epoch a (for a 1/distance source population; the power is the tail index). That is a test against real inputs (primordial tensor bound, the merger background's history), not a fit.

**Post-run check.** The late slope was read from a ≥ 0.5 in Case A; the a⁻⁹ comes from x³ with x ∝ a⁻³, and the remaining steepness from the strain history. Case C's curve changes with its amplitudes, as stated; its H ∝ s³ relation does not.
