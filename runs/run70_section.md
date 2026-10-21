## 9zzr. Run 70: clocks on a lattice with curved-space conductances

*21 October 2026. Allen: "im good with your recommendations… please proceed" (09:04), step 4: build the stress-curved lattice and re-check clock universality. Registered and hashed before any engine run (`curve70/PREREG_70.md`, 07:20 UTC), with the zero-range theory's predictions computed and hashed beforehand (`theory70.json`).*
- *Disclosed: the theory was first run at λ = 0, 0.03 and 0.06. I moved to 0.06 and 0.12 before any engine run, after seeing that the predicted changes are linear in λ, so 0.03 would sit inside the noise.*
- *A 300-tick smoke test is disclosed in the registration.*
- *An independent agent checked the run. Its corrections narrow what the run shows, and they are included: the curvature here is imposed rather than produced by stress, the measured size depends on how places are represented, and the effect is not local.*

**Question.** Under option 3 the medium hops on the medium's space γ̃, which stress curves (§9zzm, §9zzo). Clock universality was shown on a flat lattice (Runs 23–24): clocks of different design agree, with a design gap falling as p_s^{−0.85}. Do the engine's clocks still follow the zero-range theory when the lattice's links carry curved-space conductances?

**The engine.** Run 24's engine and protocol are unchanged except for the hop rule:
- 36³ periodic lattice;
- 216 probe clocks, of designs H and 2H;
- p_s = 4;
- ambient P₀ = 256 or 154;
- 20,000 ticks, read over the last 15,000.

**The curved conductances.** They are imposed as a conformal factor, γ̃ = Ω²δ with Ω = e^σ.
- In 3D the Laplace–Beltrami conductance of a link is √γ̃γ̃^{ij}h = Ω at its midpoint.
- A unit that tries to hop (engine21's chance p(P)) goes along link k with probability W_k/6, or stays with probability 1 − ΣW_k/6. The mean link current is W(z_x − z_y)/6.
- With no clocks the medium stays uniform per place: the zero-range process's fugacity cancels site by site (the check).
- The conformal factor is
$$
\sigma(\mathbf x)=-\lambda\Big(\frac{6}{2\pi}\Big)^2\sum_{d=1}^{3}\Big[1-\cos\frac{2\pi(x_d-c_d)}{6}\Big],
$$
  with σ = 0 at every clock's midpoint. The scalar curvature there is R̃ = +12λ per spacing²: 0.72 at λ = 0.06 and 1.44 at λ = 0.12, a curvature radius of about one spacing.
- **Places are unequal.** Each site carries γ̃-volume Ω³: 1 at the clocks, falling to 0.37 (λ = 0.06) and 0.14 (λ = 0.12) at the cell corners. An equal-place discretisation needs an irregular graph, which is not built.

**The theory, fixed beforehand.** Run 24's zero-range theory, extended to every probe's draw and to the weighted lattice:
$$
\tfrac16\sum_yW_{xy}(z_y-z_x)=s_x-\bar s ,\qquad P_{\rm own}=R\big(z_{\rm amb}+\Delta z\big),\qquad r_j=\frac{2P_{\rm own,j}}{jH}.
$$
On the flat lattice it gives own-dips of 0.0672/0.0332 (high) and 0.0424/0.0205 (low), against Run 24's measured 0.0667/0.0338 and 0.0420/0.0197.

**Results** (own-dip 1 − P_own/P_amb, curved over flat; flat pools Run 24's two seeds with this run's λ = 0).

| | λ = 0.06: measured (theory) | λ = 0.12: measured (theory) |
|---|---|---|
| high medium, design 1 | 1.045 ± 0.012 (1.032) | 1.067 ± 0.013 (1.067) |
| high medium, design 2 | 1.021 ± 0.025 (1.030) | 1.037 ± 0.026 (1.061) |
| low medium, design 1 | 1.053 ± 0.020 (1.034) | 1.063 ± 0.021 (1.070) |
| low medium, design 2 | 1.036 ± 0.046 (1.030) | 1.052 ± 0.046 (1.062) |
| weighted mean excess | 4.3 ± 0.9% (theory ≈ 3.2%) | 6.1 ± 1.0% (theory ≈ 6.7%) |
| design gap (theory) | 0.0208 (0.0215) | 0.0223 (0.0223) |

- With λ = 0 the gap is 0.0193 (theory 0.0207; Run 24: 0.018 ± 0.002).
- Charge is conserved exactly in every run.
- A single amplitude fitted to all eight rows, scaling theory's predicted excesses, is A = 0.94 ± 0.15. That is 6.3σ from zero, with χ² = 3.9 for the theory against 43.3 for no effect, over 8 degrees of freedom (the check, with the shared flat pool's covariance included).

![Run 70](figures/70_curved.png)

**Verdicts, as registered.**
- **K70a PASSES:** with λ = 0 the new hop rule reproduces Run 24's own-dips within 1σ (0.0671/0.0340 high, 0.0412/0.0208 low).
- **K70b PASSES:** with no clocks, on the λ = 0.12 lattice, the mean P on the weakest-linked places equals that on the strongest-linked within the 2×10⁻³ threshold: 3×10⁻⁴ ± 2.7×10⁻⁴. The check finds that error too small, because density modes on the cell scale relax in about 350 ticks; its own simulation gives (0.8 ± 1.3)×10⁻³.
- **K70c PASSES:** all eight curved/flat ratios agree with the theory within 1σ. The test alone barely discriminates: an engine with no effect would also have passed six of the eight rows. The combined amplitude above is the real evidence.

**What the check added.**
1. **Confirmed with independent code:** the hop rule (the sequential binomials give W_k/6 exactly; the uniform state is stationary); the theory (its own preconditioned solver reproduces the response matrix to 10⁻¹² and the predicted ratios to 10⁻⁴); and the statistics. The probe-scatter errors are conservative: the seed-to-seed z-scores have an rms of 0.56.
2. **The size of the own-dip effect depends on how places are represented.** The run's places are unequal in γ̃-volume, and "uniform per place" means a density ∝ Ω⁻³. Rerunning the theory with release and ambient per γ̃-volume, as equal places would imply, changes the predicted own-dip ratios at λ = 0.12 from 1.067/1.061 to 1.018/0.955, so design 2's even changes sign. Only the change in the design gap is robust to the representation (1.074 against 1.076), and the data do not resolve it.
3. **The effect is not local.** With the curvature at the clock held fixed and the period of σ varied, the response per unit λ grows roughly in proportion to the period: 0.93, 1.86, 3.4 and 4.6 for 6, 12, 24 and 36 spacings. It comes from the Green's function's regular part:
$$
\frac{\delta G(0)}{G(0)}\sim C\,\tilde R\,h\,\ell_c ,\qquad C\approx0.008\text{–}0.013 ,
$$
   not from R̃h². My planned figure of 10⁻⁷² used the wrong scaling.
4. **At physical curvature it is still negligible.** For a neutron star (R̃ ≈ 0.2/(10 km)², ℓ_c ≈ 10 km) and ED's hop (10^2.5–10^3 Planck lengths), R̃hℓ_c ≈ (1–3)×10⁻³⁷, so the self-dip changes by about 10⁻³⁹ of itself. The design-dependent part is smaller still.
5. **Other limits.**
   - The curvature is imposed, not produced by the medium's stress.
   - Clocks sit at maxima of Ω, so only one sign of contrast was tested.
   - Only p_s = 4 and one geometry were run.
   - The curvature radius, about one spacing, makes a continuum reading weak.

**Reading.**
1. **Clocks read the medium only through its local fugacity, and that holds on an inhomogeneous lattice too.** On a lattice whose link conductances follow a conformal factor, with places unit at the clocks, the engine's clocks follow the zero-range theory with the weighted Green's function. The predicted 3–7% own-dip change is detected at about 6σ, at 0.94 ± 0.15 of the predicted size.
2. **Clock universality on option 3's medium space is not yet tested.**
   - The measured excess depends on the representation of places.
   - The robust quantity, the design gap, is not resolved.
   - The curvature was imposed rather than produced by stress.
   - The effect is non-local, about 0.01·R̃·h·ℓ_c. That is about 10⁻³⁹ for a neutron star, so universality is not threatened at physical scales, but the run does not show it on an equal-place, stress-curved lattice.
3. **What would test it:** the design gap with about ten times the statistics; an equal-volume discretisation (an irregular graph, or a one-dimensional conformal factor with volume-preserving coordinates); clocks at minima of Ω as well as maxima; and, eventually, a lattice whose geometry is solved from the medium's own stress.
