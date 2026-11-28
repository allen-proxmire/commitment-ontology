"""Two rings of four, rim to rim, with the nucleons labelled by kind and turning.
A ring in stacking order alternates proton, neutron; its joins are full (the two turn alike)
and weak (opposed) by turns, and alike nucleons are opposite (rule 3). Round the rim that is
p+ n+ p- n-, or p+ n- p- n+ (the full joins the proton-on-neutron ones or the
neutron-on-proton ones): one ring with the kinds swapped. Only the rim order is labelled here.
Each rim carries one flank from each nucleon. A second ring set on the rim meets the first
flank to flank, one to one, in one of four settings. Turned over, its order round the rim
reverses; its turnings, seen from outside, are carried with it unchanged (the other reading,
turnings reversed, is run as well). Rule 2 at a flank join: the two turn opposite ways."""
A = [("p", +1), ("n", +1), ("p", -1), ("n", -1)]
swapped = lambda r: [r[0]] + r[:0:-1]
def settings(first, second, turned, flip_turning):
    b = second[::-1] if turned else list(second)
    if turned and flip_turning: b = [(k, -s) for k, s in b]
    out = []
    for shift in range(4):
        pairs = [(first[i], b[(i + shift) % 4]) for i in range(4)]
        opposite = all(x[1] != y[1] for x, y in pairs)
        unlike = all(x[0] != y[0] for x, y in pairs)
        alike = all(x[0] == y[0] for x, y in pairs)
        if opposite: out.append("p on n" if unlike else "like on like" if alike else "mixed")
    return out
for hand, B in (("same sort", A), ("kinds swapped", swapped(A))):
    for turned in (False, True):
        for flip in ((False, True) if turned else (False,)):
            tag = "turned over" + (" (turnings reversed)" if flip else "") if turned else "not turned"
            print("%-12s %-32s settings with all four opposite: %s" % (hand, tag, settings(A, B, turned, flip) or "none"))
