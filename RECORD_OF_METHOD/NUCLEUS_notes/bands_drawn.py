"""Two rings of four, drawn. A nucleon is a trapezoid of three unit triangles: single side
(length 1) on top, double side (length 2) underneath, a slanted flank each side. Stacked, each
single side sits on the middle of the next double side, so four make a column, and bent shut
the column is a band: the stacking direction s runs round it (period 4h), x runs along its
axis. Bending is flat on the surface, so the band is drawn unrolled. A second band is set
beside the first, either as it is or turned over (x -> -x, s -> -s), in each of four settings,
and every stretch of edge the two share is listed: which edges, how long, which nucleons.
Labels: a ring alternates n, p. Sort a: the joins where a neutron's single side is on a
proton's double side are the full ones (the two turn alike); sort b: the other joins are.
Sort a here reads p+ n- p- n+ from a proton, which is labelled_bands.py's second reading.
Not turned, no placement shares a stretch of edge: the facing flanks slant opposite ways, and
the bare halves both have their body on the same side. Turned, the full mesh (dx = 3.5) is the
placement of greatest contact; sliding along a flank gives part of a flank and no bare half.
shared() finds collinear overlap only; the placements used were checked free of overlap."""
import math, sys
h = math.sqrt(3)/2; P = 4*h; EPS = 1e-9
def trapezoid(slot, dx=0.0, turned=False):
    s0 = slot*h
    e = {"double-left-half": ((0, s0), (0.5, s0)), "double-middle": ((0.5, s0), (1.5, s0)),
         "double-right-half": ((1.5, s0), (2, s0)), "single": ((0.5, s0+h), (1.5, s0+h)),
         "flank-left": ((0, s0), (0.5, s0+h)), "flank-right": ((2, s0), (1.5, s0+h))}
    f = (lambda p: (dx - p[0], 2*s0 + h - p[1])) if turned else (lambda p: (dx + p[0], p[1]))
    return {k: (f(a), f(b)) for k, (a, b) in e.items()}
def shared(e1, e2):
    best = 0.0
    for off in (-P, 0, P):
        (a, b), (c, d) = e1, tuple((x, s+off) for x, s in e2)
        ux, us = b[0]-a[0], b[1]-a[1]; L = math.hypot(ux, us); ux, us = ux/L, us/L
        if any(abs((q[0]-a[0])*us - (q[1]-a[1])*ux) > EPS for q in (c, d)): continue
        t = sorted(((q[0]-a[0])*ux + (q[1]-a[1])*us) for q in (c, d))
        best = max(best, min(L, t[1]) - max(0, t[0]))
    return best if best > 1e-6 else 0.0
def ring(sort):   # slots 0..3 in stacking order: n p n p; turnings by the sort
    turn = [+1, +1, -1, -1] if sort == "a" else [+1, -1, -1, +1]
    return [("n" if i % 2 == 0 else "p", turn[i]) for i in range(4)]
def contacts(dx, turned, k):
    out = []
    for i in range(4):
        for j in range(4):
            A, B = trapezoid(i), trapezoid(((k - j) if turned else (j + k)) % 4, dx, turned)   # turned: stacking order runs the other way round
            for na, ea in A.items():
                for nb, eb in B.items():
                    L = shared(ea, eb)
                    if L: out.append((i, j, na, nb, round(L, 3)))
    return out
arrow = {1: "^", -1: "v"}
print("NOT TURNED, second band slid up to the first (dx = 2): shared edge in any setting: %s" % (any(contacts(2.0, False, k) for k in range(4)) or "none (corners only; the facing flanks slant opposite ways)"))
print("TURNED OVER, dx = 3.5 (the rims coincide):")
for sortB in ("a", "b"):
    A, B = ring("a"), ring(sortB)
    for k in range(4):
        cs = contacts(3.5, True, k)
        fl = [(A[i], B[j]) for i, j, na, nb, L in cs if na.startswith("flank") and nb.startswith("flank")]
        hf = [(A[i], B[j]) for i, j, na, nb, L in cs if "half" in na and "half" in nb]
        other = [c for c in cs if not ((c[2].startswith("flank") and c[3].startswith("flank")) or ("half" in c[2] and "half" in c[3]))]
        show = lambda prs: " ".join("%s%s-%s%s" % (x[0], arrow[x[1]], y[0], arrow[y[1]]) for x, y in prs)
        ok = all(x[1] != y[1] for x, y in fl)
        print("  first a, second %s, setting %d | flanks (%d, length 1 each): %s %s| bare halves (%d, length 0.5): %s%s" % (
            sortB, k, len(fl), show(fl), "ALL OPPOSITE " if ok else "", len(hf), show(hf), " | other: %s" % other if other else ""))
if "--draw" in sys.argv:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, axs = plt.subplots(1, 2, figsize=(9, 5.2))
    for ax, (title, turned, dx) in zip(axs, (("second band not turned: corners only", False, 2.0), ("second band turned over: rims mesh", True, 3.5))):
        for band, col, tr, d in (("A", "#c9d6ea", False, 0.0), ("B", "#ead6c9", turned, dx)):
            lab = ring("a")
            for i in range(4):
                T = trapezoid((3 - i) % 4 if tr else i, d, tr)   # turned: setting 3, the all-opposite one
                pts = [T["double-left-half"][0], T["double-right-half"][1], T["single"][1], T["single"][0]]
                ax.fill([p[0] for p in pts], [p[1] for p in pts], fc=col, ec="k", lw=1)
                cx, cy = sum(p[0] for p in pts)/4, sum(p[1] for p in pts)/4
                ax.text(cx, cy, "%s %s" % (lab[i][0], "↑" if lab[i][1] > 0 else "↓"), ha="center", va="center", fontsize=12)
        ax.set_title(title, fontsize=10); ax.set_aspect("equal"); ax.axis("off")
    fig.suptitle("Two rings of four, unrolled (top edge joins bottom edge). Each trapezoid: single side up, or down when turned.", fontsize=9)
    fig.savefig(sys.argv[sys.argv.index("--draw")+1], dpi=130, bbox_inches="tight")
