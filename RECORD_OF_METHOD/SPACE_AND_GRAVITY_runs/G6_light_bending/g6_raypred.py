# Plane-wave ray prediction on the lattice for G6's light packets: a_x = -(d omega/dx) * d2omega/dkx2 at kx = 0,
# with the local flips at x (Wilson flip from 2 cos w = c0 N/psi, mass flip theta N). Compare g6_final.out.
exec(open('g6.py').read())
def pred(th,k0y,g,lapse,stretch):
    def om(kx,xx):
        N=1-lapse*g*xx; ps=1+stretch*g*xx; w=np.arccos(c0*N/ps/2); return E(kx,k0y,th*N,w)
    d=1.0; dodx=(om(0,d)-om(0,-d))/(2*d); hk=1e-3; o2=(om(hk,0)-2*om(0,0)+om(-hk,0))/hk**2
    return -dodx*o2/(g*c0**2)
g=5e-5
for k0 in [0.05,0.1,0.15,0.3]:
    print(f"light k0y={k0}: ray prediction a/(g c0^2): clock {pred(0,k0,g,1,0):.4f}  clock+stretch {pred(0,k0,g,1,1):.4f}")
