## Run 41: CO's rotating exterior at the remnant's spin (a calculation)

*19 October 2026. (step 3). Exteriors, method and reading rules were fixed and hashed (`strong/PREREG_41.md`, 12:49 UTC) immediately before the code was saved. The code itself was not hashed; it was not edited after the run. An independent agent checked the metric, the numbers and the verdict; its corrections are included.*

**Question.** Run 39 could not reach GW250114's remnant spin (a = 0.68) because it cut CO's rotating exterior at first order. Two exteriors exist at all spins. What does each give for the (2,2) ringdown at a = 0.68?

**The two exteriors** (G = c = M = 1).

**E — the engine's rule, taken literally.** The engine's current field is a linear Poisson field in lattice coordinates, so $g_{t\phi}=-2J\sin^2\theta/r$ holds exactly for the engine at all spins; it is not a truncation. Rotation reaches the clock field only through the body's quadrupole:
$$
U=\frac{M}{r}+\frac{Q\,P_2(\cos\theta)}{r^3},\quad Q=-q\frac{J^2}{M},\qquad g_{tt}=-e^{-2U},\quad g_{ij}=e^{2U}\delta_{ij}.
$$
The quadrupole depends on the body. Three values are taken:
- q = 0;
- **q = 5/7**, a rigid uniform ball whose draw carries the adopted motion weight 1 + 2v². That gives $Q=-\tfrac{4}{35}M\omega^2R^4$ with $J=\tfrac25MR^2\omega$. This is a leading-order (v²) value: reaching J = 0.68M² needs surface speeds of 0.85 or more for R ≤ 2M. So q = 0 to 1 is a bracket, not a prediction;
- q = 1 (Kerr's value).

**NJ — the Newman–Janis completion of CO's static metric** (Azreg-Aïnou's form). With $F=e^{-2M/r}$, $K=r^2e^{2M/r}$, $\rho^2=K+a^2\cos^2\theta$, $2\tilde f=K(1-F)$ and $\Delta=FK+a^2$:
$$
g_{tt}=-\Big(1-\frac{2\tilde f}{\rho^2}\Big),\quad g_{t\phi}=-\frac{2a\tilde f\sin^2\theta}{\rho^2},\quad g_{\phi\phi}=\frac{(K+a^2)^2-a^2\Delta\sin^2\theta}{\rho^2}\sin^2\theta,\quad g_{rr}=\frac{\rho^2}{\Delta}.
$$
- With Schwarzschild as the seed it gives exact Kerr. That was checked: light ring and damping time to all printed digits at a = 0, 0.3, 0.68 and 0.9.
- It agrees with CO's current field far away. Near the light ring its frame dragging is weaker: $-a(1-e^{-2M/r})$ against E's $-2a/r$ on the equator.
- **It is not derived from CO's rules.** Adopting it would change the engine's current field at strong field.

**Results** (eikonal (2,2) mode, CO / Kerr − 1 at the same mass and spin).

| exterior | a = 0 | a = 0.3 | **a = 0.68: frequency** | **a = 0.68: damping time** | quality factor f·τ at 0.68 | light ring at 0.68 |
|---|---|---|---|---|---|---|
| E, q = 0 | −4.4%, +4.6% | +9.2%, +31% | **+70%** | **−67%** | −44% | inside the throat |
| E, q = 5/7 | −4.4%, +4.6% | +3.9%, +20% | **+9.5%** | **−52%** | −47% | inside the throat |
| E, q = 1 | −4.4%, +4.6% | +2.5%, +15% | **+1.2%** | **−46%** | −45% | inside the throat |
| NJ | −4.4%, +4.6% | −7.3%, −0.1% | **−16.6%** | **−21%** | −34% | outside |
| GW250114, 90% | | | 0 to +4% | −10% to +9% | | |

**Verdict (as registered): every exterior fails at a = 0.68.** E's frequency can land inside the window (q = 1), but its damping time is about half of Kerr's. NJ's frequency is too low and its damping time too short.

The eikonal approximation's own error at a = 0.68 is larger than the registered 'marginal' band assumed: for Kerr's (2,2) mode it is +5.0% in frequency and −6.5% in damping time, against fitted values of Mω = 0.5267 and τ = 12.17M. Comparing eikonal with eikonal cancels much of it, and no verdict changes.

![Run 41](figures/41_rotating.png)

**Reading.**
1. **Under the adopted rules, in the scalar eikonal approximation, at the remnant spin LVK infers under GR, CO's spinning remnant does not ring like GW250114's.** Two independent signs:
   - **The engine's own exterior (E)** has no prograde light ring outside CO's throat from a ≈ 0.3–0.4. Its only prograde circular photon orbit lies beyond the throat, where it is far more unstable than Kerr's. Damping times are 0.33–0.54 of Kerr's, if that orbit sets the ringdown seen from outside at all, which is unclear.
   - **The standard completion (NJ)** keeps the light ring outside, but rings 17% low, and its damping time is 21% short.
   - **The quality factor f·τ does not depend on the mass.** For E it is 1.67–1.78 (eikonal Ωτ), below any Kerr value (minimum 2.00, at a = 0), so no choice of mass or spin can absorb it. NJ's is 2.069, 34% below Kerr's at a = 0.68 but equal to that of a nearly non-spinning Kerr (a ≈ 0.08). So NJ's failure assumes the spin LVK infers under GR. A joint shift in mass and spin could absorb NJ's (2,2) mode alone; its overtone or (4,4) mode would test that.
2. **What is not settled.**
   - These are eikonal modes of a scalar field, not CO's gravitational perturbations, which are not derived.
   - LVK infers the remnant's spin as well as its mass from the whole signal, assuming GR. A joint CO fit (inspiral, ISCO and ringdown together) has not been made.
   - The light ring's being outside the body is assumed. For E it lies inside the throat, which needs a body more compact than the throat.
3. **Run 28's flag becomes a tension the adopted rules cannot remove at this level of analysis.** The static exponential metric's strong field, completed either way, is what disagrees. Run 28 noted this is set by the pattern rule's exact nonlinear form ($c=N^2$ at all orders) and the clock map ($N=e^{-U}$), chosen for first-order agreement.
4. **What would remove it.** A strong-field input in the spirit of the others:
   - "outside matter, the field is GR's (Kerr's)", which keeps CO's possibility-limited core in place of a horizon (Paper_042: no singularity);
   - or a derivation that changes the pattern rule or the clock map beyond first order.
   - **This needs a ruling.** Bodies whose surface sits just outside the would-be horizon (horizonless compact objects) ring like Kerr at first, and differ through late echoes, which have their own bounds.
