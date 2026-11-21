import numpy as np, sys
sys.path.insert(0,'.')
src=open('c15g.py').read().split("kk=2*np.pi")[0]; exec(src)
four=[(1,0),(0,1)]; eight=four+[(1,1),(1,-1)]
for nm,offs in (("four",four),("eight",eight)):
    H,V,d,res,herm=build(0.15,offs)
    xi=np.arange(L); X,Y=np.meshgrid(xi,xi,indexing='ij')
    for k in (0.098,0.196,0.393,0.785):
        k0=2*np.pi*round(k*L/(2*np.pi))/L
        chi=np.sqrt(V)*np.exp(1j*k0*(X+d[...,0])); p=np.stack([chi,chi],-1).reshape(-1)/np.sqrt(2); p/=np.linalg.norm(p)
        Hp=H@p; E=np.vdot(p,Hp).real; print(nm,f"k={k0:.3f} E={E:.4f} residual={np.linalg.norm(Hp-E*p):.3e} res/k^2={np.linalg.norm(Hp-E*p)/k0**2:.3f} res/k={np.linalg.norm(Hp-E*p)/k0:.3f}",flush=True)
