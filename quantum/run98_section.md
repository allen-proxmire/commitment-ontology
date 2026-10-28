### Run 98: candidate C4, saturation as route (c) (a calculation, quantum runs)

*28 October 2026.*
- *Registered and hashed before the run (`quantum98/PREREG_98.md`, 12 files, 17:22:17 UTC), after a check of the statement (`checkC4b/`) and two independent pre-registration checks (`checkPre98/`, `checkPre98b/`), whose corrections were adopted, and Allen's "go".*
- *Validated beforehand (V1–V11, all PASS).*
- *Not blind: the checks' feasibility estimates showed room for a survivor before hashing. The registration fixes the method.*
- *A second independent agent checked the registered run (`check98/REPORT.md`): the hashes verify, a full re-run reproduces the log byte for byte, its own code for every bound agrees to 1.1×10⁻³ at 15 spot points, and its full scan reproduces every count. Its wording points are adopted below.*

**Why.** Reading I8 found that Allen's "saturation" (a pattern can hold only so much) is the one open direction for commitment by internal complexity, and that it needs a primitive CO lacks: a capacity per place. It was ruled to be added and tested (`reading_I8_C4b_statement.md`).

**The candidates.**
- **C4-β′, the hold's ceiling** (no new primitive): a unit commits at once if its stock reaches one hold,
$$
q\ge H=2\hbar_tP_\infty\iff E\gtrsim\frac{aP_\infty\hbar c}{\ell}.
$$
- **C4-β, route (c)** (new primitive ρ_K, rate Γ_K): where the mass density smoothed at r_C passes ρ_K, a linear channel opens,
$$
\frac{d\rho}{dt}\Big|_K=\Gamma_K\!\int\!\frac{d^3x}{V_c}\Big(\hat\Pi_{\mathbf x}\rho\hat\Pi_{\mathbf x}-\tfrac12\{\hat\Pi_{\mathbf x}^2,\rho\}\Big),\qquad \hat\Pi_{\mathbf x}=S\!\Big(\frac{\hat\varrho(\mathbf x)-\rho_K}{\rho_K/10}+\tfrac12\Big),
$$
  with S(s) = 3s² − 2s³ and V_c = (2πr_C²)^{3/2}. It is silent below threshold and inside a saturated bulk, and acts at threshold surfaces. Its signature is an onset in size at fixed density: a sphere of density ρ_b saturates at R_K/r_C = χ₃⁻¹(ρ_K/ρ_b) (0.764, 1.538 and 2.500 at ρ_K/ρ_b = 0.1, 0.5 and 0.9, for any material).

**The test.** A point (r_C, ρ_K) survives if a cell at ρ_K holds at least 10 nucleons (N_cell = ρ_KV_c/m_N ≥ 10, so an onset in size exists), some bound applies, and every bound allows Γ_K ≥ 10·λN_cell, where
$$
\lambda N_{\rm cell}=\kappa_bc^2\rho_KV_c/\hbar
$$
is route (b) summed over one cell, at the floor κ_b = 5.62×10⁻³⁶. Bounds: LISA Pathfinder's test-mass noise, Earth's heat (PREM), the Sun, a white dwarf, interference (172 kDa clusters, Rb atoms). Grid: 25 r_C across Run 96's window × 421 ρ_K from 10⁻³⁰ to 10¹² kg m⁻³.

**Result.**
- **C4-β′: INERT.** The threshold is 10⁵²–10⁶³ eV (10⁴³–10⁵⁴ nucleon rest energies) at every aP∞ and both hops.
- **K98, C4-β: LEAD AT LABORATORY DENSITIES** (no power; two free parameters).

| quantity | value |
|---|---|
| tested points (N_cell ≥ 10, a bound applies) | 4580 |
| survivors | 4580 (all); 3580 with ρ_K ≤ 2.26×10⁴ kg m⁻³; 4567 also at κ_top; all at the ×30 and ×70 onset factors |
| survivors' ρ_K | 1.0×10⁻¹⁴ to 2.5×10⁹ kg m⁻³ |
| margin Γ_max/(10λN_cell) | 3.4×10⁷ to 3.2×10³³ |
| binding bounds (laboratory survivors) | LISA 2465, interference 1058, Earth 32, the Sun 25 |

- **Inside the tested region the scan could not discriminate,** as the registration expected.
- **What "lead at laboratory densities" means.** Γ_K anywhere between 10λN_cell and Γ_max is allowed. At Γ_K = 10λN_cell the effect lies below present sensitivity by the margin:

| region | smallest margin | where | set by |
|---|---|---|---|
| all ρ_K ≤ osmium | 3.4×10⁷ | ρ_K ≈ 8×10⁻³ kg m⁻³, lowest r_C | 172 kDa cluster interferometry |
| solids and liquids (10³–1.98×10⁴) | 1.0×10⁹ | ρ_K = 5×10³, lowest r_C | Earth's heat (lower mantle) |
| same, laboratory bound alone | 1.2×10¹² to 6.7×10¹⁴ | ρ_K = 10⁴ | LISA Pathfinder |

  It is not a laboratory signature. Reaching the onset rate would take superpositions of bodies of about 10⁻¹⁶ kg or more held for about a second (at the smallest r_C), resolving the jump with size, since route (b) also decoheres them.
- **The hold's ceiling as the rate,** Γ_K = c/ℓ (1.85×10⁴³ s⁻¹ P08, 2.88×10⁴⁰ s⁻¹ engine), is allowed only where a single stellar luminosity is the only bound:
  - the white dwarf, at ρ_K ≥ 10⁶ kg m⁻³ and r_C ≥ 1.8×10⁻⁵ m (P08, 98 points) or ≥ 8×10⁻⁶ m (engine, 205 points);
  - for the engine, also the Sun, at 2–6×10⁴ kg m⁻³ and r_C ≥ 3.9×10⁻⁵ m (9 points). One of them, ρ_K = 1.995×10⁴, is an artefact of coverage: it lies just above LISA's test-mass density, where no laboratory bound is registered.

  The reason is in the model: one particle's share of the smoothed density is tiny next to δρ in dense matter, so smooth stellar gradients barely register. Wherever a laboratory bound applies, the ceiling is excluded by at least 16 decades. Unregistered bounds (cooler or heavier white dwarfs, the real solar core, giant planets) could close these points.

**Untested.**
- The per-particle regime, N_cell < 10 (5020 grid points), where every particle saturates on its own.
- ρ_K from 7.64×10⁴ to 10⁶ kg m⁻³, and above 2.59×10⁹.
- 1.98×10⁴ to 7.64×10⁴ kg m⁻³ is tested only by the Sun.
- The cut N_cell ≥ 10 still lets an atom of mass number A saturate alone when N_cell < A: 344 laboratory survivors have N_cell < 238, and the 1.6×10⁸ margin plateau at r_C ≳ 6×10⁻⁷ m comes from Rb atoms.
- `run98.json` keeps 2000 of the 4580 survivors and no grid; the check's `scan_indep.json` has the full grid.

**Gravity (open).** Saturation commitments are ruled records that deposit. Whether they smooth or roughen gravity's graininess, and so whether Run 96's floor (used here as the comparison κ_b) still holds, is not computed.

**What it means.**
- **The record's own capacity-type quantity, the hold, does nothing** as a threshold (C4-β′).
- **A new capacity primitive gives a consequence the GRW-type models lack**, an onset in size at fixed density that differs between materials, and it survives every registered bound. It survives because ρ_K and Γ_K are free: the allowed Γ_K spans 7 to 33 decades. It is a lead, not a result, until something in CO fixes ρ_K or Γ_K.
