import numpy as np,sys,itertools; sys.path.insert(0,'.')
from i2 import Ak,Fb
w=5*np.pi/16; th=0.03
orders=list(itertools.permutations(range(3)))
def Us(k,o): a,b,c=o; return Ak(a,k[a],w)@Ak(b,k[b],w)@Ak(c,k[c],w)@Fb(th)@Ak(c,k[c],w)@Ak(b,k[b],w)@Ak(a,k[a],w)
rng=np.random.default_rng(0); e6=[]; e1=[]
for _ in range(20000):
    k=rng.uniform(-np.pi,np.pi,3); U6=np.eye(4)
    for o in orders: U6=Us(k,o)@U6
    e6+=list(np.angle(np.linalg.eigvals(U6))); e1+=list(np.abs(np.angle(np.linalg.eigvals(Us(k,orders[0])))))
e6=np.abs(np.array(e6)); e1=np.array(e1)
print("single step: min |E| =",e1.min(),"  max |E| =",e1.max(), " (bandwidth vs 2pi/6 =",2*np.pi/6,")")
print("six-step product: min |phase| =",e6.min()," min distance from pi =",(np.pi-e6).min())
h,_=np.histogram(e6,bins=24,range=(0,np.pi)); print("six-step phase histogram (0..pi, 24 bins):",h)
# cyclic three-order cycle xyz, yzx, zxy
cyc=[(0,1,2),(1,2,0),(2,0,1)]; e3=[]
for _ in range(20000):
    k=rng.uniform(-np.pi,np.pi,3); U3=np.eye(4)
    for o in cyc: U3=Us(k,o)@U3
    e3+=list(np.abs(np.angle(np.linalg.eigvals(U3))))
e3=np.array(e3); print("three-step cyclic product: min |phase| =",e3.min()," min distance from pi =",(np.pi-e3).min())
h,_=np.histogram(e3,bins=24,range=(0,np.pi)); print("histogram:",h)
