# Two massive patterns in 2D attract through their lattice-evolved fields; check Newton in 2D, action = reaction, causality.
# Displacements are differences from the no-field run (same spreading and wrap), positions by circular mean.
LX,LY=1200,800
exec(open('g14.py').read())
import sys
tha,thb=0.4,0.3; D=200; sig=60; T=700
phx=np.exp(2j*np.pi*x/Lx)
def cpos(q): return np.angle(np.sum(q*phx))*Lx/(2*np.pi)
def run(kappa):
    pa=pk_at(tha,0,0,sig,-D,0); pb=pk_at(thb,0,0,sig,+D,0)
    Pa=np.zeros((Lx,Ly)); Va=np.zeros((Lx,Ly)); Pb=np.zeros((Lx,Ly)); Vb=np.zeros((Lx,Ly)); xa=[];xb=[]
    for t in range(T+1):
        qa=np.sum(abs(pa)**2,0); qb=np.sum(abs(pb)**2,0); xa.append(cpos(qa)); xb.append(cpos(qb))
        if kappa:
            field_step(Pa,Va,tha*qa,kappa); field_step(Pb,Vb,thb*qb,kappa)
        Na,wa=flips(Pb); Nb,wb=flips(Pa)
        pa=step(pa,wa,tha*Na); pb=step(pb,wb,thb*Nb)
    return np.unwrap(np.array(xa)*2*np.pi/Lx)*Lx/(2*np.pi), np.unwrap(np.array(xb)*2*np.pi/Lx)*Lx/(2*np.pi)
kappa=1e-2
xa0,xb0=run(0); xa1,xb1=run(kappa); da=xa1-xa0; db=xb1-xb0
t=np.arange(T+1); r=2*D; arrive=r/c0
def pred_a(th_src):
    out=np.zeros(T+1); m=t>arrive; out[m]=c0**2*kappa*th_src/(2*np.pi*r)/np.sqrt(1-(r/(c0*t[m]))**2); return out
pa_d=np.cumsum(np.cumsum(pred_a(thb))); pb_d=-np.cumsum(np.cumsum(pred_a(tha)))
print(f"field front arrives at t = {arrive:.0f}")
for tt in [int(0.9*arrive),300,450,600,700]:
    print(f"t={tt}: dx_a {da[tt]:+.4f} (pred {pa_d[tt]:+.4f}), dx_b {db[tt]:+.4f} (pred {pb_d[tt]:+.4f}), (theta_a dx_a + theta_b dx_b)/(theta_a |dx_a|) = {(tha*da[tt]+thb*db[tt])/max(abs(tha*da[tt]),1e-12):+.3f}")
    sys.stdout.flush()
