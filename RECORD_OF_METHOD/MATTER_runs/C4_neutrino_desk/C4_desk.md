# C4: neutrinos on the flow step (desk, 16 Nov 2026)

**Question.** Does the flow step predict anything for high-energy neutrinos, as it does for photons?

**Standing of neutrinos in CO.** The weak interaction is absent, so how neutrinos are made, detected and mixed is a silence. What follows is kinematics only, conditional on neutrinos being patterns on the flow step with Dirac masses m₁, m₂, m₃ and the measured mixing.

**The step's dispersion for a light fermion.** In hop units (ħ = c = ℓ = 1),

E(k)² = Σ_j sin²k_j + (m + r Σ_j(1 − cos k_j))² = m² + k²(1 + rm) + O(k⁴),

so for E ≫ m

E ≈ k(1 + rm/2) + m²/(2k) + (c₂/3)k³,

with c₂(n̂) = 3(r²/8 − Σn⁴/6), the same for every species. The term k·rm/2 is the speed excess s = ½ r·mcℓ/ħ. It is the same in every direction (the cross term 2m·rΣ(1 − cos k_j) = m r k² + O(k⁴)), in the lattice's rest frame; the bound below takes Earth to move slowly in that frame.

**Two mass states.** Their energies differ by

ΔE = Δm²c⁴/(2E) + E · r(m₃ − m₂)c²/(2E_ℓ),   E_ℓ = ħc/ℓ.

The second term grows with energy, is the same in every direction, is CPT-even, and is diagonal in the mass basis, so it oscillates with the standard mixing angles. Checked on the step's exact dispersion along an axis, a face diagonal and a body diagonal to 5 × 10⁻⁵ (c4_check.py).

**In the language of the bounds.** With θ₂₃ near 45°, a term diagonal in the mass basis appears in the flavour basis as an off-diagonal μτ entry E·c, the isotropic dimension-four coefficient of the Standard-Model Extension:

|c_μτ| = r(m₃ − m₂) sin 2θ₂₃ / (4E_ℓ), real (with H ⊃ −E·c̊ its sign is negative; the bound does not depend on it).

The rotation also leaves a diagonal μμ − ττ part, cot 2θ₂₃ times the off-diagonal one (about 15% at θ₂₃ ≈ 49°), and the three-flavour μτ entry shifts c by about 2% (normal ordering) or 6% (inverted). Because the term lines up with the standard mixing, it acts as an energy-dependent addition to Δm²₃₂ with the same sign in both orderings, so IceCube's fit with diagonal entries set to zero carries over to about 15%. *(Corrected by C7: with three flavours the transfer holds to about 1% through the Earth's centre at 2–18 TeV, a few percent near the horizon; the three-flavour shifts of c are +3.3% (normal, lightest 0), −1.0% (lightest 0.03 eV), −2.6% (inverted).)*

**The bound.** IceCube's atmospheric ν_μ through the Earth (reconstructed muon energies 0.4–18 TeV, isotropic coefficients, two-flavour μτ, diagonal entries zero) give |Re c̊⁽⁴⁾_μτ| < 2.7 × 10⁻²⁸ at 90% (the step's term is real) (IceCube Collaboration, Nature Physics 14, 961 (2018)). With r = ½ and m₃ − m₂ = 0.041 eV (normal ordering, lightest mass near zero, as cosmology's bound on the sum favours):

E_ℓ ≳ 1.9 × 10²⁵ eV,   ℓ ≲ 1.0 × 10⁻³² m,   δ ≳ 3 × 10⁻⁵.

At ℓ = 2.4 × 10⁻³¹ m (the photon bound) c_μτ = 6.2 × 10⁻²⁷, 23 times the limit; at the Crab candidate 3.2 × 10⁻³² m, 8.3 × 10⁻²⁸, 3 times it. The bound scales with m₃ − m₂: ℓ ≲ 1.6 × 10⁻³² m at 0.027 eV (normal ordering, m₁ ≈ 0.03 eV), 8.8 × 10⁻³³ m (inverted ordering, lightest near zero; C7); if the masses were near KATRIN's limit (quasi-degenerate, m₃ − m₂ ≈ 0.0028 eV), 1.5 × 10⁻³¹ m.

**Which reading it applies to.** The same switch as the photon test. If the speed counter-terms absorb each species' mass-dependent excess (one per mass state), the term is cancelled and neutrinos say nothing. If the excess is kept, the bound holds, and at it the photon ceiling is E_th = C√(mₑc²·E_ℓ) ≳ 9–16 PeV (C = 2.9–5.1). Keeping the excess and passing the neutrino data needs the hop below about 10⁻³² m; absorbing it needs a counter-term per neutrino mass state, the gap between the two states' speeds cancelled to about 5 × 10⁻²⁸, far below the 10⁻²⁰ the charged species need.

**What the step adds beyond the bound.** If the excess is kept and ℓ is near the bound: an extra ν_μ disappearance through the Earth growing with energy, P(ν_μ → ν_τ) = sin²2θ₂₃ sin²(ΔE·L/(2ħc)), the lattice term equal to the standard one at about 1.5 TeV; the same for antineutrinos; no dependence on direction or time of day. Time of flight: every fermion lags straight light by |c₂|(E/E_ℓ)² at E ≫ m, varying by the cube pattern; at 220 PeV and ℓ = 2.4 × 10⁻³¹ m (the absorbed reading) up to 3 × 10⁻¹⁴ of the travel time along an axis, 5 × 10⁻¹⁵ along a body diagonal (an hour to ten minutes over a gigaparsec), and about 500 times less at ℓ = 10⁻³² m (the kept reading); too small to test without an identified source. Neutrinos are never faster than straight light (the excess is capped, as for the electron: m(r/2 − √(2|c₂|)) < 0 in every direction), so ν → νγ is forbidden; and they share c₂ with the electron, whose mass terms only raise its energy at a given momentum, so ν → νe⁺e⁻ is forbidden too. The bounds on superluminal neutrinos from those processes do not apply.

**Reading.** In the reading where the speed excess is kept, IceCube's atmospheric neutrinos bound the hop at ℓ ≲ 1.0 × 10⁻³² m, stronger than the photon bound and the Crab candidate; conditional on neutrinos as flow patterns with Dirac masses and on the lightest mass being small. In the absorbed reading, no neutrino effect. Grade: candidate.
