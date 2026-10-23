## Run 11b: shear of relations

**Question.** Run 11 found that the cadence field alone radiates 1/6 of what binary pulsars lose. Its reading said the missing radiation must come from **shear**: relations stretched one way and squeezed the other, travelling at $c$. This run gives relations a full strain field and measures what an orbiting pair radiates into it. It does this under two ways of counting what is real.

**Target, fixed in advance.** As in Run 11, the target is GR's quadrupole power for a circular binary:

$$
P_{\rm GR}=\frac{32}{5}\,\frac{G\mu^2a^4\omega^6}{c^5}
$$

The double pulsar (Kramer et al. 2021) agrees with this to $1.3\times10^{-4}$. So any extra radiation channel is excluded unless it is at least ten thousand times weaker than GR's.

A pre-registration (`PREREG.md` in the bundle) was written before any run. It fixes the predictions and the reading below.

### Field

Relation strain is a symmetric $3\times3$ field $s_{ij}$ with six components. Each component is a wave at $c=1$, sourced by the stress of matter:

$$
\ddot s_{ij}=\nabla^2 s_{ij}+16\pi G\,T_{ij},\qquad G=\frac{1}{16\pi}\ \text{(lattice units)}
$$

This is linearised gravity in harmonic gauge, restricted to its spatial part. At this order "each component is a wave" and "linearised GR" are the same equation.

Energy flux through a sphere of radius $R$, time-averaged:

$$
S=-\frac{1}{32\pi G}\,\big\langle\dot s_{ij}\,\partial_r s_{ij}\big\rangle=-\tfrac12\big\langle\dot s_{ij}\,\partial_r s_{ij}\big\rangle,\qquad P=\oint S\,R^2\,d\Omega
$$

### Source: the bodies and the relations that bind them

The two bodies have equal masses $m_b$, sit at separation $a$, and orbit at angular frequency $\omega$. The reduced mass is $\mu=m_b/2$. Their stress has two parts:

- **Bodies:** each carries its momentum flux, $m_b\,v_iv_j$, on a Gaussian blob of width $s=1.5$.
- **Relations binding the pair:** the line joining the bodies carries the binding tension, $-F\,\hat n_i\hat n_j$ with $F=\mu\omega^2a$. Here $\hat n$ is the unit vector from one body to the other. The tension is spread over 16 blobs along the line.

Together they give exactly the source the quadrupole formula needs. With $\hat t$ the direction of motion:

$$
\int T_{ij}\,d^3x=\underbrace{\mu\omega^2a^2\,\hat t_i\hat t_j}_{\text{bodies}}\;\underbrace{-\;\mu\omega^2a^2\,\hat n_i\hat n_j}_{\text{relations}}=\tfrac12\,\ddot I_{ij},\qquad I_{ij}=\sum m\,x_ix_j
$$

The tension is not optional. Momentum conservation, $\partial_\mu T^{\mu\nu}=0$, requires that whatever holds the pair together carries stress. In GR that stress lives in the Newtonian field itself, spread through space. For the quadrupole only its integral matters, and a line of tension between the bodies has the same integral. In the ontology's terms: **the binding lives in the relations between the bodies, and those relations are under tension.**

### Splitting the radiation by polarisation

At each point on the sphere, with outward direction $\hat n$ and transverse projector $P_{ij}=\delta_{ij}-n_in_j$, the strain splits into four parts that do not mix:

| Part | Projection | What it does to relations |
|---|---|---|
| TT (plus and cross) | $s^{TT}=PsP-\tfrac12P\,\mathrm{tr}(PsP)$ | stretch one way, squeeze the other, across the direction of travel: **shear** |
| breathing | $\tfrac12P\,\mathrm{tr}(PsP)$ | uniform stretch across the direction of travel |
| longitudinal | $\hat n\hat n\,(\hat n\cdot s\cdot\hat n)$ | stretch along the direction of travel |
| vector | $s-PsP-\hat n\hat n\,(\hat n\cdot s\cdot\hat n)$ | shear between the direction of travel and across it |

The power in each part is the same flux integral, taken with that part alone.

### Two countings of what is real

- **(R) Relations are all there is.** Two rules together leave only TT.
  - **Sliding places is free.** Space is who relates to whom, so places have no identity apart from their relations. Sliding every place by a small amount, $x\to x+\xi(x)$, changes the strain by $\partial_i\xi_j+\partial_j\xi_i$. That relabels the places but changes no relation, so it can carry no energy. For a wave travelling along $\hat n$, this is exactly the vector and longitudinal parts.
  - **Isotropic stretch is bound to matter.** The breathing part cannot be made by sliding. It is a uniform stretch, the same kind of quantity as capacity. Under the reading fixed in advance, it is set by matter at each moment rather than radiating. That is the same rule the pre-registration applied to the capacity scalar; see Reading 3.
  - *Wording corrected while writing up:* the pre-registration said sliding alone removes every non-TT part. It removes the vector and longitudinal parts only. Prediction R1 (TT ÷ GR) is unchanged.
- **(E) Every strain pattern is real.** Places have identity, and stretch radiates freely. **All six components count.**

### Predictions (pre-registered)

The radiation-zone field is $s_{ij}\propto\ddot Q_{ij}(t-r)/r$ with $Q=\tfrac12\ddot I$ traceless. Per unit $Q{:}Q$, its angular integrals are:

$$
\textstyle\int\!\big|s^{TT}\big|^2d\Omega=\frac{8\pi}{5},\quad \int\!\big|s^{\rm vec}\big|^2d\Omega=2\!\int\!|PQ\hat n|^2d\Omega=\frac{8\pi}{5},\quad \int\!(\hat nQ\hat n)^2d\Omega=\frac{8\pi}{15},\quad \int\!\big|s^{\rm br}\big|^2d\Omega=\frac{4\pi}{15}
$$

These four sum to $4\pi$.

- **R1.** $P_{TT}/P_{\rm GR}=1.00$. The window is ±0.05 after the body-size factor $e^{-(2\omega s)^2}$ is divided out. A result outside it would mean the source or the counting is wrong.
- **E1.** $P_{\rm all}/P_{\rm GR}=4\pi\big/\tfrac{8\pi}{5}=2.5$.
- **E2.** Shares of $P_{\rm all}$: TT 0.400, vector 0.400, longitudinal 0.133, breathing 0.067.
- **Checks:** the power follows $\omega^6$, and it does not depend on the sphere's radius.

### Method

- **Lattice:** 171³, with an absorbing layer 30 wide ($\sigma=0.3\,((W-d)/W)^2$). Leapfrog with $dt=0.5$. All six components are evolved together.
- **Switch-on:** the source is turned on over $t=200$ with a cosine ramp. The run then settles for the light-crossing time plus 4 radiation periods.
- **Measurement:** a lock-in at $2\omega$ over 12 whole radiation periods. It records $\dot s_{ij}$ and $\partial_r s_{ij}$ at every lattice place on the sphere (31,742 places at $R=50$). Flux per part is $-\tfrac14\,\mathrm{Re}\big(\Pi\dot{\tilde s}:\Pi\partial_r\tilde s^{*}\big)$.
- **No reference field.** Run 11 needed one; here the lock-in over whole periods rejects the static part of the source.
- **Sweep:** $a=3,4$; $\omega=0.05$–$0.12$; $R=40,50,60$.
- **Control:** the binding tension switched off, leaving only the bodies.

### Results

All values are power ÷ GR, with the body-size factor divided out.

| a | ω | (ωa)² | body-size factor | **TT ÷ GR** | all six ÷ GR | all ÷ TT |
|---|---|---|---|---|---|---|
| 4 | 0.05 | 0.040 | 0.978 | 0.973 | 2.424 | 2.493 |
| 4 | 0.065 | 0.068 | 0.963 | 1.008 | 2.517 | 2.498 |
| 4 | 0.08 | 0.102 | 0.944 | 0.979 | 2.437 | 2.490 |
| 4 | 0.10 | 0.160 | 0.914 | 0.975 | 2.423 | 2.486 |
| 4 | 0.12 | 0.230 | 0.878 | 0.964 | 2.392 | 2.481 |
| 3 | 0.08 | 0.058 | 0.944 | 0.987 | 2.461 | 2.494 |
| 3 | 0.10 | 0.090 | 0.914 | 0.988 | 2.461 | 2.492 |
| 3 | 0.12 | 0.130 | 0.878 | 0.983 | 2.446 | 2.489 |
| 4 (R = 40) | 0.08 | 0.102 | 0.944 | 0.979 | 2.437 | 2.490 |
| 4 (R = 60) | 0.08 | 0.102 | 0.944 | 0.977 | 2.433 | 2.490 |
| **mean of 10** | | | | **0.981 ± 0.012** | **2.443 ± 0.033** | **2.490 ± 0.005** |
| 4, tension off | 0.08 | 0.102 | 0.944 | 0.241 | 0.602 | 2.498 |

**Polarisation shares**, mean of 10 runs, with the prediction in brackets:

| TT | vector | longitudinal | breathing |
|---|---|---|---|
| 0.402 (0.400) | 0.398 (0.400) | 0.135 (0.133) | 0.065 (0.067) |

**The same parts in units of GR:**
- vector + longitudinal (what sliding removes): 1.30 ± 0.02 (predicted 1.33)
- breathing (isotropic stretch): 0.159 ± 0.004 (predicted 1/6)

The breathing figure is the same size as Run 11's cadence field, which gave 0.166.

**Checks:**
- **Frequency law.** Power against $\omega$ has log-slope 5.98 at $a=4$ and 5.99 at $a=3$, against the expected 6.
- **Sphere radius.** Spheres at 40, 50 and 60 agree to 0.16%.
- **Small shortfall.** TT sits 1–3.5% below 1, and the shortfall grows with $(\omega a)^2$. A straight-line fit (excluding ω = 0.05) gives $\mathrm{TT/GR}=1.005-0.18\,(\omega a)^2$. This is what finite source size beyond the quadrupole approximation does. At ω = 0.05 the absorbing edge reflects a few percent, as it did in Run 11.

**Tension-off control** (not in the pre-registration document). Without the binding tension, only the bodies' $\mu\omega^2a^2\,\hat t\hat t$ remains. Of that, only half oscillates:

$$
\hat t\hat t=\tfrac12(\hat t\hat t+\hat n\hat n)+\tfrac12(\hat t\hat t-\hat n\hat n)
$$

The first term is constant, so the expected power is $(\tfrac12)^2=0.25$ of GR. Measured: 0.241. **Half of the radiating stress amplitude lives in the relations that bind the pair.**

### Against the pre-registration

| Prediction | Expected | Measured | |
|---|---|---|---|
| R1: TT ÷ GR | 1.00 ± 0.05 | 0.981 ± 0.012 | **pass** |
| E1: all six ÷ GR | 2.5 | 2.443 (all ÷ TT: 2.490 ± 0.005) | **pass** |
| E2: shares TT / vector / longitudinal / breathing | 0.400 / 0.400 / 0.133 / 0.067 | 0.402 / 0.398 / 0.135 / 0.065 | **pass** |
| ω⁶ law | slope 6 | 5.98, 5.99 | **pass** |
| independent of sphere radius | — | 0.16% | **pass** |

### Reading

**1. With "relations are all there is", shear gives GR's binary radiation: 0.98 of GR, within the pre-registered window.**
- What survives is two polarisations, plus and cross. This is what LIGO/Virgo's three-detector events favour.
- The two rules behind the counting are the ontology's own, not fitted:
  - sliding places is free, which follows from "space is who relates to whom"
  - isotropic stretch is bound to matter, which is the capacity rule in Reading 3

**2. "Every strain pattern is real" is excluded.**
- It radiates 2.44× GR. Of that, 40% is vector, 13% longitudinal and 7% breathing.
- The double pulsar allows about $10^{-4}$ beyond GR, so this is off by four orders of magnitude.
- Places cannot have identity apart from their relations.

**3. Isotropic stretch, capacity included, must not radiate energy of its own.**
- Two isotropic channels would each add about 1/6 of GR if they radiated freely:
  - the breathing part here: 0.16
  - the capacity (cadence) scalar of Runs 1–10: 0.17 (Run 11)
- Either one alone already takes the total to 1.15 of GR, which is excluded.
- **What works is a constraint.** These fields are set by where matter is at each moment, not by a wave equation of their own. GR works the same way: in its gauge-invariant split (Flanagan & Hughes 2005), only the TT part obeys a wave equation. The scalar parts, the Newtonian potential and the isotropic spatial stretch, obey Poisson-type equations tied to matter.
- Light bending (Run 9) and the perihelion (Run 10) use only the static profiles, so they are untouched.
- **Open question for CO's event layer:** how does the capacity shortage follow moving matter without being a wave?
  - A Planck-step random walk is far too slow to keep up.
  - Ballistic spreading at $c$ radiates.

**4. The binding lives in relations.** With the tension off, the power falls to a quarter. The relations holding the pair together must carry stress, and that stress radiates as much as the bodies' motion does.

**5. What this is and is not.**
- **Is not:** a new prediction. This is linearised GR, so the run shows that the ontology *can* carry it, and which readings of the ontology cannot.
- **Is (the CO content):**
  - sliding places is free, which follows from "space is who relates to whom"
  - isotropic stretch and capacity are bound to matter, with no waves of their own
  - binding tension in the relations

**6. Saddles.** CO's earlier saddle-shaped geometry was tidal: the Hessian of a scalar, i.e. second derivatives of capacity. That is a static stretch-and-squeeze around a mass. It is not this shear, which is a travelling wave of its own.

**7. Pointer forward.**
- The physical part of shear, what survives relabelling, is curvature: the mismatch accumulated going around a closed loop of relations.
- That is the same square-loop structure Run 13 needed to hold knots.
- So the natural next construction is Regge-like dynamics on the random cubical complex: shear as loop mismatch, on the same substrate that holds particles.

![Run 11b](figures/11b_shear.png)

---

