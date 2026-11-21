# A box of trapped massless pattern on the 1D flow step, in a uniform field (N, psi^2): does it tick and weigh like mass?
# H = 1/2{D,K} + sigma_z m(x) N, D = N/psi^2 (P7f restated). Inside the box m = 0; outside m = M (the walls).
# A rigid box keeps its proper width: coordinate width w = w0/psi^2. Prediction: E = N * E0, the same factor as a rest mass m N.
import numpy as np,sys; sys.path.insert(0,'../../SPACE_AND_GRAVITY_runs/F1_flow_gravity')
from flow1d import build
r=0.5; L=900; M=1.0
def levels(w,N0,psi2,M=M,n=3):
    x=np.arange(L); inside=(x>=L//2-w//2)&(x<L//2-w//2+w); mN=np.where(inside,0.0,M)*N0
    H=build(L,1.0,r,mN,np.full(L,N0/psi2)).toarray(); e=np.linalg.eigvalsh(H); return np.sort(e[e>1e-9])[:n]
w0=240; E0=levels(w0,1.0,1.0)
print(f"box of proper width {w0}, no field: lowest levels {np.round(E0,6)} (continuum, hard walls: (n+1/2) pi/w = {np.round((np.arange(3)+0.5)*np.pi/w0,6)})")
print("field           N     psi^2   coord width   E_1/N        ratio to no-field   rest mass m=0.01: E/(mN)")
for psi2 in (1.0,1.2,1.5,2.0):
    N0=2-psi2 if psi2<2 else 0.25     # N = 1 - Phi, psi^2 = 1 + Phi (and one stronger case)
    w=int(round(w0/psi2)); E=levels(w,N0,psi2)
    xm=np.arange(L); Hm=build(L,1.0,r,np.full(L,0.01*N0),np.full(L,N0/psi2)).toarray(); em=np.linalg.eigvalsh(Hm); em=em[em>0].min()
    print(f"Phi={psi2-1:.1f}       {N0:.2f}  {psi2:.1f}     {w:4d}          {E[0]/N0:.6f}     {E[0]/N0/E0[0]:.5f}             {em/(0.01*N0):.5f}")
# weight: a small change of height in a weak field changes the box's energy by -g E0 dx, as for a mass
g=1e-3; Ea=levels(w0,1.0,1.0)[0]; Eb=levels(int(round(w0/(1+g*50))),1-g*50,1+g*50)[0]
print(f"weak field, 50 places higher (g = {g}): dE/E0 = {(Eb-Ea)/Ea:+.5f}; a rest mass gives -g*50 = {-g*50:+.5f}")
# what the trapped pattern's own mass is: zero. The box's energy is all travel.
print(f"box energy {E0[0]:.5f} against the pattern's own mass 0; a free massive pattern with the same tick rate has m = {E0[0]:.5f}")
