# Mining: event-density-ontology-models and cdt-3p1-sampler-note, for CO

## 1. What each repo does and finds

**event-density-ontology-models.** Rule-based lattice models (32³ grids, boxes 15–30) on a *supplied* 3D neighbour relation, with no metric, inertia or field equation. Its findings, once the overclaiming is stripped out:
- **Clock well / Newtonian shortage** (`results/EVENT_LAYER.md` R24–25). This is a conserved quantity diffusing around a sink: the lattice Poisson solution, as the repo itself concedes. CO already has it as R3 (derived). Nothing falls, and the steering rule that makes loops gather is added. There is also a reach-against-strength trade, ℓ_scr = √(D·ρ/(χ·R)), so a single medium cannot be both strong near a mass and long-ranged.
- **Age relic** (R22). If time is defined as a count, a head start cannot be repaid. That is true by definition, so it is not an output.
- **Clock floor (no d ≤ 2), knots (d = 3), handedness** (`results/RESULTS.md` 2, 3, 5). These are Strogatz–Mirollo / Hong et al., standard knot theory and roughly Nielsen–Ninomiya, restated. The d = 3 cap depends on "particle = uncuttable loop".
- **Space cannot be grown** (`MODEL_RESULTS.md` R16, R18, R19). Nine growth models and four neighbour rules gave strands, small worlds or a glass (d_growth ≈ 2.3 while the walk is trapped below d = 1). Once the permitted pairs come from 3D positions, *random* link selection does exactly as well as ED's rules (d ≈ 3.0–3.2). So geometry is always the input. This matches CO's P4 independently: every unit-based law fails.
- **The "CDT constraint"** (`results/CDT_Constraint.md`). Holding N0, N41 and N32 fixed as "budgets" is a microcanonical choice, not a derivation:
  - N32/N41 = 1 is just the staircase product triangulation of a slab (a crystal).
  - N0/N4 = 0.044 depends on ED's chosen vertex density.
  - In 3+1 it misses phase C (≥ 0.073), in the direction of crumpled phase B.
  - In 2+1, τ = 1/3 lands in the extended phase. That is weak: the extended phase covers τ ≈ 0.2–0.47.
  - Verdict: negative, and the dictionary is invented.

**cdt-3p1-sampler-note.** A real, modest methods note on the public tryggth/CDT 3+1 Lisp code:
- The code accepts moves on exp(−ΔS) with no Metropolis–Hastings proposal ratio, which roughly equals simplices created ÷ destroyed (H₂₈ = 4, H₄₆ = 3/2, H₂₄ = 2).
- As shipped, the code gives N32/N41 = 0.87 instead of 1.25.
- Reading the missing ratio as a coupling shift (κ₀ + ln 2, Δ + ½ ln ¾, κ₄ + ½ ln(8/3)) accounts for about 75% of the effect. That missed 2 of 3 tolerances fixed in advance, so it is a "first approximation".
- With `code/mh_fix.lisp` and `sampler_patched.lisp`, the sampler reproduces N32/N41 ≈ 1.25 and N0/N4 ≈ 0.079 at (2.2, 0.6).
- **It adds nothing about 3+1 emergence.** No spectral or Hausdorff dimension, volume profile or de Sitter fit is measured anywhere in either repo (checked by grep). Its asset is a validated 3+1 CDT instrument, checked at 8k–16k simplices only.

## 2. What could give CO a genuine output

Almost nothing in these repos does. Every ED "output" either restates known mathematics or follows from a rule written to produce it. The real content worth carrying over:
- (a) Two independent programmes (ED R16–19 and CO P2–P5) agree that geometry from finite, local, unit- or order-based growth fails. That points to the obstruction being generic, not CO-specific.
- (b) A working CDT sampler.

## 3. CDT ingredients as CO primitives

**What CDT's 3+1 emergence actually is.** In phase C the *macroscopic* geometry is extended and four-dimensional:
- Hausdorff dimension ≈ 4, spectral dimension running from about 4 at large scales to about 2 at short ones;
- the slice-volume profile V₃(t) ∝ cos³(t/B), matching minisuperspace de Sitter.

The "4" is put in by the 4-simplices. What emerges is that the input dimension *survives* rather than crumpling (d → ∞, phase B) or going branched-polymer (d ≈ 2, phase A). It also needs tuned couplings (κ₀, Δ) and Wick rotation. This is ED R19's lesson, nonperturbatively.

**Mapping CO onto it.** PI-weak does license CDT's proper-time foliation. But "commitments are the time-slices" clashes with CO as it stands:
1. **A CO commitment is local** (one place's tick), and gravity is a clock-rate gradient across places. In CDT every slab has lapse 1 globally, so a CO clock gradient would have to be read off simplex structure, not imposed. The workable mapping is commitment = a local simplex or vertex event inside a slab. A slab is then one global "round".
2. **Conserved possibility kills CDT's output.** If units are spatial tetrahedra per slice, conservation fixes N3(t), and the de Sitter profile *is* the fluctuation of N3(t). P4's creation law A″ corresponds to CDT's (2,8)/(4,6) moves, whose rates the Regge action sets, not CO. ED's CDT test tried exactly "conservation fixes counts" and landed outside phase C.
3. **So a CO-on-CDT is CDT plus vocabulary unless CO fixes something CDT tunes.** It would not move "where three dimensions come from" off the inputs list. The input becomes the simplex dimension plus phase-C couplings. CO already borrows Regge's energy on a triangulated carrier (Runs 83–91), so CDT is its natural nonperturbative completion. That is an honest restructure of borrowed inputs (replacing the cubic lattice, "3D assumed" and possibly R9), not a derivation.

## Ranked ideas

1. **Scale check (cheapest, could fail).** CDT fits of volume fluctuations to minisuperspace fix the lattice spacing in Planck units, a ≈ 2 ℓ_P (Ambjørn–Görlich–Jurkiewicz–Loll, PRL 100, 091304, 2008; quoted from memory, so verify). If CO's hop is the CDT cell, then ℓ_hop ≈ 2 ℓ_P, and the engine-hop relation gives
   $$p_c=\frac{\ell^2}{k\,a\,\ell_P^2}\approx\frac{4}{k\,a}\sim 1,$$
   against the clock floor p_c ≳ 8×10⁴, the engine's 10^2.5–10³ ℓ_P, and P6's route-(b) window of 1.7×10⁹–5.6×10¹¹ ℓ_P. On this reading CDT-as-substrate fails. Rescuing it needs a coarse-graining factor of 10^2.5 or more, which is a free number. This is one line of arithmetic.
2. **CDT as CO's geometry layer (borrowed, not derived).** Commitments become local events in a PI-weak foliation, possibility conservation is dropped, and the Regge path sum replaces R9 and the lattice. It gains a Lorentzian, extended, dynamical geometry, which CO's growth laws never gave. It produces no new number. Report it as an exchange of inputs.
3. **CO-native observable on CDT configurations.** Define a local "commitment count" per spatial vertex per slab, n_v(t) = #(4,1)+(3,2) simplices at v. With the validated sampler, test in phase C whether n_v carries a long-range correlated field that behaves like a lapse, i.e. a CO clock field that nobody put in. Expect short-range coordination noise (restatement). Register the kill rule first.
4. **ED's microcanonical point, clock well, age relic, knot and clock-floor bounds.** Nothing for CO. They are negative or restatements.

## Recommended next steps
- Do the idea-1 arithmetic (with the AGJL value checked) before anything else. If p_c ~ 1 stands, close the "commitments as CDT cells" route in a reading.
- If idea 2 is pursued, frame it from the start as replacing borrowed inputs, and record "dimension = simplex dimension, input".
- Only if 1 survives: register idea 3 using `cdt-3p1-sampler-note/code/mh_fix.lisp` + `sampler_patched.lisp`, never the unmodified tryggth code.
