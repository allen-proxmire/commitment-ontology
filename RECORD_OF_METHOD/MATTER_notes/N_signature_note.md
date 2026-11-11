# A reversal ceiling at fixed breadth: a note for experimenters

**The hypothesis.** In the Commitment Ontology (a proposed framework in which time is a count of irreversible events), a quantum handed on through resonant exchanges becomes an irreversible event once the chain of exchanges has reached a breadth of N distinct quanta (excitations: flipped spins, hopping photons). Below N the spreading is unitary and can be reversed. At N it cannot: the echo does not return, however good the control. Standard quantum mechanics has no such number: it allows reversal at every breadth. N is not derived; if it exists, only experiment sets it.

**The signature.** Reversal recovers signal up to a breadth K ≈ N and then stops, at the same K whatever the coupling strength and whatever the perturbation. Ordinary mechanisms also limit reversal. Some move with the perturbation: localisation sizes shrink as the perturbation grows (Álvarez, Suter and Kaiser, Science 349, 846 (2015)). Others are perturbation-independent: a Loschmidt-echo decay rate set by the coupling itself (Sánchez et al. 2020), and since cluster growth also tracks the coupling, the breadth at which recovery is lost could stay put under both knobs without any new physics. The distinguishing mark is a ceiling fixed in breadth while the coupling-to-perturbation ratio, the system size and the control fidelity are all varied.

**The sharp test: does the breadth of loss saturate?** Many-body echoes already show a loss that does not depend on the perturbation once interactions dominate (Sánchez et al. 2020; the "central hypothesis of irreversibility" of Pastawski and co-workers). Standard quantum mechanics explains it: in a closed system there is a lower bound on the perturbation below which decay depends on it again, and that bound shrinks as the system grows (Zangara et al., arXiv:1412.4070); by unitarity, recovery is complete in the limit of no unreversed part. Here ε means the whole unreversed part of the evolution, Σ: residual couplings not inverted (heteronuclear, chemical-shift, non-secular dipolar), higher-order average-Hamiltonian and finite-pulse-width terms, field inhomogeneity, coupling to the environment (T₁, T₁ρ), and readout error. It cannot be dialled to zero; what can be varied is its ratio to the coupling, Σ/J, by maximising the coupling relative to the residual (Sánchez et al. scaled the interactions down to vary it).

So the test is stated as a scaling, not an extrapolation. Let K* be the breadth at which recovery is lost:

| as Σ/J is made smaller | prediction |
|---|---|
| standard quantum mechanics | K* keeps growing, without limit |
| CO | K* saturates at N |

A K* that keeps growing as Σ/J falls, past a few hundred quanta, raises the bound on N; a K* that stops at the same breadth in different systems and under different couplings would be N. Two cautions. Some unreversed terms scale with the coupling (the higher-order terms grow as J²τ), so raising J can leave Σ/J unchanged and produce a ceiling fixed in breadth with no new physics: a claimed N needs every term characterised and shown to scale away. And since N ≳ 50 already, the test needs breadths well above 50, so systems of hundreds to thousands of spins or atoms; small arrays cannot reach it.

**Measure size, not time.** Breadth in a real system grows by multiplication (gain g per step of time τ), so the time to reach N is t_N = τ ln N / ln g. A breadth of 50 and one of 10⁶ are reached within a factor of about 3.5 in time, so a delay or a timescale says little about N. The mark is the breadth at which reversal stops.

**What counts as a test.** Two conditions:
1. **The spreading is carried by the system's own interactions,** such as energy-conserving flip-flops, exchange or excitation hopping. A drive may flip the sign of the Hamiltonian or scale it, with no net energy exchanged per cycle, but it must not supply the quanta at each step. Double-quantum NMR sequences and laser- or gate-built interactions do not test it.
2. **Breadth is measured before the reversal,** in distinct quanta reached, not only in recovered signal. For a high-temperature spin system that means about half the correlated spins: the up spins inside the region the disturbance has reached.

**Current bound.** A scaled dipolar Loschmidt echo in adamantane partially recovers (the echo amplitude decaying) information spread over up to about 10² spins, with the secular dipolar Hamiltonian, whose flip-flops conserve energy, and sign-flipping pulse trains (Sánchez et al., PRL 124, 030601 (2020)). That gives N ≳ 50, conditional on the counting above (halving correlated spins to quanta is this note's convention, not a standard one). Larger clusters are reported, hundreds to thousands of correlated spins in adamantane and CaF₂, including the localization study whose cluster size shrinks as the perturbation grows (Álvarez, Suter and Kaiser 2015), but those use the double-quantum Hamiltonian, which flips pairs of like spins and takes its energy from the drive at each step; they do not meet condition 1, so they do not raise the bound. No ceiling at fixed breadth has been reported.

**The cheapest step up.** The localization study repeated with the secular (flip-flop) Hamiltonian: cluster size at the moment of reversal, measured against the perturbation, out to hundreds of spins. A saturating size would be the signature; a size that keeps growing as the perturbation falls would raise the bound on N toward the largest cluster reached.

**Suitable platforms.**
- **Rydberg gases with dipolar exchange,** reversed by transferring each spin to a pair of states where the coupling changes sign (Geier et al., Phys. Rev. Research (2024), with about 10³ atoms). The missing piece is a measurement of the correlation spread before reversal, at several densities.
- **Solid-state NMR polarization or Loschmidt echoes** with zero- and double-quantum-free flip-flop Hamiltonians, with the cluster size measured at the moment of reversal and the coupling scaled.
- **Superconducting-qubit lattices** with natural photon hopping, reversed by frame changes (Braumüller et al., Nature Phys. 18, 172 (2022)). Breadth there is only a few quanta so far.

**What would count against it.** Recovery continuing smoothly past a few hundred, then thousands, of quanta, with no fixed ceiling, raises the bound on N. A clean recovery at breadth K sets N > K. A ceiling that moves when the coupling or perturbation is varied is ordinary physics, not N.

Record: https://github.com/allen-proxmire/commitment-ontology/blob/main/RECORD_OF_METHOD/MATTER_record.md (entries on the stopping number).
