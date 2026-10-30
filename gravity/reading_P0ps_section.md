## Note D: what fixes P₀/p_s? The earlier clock and medium papers (a reading)

*20 October 2026. The earlier project's papers, working notes and event-layer models were fetched, as current on 11 October. An agent surveyed the papers and notes for clock and medium papers, and the core ones and the event-layer models were read in full. Point 4 is an inference, not the corpus's. An independent agent checked the quotes against the papers and the inference against the engine's code; its corrections are included.*

**The question.** Run 55 left CO's strong-equivalence-principle prediction bounded but not sharp:
$$
\Delta\simeq C\,\frac{p_s}{P_0},\qquad \frac{P_0}{p_s}\gtrsim(1.7\text{–}2.1)\times10^5\ \ \text{(the pulsar triple, Run 57)} .
$$
- p_s is the medium's crossover: a place's outflow is linear below it and logarithmic above it, f(n) = c ln(1 + n/p_s).
- P₀ is the vacuum's possibility per place.
- Does anything in CO fix P₀/p_s, or either number?

**1. The clock papers fix the lapse's form, never an absolute level.**
- **GR-I** (`Paper_GR-I_WeakFieldEinsteinMetric.md` §4): from the null condition and a commitment rate linear in bandwidth (Γ ∝ b, P-Commitment-Linear),
$$
N^2\sim b,\qquad g_{ij}\sim b^{-1},
$$
  with "b enters as the dimensionless ratio to its asymptotic value". The 12 September outside review notes that with b harmonic this gives PPN β = 0.
- **GR-III** (`Paper_GR-III_DynamicalRule.md` §3–4): the medium is linear diffusion with a sink, ḃ = D∇²b − κρ, with b → 1 in the vacuum. α = 1 is argued from P11, and only κ/D is fixed.
- **The relational tick** (`Paper_RelationalTick_v1.md`): "the vacuum event-density magnitude is robust but unpinned" (§2, on α₁), and "an order-one commitment factor that the corpus inherits everywhere and derives nowhere" (§3, on mass as memory).
- **The commitment concept note:** Γ_commit ~ b_int/reserve, with "one unnamed rate constant".

**2. The medium papers give no per-place capacity and no crossover.**
- **P04** (the bandwidth primitive): bandwidth is a dimensionless, non-negative, additive scalar. "Canonical P04 gives non-negativity, not an upper bound." Arcs that need a bound must name one; the named bounds have no values:
  - P-Locus-Bandwidth-Bound (`Paper_UnifiedP04TransportBudget`);
  - P-V5-Budget (`Paper_065_Monogamy`).
- **The working note "N_bw needs a quantum" (7 September 2026), §5–6:** the ratio of a place's capacity to its smallest unit, N_bw = B_max/b_min, "needs a quantum", and "the bandwidth quantum is ABSENT and UNFORCED". That ratio is the nearest thing in the corpus to P₀/p_s.
- **"Where ED is silent"** (question 9) says the same. The state-of-the-ontology summary, an AI session's account, agrees: "the upper limit is not in any primitive".
- **The one per-cell number** (`Paper_112_hbar_Origin` §3.6, B_P04 ≈ 10⁹ W per cell) is a relabelling of ħ by its own disclaimer. It is also dimensionful, against P04's [b] = 1.
- **No logarithmic outflow anywhere.** CO's saturating laws (the PDE notes and `Arc_BH_3`) are jamming forms, with no values. GR-III's medium is linear. The engine's logarithm was brought in for β = 1 (Runs 21–25).
- **The event-layer models** (their results summary, result 23): possibility per place is a setting (1 to 8 units), and the one ceiling is CO's own, a place committing at most once per ħ.
  - Their trade-off between how far a shortage reaches and how strongly clocks feel it (`Gravity_As_Accounting.md` §4) comes from a vacuum that commits, which screens the shortage.
  - **The engine's vacuum never commits,** so its shortage is unscreened whatever P₀ or p_s. The clock's response per unit of draw is set by c ≈ p_s alone, and P₀/p_s controls only the departure from scale-free. The analogy holds for p_s and for strength only.

**3. Where CO does give numbers, they do not fit the engine's two scales.**
- **Capacity at saturation:** about one degree of freedom per Planck area (`Paper_025_HolographicBound.md`, N(R) ≤ 4πR²/ℓ_ED²; `Paper_HorizonTilingThreeCounts.md`). Read as p_s, that is p_s ~ 1, which clocks of different design exclude. Run 24 measured a 5.6% design gap directly at p_s = 1.
- **The vacuum's occupancy:**
  - `Phase3_GR_Alpha1_Magnitude.md` gives ρ_event/ρ_Planck ≲ 10⁻⁹³ (from the source) down to a floor of 10⁻¹²². The 12 September review withdrew the α₁ argument built on it as "a dimensional estimate". `Phase3_GR_LambdaOfRho_Derivation.md` leaves the magnitude unpinned ("10⁻⁵? 10⁻⁴⁷?").
  - These count *commitments*, which the engine puts only in matter. CO's possibility-like b is only ever normalized (b = 1), so the corpus has no per-place number for vacuum possibility.
- **The large numbers on offer are cosmological** (10⁶¹, 10¹²², Θ_ED; `Scoping_ThetaED_FirstPrinciples_2026-07-06.md`). The corpus warns against matching them: "it's easy to take a big number like 10¹²² and find matches", and "ED's 10¹²² is 1/Λ taken from observation" (ED_Attempt_03, `Specificity_Mechanisms.md`).

**4. One structural tie, in the engine (an inference, checked against the code).**
- **The field.** In a scale-free medium the engine's coupling per unit of draw is set by p_s:
$$
U=\frac{6}{c}\,G_{\rm lat}\!*s,\qquad c=\frac{0.99}{\ln(1+1/p_s)}\approx0.99\,p_s ,
$$
  so a body drawing S units per tick has U → 3S/(2πc r), with r counted in hops (`zrp35.py`: the traffic equation gives Δz = 6(s − s̄)).
- **The draw.** A reserved pair renews at rate (P_a + P_b)/H, each renewal takes one unit from each of its places, and H = 2ħ_t P₀. So a pair draws S = 2/ħ_t per tick.
- **Light speed.** Light crosses ħ_t hops per vacuum hold. That is a ratio of counts, so the ruling that the tick is not physical time does not enter.
- **The energy.** CO says mass is a rate of becoming, so the pair's rest energy is E = aħ/T_hold.
- **The result.** Equating U to GE/(c⁴r):
$$
\frac{G\hbar}{c^3\ell_{CO}^2}=\frac{3}{\pi a\,c}\approx\frac{\kappa}{p_s},\qquad \kappa=\frac{3}{0.99\,\pi a}=0.15\ (a=2\pi),\ \ 0.97\ (a=1).
$$
  CO fixes a nowhere. The event-layer harness's 0.1 rad per blink would give κ ≈ 9.6.
- **P₀ cancels,** through H ∝ P₀. So:
  - **CO's P-G-Closure** (`Paper_027_Newtons_G.md` §2: the coefficient in G = c³ℓ_ED²/ħ "is unity … labelled here rather than absorbed", together with ℓ_ED = ℓ_P) would need
$$
p_s=\big(e^{0.99\pi a/3}-1\big)^{-1}\approx0.0015\text{–}0.55 .
$$
    Run 24 excludes that directly (the 5.6% design gap at p_s = 1).
  - **Otherwise the hop is ℓ_ED ≈ √(p_s/κ) ℓ_P ~ 10^2.5–10^3.2 ℓ_P,** using the extrapolated p_s ≳ 4×10⁵. Or something else carries a factor of about p_s.
  - **The natural carrier would be the draw per renewal,** but a renewal that draws ~p_s units brings back the order-one self-dip that p_s was introduced to remove. So the tie is structural: a commitment that is light compared with the crossover means a weak G per pair.
  - **This bears on p_s only, not on P₀/p_s.** It is the kind of conflict Paper_027's revised falsifier F-P anticipates: a scale fixed independently of G that disagrees with √(ħG/c³).

**Reading.**
1. **Nothing in CO fixes P₀/p_s, or either number.** The corpus's own position is that per-place budget numbers are not in any primitive. P₀ and p_s stay tracked inputs, like Θ_ED in the corpus.
2. **So the strong-equivalence-principle prediction stays bounded, not sharp:** a sign (Δ > 0), a growth with compactness and a non-additivity, with its size limited by the pulsar triple.
3. **The engine and the corpus differ in three places:**
   - the lapse (the engine's N = P/P₀ against GR-I's N² ∼ b);
   - the medium (logarithmic outflow above p_s against GR-III's linear diffusion);
   - where the vacuum sits (far above its crossover in the engine; far below saturation in the corpus).

   These record where the engine departed from the corpus to pass β = 1 and clock universality.
4. **The engine's G ties p_s to the hop.** P-G-Closure with ℓ_ED = ℓ_P is incompatible with the engine's clocks. If the engine stands, CO's hop is about 10^2.5–10^3 Planck lengths, or the corpus is carrying two scales under one name (Paper_027's F-P).

*Note (30 October, Reading I18c):* R1 is amended beyond first order (a pure logarithm above p_c ≡ (1/p_s + 1/P∞)⁻¹, joined smoothly to f = 0.99P below). Results here that rest on g ≈ p_s/P, or on R1's curvature above the crossover, belong to the original R1; most had already lapsed as gravity results with ε = 0 in gravity. Where p_s sets a scale, read p_c.

*Note (30 October, Run 104):* the rerun under the amended outflow reads UNRESOLVED (the p_c = 1 gap lies between the through-p and through-B predictions); both carried-over clock bounds are kept, and the run's own fit reaches gap 10⁻⁶ at p_c ≈ 1.0×10⁶ (inference).
