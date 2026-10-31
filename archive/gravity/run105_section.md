### Run 105: Run 104 at p_c = 1 with eight seeds (a registered calculation, gravity sector)

*31 October 2026 (registered 01:10:55 UTC; 30 October local).*
- *Registered and hashed before the run (`modes105/PREREG_105.md`). It uses Run 104's code, predictions, thresholds and reading labels unchanged.*
- *No independent pre-check, under the lean protocol (disclosed).*
- *One post-run check (`check105/`) found no errors. The hashes verify, every output postdates the stamp, the analysis reruns byte for byte, and an independent recompute from the 16 outputs reproduces every number.*

**Why.** Run 104 read UNRESOLVED, and the p_c = 1 discrimination needed more seeds. Seeds 3–8 were added at p_c = 1 (high and low media), and seeds 1–2 are Run 104's outputs.

**Result: THROUGH B.**
- **The gap at p_c = 1** is 0.0697 ± 0.0023 over 8 seeds. The spread between seeds gives 0.0025, which agrees with the probe bootstrap.
- **THROUGH B fits:** χ²_B = 4.56.
- **THROUGH p is excluded:** χ²_p = 16.11, driven by p_c = 1, where z_p = +3.42. Without that point χ²_p would be 4.45.
- **The gap lies between the predictions:** t = 0.56 ± 0.18 (0 for THROUGH p, 1 for THROUGH B), and z_B = −1.68 at p_c = 1. B fits because its extrapolated prediction carries the larger error (σ_B = 0.0061, against σ_m = 0.0023), not because the gap matches it.
- **Cb's own fit** (inference): slope −0.807 ± 0.052, reaching gap 10⁻⁶ at p_c ≈ 1.0×10⁶ (1σ 4.2×10⁵–2.4×10⁶). The slope is 0.5σ from THROUGH p's −0.85 and 2.0σ from THROUGH B's −1.00.

**Disclosed.**
- The seeds were added after Run 104's UNRESOLVED, which leaned towards B. The registration's planning power had said a gap held at 0.0692 would read THROUGH B, so the registered 1% false-exclusion rate does not strictly hold for this two-stage design.
- Seeds 3–8 alone give the same reading: g = 0.0698 ± 0.0025, χ²_p = 15.44, χ²_B = 4.42.

**What it means** (PREREG_105 §5).
- **The carried-over clock floor from Runs 23–24** is 8×10⁴ (through B, stated in c/0.99; 1σ 3.6×10⁴–1.9×10⁵). The 4×10⁵ figure lapses.
- **Cb's own bound of about 1.0×10⁶** lies above it. That bound measures something different and is kept separately: PREREG_104 §7 expected about 8×10⁴ under THROUGH B, and the two 1σ ranges do not overlap.
- **Every figure is graded inference.** Each is conditional on Reading I6 ruling 4 (physical clocks do not dip themselves) and holds in the large-dip regime only (PREREG_104 §12).
- **More seeds will not sharpen this.** The limit is now the error on the B prediction, which comes from Run 24.
