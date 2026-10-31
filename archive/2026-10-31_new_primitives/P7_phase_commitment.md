## P7: phase-randomising commitment forces the Born exponent (draft, unchecked)

*31 October 2026. The idea, commitment as irreversible with environmental phase-randomisation over a U(1) phase, is taken from an earlier framework of Allen's, and it answers Allen's I16 question ("if CO's one-way commitment forced the counting step rather than just allowing it"). Reading I16 §1: "phase-free does not fix the power". That is true for phase-freedom alone. With phase randomisation and additivity together, the power is fixed.*

### 1. The statement
**Two inputs.**
- (C) A commitment randomises the relative phase of the contributions it merges: after commitment, θ is uniform and independent.
- (A) A merged record's weight, averaged over the randomised phase, equals the sum of its parts' weights. Once the phases are random the parts are alternatives, and probabilities of alternatives add.

**The weight** is a function of the modulus of the record's amplitude, F(|ψ|), with F(0) = 0 and F twice differentiable. Then (A) and (C) require
$$
\mathbb E_\theta\,F\big(|a+b\,e^{i\theta}|\big)=F(a)+F(b)\qquad\forall\,a,b\ge0 .
$$

**Claim (derived).** The only solution is F(x) = k x².

**Proof.**
- Write F(x) = G(x²). Then |a + b e^{iθ}|² = a² + b² + 2ab cos θ.
- Expand to order b², using E cos θ = 0 and E cos²θ = ½:
$$
G(a^2)+G'(a^2)\,b^2+G''(a^2)\,a^2b^2+O(b^3)=G(a^2)+G(b^2)=G(a^2)+G'(0)\,b^2+O(b^4).
$$
- So for every x = a²,
$$
G'(x)+x\,G''(x)=\frac{d}{dx}\big(x\,G'(x)\big)=G'(0).
$$
- Integrating gives x G′ = G′(0)x + C. Regularity at 0 gives C = 0, so G′ is constant: G(x) = kx, and F(x) = kx².
- **Sufficiency:** E|Σ c_k e^{iθ_k}|² = Σ|c_k|² for independent uniform phases.
- **Numerical check** (`p7_phase.py`): over four (a, b) pairs, the relative violation is 2×10⁻¹⁶ for p = 2, and 0.2–2.0 for p ∈ {0.5, 1, 1.5, 2.5, 3, 4}.

### 2. What it changes in CO
- **Q6 as an added principle is replaced** by two pieces:
  - (C), a physical property of commitment: the arrow destroys relative phase. This ties Born to the one-way primitive CO already has;
  - (A), the additivity of probabilities for alternatives, which is ordinary probability.
- **The power 2 is no longer A5's √P by fiat.** It is the unique weight consistent with one-way, phase-destroying commitment.
- **Still borrowed:** complex amplitudes (A5a), and the assumption that the weight depends only on the modulus.

### 3. Grade, honestly
- **The theorem is elementary.** It is close in spirit to known decoherence-based arguments for Born (for example Zurek's envariance) and almost certainly appears in some form in the literature. That needs checking before any claim of novelty.
- **For CO it is new:**
  - it is the first route by which a CO primitive, one-way commitment with phase loss, forces part of Born rather than allowing it;
  - it would turn Q6 from an added principle into a consequence.
- **Not an output beyond quantum mechanics:** it derives Born's form; it predicts no new number.

### 4. Kill test
Find a weight F ≠ x² that satisfies (A) and (C), for example a non-smooth or non-modulus weight. Or show that (A) secretly assumes Born. The first is closed for smooth modulus weights by §1. The second is a conceptual check for the reviewer.
