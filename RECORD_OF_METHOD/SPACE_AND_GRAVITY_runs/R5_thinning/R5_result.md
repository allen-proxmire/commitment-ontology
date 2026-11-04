# R5: thinning an all-to-all start, with and without pairing

Script: [`r5_thinning.py`](r5_thinning.py); numbers in `r5_result.json`, `r5_result_large.json`, `r5_scaling.json`.

**Registered before running.** Regime R4 missed: many places, few quanta each, every pair related at the start, relations that carry nothing die. Variant A: quanta pick a random surviving relation. Variant B: a quantum's first passage through a place pairs the relation it came by with the one it leaves by, and transit keeps to its pairs (inertia). Expectation: A is a random graph of degree about q + 1, expander-like; B is a union of lines, dimension unknown.

**Result.**

| run | places | component | mean degree | N within r = 1…5 | reading |
|---|---|---|---|---|---|
| A, q = 6 | 400 | 395 | 7.4 | 10, 71, 282, 391, 395 | random graph; whole graph within three hops; no dimension |
| B, q = 6 | 400 | 218 | 2.8 | 4, 12, 28, 61, 110 | lines; slow growth |
| B, q = 8 | 400 | 339 | 4.3 | 6, 30, 111, 250, 327 | |
| B, q = 8 | 800 | 600 | 3.6 | 5, 22, 76, 212, 418 | |
| B, q = 8 | 1600 | 1300 | 4.0 | 6, 28, 116, 390, 881 | |
| B, q = 12 | 800 | 706 | 4.7 | 7, 38, 167, 462, 672 | |

- **A:** as registered. Thinning alone leaves a random graph of degree ≈ q + 1 with no dimension.
- **B, small:** pairing turns the random start into lines; degree falls to 3–4 and neighbourhoods grow slowly. At one size this looks like a finite dimension between 2 and 3.
- **B, scaling:** at fixed q the ratio N(r+1)/N(r) at small r rises with system size (r = 2→3: 3.7, 3.4, 4.2; r = 3→4: 2.3, 2.8, 3.4 for 400, 800, 1600) and settles toward degree − 1 ≈ 3. That is the signature of an expander: exponential growth cut off by finite size, not a polynomial N(r) ∝ r^d. A three-dimensional lattice would hold the ratio near (1 + 1/r)³ and falling. **Pairing does not give a finite dimension in the large limit.**
- Degree does track quanta per place (q = 6, 8, 12 → 2.8, 4.0, 4.7 with pairing; ≈ q + 1 without), as the second finding of R4 said.

**Reading.** Thinning sets how many relations a place keeps; pairing by first passage (inertia) organises them into lines; neither says which places the lines connect, so the lines wander through the whole start at random and the result is an expander. Locality is still absent. The one thing left that can supply it is the mismatch cost: among the lines a place can feed, those that close loops consistently cost nothing and those that do not cost. On a bare graph with occupancies, "out of step" has to be given a meaning before that can be run; a proxy such as "prefer relations whose ends are already close by other paths" would be an added locality rule, and a run with it would return it. So the next step is not a run. It is to say what "a loop whose occupancies cannot be laid flat" means when there is no embedding to lay it in.

**Post-run check.** N(r) counts are averaged over 150 start places; the scaling runs share a seed. Fragmentation (component < places) is the thinning of places that lost every relation; it does not affect the growth reading within the component.
