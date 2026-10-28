## Reading I8, candidate C4-β in full: saturation, a third route to commitment

*28 October 2026. Ruled in Reading I8 §8: CO gets a capacity per place, Allen's "bandwidth", as a new primitive to be written out and tested. Revised after an independent check, whose corrections are adopted. The choices in §7 are ruled. The registered form, with the step S and the bounds, is Run 98's registration; the result is in `run98_section.md`.*

### 1. The new primitive, as a threshold density of the configuration
**(K) Where a configuration's stock of possibility, smoothed at r_C, exceeds a fixed amount per place, its matter commits by a further route.**
- K is a property of the **configuration's** stock density, not of the medium's places. So it does not read N or the external potential (Q6), and it does not repeat R6's "needs free capacity", which was excluded under Q6.
- K is a **threshold**, not a cap: matter denser than it exists, and simply commits faster. "Capacity" in Allen's sense is the density at which a pattern can no longer hold its superposition.

### 2. The stock density
Per place:
$$
\hat\rho(\mathbf x)=\sum_i q_i\,\ell^3\,G_{r_C}(\mathbf x-\hat{\mathbf x}_i),\qquad G_{r_C}(\mathbf y)=(2\pi r_C^2)^{-3/2}e^{-y^2/2r_C^2},\qquad q_i=\frac{2m_ic^2}{E_{\rm pair}} .
$$
- m_i is the unit's **rest mass**, a c-number per species, with no binding or excitation energy. With the operator Ĥ_i instead, Π̂ would not commute with x̂ and energy superpositions would decohere (Q7).
- E_pair is the **vacuum** constant. A local hold length would make the condition read the potential, at order Φ/c².
- ρ̂ is a density in the foliation, the same preferred frame as M2's rate. At laboratory speeds the effect is γ − 1 ~ 10⁻¹².
- The condition ρ̂ > K is then the same as a mass density smoothed at r_C exceeding
$$
\rho_K=\frac{K\,E_{\rm pair}}{2c^2\ell^3}=\frac{K\,a\,\hbar}{2c\,\hbar_t\,\ell^4}\quad(\text{kg m}^{-3}).
$$
  K is observable only together with ħ_t, a and ℓ.
- **Disclosure** (arithmetic on Run 97, not a test): with C1b's ħ_t, ρ_K/K ≈ 10⁻⁴²–10⁻⁶¹ kg m⁻³. A laboratory-scale ρ_K would need K ~ 10⁴²–10⁶⁵ units per place, and K ~ P∞ would give ρ_K ~ 10⁻¹⁵–10⁻³⁴ kg m⁻³. ρ_K is therefore treated as the free parameter.
  - *Correction (Reading I9's check): C1b's ħ_t already contains κ_b = 1/(aP∞), so with K = P∞ the threshold is exactly one unit per cell, ρ_K = m_N/V_c(r_N) (8×10⁻¹⁶–1.7×10⁻¹⁰ kg m⁻³), not 10⁻³⁴–10⁻¹⁵. The conclusion, that the record does not fix a laboratory ρ_K, stands.*

### 3. What saturation does: a gated, linear channel
$$
\frac{d\rho}{dt}\Big|_K=\Gamma_K\!\int\!\frac{d^3x}{V_c}\Big(\hat\Pi_{\mathbf x}\rho\hat\Pi_{\mathbf x}-\tfrac12\{\hat\Pi_{\mathbf x}^2,\rho\}\Big),\qquad \hat\Pi_{\mathbf x}=\sigma\!\Big(\frac{\hat\varrho(\mathbf x)-\rho_K}{\delta\rho}\Big),\qquad V_c=(2\pi r_C^2)^{3/2},
$$
with ϱ̂ = Σm_iG_{r_C}(x − x̂_i), σ a smooth step **with compact support** (0 below ρ_K − δρ/2, 1 above ρ_K + δρ/2), and **δρ = ρ_K/10** (tied, so it is not a third free parameter).

**Properties:**
- **Linear and diagonal in position,** so no measurement choice can signal. Alice's measurements commute with every Π̂_x, so Run 95's failure modes do not arise.
- **Silent where Π̂ is uniform,** inside a saturated bulk as in empty space, since D[Π] = D[1 − Π]. It acts only on threshold surfaces, and between branches whose saturated regions differ.
- **Silent below threshold:** with σ of compact support, nothing acts below ρ_K − δρ/2.

**What it reopens, named:**
- **"Route (b) is a rate, not a threshold"** (Note I §3, §5). C4-β is a gated rate; the ruling's ground (no self-sourced quantity) does not cover a carried stock density.
- **"Per unit"** (Reading I3 ruling 5). Π̂ is collective over the units within ~r_C, grouped by position. A probe can decohere because it sits near dense matter.
  - So this is a **third route to commitment,** route (c), beside routes (a) and (b).
  - Because the units are grouped by position, not entanglement, the channel stays linear and does not signal by measurement choice. Its influence over ~r_C in the foliation is of R4's class, "signalling through the field", and invisible at r_C ≤ 51 μm (light-crossing ≲ 2×10⁻¹³ s).

**Its parent:** mass-proportional CSL (Ghirardi, Pearle and Rimini 1990), with L ∝ ϱ̂ replaced by the step σ((ϱ̂ − ρ_K)/δρ). Inside the band it *is* CSL. It differs through a silent saturated bulk and a rate per cell that saturates at Γ_K instead of growing as ϱ². No published step-form model was found (search incomplete). It is a linear version of the earlier work's threshold alternative.

### 4. The cost (formulas from the check, §3)
The momentum transfer is exact, since only the kinetic energy fails to commute with the Π̂_x:
$$
\frac{d\langle p_{j,k}^2\rangle}{dt}=\Gamma_K\hbar^2\!\int\!\frac{d^3x}{V_c}\big\langle(\partial_{x_{j,k}}\hat\Pi_{\mathbf x})^2\big\rangle,\qquad \partial_{\mathbf x_j}\hat\Pi_{\mathbf x}=\frac{\sigma'}{\delta\rho}\,m_j\nabla G_{r_C}(\mathbf x-\mathbf x_j).
$$
- **A rigid saturated body's centre of mass** diffuses only through its threshold surface S_K:
$$
\frac{d\langle P_k^2\rangle}{dt}=\frac{\Gamma_K\hbar^2c_\sigma}{V_c\,\delta\rho}\oint_{S_K}|\nabla\varrho|\,n_k^2\,dA,\qquad c_\sigma=\int\sigma'^2du .
$$
- **Heating** occurs only in a thick threshold shell, such as a planetary or stellar interior where the density crosses ρ_K. A uniformly saturated bulk does not heat: the structural difference from CSL.
- **Every cost scales as Γ_K/δρ,** and the signature as Γ_K.

### 5. The signature, in CO's terms
**A sudden onset in size, at fixed material density.**
- A body of density ρ_b > ρ_K saturates once it is large enough: for a sphere, ϱ(0)/ρ_b = P(χ₃ < R/r_C), so R_K ≈ 1.5 r_C at ρ_K = ρ_b/2.
- Its decoherence rate then jumps from about Nλ (route (b)) to about Γ_K V_sat/V_c, within ΔR ~ r_C δρ/ρ_b.
- **Equal masses of different densities differ:** gold saturates where silica need not. That is Allen's point 1, at the scale r_C.
- **"Sudden," defined:** a jump of at least 10× in the decoherence rate within ΔR ≤ r_C.
- **The form testable today** is the onset in size of centre-of-mass force noise and heating. Interference needs superpositions of particles larger than about 0.14 μm (≳10¹⁰ Da).

### 6. What is to be registered (no values computed here)
- **Parameters:** ρ_K and Γ_K. δρ = ρ_K/10 and σ (compact support) are fixed.
- **The GRW-type rate at threshold,** the comparison: route (b) summed over one cell at ρ_K,
$$
\lambda N_{\rm cell}=\kappa_bc^2\rho_KV_c/\hbar .
$$
- **Bounds, each a separate criterion:**
  - centre-of-mass noise of bodies of size ~r_C (levitated nanospheres, cantilevers) and of LISA Pathfinder's test masses, where ρ_K is below their density;
  - Earth's heat, with a registered density and mineral model, where ρ_K lies in the Earth's density range;
  - stellar heating (the Sun's core, white dwarfs, neutron stars) for ρ_K above 2.26×10⁴ kg m⁻³;
  - SNO and XENONnT, only as narrow windows in ρ_K around their media's densities;
  - interference only if ρ_K < 0.03 kg m⁻³, plus proximity decoherence at material gratings;
  - Run 96's window for r_C (with B16), with r_C shared with route (b) (a choice, stated).
- **The outcome, in three cases:**
  1. **FAILS AS STATED:** no (ρ_K, Γ_K) with Γ_K ≥ 10·λN_cell survives at any r_C in the window. Then C4-β cannot differ from GRW in its distinctive way.
  2. **LEAD WITH A LABORATORY SIGNATURE:** some survive with ρ_K below laboratory densities. The registration names the density and size scales of the onset.
  3. **LEAD, NOT OBSERVABLE IN THE LABORATORY:** survivors exist only above 2.26×10⁴ kg m⁻³, where no laboratory body saturates.
- **The hold's ceiling** (Γ_K ~ c/ℓ ~ 10⁴⁰ s⁻¹) is registered as the first case. It is expected to be excluded.
- **Disclosure before hashing:** the check's feasibility estimates show room for case 2 against LISA (5 or more decades), and that Earth's heat may decide it at small r_C. The registration is therefore not blind on whether room exists.

### 7. Rulings (28 October; Allen: "do as you recomm")
1. **Saturation is route (c),** a third route to commitment beside routes (a) and (b). It reopens "route (b) is a rate, not a threshold" and "per unit" only as §3 names.
2. **A saturation commitment is a record:** it carries a stamp and a deposit and counts in λ_tot. Its effect on gravity's graininess, and so on Run 96's LISA floor, is open.
3. **δρ = ρ_K/10, with a compactly supported step,** registered as the cubic smoothstep S(s) = 3s² − 2s³ (c_s = ∫S′² ds = 1.2).
