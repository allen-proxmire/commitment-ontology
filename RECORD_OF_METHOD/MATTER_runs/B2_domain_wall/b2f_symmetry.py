import numpy as np,sys; sys.path.insert(0,'.')
exec(open('b2f_run.py').read().split('L_list=')[0])
rng=np.random.default_rng(3); L=16
half=[np.ones(3)+rng.normal(size=3) for _ in range(L)]
sym_shift=half+half                                   # n_{s+L}=n_s
sym_mirror=half+half[::-1]                            # n_{2L-1-s}=n_s (reflection through the walls)
sym_mirror2=[half[(L-1-s)%L] if s<L else None for s in range(2*L)]
for name,ns in [('half-ring shift copy',sym_shift),('mirror s->2L-1-s',sym_mirror)]:
    v=speeds(L,Pblock(ns,0.2)); print(f"{name:22s} v1={v[0]:.6f} v2={v[1]:.6f} diff={abs(v[0]-v[1]):.1e}")
# mirror s -> L-1-s on each half separately (fixes the walls)
m3=[half[L-1-s] for s in range(L)]; m3=half[:L//2]+half[:L//2][::-1]; ns=m3+m3[::-1]
v=speeds(L,Pblock(ns,0.2)); print(f"{'mirror about each wall':22s} v1={v[0]:.6f} v2={v[1]:.6f} diff={abs(v[0]-v[1]):.1e}")
# reflection through the middle of each half: s -> L-1-s (mod 2L); keeps theta(s), exchanges the walls
rng=np.random.default_rng(4); a=[np.ones(3)+rng.normal(size=3) for _ in range(L//2)]; b=[np.ones(3)+rng.normal(size=3) for _ in range(L//2)]
first=a+a[::-1]; second=b+b[::-1]                    # each half symmetric about its own middle
v=speeds(L,Pblock(first+second,0.2)); print(f"{'reflect s->L-1-s':22s} v1={v[0]:.6f} v2={v[1]:.6f} diff={abs(v[0]-v[1]):.1e}")
