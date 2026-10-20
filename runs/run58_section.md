## 9zze. Run 58: a fifth grid for the far-field first law

*20 October 2026. Allen: "do as you recommend" (step 3, housekeeping). Registered and hashed before the run (`grid58/PREREG_58.md`, 15:37 UTC). An independent agent checked the run; its corrections are included.*

**Question.** Run 56 passed the far-field first law on the line, with a post hoc 9th point, and could not tell whether the miss shrinks as h or h². Does a fifth grid settle it?

**Setup.**
- Run 53's radius scan at h = ⅛: 9 points, radius about 31–33 cells.
- The outer loop is capped at 30, its count is recorded, and any point that reaches the cap is flagged.
- Simpson's rule for the first law at the middle point.
- The fit is weighted over the scan means at h = ¼, ⅕, ⅙, 1/7 and ⅛.

**Results.**

| h | ¼ | ⅕ | ⅙ | 1/7 | ⅛ |
|---|---|---|---|---|---|
| mean miss (b) | +0.0165 | +0.0118 | +0.0086 | −0.0007 | **+0.0034** |
| standard error | 0.0057 | 0.0029 | 0.0022 | 0.0015 | 0.0009 |

- Two of the nine h = ⅛ points reached the cap (f = 0.970 and 1.045, flagged as registered).
  - The check replayed f = 0.970. The composite drifts until iteration 9, when 60 surface cells switch on, then settles into a two-state cycle whose misses differ by 1.8×10⁻⁶ b.
  - Dropping both capped points moves c₀ by under 0.001 b.
- Simpson's rule at the middle point gives a first-law residual of 3.2×10⁻¹⁰.

| form | c₀ (b) | error (χ²-scaled) | χ²/dof |
|---|---|---|---|
| **c₀ + ah² (registered)** | **−0.0027** | 0.0037 | 12.4/3 |
| c₀ + ah | −0.0108 | 0.0085 | 13.4/3 |
| c₀ + ah + bh² | +0.017 | 0.048 | 11.5/2 |
| constant | +0.0037 | — | 26.9/4 |

**Verdicts, as registered.**
- **K58a PASSES.** c₀ = −0.0027 ± 0.0037 b, within the threshold of 0.01.
- **K58b is UNDECIDED.** Δχ² = +1.0 between the two forms.

**Reading** (corrected by the check).
1. **c₀ = 0 in the continuum is analytic** (Run 50's dilation argument). Five grids give c₀ = −0.003 ± 0.004 b with the h² form or −0.011 ± 0.009 b with the h form, so the form is still undecided.
2. **On the lattice the far-field first law now holds to about 0.5% of κω.** The two-form 2σ envelope is about −0.028 to +0.006 b (b ≈ 0.2). The three-term form is unconstrained. This supersedes Run 56's "about 1%".
3. **The scan means are not independent samples, and their errors understate the scatter.**
   - The spread within each scan scales as h² (sd/h² = 0.17–0.24), so each mean samples a quasi-periodic surface term over a non-integer number of periods.
   - Almost all the χ² comes from h = 1/7: dropping it leaves χ² = 0.5 for 2 degrees of freedom. The h = ⅛ mean is about 5σ above the four-grid prediction.
   - Leaving out one grid at a time gives c₀ from −0.010 to −0.002 (h²) and from −0.028 to −0.009 b (h).
4. **The discrete first law holds to ≤ 2×10⁻⁹ at every kink-free point tested** (Runs 56, 58; Simpson's rule at the h = ⅛ middle point gives 3.2×10⁻¹⁰).
