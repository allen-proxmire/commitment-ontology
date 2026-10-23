## Note C: ED's black-hole radiation papers under option A and "the core commits" (a reading)

*19 October 2026. (step 2: look at re-emission in the papers). An agent read the papers, the Attempt B cards, the derivation attempts and the 12 September review. A second, independent agent checked the quotes and numbers; its corrections are included.*

**Question.** It was ruled that the core commits what reaches it, and a commitment is never undone. ED's radiation papers (039, 047, 047_5, 050, 052) say black holes radiate. Do the two fit together, and does either give a signal that differs from GR?

**What the papers say.**

| paper | claim | how radiation or information leaves | formulas | what it assumes |
|---|---|---|---|---|
| 039 Horizon decoupling | the horizon is a decoupling surface, where cross-bandwidth Γ_cross → 0 | correlations at the surface turn thermal (KMS); "committed information cannot cross the substrate-level decoupling surface" (§3.4); entanglement set up before the horizon formed "straddles" it (§3.5) | $T_H=\hbar\kappa/2\pi k_B c$; $dM/dt\sim-\hbar c^4/G^2M^2$; Planck remnant $M_\star=M_P$; $n_{\rm ED}=n_{\rm Planck}[1-c_1(\omega/\omega_c)^2]$, $\omega_c=c/\ell_P$, c₁ = ½–1 | r_H and κ are GR's ("not derived independently", §3.2); no anti-evaporation (P11, V1) |
| 042 No singularity | a cumulative bound $C_{\rm cum}(r)\le C_{\max}\sim(r/\ell_P)^3$ | silent | — | the bound is posited (its derivation was attempted and failed); C_cum grows monotonically |
| 047 Hawking spectrum | Planck spectrum at T_H, with the (ω/ω_c)² correction | as 039 | $n=1/(e^{\hbar\omega/k_BT_H}-1)$ | κ inherited from GR (Kerr: from M, J) |
| 047_5 Universalization | T = ħκ/2πk_Bc for every horizon (Rindler, de Sitter, acoustic) | — | Unruh, Gibbons–Hawking, acoustic κ | the same formula applied to each case; the review notes the acoustic case "has no testable content" |
| 050 Page curve | entanglement rises, then falls after the Page time | two postulates (P-V5-EntBudget, P-Re-routing) re-route information into the radiation | $S\approx(dS/dt)_H\,t$, $(dS/dt)_H\sim c^3/GM$; t_Page ≈ 0.54 τ_BH (inherited) | the postulates |
| 052 Paradox synthesis | the paradox "is not generated" (a framing its own claim table says was softened, to "supplies a mechanism for unitarity-preserving evolution") | infall → straddles the surface → re-routed into radiation → residue in the Planck remnant | — | "No claim that this paper supplies novel empirical predictions beyond Papers 039/047/050" |
| 052_5 Merger lag | a delay between GR's merger time and the substrate's | not about radiation | $\tau=\tau_{V5}+\tau_{\rm mob}+\tau_{\rm cascade}$ | predicts existence only; τ_V5 open; as written $\tau_{\rm mob}\sim\int|\nabla\mu|^2/\mu^2\,dt/c^2$ has units s³/m⁴, not seconds |

**Status.**
- The review notes added to the papers on 12 September say:
  - 039: "The 'decoupling surface' is a relabeling. It is placed at the GR horizon (§3.2, as the paper says), and Γ_cross → 0 there is asserted, not computed."
  - 047: "κ and the horizon location are borrowed from GR, and the periodicity is the standard Euclidean one."
- `STATE_OF_THE_ONTOLOGY.md` says: "The accounts of horizons, Hawking radiation… are readings. None has been tested and none adds content."
- Nothing is withdrawn.

**Reading.**
1. **The papers fit "the core commits".** Their radiation comes from correlations at the surface, not from anything released by the interior, and 039 already says committed information cannot cross.
   - Under option A the exterior is Kerr, so the number they need is there: $\kappa=(r_+-r_-)/2(r_+^2+a^2)$, borrowed from GR, as the papers say.
   - **But a number in the metric is not emission.** Under option A the core sits where the horizon would be, and Run 43 placed its surface just outside r₊.
     - Steady emission at $T_H=\hbar\kappa/2\pi k_Bc$ needs a horizon, or a surface that puts quantum fields in a horizon's state.
     - A static surface without a horizon does not radiate. That was Run 32's zero-temperature point.
   - **Assumed, not derived: the committing core acts on quantum fields as a horizon would.** Without that assumption, ED's black holes do not radiate at all.
2. **The ruling meets the bound that ended Attempt 03's line, by input and rule. It does not reopen that line.**
   - Attempt 03 (C31–C34) found that a shallow, capped core releases 63% of what falls on it as heat. Even the kindest count, the 10% that escapes on first emission, is about 25 times what Sgr A* allows. Its verdict: "ED's strong-field line is closed under its exit rule (RD6, C33)".
   - Under option A plus "the core commits", nothing is re-emitted except Hawking radiation, if that is assumed. For Sgr A* (4.3×10⁶ M☉) that is at about 1.4×10⁻¹⁴ K, so the bound is met.
   - Option A replaces ED's own strong field rather than repairing it, so Attempt 03's verdict on that field stands.
3. **No ED-specific signal.** Hawking radiation from astrophysical black holes is far too faint to see. GW250114's remnant would sit at about 8×10⁻¹⁰ K, and a solar mass at 6.2×10⁻⁸ K. The paths to a difference all fail:
   - **The (ω/ω_c)² correction** scales as (M_P/M)², about 10⁻⁷⁶ for a solar mass, with c₁ unfixed.
   - **The Planck remnant** matters only for primordial black holes.
   - **The Page time** is inherited.
   - **The merger lag (052_5)** predicts only that a lag exists, and is not a signal of the core. It should not be cited as one until its τ_V5 and units are fixed.
4. **One question needs a ruling: do ED's black holes evaporate?** 039 has the black hole lose mass ($dM/dt<0$). 042 has the core's record only grow, and the ruling makes it permanent. Two readings are consistent with the ruling:
   - **(a) Yes, they evaporate.** This needs two assumptions:
     - the committing core acts on quantum fields as a horizon would (item 1);
     - the pull, which in the engine is the core's ticking (Run 30), can be lowered by emission at the surface while the record stays. Run 30 allows this but does not supply a mechanism, and the engine has none yet.
     
     This keeps 039 and 047. If 050's postulates are also adopted, they return the same information to the radiation that the record keeps. That counts it twice, unless the record is classical.
   - **(b) No, they never evaporate.** Nothing lowers the core's pull, and no new mechanism is needed. 039, 047 and 050 do not apply to black holes under option A.
   - **The two differ observably only for small primordial black holes.** Bounds on those from the gamma-ray background assume they evaporate.
   - **This needs a ruling.**

   **Ruled (19 October): black holes evaporate.** That is reading (a). Its two assumptions are now tracked:
   - the committing core acts on quantum fields as a horizon would;
   - its pull (its ticking) drops by emission at the surface, while its record stays.

   **The framing (19 October): "the precise way to say it is near-max commitment… max commitment is probably an unreachable limit."** A black hole is a core at near-maximum commitment, not a singularity.
   - This matches the engine: a body's draw throttles itself, so its clock slows but never stops (Run 32; Attempt B: "approaching but never reaching zero return").
   - It also matches Run 43, where the core's surface sits at a small, nonzero clock rate.
   - Strictly, then, there is no true horizon, only a surface very near where one would be. The two working assumptions apply to that surface: it absorbs everything (no echoes), and it radiates as a horizon would.

   **The endpoint is not ruled.** Paper 039's Planck-mass remnant ($M_\star=M_P\approx2.18\times10^{-8}$ kg) came from an earlier session. Full evaporation is favoured as simpler, without committing to it.
   - **The question both endpoints share** is whether the radiation carries out the information about what fell in. Paper 050 says it does, through correlations (the Page curve), by two postulates. That is open in mainstream physics too: the black-hole information problem.
   - **A Planck-mass remnant** must hold whatever the radiation does not carry out. If the radiation were purely thermal, that would be everything that ever fell in, an unbounded amount in a Planck mass: the known problem with remnants. If 050 holds, the remnant need hold only a residue (052).
   - **Full evaporation** has no leftover object to fill. "Kept as record" then means kept in the history (the commitments happened), which is what the record already is in ED.
   - **The record and the pull.** In the engine, what pulls is matter present now times its clock rate (Run 30), not the history of commitments. So the mass can be radiated away while the record of past commitments stands. This is how the engine already works, not a new problem.
5. **Also open:**
   - Information from matter that falls in after the horizon forms. 039's straddling covers only what was entangled before. Under "the core commits" that information is kept as record, not lost, but it reaches the radiation only through 050's postulates.
   - The units in 052_5.
