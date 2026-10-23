# Design note: a spherical lattice for a hole, under two readings of how the medium's space curves

22 October 2026. This note follows Run 77 and the two readings kept as options to test (22 October): **(A)** space is the pattern of relations, so curving it means relations form, dissolve or rewire; **(B)** relations stay fixed, and space is read from the medium's state across them. It records first how relations form and dissolve, then how an option-3 hole would be built in the engine under each reading, and what a run could and could not test. It is a calculation; no engine run was made. Numbers come from `sphere78/design78.py` (outputs `design78.json`, `design78_candidates.json`). An independent agent checked sections 2–8 with its own code (`check5759/w78/`); its corrections are included, and listed at the end.

## 1. Can relations form or dissolve?

**Stated (22 October):**
- A dissolved link goes back to possibility.
- A relation has two parts, so it dissolves into a possibility pattern with two parts, as in entanglement.
- Three-dimensional space is assumed for now. How space itself forms is not the question here.

**What this means for the two readings.**
- **Both stay open.** Under (A), relations around a hole can dissolve and re-form so that their pattern has option 3's shape, inside an assumed three-dimensional space. Under (B), they stay put and the medium's state across them carries the shape.
- **A dissolved relation keeps its two ends tied.** If it leaves a two-part possibility pattern, re-forming would favour the same pair of places, or places near them. That keeps re-forming local, which (A) needs if the relational pattern is to stay three-dimensional while it reshapes.
- **Persistence by renewal (a note of 22 October).** Matter persists by re-committing, and that renewal is what lets it be cut, moved and recombined: a commitment that persisted without renewal could never be reconfigured. The same holds for the medium's space under (A). For it to curve under option 3 its relations must be able to dissolve and re-form; for it to keep its shape, they must re-form near where they were.
- **Precedents for (B):** relations already carry a state in the record. In Run 11b relations shear, and isotropic stretch is set by matter. In Note E's second picture possibility hops on physical space at the local tick rate, since √γ̃γ̃^{ij} = N√g g^{ij}.
- Rulings and models from the earlier attempts (A–C) about how space forms are not relied on here.

## 2. The target: an option-3 hole with the ruled core

**The exterior** (Run 67; in vacuum the equations for γ̃ and φ do not involve the medium):
$$
\tilde\gamma=dr^2+h(r)^2d\Omega^2,\qquad h^2=r(r-2m),\qquad \varphi(r)=\tfrac12\ln\frac{r\,(R-2m)}{(r-2m)\,R},
$$
with φ = 0 at the reservoir shell r = R, where released possibility re-enters (as in Run 77). The medium's fugacity is z(r) = z_R − cφ(r), the occupancy P(r) = R_eq(z) (the zero-range equation of state, Run 22; section 3 corrects it for the engine's update), and the clock N = P/P_R. Run 67's mean-field form, adapted here to a reservoir at finite R (N = (1+ε)n − ε with ε = p_s/P_R and n the GR lapse normalised at the reservoir), differs from R_eq by up to 0.02 just outside the throat and by 0.015 at the core (6–8% of N_c), so R_eq is used.

**Landmarks:**
- **the core:** where P = 2p_s (the ruling of 21 October), so N_c = 2p_s/P_R;
- **the throat:** the minimum of the areal radius h/N (Run 67);
- **the light ring:** the minimum of h/N².

**The flux a mass m needs.** On a lattice of equal places with c_n = 1, the mean current between shells is (A(r)/6)·Δz, with A = 4πh² the shell's area in γ̃. A steady inward flux Φ gives
$$
\varphi(r)=\frac{6\Phi}{c\,c_n}\int_r^R\frac{dr'}{4\pi r'(r'-2m)}=\frac{6\Phi}{8\pi mc\,c_n}\ln\frac{r\,(R-2m)}{(r-2m)\,R},\qquad\text{so}\qquad \Phi=\frac{2\pi mc\,c_n}{3}.
$$
Far out φ ≈ 6Φ/(4πc·c_n r) = m/r, the same statement. **The medium's curvature** is R̃ = 2|∇̃φ|² = 2m²/h⁴, largest at the core.

**Resolution: ε must be about 1/8–1/10.** In γ̃, distances near the hole are short: the whole region from the core to the throat sits close to r = 2m.

| P_R (ε) | m | core: r_c − 2m | throat: r − 2m | core shell, places |
|---|---|---|---|---|
| 64 (1/64, Run 77's medium) | 12 / 20 | 0.02 / 0.03 | 0.35 / 0.59 | 6 / 17 |
| 16 (1/16) | 12 / 20 | 0.33 / 0.54 | 1.55 / 2.58 | 99 / 276 |
| 10 (1/10) | 12 / 16 | 0.83 / 1.11 | 2.45 / 3.27 | 260 / 462 |
| 8 (1/8) | 12 / 16 | 1.30 / 1.73 | 3.04 / 4.05 | 413 / 734 |

(Lattice spacing 1, reservoir at R = 4m.) At Run 77's ε the core lies a few hundredths of a spacing from r = 2m, inside the first shell. At ε = 1/8–1/10 the core is about one spacing out and the throat about two shells beyond it (1.6–2.3 shells).

**Redshifts are relative to the reservoir,** which sits at GR lapse 0.71 for R = 4m. Relative to infinity the core's redshift would be 5.7 (ε = 1/8) or 7.1 (1/10), not 4 or 5. And at these ε the hole is shallow: the core's areal radius is about 2.7m relative to infinity, against 3m at physical ε (Run 74).

## 3. What the medium alone can and cannot test

**One identity is exact on any graph and with any update.** The mean current along a relation is
$$
\langle J_{xy}\rangle=\frac{W_{xy}}{6}\,(z_x-z_y),\qquad z=\langle f(P)\rangle ,
$$
because each unit leaves with probability f(P)/P and then takes relation k with probability W_k/6. So the shell-averaged z solves Σ_y W_xy(z_x − z_y) = 6s_x exactly, with s_x the net source at x (measured to 0.9995–1.0002, the check). **The medium's z-profile cannot fail on any graph.** This is why Run 77's K77b held, as its check found.

**The occupancy at given z is not the zero-range equation of state at low P.** In continuous time the medium would be a zero-range process, whose stationary state is a product of one-place distributions with P = R_eq(z) (a Jackson network). The engine updates every unit at once, once per tick: binomial departures, then a choice of relation. That update is not product-form (the check, exactly on two- and three-place systems). On a uniform lattice with ΣW = 6, the mean P at given z falls below R_eq(z):

| P | 2 | 4 | 8 | 16 | 64 |
|---|---|---|---|---|---|
| ⟨P⟩/R_eq(⟨f⟩) − 1 (the check, 32³) | −3.1% | −2.7% | −1.7% | −0.8% | −0.12% |
| the same, a second measurement (20³) | −3.0% | | −1.6% | | −0.13% |

- The variance is 12–17% below the zero-range value, and neighbouring places are weakly correlated (+0.02 to +0.035).
- The departure shrinks in proportion to ΣW (−0.36% at ΣW = 1), so it also depends on each place's own total.
- Run 77's K77c (clocks against R_eq) passed as a ratio at P ≈ 45–80, where the departure is about 0.1% and cancels.
- **A possible explanation for Runs 72b–76 (not tested).** The zero-range theory underestimated these clocks' own dips by 0.25% (design 1) and 0.5–0.6% (design 2), the same on every lattice. A clock depletes its own places, and the engine's departure grows as P falls, so the engine's dips should come out deeper than R_eq predicts. The sign fits, and so does the independence from the lattice. Whether the size fits is not known: it depends on the departure at the clocks' own places and on Run 72's hop-rate factor (c_n = 0.45, which shrinks the departure in proportion). Recomputing Run 72's theory with the engine's own equation of state would test it in minutes.

**What a static run can test is therefore:**
- the engine's own equation of state at low P (which any hole theory needs first);
- matter in the medium: the core, whose pairs hold and renew, and clocks, whose dips depend on their local relations.

## 4. Building it under (A): shells counted from option 3's areas

- **Shells** at r_n = r_c + n (n = 0 the core shell, the last the reservoir), with
$$
M_n=\mathrm{round}\big(4\pi\,r_n(r_n-2m)\big)
$$
  places: each place is one unit of γ̃'s volume, about one spacing across in every direction.
- **Tangential relations:** each shell triangulated (points spread evenly on the sphere, cotangent weights). An equilateral cell of unit area gives a tangential sum of 6/√3 ≈ 3.46 per place; a real triangulation (5-, 6- and 7-neighbour places) gives 3.55–4.0.
- **Radial relations:** weighted by the overlap of each place's cell with the cells of the neighbouring shell, so the total between shells n and n+1 is the shell's series conductance, G_{n+½} = 1/∫_{r_n}^{r_{n+1}}dr/A(r) (≈ A(r_{n+½}) away from the core). Series conductances, and a reservoir placed exactly on the last shell (R − r_c an integer), remove the discretisation error that midpoint conductances leave (P at the core 2.06–2.08 instead of 2).
- **Relations are equal per unit area of γ̃, not per place.** Near the core the place count doubles within one spacing, so radial shares per place run 1.31–1.63 out of the core shell and 0.71–0.81 into the next. With overlap weights the largest per-place total is 6.00 (built explicitly, 142,000–349,000 places): c_n = 1, with no margin. Nearest-place radial links of equal weight would give 8.7, so c_n ≈ 0.69.
- **Engine changes:** neighbour lists of varying length instead of six (about 1.5× the cost per place, the check); release over the reservoir shell; a hold kH that need not be an integer; and an even number of places in the core shell, so it can be filled with pairs. The hop rule is unchanged: a unit leaves with probability f(P)/P and takes relation k with probability W_k/6.

## 5. Building it under (B): fixed relations, hops set by the medium's state

The relations are those of flat space: shells at radii ρ_n = ρ_c + n holding 4πρ_n² places each. (A cubic block cannot carry radial-versus-tangential differences, Note F, so (B) also needs shells.) Equal places map the graph to γ̃ by ρ²dρ = h²dr. Each relation's conductance is its γ̃ cross-section over its γ̃ length:
$$
W_r=\Big(\frac{h}{\rho}\Big)^{4},\qquad W_t=\Big(\frac{\rho}{h}\Big)^{2},\qquad \frac{W_t}{W_r}=\Big(\frac{\rho}{h}\Big)^{6}.
$$
- The inner radius ρ_c is free. Chosen to minimise the largest per-place total, the anisotropy stays at 2.0–2.1 (ε = 1/8) and 2.5–2.6 (1/10); at ε = 1/64 it reaches about 40.
- **The hop rate.** A sphere has no square grid, so (B)'s shells must be triangulated too. Like for like with (A), c_n ≈ 0.95–1.0 (0.984 and 0.949 on real triangulations); with a 4-neighbour stencil it would be 0.91–0.95, and 0.43 at ε = 1/64.
- **In a static run these conductances are imposed from option 3's solution,** as in Run 77. For a spherical vacuum hole, φ and |∇̃φ| fix r and m locally (and ρ³ = r³ − 3mr² + C, with C ∝ m³), so a directional rule W(φ, ∇̃φ) can reproduce the whole family of holes. For other configurations the equal-volume map is non-local and no pointwise rule gives it. A general rule for (B) would evolve the conductances by a local equation whose solution is option 3's γ̃ (Note E, route 2), and it must avoid the freezing found in Run 17.

## 6. Where the readings differ

| | (A) shells from option 3's areas | (B) flat relations, state-set hops |
|---|---|---|
| the medium's profile z(r) | option 3's, up to discretisation error (removed by series conductances) | the same |
| relations near the core | equal per unit area; per place, radial shares differ by up to 2× | radial and tangential differ by up to 2.6× |
| hop rate | c_n = 1, just | c_n ≈ 0.95–1.0 |
| clocks near the core | dips set by their local relations | dips set by anisotropic relations; near the core the difference from (A) is dominated by the update's equation-of-state departure, which varies with each place's total |
| how the geometry forms | relations dissolve into two-part possibility patterns and re-form; no rule yet | conductances evolve; no rule yet |

So a static run separates the readings only through clocks near the core, where the theory's own equation-of-state error (about 3% at P = 2–4) would have to be corrected first. **The readings separate for real in dynamics:** how the geometry comes to be option 3's.

## 7. Candidate static designs

ε = 1/8 or 1/10, reservoir at R = 4m. Relaxation times are from a linearised mean-field model that reproduces Run 77's check exactly (6,375 and 12,564 ticks); this lean medium (P ≤ 10) responds 6–8× faster than Run 77's, and most of the volume sits near the reservoir. Run length is then set by the reading window, 25,000 ticks, at about 0.56 µs per place per tick for variable neighbour lists (the check).

| P_R | m | core: r_c − 2m, places, redshift (to the reservoir), R̃ | throat: r − 2m, N | light ring | shells, places (A) | relaxation (ticks) | per run (25,000 ticks) |
|---|---|---|---|---|---|---|---|
| 8 | 12 | 1.30, 413, 4.0, 0.27 | 3.04, 0.43 | 38.0 | 23, 142,000 | 790 | about 0.55 h |
| 10 | 12 | 0.83, 260, 5.0, 0.67 | 2.45, 0.40 | 37.3 | 24, 150,000 | 1,030 | about 0.6 h |
| 8 | 16 | 1.73, 734, 4.0, 0.15 | 4.05, 0.43 | 50.6 | 31, 349,000 | 1,450 | about 1.35 h |
| 10 | 16 | 1.11, 462, 5.0, 0.38 | 3.27, 0.40 | 49.7 | 31, 333,000 | 1,730 | about 1.3 h |

- **The core** would be committing pairs filling the core shell (Run 77's mechanism), drawing σ = 2P/(kH) per place (H = 640), with k fixed beforehand from the theory so that the self-consistent hole holds P = 2p_s at the core. For P_R = 8, m = 16 this needs Φ ≈ 48 units per tick, about 0.065 per core place, so k ≈ 0.096 (0.071, 0.044 and 0.059 for the other three designs). The draw law assumes a pair re-commits at once; at P = 2 a place is empty 16–19% of ticks, so the theory's draw is approximate at the few-per-cent level unless waiting is modelled.
- **Clocks' design-dependent effect** is non-local, about 0.01·R̃·h·ℓ_c (Run 70's check). Runs 72/72b measured design-gap shifts of 0.2–0.8% at R̃ = ±1.1 over a 6-spacing period. Here R̃ = 0.15–0.7 extends over only 1–2 spacings, which suggests about 0.1% or less: likely below what 20 seeds resolve (±0.2%). And at P = 2–4 the zero-range theory's equation of state is itself off by about 3% (section 3), so it needs that correction first.

## 8. Choices

| choice | what it tests | cost |
|---|---|---|
| (0) Measure the engine's own equation of state at low P, and recompute Run 72's clock theory with it | whether the update explains the theory's 0.25–0.6% underestimate of clock dips (Runs 72b–76); the corrected theory any hole run needs | minutes; no registration needed for the measurement, one for the test |
| (i) A static hole under (A) | the ruled core holding the hole's flux with 2–4 units per place, in strongly curved space (R̃ up to 0.7); clocks at redshift 4–5 (to the reservoir) against the corrected theory | engine changes (section 4); about 0.6 h per run at m = 12 |
| (ii) (i) plus the same hole under (B) | whether the representation changes clocks near the core; the difference is dominated by the update's equation of state, which varies with each place's total | about twice (i) |
| (iii) Design a rule for how the geometry forms, for each reading | (A): relations dissolving into two-part possibility patterns and re-forming near where they were, toward option 3's areas, in assumed 3D space; (B): conductances evolving locally toward option 3's γ̃ without Run 17's freezing | design work and rulings before any run |

The plan: (0) first, since it is cheap and every later theory needs it. (iii) is where the readings actually separate. (i) is a first platform for any later dynamical run, and its core test is new; (ii) adds little until the theory is corrected for the update.

## 9. What the check added

1. **The product-form claim was wrong for the engine.** Only the mean-current identity is exact on any graph; the occupancy at given z departs from the zero-range equation of state by −3% at P = 2 to −0.1% at P = 64 (section 3). A second measurement reproduced it.
2. **"c_n = 1, largest total 5.47" assumed ideal cells.** Built explicitly, overlap weights give 6.00 (c_n = 1, no margin), and nearest-place weights would give c_n ≈ 0.69. Relations are equal per area, not per place.
3. **The relaxation times were about ten times too long.** Runs take about 0.55–0.6 h (m = 12) and 1.3–1.4 h (m = 16), not 0.6–2.8 h.
4. **The clock effect near the core was overstated:** about 0.1% or less, not 0.15–0.7%.
5. **(A) and (B) agree on z(r) only up to discretisation error**; series conductances remove it.
6. **A directional rule W(φ, ∇̃φ) can reproduce spherical holes;** it fails only for other configurations.
7. **(A) and (B)'s hop rates differ mainly through the stencil,** not the reading; like for like they are 1 and 0.95–1.0.
8. **Redshifts are to the reservoir,** and the hole at these ε is shallow (core at about 2.7m relative to infinity).
