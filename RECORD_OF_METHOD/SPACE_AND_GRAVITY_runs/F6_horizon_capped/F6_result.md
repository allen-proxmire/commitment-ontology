# F6: the 1D horizon runs with the drift inside the tick limit (21 Nov 2026)

F1e–h set the drift to √(400/6) = 8.16 near the centre, above the 1D tick limit (6.43 at m = 0.5, τ_f = 0.4) for ρ < 10. Here the same scripts run with one change: the drift capped at 4 (reached at ρ = 25, inside the absorber's ρ < 30).

| run | F1 (drift to 8.16) | F6 (drift capped at 4) |
|---|---|---|
| f1e, mean at target 400 | −0.0038 of the distance fallen | −0.0040 |
| f1f, median at target 199.7 / 119.7 | +0.0203 / +0.0549 | +0.0203 / +0.0540 |
| f1g, median at 199.7 / 119.7 | +0.0063 / +0.0114 | +0.0063 / +0.0123 |
| f1h, lag at 199.7 / 119.7 | +6.3 / +12.3 places | +6.3 / +13.3 places |
| recount with absorbed weight at the centre (f1g_diag_inner), median at 199.7 / 119.7 | +0.0003 / +0.0003 | −0.0007 / −0.0006 |

**Reading.** With the drift inside the tick limit everywhere, the fall through the horizon (r_s = 400) stays on the free-faller's path: the recounted median is within 0.07% of the distance fallen at 0.5 r_s and 0.3 r_s (0.03% with the uncapped drift). The earlier runs' excursion above the limit did not carry the result.
