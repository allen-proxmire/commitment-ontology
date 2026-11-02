"""R2: H(a) = nu * (A(a)/A_*)^3 against the measured expansion history.

Under born-of-record the floor is pinned and H = nu * Pr(xi > Delta/(A P_max)).
With a 1/distance source population Pr(xi > y) = y^-3, so H ∝ A(a)^3, A the
characteristic wave amplitude per place at epoch a.

Two things are computed.
1. The A(a) the measured expansion history REQUIRES:
       A_req(a) = A_today * (H_LCDM(a)/H0)^(1/3),  H_LCDM = H0 sqrt(Or a^-4 + Om a^-3 + OL).
2. Candidate wave histories, from real inputs, on the same axes:
   - primordial, rms over all modes: dominated by modes at horizon entry,
     h_entry = sqrt(r A_s), r <= 0.03, A_s = 2.1e-9 -> ~8e-6, constant in a;
   - primordial, a single sub-horizon mode: decays as 1/a after entry;
   - astrophysical (SMBHB) background: today A ~ 2.4e-15 (PTA, at 1/yr);
     history taken ∝ cumulative star formation (Madau & Dickinson 2014), redshifted 1/a.
A is dimensionless strain. The ratio H/H0 depends only on the SHAPE of A(a).
"""
import numpy as np, json

H0 = 1.0
Or, Om, OL = 9.0e-5, 0.31, 0.69
a = np.logspace(-9, 0, 600)    # from BBN-ish (a~1e-9) to today
H_lcdm = np.sqrt(Or * a**-4 + Om * a**-3 + OL)

A_today = 2.4e-15
A_req = A_today * H_lcdm**(1/3)

# candidates
A_prim_rms = np.full_like(a, np.sqrt(0.03 * 2.1e-9))
A_prim_mode = np.sqrt(0.03 * 2.1e-9) * (1e-3 / a); A_prim_mode = np.minimum(A_prim_mode, np.sqrt(0.03*2.1e-9))  # a mode entering at a=1e-3

def sfr(z): return (1+z)**2.7 / (1 + ((1+z)/2.9)**5.6)
z = 1/a - 1
# cumulative SFR up to epoch a (in a), redshifted by 1/a from then to now is folded crudely: amplitude at epoch ∝ cum(a)
cum = np.cumsum(sfr(z) * np.gradient(a))
A_astro = A_today * cum / cum[-1]

# required ratios at landmarks
def at(arr, aa): return float(np.interp(aa, a, arr))
landmarks = {"BBN a~1e-9": 1e-9, "recombination a~9e-4": 9.1e-4, "z=2": 1/3, "z=1": 0.5, "z=0.5": 1/1.5}
req = {k: at(A_req, v)/A_today for k, v in landmarks.items()}
H_from = {
  "prim_rms": (A_prim_rms/A_prim_rms[-1])**3,
  "prim_mode": (A_prim_mode/A_prim_mode[-1])**3,
  "astro": (A_astro/A_astro[-1])**3,
}
out = {"A_req_over_A_today": req,
       "H_over_H0_lcdm_at_landmarks": {k: at(H_lcdm, v) for k, v in landmarks.items()},
       "H_over_Htoday_from_candidates_at_landmarks": {n: {k: at(v, aa) for k, aa in landmarks.items()} for n, v in H_from.items()}}
json.dump(out, open("r2_result.json", "w"), indent=1)
print("Required A(a)/A_today for H ∝ A^3 to match LCDM:")
for k, v in req.items(): print(f"  {k:24s} {v:10.3g}")
print("H/H_today implied by each candidate A(a):")
for n, v in H_from.items():
    print(" ", n, {k: f"{at(v, aa):.3g}" for k, aa in landmarks.items()})
print("LCDM H/H0:", {k: f"{at(H_lcdm, v):.3g}" for k, v in landmarks.items()})

try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].loglog(a, A_req, "k--", label="A required (from measured H)")
    ax[0].loglog(a, A_prim_rms, label="primordial, rms (r=0.03)")
    ax[0].loglog(a, A_prim_mode, label="primordial, one mode, 1/a")
    ax[0].loglog(a, A_astro, label="astrophysical (SMBHB), cumulative SFR")
    ax[0].set_xlabel("a"); ax[0].set_ylabel("A (strain)"); ax[0].legend(fontsize=7); ax[0].set_title("Wave amplitude per place")
    ax[1].loglog(a, H_lcdm, "k--", label="ΛCDM")
    for n, v in H_from.items(): ax[1].loglog(a, v, label=f"H ∝ A³: {n}")
    ax[1].set_xlabel("a"); ax[1].set_ylabel("H / H(today)"); ax[1].set_ylim(1e-3, 1e20); ax[1].legend(fontsize=7); ax[1].set_title("Expansion history")
    fig.tight_layout(); fig.savefig("r2_H_vs_A3.png", dpi=130)
except Exception as e:
    print("plot skipped:", e)
