# C1: the body-centred-cubic Dirac automaton in CO's terms (desk study, 15 Nov 2026)

**Why.** CO's palindromic walk gives the vacuum direction-dependent finite parts (I4), and cycling the hop order destroys the gap. The remaining route to cubic symmetry is a single-step walk that is cubic by construction. The known candidate is the Weyl/Dirac quantum cellular automaton on the body-centred-cubic lattice (Bisio, D'Ariano, Perinotti; Found. Phys. 45, 1203 (2015); arXiv:1601.04832, Eq. 15 and Sec. VI).

**The automaton.** Each place has eight neighbours along the body diagonals. Weyl step A_k = u_k I − i ñ_k·σ, with c_i = cos(k_i/√3), s_i = sin(k_i/√3):
- u_k = c_x c_y c_z + s_x s_y s_z,
- ñ_k = (s_x c_y c_z − c_x s_y s_z, −c_x s_y c_z − s_x c_y s_z, c_x c_y s_z − s_x s_y c_z),
- ω_k = arccos u_k; light speed 1/√3 per step (in units of the neighbour distance).
Dirac step: two Weyl blocks coupled by the mass, D_k = n u_k I − i n γ⁰γ·ñ_k + i m γ⁰, n² + m² = 1, ω_k = arccos(n u_k).

**Checks (c1_desk.py, c1_desk_out.txt).**
1. *Unitary:* yes (10⁻¹⁶).
2. *Doubling: present.* u = +1 (a massless point at quasienergy 0) at k = 0 and at the three-fold vertices of the zone (±½, ±½, ±½)√3π, one class of four equivalent vertices: a second light Weyl species. u = −1 (massless points at quasienergy π) at the other class of three-fold vertices and at the four-fold vertices (±1, 0, 0)√3π: further species at π. The automaton would need a Wilson-type term, and none is known for it (new construction).
3. *Not cubic in its states.* The dispersion u_k is invariant under axis permutations, but the spin directions ñ are not related by any rotation (best-fit residual 1.6, against 10⁻¹⁶ for u). The automaton's covariance group is the binary rotations about the axes only (order 4), as the paper states. Response tensors of its vacuum need not be isotropic.
4. *A first-order, direction-dependent term in the dispersion.* The s_x s_y s_z term makes ω odd in k along body diagonals: ω(k) − ω(−k) = −0.128 k² along (1,1,1), and the quadratic coefficient of ω/k is −1.18 along (1,1,1) and +1.13 along (1,−1,1), against 0 along an axis. That is Lorentz violation at first order in kℓ (dimension five), helicity-dependent in the Dirac automaton. Such terms for electrons are bounded far below order one in Planck units (Crab synchrotron; Jacobson, Liberati and Mattingly 2003), so at any grain near or above the Planck length this automaton is excluded for matter. CO's palindromic walk has no first-order term (its dispersion is even and cubic at low energy).

**Reading.** The body-centred-cubic automaton does not restore cubic symmetry where CO needs it, has extra species, and adds a first-order Lorentz violation that CO's walk does not have. Not a route. What remains for the direction dependence: direction-dependent counter-terms on CO's walk (a tensor of tunings), or a cubic single-step construction not yet known. Silence on the second.
