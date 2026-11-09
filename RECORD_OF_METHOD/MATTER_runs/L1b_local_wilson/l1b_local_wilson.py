"""L1b: strictly local Wilson walk A_j = S+ F(w) S- F(-w); palindrome A_x A_y A_z F(theta) A_z A_y A_x."""
import numpy as np, itertools, json
I2=np.eye(2); Z=np.zeros((2,2))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
alpha=[np.block([[Z,si],[si,Z]]) for si in s]; beta=np.block([[I2,Z],[Z,-I2]])
Pp=[(np.eye(4)+a)/2 for a in alpha]; Pm=[(np.eye(4)-a)/2 for a in alpha]
F=lambda a: np.cos(a)*np.eye(4)-1j*np.sin(a)*beta
Sp=lambda j,k: Pp[j]*np.exp(1j*k)+Pm[j]; Sm=lambda j,k: Pp[j]+Pm[j]*np.exp(-1j*k)
A=lambda j,k,w: Sp(j,k)@F(w)@Sm(j,k)@F(-w)
def U(k,th,w): return A(0,k[0],w)@A(1,k[1],w)@A(2,k[2],w)@F(th)@A(2,k[2],w)@A(1,k[1],w)@A(0,k[0],w)
def qe(M): return np.sort(np.abs(np.angle(np.linalg.eigvals(M))))
def gapless(w,n=40,tol=0.08):
    ks=np.linspace(-np.pi,np.pi,n,endpoint=False); z=[];p=[]
    for k in itertools.product(ks,repeat=3):
        e=qe(U(k,0,w))
        if e[0]<tol: z.append(k)
        if e[-1]>np.pi-tol: p.append(k)
    def clusters(H):
        if not H: return []
        H=np.array(H); lab=-np.ones(len(H),int); c=0
        for i in range(len(H)):
            if lab[i]<0:
                stack=[i]; lab[i]=c
                while stack:
                    a=stack.pop(); d=np.abs(((H-H[a])+np.pi)%(2*np.pi)-np.pi).max(1)
                    for b in np.where((d<0.2)&(lab<0))[0]: lab[b]=c; stack.append(b)
                c+=1
        return [np.round(H[lab==i].mean(0)/np.pi,2).tolist() for i in range(c)]
    return clusters(z),clusters(p)
dirs={'axis':np.array([1,0,0.]),'face':np.array([1,1,0.])/np.sqrt(2),'body':np.array([1,1,1.])/np.sqrt(3)}
ks=np.linspace(0.005,0.08,16)
def fit(n,th,w):
    E=np.array([qe(U(k*n,th,w))[0] for k in ks]); X=np.vstack([ks**2,ks**4]).T; y=E**2-th**2
    (a,b),*_=np.linalg.lstsq(X,y,rcond=None); return a,b,np.max(np.abs(X@np.array([a,b])-y))/np.max(np.abs(y))
print("pre-check w=0 speeds:",{d:round(np.sqrt(fit(n,0,0)[0]),6) for d,n in dirs.items()})
out={}
for w in (0.2,0.3,np.pi/10):
    z,p=gapless(w); row={'gapless_0':z,'gapless_pi':p,'dirs':{}}
    print("w=%.4f gapless(0-sector)=%s gapless(pi-sector)=%s"%(w,z if len(z)<12 else len(z),p if len(p)<12 else len(p)))
    for d,n in dirs.items():
        a0,b0,r0=fit(n,0,w); sv={}
        for th in (0.01,0.02,0.04):
            a,b,r=fit(n,th,w); sv[th]=(np.sqrt(a/a0)-1,(np.sqrt(a/a0)-1)/th,r)
        ev=np.sort(np.angle(np.linalg.eigvals(U(0.08*n,0,w)))); split=(ev[3]-ev[2])/0.08**2
        row['dirs'][d]={'c0':np.sqrt(a0),'bend':b0/a0**2,'s':sv,'split_over_k2':split,'resid0':r0}
        print("  %s c0=%.5f bend=%.4f split/k2=%.1e s/theta=%s resid=%.0e"%(d,np.sqrt(a0),b0/a0**2,split,[round(v[1],4) for v in sv.values()],max(v[2] for v in sv.values())))
    out[str(round(w,4))]=row
json.dump(out,open('l1b_result.json','w'),indent=1,default=float)
