## 9zzs. Run 71: can a collapse get through the throat?

*21 October 2026. Step 3 followed from Run 68: a registered collapse model through the throat. Registered and hashed before any ED trajectory was integrated (`collapse71/PREREG_71.md`, 11:23 UTC).*
- *Disclosed: a development test of the pipeline on GR (R₀ = 7, not registered).*
- *`analyse71.py` was written after the run and is not in the hashed set. The scalings in the horn were fitted after the run (`posthoc71.py`, saved after the check began).*
- *An independent agent checked the run. It confirmed the model and every number. It then found that the main late-time results hold only for exactly pressureless dust: with any surface pressure the shell turns back and comes out again. Its findings, and a post hoc run with pressure (Run 71b, `bounce71b.py`, not registered), are included.*

**Question.** Run 67's static hole has a throat, a minimal areal radius at redshift about 74, just outside the cold zero-clock surface. Between the throat and that surface the areal radius grows without bound: the horn.
- Run 68 found the hole does not evaporate, assuming a collapse reaches the zero-clock surface with a smooth ray map.
- Its check found that GR dust cannot pass the throat: dust keeps Γ = ∂R/∂ℓ > 0, and Γ < 0 in the horn.

So: can collapsing matter get through, and what carries it? Does the radiation still switch off? Does the end state absorb or reflect?

**The model.**
- **Exterior:** Run 67's exact static solution, held fixed through the collapse, as Birkhoff's theorem would hold it in GR.
  - This is an assumption, not a consequence. Birkhoff needs vacuum, and here the exterior carries the medium's stress, with which the shell exchanges energy (the check).
- **The shell:** a thin shell, of dust (registered) or with surface pressure p = wσ (post hoc).
- **Interior:** flat (a regular centre).
- **Read with GR's equations**, the medium's stress included. The exterior's effective stress has ρ + p_r = −N²R_rr/(4πR).
- **Israel's two junction conditions:**
$$
\sqrt{1+\dot R^2}-R_r\sqrt{N^2+\dot r^2}=\frac{M_s}{R},\qquad
\frac{\ddot r+NN_r}{\sqrt{N^2+\dot r^2}}-\frac{\ddot R}{\sqrt{1+\dot R^2}}=(1+2w)\frac{M_s}{R^2}.
$$
- **Together they imply an energy exchange with the medium:**
$$
\dot M_s=-R\,R_{rr}\,\dot r\sqrt{N^2+\dot r^2}\;-\;2w\,M_s\frac{\dot R}{R},
$$
  - The first term is 4πR²T^out_{μν}u^μn^ν, the medium's stress acting on the shell.
  - The second is the ordinary work of the pressure.
  - In GR, dust's M_s is conserved.
- **The test field:** the 1+1 field at infinity, in-vacuum, with F(u) = −Sch[p](u)/24π. Rays reflect at the regular centre.
- **Runs (registered):** dust, ε = 10⁻², 10⁻³, 10⁻⁴ and 5×10⁻⁶, released from rest at R₀ = 10m and 4m, with GR controls.

**Results for dust (registered).**

| ε | γ at the throat | peak F/F_H | burst ends (N at the shell) | Δu_eff, shell | Δu_eff, Run 68 (same ends) | negative tail (share of the energy) |
|---|---|---|---|---|---|---|
| 10⁻² | 2.3 | 0.817 | 1.50ε | 16.1M | 25.5M | −4.8% |
| 10⁻³ | 4.6 | 0.963 | 1.49ε | 33.6M | 43.0M | −2.6% |
| 10⁻⁴ | 9.8 | 0.9936 | 1.53ε | 51.8M | 61.2M | −1.7% |
| 5×10⁻⁶ | 26.6 | 0.99938 | 1.55ε | 75.7M | 85.2M | −1.2% |

(R₀ = 10m; R₀ = 4m agrees within 1M in Δu_eff. γ is the Lorentz factor relative to static observers.)

1. **The medium's stress carries the shell through the throat.**
   - Read as GR's matter, ED's medium violates the null energy condition throughout the static exterior: ρ + p_r → −3ε/(4πr⁴) far out (the check), and about −0.03 at the throat.
   - A falling shell takes rest mass from that stress. At the throat its rest mass equals the throat's areal radius (M_s/R_t = 1 to 10⁻¹³). That is forced by the first condition for any finite crossing speed (the check), so the real result is that it crosses at finite speed.
   - With the exchange switched off, a shell released from rest has M_s ≈ 0.5–0.6R_t. It would meet the throat at light speed relative to static observers and could not continue.
2. **In the horn, dust never reaches the zero-clock surface in its own time.**
   - It approaches as τ − τ_t ≈ 4ε²/N. The check derived the coefficient, 4, analytically.
   - Its areal radius grows as 2ε/N. Its surface density tends to 1/(16πε): about 1/(2ε) times more rest mass per unit area than at the throat, drawn from the medium. So the dust's particle number is not conserved; the exchange is reversible (below).
   - It reaches the discrete regime (one unit per place, N = ε/p_s) after about 4εp_s of proper time, for any p_s. That is about 8M if p_s = 4×10⁵, a value no data fix.
3. **The radiation switches off: no evaporation, for dust.**
   - The flux reaches Hawking's while the shell is at N ≫ ε (0.9994 F_H at ε = 5×10⁻⁶). It switches off when the shell is at N ≈ 1.5ε, undershoots slightly, then decays as F → −1/(64πu²).
   - The emitted energy follows Run 68's slope, 8M per e-fold of P∞/p_s, but is 9.4M shorter than Run 68 counted between the same endpoints. The check splits this: about 8.4M because the burst ends earlier, and 1.0M of negative undershoot. In GR the same comparison differs by only 0.1–0.2M, so the offset is physical.
   - **Run 68's conclusion holds for dust, but not by Run 68's mechanism.** The ray map at the endpoint is not smooth; it is a power law, U ≈ 2√2 ε²√u. That is the case α = ½ which the check on Run 68 had flagged, and it gives the late tail −(1 − α²)/(48πu²) = −1/(64πu²) exactly. Run 68's smooth map gave a u⁻³ tail instead.
4. **Absorb or reflect, for dust: neither.**
   - Rays that enter the interior later come back out, delayed as u ≈ (ΔU/2√2ε²)² and redshifted by about ε⁴/ΔU.
   - At ε = 5×10⁻⁶, one M of interior time comes back after about 2×10²⁰ M: about 3×10⁸ years for a 10 M☉ hole.

**What the check added: the result depends on the matter's pressure.** The check used independent code and an analytic reduction of the horn equations (rescaled ν = N/ε). With a surface pressure p = wσ:

| matter | crosses the throat? | in the horn |
|---|---|---|
| dust (w = 0) | yes | creeps toward the zero-clock surface for ever (τ ≈ 4ε²/N); the borderline case |
| pressure (w > 0) | yes | **turns back where N ≈ wε** (N_turn/wε = 1.00–1.14 for w = 0.003 to ½) and **comes back out**. From rest the motion is periodic: w = 0.01 falls in, turns at R ≈ 200, returns to its start at R = 10m with its rest mass restored (1.0559), and repeats every 110M of its own time |
| tension (w < 0) | yes | absorbed: N falls exponentially, as e^(−|w|τ/4ε); U converges (U′ ∝ u^(−1.93)) |

- **Where it turns.** In the mean field, P/P∞ = (N + ε)/(1 + ε), so N = wε is where **the medium holds about (1 + w)·p_s per place**. Matter with pressure turns back just above where possibility runs out.
- **When it turns.** For a shell released from rest, u_turn ≈ [4.1 ln(P∞/p_s) − 5]M/w². At ε = 5×10⁻⁶ that is about 45M/w²:
  - about 400M for radiation-like pressure (w = ⅓), about 20 ms for a 10 M☉ collapse;
  - about 4.5×10⁵ M for w = 0.01.
- **Robustness.** Starting radius (R₀ = 50) and throwing the shell in (γ₀ = 10, 100) do not change these outcomes.
- **A null shell** crosses on kinematics alone and reaches N = 0 at finite affine parameter; its energy exchange was not computed.
- **Run 71b (post hoc, not registered):**
  - It reproduces the turn at N = 1.012wε for w = 0.01 at ε = 10⁻⁴.
  - It tests the flux pipeline through a turning point on a GR shell with pressure: Taylor-mode and finite-difference Schwarzians agree to 0.5%.
  - The flux when the matter comes back out has large positive and negative spikes (hundreds of F_H). These have not been separated from the thrown-in initial condition, so no bounce flux is reported.

![Run 71](figures/71_collapse.png)

**Verdicts, as registered.**
- **K71-GR PASSES:** the GR controls' late flux is Hawking's, F/F_H = 1.000000.
- **K71a PASSES:** the null energy condition fails at the throat for every ε. It also fails everywhere outside, at about −3ε/(4πr⁴).
- **K71b PASSES:** every dust shell crosses the throat at finite speed and enters the horn; the junction-exchange residual is about 10⁻¹².
- **K71c UNDECIDED, recorded on the stricter reading.**
  - There is no sustained flux, and neither failure condition is met.
  - The energy after switch-off is negative: −1.2% at ε = 5×10⁻⁶ and −1.7% at 10⁻⁴.
  - It passes the clause "less than 1% of the total" only as signed energy; read as a magnitude it does not. The clause was meant as a magnitude.
- **K71d UNDECIDED:** for dust, U′(u) ∝ u^(−1/2) is still falling, but slower than 1/u, so U grows without bound. The check: within the model the outcome is set by the equation of state. Pressure reflects (the matter itself returns), tension absorbs, and dust is the marginal case.

**Reading.**
1. **A collapse can pass the throat, carried by the medium's own stress.** The obstacle found in Run 68's check holds only if matter is sealed off from the medium. With both of Israel's conditions, the medium's stress (which violates the null energy condition) gives the shell exactly what it needs to cross.
2. **Beyond the throat this model does not give a stable hole for ordinary matter.**
   - Dust creeps toward the zero-clock surface for ever and emits no sustained flux: Run 68's "no evaporation" holds for it, by a power-law endpoint.
   - Any pressure turns the matter back where the medium holds about (1 + w)p_s per place, and it comes back out after about 45M/w² (at ε = 5×10⁻⁶). The exchange is reversible: the medium returns the rest mass it gave.
   - Collapsing stellar cores have pressure. A bounce within milliseconds to seconds of formation would be plainly visible, and black holes (X-ray binaries, gravitational-wave remnants, Sgr A*) are observed to stay. So this model, as it stands, conflicts with data.
3. **What would make ED's holes stable here: commitment before the bounce.**
   - The ruling of 19 October is that the core commits what reaches it. In this model the core is never reached. Matter with pressure turns back at P ≈ (1 + w)p_s, before the zero-clock surface (P = p_s), and before the discrete regime.
   - For the ruling that ED's holes are stable to hold for ordinary matter, the commitment has to act there: **where the medium's possibility per place falls to about p_s, within a factor of about 2 (w ≤ 1)**.
   - That needed a ruling. It places ED's core at the crossover scale p_s, where possibility runs out. An alternative was exterior dynamics that are not held fixed: the shell's draw grows about 10³-fold in the horn, so the exterior mass need not stay fixed (the check).
   - **Ruled 21 October: infalling matter commits where the medium's possibility per place falls to about 2p_s (§10).**
4. **Limits:**
   - the exterior is held fixed (no back-reaction);
   - a thin shell, not a star;
   - the 1+1 radial sector;
   - the mean-field medium;
   - no rotation;
   - the flux through a bounce is not computed reliably.
