### Run 91: does the whole field-order-2 algebra close at order a²? (Note H, field order 2; a calculation)

*26–27 October 2026.*
- *Registered and hashed before the run (`modes91/PREREG_91.md`, with the code, the validation outputs and a dry run; 63 files; 20:52:30 UTC on 26 October).*
- *Validation beforehand:*
  - *the sparse Jacobian's exactness at D2 for every form;*
  - *the joint solve at order a, with and without the O₁ hold;*
  - *a planted toy at D2;*
  - *negative controls at order a;*
  - *a timing build;*
  - *a dry run at order a.*
- *An independent agent checked the run (below), and its corrections are adopted here.*

**Why.** At field order 2, the record so far has the algebra closing:
- at the continuum degree and at order a (Run 87);
- at order a², in the kinetic sector, once the theory may change three things there (Run 89): the kinetic dressing P, the second-order energy's lapse coupling δM and the first-order energy's lapse coupling δC;
- with relativistic waves forced within form (iii) (Run 90).

The potential sector at order a² is the remaining part of field order 2:
- (C), {H, D} at order h², where Regge's third-order energy T₃ enters;
- (D), {D, D} at order πh.

It is the decisive test for GR's route at field order 2, and the agreed cut-off for the gravity sector (stated 26 October).

**The design changed before registration.** The first design held the kinetic sector at Run 90's solution K90z0 and solved the potential sector alone, as a linear least-squares problem. Its validation showed that this cannot work. Even at order a, where Run 87 found closure, the potential sector on K90z0's kinetic Hamiltonian leaves a certified substantive residual (ρ = 7.5×10⁻³ in C4).

K90z0 is one member of a kinetic solution family with 1,678 null directions, and the potential sector selects among the members. So Run 91 solves all eight conditions together. At order a the joint solve closes from K90z0, with or without the O₁ hold, which reproduces Run 87.

**Question.** With the kinetic sector in Run 90's form (iii), so that the order-a constant-lapse kinetic change O₁ is held at zero, does the whole system close at D2:
- **(a)** with T₃ as registered (Regge's, with N0′'s β₂ and the end-average lapse);
- **(b)** with, in addition, T₃'s lapse coupling changed at orders a and a²;
- **(c)** with T₃'s general change at those orders, the waves' cubic vertex included?
- And only if none closes, **(u)**: does (c) close with O₁ free?

Form (b)'s change vanishes for constant lapse:
$$
\delta T_3(p_1,p_2,p_3)_{xyn}=\tfrac16\sum_{\text{perms}} i(p_1+p_2+p_3)_b\,Z_3(\text{perm})_{b\,\text{perm}},\qquad Z_3\ \text{at degrees }2\text{–}3 .
$$
Form (c)'s is the general change, at degrees 3–4:
$$
\delta T_3=\tfrac16\sum_{\text{perms}}\Delta T_3 .
$$

**The system** (`conds91.py`, `joint91.py`). The kinetic sector is Run 89's form (ii) with Run 90's O₁ hold. The potential sector is Run 87's
$$
\text{(C)}\quad T_3\cdot G+M\cdot S\,(\times2)+C\cdot T+M\cdot L^0+\Lambda\cdot C\,(\times2)=0,\qquad
\text{(D)}\quad S\cdot S\,(\times2)+T\cdot G\,(\times2)-S\cdot B^0-G\cdot B=0,
$$
with M → M + δM and C → C + δC carried in as in the kinetic sector. The unknowns, all solved together through the D2 degrees:
- the kinetic sector's S, L⁰, B⁰, W⁽¹⁾, U⁽¹⁾, V, Y, P, Q, Z and δC;
- the potential sector's T (the sliding's h² part), Λ (the h-dependence of L) and B (the h-dependence of [u, v]), through degree 3.

CG (δC·G = 0) and O₁ = 0 are imposed exactly, through an orthonormal kernel basis.

| form | reduced unknowns | free columns | coefficient rows | Jacobian non-zeros |
|---|---|---|---|---|
| (a) | 25,078 | 24,505 | 518,460 | 59.6 million |
| (b) | 48,966 | 47,297 | 518,460 | 64.3 million |
| (c) | 51,102 | 48,497 | 518,460 | 61.4 million |

**The method** (`sparse91.py`, `joint91.py`).
- **Residual and Jacobian.** The residual is the vector c(z) of exact monomial coefficients (Run 89's coefficient mode). It is quadratic in z. Its Jacobian is built term by term and stored sparse, and it is exact: central differences agree to 1.4–1.8×10⁻¹⁴.
- **The step.** Gauss–Newton with Run 90's never-increase rule: LSMR on the row-weighted, column-scaled system, truncated at 5,000 iterations. A step must lower the cost, by halving down to 2⁻¹⁰ or by damped LSMR; otherwise the start stops ("stalled").
- **Stopping:**
  - cost below 10⁻²⁰ of the start;
  - a relative decrease at most 10⁻⁸ ("slow");
  - two consecutive steps each lowering the cost by less than 1% ("stagnant");
  - 16 iterations, or 8 for controls.

  Checkpoints let a start resume after the 90-minute process budget.
- **The rules.** A start *closes* if, on both point sets, non-floored max ρ ≤ 10⁻⁸ and floored max |r|/largest ≤ 10⁻¹². It is *failing* if it does not close, its held-out substantive max ρ (blocks with ≥ 10⁻² of the largest content) is ≥ 10⁻⁴, and it stopped progressing.
- **The verdicts.** A form EXISTS if a start closes and both controls fail. A form is NOT FOUND if all three starts fail.

**Validation (before registration).**

| item | result |
|---|---|
| V5: Jacobian exactness at D2, forms (a)–(c) | central differences agree to 1.4×10⁻¹⁴, 1.6×10⁻¹⁴ and 1.8×10⁻¹⁴; peak memory about 3 GB |
| V6: order a, joint, from K90z0 | closes in 5 iterations, with O₁ held (\|O₁\| = 1.4×10⁻¹⁹) and with it free (\|O₁\| = 0.070); held-out 1.1×10⁻¹⁵ |
| V7: planted toy at D2 (a known exact solution 0.1‖K90z0‖ away) | converged in 4 full steps (cost ratio 1.5×10⁻²⁶; largest block 38.7 → 4.3×10⁻¹²); the truncation does not stop convergence |
| V8: random terms in C4 and D3, order a | both failing (substantive ρ 0.13 and 0.063), with the iterate norm growing from 16 to 161 and 381 |
| V9: timing at D2 | Jacobian 101 s; LSMR 0.15 s per iteration |
| dry run, order a | every step exits 0; at order a it reproduces Run 87 (closes; both controls failing) |

**Result (registered).**

| step | form | start | iterations, end | weighted cost | held-out max ρ: substantive; non-floored | outcome |
|---|---|---|---|---|---|---|
| K91a0 | (a) | K90z0 | 8, stagnant | 2,556 → 9.72 | 1.9×10⁻² (D4); 0.28 | failing |
| K91a1 | (a) | K90z0 perturbed (seed 9111) | 4, stagnant | 2,541 → 0.0544 | 2.1×10⁻³ (D4); 0.63 | failing |
| K91a2 | (a) | K90z0 perturbed (seed 9112) | 4, stagnant | 2,662 → 0.0548 | 2.0×10⁻³ (D4); 0.66 | failing |
| **K91b0** | **(b)** | K91a2's solution | 4, slow (at rounding) | 0.0584 → 2.7×10⁻²⁰ | **1.0×10⁻¹⁵; 3.1×10⁻¹⁴** (floored 2.1×10⁻¹⁶) | **closes** |
| NC-C | (b) + a random C5 term | K91b0's solution | 6, stagnant | 2,405 → 1,553 | 4.3×10⁻² (C4); 0.80 | failing, as required |
| NC-D | (b) + a random D4 term | K91b0's solution | 3, stagnant | 249 → 103 | 6.0×10⁻² (D4); 0.77 | failing, as required |

- Form (a): **NOT FOUND**.
- Form (b): **EXISTS**.
- Forms (c) and (u) were not run, as registered.

**Overall (registered): CLOSES WITH A LAPSE COUPLING.** K91 (GR's route survives field order 2 through a²) **PASSES**. K91r (Regge's third-order energy needs no change at a²) **FAILS**: by the check's reading, Regge's third-order energy as registered was not found to close from three starts.

**The registered report.**
- **Form (a)'s residual.** At the best start (K91a2):
  - 96% of the held-out residual is in (C), 2.8% in (D), and under 1% in the kinetic conditions;
  - the substantive ρ is 10⁻⁴–10⁻³ throughout, largest in D4 (2.0×10⁻³), DD14, C5 and D3.
- **The change that closes it.** δT₃ vanishes exactly at constant lapse. The registered measure gives it as 6.7% of Regge's own T₃ at degrees 3–4. That figure mixes the two degrees at one momentum scale; the check corrects it below. It is about 1% of Regge's order-a part and 12–16% of its order-a² part, for this member of the Z₃ family, which is not a minimised change.
- **The kinetic sector.** At K91b0 it differs from K90z0 by 0.86‖K90z0‖. Most of that, 0.82, was already present at K91a2's iterate: its random start plus its own steps. K91b0's own steps moved it by 0.13.
  - The movement sits at the top degrees: W⁽¹⁾ at degree 2, U⁽¹⁾ and S at degree 3, Z at degree 3.
  - The continuum parts are unchanged, apart from drift inherited from the random start.
  - The dressing P barely moves (cosine 0.97), and nor does δC (0.995).
- **The waves stay relativistic** at K91b0.
  - The `lorentz` dispersion rows hold to 4.2×10⁻¹⁵.
  - The registered Richardson estimate agrees to 6.2×10⁻⁶. That is the estimate's own error: the check's exact extraction gives the ε⁴ coefficient to 4×10⁻¹³ and the splitting to ≤ 2×10⁻⁸, so Lorentz to rounding.
  - |O₁| = 4.9×10⁻¹⁷.
  - The failing form-(a) iterates are not relativistic: their ε⁴ coefficient is off by about 6×10⁻³.

![Run 91](../figures/91_lapse_coupling.png)

**The independent check.** All 62 hash lines verified at the start and at the end, and the files of Runs 85–91 were unchanged throughout. Its findings:
1. **K91b0's closure is real.**
   - On fresh points (seed 91777) it gives non-floored max ρ 3.1×10⁻¹⁴, floored 2.1×10⁻¹⁶ and substantive 1.0×10⁻¹⁵.
   - Constraints and holds are met to rounding: |O₁| 4.9×10⁻¹⁷, CG 1.5×10⁻¹⁵, and all 1,650 held coordinates are exactly 0.
   - In coefficient mode the "held-out" points check the exact extraction of coefficients; they are not an independent sample.
2. **Z₃ is a lapse coupling, and the closure is not trivial.**
   - Z₃'s terms vanish exactly at zero lapse momentum and at zero shift momentum, at every degree. They reach only C4 (rank 734) and C5.
   - At K91b0, form (a)'s own C, with no Z₃, closes on the constant-lapse slice to 6×10⁻¹³. So Regge's energy closes the constant-lapse part by itself once the other unknowns adjust, and Z₃ supplies only the part that depends on the lapse momentum.
   - Z₃'s range misses 64–79% of form (a)'s own C residual at K91a2, so Z₃ alone does not fix form (a): the joint solve moved the other unknowns too.
   - Form (b)'s whole Jacobian misses 76% of NC-C's term and 64% of NC-D's. The controls' failures are linear facts.
3. **Form (a)'s NOT FOUND holds by the registered rule, but its stops were solver-limited.**
   - 25 of the run's 29 steps hit the LSMR truncation. Form (a)'s steps were accepted at λ = 1/32–1/64. Its three "stagnant" ends had stationarity σ = 0.7–1.3×10⁻², against about 1.4×10⁻³ for a random residual.
   - **Post hoc**, from K91a2:
     - the potential sector solved exactly with the kinetic sector fixed lowers the cost by 33%;
     - eight Levenberg–Marquardt steps with untruncated solves reach a near-stationary point (σ ≈ 10⁻⁴) 34% lower in cost.
   - At that point the substantive residual is still 1.2×10⁻³ (DD14, C5, D4), 12× the threshold. So this basin's failure is robust, and the registered stop was not stationary. NOT FOUND rests on three basins.
4. **The Jacobian.** Its non-zeros fall from 63.8 million at K91b0's start to 44.9 million at the solution. The coordinates the conditions force to zero sit at 10⁻¹¹–10⁻⁴ at a non-closing iterate and at 10⁻¹⁵ at the closure, so their products fall under the drop rule. At the solution J is exact: central differences agree to 2.5×10⁻¹⁴. Closure is judged on the exact residual, so the drop rule bears only on the steps.
5. **The restart.** Every step's starting cost equals the previous step's final cost bitwise, the resumes included. The final iterates equal the last checkpoints.
6. **The conditions are what they claim to be.**
   - Run 87's C and Run 89's HD1, B and HH1, evaluated with dressed knowns (M + δM, C + δC, T₃ + δT₃), match the swapped conditions to 2–3×10⁻¹⁶. So the same δM and δC enter both sectors, and nothing else changes.
   - δT₃ is symmetric over its legs to 3×10⁻¹⁶.
   - **One gap:** (D) is Run 87's narrow form, without Run 88's third π-linear structure function ν in {D, D}. That cannot affect the closure. At K91a2, adding ν (post hoc) leaves the substantive residual at 1.4×10⁻³, because form (a)'s residual sits in C, which ν cannot reach.
7. **The vertex.** Regge's h³ vertex is kept at constant lapse, but the ππh vertex W⁽¹⁾ is free in every form, and it changes:
   - at k = 0 it differs from K90z0's by 14% at order a and 112% at order a²;
   - its continuum part is unchanged to 2×10⁻¹⁵.

   The on-shell cubic interaction was not computed.

**Corrections adopted (the check).**
- **The dispersion accuracy** is rounding, not 6.2×10⁻⁶ (finding 7 of Run 90's check, again).
- **δT₃'s size** is about 1% of Regge's order-a part and 12–16% of its order-a² part, not a single 6.7%. The order-a part is not shown necessary: form (a) closes at order a (V6), and a form with Z₃ at degree 3 only was not tested.
- **K91r reads** "Regge's third-order energy as registered was not found to close from three starts". It does not read "needs a change".
- **The registration's limit** "a NOT FOUND rests on three starts per form, each ending stationary" is false as worded. The starts ended stagnant under truncated steps; post hoc, a damped solve reaches a near-stationary point 34% lower in cost, where the substantive ρ is still 1.2×10⁻³.
- **"The waves' cubic vertex is unchanged"** becomes: Regge's h³ vertex is kept, not shown forced, since (c) was not run; and the ππh vertex W⁽¹⁾ changes at a and a².
- **The kinetic movement** is mostly inherited from K91a2's random start (0.82 of the 0.86).
- **Disclosed:** a line was added by hand to `run91_K91a2.log` to record the restart, and `run91_chain.txt` lists one K91a1 line twice for a single process.


**Reading.**
1. **On this lattice, a Hamiltonian exists for which GR's constraint algebra closes at field order 2 through order a², kinetic and potential sectors together.** So GR's route survives field order 2.
   - Beyond Regge's construction, it needs:
     - the kinetic dressing;
     - the lapse couplings of the first- and second-order energies (Run 89);
     - the lapse coupling of the third-order energy (here).
   - Every one of these except the dressing vanishes at constant lapse.
   - This is one solution, from one start: a formal closure at the origin of momentum space, not a global certificate.
2. **Regge's third-order energy as registered was not found to close** from three starts. The residual is substantive: about 2×10⁻³, and 1.2×10⁻³ at a post hoc near-stationary point.
   - Allowing its lapse coupling to change at orders a and a² closes the system.
   - The change is about 1% of Regge's order-a part and 12–16% of its order-a² part, for this member of the family. Its order-a part is not shown necessary.
   - It is the counterpart, one order higher in the fields, of Run 89's δM for the second-order energy.
3. **At constant lapse, Regge's h³ vertex is kept.** Form (c), which could change it, was not needed, so keeping it is possible; it is not shown forced. The ππh vertex W⁽¹⁾ is free in every form, and it does change at a and a², so the waves' full cubic interaction at a² is not Regge's. The on-shell amplitude was not computed.
4. **The waves stay relativistic at the joint closure.** That is a consistency check of Run 90's result within form (iii), not new information. What is new is a far member of the family: 0.86‖K90z0‖ from K90z0, most of it inherited from the perturbed start.
5. **What is not derived.** GR's constraint algebra is imposed here, not derived from CO's primitives. The changes are the theory's lattice-level freedoms, found, not predicted.

**Limits.**
- **Formal:** at the origin of momentum space; through a²; at field order 2.
- **Form (a)'s NOT FOUND** rests on three starts that ended stagnant under truncated steps, not at stationary points. A post hoc damped solve from the best one keeps the substantive residual at 1.2×10⁻³. It is not a global certificate.
- **(D) is Run 87's narrow form,** without Run 88's structure function ν. That cannot affect the closure, and post hoc it does not help form (a).
- **The closure is constructive and controlled** (two random terms not absorbed).
- **O₁ is held** (form (iii)). Closures with an order-a constant-lapse kinetic change are untested.
- **Field order 3,** where Regge's own vertex symmetry is expected to break (Bahr and Dittrich), is untested.
- **The setting:** N0′, λ = 1, a flat background, one triangulation.

**Disclosed.**
- **The design change before registration,** with the first design's validation (V1–V4) kept.
- **The solver changed three times during validation,** each time on a negative control at order a, which is not a registered system:
  - LSMR truncated at 5,000 iterations, after one untruncated step took 15,266 iterations;
  - the stagnant rule added, with its threshold raised from 10⁻³ to 10⁻²;
  - the controls' cap set to 8.

  A drafted stationarity threshold for failing starts was dropped before registration.
- **A container restart interrupted K91a2** after its iteration-1 checkpoint. It resumed from the checkpoint at the checkpointed cost, and every registered file's hash verified afterwards.
- **No Gauss–Newton step on a registered D2 system was taken before registration.**
- **Two log artefacts:** a line was added by hand to `run91_K91a2.log` to record the restart, and `run91_chain.txt` lists one K91a1 line twice for a single process.
