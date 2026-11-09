"""L1: low-energy dispersion of the 3D walk (palindrome + Wilson; sequential for comparison)."""
import numpy as np, json
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
P=lambda j,k: Pp[j]*np.exp(1j*k)+Pm[j]*np.exp(-1j*k)
W=lambda k: sum(1-np.cos(kj) for kj in k)
def M(k,th,r):
    a=th+r*W(k); return np.cos(a)*np.eye(4)-1j*np.sin(a)*beta
def Upal(k,th,r): return P(0,k[0])@P(1,k[1])@P(2,k[2])@M(k,th,r)@P(2,k[2])@P(1,k[1])@P(0,k[0])
def Useq(k,th,r): return P(0,k[0])@P(1,k[1])@P(2,k[2])@M(k,th,r)
def qe(U): return np.sort(np.abs(np.angle(np.linalg.eigvals(U))))
dirs={'axis':np.array([1,0,0.]),'face':np.array([1,1,0.])/np.sqrt(2),'body':np.array([1,1,1.])/np.sqrt(3)}
ks=np.linspace(0.005,0.08,16)
def fit(Uf,n,th,r):
    E=np.array([qe(Uf(k*n,th,r))[0] for k in ks])
    X=np.vstack([ks**2,ks**4]).T; y=E**2-th**2
    (A,B),res,*_=np.linalg.lstsq(X,y,rcond=None)
    resid=np.max(np.abs(X@np.array([A,B])-y))/np.max(np.abs(y))
    return A,B,resid
r=0.3; out={'r':r,'palindrome':{},'sequential_split':{}}
print("pre-check r=0 th=0 speeds:",{d:round(np.sqrt(fit(Upal,n,0,0)[0]),6) for d,n in dirs.items()})
for d,n in dirs.items():
    A0,B0,res0=fit(Upal,n,0,r); row={'A0':A0,'c0':np.sqrt(A0),'bend_B0_over_A0sq':B0/A0**2,'resid0':res0,'s':{}}
    for th in (0.01,0.02,0.04):
        A,B,res=fit(Upal,n,th,r); row['s'][th]={'s':np.sqrt(A/A0)-1,'s_over_rth':(np.sqrt(A/A0)-1)/(r*th),'resid':res}
    out['palindrome'][d]=row
    sp=[]
    for k in (0.01,0.02,0.04,0.08):
        e=qe(Useq(k*n,0.0,r)); sp.append([k,e[0],e[1],e[2],e[3]])
    out['sequential_split'][d]=sp
for d,row in out['palindrome'].items():
    print(d,"c0=%.6f bend=%.4f"%(row['c0'],row['bend_B0_over_A0sq']),{th:(round(v['s'],6),round(v['s_over_rth'],4),'%.1e'%v['resid']) for th,v in row['s'].items()})
for d,sp in out['sequential_split'].items():
    print("seq",d,[(k,round(e1,6),round(e2,6),'split=%.2e'%(abs(e2-e1)) ) for k,e1,e2,e3,e4 in sp])
json.dump(out,open('l1_result.json','w'),indent=1,default=float)
