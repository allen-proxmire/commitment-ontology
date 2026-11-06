"""Check: cost of stretching a three-tile pattern under CO's own transit rule, vs a string.
(1) Ordinary transit (ratio hopping, speed c): the pattern renews once per round trip, T ~ 2L/c,
    so omega ~ pi c / L and m c^2 ~ pi hbar c / L  -- falls with separation (Compton/zero-point scaling).
(2) Engaged kinship: one held quantum of energy hbar c/a per grain a along the length: E = (L/a)(hbar c/a)
    = (hbar c / a^2) L -- linear, string tension sigma = hbar c / a^2.
Compare with the QCD string tension and find the grain a it implies."""
hbar_c=197.327e-3   # GeV fm
sigma_qcd=0.9       # GeV/fm  (~ (0.42 GeV)^2 / hbar c)
l_hop=1.1e-18/1e-15 # fm (top-quark hop, MATTER.md)
print("(1) ordinary transit: m c^2 ~ pi hbar c / L ; at L=1 fm:", round(3.1416*hbar_c,3),"GeV  (decreases with L: no confinement)")
print("(2) engaged kinship: sigma = hbar c / a^2")
print("    with a = hop length", l_hop, "fm: sigma =", "%.2e"%(hbar_c/l_hop**2), "GeV/fm  vs QCD", sigma_qcd)
a=(hbar_c/sigma_qcd)**0.5
print("    grain needed for QCD tension: a =", round(a,3), "fm  (a new length, not in the inventory)")
# the figure quoted in NUCLEUS.md: tile mass m_p/3
m_tile=0.938272/3; sigma_tile=m_tile**2/hbar_c
print("(3) grain = tile renewal length: m_tile = m_p/3 =",round(m_tile,4),"GeV; a =",round(hbar_c/m_tile,3),"fm; sigma = m_tile^2/hbar c =",round(sigma_tile,3),"GeV/fm vs QCD",sigma_qcd)
