### Run 102: matter in Run 91's full constraint algebra, gravity free (a calculation, gravity sector)

*30 October 2026.*
- *Registered and hashed before the run (`modes102/PREREG_102.md`, v5, 158 files, 05:14:09 UTC; disclosed material, 210 files, hashed separately), after three independent pre-registration checks (`checkPre102/`, `checkPre102b/`, `checkPre102c/`), whose corrections were adopted, and Allen's "go". The registered text's title still reads "(DRAFT, not hashed)"; the registered version is v5.*
- *The run driver (`run_all102.sh`) is not hashed. It verifies the registered hashes and runs the registered steps in order, one process each, rerunning on exit 3.*
- *A second independent agent checked the registered run (`check102/REPORT.md`): the hashes verify, the report and mass steps rerun bitwise, K102_1's end report recomputes with no differing key, and an independently written residual code confirms the closure. Its wording points are adopted below.*

**Why.** Run 101 found matter (its M1) not to close with Run 91's gravity held fixed (K101y), and to close jointly with Run 90's gravity free (K101j). Whether Run 91's full system, field order 2 with its C and D conditions, can make room for matter was left open.

**The question, K102.** Does M1's massless scalar matter close together with Run 91's form-(b) gravity (kinetic sector with O₁ held; C and D with Z₃), with gravity's unknowns free? Four starts, in a registered order; a start closes if every held-out condition meets Run 89/91's thresholds; EXISTS needs a closing start, both controls failing as required with f_out ≥ 10⁻³ (LSMR converged), the mass channel closing, and no bug signal.

**Result: K102 EXISTS.**

| item | value |
|---|---|
| K102_1 (continuation from K101j0) | closes; stationary at the rounding floor after 6 steps (cost ratio 3.4×10⁻²⁰) |
| held-out residuals at K102_1 | non-floored max ρ 3.7×10⁻¹⁵ (MHH3); substantive ≤ 1.6×10⁻¹⁵ in every sector (kinetic, potential, matter); constraint O₁ 9.8×10⁻²⁰ |
| matter's dispersion | ω² = ω²₂s² + ω²₄s⁴ with ω²₂ = 1 to 1.1×10⁻¹⁵, \|ω²₄\| ≤ 1.7×10⁻¹⁷ (35 directions) |
| gravity's speed | c²_grav = ℓu ∈ [1 − 1.1×10⁻¹⁵, 1], free here and found equal to 1; TT rows hold to 3.4×10⁻¹⁵ |
| K102_2–4 | skipped, as registered, once K102_1 closed |
| NC-M (random term in MHH4) | fails at its cap of 8: matter-sector residual 6.3×10⁻² (kinetic 3.7×10⁻⁵, potential 2.1×10⁻⁵); f_out 0.39 |
| NC-C (random term in C5) | fails at its cap in every sector (kinetic 7.5×10⁻², potential 3.9×10⁻², matter 1.7×10⁻²), drifting \|z\| 31.8 → 208; f_out 0.77 |
| mass channel | closes (held-out 9.3×10⁻¹⁶); ÂB̂_m − 1 = 0, 0, 2.4×10⁻¹⁷ at degrees 0, 1, 2 |

**How gravity moved.** The movement from Run 91's K91b0 is 27.8, but most of it is one coupling.

| quantity | value |
|---|---|
| end − K91b0 | 27.8, of which Z₃ (the lapse coupling of the third-order energy) 26.1: \|Z₃\| 2.24 → 26.14 |
| already at the start | 30.3 (the continuation's linear solve) |
| moved by the solver | 11.4 |
| kinetic sector, end − K91b0 | 7.9 (against \|K91b0 kinetic\| = 11.3) |
| interface (L0, B0, Q), end − K91b0 | 1.47 (0.59 during the solve) |

The change to Regge's third-order energy, δT₃, is 15% of its order-a part and 3.2× its order-a² part at K102_1, against 1% and 15% at K91b0. It vanishes at constant lapse, so Regge's h³ vertex is kept and the change is all lapse-dependent. K102_1 is one member of the closing family, not a minimised change; whether a lapse coupling this large is needed is open.

**Irregularities** (no effect on any value; disclosed).
- The driver relaunched from the first step. Starts with a record did nothing (K102_1) or rewrote identical skipped records (K102_2–4). The control branch has no existing-record guard, so NC-M recomputed its end report once from its checkpoint (489 s). The check reran this in a copy: the record and its z are bitwise identical.
- The driver was then edited to skip steps with a final record (between NC-M and NC-C). The pre-edit version was not kept; the change was one line. The log line recording the edit was added by hand.
- The post-run check's own inspection wrote four stray bytecode files (three in `modes102/lib/`, one in `modes91/`); none hashed or used. They were deleted afterwards and the hashes re-verified.
- The controls' reported "c²_grav nan" is a print default for keys control records do not carry, not a computed value.

**What it means.**
- **Run 91's full gravity can make room for matter.** Matter closes on a member of Run 91's family of field-order-2 closures, and both stay relativistic. The coupling is one way at this order: no gravity condition involves matter's unknowns, so this is a new Run 91 closure plus an M1 closure on its interface, not matter sourcing gravity.
- **It extends, not contradicts, Run 101.** K101y's NOT FOUND (gravity held at K91b0) stands; Run 102 confirms Run 101's reading that it was not evidence against a joint closure.
- **The relativity is inherited.** ω²₂ = 1, ω²₄ = 0 and c²_grav = 1 follow from the imposed boost relation {H[1], H[xᵃ]} = D[e_a], as Run 101 found; CO does not derive Lorentz invariance here.

**What it does not show.** Field order 3; uniqueness or a minimal change (one solution from one start); forms (c) and (u), or O₁ free; (D) with Run 88's ν; anything beyond the formal origin of momentum space, a flat background and one triangulation; Run 101's null-space check (E4) at K102_1. Everything is conditional on M1, a candidate.
