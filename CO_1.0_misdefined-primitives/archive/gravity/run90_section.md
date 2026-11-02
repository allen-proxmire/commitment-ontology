### Run 90: does first-class closure at order a² force relativistic gravitational waves? (Note H, field order 2; a calculation)

*26 October 2026.*
- *Registered and hashed before the run (`modes90/PREREG_90.md`, with the code, the validation outputs and a dry run; 00:57:18 UTC).*
- *Validation beforehand:*
  - *the wave-speed rows against exact eigenvalues;*
  - *the solver on negative, planted and warm-start problems at D2, including a reproduction of Run 89's K89a;*
  - *a timing build;*
  - *two dry runs, the first of which led to two disclosed changes before registration.*
- *An independent agent checked the run (below), and its corrections are adopted here.*

**Why.** Run 89's check found that the full kinetic sector's closing Hamiltonian (K89b's) makes the constant-lapse gravitational waves relativistic through order a²:
$$
\omega^2_{TT}=s^2+O(s^5)\qquad\text{instead of Run 84's}\qquad \omega^2=s^2-\tfrac1{12}\textstyle\sum_a s_a^4+O(s^6).
$$
Its interpretation, not proved, was that GR's algebra contains the boost relation {H[1], H[x^a]} = D[e_a], so first-class closure at a² should *force* this. It recommended testing that with the dispersion imposed.

**Question.** In the kinetic sector at D2, with Run 89's freedoms:
- does every closure have ω²_TT = s² + O(s⁵)?
- is Run 84's dispersion excluded?
- is an isotropic but non-relativistic dispersion excluded?

The last is the discriminating test. An isotropic s⁴ term is allowed by every lattice symmetry, and only the boost relation forbids it.

**The wave speed as a constraint** (`disp90.py`). At constant lapse, δM and δC vanish, so ω² = −eig(Ω̂M̂), with
$$
\hat\Omega(s)=K^{-1}+\Omega_2(0,s),\qquad \hat M(s)=M(-s,s).
$$
Write s = εŝ, and let P have no order-a constant-lapse part (below). Then the order-ε⁴ change of the two TT frequencies relative to Run 84 is given by first-order degenerate perturbation theory:
$$
\delta\omega^2=\varepsilon^4\,\mathrm{eig}\big(-L\,O_2(\hat s)\,M_2(\hat s)\,R\big),\qquad LR=1,
$$
where R and L are the right and left eigenvectors of A₀ = K⁻¹M₂ for its isolated two-fold eigenvalue −1.
- The 2 × 2 matrix is similar to a Hermitian one, so "both polarisations shift by c(ŝ)" holds exactly when −LO₂M₂R = c(ŝ)·1.
- That condition is imposed exactly, at 48 directions, as linear rows on P's degree-2 part (rank 10, saturated by 20 directions).
- **Validation:** against exact eigenvalues, random P agree to 3.6×10⁻⁵, K89a0 to 1.2×10⁻⁵, and Ω₂ = K⁻¹q(s) to 1.3×10⁻⁶. These limits are those of the Richardson estimate. The check's exact extraction (a Cauchy integral in ε) gives 5.8×10⁻¹⁴.

**The targets** (the change relative to Run 84):

| target | c(ŝ) | dispersion |
|---|---|---|
| Run 84's | 0 | ω² = s² − Σs_a⁴/12 |
| relativistic | Σŝ_a⁴/12 | ω² = s² + O(s⁵) |
| isotropic | Σŝ_a⁴/12 − 1/20 | ω² = s² − s⁴/20 (Run 84's angular average) |

**The Run 89 check's rows.** That check's rows used the orthogonal projector onto TT(s) instead of left and right eigenvectors.
- For random P they miss the exact eigenvalues by 0.12; at K89a0 they agree.
- The registration concluded from this that its post hoc "form (i) cannot keep Run 84's dispersion (minimum 0.61)" was not established. **That conclusion was wrong (Run 90's check, below).** At constant lapse, HH1 forces the two sets of rows to coincide at every form-(i) closure. So the 0.61 stands, and K90d confirms it.

**The forms.**
- **(iii):** Run 89's form (ii), the full kinetic sector (HD1, DD1, A, B, HH1, CG with P, Q, Z, δC), with the constant-lapse order-a kinetic change set to zero, Ω₂(0, s)|deg 1 = 0.
  - With that term nonzero, the a² dispersion picks up a term quadratic in it, and the constraint would not be linear.
  - K89b0 has one (|O₁| = 1.52), and its dispersion is relativistic only with that term's second-order part included. Whether closure survives its removal is K90z.
- **(i):** Run 89's form (i), the spatial sector with {H, H} at order π but no (B).

**Two changes before registration, from the first dry run.**
- **CG is imposed exactly.** CG, δC(k)·G(−k) = 0, is linear in δC alone (12 rows on 18 coordinates, leaving the 6 gauge-invariant directions). As a soft condition its single term gives ρ = 1 at any nonzero residual; that is what Run 89's NC2 reported as "CG5 ρ = 1.0".
- **NOT FOUND needs a real residual.** A block whose content is one small term reports ρ = 1 at any residual, so NOT FOUND now also needs some held-out block residual of at least 10⁻¹⁰ of the largest block's term sum.

**The solver** (`solver90.py`) is Run 89's coefficient-mode Gauss–Newton with these changes:
- it never accepts a cost increase: step halving to 2⁻¹⁰, then Levenberg–Marquardt steps, and otherwise it stops ("stalled"). This is the Run 89 check's hygiene item;
- every constraint is imposed exactly, as z_F = z_p + Ey with E an orthonormal basis of ker C;
- warm starts from stored solutions, projected onto the constraint;
- it stops at rounding level.

**Result (registered).**

| rule | form | dispersion imposed | starts | held-out, over the starts: max ρ; largest \|r\| / largest block | verdict |
|---|---|---|---|---|---|
| **K90z** | (iii) | none | 1 (closed at start 0, three steps) | non-floored 1.3×10⁻¹⁵ | **EXISTS: PASS** |
| **K90b** | (iii) | relativistic | 1 (closed at start 0) | 1.2×10⁻¹⁵ | **EXISTS: PASS** |
| **K90a** | (iii) | Run 84's | 3 (costs stall at 0.033, 0.032, 0.041) | 0.98–0.99; 1.4–1.9×10⁻³ | **NOT FOUND: PASS** |
| **K90c** | (iii) | isotropic | 3 (costs 0.011, 0.021, 0.28) | 0.28–1.0; 1.6–1.8×10⁻³ | **NOT FOUND: PASS** |
| **K90d** | (i) | Run 84's | 3 (costs 0.020) | 0.73–0.74; 3.0–3.2×10⁻³ | **NOT FOUND: PASS** |
| **K90e** | (i) | relativistic | 3 (costs 0.028) | 0.76–0.79; 4.1–4.6×10⁻³ | **NOT FOUND: PASS** |
| NC90 | (iii) + a random B4 term | relativistic | 1 (cost 235 → 92) | 1.0; 8×10⁻³ | NOT FOUND, as required |
| NC89r | Run 89's NC2, with this solver | — | 1 (cost 133 → 91) | 1.0; 7×10⁻³ | NOT FOUND (the cost fell monotonically, but \|z\| grew 24×) |

**Overall (registered): LORENTZ FORCED.**

**The registered report.**
- **Dispersion.** K90z's closure, with no dispersion imposed, has the relativistic dispersion:
  - its rows are met to 3.1×10⁻¹⁵;
  - the exact eigenvalues at 30 directions agree to 6.9×10⁻⁶ (Richardson). The check's exact extraction gives 7.7×10⁻¹⁴: **Lorentz to rounding**;
  - the polarisation splitting is at most 1.3×10⁻⁵ (exact: 9.4×10⁻¹⁴), and the order-a change at most 3.6×10⁻⁷ (exact: 1.7×10⁻¹⁴).
- **The family.** The dispersion cannot change along the solution family to first order: the dispersion rows applied to the 1,678-dimensional null space have singular values ≤ 8×10⁻¹⁵ of their norm.
- **Where the failing fits stall.** The largest ρ is in four low-degree blocks with tiny content (B1, HD12, DD11, A0, each about 5×10⁻⁶ of the largest block). The substantive failure is in the top-degree blocks: DD14, HH13, HH14, B4, HD15 and A3.
  - On the blocks with at least 10⁻² of the largest content (the check's measure), the held-out max ρ is:
    - K90a: 4.8–6.7×10⁻³;
    - K90c: 1.6–1.7×10⁻³ (start 2: 1.8×10⁻²);
    - K90d: 2.0–2.1×10⁻²;
    - K90e: 2.1–2.3×10⁻².
  - So every NOT FOUND clears the 10⁻⁴ threshold by a factor of at least 16 on substantive content.

![Run 90](../figures/90_lorentz_forced.png)

**The independent check.** Its certifying computations were all independent of the solver path:
- Cauchy-integral degree extraction on fresh points;
- LAPACK SVD, pivoted QR and least squares on the exact S3-reduced coefficient system;
- the TT dispersion by an exact Cauchy integral in ε of the TT effective matrix, with its own perturbation theory;
- the constraints (O₁, CG, dispersion) rebuilt independently.

The findings:
1. **Hashes, time order, reproduction.**
   - 33/33 hashes OK at the start and the end.
   - Code, validation and dry runs precede the registration.
   - All 16 stored steps reproduce every logged block exactly, and every step was monotone.
2. **K90z and K90b: certified.**
   - Independent extraction gives non-floored max ρ 5.0×10⁻¹⁴.
   - LAPACK rank 3,895 (3,885 with the relativistic rows) matches the engine, with a clean gap.
   - The exact dispersion is
$$
\omega^2=s^2+O(s^5)\qquad\text{to }7.7\times10^{-14}.
$$
     Directly, over 200 directions, |ω² − s²|/s⁴ falls in proportion to |s| (7.3×10⁻⁵ at |s| = 0.01), against Run 84's 0.028–0.083.
   - K90b adds nothing beyond K90z, whose solution already met the relativistic rows.
3. **The dispersion is rigid along the family.**
   - The null space (1,678 directions) coincides with the engine's: all principal cosines are 1.
   - The dispersion rows on it vanish to 9.3×10⁻¹⁶. Equivalently, the dispersion is a first-order consequence of the conditions.
   - Closures re-found at finite distances along the family, out to |δz| = 3.2, keep the relativistic dispersion to 4×10⁻¹⁴.
4. **K90d and K90e: certified within form (i) at D2.**
   - **K90e.** The blocks with no bilinear term force S₀ = L⁰₀ = 0, after which they are affine and are inconsistent with the relativistic rows: the minimum residual is 0.526, nearly all in HH14. The isotropic rows fail the same way.
   - **K90d.** The problem reduces exactly to 10 sliding coordinates, and range inclusions give a minimum residual of at least 2.107×10⁻² for every value of them. In fact it is constant, which explains the Run 89 check's "0.6096 every time". Only A3 fails.
5. **K90a and K90c: supported, not certified globally.**
   - Variable projection was run with the partners S, L⁰ and δC held at K90z's solution and at three points along its family, and every other unknown solved exactly with the dispersion imposed. It leaves substantive ρ of 9.3–9.5×10⁻³ for Run 84's dispersion and 2.2–2.3×10⁻³ for the isotropic one, and moving the partners from there gives no descent.
   - The affine part of form (iii) admits every target, so no affine certificate exists.
6. **The Run 89 check's 0.61 stands.** Its orthogonal-projector rows coincide with the exact rows wherever HH1 holds at constant lapse with δC = 0, so at every form-(i) closure: at K89a0 to 1.7×10⁻¹⁶. In forms with δC they are not exact even at closures (K90z0: 7.5×10⁻³), but they were never used there.
7. **The low-degree blocks with ρ ≈ 1 are solver artefacts.** The fits leave S₀ and L⁰₀ at about 10⁻⁴, although the affine blocks force both to zero. Setting them to zero removes those blocks and leaves the substantive ones unchanged.
8. **What admits relativistic waves (post hoc).** At constant lapse, HH1 links the dispersion's Ω₂(0, s) to the first-order energy's a² lapse coupling:
$$
O_2C_2=f_0-\Omega_{D4}(0)\,\delta C_4\pmod{G_1}.
$$
   - With δC = 0, {H, H} at order π excludes the relativistic and the isotropic dispersions, in form (iii) exactly as in form (i).
   - With δC free, it admits both. The remaining conditions, (B) among them, then remove the isotropic s⁴ freedom that form (i) keeps.
   - In form (i), K89a0's family has exactly one free dispersion direction: an isotropic s⁴ shift of both polarisations together.

**Corrections adopted (the check).**
- **The registration's doubt about the Run 89 check's 0.61** was wrong (finding 6). The check's rows are stronger than the exact ones in general (rank 14 against 10) and exact at every form-(i) closure, so its result stands; K90d confirms it, and the check certifies it.
- **The registered dispersion figures** (6.9×10⁻⁶ and the validation's 10⁻⁵–10⁻⁶) are the Richardson estimate's error, not properties of the solutions. Exact extraction gives 10⁻¹⁴.
- **The report's "best start"** was chosen by the smallest held-out max ρ, which non-substantive blocks set. For K90c that picked start 2 (cost 0.28), so the report's K90c residual shares (A 0.743, B 0.164) describe the worst fit. At K90c0 the shares are B 0.876, HD1 0.094 and A 0.027.
- **The NOT FOUND guard is weak in principle,** and ρ can be lowered by inflating unknowns along near-null directions. The verdicts here rest on the substantive blocks, by a factor of at least 16. Future rules should judge NOT FOUND on substantive blocks and report absolute residuals with |z|.
- **The controls' "no divergence" holds for the cost only.** The iterate norm grew from 12.7 to 305 (NC89r) and from 12.9 to 433 (NC90): the pseudo-inverse admitted large steps along near-null directions. The controls are carried by the linear test, in which 60% of the NC90 term lies outside the Jacobian's range.
- **Form (i)'s registered reading.** "Fixes a dispersion" should read "restricts it": the birefringent anisotropic part is fixed, while an isotropic s⁴ coefficient is free along K89a0's family. K90e's stated reason ("nothing forces Lorentz dynamics") was wrong: HH1 excludes Lorentz exactly when δC = 0, so the verdict is certain, not low-confidence.
- **Order and disclosure,** none of which bears on the verdicts:
  - K90b0 ran before K90a0, although the registration lists K90a first;
  - starts that were not needed (K90z1–2, K90b1–2) left no "skipped" records;
  - the dry run's K90a0 also previewed K90a1's start;
  - the hashed V3 log holds the first V3d; the rerun is recorded only in `validate90.json`.
- **In the record, Runs 89 and 89's check: "in both cases the dispersion is effectively fixed"** is too strong for K89a0. Its birefringent anisotropic part is fixed, and an isotropic s⁴ coefficient is free to first order. K89b0's is fixed.

**Reading.**
1. **On this lattice, at order a² in the kinetic sector, GR's constraint structure fixes the gravitational waves' constant-lapse dispersion to the relativistic one.**
   - With no order-a constant-lapse kinetic change, every closure tested carries ω² = s² + O(s⁵) exactly, and the solution family cannot move it.
   - Run 84's lattice dispersion and an isotropic non-relativistic one are not found. That is from three starts each and from variable projection along the family, though it is not proved globally.
   - In lattice language this is a Symanzik-type O(a²) improvement that the algebra demands.
2. **What makes it possible is the first-order energy's a² lapse coupling,** which lets {H, H} at order π accept relativistic waves at all. The rest of the conditions then fix the isotropic part. This fits the boost-relation reading, but Run 90 does not isolate (B) as the cause.
3. **The spatial sector alone** (form (i), with {H, H} at order π and no δC) admits neither Run 84's dispersion nor a relativistic one. Its waves keep a fixed birefringent part, plus one free isotropic s⁴ term. This is at λ = 1, with HH1 and without the α term, so it is not the khronometric route proper.
4. **What is not derived.** The waves' Lorentz invariance is tied to GR's constraint algebra, which is imposed here, not to CO's primitives. This is consistent with the record's borrowed Lorentz input (19 October). The effects are of relative order (as)², far below observation. They bear on which lattice dynamics is consistent.

**Limits.**
- The kinetic sector only. The potential sector at a² (C, D at D2) is untested and needs a sparse solver.
- Formal, at the origin of momentum space; through a²; at field order 2.
- Form (iii) excludes an order-a constant-lapse kinetic change. Closures with one have a dispersion that is nonlinear in P, and that case is untested.
- Three targets, not every dispersion. "Forced" means: two alternatives are excluded, and K90z's family does not move the dispersion to first order.
- In form (iii) a NOT FOUND rests on three starts and on variable projection along K90z's family; it is not certified globally. In form (i) both verdicts are certified at D2.
- This ties the waves' Lorentz invariance to GR's constraint algebra, which is imposed. It does not derive Lorentz invariance from CO's primitives.
- N0′, λ = 1, a flat background, one triangulation.

**Disclosed.**
- The first dry run, kept in `dry_first/`, led to the two changes above, before registration.
- The dry run's single iteration of K90z0 is the registered start 0, and it previewed it (2.1×10⁻³ after one step).
- The stopping rule was added after validation V3a–c; V3d was rerun with it.
- K90c2 was first launched by mistake as a detached process, killed within about 2 s, and its header-only log deleted before the registered launch. The step is deterministic; the check found K90c2's log consistent with this but could not verify the deleted launch.
