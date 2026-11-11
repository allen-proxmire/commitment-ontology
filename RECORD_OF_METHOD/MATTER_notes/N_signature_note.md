# Does the breadth of an irreversible echo saturate? A one-page test

**The hypothesis.** In the Commitment Ontology (a proposed framework in which time is a count of irreversible events), a quantum handed on through resonant exchanges becomes an irreversible event once the chain has spread over a breadth of N distinct quanta (flipped spins, hopping excitations). Below N the spreading is unitary and reversible; at N it is not. Standard quantum mechanics has no such number. N is not derived; only experiment could set it.

**The rival account.** Many-body echoes already lose signal in a way that does not depend on the perturbation once interactions dominate (Sánchez et al., PRL 124, 030601 (2020); Pastawski's "central hypothesis of irreversibility"). Standard quantum mechanics explains this: in a closed system the perturbation below which decay depends on it again shrinks as the system grows (Zangara et al., arXiv:1412.4070), and by unitarity recovery is complete when nothing is left unreversed. So "the echo is lost" is not evidence for N.

**The test.** Let Σ be the whole unreversed part of the evolution (unreversed couplings, higher-order average-Hamiltonian and finite-pulse terms, field inhomogeneity, coupling to the environment, readout error) and J the coupling. Let K* be the breadth (spins or excitations reached, measured before reversal) at which recovery is lost.

| as Σ/J is made smaller | prediction |
|---|---|
| standard quantum mechanics | K* keeps growing once Σ/J is below the crossover where decay depends on Σ (Zangara et al.); above it, a ceiling set by each system's dynamics |
| CO | K* stops growing at N, the same in every system, in quanta |

**What qualifies.**
1. The spreading is carried by the system's own energy-conserving interactions (flip-flops, exchange, excitation hopping). A drive may reverse or scale the Hamiltonian but must not supply the quanta at each step. The double-quantum Hamiltonian of multiple-quantum NMR (pairs of like spins flipped, the Zeeman energy made up by the pulse train) does not qualify.
2. Breadth is measured before reversal, in quanta: for a high-temperature spin system, about half the correlated spins.
3. Every term in Σ is characterised. Some scale with J (higher-order terms grow as J²τ), so raising J can leave Σ/J unchanged and fake a ceiling.

**Present bound.** Sánchez et al. 2020 (secular dipolar Hamiltonian, adamantane) recover information spread over about 10² spins: N ≳ 50. Larger clusters, hundreds to thousands of spins, have been reported with the double-quantum Hamiltonian and do not qualify.

**The experiment to run.** The localization study of Álvarez, Suter and Kaiser (Science 349, 846 (2015)), repeated with the secular (flip-flop) Hamiltonian: cluster size at the moment of reversal, measured against Σ/J, out to hundreds of spins, in more than one crystal. A size that keeps growing as Σ/J falls raises the bound on N toward the largest cluster reached. A size that stops at the same breadth in different crystals, with Σ fully characterised, would be N.

**The cheapest version, in an existing setup.** Sánchez et al. (arXiv:2112.00607, adamantane) reverse the secular dipolar Hamiltonian scaled by a factor k, set by off-resonance irradiation, from k ≈ 0.05 to 0.9; they report the unreversed part (pulse errors, truncation, r.f. inhomogeneity) as roughly constant, so Σ/J is nominally ∝ 1/k (the true range is set by measuring Σ(k): higher-order average-Hamiltonian terms scale as k², and offset-dependent pulse errors change with k). They did not report the breadth at which the echo is lost against k. Spin counting can be added at the moment the echo falls to a fixed fraction, at each k, encoding about an axis perpendicular to the effective-field (quantisation) axis of the scaled Hamiltonian, from a transverse initial state (that Hamiltonian conserves the component along its own axis; counting as in Wei, Ramanathan and Cappellaro, PRL 120, 070501 (2018)).

**What a flat result would and would not mean.** In the regime the same group calls perturbation independent, the echo decays at a rate set by the coupling (T₃ ∝ T₂), so it reaches a fixed fraction at a time ∝ 1/(kJ) while clusters grow at a rate ∝ kJ: K* is flat in k under standard quantum mechanics too. So a flat K* separates nothing by itself. Two things can:

| check | standard quantum mechanics (emergent irreversibility) | CO |
|---|---|---|
| Σ/J pushed below the crossover where decay depends on Σ again (reachable in smaller or more isolated systems, Zangara et al., but only those with more than N spins can show N) | K* grows | K* stops at N |
| the ceiling compared across crystals, Hamiltonians and platforms, in quanta | set by the dynamics: shifts with geometry and coupling topology | the same N everywhere |

**A contrast in the literature, not evidence.** Under the secular Hamiltonian recovery is lost after about 10² correlated spins (Sánchez et al., arXiv:2112.00607); under the double-quantum Hamiltonian, which does not qualify, clusters of about 10⁴ have been reversed (the earlier works cited there). If N were near 10², that is the pattern CO would show; emergent irreversibility gives a dynamics-set ceiling instead, which should shift with crystal and Hamiltonian. The second row of the table separates them.

**Other platforms, for the universality check (literature read 2026-11-11).** No second platform yet reports a breadth in quanta at echo loss under a qualifying Hamiltonian.
- *Rydberg gases* (Geier et al., Phys. Rev. Research 6, 033197 (2024)): the dipolar exchange between S and P Rydberg states is a flip-flop (XX) Hamiltonian, which qualifies, and its sign is reversed by state transfer; the magnetization revives, with atomic motion identified as the main unreversed part. No cluster size is counted. The step needed: multiple-quantum or out-of-time-order spin counting at the moment of echo loss, which the authors name as an application.
- *Fluorapatite* (quasi-one-dimensional ¹⁹F chains; Cho, Cappellaro, Cory, Ramanathan 2006; Zhang et al. 2009): spin counting is done under the double-quantum Hamiltonian, which does not qualify.
- *Superconducting-qubit lattices* with natural photon hopping (Braumüller et al., Nature Phys. 18, 172 (2022)): qualifies; breadth a few quanta so far.
So the universality row of the test cannot yet be filled from the literature; adamantane under the secular Hamiltonian (about 10² spins) is the only qualifying number.

**Time is a weak signature.** Breadth grows by multiplication, so the time to reach N grows only as ln N: breadths of 50 and 10⁶ are reached within a factor of about 3.5 in time. Measure breadth, not time.

Record: [`MATTER_record.md`](../MATTER_record.md), entries on the stopping number.
