# A reversal ceiling at fixed breadth: a note for experimenters

**The hypothesis.** In the Commitment Ontology (a proposed framework in which time is a count of irreversible events), a quantum handed on through resonant exchanges becomes an irreversible event once the chain of exchanges has reached a breadth of N distinct quanta (excitations: flipped spins, hopping photons). Below N the spreading is unitary and can be reversed. At N it cannot: the echo does not return, however good the control. Standard quantum mechanics has no such number: it allows reversal at every breadth. N is not derived; if it exists, only experiment sets it.

**The signature.** Reversal recovers signal up to a breadth K ≈ N and then stops, at the same K whatever the coupling strength and whatever the perturbation. Ordinary mechanisms also limit reversal. Some move with the perturbation: localisation sizes shrink as the perturbation grows (Álvarez, Suter and Kaiser, Science 349, 846 (2015)). Others are perturbation-independent: a Loschmidt-echo decay rate set by the coupling itself (Sánchez et al. 2020), and since cluster growth also tracks the coupling, the breadth at which recovery is lost could stay put under both knobs without any new physics. The distinguishing mark is a ceiling fixed in breadth while the coupling-to-perturbation ratio, the system size and the control fidelity are all varied.

**What counts as a test.** Two conditions:
1. **The spreading is carried by the system's own interactions,** such as energy-conserving flip-flops, exchange or excitation hopping. A drive may flip the sign of the Hamiltonian or scale it, with no net energy exchanged per cycle, but it must not supply the quanta at each step. Double-quantum NMR sequences and laser- or gate-built interactions do not test it.
2. **Breadth is measured before the reversal,** in distinct quanta reached, not only in recovered signal. For a high-temperature spin system that means about half the correlated spins: the up spins inside the region the disturbance has reached.

**Current bound.** A scaled dipolar Loschmidt echo in adamantane partially recovers (the echo amplitude decaying) information spread over up to about 10² spins, with flip-flop dynamics and sign-flipping pulse trains (Sánchez et al., PRL 124, 030601 (2020)). That gives N ≳ 50, conditional on the counting above (halving correlated spins to quanta is this note's convention, not a standard one). No ceiling at fixed breadth has been reported.

**Suitable platforms.**
- **Rydberg gases with dipolar exchange,** reversed by transferring each spin to a pair of states where the coupling changes sign (Geier et al., Phys. Rev. Research (2024), with about 10³ atoms). The missing piece is a measurement of the correlation spread before reversal, at several densities.
- **Solid-state NMR polarization or Loschmidt echoes** with zero- and double-quantum-free flip-flop Hamiltonians, with the cluster size measured at the moment of reversal and the coupling scaled.
- **Superconducting-qubit lattices** with natural photon hopping, reversed by frame changes (Braumüller et al., Nature Phys. 18, 172 (2022)). Breadth there is only a few quanta so far.

**What would count against it.** Recovery continuing smoothly past a few hundred, then thousands, of quanta, with no fixed ceiling, raises the bound on N. A clean recovery at breadth K sets N > K. A ceiling that moves when the coupling or perturbation is varied is ordinary physics, not N.

Record: https://github.com/allen-proxmire/commitment-ontology/blob/main/RECORD_OF_METHOD/MATTER_record.md (entries on the stopping number).
