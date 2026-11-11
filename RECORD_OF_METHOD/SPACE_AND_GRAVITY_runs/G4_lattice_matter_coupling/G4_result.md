# G4 result (held for the author) — matter's coupling to the staggered carriers on the lattice

Registered first ([`REGISTRATION.md`](REGISTRATION.md)). Matter: the Wilson–Dirac lattice Hamiltonian, continuous time, r = 1.

| case | unknowns | relative residual | result |
|---|---|---|---|
| C1: 1 + 1, R = 1, 2 | 136; 344 | 1 × 10⁻¹⁴; 5 × 10⁻¹⁵ | solvable |
| C2: 2 + 1, no symmetry demanded, R = 1, 2 | 4 172; 25 068 | 1 × 10⁻¹³; 9 × 10⁻¹⁴ | solvable |
| 2 + 1, symmetric (one P_xy per face), m = 0.3, R = 1, 2 | 3 148; 19 884 | 1 × 10⁻¹³; 2 × 10⁻¹³ | **solvable** |
| 2 + 1, symmetric, m = 0, R = 1 | 3 148 | 2 × 10⁻¹³ | **solvable** |
| 3 + 1, symmetric, m = 0.3, R = 1 | 219 456 | 7 × 10⁻¹³ | **solvable** |

**Post-run check (C3).** In place of a term-by-term comparison with the Dirac field's Belinfante tensor, its one-particle values were checked. For each solution, the totals in band states at 20 random momenta: E equals the band energy (to 5 × 10⁻¹³), J_i equals E v_i (the energy current), and P_ij equals E v_i v_j (a symmetric momentum flux), to the finite-difference error of the velocities (≤ 2.5 × 10⁻⁸). The solutions are physical, not trivial.

**Reading.** At the smallest range (each object's operator reaching one site beyond it), the lattice matter field has an exactly conserved, exactly symmetric stress tensor placed as the staggered carriers need: energy at places, energy current = momentum density on links, diagonal flux at places, one shared off-diagonal flux per face. Given run G3's relabelling rules (the identities are their dual; the coupling itself was not relabelled in code), the coupling Σ h·T is then exactly unchanged by the lattice relabellings, at linear order: no backdrop for the walk holds exactly on the lattice for this stand-in, as run G3 found for the carriers' cost. The stand-in's low-energy speed is √(1 + mr) in hop units, so energy current = c_eff² × momentum per species (the frame problem's per-sector speed, of order mℓ, not a new effect).

**Not covered.** The discrete-time walk itself (a Hamiltonian stand-in); free matter only (no interactions), where every function of momentum is conserved, which makes the test less risky; nonlinear order; uniqueness (solutions are not unique: improvement terms remain free). The solved operators were not required to be Hermitian; the Hermitian part of a solution also solves.
