# B3b: registration (15 Nov 2026, after B3, before this run)

**B3 as registered.** F1 PASS (ε = 0: m = 3.2×10⁻³ … 4.7×10⁻⁶ for L = 8 … 24, slope −0.41 per place, R² = 0.9995). F2 FAIL: at ε = 0.2 the coherent disturbance falls cleanly (slope −0.19, R² = 0.9996), but the random draws fall unevenly (R² 0.43–0.98; one draw rises at L = 24). All m(24) are below 1% of the control's leak (1.7×10⁻³ against 0.168), which is the protection's signature in size, but the registered straight-line condition failed.

**Design error.** The disturbance's strength was copied from B2 without scaling to this step's bulk gap. Per tick, the flow's bulk gap is τM = 0.2 rad, so ε = 0.2 rad per tick equals the gap (on the palindrome the gap was 0.5 and ε/gap = 0.4). A disturbance as large as the gap can close it locally, and the sub-gap window (|E| < 0.1) then admits bulk levels, which explains the uneven falls. B3 stays recorded as failed.

**This check.** Same as B3 with ε = 0.08 (ε/gap = 0.4, as in B2), same seed and draws, same conditions: F2 fails if any case's log m against L is not a falling line (slope > −0.1 or R² < 0.98) or m(24) exceeds 1% of the control's leak at the same ε.
