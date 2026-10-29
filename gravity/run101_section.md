### Run 101: a matter field in the lattice constraint algebra (a calculation, gravity sector)

*29 October 2026.*
- *Registered and hashed before the run (`modes101/PREREG_101.md`, 35 files, 16:31:35 UTC; disclosed material, 128 files, hashed separately), after two independent pre-registration checks (`checkPre101/`, `checkPre101b/`), whose corrections were adopted, and Allen's "go".*
- *The run script (`run_all101.sh`) is not hashed. It verifies the registered hashes first and then runs the registered steps in the registered order, one process per step.*
- *A second independent agent checked the registered run (`check101/REPORT.md`): the hashes verify, and the re-run steps (K101y0–2, K101j0, K101e0, K101n0 and the report) reproduce bitwise. Its wording points are adopted below.*

**Why.** Reading I11 (ruled) found that a plain lattice term for patterns is excluded by data, and asked whether the record's own closure conditions force matter to be relativistic on the lattice, as Run 90 found for gravitational waves.

**The new statement, M1** (graded lead). A scalar pattern field ψ and its momentum sit on the same places as gravity. H and D are sums of a gravity part and a ψ part, sharing one set of structure functions. R6 is the flat, stationary limit of this. Everything below is conditional on M1.

**What the algebra decides in advance (a restatement, not a derivation).** Three slices of the matter conditions settle the dispersion exactly, for any closure:
1. {H, D} at zero metric momentum forces the matter shift generator to be σ(s) = iℓs, and the lapse change under a constant shift to be linear, L0(k, 0) = iℓk.
2. {H, H} at k₁ = 0 then gives
$$
\omega^2=\ell u\,s^2,
$$
   with u the linear coefficient of the {H, H} structure function at constant lapse. That is gravity's own speed, so ω²₄ ≡ 0 at every kept degree.
3. The mass channel gives ÂB̂_m ≡ 1, so the mass term has no momentum dependence. This step is argued; the mass set was not solved.

This is the Poincaré relation, [K, H] = P, imposed through the boost relation {H[1], H[xᵃ]} = D[e_a] (the hypersurface-deformation result; literature citations not re-verified). **CO does not derive Lorentz invariance here: it inherits it from the boost relation it already borrows.** A solver-independent certificate built from these slices bounds |ω²₄ − t| for the relativistic, nearest-neighbour and isotropic targets at every end point.

**The registered questions.**
- **K101y (primary):** does matter close with gravity's structure functions held at Run 91's K91b0, the record's full field-order-2 closure?
- **K101j:** does matter close jointly with Run 90's form-(iii) gravity left free?

**Result.**

| rule | gravity | reading | detail |
|---|---|---|---|
| **K101y** | Run 91's K91b0, held | **NOT FOUND** | three starts, each stopped at the iteration cap; substantive residuals 1.2–4.0×10⁻³ (the {H, H}/{H, D} clash in MHH4 and MHDq) |
| K101z | Run 90's K90z0, held | NOT FOUND | three starts |
| **K101j** | Run 90's form (iii), free | **EXISTS (certified: E1–E5)** | non-floored residual 1.1×10⁻¹³; ω²₂ = 1 and ω²₄ = 0 to 10⁻¹⁶; null-space gap 5.6×10¹¹; gravity's TT dispersion stays Run 90's relativistic one (row distance 4×10⁻¹⁵); gravity moves 0.71 from K90z0 |
| K101e | spatial conditions only, with an isotropic s⁴ target | EXISTS | without {H, H} an isotropic s⁴ term is admitted, so ω²₄ ≡ 0 in K101j comes from the boost relation |
| K101f | spatial conditions only, nearest-neighbour target | NOT FOUND | soft target; reported only |
| K101n | without the Σ1 shift freedom | NOT FOUND | total failure at leading degree; Σ1 is needed to absorb the part of gravity's B0 that is a basis choice |

- **How strong K101y's NOT FOUND is.** It is valid by the registered rule, but not a certificate. The system is bilinear, so the Run 88-type linear certificate is not available.
  - Post hoc (not registered), a damped solve from start 2's end reaches a near-stationary point (stationarity 4×10⁻⁵) with its substantive residual unchanged, 1.2×10⁻³.
  - From start 0 it halves the cost and leaves the residual at 2.0×10⁻³, 20× the threshold.
  - Most of the residual lies outside the Jacobian's range.
- **The contrast is held against free, not Run 91 against Run 90.** Matter also fails on Run 90's gravity held fixed (K101z), and closes once that gravity is freed (K101j). So K101y's failure repeats the held-gravity pattern, and is not evidence against a joint closure with Run 91's full system.
- **The guard control** (NC101y) did not run, as registered, because K101y did not close.

**Part F, the finite-range residual** (reported). On a finite-range lattice the algebra closes only to an order set by the stencil range; the residual is the order at which closure fails, not a prediction.
- At the minimal range with R6's ultralocal kinetic term, the a⁴ residual is −s⁶/90 along the axes (subluminal) and −s⁶/360 along (1, −1, 0).
- It is free along the diagonals, and free in every direction for a non-ultralocal kinetic term.
- Removing it becomes possible at range 3.
- Its sign is a property of the stencil chosen, not of CO.

**What it means.**
- **Relativity for matter on the lattice follows from the borrowed boost relation,** not from CO's primitives.
- **CO's standing gravity cannot simply have matter added with gravity held fixed** (not found from three starts). With Run 90's gravity free, matter and gravity close together and both stay relativistic.
- **Whether Run 91's full gravity can make room for matter is open:** the joint closure in Run 91's full system (Run 102, planned).
