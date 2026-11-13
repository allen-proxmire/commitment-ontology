# Exact lattice prediction for slow fall: a = -(dE0/dz) * E''(k=0), with E0(theta N) the rest energy
exec(open('g5_free_fall.py').read().split('print("drift check')[0])
_packet=packet
def pred(th,g):
    d=1e-5; dE0=(E(0,th*(1+d))-E(0,th*(1-d)))/(2*d)   # dE0/dN at N=1
    hk=1e-3; Epp=(E(hk,th)-2*E(0,th)+E(hk,th))/hk**2 if False else (E(2*hk,th)-2*E(hk,th)+E(0,th))/hk**2
    return g*dE0*Epp
for th in [0.1,0.2,0.4]:
    for wd in [60,150,300]:
        packet=lambda t,width=wd: _packet(t,width)
        acc,v0,dx=run(th,2e-6)
        print(f"theta={th} width={wd}: a/(g c0^2)={acc/(2e-6*c0**2):.4f}  a/lattice_pred={acc/pred(th,2e-6):.4f}")
