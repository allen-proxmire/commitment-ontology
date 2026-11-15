# C2: nesting order chosen by sublattice (desk, 15 Nov 2026)

**Idea (from the I4/tuning-4 cold read).** Let the palindrome's nesting order depend on the place, cyclically by sublattice (s = (x + y + z) mod 3 carrying xyz, yzx, zxy). A cyclic permutation of the axes followed by a one-place translation would then map the walk to itself, so its point symmetry could be cubic without the time-folding that removed the gap when the order cycled by step.

**Check (c2_desk.py, c2_desk_out.txt; 6³ ring, w = 5π/16, θ = 0.3).** The step is a product of operators that each act on the whole lattice, so the order cannot be chosen place by place directly. The natural definition, W = Σ_s U_(order s) P_s (each place's state stepped with its own order), is not unitary: max |W†W − I| = 0.22, singular values from 0.057 to 1.71 (the single-order step is unitary to 10⁻¹⁵). A state leaving one sublattice is stepped by one order while another order acts on its arrival, and probability is not kept.

**Reading.** A sublattice-dependent order is not a rule on CO's current step; it would need a new, partitioned construction (local blocks that commute, as in a brickwork automaton), whose gap, species count and symmetry are unknown. Silence.
