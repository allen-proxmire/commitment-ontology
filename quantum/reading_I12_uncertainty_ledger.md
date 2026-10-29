## Reading I12: uncertainty as a ledger

*29 October 2026. Allen's idea, in his words: "theres only so much budget. no infinities. if position and momentum are from the same commitment budget, you always rob one to pay the other. the ledger always fully to account." Graded under Reading I7's grades where they apply; (B) is graded a restatement, which I7 does not list. Revised after an independent check, whose corrections are adopted. Ruled in §5. Nothing here is registered. "Ledger" is used here because "budget" already names the clock and possibility budgets of Runs 10–26.*

**In plain terms.** If position and momentum drew on one fixed budget, with each sharpness its budget over its share, every particle would carry a momentum floor far above what ordinary atoms show. Read as an *information* ledger, the idea is exactly quantum mechanics' strongest form of the uncertainty principle, the entropic one: true, but not new. "No infinities" alone adds nothing, since quantum mechanics already keeps every spread finite. A floor needs a fixed bound on what a pattern can carry. CO has a candidate, finitely many places in any region, and on the engine's hop it would put the floor in tension with a recent oscillator bound. Each route-(b) record is a localisation whose noise and disturbance multiply to exactly ħ/2, the least allowed.

### 1. Three ways to write the ledger

**(A) Sharpness as a share of a fixed budget.** B = B_x + B_p, with each spread inverse to its share:
$$
\Delta x=\frac{a}{f},\qquad \Delta p=\frac{b}{1-f}\ \Rightarrow\ \Delta p=\frac{b\,\Delta x}{\Delta x-a},\qquad \Delta x\,\Delta p=\frac{b\,\Delta x^2}{\Delta x-a}\ \ge\ 4ab\ \ (\text{at }\Delta x=2a).
$$
- It has floors at both ends, Δx > a and Δp → b, and the product grows away from one width.
- **As the origin of ħ (4ab = ħ/2) it is excluded:**
  - Hard scattering localises interactions to about 10⁻¹⁸–10⁻¹⁹ m, so a ≲ 10⁻¹⁸ m (≲ 0.84 fm at the weakest, from quark confinement). Then b = ħ/(8a) ≳ 25 GeV/c (≳ 30 MeV/c at the weakest).
  - The hydrogen ground state's momentum spread, about 2.2 keV/c per axis, already rules out the weakest case by 4 orders of magnitude. Delta-kick-cooled atoms (σ_p ≈ 3×10⁻³⁰ kg m s⁻¹) rule it out by about 10.
  - Oscillator ground states (trapped ions, ground-state-cooled resonators) and squeezed mechanical states reach Δx Δp = ħ/2 at widths spanning many decades. Form (A) cannot.
- **With a and b free and 4ab ≪ ħ/2,** (A) is no longer the source of ħ; it reduces to the two floors of (C).
- **Grade:** excluded.

**(B) An information ledger.** Knowledge of position plus knowledge of momentum is capped:
$$
h(x)+h(p)\ \ge\ \ln(\pi e\hbar)\quad(\text{per dimension}),
$$
with h the differential entropies, in nats. This is the entropic uncertainty relation (conjectured by Everett and by Hirschman, 1957; proved by Beckner and by Białynicki-Birula and Mycielski, 1975).
- Lowering h(x) raises the floor on h(p) by the same amount; at the bound the trade is exact. The relation is a floor on combined uncertainty, not a conserved total. Mixed states add their own entropy (Frank and Lieb).
- It implies Heisenberg's form, since a Gaussian has the largest entropy at fixed variance:
$$
\ln(2\pi e\,\sigma_x\sigma_p)\ \ge\ h(x)+h(p)\ \ge\ \ln(\pi e\hbar)\ \Rightarrow\ \sigma_x\sigma_p\ge\tfrac{\hbar}{2}.
$$
- Pure Gaussian states with no position–momentum correlation (coherent and squeezed states) saturate it at any width.
- **Grade:** a restatement of standard quantum mechanics. It is the ledger idea in its strongest established form.

**(C) A bounded ledger.**
- **Finiteness alone gives no floors.** Standard quantum mechanics already keeps every spread finite and nonzero (a delta function is not a state). A floor needs a *fixed upper bound* on what a pattern can carry, per pattern or universal.
- **CO's full statement offers one:** finitely many places in any finite region (ONTOLOGY_full, "no infinities", 24 October). If a pattern's position is defined only to a place, Δx has a floor of order the hop ℓ.
- **A momentum floor** Δp ≳ ħ/X_max is plain Heisenberg for anything confined; it is new only if X_max is universal. The horizon would give Δp_min ~ ħH₀/c ≈ 8×10⁻⁶¹ kg m s⁻¹, which is unmeasurable.
- **A universal momentum cap** is not boost-invariant. CO borrows Lorentz invariance (R7, R8), so a cap meets Reading I11's objection unless special relativity is deformed, which would be another new statement.
- **At the level of floors** this corresponds to the extended generalised uncertainty principle (Kempf 1994):
$$
\Delta x\,\Delta p\ \ge\ \frac{\hbar}{2}\big(1+\alpha\,\Delta x^2+\beta\,\Delta p^2\big),\qquad \Delta x_{\min}=\hbar\sqrt\beta,\quad \Delta p_{\min}=\hbar\sqrt\alpha,\qquad \beta=\frac{\beta_0}{(M_Pc)^2},\ \Delta x_{\min}=\sqrt{\beta_0}\,\ell_P .
$$

**What each candidate scale gives:**

| candidate ledger | floor | status |
|---|---|---|
| places in a region, on the engine's hop (ℓ ≈ 10^{2.3}–10^{3.2} ℓ_P) | Δx_min ≈ ℓ, so β₀ ≈ 4×10⁴–3×10⁶ | below Bushev et al.'s β₀ < 5×10⁶ (sapphire resonator, 2019); above the phonon-cavity preprint's β₀ < 62 (Campbell et al., 2023). Both bounds assume the deformation acts on composite centres of mass with a mass-independent β₀, and for composites the effect is expected to fall roughly as 1/N². **A conditional tension, not an exclusion.** |
| places on P08's hop (ℓ = ℓ_P) | β₀ ≈ 1 | below every bound |
| the vacuum's hold, under C1a ((2π)^{3/2}r_C³ = 2ħ_tℓ³) | the hold's volume is the route-(b) localisation volume, so Δx_min ~ r_C | as a floor on every state's Δx, excluded by atomic sizes; as a limit on route-(b) records, it is §2 |
| the pattern's renewals, E/(aħ) per unit time | aħ/(mc), a times the reduced Compton wavelength | already the single-particle localisation limit of relativistic quantum theory (and the renewal count matches the Margolus–Levitin bound); distinctive only if a ≫ 1 |
| the pattern's possibility stock, q = 2E/E_pair (Reading I4, S-i) | depends on E_pair, hence on ħ_t | the most direct "budget" in CO's terms; not yet written out as a floor |

**Bounds on β₀** (convention above; composite-body bounds assume a mass-independent β₀):

| source | β₀ < |
|---|---|
| Lamb shift; Landau levels; STM tunnelling (Das and Vagenas 2008) | 10³⁶; 10⁵⁰; 10²¹ |
| J/ψ levels (Ali, Das and Vagenas 2011) | 10³⁴ |
| AURIGA bar (Marin et al. 2013) | ~10³³ |
| sapphire resonator (Bushev et al. 2019) | 5×10⁶ |
| phonon cavity (Campbell, Tobar, Goryachev and Galliou 2023, preprint) | 62.4 (3σ) |
| equivalence principle (Ghosh 2014) | 10²¹ |

- **Grade:** an open direction, not yet a lead. It becomes a lead once a fixed per-pattern bound is written out in CO's terms, with its dynamical consequence: a floor with no effect on spectra cannot be tested.

### 2. A CO-native reading: route-(b) records saturate the error–disturbance bound
Route (b) localises a unit with
$$
L(x)=(\pi r_C^2)^{-3/4}e^{-(q-x)^2/2r_C^2}
$$
(Q4).
- **Noise.** The record's outcome density is |ψ|² smeared by |L|² ∝ e^{−(q−x)²/r_C²}, a Gaussian of variance r_C²/2 per axis. So the position noise is ε = r_C/√2.
- **Disturbance.** The momentum kick is ⟨Δp_i²⟩ = ħ²/(2r_C²) per axis, the same for every state (summed over the three axes, B16's 3ħ²/(2r_C²)). So η = ħ/(√2 r_C).
- **So**
$$
\varepsilon\,\eta=\frac{\hbar}{2},
$$
  the least the error–disturbance relation allows for an unsharp position measurement (Arthurs and Kelly 1965; Ozawa 2003; Busch, Lahti and Werner 2013).
- A localisation channel is not a state. The state after a record is minimum-uncertainty only if the state before it was broad and unchirped.
- **In the ledger's terms,** each commitment buys position at r_C/√2 and pays exactly ħ/(2ε) in momentum disturbance.
- **Status:** a reading, true of any pure, real Gaussian localisation. Its scale is r_C, itself a primitive input bounded by data (0.09–51 μm), not fixed.

### 3. What this means
- **The share form (A) is excluded** as the origin of ħ.
- **The information form (B) is the entropic uncertainty relation:** the ledger idea, in established form.
- **A bounded ledger (C) is the one route to a deviation.** CO's "finitely many places" is a candidate. On the engine's hop it would put the minimal length at β₀ ≈ 10⁵–10⁶, in conditional tension with the newest oscillator bound. On P08's hop it is invisible.
- **Route (b)'s records saturate the error–disturbance bound,** at the scale r_C.

### 4. Choices for a ruling
1. **Record §3.**
2. **Whether to write out a bounded ledger:** state which bound a pattern carries (places in a region, the possibility stock q, or another), what it does to spectra, and compare it with the β₀ bounds, including the composite-body question. If adopted, it would be graded a lead.

### 5. Rulings (29 October; Allen: "do as you recommend")
1. **§3 is recorded:**
   - the share form is excluded as the origin of ħ;
   - the information form is the entropic uncertainty relation (a restatement);
   - a bounded ledger, through finitely many places in a region, is the one route to a deviation;
   - route-(b) records saturate the error–disturbance bound at the scale r_C.
2. **A bounded ledger is to be written out:** which bound a pattern carries, its effect on spectra, and its comparison with the β₀ bounds, including whether a minimal length applies to a composite body's centre of mass or only to its constituents.
