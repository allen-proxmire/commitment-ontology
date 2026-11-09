import numpy as np
sx=np.array([[0,1],[1,0]]);sz=np.diag([1.,-1])
F=lambda a: np.cos(a)*np.eye(2)-1j*np.sin(a)*sx
Sp=lambda k: np.diag([np.exp(1j*k),1]); Sm=lambda k: np.diag([1,np.exp(-1j*k)])
for k in (0,np.pi):
    U=Sp(k)@F(0.3)@Sm(k)@F(-0.3)
    print(k, np.round(np.angle(np.linalg.eigvals(U)),4))
