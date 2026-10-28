## Reading I9: what could fix saturation's two numbers; saturation records and gravity; the relativistic-kick choice

*28 October 2026. After Run 98 (C4-β, route (c), a lead at laboratory densities with ρ_K and Γ_K free). Graded under Reading I7's criterion (derived, lead, fitted). Revised after an independent check (`checkI9/REPORT.md`), whose corrections are adopted. Ruled in §8. Numbers are arithmetic, not a test.*

### 1. Why
Run 98's lead survives because ρ_K and Γ_K are free: the allowed Γ_K spans 7 to 33 decades. It becomes a prediction only if something in CO fixes ρ_K, Γ_K, or a relation between them.

### 2. Fixing ρ_K
The threshold is a stock per place, K, read as a mass density (Reading I8, C4-β §2):
$$
\rho_K=\frac{K\,a\,\hbar}{2c\,\hbar_t\,\ell^4}.
$$
- **Under C1a** (ħ_t = V_c/2ℓ³) this is
$$
\rho_K=\frac{K\,a\,m_\ell}{V_c},\qquad m_\ell=\frac{\hbar}{c\ell},
$$
  so a cell at threshold holds K·a hop masses (Planck masses for P08's hop).
- **Under C1b** (V_c = 2ħ_tℓ⁴κ_b/λ_C, with κ_b = 1/(aP∞)), with K = P∞ it is exactly
$$
\rho_K=\frac{\hbar}{c\,\lambda_C V_c}=\frac{m_N}{V_c(r_N)},
$$
  one unit per cell, for every species and every aP∞ and hop.

| candidate | ρ_K (kg m⁻³) | where it lands | grade |
|---|---|---|---|
| **K = P∞, C1a** | ≳3×10²⁷ (to 3×10⁴⁷) | far above any matter. It **is** C4-β′ per cell (cell energy aP∞ħc/ℓ) | derived given C1a (itself a lead); inert |
| **K = 1 (or p_s), C1a** | K·a·m_ℓ/V_c: at a = 1, 1.0×10⁴–1.9×10¹² (P08), 16–2.9×10⁹ (engine) | **laboratory densities** at r_C ≳ 39 μm (P08) or a few to tens of μm (engine). A laboratory onset needs K ≲ 10³, with r_C and a chosen together | lead; CO-native, but in effect fitted through r_C and a (ρ_K ∝ a r_C⁻³) |
| **K = P∞, C1b** | exactly m_N/V_c(r_N): 8×10⁻¹⁶–1.7×10⁻¹⁰ | N_cell = 1: an isolated unit sits at the step's midpoint. The per-particle regime by construction, untested by Run 98 | lead (rests on C1b) |
| **Λ's density** | 5.8×10⁻²⁷ | per-particle regime (N_cell 10⁻²⁰–10⁻¹¹), untested | borrowed (measured), new identification |
| **a Compton mass per cell**, ħ/(cr_C) per V_c | 3×10⁻²⁷–3×10⁻¹⁶ | per-particle regime, untested | lead |
| **nuclear saturation** (0.16 fm⁻³) | 2.7×10¹⁷ | neutron-star interiors, untested | borrowed |
| **atomic density**, m_u/a₀³ | 1.1×10⁴, or 2.7×10³ with (4π/3)a₀³ | laboratory densities, between aluminium and lead | borrowed; in effect fitted, since the O(1) factor decides which materials saturate |

- **No CO quantity fixes ρ_K at laboratory densities without a free choice** of K, a and r_C. Under C1a, K = P∞ is inert and K = 1 reaches laboratory densities only at large r_C. K spans the gap between them, so nothing in the record picks the value.
- The CO-native C1b reading puts the threshold at exactly one unit per cell. That is a definite statement, but in the regime Run 98 did not classify.

### 3. Fixing Γ_K

| candidate | Γ_K | against 10λN_cell | grade |
|---|---|---|---|
| **the hold's ceiling**, c/ℓ | 2.9×10⁴⁰ or 1.9×10⁴³ s⁻¹ | excluded by ≥16 decades wherever a laboratory bound applies (Run 98) | excluded |
| **one commitment per light-crossing of a cell**, c/r_C | 5.9×10¹² (cap) to 3.3×10¹⁵ s⁻¹ (lower edge) | allowed and ≥10λN_cell at 3050 of 4580 tested points (2090 of 3580 at laboratory densities; 276 of 350 in solids, every r_C ≳ 0.44 μm). Excluded below about 0.34 μm by Earth, LISA and interference. **Margins down to 1** | lead; keeps the ≥10× jump |

*Note (after Run 99): the c/r_C row's "276 of 350 in solids, every r_C ≳ 0.44 μm; excluded below about 0.34 μm" was approximate. With Run 98a's and Run 99's bounds the edge at solid densities is 0.23–0.44 μm, and 0.85–1.44 μm near germanium's density (`run99_section.md`).*
| **the renewal rate of the cell's mass**, ρ_KV_cc²/(aħ) = P∞λN_cell | – | excluded at every point checked for a ≤ 1 | excluded |
| **once per hold, C1a**, c/(ħ_tℓ) = 2cℓ²/V_c | 7×10⁻⁵⁰ to 6×10⁻³⁶ s⁻¹ | far below λN_cell (0.06–10⁸ s⁻¹ at the floor). Under C1b it is smaller still | derived given C1a; no signature |
| **a saturated cell commits as one route-(b) unit** | λN_cell = κ_bc²ρ_KV_c/ħ | allowed by ≥3.4×10⁸; ratio 1, so no 10× jump | lead (one new statement) |

**Γ_K = c/r_C.** The hold's ceiling at the scale of a cell: a saturated cell commits once in the time light takes to cross it. It needs one new statement, keeps Run 98's distinctive jump, and fixes Γ_K with no free number. Unlike Run 98, its margins reach 1, so a registered scan would have real power. Where they reach 1 has not been mapped beyond the check's counts.

**The cell-as-unit reading.** The decoherence rate between two branches is
$$
\Gamma_{\rm dec}=\frac{\Gamma_K}{2}\int\frac{(\Pi_1-\Pi_2)^2}{V_c}\,d^3x .
$$
For a body of density ρ_b > ρ_K displaced by D ≫ its size + r_C, with V_sat ≡ ∫Π²d³x:
$$
\Gamma_{(c)}=\frac{\kappa_bc^2\rho_KV_{\rm sat}}{\hbar},\qquad \Gamma_{(b)}=\frac{\kappa_bc^2\rho_bV}{\hbar},\qquad \frac{\Gamma_{(c)}}{\Gamma_{(b)}}=\frac{\rho_K}{\rho_b}\frac{V_{\rm sat}}{V}\lesssim1.05 .
$$
- The rate rises over several r_C past R_K, approaching ρ_K/ρ_b as 1 − O(r_C/R). It can overshoot near 1.5 r_C when ρ_K ≪ ρ_b.
- That is Allen's point 1 at a definite size: gold and silica differ when ρ_K lies between their densities. But it is a step of at most about 2× on route (b)'s own rate, which is itself unobserved, not the ≥10× jump.
- **Variants:**
  - A rate ∝ ϱ̂Π̂ (L ∝ ϱ̂^{1/2}Π̂) gives 2× for R ≫ r_C.
  - The literal L ∝ ϱ̂Π̂ gives (ρ_b/ρ_K)V_sat/V, a jump again.
  - Neither is silent in a saturated bulk: both bring back CSL-type bulk heating.

### 4. What §2–§3 mean
- **The noticeable form of C4-β needs ρ_K fitted or borrowed.** No CO quantity fixes it at laboratory densities without a free choice.
- **Γ_K can be fixed by a lead that keeps the jump**, c/r_C, and the record allows it over most of the tested region, with margins reaching present sensitivity. The cell-as-unit reading also fixes Γ_K, at the price of the jump.
- **So the strongest form on the table is C4-β with Γ_K = c/r_C:** one free parameter, ρ_K, plus r_C shared with route (b). That form can fail.

### 5. Saturation records and gravity (the open item from ruling 2)
- **A proposed reading of Reading I8's ruling 2** (a new inference, unreviewed):
  - Inside a uniformly saturated bulk Π̂ = 1, and the channel acts as the identity.
  - Since D[Π] = D[1 − Π], the channel can be unravelled with no jumps there, so the bulk makes no record. Ruling 2 then applies at threshold surfaces, where 0 < Π̂ < 1 and a commitment fixes where the surface is.
  - This agrees with Q2 (deposits only where a record fixes position) and Reading I6 (λ_tot counts depositing records). But neither settles it alone: the unravelling L = Π would give trivial bulk jumps, which would contradict ruling 2's "carries a deposit".
- **Surface records smooth gravity; they cannot roughen it.**
  - By Campbell's theorem the deposit noise is λ_tot(E/λ_tot)² = E²/λ_tot.
  - Run 96's floor can only fall. A lower floor only enlarges Run 98's margins, so the registered floor is conservative for survival and the verdict is unaffected.
  - Under Reading I6 ruling 6 a surface record carries only the shell's mass, so the interior noise stays route (b)'s and the floor barely moves.
- **Sizes.**
  - With Γ_K free at Run 98's Γ_max, under the L = Π unravelling, surface records would outnumber route (b)'s in a LISA test mass by 10⁴ (r_C = 0.09 μm) to 10¹¹ (the cap), at ρ_K = 10³.
  - Under the cell-as-unit reading, their rate relative to route (b) is 10⁻⁸–10⁻⁴ at ρ_K ≤ 10⁴, and up to 3×10⁻³ near ρ_b, so the floor changes by at most 0.3%.
- **Not ruled:** what a surface record deposits (which energy, and where; the √1.5 r_C smearing was written for a single unit).

### 6. The relativistic-kick choice (deferred since B16)
For r_C below about √6ħ/(mc), a route-(b) kick ⟨Δp²⟩ = 3ħ²/(2r_C²) is relativistic. B16's primary form is used only above that length (9.67 μm for ν₃).
- **R-a (as now).** Primary bounds stay within the non-relativistic validity, and the relativistic extension is a labelled variant. This choice sets Run 96's top edge between 0.36 and 9.67 μm (cap 2.0×10⁻²⁸ at 0.16 eV) and K97-rel.
- **R-b, relativistic kicks** (E = √(p²c² + m²c⁴) per hit). The variant becomes primary and binds from about 0.36 μm, with κ_top(cap) ≈ 3.9×10⁻²⁹ at Σ_max = 0.12 eV (B16-NR's primary uses 0.16 eV).
- **R-c, a minimum localisation width.** The effective width is max(r_C, √6ħ/mc), the length above which the kicks stay non-relativistic. That gives κ_b < 7.6×10⁻²⁰w² = 7.1×10⁻³⁰ for ν₃ below 9.67 μm, binding from 3.1 μm (where it meets B7′) to 9.67 μm. The window stays open, 1.3×10⁶ above the floor.
  - With the Compton width ħ/mc instead, the bound is 1.2×10⁻³⁰, but the formula is then extrapolated outside its validity.
  - R-c is a lead. It makes the effective width species-dependent for neutrinos, which reopens Reading I5's ruling 5.
  - Relativistic collapse models have no standard Compton cap. The usual remedy smears the collapse through a mediating field (Bedingham 2011; Pearle). Tumulka's relativistic GRW sidesteps the question.

### 7. Choices for a ruling
1. **The ρ_K finding:** no CO quantity fixes ρ_K at laboratory densities without a free choice of K, a and r_C. A laboratory onset needs ρ_K fitted or borrowed. Under C1b, K = P∞ gives one unit per cell.
2. **Γ_K = c/r_C,** one commitment per light-crossing of a cell. Whether to register it as Run 99: C4-β with Γ_K fixed, ρ_K free, a scan with real power.
3. **The cell-as-unit reading** (Γ_K = λN_cell): record it as the alternative that trades the jump for a step of ρ_K/ρ_b.
4. **Saturation records and gravity:** whether §5's reading of ruling 2 stands (a uniformly saturated bulk makes no record; ruling 2 applies at threshold surfaces), and whether surface records deposit.
5. **The relativistic-kick choice:** R-a, R-b or R-c.

### 8. Rulings (28 October; Allen: "do as you recommend")
1. **The ρ_K finding is recorded:** no CO quantity fixes ρ_K at laboratory densities without a free choice of K, a and r_C; a laboratory onset needs ρ_K fitted or borrowed.
2. **Γ_K = c/r_C is registered as Run 99:** C4-β with Γ_K fixed and ρ_K free.
3. **The cell-as-unit reading is recorded as the alternative,** trading the jump for a step of ρ_K/ρ_b.
4. **A uniformly saturated bulk makes no record;** Reading I8's ruling 2 applies at threshold surfaces (a reading). What a surface record deposits is not ruled.
5. **R-a:** primary bounds stay within the non-relativistic validity; the relativistic extension stays a labelled variant.
