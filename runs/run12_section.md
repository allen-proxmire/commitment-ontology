## Run 12: particles as knots (D14)

**Claim tested.** A particle is a knot of commitments that cannot be cut. Its mass is the cost of holding the knot.

**Target fixed in advance.** A director field with an alignment term and a squared-winding term is the Faddeev–Skyrme model. Its knotted solitons (hopfions) have known continuum energies, from Sutcliffe 2007 (arXiv:0705.1468):

| Q | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $E_Q$ (Faddeev units) | 1.204 | 1.967 | 2.754 | 3.445 |
| $E_Q/E_1$ | 1 | 1.634 | 2.287 | 2.861 |

### Model

Each node carries a unit director $\mathbf n_i\in S^2$: the orientation its commitments hold. The vacuum is $\mathbf n=(0,0,-1)$.

**Coh (alignment)** is the cost of neighbouring commitments disagreeing:

$$
E_{\rm coh}=h\sum_{\langle ij\rangle}|\mathbf n_j-\mathbf n_i|^2\;\longrightarrow\;\int|\partial\mathbf n|^2\,d^3x
$$

**Str (holding a topological commitment)** is the squared winding density. On the lattice it is the symmetric "four-corner" form, the squared area that each corner's two links sweep on the sphere:

$$
E_{\rm str}=\frac1h\sum_i\sum_{a<b}\tfrac14\sum_{s_a,s_b=\pm}\big|(\mathbf n_{i+s_a\hat a}-\mathbf n_i)\times(\mathbf n_{i+s_b\hat b}-\mathbf n_i)\big|^2\;\longrightarrow\;\int\sum_{a<b}|\partial_a\mathbf n\times\partial_b\mathbf n|^2\,d^3x
$$

The energy in Faddeev units is

$$
E=\frac{1}{32\pi^2\sqrt2}\,\big(E_{\rm coh}+E_{\rm str}\big).
$$

**Uncuttable rule (D14).** A relation may bend by up to 60° at no cost but may not flip:

$$
E_{\rm cut}=k_b\,h\sum_{\langle ij\rangle}\max\!\big(0,\;1-\mathbf n_i\cdot\mathbf n_j-c_0\big)^2,\qquad c_0=0.5,\;k_b=2000 .
$$

**Knot number (Hopf charge).** With $B_i=\tfrac12\epsilon_{ijk}\,\mathbf n\cdot(\partial_j\mathbf n\times\partial_k\mathbf n)$ and $\nabla\times\mathbf A=\mathbf B$ (solved by FFT, fourth-order differences):

$$
Q=\frac{1}{16\pi^2}\int\mathbf A\cdot\mathbf B\,d^3x .
$$

**Why Str is needed (Derrick).** Under a rescaling $x\to\lambda x$:

$$
E_{\rm coh}\to\lambda\,E_{\rm coh},\qquad E_{\rm str}\to E_{\rm str}/\lambda .
$$

- Coh alone always lowers its energy by shrinking, so it has no stable size.
- Coh + Str has a minimum at $E_{\rm coh}=E_{\rm str}$ (virial = 1).
- The knot's size and mass then come from the two couplings: $R\sim\sqrt{k_{\rm str}/k_{\rm coh}}$, $M\sim\sqrt{k_{\rm coh}k_{\rm str}}$, and $M R\propto k_{\rm str}$.

**Seeds.** A compact rational-map ansatz, exactly vacuum beyond radius ρ, so the periodic box has no seam:

$$
Z_0=\cos f+i\tfrac{z}{r}\sin f,\quad Z_1=\tfrac{x+iy}{r}\sin f,\quad f=\pi(1-r/\rho),\quad W=Z_1^{\,m}/Z_0^{\,k},\quad Q=mk .
$$

**Relaxation.** FIRE on the sphere, with each site's step capped at 0.02 so there are no jumps that could cut. This is followed by plain projected gradient flow as a stability check.

### Results

**(a) Spectrum.** N = 80, h = 0.2 (box 16), Coh + Str, no cutting rule.

| Q | Seed (m, k) | E (lattice) | E (Sutcliffe) | $E_Q/E_1$ | $E_Q/E_1$ (Sutcliffe) | Q measured | Virial $E_{\rm coh}/E_{\rm str}$ | Core radius | max \|grad\| |
|---|---|---|---|---|---|---|---|---|---|
| 1 | (1,1) | 1.1951 | 1.204 | 1 | 1 | −0.989 | 0.868 | 1.34 | 8×10⁻¹⁴ |
| 2 | (2,1) | 1.9637 | 1.967 | **1.643** | 1.634 | −1.989 | 0.922 | 1.84 | 8×10⁻¹² |
| 3 | (3,1) | 2.7475 | 2.754 | **2.299** | 2.287 | −2.985 | 0.913 | 2.25 | 5×10⁻⁶ |
| 4 | (2,2) | 3.4826 | 3.445 | **2.914** | 2.861 | −3.963 | 0.953 | 2.13 | 1×10⁻³ |

- The ratios agree to within 0.5–0.6% for Q = 2 and 3, and to 1.9% for Q = 4.
- The Q = 4 relaxation had not fully converged (max |grad| = 10⁻³). Q = 4 also has competing minima, so its energy is an upper bound.
- The spectrum follows the known sub-additive law $E_Q\approx E_1Q^{3/4}$. Two Q = 1 knots (2 × 1.195 = 2.39) have more energy than one Q = 2 knot (1.964), so **knots bind**, by about 18%.

**(b) Resolution (h → 0).** On the same 12.8 box, Q = 1 was relaxed at h = 0.2 and h = 0.1:

| Grid | E | Virial | Q measured | Core radius | max \|grad\| |
|---|---|---|---|---|---|
| h = 0.2 (N = 64) | 1.1977 | 0.854 | −0.99 | 1.34 | 10⁻¹³ |
| h = 0.1 (N = 128), started from the h = 0.2 knot | **1.2241** | **0.943** | **−0.9995** | 1.41 | 4×10⁻⁶ |
| Straight line in h², read at h = 0 | 1.233 | 0.973 | — | — | — |

- The Derrick balance moves toward 1 as the grid refines, so most of the imbalance on the coarse grid is discretisation. A few percent remain at h → 0, which fits the finite periodic box: Derrick's virial = 1 holds exactly only in infinite space.
- The absolute energy rises with resolution and lands within about 2% of the literature. Sutcliffe gives 1.204 and says it "appears to underestimate the energy by … about 1%"; earlier studies give about 1.21.
- **The ratios are the robust comparison.** Sutcliffe quotes his relative energies to about 0.1%, and ours agree with them to 0.5% (Q = 2, 3).

**(c) Control: Coh alone.** N = 64, h = 0.2, 8,000 steps of gradient flow from the same Q = 1 seed.

| Rule | Q | Core radius | E | Smallest link dot product |
|---|---|---|---|---|
| Cutting allowed | −0.992 → **0.000** by step 2,000 | 1.30 → 0 | 0.742 → 0.0008 | +1.000 (all aligned) |
| Uncuttable | −0.992 → −0.776 | 1.30 → **0.56** | 0.742 → 0.233 | **+0.493** (held at the rule's limit) |

- Without Str the knot unties if it can. If it cannot, it shrinks until links reach the 60° the rule allows, then stalls at about three grid spacings.
- In a scaleless substrate nothing would stop that shrinking. In a substrate whose hop is the Planck length, the knot ends one hop across: a Planck-mass object.

**(d) Quench.** "Knots, Not Crystals" left open whether a quench freezes a protected winding into the director field. Here a random field was relaxed for 20,000 steps of gradient flow (N = 64, h = 0.25).

| Rule set | Energy in box: start → 5,000 → 20,000 | Net Q in box | Lumps left |
|---|---|---|---|
| Coh + Str, cutting allowed | 14,962 → 13.5 → **2.65**, still falling | −0.05 | Two, carrying Q = −0.05 and 0.00: **no knots** |
| Coh + Str, uncuttable | 14,962 → 2,904 → **2,895**, flat | −0.27 | One tangle over **74%** of the box: **jammed** |
| Coh alone, uncuttable | 880 → 316 → **314**, flat | −0.63 | One tangle over 75% of the box: **jammed** |

A lump is a connected region where the director points more than 60° away from the box's average direction. Each lump's own Q was measured by blending the field to that direction outside the lump.

### Reading

- **Particles as knots pass.** Coh (alignment) plus Str (the squared winding density) holds stable knots of every charge tried, and their energies are the known continuum spectrum. Because this is the established Faddeev–Skyrme model, the agreement is **a pass, not a prediction.** CO's specific content is that Str must be the squared winding density: the cost of holding a topological commitment.
- **Coh alone fails, as Derrick's theorem says it must.** With cutting allowed the knot unties. With CO's uncuttable rule it collapses to the smallest scale the substrate has.
- **Scale.** The size and mass come from the two couplings:

  $$R\sim\sqrt{k_{\rm str}/k_{\rm coh}},\qquad M\sim\sqrt{k_{\rm coh}k_{\rm str}},\qquad MR\propto k_{\rm str}.$$

  If Str's coupling is set by the hop (as in CO's Bullet Cluster papers, $e\sim(\kappa\ell_P^2)^{-1/2}$), knots are Planck-sized. Ordinary particles need $k_{\rm coh}\ell_P^2/k_{\rm str}\sim(m/m_P)^2\sim10^{-45}$, which is the hierarchy problem stated in CO's terms.
- **Quench.** An instant quench gives no isolated particles: nothing survives if cutting is allowed, and a jammed glass forms if it is not. Whether a slow switch-on of the uncuttable rule leaves isolated knots is tested in Run 13.
- **Grid dependence.** These runs use a cubic grid only to discretise a continuum field. An earlier forward-difference version of Str was evaded by single-site flips that cut the knot (link dot product down to −0.98). The symmetric four-corner form above is not. Run 13 repeats the test on a relational graph with no grid.

![Run 12](figures/12_knots.png)

