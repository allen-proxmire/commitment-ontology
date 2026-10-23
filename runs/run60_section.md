## Run 60: can ED hold 2 M☉ with matter that nuclear theory and QCD allow?

*20 October 2026. (ED's interior equations bind for neutron stars; step 2 is the gravity-independent test). Registered and hashed before the run (`nuc60/PREREG_60.md`, 17:09 UTC). An independent agent reproduced it with its own code; its corrections are included.*

**Question.** Run 59 limited dense matter only by causality. Nuclear theory and QCD limit it further without assuming any theory of gravity. Can ED hold PSR J0740+6620 (2.08 ± 0.07 M☉) with matter they allow?

**The gravity-independent limits.**
- **Chiral effective field theory** at 1.1 n_s (Hebeler et al. 2013, as tabulated by Komoltsev & Kurkela 2022): n_L = 0.176 fm⁻³, p_L ∈ [2.163, 3.542] MeV/fm³. At 2 n_s the N3LO neutron-matter sound speed is c_s² = 0.10 ± 0.07 (Drischler et al. 2020).
- **Causality:** c_s² ≤ 1.
- **Perturbative QCD** at μ_H = 2.6 GeV (Komoltsev & Kurkela 2022, X = 1, 2, 4). A point (μ, n, p) can be joined to QCD by a causal, stable, consistent equation of state if and only if
$$
\frac{n}{\mu}\le\frac{n_H}{\mu_H},\qquad \frac{n(\mu_H^2-\mu^2)}{2\mu}\;\le\;p_H-p\;\le\;\frac{n_H(\mu_H^2-\mu^2)}{2\mu_H},
$$
  with μ = h m_N and n_B = ρ/m_N (so μ n_B = e + p exactly). The check confirms these are the complete conditions from the high-density side.

**Method.** A realistic equation of state up to n_χ, then a constant sound speed c_s² = s:
$$
h=h_m\Big(\frac{n}{n_m}\Big)^{s},\qquad e=e_m+\frac{h_m n_m}{1+s}\Big[\Big(\frac{n}{n_m}\Big)^{1+s}-1\Big],\qquad p=p_m+s\,(e-e_m).
$$
ED's stars of 2.08 and 1.94 M☉ are found with Run 57's solver, and the QCD test is applied at every point from n_χ to each star's centre.

**Verdicts, as registered** (X = 2; X = 1 and 4 agree).
- **K60a PASSES** (chiral EFT to 1.1 n_s, then any c_s² ≤ 1, QCD). With MPA1 or SLy below, ED reaches 2.08 M☉ for s ≥ 0.35 (0.327 on a continuous scale). Every such star passes QCD.
- **K60b PASSES** (SLy or APR4 to 2 n_s, then QCD). ED reaches 2.08 M☉ for s ≥ 0.80. The stars' centres are at 3.1–3.2 n_s and pass QCD. With MPA1 to 2 n_s (reported) s ≥ 0.70 suffices.

| case | smallest s for 2.08 M☉ | ED M_max at s = 1 | GR M_max at that s | centre of the 2.08 M☉ star | ED radius at 2.08 / 1.4 M☉ |
|---|---|---|---|---|---|
| MPA1 or SLy to 1.1 n_s | 0.35 | 2.91 | 2.47 (s = 0.35) | 2.4 n_s (s = 0.35) | 13.8 / 13.9–14.4 km |
| SLy to 2 n_s | 0.80 | 2.19 | 2.72 (s = 0.8) | 3.1 n_s | 11.6 / 12.1 km |
| APR4 to 2 n_s | 0.80 | 2.18 | 2.70 (s = 0.8) | 3.2 n_s | 11.3 km / — |

**What the check added.**
1. **QCD never binds inside these stars.** Continuing each equation of state past the centre, the QCD test first fails at 2.2–2.5 n_s for s = 1 from 1.1 n_s, at 8–15 n_s for s = 0.35, and at 4.4–5.6 n_s for s = 0.8 from 2 n_s. Each is above the centre of the 2.08 M☉ star (1.3, 2.4 and 3.1–3.2 n_s). So both verdicts are set by causality and by where chiral EFT is trusted. That matches Komoltsev & Kurkela's own statement that QCD first limits the equation of state at about 2.2–2.5 n_s.
2. **A jump in c_s² at 2 n_s is not excluded by anything gravity-independent.** p, e and n stay continuous, and the paper allows even first-order transitions.
3. **The reproduction matches.** Centre densities and radii agree with Run 60's own numbers; s = 1 from 1.1 n_s puts the 2.08 M☉ star far down a branch that tops out at 2.91 M☉, so it is large and dilute (centre 1.3 n_s, radius 15.3 km).

![Run 60](figures/60_nuclear.png)

**Reading.**
1. **ED's interior equations survive the gravity-independent test only if dense matter is at or near the causal limit just above where nuclear theory is trusted.** That is a definite, falsifiable requirement on the equation of state, not support for ED. ED needs one of two things:
   - **(a) c_s² ≥ 0.33 from 1.1 n_s.** This sets chiral EFT aside above 1.1 n_s: at 2 n_s it is about 3σ above the N3LO neutron-matter band, and β-equilibrium matter is softer still. It gives large radii, 13.8–15.3 km at 2.08 M☉.
   - **(b) Chiral-EFT-like matter to 2 n_s, then c_s² ≥ 0.8 up to the centre (3.1–3.2 n_s).** SLy and APR4 sit at the stiff 1σ edge at 2 n_s, so a softer base would need s closer to 1. Its radii are about 11.6 km at 2.08 M☉ and 12.1 km at 1.4 M☉.
2. **GR needs neither.** It holds J0740 with APR4 and MPA1 as they are, and with SLy within 1σ. With K60b's s = 0.8 matter it would give 2.7 M☉.
3. **The next tests are radii and tidal deformability.**
   - NICER and GW170817 suggest radii of roughly 12–13 km (to be checked against the papers). That would disfavour route (a) and leave route (b).
   - Those inferences use GR's exterior. ED's exterior agrees with it at first post-Newtonian order but differs at O(U²) in the spatial metric, and ED's tidal Love numbers have not been derived.
   - So the comparison needs ED's own light bending to O(U²) and Love numbers first.
