# I1 result: induced light, first rung (14 Nov 2026)

| θ | Z_E | Z_B | c_ind (hops/step) | c_ind/c₀ − 1 | fit residual (B, E) | status |
|---|---|---|---|---|---|---|
| 0.3 | −0.0356 | −0.0344 | 0.984 | −11.5% | 0.2%, 0.004% | valid |
| 0.5 | −0.0891 | −0.0738 | 0.910 | −18.1% | 0.06%, 0.009% | valid |
| 0.8 | −0.239 | −0.216 | 0.951 | −14.4% | 6.0%, 0.4% | invalid (fit residual > 1%) |

**Outcome as registered: unequal.** Induced light runs 11–18% below c₀ at the two valid masses.

**Not expected: both Z negative.** A static magnetic field lowers the walk's vacuum energy and a static potential raises it, the reverse of a Dirac sea (where second-order perturbation of a ground state by a potential always lowers it). So at these masses the induced Maxwell term has the wrong overall sign. The likely cause is the Floquet vacuum: the walk's bands span most of (−π, π) (π-gap ≈ 0.5), so the field enters the effective Hamiltonian i log U with large second-order (time-step) corrections, and couplings across the π-gap and the heavy extra species contribute at order one. The light species' contribution, which carries the expected sign and Lorentz-invariant speed c₀, grows only as ln(1/θ), and at θ = 0.3–0.8 that log is about 1. |Z| falls as θ falls (0.24 → 0.089 → 0.036), consistent with a positive log term eating into a negative lattice-scale term, but these masses cannot show a sign change.

**What this does and does not say.** At lattice-scale masses, CO's walk with the posited vacuum induces a wrong-sign field and a slow induced light. It says nothing yet about physical masses (θ ≈ 10⁻²³, ln(1/θ) ≈ 53), where the leading log should dominate. The static q⁴ coefficients (c₄/c₂) are fit-sensitive and are not light's bending (frequency terms not computed).

**Next rung.** Reach small θ (q ≪ θ ≪ 1) by computing the response in momentum space (second-order coupling of k to k ± q only), so Nx no longer limits q; then Z(θ) against ln(1/θ): sign change, slope against the leading-log value, and c_ind → c₀.
