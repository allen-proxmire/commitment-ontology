## 9zr. Run 47: can pulsar timing see a neutron star that pulls 4% less than its energy?

*20 October 2026. Allen: "Do 1, then 46c". Registered and hashed with its code before it was run (`apmass/PREREG_47.md`, 23:20 UTC on 19 October). A keyword name in the code was fixed before hashing; nothing was run before. An independent agent checked the run. Its corrections are included: K47a holds by construction; K47b's signal is mostly absorbed by a timing fit; the inertial mass is an assumption; the ζ₂ reading; the first-law statement; the double pulsar.*

**Question.** At neutron-star compactness (U_self ≈ 0.22), a bound pattern's draw, its **active** mass, is 4% short of its energy at infinity κω (Runs 46–46c).
- Its fall, by ω, is consistent with zero. So its **passive** mass, taken as the Killing energy's response to a potential, is κω.
- The engine has no inertia. **This run assumes its inertial mass is also κω**, so m_P = m_I. The alternatives are in Reading 4.
- Under that assumption, does a 4% active deficit clash with binary-pulsar limits?

**The engine's numbers.**
$$
m_A=(1-\delta)\,m_P,\qquad m_P=m_I\ (\text{assumed}),\qquad \delta\approx0.04\times(\text{share of the star's energy in such patterns}).
$$
- The δ is second order in the body's own potential: the miss is about 0.6–0.9 U·b, with b ≈ U.
- **The ζ₂ bound.** Pulsars bound the self-acceleration of eccentric binaries to |ζ₂| < 1.3×10⁻⁵ (Miao et al. 2020, ApJ 898, 69; arXiv:2006.09652).
  - That test needs an active mass that *varies with the companion's potential* differently from the passive mass.
  - A fixed ratio m_A/m_P per body, as here, gives only a periodic wobble (below).
- **In the engine, that variation is the gap between the draw-based and ω-based falls, Δ_draw − Δ_ω.**
  - It is −1.4 to −2.9×10⁻³ at finite grid (Run 46c) and not converged, about 100 times the bound.
  - **So the engine leaves that test unresolved; it does not pass it.** The dilation argument (§9zs) predicts zero in the continuum.
- **At weak field**, ζ₂ = 2(β − 1) ≈ −0.9 p_s/P₀ (Run 30). The newer bound then needs P₀/p_s ≳ 7×10⁴, which is inside the triple's ≳ 10⁵ (Run 45).

**The claim (analytic).** With m_P = m_I for every body, each body's acceleration in a Newtonian N-body system is
$$
\ddot{\mathbf x}_i=\sum_{j\ne i}G\,m_{A,j}\,\frac{\mathbf x_j-\mathbf x_i}{|\mathbf x_j-\mathbf x_i|^3},
$$
because the passive and inertial masses cancel. That is exactly an ordinary Newtonian system with masses m_A,j.
- The active-weighted centre is unaccelerated: Σ m_A,i ẍ_i = 0 by antisymmetry, whether or not the bodies' deficits differ.
- So there is no secular self-acceleration at any eccentricity.
- Every orbit is the ordinary one. Only the inertia-weighted centre wobbles, periodically.

**The check (registered).** An 8th-order integrator (DOP853, tolerance 10⁻¹³) ran each system twice:
- **A:** the pulsar with m_A = 0.96 m and m_P = m_I = m;
- **B:** an ordinary system with the pulsar's mass set to 0.96 m.

Both start from the same initial conditions, set by Kepler with the active masses.

| system | A against B, pulsar position | other measure | verdict |
|---|---|---|---|
| two-body, e = 0.6, 20 orbits | 1.2×10⁻¹² of a | active-weighted centre drift 2×10⁻¹⁵ of a per orbit; inertia-weighted centre wobbles by 7.8×10⁻³ of a, periodically | **K47a passes, by construction** |
| triple shaped like PSR J0337+1715 (1.438 + 0.198 M☉ at 1.63 d; 0.410 M☉ at 327 d), 3 outer orbits | 8.9×10⁻¹¹ of the inner orbit | — | **K47a passes, by construction** |
| the same triple with a real equivalence-principle violation, m_P = (1 + 10⁻⁶) m_I (C) | 7.0×10⁻⁴ of the inner orbit in raw positions. Most of that is a change of orbital periods, which a timing fit absorbs. Refitting an ordinary triple (masses and initial conditions, linearised; noise floor 1.6×10⁻¹²) leaves 7.5×10⁻⁹ of the inner orbit, or 3.6×10⁻⁹ along one line of sight (about 60–120 ns) | — | **K47b passes** (registered: > 10⁻⁹), by a margin of 4–7 after refitting |

**K47a is a tautology.**
- With m_P = m_I, A and B are the same equations; their accelerations agree to 1.5×10⁻¹⁶.
- The differences in the table are rounding error that grows over the run.
- So the integrations confirm the algebra; they do not test anything beyond it.

**Reading.**
1. **If passive and inertial mass are equal, binary-pulsar timing cannot see the engine's 4% active-mass deficit at Newtonian orbital order.** That holds in two-body and three-body systems, at any eccentricity.
   - A neutron star's measured mass is then its active mass.
   - In the engine that mass is up to about 4% below the sum of its constituents' energies at infinity.
2. **What pulsars do test is m_P against m_I:** the triple's Δ = (+0.5 ± 1.8)×10⁻⁶. That is the fall test of Runs 45–46c. The engine resolves it only to about 10⁻³; the dilation argument (§9zs) would carry it further.
3. **Where the deficit could still be seen:**
   - **Post-Newtonian orbital terms and radiation (the deciding open question).** The double pulsar J0737−3039A/B agrees with GR in its post-Keplerian parameters to about 10⁻⁴ (Kramer et al. 2021, Phys. Rev. X 11, 041050; arXiv:2112.06795). Suppose ED's post-Newtonian two-body law put inertial mass in one term and active mass in another. A 4% mismatch would then be about 100 times too large. The engine has no such law yet.
   - **The star's mass against its constituents.** For J0737−3039B, electron-capture supernova models give a baryonic mass of 1.358–1.375 M☉, against a gravitational mass of 1.2489 M☉ (Podsiadlowski et al. 2005, astro-ph/0506566; Newton & Li 2009, arXiv:0908.1731). That puts the binding energy at 0.11–0.126 M☉, a window of about 0.017 M☉. A 4% deficit on most of the star's mass is about 0.05 M☉.
     - The comparison depends on the formation model and the equation of state.
     - It is **a possible tension, not computed**.
     - SN 1987A's neutrinos, NICER and GW170817 are not independent tests here: their inferences depend on the equation of state.
4. **Which energy is inertial decides what the 4% means.** The engine fixes the active mass (the draw) and the fall, but not the inertia.
   - **Inertia = κω (this run's assumption):** the deficit is invisible at Newtonian order. Post-Newtonian order is open (item 3).
   - **Inertia = the far field, m_A**, as the boosted-field input (Run 34) suggests: the draw-based fall then fixes the passive mass. If that fall is zero (the dilation argument, in the continuum), all three masses are equal. The 4% is then only a first-law anomaly: how a star's mass relates to its constituents (item 3, second bullet).
   - **Mixed** (passive by draw, inertial κω): a 4% equivalence-principle violation, excluded by about 10⁴.
5. **As theory, it is a departure from GR, perhaps partly from the body model.**
   - In GR, adding a quantum whose energy at infinity is ħω to a static star raises its total mass by ħω to first order, when the star re-equilibrates at fixed baryon number and entropy (Hartle–Sharp; Sorkin–Wald–Zhang).
   - The quantum's own Tolman integral is not ħω in GR either: `body46.py` gives κ(ω + 2Σ|∇ψ|²), and the star's stress response makes up the rest.
   - The engine holds the body at fixed proper size by rule, not by re-equilibrating. So part of the 4% may come from that body model rather than from ED.

*Later (§9zu, post hoc): sized by exact hydrostatics, the stress turns the 4% deficit into a +0.6% excess, so the deficit analysed here may not exist. Run 50 is to settle it.*
