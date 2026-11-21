# CO's neutrino term with three flavours, against IceCube's isotropic dimension-four limit.
# H(E) = U diag(m_i^2/2E + kap E m_i) U^dag + diag(V,0,0),  kap = r/(2 E_l),  E_l = hbar c / l   (eV units)
# SME comparison model (IceCube 2018): H = U diag(m_i^2/2E) U^dag + diag(V,0,0) + E c [[0,0,0],[0,0,1],[0,1,0]], c = 2.7e-28.
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq
r=0.5; hc=1.97327e-7; km=5.0677e9          # eV m ; eV^-1 per km
def U(t12=33.4,t23=49.0,t13=8.6,d=197.0):
    a,b,c,d=np.radians([t12,t23,t13,d]); s12,c12,s23,c23,s13,c13=np.sin(a),np.cos(a),np.sin(b),np.cos(b),np.sin(c),np.cos(c); e=np.exp(1j*d)
    return np.array([[c12*c13,s12*c13,s13/e],[-s12*c23-c12*s23*s13*e,c12*c23-s12*s23*s13*e,s23*c13],[s12*s23-c12*c23*s13*e,-c12*s23-s12*c23*s13*e,c23*c13]])
def masses(order,m_light=0.0):
    d21,d3=7.42e-5,2.51e-3
    if order=='NO': m1=m_light; return np.array([m1,np.sqrt(m1**2+d21),np.sqrt(m1**2+d3)])
    m3=m_light; m2=np.sqrt(m3**2+d3); return np.array([np.sqrt(m2**2-d21),m2,m3])
L=12742*km; V=7.63e-14*8.4*0.47     # through the centre; mean density along a diameter about 8.4 g/cc, Ye 0.47
def Pmumu(E,m,Um,kap=0.0,c=0.0):
    H=Um@np.diag(m**2/(2*E)+kap*E*m)@Um.conj().T+np.diag([V,0,0]).astype(complex)
    H[1,2]+=E*c; H[2,1]+=E*c
    return abs(expm(-1j*H*L)[1,1])**2
Um=U(); c0=2.7e-28
print("two-flavour desk value: |c| = r (m3-m2) sin2th23/(4 E_l)")
for order,ml,lab in (('NO',0.0,'normal, lightest 0'),('NO',0.03,'normal, lightest 0.03 eV'),('IO',0.0,'inverted, lightest 0')):
    m=masses(order,ml); cm=Um@np.diag(m)@Um.conj().T          # c_ab / kap
    cmt=cm[1,2]; dd=(cm[1,1]-cm[2,2]).real/2
    two=abs(m[2]-m[1])*np.sin(np.radians(98.0))/2
    El=r*abs(cmt.real)/(2*c0); l_lead=hc/El
    # full three-flavour match: l at which CO's extra disappearance equals the SME model's at c0, at several energies
    out=[]
    for E in (2e12,5e12,1e13,1.8e13):
        tgt=Pmumu(E,m,Um)-Pmumu(E,m,Um,c=np.sign(cmt.real)*c0)   # SME limit taken two-sided; sign matched to CO's term
        f=lambda lg: (Pmumu(E,m,Um)-Pmumu(E,m,Um,kap=r/(2*hc/10**lg)))-tgt
        try: out.append((E/1e12,10**brentq(f,np.log10(l_lead/1.6),np.log10(l_lead*1.6))))
        except ValueError: out.append((E/1e12,float('nan')))
    print(f"{lab}: masses {np.round(m,4)}; c_mutau/kap = {cmt.real:+.5f}{cmt.imag:+.5f}i (two-flavour {two:.5f}, ratio {abs(cmt.real)/two:.3f}); diagonal half-difference/kap = {dd:+.5f}")
    print(f"    leading order (|Re c_mutau| = c0): l < {l_lead:.3e} m; full match at E = "+", ".join(f"{e:g} TeV: {l:.3e}" for e,l in out))
