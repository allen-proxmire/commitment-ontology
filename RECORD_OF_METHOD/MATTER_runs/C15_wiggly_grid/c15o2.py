# c15o with every difference one hop wide (c15o's cross term and mixed part were two hops wide, blind to strict alternation).
# S's cross term: the product of forward differences on a k-link, averaged over the two k-links at the place.
# M_i: taken at the centre of the (j,k) square: d_j d_k a_i = f_j f_k a_i; d_j a_k = f_j a_k averaged across the square along k; lengths averaged over the square's corners.
import numpy as np
L=32; g=np.arange(L)-L/2; x=np.meshgrid(g,g,g,indexing='ij'); eps=0.1
f=lambda u,i:np.roll(u,-1,i)-u; b=lambda u,i:u-np.roll(u,1,i); m=lambda u,i:(u+np.roll(u,-1,i))/2; mb=lambda u,i:(u+np.roll(u,1,i))/2
def six(a):
    out=[]
    for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
        out.append(b(f(a[j],i)/m(a[i],i),i)+b(f(a[i],j)/m(a[j],j),j)+mb(f(a[i],k)*f(a[j],k)/m(a[k],k)**2,k))
        sq=lambda u:m(m(u,j),k)
        out.append(f(f(a[i],j),k)-m(f(a[k],j),k)*m(f(a[i],k),j)/sq(a[k])-m(f(a[j],k),j)*m(f(a[i],j),k)/sq(a[j]))
    s=np.array(out)[:,4:-4,4:-4,4:-4]; return np.sqrt((s**2).mean(axis=(1,2,3))).max()
one=np.ones((L,L,L)); R0=200.0; r=R0+x[0]; th=np.pi/2+x[1]/R0
cen=np.array([3*L,2.5*L,-2*L]); d2=sum((x[i]-cen[i])**2 for i in range(3)); inv=(d2.mean()/d2)
rng=np.random.default_rng(3); par=(-1.0)**(x[0]+x[1]+x[2]); alt=(-1.0)**np.arange(L)
cases={
 "even grid":[one,one,one],
 "flat: a fan":[one,1+eps*x[0]/L,one],
 "flat: a ball's own lines, far from the centre":[one,r/R0,r*np.sin(th)/R0],
 "flat: turned inside out about a far point":[inv,inv,inv],
 "flat: each line relabelled alone, uneven hop to hop by 0.1":[one*(1+eps*rng.standard_normal(L))[:,None,None],one*(1+eps*rng.standard_normal(L))[None,:,None],one*(1+eps*rng.standard_normal(L))[None,None,:]],
 "flat: each line relabelled alone, strictly alternating by 0.1":[one*(1+eps*alt)[:,None,None],one*(1+eps*alt)[None,:,None],one*(1+eps*alt)[None,None,:]],
 "curved: a bowl":[1+eps*(x[0]**2+x[1]**2+x[2]**2)/L**2]*3,
 "curved: a ripple 16 hops long":[1+eps*np.sin(2*np.pi*x[0]/16)*np.sin(2*np.pi*x[1]/16)*np.sin(2*np.pi*x[2]/16)]*3,
 "curved: independent from place to place, 0.1, one number per place":[1+eps*rng.standard_normal((L,L,L))]*3,
 "curved: independent, 0.1, a number per place per line":[1+eps*rng.standard_normal((L,L,L)) for _ in range(3)],
 "curved: a chequer of 0.1 (alternating in every direction)":[1+eps*par]*3,
}
for nm,a in cases.items(): print(f"{nm}: largest of the six, rms {six(a):.1e}")
