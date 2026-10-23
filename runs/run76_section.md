## Run 76: does the negative-curvature design-2 cell replicate?

*21–22 October 2026. This is the replication recommended by Run 75's check. It was registered and hashed before any run (`rep76/PREREG_76.md`, 21:37:16 UTC), with the baseline fixed beforehand (`baseline76.json`).*
- *The registration's header time was corrected and the files re-hashed 5 s after a first hash, before any run.*
- *An independent agent checked the run (below).*

**Question.** On Run 72's negative-curvature lattice (s = −1), the zero-range theory's error for design 2 was −0.06 ± 0.17% (seeds 201–220). On the four other lattices tested it is +0.63 ± 0.14%.
- That deviation was about 2.5σ after correcting for having been picked out.
- It had weakened from Run 72's seeds to Run 72b's.
- Run 75 showed it does not come from the clocks' outer links.

Does it replicate with fresh seeds?

**Design.** Run 72's engine and lattice, unchanged (s = −1, λ = 0.25, high medium, p_s = 1, Run 24's 216 clocks). There are 40 fresh seeds, 221–260. For design j, the theory's error is
$$
\text{off}_j=\frac{\overline{\text{dip}}_j}{\text{dip}^{\rm theory}_j}-1,\qquad \Delta=\text{off}_2^{\,s=-1}(\text{seeds }221\text{–}260)-\text{off}_2^{\rm base},\qquad \text{off}_2^{\rm base}=+0.632\pm0.142\% .
$$
- **K76a REPLICATES** if Δ ≤ −3σ.
- **DOES NOT REPLICATE** if Δ ≥ −1σ.
- **UNDECIDED** otherwise.

**Results** (conservation exact in every run).

| s = −1 seeds | design-2 error | Δ from baseline | design-1 error |
|---|---|---|---|
| 201–220 (Runs 72, 72b; where the cell was found) | −0.06 ± 0.17% | −0.69 ± 0.22% | +0.16 ± 0.10% |
| **221–260 (Run 76, registered)** | **+0.26 ± 0.16%** | **−0.37 ± 0.22% (−1.7σ)** | +0.22 ± 0.06% |
| all 60 (reported) | +0.15 ± 0.12% | −0.48 ± 0.19% (−2.5σ) | +0.20 ± 0.05% |

- **The scatter was larger than planned, but normal.** The new seeds' standard error came out at 0.16%, against an expected 0.12%.
  - The plan had taken its figure from seeds 201–220, whose scatter was unusually small (0.75% per seed, p = 0.03).
  - The new seeds scatter like every other lattice: 1.03% per seed, against 1.00–1.43% elsewhere (the check).
- **Design 1 shows no deviation:** Δ = −0.05 ± 0.07% on the new seeds.

![Run 76](figures/76_replication.png)

**Verdict.**
- **K76a is UNDECIDED.** The fresh seeds put the cell at −0.37 ± 0.22% from the baseline: about half the deviation that first drew attention, at 1.7σ.
- It neither clears the 3σ bar nor sits within 1σ of the baseline.

**What the check added.**

1. **Independent reproduction.** Every number was reproduced from the run files, the baseline included, and the verdict logic matches the registration.
   - All 40 runs post-date the hash, use the registered parameters and conserve exactly.
   - No output duplicates an earlier run, and no seed overlaps an earlier run's.
2. **Power was overstated in the registration.** With a realistic σ (0.23%), the chance of REPLICATES was:
   - about 0.48 if the first deviation was real at full size;
   - 0.17 at −0.48%;
   - 0.08 at −0.37%.
   The 0.84 chance of DOES NOT REPLICATE under no effect was right.
3. **The seed blocks show no steady trend.**

| s = −1 seeds | Δ from baseline |
|---|---|
| 201–210 | −0.89 ± 0.27% |
| 211–220 | −0.49 ± 0.28% |
| 221–240 | −0.14 ± 0.29% |
| 241–260 | −0.61 ± 0.25% |

   - The blocks agree with each other (p = 0.16). The "weakening" from 201–210 to 211–220 does not continue.
   - The discovery seeds and the fresh seeds differ by −0.32 ± 0.23% (1.4σ). That fits a discovery inflated by selection, but noise explains it too.
4. **The combined evidence stays under 3σ.**
   - The look-elsewhere-corrected discovery combined with the replication gives 1.8–2.7σ, depending on how the discovery's scatter is estimated.
   - With the scatter pooled over all lattices, Run 75's "about 2.5σ" falls to about 1.4–1.75σ.
   - From the replication alone, the likelihood ratio of the best-fitting shift (−0.37%) against zero is 4.4. For the full first size (−0.69%) against zero it is 1.5.
5. **How big a lattice-dependent piece could be.**
   - The fresh seeds place the s = −1 shift between −0.80% and +0.05% (95%).
   - The spread of the design-2 error between lattices is at most about 0.75% (95%).
   - For design 1 it is under 0.17%.
6. **What a 3σ answer would cost.** For a −0.37% shift, about 230 more runs (about 125 on s = −1 and 105 on baseline lattices) for an even chance, and about 440 for 80% power. That is 11–22 hours.
   - More s = −1 seeds alone cannot get there, because the baseline's ±0.14% already exceeds the 0.12% required.
7. **The theory's error has a sign.** All ten per-lattice errors (five lattices, two designs) are positive, so the theory slightly underestimates the dips.

**Reading.**
1. **The negative-curvature cell is not established.** In fresh data it sits 0.37 ± 0.22% below the other lattices: half its first size, and not significant. A lattice-dependent part of the theory's design-2 error is neither shown nor excluded; the fresh seeds allow up to about 0.8%.
2. **The zero-range theory slightly underestimates the clocks' own dips** (high medium, p_s = 1, five lattices: flat, s = ±1, a = e^±1):
   - design 1: by 0.25 ± 0.03%;
   - design 2: by 0.63 ± 0.14% on the four baseline lattices, or 0.47 ± 0.11% with the s = −1 replication included.
   Within errors the underestimate is the same on every lattice, and each single lattice's design-2 error is known only to ±0.16–0.64%. In absolute terms it is about 0.1 points of occupancy, on dips of about 18–29% of ambient.
3. **The line is closed here** unless a later result depends on it. A 3σ answer would take 230–440 more runs (11–22 hours, the check). The question is about the theory's last fraction of a percent, at curvatures far larger than any physical one: Run 70's check scales the design-dependent effect to about 10⁻³⁹ for a neutron star.
4. **For future replications,** plan σ from the scatter pooled across lattices, not from the discovery cell's own scatter (the check).
