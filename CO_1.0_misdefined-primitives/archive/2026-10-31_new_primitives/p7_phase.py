# P7 check: E_theta F(|a + b e^{i theta}|) = F(a) + F(b) for all a, b >= 0, with F(x) = x^p. Only p = 2 satisfies it.
import numpy as np
th = np.linspace(0, 2*np.pi, 200001)[:-1]
for p in [0.5, 1, 1.5, 2, 2.5, 3, 4]:
    worst = 0
    for a, b in [(1, 1), (1, 0.3), (2, 0.7), (0.4, 1.9)]:
        lhs = np.mean(np.abs(a + b*np.exp(1j*th))**p); rhs = a**p + b**p
        worst = max(worst, abs(lhs - rhs) / rhs)
    print(f"p = {p}: worst relative violation {worst:.2e}")
# three terms, independent phases, p = 2
rng = np.random.default_rng(0); c = np.array([0.7, 1.3, 0.4]); ph = rng.uniform(0, 2*np.pi, (400000, 3))
print("3 terms, p=2:", np.mean(np.abs((c*np.exp(1j*ph)).sum(1))**2), "vs", (c**2).sum())
