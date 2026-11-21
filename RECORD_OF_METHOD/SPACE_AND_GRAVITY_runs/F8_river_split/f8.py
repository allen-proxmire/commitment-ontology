# How does a river split into births and flow through fixed places? Desk check of three candidate rules on five rivers.
# Flat slices, unit lapse, river b(x). K_ij = (d_i b_j + d_j b_i)/2.  Constraint: C = (div b)^2 - K_ij K_ij = 16 pi G rho + 2 Lambda c^2.
# Rule 1: births per place per time = div b.   Rule 2: births at the constraint's rate, sqrt(3C/2).   Rule 3: places ride with the stuff: births = div v of the stuff there.
import numpy as np
G=6.674e-11; c=2.998e8
def KC(b,x,h=1e-5):
    x=np.array(x,float); L=np.linalg.norm(x); d=np.zeros((3,3))
    for j in range(3):
        e=np.zeros(3); e[j]=h*L; d[:,j]=(b(x+e)-b(x-e))/(2*h*L)
    K=(d+d.T)/2; div=np.trace(K); return div, div**2-np.sum(K*K)
pt=np.array([0.3,-0.7,0.5])
# rivers, in units GM = 1 (and H = 1 where present)
pg=lambda x: -np.sqrt(2/np.linalg.norm(x))*x/np.linalg.norm(x)
hub=lambda x: 1.0*x
sds=lambda x: np.sqrt(2/np.linalg.norm(x)+np.linalg.norm(x)**2)*x/np.linalg.norm(x)
Rb=2.0; inside=lambda x: -np.sqrt(2/Rb**3)*x          # uniform body of radius Rb, mass 1: b = -sqrt(2 G m(r)/r)
for name,b,p,expect in (("mass in empty space (b = -sqrt(2GM/r))",pg,pt,"C = 0"),("uniform expansion (b = Hx)",hub,pt,"C = 6H^2 = 6"),
                        ("mass with Lambda (b^2 = 2GM/r + H^2 r^2)",sds,pt,"C = 6H^2 = 6"),("mass with Lambda, ten times nearer",sds,pt/10,"C = 6"),
                        ("inside a uniform body (constraint value only: a body held up needs a lapse that is not 1)",inside,pt,"C = 16 pi G rho = 12GM/R^3 = 1.5"),
                        ("a collapsing ball of dust, inside (b = -|H|x)",lambda x: -0.7*x,pt,"C = 6H^2 = 2.94, div b = 3H = -2.1")):
    div,C=KC(b,p); r=np.linalg.norm(p)
    print(f"{name}: div b = {div:+.4f}, C = {C:+.5f}  ({expect}); rule 2 rate sqrt(3C/2) = {np.sqrt(max(1.5*C,0)):.4f}")
r=np.linalg.norm(pt); print(f"   check, empty space: div b = -(3/2) sqrt(2GM/r^3) = {-1.5*np.sqrt(2/r**3):+.4f}")
# numbers
ME=5.972e24; RE=6.371e6; rho=ME/(4/3*np.pi*RE**3)
print(f"Earth's surface: river speed sqrt(2GM/R) = {np.sqrt(2*G*ME/RE)/1e3:.1f} km/s; rule 1 would remove places just above it at (3/2)sqrt(2GM/R^3) = {1.5*np.sqrt(2*G*ME/RE**3):.2e} per second")
print(f"inside the Earth (mean density {rho:.0f} kg/m^3): rules 1 and 2 give sqrt(24 pi G rho) = {np.sqrt(24*np.pi*G*rho):.2e} per second, with nothing moving; rule 2 has no sign")
H0=2.2e-18*np.sqrt(0.69)   # Lambda's part of today's rate
for nm,M in (("the Sun",1.989e30),("a galaxy of 1e12 Suns",1.989e42)):
    rx=(2*G*M/H0**2)**(1/3); print(f"{nm} in the expansion: flow through the places = sqrt(2GM/r + H^2 r^2) - Hr; equal parts at r = (2GM/H^2)^(1/3) = {rx:.2e} m = {rx/9.461e15:.0f} light-years = {rx/3.0857e22:.2e} Mpc")
x=10*2**(1/3); print(f"   far out the flow through the places falls as GM/(H r^2): at 10x that radius it is {(np.sqrt(2/x+x**2)-x)/np.sqrt(2/x):.3f} of the lone mass's river")
