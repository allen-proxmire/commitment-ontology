**Q1 check: one pass on (a), (b) and (c)**

**Verdict.** None of the mathematics in Q1 is new.
- (a) is a known theorem with a known route to the Born power. The same route was published in 2014 and again in 2026, the second time in record-formation language.
- (b) is a correct, elementary uniqueness result once a short gap in the proof is fixed. This pass found no published source for it in exactly this form. Its premise (A) does not assume Born outright, but it does carry a noncontextuality assumption.

CO's own contribution is a reading of these results in its terms: conserved possibility under mixing hops gives the power 2, and commitment that randomises phase with additive weights gives the Born weight. That is a way of organising known results, not a derivation from CO alone. Q6 is not removed. It is split into a modulus-only weight (borrowed), premise (A) (a new statement) and the conservation premise, which (a) does not derive. Q1's grade line should read: (a) restatement; (b) derived, conditional on the new statement (A); (c) open. No new number comes out.

The target's own scripts reproduce the stated numbers: about 20–160% change in Σ|a|^p for p ≠ 2, and violations of 0.2–2.0 in P7. The one file written is `/home/claude/checkQ1/checkQ1.py`.

### 1. Part (a): the Aaronson citation

**What Aaronson actually states** (quant-ph/0401062, §2). There is no numbered theorem. For p ≠ 2 the claim is that the linear maps A with ‖Ax‖_p = ‖x‖_p for **all** x are "generalized diagonal" matrices, meaning a permutation times a diagonal matrix:
- The proof is for real matrices, by cases: even p > 2, odd p, p = 1, and non-integer p > 0.
- For complex amplitudes he gives two norms. One reduces to 2n reals, which gives Σ(|Re a|^p + |Im a|^p), not Σ|a_i|^p. For Σ|a_i|^p itself he writes "We omit a proof of this fact."
- Invertibility is not a hypothesis.
- He adds that this "merely pushes the question … back to the Pythagorean Theorem."

**ERRORS**
- **E1. Wrong source for the complex case.** Q1 cites Aaronson for complex Σ|a_i|^p, the one case he leaves unproved. The proper sources are the Banach–Lamperti isometry theorem (Lamperti 1958) and its finite-dimensional complex form (a phase times a permutation).
- **E2. Gap for general F.** Q1 sets P_i = F(|a_i|) with F general, but the cited theorem covers only F = x^p. A short argument closes this for complex amplitudes when F is continuous and strictly increasing:
  - The maps that preserve ΣF form a compact group G that contains the diagonal phase torus T.
  - If G contains a mixing map, its identity component is larger than T. It then contains a U(2) block on two places i, j.
  - So F(|a_i|) + F(|a_j|) is a function of |a_i|² + |a_j|² only, which gives F = kx².
  
  Either add this argument or cite it.

**WORDING**
- "Not a phase-permutation" should read "not a generalised permutation" (a permutation times unimodular phases), and "for all states" should be added.
- "Invertible" is not needed.
- The conclusion should also say that M is then unitary.

**Does the framing smuggle anything in? Yes, in three places.**
- The conserved quantity is assumed to have the form Σ_i F(|a_i|): additive over places and depending only on each modulus. This is the load-bearing input.
- Linear complex amplitudes are borrowed.
- "Interference happens" is the assumption that some hop is not a generalised permutation.

Given all three, √P follows from a known theorem. So A5's √P becomes "forced by the conservation premise". It does not come from nothing.

**Prior art for the same route (a needed citation).**
- Lesovik, arXiv:1411.6992 (2014): the exponent 2 from conserving ∫|Ψ|².
- Axelsson, *J. Mod. Phys.* 17(10), 1282 (2026), "Born's Rule from Reversible Evolution and Record Formation". This is essentially (a). It requires Σ|(Uα)_i|^p = Σ|α_i|^p under continuous reversible maps and picks p = 2 via finite-dimensional Lamperti, in the language of persistent records.

**Grade for (a): restatement.**

### 2. Part (b): the P7 proof

**OK**
- The complex-phase expansion is correct: E u = b² and E u² = b⁴ + 2a²b² give (xG′)′ = c.
- The general solution of that equation is G = cx + C ln x + D. F(0) = 0 rules out the ln term, so F = kx².
- Sufficiency holds.
- Non-power F fail the full equation: for x² + x⁴ the violation is 7.8; for 1 − e^{−x²} it is 0.57; the control x² gives 3×10⁻¹⁶.

**ERRORS**
- **E3. The regularity hypothesis is misplaced.** "F smooth" does not make G(y) = F(√y) differentiable at 0. For F = x, G = √x and G′(0) is infinite, yet the proof uses G′(0). The repair is short:
  - Fix a > 0. The left side is smooth and even in b, so G(b²) = c·b² + O(b⁴) with c = G′(a²) + a²G″(a²).
  - This c does not depend on a, so G′(0) = c exists.
  
  The correct hypothesis is F ∈ C²(0, ∞) and continuous at 0.
- **E4. The real (±1) case is not closed as written.** The equation G′ + 2xG″ = c has general solution G = cx + 2C√x + D. F(x) = x (G = √x) satisfies it exactly with c = 0 (confirmed numerically in `checkQ1.py`). So "again only G linear" does not follow from the second-order equation alone. F = x is excluded only by the O(b) term, through the evenness argument in E3, or by the full equation: (|a+b| + |a−b|)/2 = max(a, b) ≠ a + b. The conclusion stands; the proof needs that line.

**Is premise (A) circular?** It does not assume F = x². It is a fair "alternatives add once interference is washed out" premise, but two inputs sit inside it.
- **Noncontextuality.** Each contribution is assumed to carry the same weight F(|c|) whether it stands alone or is merged into one record, and every record is assumed to use one F of one modulus. That is Q6's noncontextuality without the power.
- **The phase-randomisation model in (C).** (C) needs commitment to literally randomise a c-number relative phase. If (C) is instead justified by "decoherence is equivalent to random phases", the argument is circular. That equivalence holds at the level of ρ = E[ψψ†], whose operational meaning is the trace rule. Under a non-Born F, entangling decoherence and random-phase dephasing are not equivalent.

**Where (b) sits relative to known derivations**
- **Gleason / Busch / Logiurato–Smerzi:** noncontextuality over all bases or effects. This is stronger than (b) and also gives basis-independence, which (b) does not.
- **Zurek envariance (2005):** phase-envariance shows that phases do not matter, then a counting step. (b) uses phase averaging plus additivity instead of the swap-and-count step. The two are related in spirit.
- **Deutsch–Wallace:** decision theory. Not close.
- **Saunders (2004, *Proc. R. Soc. A* 460):** the weight depends only on the amplitude at the detector, plus additivity over channels, plus continuity. This is the closest structural relative found.
- **Masanes–Galley–Müller (2019):** derive Born and state update from the remaining postulates (rays, unitary dynamics, tensor composition), with no additivity premise of this kind. This is a different and stronger route.
- **Zhang, arXiv:2603.06211 (2026):** argues that additivity is an irreducibly probabilistic input to every such derivation. This applies directly to (A).

No published "random-phase average plus additivity ⇒ x²" derivation turned up in this pass. The step is elementary and plausibly folklore (it is the converse of "random phases ⇒ incoherent addition"), so a novelty claim should not be made.

**Grade for (b):** derived (elementary), conditional on (A), a new statement for CO, and on the borrowed modulus-only weight.

**WORDING**
- "(a) and (b) are independent" is too strong. Both assume a modulus-only weight and linear amplitudes.
- (b) fixes only the shape of F, up to k. Setting k = 1 needs Σ|a|² = 1, which comes from (a).

### 3. Part (c): the Piron–Solèr table

**ERRORS**
- **E5. The theorem statement is incomplete.**
  - Piron (1964) also needs irreducibility and height ≥ 4. Its output is an orthomodular (generalised Hilbert) space over a division ring with involution, not yet ℝ, ℂ or ℍ.
  - Solèr (1995) then needs an infinite orthonormal sequence to pin the field down to ℝ, ℂ or ℍ.
- **E6. The first three "yes" rows are overstated.** What CO supplies is a family of Boolean algebras, one per record type. That is a partial Boolean algebra in the Kochen–Specker sense, not a lattice. An orthocomplement on the whole lattice, and completeness (which has no row), need the lattice first. "Kept and repeatable" (P² = P) is not a Piron axiom; it motivates ideal measurements and the covering law. Better wording: "supplies Boolean blocks; the lattice, its completeness and its orthocomplement are not shown."

**OK**
- The "not shown" rows (orthomodularity, atomicity and covering, Solèr's sequence) are fair.
- The ℂ row is fair: local tomography is the standard way to exclude ℝ and ℍ.

**WORDING.** Masanes–Müller (2011) is a full reconstruction of finite-dimensional quantum theory, Born rule included. It is not a way to select the field on its own. If it is borrowed, it makes (a) to (c) redundant rather than completing them.

### 4. Does Q1 replace Q6 and A5's √P?

It moves them; it does not remove them. Q1's "after Q1" table should be revised to match.
- **A5's √P** now rests on the premise that possibility is conserved as Σ_places F(|a|) under mixing hops. That premise is a new statement, or borrowed, but it is not derived.
- **Q6** gives Pr(E) = ⟨ψ|E|ψ⟩ for every effect E. After Q1:
  - The modulus-only, one-F-for-every-record noncontextuality is still borrowed.
  - (A) is a new statement.
  - (C) needs commitment to physically randomise a c-number phase. That is a new statement for CO, and it is not equivalent to entangling decoherence without the trace rule.
- **Still borrowed:** linear complex amplitudes, the ℂ field, the Hilbert-space form, and general effects/POVMs, which (b) does not reach.

Sources:
- [Aaronson, quant-ph/0401062](https://arxiv.org/pdf/quant-ph/0401062v1)
- [Johnston, isometries of the p-norms (complex permutations)](https://njohnston.ca/2010/09/isometries-of-the-vector-p-norms-signed-and-complex-permutation-matrices/)
- [Lesovik, arXiv:1411.6992](https://arxiv.org/pdf/1411.6992)
- [Axelsson, arXiv:2604.07418 / JMP 2026](https://arxiv.org/html/2604.07418)
- [Zhang, arXiv:2603.06211](https://arxiv.org/html/2603.06211v1)
- [Logiurato–Smerzi, arXiv:1202.2728](https://arxiv.org/pdf/1202.2728)
- [Zurek, quant-ph/0211037](https://arxiv.org/pdf/quant-ph/0211037)

**Recommended next steps**
1. In (a), replace the Aaronson citation with Lamperti 1958 and the complex isometry result, add the compact-group step for general F, and cite Lesovik 2014 and Axelsson 2026. Regrade (a) as restatement.
2. In P7 §1, change the regularity hypothesis to F ∈ C²(0, ∞) and continuous at 0, add the "G(b²) is even in b" line, and fix the real-case sentence (F = x solves the local equation and is excluded only by the O(b) or full equation).
3. Restate the claim about Q6: it is split into a borrowed modulus-only weight, the new statement (A), and (C) as literal c-number phase randomisation. Update Q1's "after Q1" table to match.
4. Fix the Piron–Solèr statement (irreducibility, height ≥ 4, the division ring) and change rows 1–3 to "Boolean blocks only".
5. Before any novelty claim for (b), run a targeted search of Saunders 2004 and its citing papers.