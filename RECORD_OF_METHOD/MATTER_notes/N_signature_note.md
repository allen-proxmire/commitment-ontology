# Does the breadth of an irreversible echo saturate? A one-page test

**The hypothesis.** In the Commitment Ontology (a proposed framework in which time is a count of irreversible events), a quantum handed on through resonant exchanges becomes an irreversible event once the chain has spread over a breadth of N distinct quanta (flipped spins, hopping excitations). Below N the spreading is unitary and reversible; at N it is not. Standard quantum mechanics has no such number. N is not derived; only experiment could set it.

**The rival account.** Many-body echoes already lose signal in a way that does not depend on the perturbation once interactions dominate (Sánchez et al., PRL 124, 030601 (2020); Pastawski's "central hypothesis of irreversibility"). Standard quantum mechanics explains this: in a closed system the perturbation below which decay depends on it again shrinks as the system grows (Zangara et al., arXiv:1412.4070), and by unitarity recovery is complete when nothing is left unreversed. So "the echo is lost" is not evidence for N.

**The test.** Let Σ be the whole unreversed part of the evolution (unreversed couplings, higher-order average-Hamiltonian and finite-pulse terms, field inhomogeneity, coupling to the environment, readout error) and J the coupling. Let K* be the breadth (spins or excitations reached, measured before reversal) at which recovery is lost.

| as Σ/J is made smaller | prediction |
|---|---|
| standard quantum mechanics | K* keeps growing, without limit |
| CO | K* stops growing at N, the same in every system |

**What qualifies.**
1. The spreading is carried by the system's own energy-conserving interactions (flip-flops, exchange, excitation hopping). A drive may reverse or scale the Hamiltonian but must not supply the quanta at each step. The double-quantum Hamiltonian of multiple-quantum NMR (pairs of like spins flipped, the Zeeman energy made up by the pulse train) does not qualify.
2. Breadth is measured before reversal, in quanta: for a high-temperature spin system, about half the correlated spins.
3. Every term in Σ is characterised. Some scale with J (higher-order terms grow as J²τ), so raising J can leave Σ/J unchanged and fake a ceiling.

**Present bound.** Sánchez et al. 2020 (secular dipolar Hamiltonian, adamantane) recover information spread over about 10² spins: N ≳ 50. Larger clusters, hundreds to thousands of spins, have been reported with the double-quantum Hamiltonian and do not qualify.

**The experiment to run.** The localization study of Álvarez, Suter and Kaiser (Science 349, 846 (2015)), repeated with the secular (flip-flop) Hamiltonian: cluster size at the moment of reversal, measured against Σ/J, out to hundreds of spins, in more than one crystal. A size that keeps growing as Σ/J falls raises the bound on N toward the largest cluster reached. A size that stops at the same breadth in different crystals, with Σ fully characterised, would be N.

**Other platforms.** Rydberg gases with dipolar exchange, reversed by state transfer (Geier et al., Phys. Rev. Research 2024, ~10³ atoms); superconducting-qubit lattices with natural photon hopping (Braumüller et al., Nature Phys. 18, 172 (2022); breadth a few quanta so far).

**Time is a weak signature.** Breadth grows by multiplication, so the time to reach N grows only as ln N: breadths of 50 and 10⁶ are reached within a factor of about 3.5 in time. Measure breadth, not time.

Record: [`MATTER_record.md`](../MATTER_record.md), entries on the stopping number.
