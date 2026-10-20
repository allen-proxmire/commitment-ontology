# Knots, Not Crystals: The Order Event Density Does Not Have, and the Order That Matters

**Allen Proxmire**

**July 2026**

**Series:** Event Density (ED) Generative Papers — substrate-evaluation arc (structural invariants of the certified Σ-rule)
**Status:** Publication draft (short). A structural invariant of the certified substrate, measured across five arcs, with a sharp scope boundary: it governs correlation-based order and says nothing about topological defects. Companion to `Paper_CommonCauseNotChannel_A1` (the A1 common-cause result it generalizes) and the Bullet_Arc theory notes (whose correlation-negatives it explains and correctly bounds). Standalone; cold-reader accessible.
**Repository target:** `physics-papers/substrate-evaluation/` (ED-Generative)

---

## Preamble: What This Paper Does NOT Claim *(written first per QC discipline; abstract reconciled against this)*

1. **The 13 substrate primitives are not derived** (position paper, Paper_087).
2. **This is a structural reading confirmed by measurement, not a theorem.** The invariant is stated and shown to hold across five independent arcs on the certified substrate; it is not proved for all rules or all instantiations.
3. **The invariant governs correlation-based order only.** It is explicitly *not* a statement about topological defects (knots). §5 draws that boundary sharply: a topological defect is categorically different from correlation order, and this invariant neither predicts nor forbids one.
4. **It therefore does not condemn topological-defect mechanisms.** In particular, the Bullet_Arc's monopole account is *not* refuted by the correlation-negatives reported here; those negatives measure a different quantity (§5), and the knot question remains separately open.
5. **No new mechanism is added.** The paper re-describes what the certified rule's blindness structure permits and forbids, using only the certified Σ-rule and derived fields read off it.

---

## Abstract

Across five independent probes of the certified Event Density Σ-rule substrate, one structural pattern recurs, and it has a clean two-sided form. **(Negative side)** If the selection rule is *blind* to a quantity (its Σ never reads it), the only long-range correlation that quantity can carry is **common cause** (shared history), and sparse becoming erases almost all of it, leaving a faint residual. **(Positive side, refined)** A quantity the rule *reads* can carry genuine interaction correlation, but reading is *necessary, not sufficient*: correlation reaches only as far as the terms that read it, so a locally-read quantity (a target plus a nearest-neighbor penalty) acquires short-range structure and no long-range order. Long-range order additionally requires an *ordering* (propagating or aligning) coupling, and the certified Σ-rule has none in any sector. The consequence is exact: **the certified substrate has no spontaneous long-range correlation-order anywhere** — the blind sectors for lack of any interaction, the read sectors because their interactions are local-stabilizing. This paper states the invariant, gives the five-arc evidence, and then draws the boundary that matters most: **this is a statement about crystals, not knots.** A topological defect is not a correlation phenomenon; it is a protected winding on a target space with nontrivial homotopy ($\pi_2(S^2)=\mathbb{Z}$ for a monopole), and it can be created and protected independently of whether the field is long-range correlated. The invariant therefore governs correlation-based order and is silent on topological defects — a distinction that both bounds the invariant honestly and corrects any reading of the correlation-negatives as evidence against a knot mechanism.

---

## 1. The invariant

There are three kinds of correlated behavior a substrate field can show, and the certified rule Σ determines which of them a given quantity can have:

1. **Common-cause coherence** — weak, history-set, washed out by sparse becoming (a faint residual).
2. **Short-range stiffness** — strong nearest-neighbor structure, a fixed correlation length, no long-range order.
3. **Long-range order** — correlation that reaches across the system ($C(r)\to\text{const}$).

The invariant says which quantity gets which:

> **Blindness → common-cause only.** If the substrate rule is blind to a quantity, the only long-range correlation that quantity can carry is common cause (shared front or seed history), and sparse becoming erases almost all of it, leaving a faint residual thread. *(Kind 1.)*
>
> **Local read → short-range stiffness, not order.** If the rule reads a quantity but only through local terms (a target, a nearest-neighbor penalty), the field gains short-range structure and no long-range order. *(Kind 2.)*
>
> **Long-range order requires an ordering coupling** — a term that propagates or aligns across distance — which the certified Σ-rule has in **no** sector. *(Kind 3, and it is empty.)*

Stated once more, plainly, this is the recurring pattern probing surfaced in domain after domain:

> **Blindness → common-cause only.** If the substrate rule is blind to a quantity, the only long-range correlation that quantity can carry is common cause (shared front or seed history), and sparse becoming erases almost all of it, leaving a faint residual thread.
>
> **Non-blindness is necessary but not sufficient.** A quantity the rule reads can carry genuine interaction correlation, but only out to the range of the terms that read it. A locally-read quantity acquires short-range structure and no long-range order. Long-range order additionally requires an *ordering* coupling — a term that propagates or aligns across distance — which the certified Σ-rule has in no sector.

The two sides combine into one exact statement about the certified substrate: **there is no spontaneous long-range correlation-order in any sector.** The blind sectors (orientation, flow direction) carry only common-cause correlation, faint and history-set; the read sectors (commitment density) carry only short-range structure, because the rule reads them through local-stabilizing terms and never through an ordering coupling.

## 2. Why the sign structure is forced

> **Naming note, added 2026-09-05.** **The certified rule's `Coh`, `Str` and `Grad` are density-level stand-ins and are *not* the substrate functionals of the same name.** The corpus already half-records this — `../event-density/theory/P12_Coherence_PhaseAlignment_Scoping.md` Step 1 calls the certified `Coh = -(ρ-ρ_*)²` *“a density-target, not a coherence measure; **arguably mislabeled**”* — but nowhere a reader would meet it. The substrate `Coh` is the phase-interference content (`Paper_PhaseCoherence_P12Coh` §2); the substrate `Str` is per-channel `P-Quadratic-Strain`. **The shared names are a tractability artifact of a single-rule-type simulator with no explicit polarity, not a claim that these are the same functionals.** `foundations/Note_SigmaC_Defined_2026-09-05.md` §3.

The certified Σ functional is $\Sigma = k_c\,\mathrm{Coh} - k_s\,\mathrm{Str} - k_g\,\mathrm{Grad}$, with $\mathrm{Coh} = -(\rho_v - \rho_\star)^2$ (a local density target), $\mathrm{Str} = \rho_v$ (a local density penalty), and $\mathrm{Grad} = |\rho_v - \rho_u|$ (a nearest-neighbor gradient penalty). Every term is local, and every term reads the commitment density $\rho$ and graph-local structure only. Two facts follow directly:

- **Orientation and flow direction are never read** — the rule is blind to them. A blind quantity has no interaction term at all, so nothing couples distant values; the only way two distant directions can correlate is that a shared front imprinted both. That is common cause, and it is all there is.
- **The density is read, but only locally** — a target and a nearest-neighbor penalty. These build correlation across one edge and stop. No term compares or couples densities across distance, so no long-range order can grow. What emerges is a locally-smoothed field with a short correlation length.

There is no term of either kind — for any quantity — that propagates or aligns across distance. So no sector orders.

## 3. The five-arc evidence

The invariant is not read off one probe; it is the common structure of five:

1. **A1 / determinability boundary** (`Paper_CommonCauseNotChannel_A1`): the controlled channel capacity between regions is exactly zero; the boundary's correlation is shared-origin common cause, not a transmission channel. The original instance.
2. **Sparse becoming** (GR-IV arrow's-alibi): sparse commitment is what keeps the substrate coherent and suppresses preferred-frame effects — and it is also what erases the common-cause residual, leaving only a thread.
3. **Curvature emergence**: the deep open piece is whether an ordering or stiffness structure emerges from coarse-graining; the invariant frames why that is the crux.
4. **Bullet director field, 2D and 3D**: the commit-flow director is displaceable from the matter but only short-range coherent; long-range correlation is a faint common-cause residual in 2D and a seed-splay anti-correlation in 3D. Cause: the rule is orientation-blind. Measured with $O(3)$ genuinely reachable (certified rule on a 3D graph) and the topological-charge tool validated.
5. **Bandwidth/density sector**: the non-blind density $\rho$, tested directly, carries strong short-range correlation ($C(r{=}1)\approx +0.12$) but no long-range order ($\xi\approx 2$, long-range at the shuffle floor) — because the rule reads it only locally. The refinement (necessary-not-sufficient) comes from this arc.

Five arcs, one structure. That recurrence is the reason to treat it as a structural invariant of the substrate rather than a coincidence of one measurement.

## 4. Design consequence

The invariant is a tool for knowing where emergent correlation-order can and cannot live. To ground a claim of emergent long-range order, the order parameter must sit in a sector the rule *reads*, and the rule must contain an *ordering* coupling for it — not merely a local-stabilizing read, and never a blind sector. Inserting an ordering coupling by hand for a quantity the rule does not read is not grounding; it smuggles in exactly what the substrate lacks. On the certified rule as it stands, no sector meets the bar, so no correlation-order emerges anywhere.

## 5. The boundary that matters: crystals, not knots

Here is the scope line, and it is the most important sentence in the paper. **Everything above concerns correlation-based order — the crystal. It says nothing about topological defects — the knot. They are categorically different, and they live in different layers.**

A correlation-ordered field (a crystal, a ferromagnet) is characterized by its two-point function: order *is* long-range correlation, $C(r)\to\text{const}$. A **topological defect** (a knot, a monopole) is not that. It is a protected winding of a field whose target space has nontrivial homotopy — for a unit-vector field on $S^2$, $\pi_2(S^2)=\mathbb{Z}$, and a hedgehog carries an integer charge that no smooth deformation can remove. The two are independent in principle:

- A field can be **long-range correlated with no defects** (a clean crystal): high $C(r)$, zero winding.
- A field can **host a protected defect with no long-range correlation** (a knot in a disordered medium): short $C(r)$, nonzero winding. The winding is protected by the *topology of the target space and the boundary conditions*, not by the correlation length.

What a topological-defect mechanism actually requires is therefore **not** what this invariant measures. It requires (i) the field to take values on a manifold with the right homotopy (a genuine $S^2$-valued director), (ii) a process that *creates* a winding (a Kibble–Zurek quench through a rapid reconfiguration), and (iii) that the winding, once created, is *protected* (guaranteed by the homotopy). None of these three is a long-range correlation. A knot can be frozen into a field that is otherwise short-range and disordered, and it will persist, because its stability is topological, not statistical.

This has a direct and honest consequence for how the correlation-negatives of §3 (arc 4) should be read. Those probes measured the *relaxed* director field's *correlation* — its crystallinity. They correctly found none. But **correlation is the wrong observable for a knot.** The measurements do not test whether a quench can freeze a protected winding into the $S^2$-valued director, nor whether such a winding would persist; those are topological, dynamical questions in a different layer, and they remain open. So the correlation-negatives explain that the substrate is not a crystal; they are *not* evidence that it cannot hold a knot. Reading them as the latter — as this program briefly did — conflates the two layers.

The invariant, stated at its correct scope: **it governs whether correlation-based long-range order emerges, and the answer on the certified rule is no, in every sector. It is silent on whether topological defects can be created and protected, which is a categorically different question that its observable (the two-point function) cannot see.**

## 6. Falsification criteria

- **F1:** If a quantity the certified Σ-rule never reads were found to carry long-range correlation beyond the common-cause / shuffle floor (not attributable to shared history), the blindness → common-cause side would fail.
- **F2:** If a locally-read quantity were found to develop genuine long-range order without any ordering coupling being present, the necessary-not-sufficient side would fail.
- **F3 (the scope claim):** If a topological defect's stability or creation were shown to *require* long-range correlation order in this substrate, the crystal/knot separation of §5 would be wrong, and the invariant's silence on knots would be unjustified.

## 7. Position Statement

The certified Event Density substrate carries **no spontaneous long-range correlation-order in any sector**: blind quantities carry only common-cause correlation (faint, history-set, erased by sparse becoming), and read quantities carry only short-range structure, because the rule reads them through local-stabilizing terms and contains no ordering coupling anywhere. This is a structural invariant, confirmed across five arcs, and it is a statement about **crystals**. It is *not* a statement about **knots**: a topological defect is a protected winding on a target space with nontrivial homotopy, categorically different from correlation order, living in a different layer, and neither predicted nor forbidden by an invariant whose observable is the two-point function. The practical content is twofold: it tells you where emergent correlation-order can live (a read sector with an ordering coupling, of which the certified rule has none), and it warns, sharply, against reading correlation-negatives as evidence against a topological-defect mechanism — the crystal and the knot are different questions, and this invariant answers only the first.
