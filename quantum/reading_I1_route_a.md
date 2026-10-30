## Reading I1: what a route-(a) record is (a reading, before Test I1)

*27 October 2026.*
- *Revised after an independent check (`checkI1/REPORT.md`), whose corrections are adopted here.*
- *This is a reading of the record against standard measurements; the estimates are order of magnitude. Inferences not in the record are marked "(inference)".*

**The question** (Note I §8, I1). Model a pattern meeting committed matter in CO's terms, derive the coherence loss, and check it against measured decoherence. It includes:
- a control in which the matter keeps no which-path record;
- an account of emitted thermal photons, which are patterns, not committed matter.

Three open items wait on I1:
- route (a)'s rate in bulk matter, which decides the upper part of Run 92's window;
- whether route (b) is symmetrised CSL-type or GRW-type (deferred to I1, 27 October);
- Q7, to be registered with I1.

### 1. What the record says

| item | statement | source | status |
|---|---|---|---|
| route (a) | "a pattern that interacts with committed matter is recorded at its surroundings' resolution"; laboratory test masses, decohered all the time by gas and thermal radiation, draw at fine resolution | ONTOLOGY §1; Reading I0 | ruled 27 October |
| which interactions record | an interaction that depends on the pattern's path can leave a record; interactions that leave no which-path record keep coherence (Bragg reflection in neutron interferometers, material gratings, mirrors) | Note I §5 | design-note requirement |
| what route (a) must reproduce | Q5: ordinary decoherence at the measured rates (collisional decoherence of fullerenes, Hornberger et al. 2003; decoherence through internal clocks) | Note I §4 | requirement |
| what it would add | "a consistency requirement and a relabelling risk, not a prediction"; route (a) reproducing decoherence is "not remarkable" | Note I §5, §9 | design-note assessment |
| a commitment's hold | "a pattern's commitment is filled by the possibility the pattern itself carries" (stated 27 October); ruled the same day for route (b): the stock, in proportion to the energy, fills R2's hold, so the rate is κ_b ω | ONTOLOGY §1; Reading I4 | stated; ruled for route (b) |
| deposits | each record deposits the pattern's draw E_TK/λ_tot at the recorded place, smeared at r_C (listed under route (b)'s form) | M3, ruled 27 October | ruled for route (b) |
| other rulings used | the local stamp (26 October); M1 (route (b) on every pattern); M4 (units electrons and nucleons); the operator rate κ_bĤ/ħ; κ_b = 1/(aP∞); the phase turned by the time-averaged count | ONTOLOGY §1 | ruled |
| photons and matter | photons are patterns; matter is commitment that keeps re-making itself. What is matter and what is pattern is open (a cluster is matter, yet its centre of mass interferes) | ONTOLOGY §2; Note I §10 | primitive; open |

**What the record does not say:**
- the kernel of a route-(a) record, that is, how much coherence one record removes between two branches D apart;
- where a route-(a) record's deposit lands, and at what resolution (inference so far);
- whether the hold statement of 27 October covers route-(a) records;
- the rate of route-(a) records for matter in bulk.

**The ruling as worded fails I1's own control.** "A pattern that interacts with committed matter is recorded" covers Bragg crystals, gratings, mirrors and absorbing foils, all of which keep coherence (Rauch, Treimer and Bonse 1974; Summhammer, Rauch and Tuppinger 1987). So the which-path condition below is an amendment to the ruling, not a reading of it (§8, choice 1).

### 2. What is measured

- **Gas collisions** (Hornberger et al. 2003). C₇₀ in a Talbot–Lau interferometer (grating period 991 nm): visibility falls as V₀e^{−p/p₀} with gas pressure. Across gases spanning almost two orders of magnitude in mass and interaction strength, it agrees with a parameter-free decoherence theory that includes velocity and detector-selection corrections (15% pressure uncertainty, 5% theory). For almost all paths, each collision removes the coherence completely, so the rate is the collision rate.
- **Thermal emission** (Hackermüller et al. 2004). C₇₀ heated to about 2500–3000 K emits a few visible photons (λ ≲ 0.83 μm; the emission rides on C₇₀'s S₀→S₁ absorption band) across path separations up to about 1 μm. The standard kernel is
$$
\eta(d)=\frac{\sin(2\pi d/\lambda)}{2\pi d/\lambda}.
$$
  Visibility falls from 47% to 0 with heating power. The paper names the position of the laser focus as the main source of the remaining difference from theory.
- **Single-photon which-path against separation** (Chapman et al. 1995; Pfau et al. 1994; Kokorowski et al. 2001). Atoms in an interferometer each scatter one photon (Na, 589 nm). The measured contrast against arm separation d:
  - falls to zero at about d = λ/2;
  - partly revives at larger d;
  - carries a phase that jumps by about π where the contrast vanishes.

  Selecting atoms by their recoil regains over 60% of the lost contrast at d = λ/2. With more photons per atom the dependence on d changes qualitatively (Kokorowski et al. 2001).
- **No which-path record, coherence kept:**
  - perfect-crystal neutron interferometers rely on Bragg diffraction (Rauch, Treimer and Bonse 1974);
  - an absorbing foil and a chopper of equal transmission reduce neutron fringes differently (Summhammer, Rauch and Tuppinger 1987);
  - with an erasable which-path marker, the fringes return once it is erased (Bertet et al. 2001, cavity QED).

  The marker in Bertet et al. is a pattern (cavity photons), not committed matter, so it is not a control "in which the matter keeps no which-path record" in CO's sense.

### 3. Readings of "a record"

**(R-a1) A record is the which-path information that committed matter keeps.**
- **The rule:** one interaction multiplies the branches' coherence by ⟨E₂|E₁⟩. Its magnitude is the loss, and its phase is a shift. For elastic scattering by a central potential, averaged over isotropic incidence:
$$
1-\int d\Omega\,\frac{|f(\mathbf q)|^2}{\sigma}\,e^{i\mathbf q\cdot\mathbf D/\hbar},
$$
  with the rate n⟨vσ⟩.
- **Against the measurements:**
  - Gas collisions: the collision rate.
  - Thermal emission: the sinc kernel.
  - Single photons: the zero at λ/2, the revival, the phase jump and the regain on selection, all as measured.
  - Bragg diffraction and gratings: no record, as measured.
- **What it adds:** this is standard decoherence. It reproduces Q5 with the rates borrowed (cross-sections, emission spectra); it adds that a record is kept.

**(R-a2) A record is a Gaussian localisation of the pattern, made at the interaction, at the surroundings' resolution** (route (b)'s form, triggered by the interaction). One record removes 1 − e^{−D²/4σ²}.
- **Excluded by the single-photon experiments.** The Gaussian kernel is positive and falls monotonically for every σ. It gives:
  - no zero and no revival;
  - no phase, since a localisation gives no mean kick;
  - no regain on selection, since the localisation has already removed the other branch.

  Chapman et al. 1995 and Kokorowski et al. 2001 measure all three (Pfau et al. 1994 maps the coherence lost against separation).
- **Thermal emission alone could not have told.** With the paper's visible spectrum, a Gaussian changes the loss per photon by only 2–8% (0.92–0.94× with σ matched at small separation, 0.97–0.98× with σ = λ/2π). The single-photon data are what decide it.
- **Bragg diffraction:** a Gaussian at the crystal's resolution (about 0.3 Å) would also destroy the coherence the interferometer shows.

**(R-a3) The commitment and its deposit are made when the which-path carrier is itself recorded** (for a photon, at its absorption by committed matter).
- **Not a claim about the observed coherence.** Visibility is lost at the entangling event. Dürr, Nonn and Rempe 1998 show fringe loss with no momentum back-action, and no-signalling forbids the unconditioned visibility from depending on the carrier's later fate. So (R-a3) says *when the commitment and the deposit happen*, not when coherence is lost. With that wording it gives the same visibilities as (R-a1).
- **It depends on two open items:**
  - it makes a photon's absorption commit a distant molecule, a two-place commitment that Note I's I3 requires to be registered first;
  - it uses a line between matter (the gas, the walls) and patterns (photons) that the record leaves open.

### 4. Does the hold statement cover route (a)?

- If a route-(a) record were also filled by the pattern's own stock (Reading I4), its rate would be capped at κ_b ω, the route-(b) rate:
  - C₇₀ at the window's upper edge: about 10⁻¹⁸ s⁻¹ at r_C = 100 nm, and 10⁻⁶ s⁻¹ at 1 m;
  - against Hornberger's collision rates of about 10²–10³ s⁻¹.
- So **Q5 fails unless route-(a) records are exempt.** They would have to be filled by the committed matter's possibility, as the engine's matter commitments are (R2 as written), or not held at all (§8, choice 2).

### 5. Route (a)'s rate in bulk matter, and the bound it gives

- **The quantity that matters is a fraction.** Under M3 a body's draw is shared between its route-(a) and route-(b) records. A fraction
$$
f=\frac{\lambda_b}{\lambda_a+\lambda_b}
$$
  is deposited smeared at r_C, and at distances ≪ r_C it is missing from the body's active mass (inference).
- **Why it can be measured.** If λ_a depends on the material, f does too. A composition-dependent ratio of active to passive mass is bounded by lunar laser ranging, which applies when r_C ≫ the Moon's radius:
  - f(Al) − f(Fe) < 4×10⁻¹² (Bartlett and van Buren 1986);
  - < 3.9×10⁻¹⁴ (Singh et al. 2023).
- **Three readings of λ_a for an atom in bulk** (each an inference):
  - **(i) per unit, from its interactions:** of order 10¹²–10¹³ s⁻¹ from phonons in insulators, and 10¹⁴ s⁻¹ from conduction electrons in metals. This depends on material and temperature, so LLR bites.
  - **(ii) per body:** test masses decohered all the time as wholes.
  - **(iii) bulk constituents as matter renewing:** at about mc²/(aħ) ≈ 10²⁴ s⁻¹, the same per unit of mass in every material, so LLR does not bite.
- **Under (i),** with f ≲ 3.9×10⁻¹⁴ and λ_a = 10¹³ s⁻¹:
$$
\lambda_b\lesssim0.4\ \text{s}^{-1},\qquad \kappa_b\lesssim2.7\times10^{-25},\qquad a P_\infty\gtrsim3.7\times10^{24}\ \ (\kappa_b=1/aP_\infty),
$$
  where κ_b ≲ 2.7×10⁻²⁵ follows from λ_b = κ_b m_Nc²/ħ.
  - W's upper edge (RadioAstron, 2.87×10⁻⁴⁴ r_C²) reaches this at r_C ≈ 3×10⁹ m, or about 10⁹–10¹¹ m across λ_a = 10¹²–10¹⁴ s⁻¹ and the two LLR bounds.
  - **So under (i), LLR caps κ_b wherever W's upper edge is higher, for r_C above about 10⁹–10¹¹ m.** It narrows W's range of κ_b there; it does not close W. With κ_b = 1/(aP∞) it needs a·P∞ ≳ 4×10²¹–4×10²⁵ at any r_C. That excludes a·P∞ near gravity's limit, and with it Reading I4's "the gravity limit only for r_C ≳ 10¹⁶ m".
  - **Run 92's addendum sentence** ("conditional on route (a)'s rate above 1.6×10¹⁶ m") was too weak by the same argument. It used λ_b < λ_a where f ≪ the LLR bound is needed.
  - **The per-pattern reading's window** (κ_b ≳ 8×10⁻²⁸, r_C ≳ 1.7×10⁸ m) survives under (i), between 8×10⁻²⁸ and 2.7×10⁻²⁵.

### 6. Identical units: how route (b) is symmetrised

The step "route (a) is linear in the density, so route (b) is CSL-type" goes past the record. The two options, and what each costs:
- **GRW-type** (Tumulka 2006; Dove and Squires 1995): the total record rate is Σλ_k. This agrees with M2 (additive over units) and M4 (each unit commits on its own).
  - Heating, emission and break-up are overstated by Run 92's labelled treatment, by up to the number of like units within r_C (Run 92's addendum). So W can only widen.
- **CSL-type** (jump operators linear in the density): the total record rate is N²λ for N units within r_C. That conflicts with M2 and M4. Run 92's edges move both ways:
  - **B10 is suppressed.** The two nucleons of a deuteron within r_C are kicked together, and the leading break-up term falls to about 2×10⁻⁷ of the labelled value (Jones, Pearle and Ring 2004).
  - **B2 is enhanced.** The test mass's centre-of-mass noise is coherent: κ_b < 5.3×10⁻⁴⁰ r_C² for r_C much larger than the 46 mm test mass, about 6 decades below Run 92's upper edge from about 0.1 to 70 m.

So Run 92's sentence that "the labelled treatment is conservative for every upper bound" is wrong under either symmetrisation. Under GRW-type the labelled bounds are too strong, and W only widens. Under CSL-type they err in both directions.

### 7. Q7 under the rulings

The rate is the operator κ_bĤ/ħ with κ_b = 1/(aP∞). The ⁸⁸Sr tweezer clock (Young et al., *Nature* 588, 408 (2020): ΔE = 1.775 eV; single-atom coherence 48(8) s, inferred for the central atoms, and at least 33(2) s across the array) gives:

| whose energy carries ΔE | bound on κ_b | bound on a·P∞ |
|---|---|---|
| an electron's, with its orbital energy | κ_b < 1.8×10⁻¹¹ | ≳ 5.6×10¹⁰ |
| the atom's | κ_b < 2.9×10⁻⁶ | ≳ 3.5×10⁵ |

- **For the electron's reading, by value of a:** P∞ ≳ 5.6×10¹¹ (a = 0.1), 5.6×10¹⁰ (a = 1) or 8.9×10⁹ (a = 2π), against gravity's 6.4×10¹⁰.
- **If the two valence electrons share ΔE,** Γ halves.
- **Under §5's reading (i),** LLR's bound (a·P∞ ≳ 4×10²¹–4×10²⁵) is far stronger than Q7.

### 8. Choices for a ruling

1. **Amend route (a)'s ruling.** A record is made only when committed matter keeps path-dependent (which-path) information (R-a1's condition). As worded, the ruling fails the Bragg, grating and foil controls.
2. **Whether the hold statement covers route (a).** If it does, Q5 fails by about 20 decades. The option that keeps Q5: route-(a) records are filled by the committed matter's possibility (R2 as written) or are not held.
3. **When a route-(a) commitment and its deposit are made:** at the entangling interaction, or when the carrier is itself recorded (R-a3, which depends on I3 and on the matter/pattern line).
4. **Whose λ_a counts in bulk matter:**
   - (i) per unit, from its interactions (LLR then caps κ_b for r_C above about 10⁹–10¹¹ m);
   - (ii) per body;
   - (iii) bulk constituents as matter renewing at about mc²/(aħ) (no LLR cut).
5. **Route (b)'s symmetrisation:** GRW-type (consistent with M2 and M4) or CSL-type (needs M2 and M4 revised and Run 92's edges re-derived).
6. **Whose energy enters Q7 for a bound electron:** the electron's (with its orbital energy, possibly shared between valence electrons) or the atom's.
7. **What to register as Run 93:**
   - the single-photon kernel test (R-a2 against Chapman 1995 and Kokorowski 2001);
   - the LLR bound on bulk route (b) under the λ_a reading ruled;
   - Q7;
   - or record these as readings and register none.

### What I1 adds that is not a relabelling

- **(R-a2) is excluded by measurement.** A route-(a) record cannot be a Gaussian localisation of the pattern made at the interaction. Route (a)'s coherence loss has the standard kernel, with its zeros, revivals and phase.
- **Under per-unit route-(a) rates, LLR bounds route (b) in bulk matter:** κ_b ≲ 3×10⁻²⁶–3×10⁻²², which caps κ_b in W for r_C above about 10⁹–10¹¹ m.

### 9. Rulings (27 October, "as recommended")

1. **Route (a) is amended.** A record is made only when committed matter keeps path-dependent (which-path) information.
2. **The hold statement covers route (b) only.** Route-(a) records are filled by the committed matter's possibility, as R2 is written.
3. **A route-(a) commitment and its deposit are made at the interaction.** (R-a3) waits on I3. *Closed 27 October (Reading I3 §5, ruled): (R-a3) is a two-place commitment of the excluded (T2) type, since the molecule's deposit would land when a distant party chooses to absorb the photon. It is excluded, and the record is made at the interaction.*
4. **Route (a)'s rate in bulk is per unit, from its interactions** (reading (i)), so the lunar-laser-ranging bound of §5 applies.
5. **Route (b) is symmetrised GRW-type.**
6. **Q7 counts an electron's energy,** with its orbital energy.
7. **Run 93 is registered:** Run 92's window recomputed with the lunar-laser-ranging and Q7 bounds under these rulings. The kernel's exclusion of (R-a2) is recorded as this reading's finding.

*Note (30 October): P∞ ≳ 6.4×10¹⁰ was p_s's bound times the pulsar triple's ratio bound; with ε = 0 in gravity the ratio bound and this figure lapse (Reading I17). What remains is p_s ≳ 4×10⁵ (conditional) and route (b)'s a·P∞ ≳ 2.5–5×10²⁷ (Run 96 with its relic-neutrino addendum). The upper bound p_s ≲ 1.1×10³⁰/a (Reading I11) rested on the same pulsar-triple ratio and lapses too (corrected 30 October after Reading I18's check).*
