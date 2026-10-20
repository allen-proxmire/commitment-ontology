## 9z. Run 33: does a pattern's energy pull? (a decision memo; no run)

*19 October 2026. Allen: "do the recommended steps" (step 3: give a pattern a cadence on the event layer and measure whether it pulls by ħω). A search of the three repos found no existing ED rule that turns a pattern's energy into draw. By Allen's own rule (ED_Attempt_04, `Picture.md`: "The counting rule is fixed … **before** any weights are computed"), the rule has to be chosen first. This memo sets out the candidates and what each one gives, for that choice. Nothing is run.*

**What is measured.** Energy in every form pulls with the same weight as rest mass.
- **Binding energy.**
  - Nuclei and atoms weigh less than their parts by their binding energy: $\Delta m=E/c^2$ is confirmed to 4×10⁻⁷ (Rainville et al. 2005).
  - That mass falls like any other: titanium and platinum agree to 10⁻¹⁵ (MICROSCOPE), and their binding fractions differ by about 10⁻³.
  - It pulls like any other: the Moon's aluminium crust and iron mantle agree to 4×10⁻¹² (Bartlett & van Buren 1986).
  - About 99% of a proton's mass is the energy of its quark–gluon pattern.
- **Radiation.** Radiation gravitates. The expansion rate in the radiation era, read from primordial nucleosynthesis and the CMB, counts photons and neutrinos at full weight: $N_{\rm eff}=2.99\pm0.17$ (Planck 2018).
  - In GR that rate is set by the energy density through the Friedmann constraint.
  - A theory whose expansion is driven by the active mass, $\ddot a/a=-\tfrac{4\pi G}{3}(\rho+3p)$, needs radiation's pressure weight too. With energy alone and $\rho\propto a^{-4}$, it gets $H^2=\tfrac{4\pi G}{3}\rho$, half of GR's.
- **GR's requirement, in engine terms.** The active source of static or slowly moving matter is $(T^{00}+T^{ii})$ weighted by the local clock rate (Tolman, Komar). That is:
  - rest mass with weight 1, which is Run 30's result
  - internal and binding energy with weight 1
  - momentum flux (pressure, and a moving body's $\rho v^2$) with weight 1 per direction

**What the record says** (all quoted from the repos).

| file | says | status |
|---|---|---|
| Attempt C `RULES.md`, DSR-4 (2026-10-05) | "mass is a frequency of becoming (E = ħω), so greater mass is a higher duty cycle" | ruled; "true by construction" |
| `Paper_MassWithoutMass_BindingInertia.md` (July 2026) | "the commitment rate and mass are different phenomena… mass is a separate thing that comes from binding" | simulator-tested (V5) |
| `Note_MassRate_Reconciliation` (2026-09-06) | $m\propto\Gamma_{\rm commit}\times$ reserve | "a stated bridge, conditional" |
| ontology §12 (2026-10-11) | superpositions do "not generate curvature"; "quantum systems… have low ED" | argued |
| Attempt 04 R4, ruling D30 | "Does uncommitted pattern (light) send influence? **Yes**… Radiation gravitates" | "consistent, not derived" |
| `run_event_layer.py` | a pattern's phase advances DPHI = 0.1 per completed blink, "ours" | harness setting |

Two pairs of these conflict: DSR-4 with Mass Without Mass, and §12 with D30.

**Candidate rules, and what each gives.** The first two columns of results follow from Run 30's static result and standard post-Newtonian bookkeeping. The cosmology column is the measured radiation-era expansion.

| rule | rest + binding + internal energy | moving matter (GR: weight $\tfrac32v^2$ in conserved terms) | stress (GR: 3p) | radiation | verdict before any run |
|---|---|---|---|---|---|
| **R-a. Cadence draw:** a pattern draws in proportion to its frequency ω = E/ħ (DSR-4 extended) | weight 1 ✓, since a bound state's ω includes its binding and internal energy | lab-frame ω = γm gives $+\tfrac12v^2$: Φ₁ coefficient 2 against GR's 4, so $\zeta_1+\alpha_3=-2$ and an Earth–Moon term of $+\tfrac43$ if it is ζ₁. If cadence means the tick rate seen in the lab (ω₀/γ), the weight is $-\tfrac12v^2$ and $\zeta_1+\alpha_3=-4$ | 0 against 3 | pulls by its energy only. That fails the radiation era if the expansion is driven by the active mass (half GR's H²). It is untested if ED has an energy-only Friedmann constraint | fails motion and stress |
| **R-b. Cadence plus flux:** a pattern draws for its energy *and* for its momentum flux, the possibility it carries through each place, per direction | ✓ | ✓: energy gives $\tfrac12v^2$ and flux gives $v^2$, together $\tfrac32v^2$. This covers the source of $g_{00}$ only; frame dragging, α₁ and α₂ still need the field dynamics (Run 31) | ✓ (3p) | ✓ (energy, plus the pressure weight: 2E in bulk) | GR's weights at first post-Newtonian order. It is Tolman–Komar's source, so under Allen's R1 it is "consistent, not derived" unless ED gives an independent reason for the flux to draw. D30's "influence carries motion and energy" points that way |
| **R-c. Only commitments pull;** patterns and radiation do not (§12) | only if bound patterns *are* renewing commitments whose rate includes their binding | as R-a, via the commitments | 0 | does not pull: against the measured radiation era and against D30 | fails radiation |
| **R-d. Mass from binding,** separate from the commitment rate (Mass Without Mass) | depends on the binding rule | — | — | — | conflicts with Run 30's identification of active mass with the draw |

**Reading.**
- Only a rule that counts momentum flux as well as energy (R-b) gives GR's weights for moving matter and stress.
- A pure "draw = ħω" rule (R-a) gets binding energy right, which is the part the Moon and MICROSCOPE test most directly. It misses motion and stress, as Attempt 01 and 03 found for their counting rules.
- The stress weight bites for self-gravitating bodies, where by the virial theorem $3\int p=-\Omega$. It bites less for bodies held by non-gravitational stresses, whose integrated stress vanishes (von Laue).
- Every rule's motion weight is downstream of Run 31. If the engine's field cannot follow a moving body, no draw rule for moving matter can be checked on the engine as built.

**Allen's decision.**
1. Which mass reading is canonical: DSR-4 (frequency) or Mass Without Mass (binding)?
2. Do patterns and radiation pull (D30) or not (§12)?
3. If R-b: what in ED makes possibility in transit draw, so that it is a reason rather than Tolman restated?

**Then, pre-registered:**
- a bound pattern (a Klein–Gordon pattern in a box well, binding a few % of its energy) whose draw follows the chosen rule. Its far field is measured against $E=\hbar\omega$, with binding counted, to 1%.
- moving patterns against the 1 + 2v² requirement, once the field can follow them (Run 31).

**Allen's ruling (19 October).** "yes to 1": a pattern's rest energy (ħω, binding included) draws, as in D30. With the Lorentz input (Run 34) its momentum flux draws too, so the adopted rule is R-b. Tested in Run 36.
