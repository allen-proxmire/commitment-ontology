import os; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'staggered_walk_base.py')).read().split("for th in")[0])
def E(q,th,thm): return np.sort(np.abs(np.angle(np.linalg.eigvals(U(q,th,thm)))))[0]
th=0.5; u=np.array([1,0,0.]); w=np.array([1,1,1.])/np.sqrt(3)
for d in (u,w):
  for qq in [0.05,0.1,0.2]:
    h=1e-5
    v=lambda m:(E((qq+h)*d,th,m)-E((qq-h)*d,th,m))/(2*h)
    v0=v(0)
    for m in [1e-3,2e-3]:
        vm=v(m); E0=E(qq*d,th,0); expected=-(m**2)/(2*E0**2)*v0   # Lorentz: v=v0*E0^2/E^2 approx -> v0(1 - m^2/(2E0^2))
        print(f"dir {np.round(d,2)} q={qq} thm={m}: (v_m-v_0)/v_0={((vm-v0)/v0):.3e}  Lorentz-expected={expected/v0:.3e}  residual/thm={((vm-v0)/v0-expected/v0)/m:.2e}")
print("--- E(q,m)^2 - E(q,0)^2, per m^2")
for m in [1e-3,1e-2]:
    print(m,[f"{(E(q*u,th,m)**2-E(q*u,th,0)**2)/m**2:.8f}" for q in [0.01,0.05,0.1,0.2,0.4]])
