## Q1: quantum structure from commitment (draft)

*31 October 2026. Brings together three routes found in Allen's repos: ED's P11 and P09 (phase-randomising commitment), ED Attempt 02's `Gleason_For_ED.md` (conserved hops), and event-density's Gleason/Solèr audits (record logic). Checks: `q1_checks.py`, `p7_phase.py`. Every step uses known mathematics. What would belong to CO is that its own primitives supply the premises.*

**The claim.** Take three properties CO already has, and keep one borrowed input:
- **(H) Hops.** Possibility is conserved and moves by linear maps on amplitudes that mix places, so interference happens.
- **(C) Commitment.** A commitment is one-way and destroys the relative phase of the contributions it merges.
- **(R) Records.** A record is kept (it never reverts) and repeatable (reading it again gives the same outcome).
- **Borrowed:** amplitudes with phases that evolve linearly (superposition).

From these, step (a) gives the measure of possibility, step (b) the Born weight, and step (c), still open, the Hilbert-space form.

### (a) Possibility is |amplitude|² (from H) — derived
- **Setting.** Let possibility at a place be P_i = F(|a_i|), with total Σ_i P_i conserved under every hop map M, where M is linear, invertible and not a phase-permutation.
- **The theorem** (Aaronson 2004, "Is quantum mechanics an island in theoryspace?"): for p ≠ 2, the only linear maps preserving Σ|a_i|^p for all states are generalised permutations. So hops that mix places conserve possibility only if
$$
P_i=|a_i|^2 .
$$
- **Check** (`q1_checks.py`): a Haar-random hop preserves Σ|a|² to 1×10⁻¹⁵, and changes Σ|a|^p by 20–160% for p ∈ {1, 1.5, 3, 4}. A phase-permutation preserves every p-norm, which is the theorem's one exception.
- **In CO:** A5's "amplitudes √P" stops being a definition. It is forced by conserved possibility moving with interference.

### (b) The Born weight is |amplitude|² (from C) — derived (P7)
Take an outcome weight F(|ψ|) with F(0) = 0, F smooth. Require additivity over contributions whose relative phase the commitment randomised:
$$
\mathbb E_\theta\,F\big(|a+b\,e^{i\theta}|\big)=F(a)+F(b)\ \ \forall a,b\ \Longrightarrow\ \frac{d}{dx}\big(xG'(x)\big)=G'(0),\ F(x)=G(x^2)\ \Longrightarrow\ F(x)=kx^2 .
$$
- **Random signs suffice.** With phases only ±1 (real amplitudes), the same expansion gives G′ + 2xG″ = G′(0), again only G linear. So (b) does not choose complex numbers over real ones.
- **Check** (`p7_phase.py`): exact at p = 2; violations of 0.2–2.0 at the other powers.
- **In CO:** Q6 is replaced by (C) plus the ordinary additivity of probabilities for alternatives.

**(a) and (b) are independent.** (a) fixes what is conserved; (b) fixes what an outcome weighs. They agree, P = |a|² and weight = |a|². So the record's weight equals the possibility committed: the counting step and the conservation law coincide.

### (c) The Hilbert-space form (from R) — open, with a precise list
Piron's and Solèr's theorems (Piron 1964; Solèr 1995) give a Hilbert space over ℝ, ℂ or ℍ if the propositions form a complete, orthomodular, atomic lattice with the covering law, plus an infinite orthonormal sequence.

| axiom | CO supplies it? |
|---|---|
| propositions = "a kept record shows an outcome in S" | yes (R) |
| orthocomplement (S against not-S within one record type) | yes: a record shows one outcome |
| propositions stable under re-reading (P² = P, ideal filters) | yes: kept and repeatable (R) |
| orthomodularity across record types | **not shown.** CO defines no meet or join between incompatible records |
| atomicity and the covering law (minimal disturbance, Lüders) | **not shown.** It needs a new statement: a record disturbs only what it records |
| Solèr's infinite orthonormal sequence | **not shown** (it needs unbounded refinement of records) |
| the field ℂ (not ℝ or ℍ) | **not from (b).** It needs a composition axiom, for example local tomography (Masanes–Müller), which is borrowed |

### What Q1 would change in CO's inputs

| input now | after Q1 |
|---|---|
| A5: amplitudes √P with phases (borrowed) | √P derived from (H); linear amplitudes with phases still borrowed |
| Q6: noncontextual additivity (added principle) | replaced by (C), a property of commitment |
| the Hilbert-space form (borrowed) | still borrowed; (c) lists what CO would need to derive it |

**Grade.** (a) and (b) are derived, each from known theorems (Aaronson; P7's elementary uniqueness), with CO's primitives as premises. (c) is open. No new number comes out.

### Correction after the independent check (31 October; `/home/claude/checkQ1/REPORT.md`, adopted)
- **(a) is a restatement.**
  - **The right source.** Aaronson proves only the real case and omits the proof for complex Σ|a|^p. The correct source is the Banach–Lamperti isometry theorem (Lamperti 1958, complex finite form).
  - **A step for general F** (a compact-group argument, the check's E2): a mixing map gives a U(2) block, so F(|a_i|) + F(|a_j|) depends only on |a_i|² + |a_j|², which forces F = kx².
  - **The route is published:** Lesovik, arXiv:1411.6992 (2014), and Axelsson, J. Mod. Phys. 17, 1282 (2026), "Born's Rule from Reversible Evolution and Record Formation", the second in record language.
  - **What still comes in from outside:** the conserved quantity's form Σ_places F(|a|) is a premise, not derived.
- **(b) is derived, but only conditional on new statements, and with two proof repairs.**
  - **Repair 1:** the hypothesis should be F ∈ C²(0, ∞) and continuous at 0, and the evenness of G(b²) in b closes the step that used G′(0).
  - **Repair 2:** in the real (±1) case, F = x solves the local equation, and only the O(b) term or the full equation excludes it: (|a+b| + |a−b|)/2 = max(a, b).
  - **The conditions:**
    - **(A)** is a new statement. It carries noncontextuality: one F of one modulus for every record, whether a part stands alone or is merged.
    - **(C)** needs commitment to randomise a c-number phase literally. Justifying (C) by "decoherence equals random phases" would be circular.
  - **Closest literature:** Saunders 2004 and Zurek 2005. No source was found in exactly this form, but it is plausibly folklore, so no claim of novelty is made.
- **(c), corrected statement.**
  - Piron also needs irreducibility and height ≥ 4, and gives a space over a division ring. Solèr's sequence then pins ℝ, ℂ or ℍ.
  - CO supplies only Boolean blocks, one per record type: a partial Boolean algebra, not a lattice.
- **Q6 and A5's √P are moved, not removed:**
  - A5's √P now rests on the conservation premise.
  - Q6 splits into three parts: a borrowed weight that depends only on the modulus, the new statement (A), and (C).
  - Still borrowed: linear complex amplitudes, the field ℂ, the Hilbert-space form, and general effects.

**Revised grade:**
- (a) restatement;
- (b) derived, conditional on the new statements (A) and (C);
- (c) open.

Q1 organises known results in CO's terms; it is not a derivation from CO alone.
