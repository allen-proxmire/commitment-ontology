"""R1: the gap's history under the wave rule.

Not a lattice run. Closed-form bookkeeping of the floor against capacity.

Units: possibility in hbar. x = P_inf / P_max (floor as a fraction of capacity).
Places N scale as a^3 (a = scale factor). Births per place per time r_b = H.

Crest per place: c = s(a) * x * P_max * xi, with s the characteristic strain and
xi a random factor with tail Pr(xi > y) = min(1, y^-alpha). alpha = 3 is the
tail of a uniform-in-volume population of sources (amplitude ~ 1/distance).

Tip condition: c > Delta = (1 - x) P_max   <=>   xi > (1 - x) / (s x).

Case A (rule as written): free stock conserved, so x = x0 (a0/a)^3.
Case C (rescue): floor pinned, x = x0 for all a (new places born at the floor,
their content drawn from record).

s(a): primordial ripples redshifting as 1/a, plus a structure-made background
following the cosmic star-formation history (Madau & Dickinson 2014 form),
each with a free amplitude. Only shapes are claimed; H is normalised to today.
"""
import numpy as np, json

ALPHA = 3.0

def sfr(z):  # Madau & Dickinson 2014, arbitrary units
    return (1+z)**2.7 / (1 + ((1+z)/2.9)**5.6)

def strain(a, s_prim, s_struct):
    z = 1/a - 1
    return s_prim / a + s_struct * sfr(z) / sfr(0.0)

def H_over_nu(a, x, s):
    y = (1 - x) / (s * x)
    return np.minimum(1.0, y**(-ALPHA))

a = np.logspace(-3, 0, 400)          # from z = 999 to today
out = {}

# Case A: rule as written. Floor just under capacity at a0 = 1e-3.
x0, a0 = 0.999, 1e-3
xA = x0 * (a0 / a)**3
xA = np.clip(xA, 1e-300, 0.999999)
sA = strain(a, s_prim=1e-21, s_struct=1e-15)
HA = H_over_nu(a, xA, sA)
out["A_rule_as_written"] = {"a": a.tolist(), "H_over_nu": HA.tolist(),
                           "x_today": float(xA[-1]), "H_today_over_nu": float(HA[-1])}

# Case C: pinned floor. Same strain history. Choose x0 so the gap exceeds hbar
# but crests clear it sometimes: gap/P_max = 1 - x0.
xC = np.full_like(a, 0.9)
sC = strain(a, s_prim=2e-3, s_struct=5e-3)   # amplitudes relative to the gap scale; shapes only
HC = H_over_nu(a, xC, sC)
out["C_pinned_floor"] = {"a": a.tolist(), "H_over_nu": HC.tolist()}

# LCDM for shape comparison (H/H0)
Om, OL = 0.31, 0.69
HL = np.sqrt(Om * a**-3 + OL)
out["LCDM_H_over_H0"] = HL.tolist()

# Headline numbers
late = a > 0.5
slopeA = np.polyfit(np.log(a[late]), np.log(HA[late] + 1e-300), 1)[0]
out["A_late_slope_dlnH_dlna"] = float(slopeA)
json.dump(out, open("r1_result.json", "w"))

print("Case A (rule as written): x today =", f"{xA[-1]:.2e}",
      "| H today / nu =", f"{HA[-1]:.2e}",
      "| late slope dlnH/dlna =", f"{slopeA:.2f}  (LCDM late slope -> 0; matter era -1.5)")
print("Case C (pinned floor): H/nu at a=0.01, 0.1, 0.5, 1 =",
      [f"{v:.2e}" for v in np.interp([0.01, 0.1, 0.5, 1.0], a, HC)])

try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.loglog(a, HA / HA[-1], label="A: rule as written (free stock conserved)")
    ax.loglog(a, HC / HC[-1], label="C: pinned floor (rescue)")
    ax.loglog(a, HL / HL[-1], "k--", label="ΛCDM")
    ax.set_xlabel("scale factor a"); ax.set_ylabel("H / H(today)")
    ax.set_ylim(1e-2, 1e12); ax.legend(fontsize=8); ax.set_title("R1: expansion history under the wave rule")
    fig.tight_layout(); fig.savefig("r1_H_of_a.png", dpi=130)
except Exception as e:
    print("plot skipped:", e)
