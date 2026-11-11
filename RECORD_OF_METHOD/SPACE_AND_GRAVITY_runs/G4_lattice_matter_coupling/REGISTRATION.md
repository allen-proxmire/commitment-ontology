# G4 — matter's coupling to the staggered carriers, exactly on the lattice

**Question.** The author's ruling (P7e) says no backdrop holds for the walk too. In the continuum, at linear order, that fixes matter's response to the carriers as −½ h_μν T^μν with T the symmetric stress tensor. On the lattice, the coupling Σ h·T is exactly unchanged by the staggered relabellings of run G3 (lapse and stretch at places; one-way part and place displacement on links; shear on faces) if and only if matter has local operators

- E at places (energy density), with Σ_x E_x = H,
- J_i on the links along i,
- P_ii at places, and one P_ij = P_ji on each face (i ≠ j),

satisfying exactly, as operator identities,

(I) ∂_t E_x + Σ_i [J_i(link out of x along i) − J_i(link into x along i)] = 0,
(II) ∂_t J_i(link) + [P_ii(upper end) − P_ii(lower end)] + Σ_{j≠i} [P_ij(face above the link along j) − P_ij(face below)] = 0.

The same J_i is the energy current in (I) and the momentum density in (II), and the face object P_ij serves both the i- and j-momentum flux: this is an exactly symmetric, exactly conserved stress tensor on the cubic lattice.

**Matter.** A stand-in for the walk: the Wilson–Dirac lattice Hamiltonian in continuous time (as run G3 kept time continuous), H(k) = Σ_i γ_i sin k_i + β[m + r Σ_i (1 − cos k_i)], m = 0.3, r = 1 in hop units; also m = 0. Primary: 2 + 1 dimensions (two components, Pauli matrices), where one face object P_xy carries the symmetric constraint. Secondary, if the size allows: 3 + 1 at the smallest range.

**Method.** Unknown operators are arbitrary matrices on a patch of sites within Chebyshev distance R of each object's sites (R = 1, 2). The identities and Σ E = H are linear in the unknowns; build them in real space by translation invariance and solve by sparse least squares. Existence: residual at rounding level. Non-existence: residual plateaus at order one while the controls reach rounding level.

**Controls.** (C1) 1 + 1 dimensions: no face terms; expected solvable. (C2) the same 2 + 1 problem with separate face objects for the i- and j-momentum fluxes (no symmetry demanded): expected solvable, which validates the method. (C3) for any solution, its long-wavelength limit is compared with the Dirac field's Belinfante tensor.

**Outcome unknown, and what would change.** (a) Solutions exist at some R: no backdrop for the walk holds exactly on the lattice, at linear order, for this matter; P7e's "lattice form owed" is discharged for the stand-in. (b) None up to R = 2 while C1 and C2 succeed: the walk's coupling is exactly invariant only at long wavelength; the lattice breaks it at order (kℓ)², and the obstruction is the symmetry of the stress (rotations), which ties it to the frame problem. Either way the grade of the walk's coupling in P7e is set by the result.

**Not covered.** The discrete-time walk itself (a Hamiltonian stand-in); nonlinear order; ranges beyond R = 2.

**Post-run check.** One: the sizes of the residuals against the controls, and for any solution, C3.
