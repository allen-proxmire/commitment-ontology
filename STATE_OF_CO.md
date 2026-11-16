# The Commitment Ontology, in plain language

## The idea

Time is a count of things that have happened. Not a river, not a dimension: a count. Something happens, and it cannot be undone. That is one tick. Matter is something that keeps happening. Where nothing happens, there is no time. Start from this and ask what physics has to look like.

CO starts from two things. Picture a network of places, like the points of a grid (the *lattice*). **Possibility** is what could happen: it sits at places and moves between places that are related. A **commitment** is something actually happening: an event that takes in some possibility and cannot be undone. Everything else is built from these two.

Relativity has no single "now" for the whole universe, and quantum mechanics has no event, only chances. CO takes events as basic and adds no universal now: an event's now is everything that could have reached it.

## The rules, in brief

Possibility (the P rules):
- It has no size scale of its own, so places compare their neighbours by ratio. Each hop carries one quantum, ħ (Planck's constant, the smallest unit of action).
- A place can hold only so much free possibility. Overfilled, it commits on its own.
- What an event takes in is given back when it finishes, except a small share kept as record.
- Possibility flows toward wherever more is being taken in.
- Possibility on the move keeps its direction until an event turns it.
- Possibility on the move is not free; what it uses becomes record.
- Space is just who passes possibility to whom. Sliding places around, relabelling them, or resetting a place's clock costs nothing: there is no backdrop.
- When two routes bring possibility to one place, they combine the way waves do.

Commitment (the C rules):
- Matter is an event that, on finishing, takes in the free possibility next to it for its next round. It stops when none is near.
- Each round takes in one quantum, ħ. How often the rounds come due is the mass.
- Each round keeps a small share of its quantum, δħ (δ is a small number of CO's own), as record. The record only grows: that is the arrow of time.
- At the beginning, every place was overfilled and everything committed at once.
- A measurement is an event taking in a passing quantum through a matching channel; once the chain of contacts reaches N quanta, it cannot be undone.

The full list, with equations and grades, is in [`TECHNICAL_APPENDIX.md`](TECHNICAL_APPENDIX.md).

## What follows

**Time** is matter's count. There is no clock of the world, only counts, compared:

$$\frac{\text{time at } A}{\text{time at } B}=\frac{N_A}{N_B}.$$

**Mass** is how often the rounds come due. Each round takes one quantum, so a thing of mass m ticks at

$$\omega=\frac{mc^2}{\hbar},$$

the frequency physics already gives every particle.

**The vacuum** is possibility with nothing happening: no count, so no time.

## Gravity

**Why clocks run slow near matter.** Near matter, more of the local possibility is already taken in (call the fraction h), so a clock has less to tick on:

$$\text{rate}=\frac{mc^2}{\hbar}\,(1-h).$$

Every kind of clock slows by the same factor. That is gravitational redshift.

**Why there is a pull.** Each tick keeps a crumb as record, so matter is a steady drain, and possibility flows in from around it. In the static case

$$\nabla^2\ln P_{\text{free}}=\sigma\,\delta(\mathbf r)\quad\Rightarrow\quad \frac{P_{\text{free}}}{P_\infty}=e^{-U},\qquad U=\frac{GM}{c^2r}.$$

The first part is Newton's 1/r. The next part bears on Mercury's orbit, and Mercury's measured orbit picks one of two ways to write the rule (a number fixed by data, β = 1). The inflow alone is far too slow to carry a changing pull; the network's places and links carry it.

**Why things fall.** Ticks are slower where h is higher, so a moving wave of matter turns toward matter, as light turns toward the thick side of a lens:

$$\mathbf g=c^2\nabla h,$$

the same for every mass. Falling is just moving straight in a medium that slows clocks.

**Light.** The same h lengthens routes, so light passing the Sun bends by

$$\delta\varphi=\frac{4GM}{c^2b},$$

Einstein's value, twice Newton's. This needs one number fixed by measurement: γ = 1, from the delay of radio signals from the Cassini spacecraft passing the Sun.

**Waves and the full theory.** Because moving places and resetting clocks cost nothing, the only allowed cost for the network being out of step is Einstein's, at least for small ripples. Assuming the same holds for large ones, plus a few standard assumptions (the cost is local, smooth, and treats all motions alike), Einstein's full equations are the only consistent choice (a known theorem does this step). So gravity has waves that stretch space in two ways (two polarizations), and black holes look as Einstein said from outside. This holds in the smooth, long-wavelength picture; on CO's own lattice, beyond small ripples, it is still open.

**On CO's own lattice.** How gravity enters matter's step is a choice (through the clock, the stretch of the hop, and a drift), still a candidate. With it, simulations in one and two dimensions show free fall at Einstein's rate, light bending twice the simple value, two bodies attracting only after each one's pull has crossed to the other, the sideways push of moving and rotating space, a fall through a black hole's edge along Einstein's path with light escaping from just outside it and swept in from inside, and a ball of matter collapsing into a black hole on time (in a simplified radial version). Three dimensions, a spinning body's field and stronger fields are still open.

**Where CO differs.** CO takes gravity's source to be what a body actually engages, not its undecided quantum state (a choice, still a candidate). So gravity cannot entangle two masses. If experiment shows that it can, CO's gravity is wrong.

**Three dimensions.** In one or two dimensions there are no gravity waves; in four or more there are no stable orbits; in even dimensions signals leave echoes forever. Three is the only dimension consistent with what is observed. That is a consistency check, not yet a reason.

## The universe

**The beginning.** All the first possibility in a few places: every place overfilled, so everything commits at once. Those events spread possibility into new places until every place is below the limit and the rush stops. That rapid making of places looks like inflation, with its own end. This is a shape only: no numbers yet for how long it lasted or the ripples it left.

**Expansion.** New places appear in empty regions at a steady chance per place. That steady chance is the cosmological constant, Λ, which drives the accelerating expansion. Its value comes from data. Newton's law on a growing shell gives the expansion rate H of the matter and radiation eras (Friedmann's equation):

$$H^2=\frac{8\pi G}{3}\rho-\frac{k}{a^2}+\frac{\Lambda c^2}{3}.$$

## Quantum mechanics

**Waves.** Matter ticks, so it has a phase: where it is in its cycle. When two routes meet, the only consistent way to combine them is quantum mechanics' rule:

$$p=\left|\sqrt{p_1}\,e^{i\theta_1}+\sqrt{p_2}\,e^{i\theta_2}\right|^2 .$$

**Chances.** The chance of an event somewhere is the possibility there. That is the Born rule, taken as a definition, not derived.

**The electron.** A moving pattern on a network with no backdrop needs four components, not one number per place. Matter steps on the lattice by a short flow that treats every direction of the cube alike (α and β are Dirac's matrices, k the wavenumber in each direction, τ_f the flow per tick, m the mass):

$$U=e^{-i\tau_f H},\quad H=\sum_j \alpha_j\sin k_j+\beta\Big(m+r\sum_j(1-\cos k_j)\Big),\quad r=\tfrac12 .$$

At long wavelengths this is Dirac's equation: the electron, with spin ½. A lattice also carries extra copies of each particle. The small extra term (the r term) makes them enormously heavy, at the hop scale. They must not be particles: as particles they would fall at about 0.6 of matter's rate. Treating their weight as not-matter is a choice.

**The moving clock.** A pattern's hops are shared between ticking and travelling, so a moving clock ticks slower: time dilation.

**Charge and light.** A relation also carries which way possibility passed. Its field equations are Maxwell's. Charge is a sign a pattern carries; the antiparticle is the same pattern with the sign reversed. The strength of the force, 1/137, comes from data.

**Atoms.** With two patterns, the standard two-body constructions give helium, positronium and hydrogen's 21 cm line.

**Why electrons don't share.** In three dimensions, swapping two identical patterns twice is a loop that shrinks to nothing, so one swap can only keep the sign (+1) or flip it (−1). Which: one swap can be turned into one pattern making a full turn around the other (an assumption, still a candidate). An electron's state flips sign under a full turn, so two electrons cancel and cannot share a state. Light doesn't flip, so photons pile in.

**No collapse.** A pattern left alone is never resolved, however big. Resolution needs an engagement: a contact whose chain reaches N quanta. N is a constant of CO's own, set only by experiment; present data say N is at least about 50.

**The nucleus.** "Colour" is the name physics gives the strong force's charge. In CO it is a split of a pattern into three parts alike (a choice: odd is forced, three is the least). With that, and the colour field's strength put in by hand as in standard physics, confinement and the proton's mass follow by matching to lattice QCD (the standard computer simulations of the strong force). The quark masses and charges are not supplied.

## Where it stands

**What it does.** From two starting things and a short list of rules, it reaches the classic tests of gravity (two numbers fixed by data), gravity waves, an inflation-like start, the expansion eras, three dimensions, the electron with its charge and spin, and, by matching to standard constructions, atoms and the nucleus. It has no tested prediction that differs from established physics, and no number matched where the standard theories are silent.

**What it borrows.** Many results come through known theorems and constructions; where a rule was a choice, the result is a reconstruction, not a derivation. The masses, 1/137 and the weak force are not explained.

**Its weakest point.** The lattice picks a rest frame. Once quantum corrections come in, different particles could get slightly different top speeds unless those speeds are set equal by hand. CO accepts that tuning for now, so it stands at tree level: the simplest level, before those quantum corrections.

**How it could be tested.** Three ways, each in [`ONE_PAGE.md`](ONE_PAGE.md) and [`TESTS_FOR_EXPERIMENTERS/`](TESTS_FOR_EXPERIMENTERS/):
- Very high-energy photons should split into electron pairs above a ceiling: roughly 5–9 PeV (peta-electronvolts) at the present bound, higher if the hop is smaller, and the same for every source in a given direction. The highest seen so far is 3.7 PeV.
- Gravity should never entangle two masses.
- The number N should be the same in every system.

**Relatives.** Causal sets; energetic causal sets (Cortês and Smolin); lattice fermions and quantum walks; event-based quantum theory (Haag, Blanchard–Jadczyk); quantum graphity; loop quantum gravity.

Independent, speculative, not peer-reviewed.
